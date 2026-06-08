#!/usr/bin/env python3
"""Acquire transcripts for the @ShinzenVideos YouTube channel.

The script is intentionally acquisition-only: it enumerates public playlists,
deduplicates by video ID against the existing raw YouTube transcript corpus,
fetches caption transcripts when available, falls back to local STT when
requested and needed, and writes channel/playlist manifests. It does not make
selection or source-page ingestion decisions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import date
import json
from pathlib import Path
import re
import sys
from typing import Any

from scrape_retreat_stream_transcripts import (
    ROOT,
    choose_caption,
    clean_caption_text,
    download_audio,
    duration_label,
    escape_table,
    fetch_url,
    find_existing_transcripts,
    format_transcript,
    import_ytdlp,
    is_within,
    markdown_filename,
    parse_caption,
    read_transcript_metadata,
    sanitize_title,
    transcribe_with_faster_whisper,
)


CHANNEL_NAME = "ShinzenVideos"
CHANNEL_URL = "https://www.youtube.com/@ShinzenVideos"
PLAYLISTS_URL = f"{CHANNEL_URL}/playlists"
VIDEOS_URL = f"{CHANNEL_URL}/videos"
DEFAULT_SCRATCH = Path(r"C:\tmp\shinzenvideos_channel_scrape")
DEFAULT_PYDEPS = DEFAULT_SCRATCH / "pydeps"
FALLBACK_PYDEPS = Path(r"C:\tmp\shinzen_retreat_stream_scrape\pydeps")
DEFAULT_RAW_DIR = ROOT / "raw" / "Shinzen Sources" / "yt transcripts" / "ShinzenVideos"
YT_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
PLAYLIST_ID_RE = re.compile(r"(?:list=|^)([A-Za-z0-9_-]{12,})")


@dataclass
class PlaylistRecord:
    playlist_id: str
    title: str
    url: str
    owner: str = ""
    description: str = ""
    reported_count: str = ""
    slug: str = ""
    entries: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Membership:
    playlist_id: str
    playlist_title: str
    position: int | str


@dataclass
class VideoRecord:
    video_id: str
    title: str
    duration: str = "unknown"
    duration_seconds: int | None = None
    uploader: str = ""
    channel: str = ""
    availability: str = ""
    upload_date: str = "unknown"
    memberships: list[Membership] = field(default_factory=list)
    ungrouped: bool = False
    raw_path: str = ""
    status: str = "pending"
    quality: str = ""
    source: str = ""
    notes: str = ""


def resolve_pydeps(path: Path) -> Path:
    if path.exists():
        return path
    if FALLBACK_PYDEPS.exists():
        return FALLBACK_PYDEPS
    return path


def playlist_id_from_entry(entry: dict[str, Any]) -> str:
    for key in ("id", "url", "webpage_url"):
        value = str(entry.get(key) or "")
        if not value:
            continue
        match = PLAYLIST_ID_RE.search(value)
        if match:
            return match.group(1)
    return ""


def video_id_from_entry(entry: dict[str, Any]) -> str:
    candidate = str(entry.get("id") or "")
    if YT_ID_RE.match(candidate):
        return candidate
    candidate = str(entry.get("url") or "")
    if YT_ID_RE.match(candidate):
        return candidate
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", candidate)
    if match:
        return match.group(1)
    return ""


def playlist_url(playlist_id: str) -> str:
    return f"https://www.youtube.com/playlist?list={playlist_id}"


def slugify_playlist(title: str, playlist_id: str) -> str:
    base = sanitize_title(title, playlist_id).lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    base = base[:80].strip("-") or playlist_id
    return f"{base}-{playlist_id}"


def iso_upload_date(value: Any) -> str:
    text = str(value or "")
    if len(text) == 8 and text.isdigit():
        return f"{text[:4]}-{text[4:6]}-{text[6:]}"
    return "unknown"


def seconds_or_none(value: Any) -> int | None:
    if isinstance(value, (int, float)) and value >= 0:
        return int(value)
    return None


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def membership_label(memberships: list[Membership]) -> str:
    if not memberships:
        return "ungrouped"
    return "; ".join(
        f"{item.playlist_title} ({item.playlist_id}, position {item.position})"
        for item in memberships
    )


def primary_playlist(record: VideoRecord) -> str:
    if record.memberships:
        return record.memberships[0].playlist_title
    return "ungrouped"


def uploader_label(record: VideoRecord) -> str:
    return record.channel or record.uploader or "unknown"


def update_video_from_entry(record: VideoRecord, entry: dict[str, Any]) -> None:
    if entry.get("title"):
        record.title = str(entry["title"])
    seconds = seconds_or_none(entry.get("duration"))
    if seconds is not None:
        record.duration_seconds = seconds
        record.duration = duration_label(seconds)
    if entry.get("uploader"):
        record.uploader = str(entry["uploader"])
    if entry.get("channel"):
        record.channel = str(entry["channel"])
    if entry.get("availability"):
        record.availability = str(entry["availability"])
    upload_date = iso_upload_date(entry.get("upload_date"))
    if upload_date != "unknown":
        record.upload_date = upload_date


def add_or_update_video(
    videos: dict[str, VideoRecord],
    entry: dict[str, Any],
    membership: Membership | None,
    ungrouped: bool = False,
) -> None:
    video_id = video_id_from_entry(entry)
    if not video_id:
        return
    title = str(entry.get("title") or video_id)
    record = videos.get(video_id)
    if record is None:
        record = VideoRecord(video_id=video_id, title=title)
        videos[video_id] = record
    update_video_from_entry(record, entry)
    if membership and not any(
        existing.playlist_id == membership.playlist_id for existing in record.memberships
    ):
        record.memberships.append(membership)
    if ungrouped and not record.memberships:
        record.ungrouped = True


def ydl_flat_opts() -> dict[str, Any]:
    return {
        "quiet": True,
        "skip_download": True,
        "extract_flat": "in_playlist",
        "ignoreerrors": True,
        "no_warnings": True,
    }


def ydl_info_opts() -> dict[str, Any]:
    return {
        "quiet": True,
        "skip_download": True,
        "ignoreerrors": True,
        "no_warnings": True,
    }


def enumerate_playlists(yt_dlp: Any, scratch: Path) -> list[PlaylistRecord]:
    print(f"Enumerating playlists: {PLAYLISTS_URL}")
    with yt_dlp.YoutubeDL(ydl_flat_opts()) as ydl:
        info = ydl.extract_info(PLAYLISTS_URL, download=False)
    scratch.mkdir(parents=True, exist_ok=True)
    (scratch / "playlist_enumeration.json").write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
        encoding="utf-8",
        newline="\n",
    )

    records: list[PlaylistRecord] = []
    seen: set[str] = set()
    for entry in info.get("entries") or []:
        if not entry:
            continue
        playlist_id = playlist_id_from_entry(entry)
        if not playlist_id or playlist_id in seen:
            continue
        title = str(entry.get("title") or playlist_id)
        url = str(entry.get("webpage_url") or entry.get("url") or playlist_url(playlist_id))
        if "youtube.com" not in url:
            url = playlist_url(playlist_id)
        record = PlaylistRecord(
            playlist_id=playlist_id,
            title=title,
            url=url,
            owner=str(entry.get("uploader") or entry.get("channel") or ""),
            description=str(entry.get("description") or ""),
            reported_count=str(entry.get("playlist_count") or entry.get("n_entries") or ""),
            slug=slugify_playlist(title, playlist_id),
        )
        records.append(record)
        seen.add(playlist_id)
    return records


def enumerate_playlist_entries(yt_dlp: Any, playlist: PlaylistRecord, scratch: Path) -> None:
    print(f"Enumerating playlist {playlist.playlist_id}: {playlist.title}")
    with yt_dlp.YoutubeDL(ydl_flat_opts()) as ydl:
        info = ydl.extract_info(playlist.url, download=False)
    playlist.owner = str(info.get("uploader") or info.get("channel") or playlist.owner or "")
    playlist.description = str(info.get("description") or playlist.description or "")
    playlist.reported_count = str(
        info.get("playlist_count") or info.get("n_entries") or playlist.reported_count or ""
    )
    playlist.entries = [entry for entry in (info.get("entries") or []) if entry]
    out_dir = scratch / "video_metadata"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"playlist_{playlist.playlist_id}.json").write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
        encoding="utf-8",
        newline="\n",
    )


def enumerate_channel_videos(yt_dlp: Any, scratch: Path) -> list[dict[str, Any]]:
    print(f"Enumerating channel videos cross-check: {VIDEOS_URL}")
    with yt_dlp.YoutubeDL(ydl_flat_opts()) as ydl:
        info = ydl.extract_info(VIDEOS_URL, download=False)
    (scratch / "channel_videos_enumeration.json").write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
        encoding="utf-8",
        newline="\n",
    )
    return [entry for entry in (info.get("entries") or []) if entry]


def write_markdown_transcript(
    raw_dir: Path,
    scrape_date: str,
    record: VideoRecord,
    source: str,
    quality: str,
    notes: str,
    segments: list[tuple[float, str]],
) -> tuple[Path, int]:
    target = markdown_filename(raw_dir / "videos", record.title, record.video_id)
    transcript = format_transcript(segments)
    body = "\n".join(
        [
            f"# {record.title}",
            "",
            f"- **Video ID:** {record.video_id}",
            f"- **URL:** https://www.youtube.com/watch?v={record.video_id}",
            f"- **Channel:** {CHANNEL_NAME}",
            f"- **Channel URL:** {CHANNEL_URL}",
            f"- **Primary playlist:** {primary_playlist(record)}",
            f"- **Playlist memberships:** {membership_label(record.memberships)}",
            f"- **Uploader/channel reported by YouTube:** {uploader_label(record)}",
            f"- **Upload date:** {record.upload_date}",
            f"- **Source:** {source}",
            f"- **Length:** {record.duration}",
            f"- **Scrape date:** {scrape_date}",
            f"- **Transcript quality:** {quality}",
            f"- **Notes:** {notes}",
            "",
            "---",
            "",
            "## Transcript",
            "",
            transcript,
            "",
        ]
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8", newline="\n")
    return target, len(segments)


def apply_existing_transcript(
    record: VideoRecord,
    existing_path: Path,
    raw_dir: Path,
) -> None:
    metadata = read_transcript_metadata(existing_path)
    record.raw_path = relative(existing_path)
    record.source = metadata.get("Source", "existing corpus")
    record.quality = metadata.get("Transcript quality", "existing")
    if is_within(existing_path, raw_dir):
        record.status = "written"
        record.notes = (
            "Transcript is already present in the ShinzenVideos raw output; "
            "no duplicate was written on rerun."
        )
    else:
        record.status = "existing"
        record.notes = (
            "Video ID already has a local canonical transcript outside the "
            "ShinzenVideos raw output."
        )


def acquire_video(
    yt_dlp: Any,
    pydeps: Path,
    scratch: Path,
    raw_dir: Path,
    scrape_date: str,
    record: VideoRecord,
    run_stt: bool,
    stt_model: str,
) -> None:
    video_url = f"https://www.youtube.com/watch?v={record.video_id}"
    print(f"Inspecting captions: {record.video_id} {record.title}")
    with yt_dlp.YoutubeDL(ydl_info_opts()) as ydl:
        info = ydl.extract_info(video_url, download=False)
    if not info:
        record.status = "metadata_failed"
        record.quality = "D"
        record.notes = "yt-dlp returned no metadata."
        return

    update_video_from_entry(record, info)
    info_path = scratch / "video_metadata" / f"{record.video_id}.json"
    info_path.parent.mkdir(parents=True, exist_ok=True)
    info_path.write_text(
        json.dumps(info, indent=2, ensure_ascii=False),
        encoding="utf-8",
        newline="\n",
    )

    choice = choose_caption(info)
    if choice is not None:
        try:
            caption_text = fetch_url(choice.url)
            segments = parse_caption(choice, caption_text)
            target, segment_count = write_markdown_transcript(
                raw_dir,
                scrape_date,
                record,
                choice.source,
                choice.quality,
                (
                    f"Caption track `{choice.note}`. Transcript is usable for "
                    "routing and selection; exact wording, names, technical "
                    "terms, and quiet practice segments require spot checks "
                    "before source-page citation."
                ),
                segments,
            )
            record.status = "written"
            record.quality = choice.quality
            record.source = choice.source
            record.raw_path = relative(target)
            record.notes = f"Caption track {choice.note}; recovered {segment_count} caption segment(s)."
            return
        except Exception as exc:  # noqa: BLE001 - external caption fetch can fail broadly.
            if not run_stt:
                record.status = "caption_failed"
                record.quality = choice.quality
                record.source = choice.source
                record.notes = f"{choice.note}; {type(exc).__name__}: {exc}"
                return
            record.notes = f"Caption fetch failed ({choice.note}; {type(exc).__name__}: {exc}); trying local STT."

    if not run_stt:
        record.status = "stt_needed"
        record.quality = "C pending"
        record.notes = "No English caption or auto-caption track found. Local STT fallback required."
        return

    try:
        audio_path = download_audio(yt_dlp, scratch, record.video_id, video_url)
        segments = transcribe_with_faster_whisper(pydeps, scratch, audio_path, stt_model)
        if not segments:
            record.status = "no_transcript"
            record.quality = "D"
            record.source = f"faster-whisper ({stt_model}, CPU int8, VAD)"
            record.raw_path = ""
            record.notes = (
                "Local STT recovered no speech segments; likely silent, "
                "music-only, or otherwise no usable transcript. No raw "
                "transcript file was written."
            )
            return
        target, segment_count = write_markdown_transcript(
            raw_dir,
            scrape_date,
            record,
            f"faster-whisper ({stt_model}, CPU int8, VAD)",
            "C",
            (
                "Local STT fallback because no usable English YouTube caption "
                "or auto-caption track was available, or caption fetch failed. "
                "Exact wording, Buddhist vocabulary, names, and speaker "
                "attribution require source-page spot checks."
            ),
            segments,
        )
    except Exception as exc:  # noqa: BLE001 - audio/STT can fail in many ways.
        record.status = "stt_failed"
        record.quality = "D"
        record.source = f"faster-whisper ({stt_model})"
        record.notes = f"{record.notes} {type(exc).__name__}: {exc}".strip()
        return

    record.status = "written"
    record.quality = "C"
    record.source = f"faster-whisper ({stt_model}, CPU int8, VAD)"
    record.raw_path = relative(target)
    record.notes = f"No usable caption track; local STT recovered {segment_count} segment(s)."


def write_channel_manifest(
    raw_dir: Path,
    scrape_date: str,
    playlists: list[PlaylistRecord],
    videos: dict[str, VideoRecord],
    notes: list[str],
) -> None:
    status_counts = count_by(videos.values(), "status")
    quality_counts = count_by(videos.values(), "quality")
    source_counts = count_by(videos.values(), "source")
    unique_ids = len(videos)
    playlist_entries = sum(len(playlist.entries) for playlist in playlists)
    grouped_ids = {record.video_id for record in videos.values() if record.memberships}
    ungrouped = [record for record in videos.values() if record.video_id not in grouped_ids]
    duplicate_memberships = playlist_entries - len(grouped_ids)
    existing = status_counts.get("existing", 0)
    written = status_counts.get("written", 0)

    lines = [
        "# ShinzenVideos Channel Transcript Acquisition Manifest",
        "",
        f"**Channel:** {CHANNEL_URL}",
        f"**Playlist surface:** {PLAYLISTS_URL}",
        f"**Videos surface cross-check:** {VIDEOS_URL}",
        f"**Scrape date:** {scrape_date}",
        f"**Playlists enumerated:** {len(playlists)}",
        f"**Playlist video rows:** {playlist_entries}",
        f"**Unique video IDs:** {unique_ids}",
        f"**Duplicate playlist memberships:** {max(0, duplicate_memberships)}",
        f"**Ungrouped channel videos:** {len(ungrouped)}",
        "",
        "## Acquisition Status",
        "",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- **{status}**: {count}")
    if not status_counts:
        lines.append("- No videos enumerated.")

    lines.extend(["", "## Source Breakdown", ""])
    if source_counts:
        for source, count in sorted(source_counts.items()):
            lines.append(f"- **{source}**: {count}")
    else:
        lines.append("- No transcript sources fetched.")

    lines.extend(["", "## Quality Breakdown", ""])
    if quality_counts:
        for quality, count in sorted(quality_counts.items()):
            lines.append(f"- **{quality}**: {count}")
    else:
        lines.append("- No quality tiers assigned.")

    lines.extend(["", "## Notes", ""])
    generated_notes = list(notes)
    if existing:
        generated_notes.append(
            f"Deduplication found {existing} already-covered video ID(s); no duplicate transcript was written for those IDs."
        )
    if written:
        generated_notes.append(
            f"Acquisition has {written} video ID(s) with transcript files available in the canonical raw corpus, including rerun-detected ShinzenVideos files."
        )
    if status_counts.get("stt_failed") or status_counts.get("metadata_failed"):
        generated_notes.append(
            "One or more videos remain without usable transcripts and are quality D in the manifest."
        )
    if generated_notes:
        lines.extend(f"- {note}" for note in generated_notes)
    else:
        lines.append("- No additional notes.")

    lines.extend(
        [
            "",
            "## Playlists",
            "",
            "| # | Playlist ID | Title | Reported videos | Enumerated rows | Owner | URL |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for index, playlist in enumerate(playlists, start=1):
        lines.append(
            "| {index} | `{pid}` | {title} | {reported} | {rows} | {owner} | {url} |".format(
                index=index,
                pid=playlist.playlist_id,
                title=escape_table(playlist.title),
                reported=playlist.reported_count or "",
                rows=len(playlist.entries),
                owner=escape_table(playlist.owner),
                url=playlist.url,
            )
        )

    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "_CHANNEL_MANIFEST.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_video_index(raw_dir: Path, scrape_date: str, videos: dict[str, VideoRecord]) -> None:
    lines = [
        "# ShinzenVideos Video Index",
        "",
        f"**Channel:** {CHANNEL_URL}",
        f"**Scrape date:** {scrape_date}",
        f"**Unique video IDs:** {len(videos)}",
        "",
        "This index is an acquisition artifact, not a selection report. Playlist",
        "categories preserve YouTube organization only; they are not treated as",
        "Shinzen's own teaching taxonomy.",
        "",
        "| Video ID | Title | Length | Status | Quality | Source | Primary playlist | Playlist memberships | Upload date | Uploader/channel | Raw path | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in sorted(videos.values(), key=sort_video_record):
        lines.append(
            "| `{vid}` | {title} | {duration} | {status} | {quality} | {source} | {primary} | {memberships} | {upload_date} | {uploader} | {raw_path} | {notes} |".format(
                vid=record.video_id,
                title=escape_table(record.title),
                duration=record.duration,
                status=record.status,
                quality=escape_table(record.quality),
                source=escape_table(record.source),
                primary=escape_table(primary_playlist(record)),
                memberships=escape_table(membership_label(record.memberships)),
                upload_date=record.upload_date,
                uploader=escape_table(uploader_label(record)),
                raw_path=f"`{record.raw_path}`" if record.raw_path else "",
                notes=escape_table(record.notes),
            )
        )
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "_VIDEO_INDEX.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def sort_video_record(record: VideoRecord) -> tuple[str, int, str]:
    if record.memberships:
        first = record.memberships[0]
        try:
            pos = int(first.position)
        except (TypeError, ValueError):
            pos = 999999
        return (first.playlist_title.lower(), pos, record.title.lower())
    return ("zzzz-ungrouped", 999999, record.title.lower())


def write_playlist_manifests(
    raw_dir: Path,
    scrape_date: str,
    playlists: list[PlaylistRecord],
    videos: dict[str, VideoRecord],
) -> None:
    for playlist in playlists:
        lines = [
            f"# {playlist.title} - Playlist Manifest",
            "",
            f"**Channel:** {CHANNEL_URL}",
            f"**Playlist ID:** {playlist.playlist_id}",
            f"**Playlist URL:** {playlist.url}",
            f"**Scrape date:** {scrape_date}",
            f"**Reported video count:** {playlist.reported_count or 'unknown'}",
            f"**Enumerated rows:** {len(playlist.entries)}",
            f"**Owner/uploader:** {playlist.owner or 'unknown'}",
            "",
            "Playlist categories preserve YouTube organization only; they are not",
            "treated as Shinzen's own teaching taxonomy.",
            "",
            "| # | Video ID | Title | Length | Status | Quality | Source | Raw path | Notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for index, entry in enumerate(playlist.entries, start=1):
            video_id = video_id_from_entry(entry)
            record = videos.get(video_id)
            title = str(entry.get("title") or video_id or "unknown")
            duration = duration_label(entry.get("duration"))
            if record:
                title = record.title
                duration = record.duration
                status = record.status
                quality = record.quality
                source = record.source
                raw_path = record.raw_path
                notes = record.notes
            else:
                status = "enumeration_error"
                quality = "D"
                source = ""
                raw_path = ""
                notes = "Missing video ID in playlist enumeration."
            lines.append(
                "| {index} | `{video_id}` | {title} | {duration} | {status} | {quality} | {source} | {raw_path} | {notes} |".format(
                    index=index,
                    video_id=video_id,
                    title=escape_table(title),
                    duration=duration,
                    status=status,
                    quality=escape_table(quality),
                    source=escape_table(source),
                    raw_path=f"`{raw_path}`" if raw_path else "",
                    notes=escape_table(notes),
                )
            )
        target = raw_dir / "playlists" / playlist.slug / "_MANIFEST.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def count_by(records: Any, attr: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        key = getattr(record, attr) or ""
        if not key:
            continue
        counts[key] = counts.get(key, 0) + 1
    return counts


def write_discovery_outputs(
    raw_dir: Path,
    scrape_date: str,
    playlists: list[PlaylistRecord],
    videos: dict[str, VideoRecord],
    notes: list[str],
) -> None:
    write_channel_manifest(raw_dir, scrape_date, playlists, videos, notes)
    write_video_index(raw_dir, scrape_date, videos)
    write_playlist_manifests(raw_dir, scrape_date, playlists, videos)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scratch", type=Path, default=DEFAULT_SCRATCH)
    parser.add_argument("--pydeps", type=Path, default=DEFAULT_PYDEPS)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--scrape-date", default=date.today().isoformat())
    parser.add_argument("--enumerate-only", action="store_true")
    parser.add_argument("--no-stt", action="store_true")
    parser.add_argument("--stt-model", default="tiny.en")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Acquire only the first N unique videos after enumeration. Manifests still include all enumerated videos.",
    )
    args = parser.parse_args()

    args.scratch.mkdir(parents=True, exist_ok=True)
    pydeps = resolve_pydeps(args.pydeps)
    yt_dlp = import_ytdlp(pydeps)

    playlists = enumerate_playlists(yt_dlp, args.scratch)
    if not playlists:
        raise SystemExit("No public playlists were enumerated for @ShinzenVideos.")

    videos: dict[str, VideoRecord] = {}
    for playlist in playlists:
        enumerate_playlist_entries(yt_dlp, playlist, args.scratch)
        for index, entry in enumerate(playlist.entries, start=1):
            membership = Membership(playlist.playlist_id, playlist.title, index)
            add_or_update_video(videos, entry, membership)

    for entry in enumerate_channel_videos(yt_dlp, args.scratch):
        add_or_update_video(videos, entry, None, ungrouped=True)

    existing = find_existing_transcripts(ROOT)
    for record in videos.values():
        existing_path = existing.get(record.video_id)
        if existing_path is not None:
            apply_existing_transcript(record, existing_path, args.raw_dir)
        elif args.enumerate_only:
            record.status = "missing"
            record.notes = "Enumeration only; transcript not fetched."

    notes: list[str] = []
    if pydeps != args.pydeps:
        notes.append(f"Used existing dependency cache at `{pydeps}`.")

    write_discovery_outputs(args.raw_dir, args.scrape_date, playlists, videos, notes)
    if args.enumerate_only:
        print("Enumeration-only run complete.")
        print(f"Playlists: {len(playlists)}")
        print(f"Unique video IDs: {len(videos)}")
        return 0

    pending = [record for record in videos.values() if record.status == "pending"]
    if args.limit:
        acquire_set = {record.video_id for record in pending[: args.limit]}
        for record in pending:
            if record.video_id not in acquire_set:
                record.status = "missing"
                record.notes = f"Acquisition limited to first {args.limit} pending video(s)."
        pending = [record for record in pending if record.video_id in acquire_set]
        notes.append(f"Acquisition run was limited to the first {args.limit} pending video(s).")

    for index, record in enumerate(pending, start=1):
        print(f"[{index}/{len(pending)}] Acquiring {record.video_id}")
        acquire_video(
            yt_dlp,
            pydeps,
            args.scratch,
            args.raw_dir,
            args.scrape_date,
            record,
            run_stt=not args.no_stt,
            stt_model=args.stt_model,
        )
        write_discovery_outputs(args.raw_dir, args.scrape_date, playlists, videos, notes)

    write_discovery_outputs(args.raw_dir, args.scrape_date, playlists, videos, notes)
    status_counts = count_by(videos.values(), "status")
    print("Acquisition complete.")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")
    print(f"Wrote: {args.raw_dir / '_CHANNEL_MANIFEST.md'}")
    print(f"Wrote: {args.raw_dir / '_VIDEO_INDEX.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
