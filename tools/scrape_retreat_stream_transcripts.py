#!/usr/bin/env python3
"""Scrape caption transcripts for Shinzen retreat stream playlists.

This tool is intentionally caption-first. It enumerates a YouTube playlist,
deduplicates against the existing raw YouTube transcript corpus by video ID,
fetches English captions where available, writes final Markdown transcripts
under raw/, and leaves audio/STT fallback as an explicit manifest status.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import html
import json
from pathlib import Path
import re
import sys
import unicodedata
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLAYLIST_URL = (
    "https://www.youtube.com/watch?v=kfU_XjT32Yg"
    "&list=PLjRQFjS1OrSy3q69a9femKVKH1SiywGwu"
)
DEFAULT_PLAYLIST_ID = "PLjRQFjS1OrSy3q69a9femKVKH1SiywGwu"
DEFAULT_SCRATCH = Path(r"C:\tmp\shinzen_retreat_stream_scrape")
DEFAULT_PYDEPS = DEFAULT_SCRATCH / "pydeps"
DEFAULT_RAW_DIR = ROOT / "raw" / "Shinzen Sources" / "yt transcripts" / "retreat streams"
YT_ID_RE = re.compile(r"_([-A-Za-z0-9_]{11})\.md$")
TIMESTAMP_RE = re.compile(
    r"(?P<start>\d{1,2}:\d{2}:\d{2}\.\d{3}|\d{1,2}:\d{2}\.\d{3})\s+-->\s+"
)


@dataclass
class CaptionChoice:
    source: str
    quality: str
    language: str
    ext: str
    url: str
    note: str


@dataclass
class ManifestRow:
    position: int
    video_id: str
    title: str
    duration: str
    status: str
    quality: str
    source: str
    raw_path: str
    notes: str


@dataclass
class TranscriptWriteResult:
    path: Path
    segment_count: int


def import_ytdlp(pydeps: Path) -> object:
    if pydeps.exists():
        sys.path.insert(0, str(pydeps))
    try:
        import yt_dlp  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            f"yt-dlp is not importable. Install it with: py -m pip install --target {pydeps} yt-dlp"
        ) from exc
    return yt_dlp


def import_faster_whisper(pydeps: Path) -> object:
    if pydeps.exists():
        sys.path.insert(0, str(pydeps))
    try:
        import faster_whisper  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            f"faster-whisper is not importable. Install it with: py -m pip install --target {pydeps} faster-whisper"
        ) from exc
    return faster_whisper


def sanitize_title(value: str, fallback: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_value = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", " ", ascii_value)
    ascii_value = re.sub(r"\s+", " ", ascii_value).strip(" .")
    ascii_value = ascii_value[:150].strip(" .")
    return ascii_value or fallback


def duration_label(seconds: object) -> str:
    if not isinstance(seconds, (int, float)) or seconds < 0:
        return "unknown"
    total = int(seconds)
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def timestamp(seconds: float) -> str:
    total = max(0, int(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def seconds_from_vtt(value: str) -> float:
    parts = value.split(":")
    if len(parts) == 2:
        minutes, secs = parts
        return int(minutes) * 60 + float(secs)
    hours, minutes, secs = parts
    return int(hours) * 3600 + int(minutes) * 60 + float(secs)


def clean_caption_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = value.replace("\ufeff", " ")
    value = value.replace("\u200b", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def parse_json3(text: str) -> list[tuple[float, str]]:
    data = json.loads(text)
    segments: list[tuple[float, str]] = []
    for event in data.get("events", []):
        if "segs" not in event:
            continue
        raw = "".join(seg.get("utf8", "") for seg in event.get("segs", []))
        cleaned = clean_caption_text(raw)
        if not cleaned:
            continue
        start_ms = event.get("tStartMs", 0)
        try:
            start = float(start_ms) / 1000.0
        except (TypeError, ValueError):
            start = 0.0
        segments.append((start, cleaned))
    return dedupe_segments(segments)


def parse_vtt(text: str) -> list[tuple[float, str]]:
    segments: list[tuple[float, str]] = []
    blocks = re.split(r"\n\s*\n", text.replace("\r\n", "\n"))
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        if lines[0].startswith(("WEBVTT", "Kind:", "Language:", "NOTE", "STYLE", "REGION")):
            continue

        timing_index = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if timing_index is None:
            continue

        match = TIMESTAMP_RE.search(lines[timing_index])
        if not match:
            continue
        start = seconds_from_vtt(match.group("start"))
        caption_lines = lines[timing_index + 1 :]
        cleaned = clean_caption_text(" ".join(caption_lines))
        if cleaned:
            segments.append((start, cleaned))
    return dedupe_segments(segments)


def dedupe_segments(segments: list[tuple[float, str]]) -> list[tuple[float, str]]:
    deduped: list[tuple[float, str]] = []
    previous = ""
    for start, text in segments:
        if not text:
            continue
        if text == previous:
            continue
        if previous and text.startswith(previous) and len(text) - len(previous) < 80:
            if deduped:
                deduped[-1] = (deduped[-1][0], text)
            previous = text
            continue
        deduped.append((start, text))
        previous = text
    return deduped


def coalesce_segments(segments: list[tuple[float, str]]) -> list[tuple[float, str]]:
    if not segments:
        return []

    groups: list[tuple[float, str]] = []
    start, text = segments[0]
    group_start = start
    last_start = start
    parts = [text]

    for current_start, current_text in segments[1:]:
        gap = current_start - last_start
        span = current_start - group_start
        candidate_length = sum(len(part) for part in parts) + len(current_text) + len(parts)
        if gap > 15 or span > 35 or candidate_length > 750:
            groups.append((group_start, " ".join(parts)))
            group_start = current_start
            parts = [current_text]
        else:
            parts.append(current_text)
        last_start = current_start

    groups.append((group_start, " ".join(parts)))
    return groups


def format_transcript(segments: list[tuple[float, str]]) -> str:
    groups = coalesce_segments(segments)
    if not groups:
        return "[No transcript text was recovered.]"
    return "\n\n".join(f"[{timestamp(start)}] {text}" for start, text in groups)


def markdown_filename(raw_dir: Path, title: str, video_id: str) -> Path:
    return raw_dir / f"{sanitize_title(title, video_id)}_{video_id}.md"


def find_existing_transcripts(root: Path) -> dict[str, Path]:
    existing: dict[str, Path] = {}
    yt_root = root / "raw" / "Shinzen Sources" / "yt transcripts"
    if not yt_root.exists():
        return existing

    for path in yt_root.rglob("*.md"):
        if path.name.startswith("_"):
            continue
        match = YT_ID_RE.search(path.name)
        if not match:
            continue
        video_id = match.group(1)
        # Mirror lint's canonical order: retranscribed > edited > root/other.
        current = existing.get(video_id)
        if current is None or transcript_priority(path) > transcript_priority(current):
            existing[video_id] = path
    return existing


def transcript_priority(path: Path) -> int:
    parts = set(path.parts)
    if "retranscribed" in parts:
        return 3
    if "edited" in parts:
        return 2
    return 1


def read_transcript_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return metadata

    for line in lines:
        if line.strip() == "---":
            break
        match = re.match(r"- \*\*(.+?):\*\*\s*(.*)$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip()
    return metadata


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def choose_caption(info: dict) -> CaptionChoice | None:
    language_preferences = ["en", "en-US", "en-GB", "a.en"]
    extension_preferences = ["json3", "vtt", "ttml", "srv3", "srv2", "srv1"]

    for source_key, source_label, quality in [
        ("subtitles", "youtube captions", "A"),
        ("automatic_captions", "youtube auto captions", "B"),
    ]:
        tracks = info.get(source_key) or {}
        ordered_languages = [
            lang for lang in language_preferences if lang in tracks
        ] + sorted(lang for lang in tracks if lang.lower().startswith("en") and lang not in language_preferences)
        for language in ordered_languages:
            formats = tracks.get(language) or []
            for ext in extension_preferences:
                for item in formats:
                    if item.get("ext") == ext and item.get("url"):
                        return CaptionChoice(
                            source=source_label,
                            quality=quality,
                            language=language,
                            ext=ext,
                            url=item["url"],
                            note=f"{language} {ext}",
                        )
    return None


def fetch_url(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", errors="replace")


def write_markdown_transcript(
    raw_dir: Path,
    playlist_id: str,
    scrape_date: str,
    entry: dict,
    source: str,
    quality: str,
    notes: str,
    segments: list[tuple[float, str]],
) -> TranscriptWriteResult:
    video_id = entry["id"]
    title = entry.get("title") or video_id
    target = markdown_filename(raw_dir, title, video_id)
    transcript = format_transcript(segments)
    duration = duration_label(entry.get("duration"))
    position = entry.get("playlist_index") or entry.get("__playlist_index") or ""

    body = "\n".join(
        [
            f"# {title}",
            "",
            f"- **Video ID:** {video_id}",
            f"- **URL:** https://www.youtube.com/watch?v={video_id}",
            f"- **Playlist:** {playlist_id}",
            f"- **Playlist position:** {position}",
            f"- **Source:** {source}",
            f"- **Length:** {duration}",
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
    raw_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8", newline="\n")
    return TranscriptWriteResult(target, len(segments))


def parse_caption(choice: CaptionChoice, text: str) -> list[tuple[float, str]]:
    if choice.ext == "json3":
        return parse_json3(text)
    if choice.ext == "vtt":
        return parse_vtt(text)
    # yt-dlp sometimes lists XML caption formats. They are kept as fallback by
    # stripping tags into rough text, but quality should be audited manually.
    stripped = clean_caption_text(text)
    return [(0.0, stripped)] if stripped else []


def write_transcript(
    raw_dir: Path,
    playlist_id: str,
    scrape_date: str,
    entry: dict,
    choice: CaptionChoice,
    caption_text: str,
) -> tuple[Path, int]:
    segments = parse_caption(choice, caption_text)
    result = write_markdown_transcript(
        raw_dir,
        playlist_id,
        scrape_date,
        entry,
        choice.source,
        choice.quality,
        f"Caption track `{choice.note}`. Long retreat stream transcript; exact wording should be spot-checked before source-page citation.",
        segments,
    )
    return result.path, result.segment_count


def download_audio(yt_dlp: object, scratch: Path, video_id: str, video_url: str) -> Path:
    audio_dir = scratch / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    existing = [
        path
        for path in audio_dir.glob(f"{video_id}.*")
        if path.suffix.lower() not in {".part", ".ytdl", ".json"}
    ]
    if existing:
        return max(existing, key=lambda path: path.stat().st_size)

    opts = {
        "quiet": True,
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "outtmpl": str(audio_dir / "%(id)s.%(ext)s"),
        "noplaylist": True,
        "ignoreerrors": False,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.extract_info(video_url, download=True)

    downloaded = [
        path
        for path in audio_dir.glob(f"{video_id}.*")
        if path.suffix.lower() not in {".part", ".ytdl", ".json"}
    ]
    if not downloaded:
        raise FileNotFoundError(f"Could not find downloaded audio for {video_id}")
    return max(downloaded, key=lambda path: path.stat().st_size)


def transcribe_with_faster_whisper(
    pydeps: Path,
    scratch: Path,
    audio_path: Path,
    model_name: str,
) -> list[tuple[float, str]]:
    faster_whisper = import_faster_whisper(pydeps)
    model_dir = scratch / "models"
    model_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading faster-whisper model: {model_name}")
    model = faster_whisper.WhisperModel(
        model_name,
        device="cpu",
        compute_type="int8",
        download_root=str(model_dir),
    )
    print(f"Transcribing audio: {audio_path}")
    segment_iter, info = model.transcribe(
        str(audio_path),
        beam_size=1,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 1000},
    )
    print(
        "Detected language: {language} ({probability:.2f})".format(
            language=getattr(info, "language", "unknown"),
            probability=getattr(info, "language_probability", 0.0),
        )
    )

    segments: list[tuple[float, str]] = []
    for index, segment in enumerate(segment_iter, start=1):
        cleaned = clean_caption_text(segment.text)
        if cleaned:
            segments.append((float(segment.start), cleaned))
        if index % 100 == 0:
            print(f"  transcribed {index} segment(s)")
    return segments


def write_stt_transcript(
    raw_dir: Path,
    playlist_id: str,
    scrape_date: str,
    entry: dict,
    model_name: str,
    segments: list[tuple[float, str]],
) -> TranscriptWriteResult:
    return write_markdown_transcript(
        raw_dir,
        playlist_id,
        scrape_date,
        entry,
        f"faster-whisper ({model_name}, CPU int8, VAD)",
        "C",
        "Local STT fallback because no English YouTube caption or auto-caption track was available. Exact wording, Buddhist vocabulary, names, and speaker attribution require source-page spot checks.",
        segments,
    )


def write_manifest(
    target: Path,
    playlist_url: str,
    playlist_id: str,
    scrape_date: str,
    rows: list[ManifestRow],
    notes: list[str],
) -> None:
    status_counts: dict[str, int] = {}
    quality_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for row in rows:
        status_counts[row.status] = status_counts.get(row.status, 0) + 1
        if row.quality:
            quality_counts[row.quality] = quality_counts.get(row.quality, 0) + 1
        if row.source:
            source_counts[row.source] = source_counts.get(row.source, 0) + 1

    generated_notes = list(notes)
    if status_counts.get("existing"):
        generated_notes.append(
            f"Deduplication found {status_counts['existing']} already-covered video(s); no duplicate transcript was written for those IDs."
        )
    caption_written = sum(
        1
        for row in rows
        if row.status == "written" and row.source.startswith("youtube")
    )
    stt_written = sum(
        1
        for row in rows
        if row.status == "written" and row.source.startswith("faster-whisper")
    )
    if caption_written:
        generated_notes.append(
            f"Caption fetch produced {caption_written} transcript file(s). Quality B means YouTube auto captions: useful for routing and triage, but exact wording and specialist vocabulary require source-page spot checks."
        )
    if stt_written:
        generated_notes.append(
            f"Local STT produced {stt_written} transcript file(s). Quality C means no caption track was available; exact wording, Buddhist vocabulary, names, and speaker attribution require stronger spot checks before citation."
        )
    if status_counts.get("stt_needed"):
        generated_notes.append(
            f"{status_counts['stt_needed']} video(s) had no English caption or auto-caption track and need local STT fallback before ingestion."
        )

    lines = [
        "# Shinzen Retreat Stream Transcripts - Scrape Manifest",
        "",
        f"**Playlist:** {playlist_url}",
        f"**Playlist ID:** {playlist_id}",
        f"**Scrape date:** {scrape_date}",
        f"**Videos enumerated:** {len(rows)}",
        "",
        "## Status",
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

    lines.extend(
        [
            "",
            "## Notes",
            "",
        ]
    )
    if generated_notes:
        lines.extend(f"- {note}" for note in generated_notes)
    else:
        lines.append("- No additional notes.")

    lines.extend(
        [
            "",
            "## Videos",
            "",
            "| # | Video ID | Title | Length | Status | Quality | Source | Raw path | Notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for row in rows:
        lines.append(
            "| {position} | `{video_id}` | {title} | {duration} | {status} | {quality} | {source} | {raw_path} | {notes} |".format(
                position=row.position,
                video_id=row.video_id,
                title=escape_table(row.title),
                duration=row.duration,
                status=row.status,
                quality=row.quality,
                source=escape_table(row.source),
                raw_path=f"`{row.raw_path}`" if row.raw_path else "",
                notes=escape_table(row.notes),
            )
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def escape_table(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--playlist-url", default=DEFAULT_PLAYLIST_URL)
    parser.add_argument("--playlist-id", default=DEFAULT_PLAYLIST_ID)
    parser.add_argument("--scratch", type=Path, default=DEFAULT_SCRATCH)
    parser.add_argument("--pydeps", type=Path, default=DEFAULT_PYDEPS)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--scrape-date", default=date.today().isoformat())
    parser.add_argument("--enumerate-only", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument(
        "--stt-video-id",
        default="",
        help="When a listed video has no captions, run local STT for this one video ID.",
    )
    parser.add_argument("--stt-model", default="tiny.en")
    args = parser.parse_args()

    args.scratch.mkdir(parents=True, exist_ok=True)
    yt_dlp = import_ytdlp(args.pydeps)
    existing = find_existing_transcripts(ROOT)

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": "in_playlist",
        "ignoreerrors": True,
        "no_warnings": True,
    }

    notes: list[str] = []
    print(f"Enumerating playlist: {args.playlist_url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(args.playlist_url, download=False)

    entries = [entry for entry in (playlist_info.get("entries") or []) if entry]
    if args.limit:
        entries = entries[: args.limit]
        notes.append(f"Run was limited to the first {args.limit} playlist entries.")

    enum_path = args.scratch / "playlist_enumeration.json"
    enum_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Enumerated {len(entries)} video(s). Scratch enumeration: {enum_path}")

    rows: list[ManifestRow] = []
    full_info_opts = {
        "quiet": True,
        "skip_download": True,
        "ignoreerrors": True,
        "no_warnings": True,
    }

    for index, entry in enumerate(entries, start=1):
        video_id = entry.get("id") or entry.get("url")
        title = entry.get("title") or video_id or "unknown"
        duration = duration_label(entry.get("duration"))
        if not video_id:
            rows.append(
                ManifestRow(index, "", title, duration, "enumeration_error", "D", "", "", "Missing video ID.")
            )
            continue

        existing_path = existing.get(video_id)
        if existing_path is not None:
            metadata = read_transcript_metadata(existing_path)
            existing_source = metadata.get("Source", "existing corpus")
            existing_quality = metadata.get("Transcript quality", "existing")
            if is_within(existing_path, args.raw_dir):
                status = "written"
                note = "Transcript is already present in the retreat-stream scrape output; no duplicate was written on rerun."
            else:
                status = "existing"
                note = "Video ID already has a local canonical transcript outside the retreat-stream scrape output."
            rows.append(
                ManifestRow(
                    index,
                    video_id,
                    title,
                    duration,
                    status,
                    existing_quality,
                    existing_source,
                    existing_path.relative_to(ROOT).as_posix(),
                    note,
                )
            )
            continue

        if args.enumerate_only:
            rows.append(
                ManifestRow(index, video_id, title, duration, "missing", "", "", "", "Enumeration only; transcript not fetched.")
            )
            continue

        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"[{index}/{len(entries)}] Inspecting captions: {video_id} {title}")
        try:
            with yt_dlp.YoutubeDL(full_info_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)
        except Exception as exc:  # noqa: BLE001 - record external extraction failures.
            rows.append(
                ManifestRow(index, video_id, title, duration, "metadata_failed", "D", "", "", f"{type(exc).__name__}: {exc}")
            )
            continue

        if not info:
            rows.append(
                ManifestRow(index, video_id, title, duration, "metadata_failed", "D", "", "", "yt-dlp returned no metadata.")
            )
            continue

        if info.get("duration"):
            duration = duration_label(info.get("duration"))
        if info.get("title"):
            title = info["title"]
        entry = {**entry, **{"id": video_id, "title": title, "duration": info.get("duration", entry.get("duration"))}}

        choice = choose_caption(info)
        if choice is None:
            if args.stt_video_id and video_id == args.stt_video_id:
                try:
                    audio_path = download_audio(yt_dlp, args.scratch, video_id, video_url)
                    segments = transcribe_with_faster_whisper(
                        args.pydeps, args.scratch, audio_path, args.stt_model
                    )
                    result = write_stt_transcript(
                        args.raw_dir,
                        args.playlist_id,
                        args.scrape_date,
                        entry,
                        args.stt_model,
                        segments,
                    )
                except Exception as exc:  # noqa: BLE001 - external STT can fail in many ways.
                    rows.append(
                        ManifestRow(
                            index,
                            video_id,
                            title,
                            duration,
                            "stt_failed",
                            "C failed",
                            f"faster-whisper ({args.stt_model})",
                            "",
                            f"{type(exc).__name__}: {exc}",
                        )
                    )
                    continue

                rows.append(
                    ManifestRow(
                        index,
                        video_id,
                        title,
                        duration,
                        "written",
                        "C",
                        f"faster-whisper ({args.stt_model}, CPU int8, VAD)",
                        result.path.relative_to(ROOT).as_posix(),
                        f"No caption track; local STT recovered {result.segment_count} segment(s).",
                    )
                )
                continue

            rows.append(
                ManifestRow(
                    index,
                    video_id,
                    title,
                    duration,
                    "stt_needed",
                    "C pending",
                    "",
                    "",
                    "No English caption or auto-caption track found. Local STT fallback required.",
                )
            )
            continue

        try:
            caption_text = fetch_url(choice.url)
            target, segment_count = write_transcript(
                args.raw_dir,
                args.playlist_id,
                args.scrape_date,
                entry,
                choice,
                caption_text,
            )
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, OSError, ValueError) as exc:
            rows.append(
                ManifestRow(
                    index,
                    video_id,
                    title,
                    duration,
                    "caption_failed",
                    choice.quality,
                    choice.source,
                    "",
                    f"{choice.note}; {type(exc).__name__}: {exc}",
                )
            )
            continue

        rows.append(
            ManifestRow(
                index,
                video_id,
                title,
                duration,
                "written",
                choice.quality,
                choice.source,
                target.relative_to(ROOT).as_posix(),
                f"Caption track {choice.note}; recovered {segment_count} caption segment(s).",
            )
        )

    manifest_path = args.raw_dir / "_MANIFEST.md"
    write_manifest(manifest_path, args.playlist_url, args.playlist_id, args.scrape_date, rows, notes)
    print(f"Wrote manifest: {manifest_path}")

    status_counts: dict[str, int] = {}
    for row in rows:
        status_counts[row.status] = status_counts.get(row.status, 0) + 1
    print("Status counts:")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
