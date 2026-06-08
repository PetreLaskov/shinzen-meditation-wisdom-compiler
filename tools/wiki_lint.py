#!/usr/bin/env python3
"""Dependency-free structural lint for the Agentic Knowledge Compiler.

Run from the repository root:

    python tools/wiki_lint.py

Exit code 0 means the hard invariants passed. Advisory diagnostics are printed
afterward but do not affect the exit code.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
INDEX = WIKI / "index.md"
REGISTRATION_CATALOGS = (
    WIKI / "_page_catalog.md",
    WIKI / "_sources_catalog.md",
)

SYSTEM_PAGE_NAMES = {"index.md", "log.md"}
REQUIRED_FIELDS = {
    "type",
    "thesis",
    "status",
    "domain",
    "importance",
    "confidence",
    "tags",
    "aliases",
    "sources",
    "load_when",
    "best_linked_pages",
    "updated",
}
VALID_TYPES = {
    "source",
    "entity",
    "concept",
    "thesis",
    "synthesis",
    "analysis",
    "question",
}
VALID_STATUS = {"seed", "working", "mature", "evergreen"}
VALID_CONFIDENCE = {"established", "probable", "speculative", "contested"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
LINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")
REQUIRED_SOURCE_AUDIT_SECTIONS = (
    "## Weakest Claims",
    "## Important Omissions",
    "## Contradictions/Tensions",
)
RAW_SUPPORT_SUFFIXES = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".log",
    ".m4a",
    ".mp3",
    ".mp4",
    ".png",
    ".webp",
    ".wav",
}
RAW_SUPPORT_PATHS = {
    "Shinzen Sources/FiveWaystoKnowYourself_ver1.6.pdf",
    "Shinzen Sources/Previous wiki compiler - current_model.md",
    "Shinzen Sources/README.md",
    "Shinzen Sources/SeeHearFeelIntroduction_ver1.8.pdf",
    (
        "Shinzen Sources/Shinzen Young - The Science of Enlightenment_ How "
        "Meditation Works (2016, Sounds True) - libgen.li.epub"
    ),
}
SKIPPED_YOUTUBE_VIDEO_IDS = {
    "6XJN3TjhSZ8",  # non-Shinzen-primary Har-Prakash Khalsa guided practice
    "9LNRpkKzQh8",  # pure guided meditation
    "G6npSvMb5XQ",  # silent sit
    "Meqvr2zGn2U",  # non-Shinzen-primary Har-Prakash Khalsa guided practice
    "NS7_uN8F6P8",  # non-Shinzen-primary Har-Prakash Khalsa training module
    "Sb7O7LbcYn4",  # Pali chant/recitation
    "jex0giLXNAs",  # non-Shinzen-primary Har-Prakash Khalsa training module
    "tOYiHaXtwzY",  # Om Mani Padme Hum chant
    "zA1APGkoupM",  # Spanish-only recitation
}
YOUTUBE_SELECTION_CATALOGS = (
    WIKI / "_yt_shinzenvideos_selection_report.md",
)
YOUTUBE_SELECTION_BACKLOG_EXEMPT_STATUSES = {
    "skip-manifest-only",
}
YOUTUBE_ID_RE = re.compile(r"_([-A-Za-z0-9_]{11})\.md$")
SELECTION_STATUS_HEADING_RE = re.compile(
    r"(?m)^### "
    r"(ingest-now|series-candidate|audit-needed|upgrade-existing|"
    r"practice-wisdom-backlog|defer-query-driven|skip-manifest-only)\b"
)
SELECTION_STATUS_ID_RE = re.compile(r"`([-A-Za-z0-9_]{11})`")

# Frontmatter is the first-pass routing layer, not the page's full evidence
# map. These are advisory thresholds, not hard invariants.
LOAD_WHEN_STRONG_WARNING_CHARS = 500
LOAD_WHEN_TARGET_CHARS = 320
BEST_LINKS_STRONG_WARNING_COUNT = 12
BEST_LINKS_TARGET_COUNT = 8
NON_SOURCE_SOURCES_STRONG_WARNING_COUNT = 24
NON_SOURCE_SOURCES_TARGET_COUNT = 8
ALIASES_WARNING_COUNT = 16
INDEX_OPENING_TARGET_CHARS = 12000


@dataclass
class Page:
    path: Path
    frontmatter: dict[str, str]
    text: str

    @property
    def key(self) -> str:
        return self.path.relative_to(WIKI).with_suffix("").as_posix()

    @property
    def label(self) -> str:
        return rel(self.path)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_list(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        if not body:
            return []
        parts: list[str] = []
        current: list[str] = []
        quote: str | None = None

        for char in body:
            if char in {"'", '"'}:
                if quote is None and not "".join(current).strip():
                    quote = char
                elif quote == char:
                    quote = None
                current.append(char)
                continue

            if char == "," and quote is None:
                part = "".join(current).strip()
                if part:
                    parts.append(part)
                current = []
                continue

            current.append(char)

        part = "".join(current).strip()
        if part:
            parts.append(part)

        return [strip_quotes(part.strip()) for part in parts if part.strip()]
    return [strip_quotes(value)]


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None

    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        field = FIELD_RE.match(line)
        if field:
            fields[field.group(1)] = field.group(2).strip()
    return fields


def parse_updated(value: str) -> date | None:
    try:
        return date.fromisoformat(strip_quotes(value))
    except ValueError:
        return None


def normalize_page_reference(value: str) -> str:
    target = strip_quotes(value).strip()
    if target.startswith("[[") and target.endswith("]]"):
        target = target[2:-2]
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip("/")


def is_system_path(path: Path) -> bool:
    try:
        relative = path.relative_to(WIKI)
    except ValueError:
        return False
    parts = relative.parts
    return (
        relative.as_posix() in SYSTEM_PAGE_NAMES
        or path.name.startswith("_")
        or any(part.startswith("_") for part in parts[:-1])
    )


def is_youtube_transcript_path(relative: Path) -> bool:
    parts = relative.parts
    return (
        len(parts) >= 3
        and parts[0] == "Shinzen Sources"
        and parts[1] == "yt transcripts"
    )


def youtube_video_id(relative: Path) -> str | None:
    if not is_youtube_transcript_path(relative):
        return None
    match = YOUTUBE_ID_RE.search(relative.name)
    return match.group(1) if match else None


@lru_cache(maxsize=1)
def selection_backlog_exempt_video_ids() -> set[str]:
    """Video IDs selected out of active raw-backlog warnings."""

    exempt: set[str] = set()
    for catalog in YOUTUBE_SELECTION_CATALOGS:
        if not catalog.exists():
            continue

        text = catalog.read_text(encoding="utf-8")
        headings = list(SELECTION_STATUS_HEADING_RE.finditer(text))
        for index, heading in enumerate(headings):
            status = heading.group(1)
            if status not in YOUTUBE_SELECTION_BACKLOG_EXEMPT_STATUSES:
                continue

            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            block = text[heading.end() : end]
            exempt.update(SELECTION_STATUS_ID_RE.findall(block))

    return exempt


def youtube_transcript_priority(relative: Path) -> int:
    parts = relative.parts
    if "retranscribed" in parts:
        return 3
    if "edited" in parts:
        return 2
    return 1


def is_raw_support_file(path: Path) -> bool:
    relative = path.relative_to(RAW)
    rel_posix = relative.as_posix()

    if path.name == ".gitkeep" or path.name.startswith("_"):
        return True
    if path.name.lower() == "readme.md":
        return True
    if path.suffix.lower() in RAW_SUPPORT_SUFFIXES:
        return True
    if rel_posix in RAW_SUPPORT_PATHS:
        return True
    if "assets" in relative.parts or "images" in relative.parts:
        return True

    if (
        len(relative.parts) >= 3
        and relative.parts[0] == "Shinzen Sources"
        and relative.parts[1] == "science-of-enlightenment"
        and re.match(r"(?:00[a-z]|99[a-z])-", relative.name)
    ):
        return True

    video_id = youtube_video_id(relative)
    return video_id in SKIPPED_YOUTUBE_VIDEO_IDS or (
        video_id is not None and video_id in selection_backlog_exempt_video_ids()
    )


def iter_markdown() -> list[Path]:
    if not WIKI.exists():
        return []
    return sorted(WIKI.rglob("*.md"))


def iter_compiled_page_paths() -> list[Path]:
    return [path for path in iter_markdown() if not is_system_path(path)]


def iter_raw_sources() -> list[Path]:
    if not RAW.exists():
        return []

    sources: list[Path] = []
    youtube_sources: dict[str, Path] = {}
    for path in sorted(RAW.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(RAW)
        if is_raw_support_file(path):
            continue

        video_id = youtube_video_id(relative)
        if video_id:
            current = youtube_sources.get(video_id)
            if current is None or youtube_transcript_priority(
                relative
            ) > youtube_transcript_priority(current.relative_to(RAW)):
                youtube_sources[video_id] = path
            continue

        sources.append(path)

    sources.extend(youtube_sources.values())
    return sources


def extract_link_targets(text: str) -> list[str]:
    targets: list[str] = []
    in_fence = False

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Ignore indented code examples but keep indented list continuations.
        if line.startswith("    ") and not stripped.startswith(("- ", "* ")):
            continue

        cleaned = re.sub(r"`[^`]*`", "", line)
        for match in LINK_RE.finditer(cleaned):
            target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if target.endswith(".md"):
                target = target[:-3]
            target = target.strip("/")
            if target:
                targets.append(target)
    return targets


def build_target_map(markdown_paths: list[Path], pages: list[Page]) -> dict[str, Path]:
    target_map: dict[str, Path] = {}

    for path in markdown_paths:
        if is_system_path(path):
            continue
        key = path.relative_to(WIKI).with_suffix("").as_posix()
        target_map[key.lower()] = path
        target_map[path.stem.lower()] = path

    for page in pages:
        for alias in parse_list(page.frontmatter.get("aliases", "")):
            target_map[alias.lower()] = page.path

    return target_map


def validate_flat_page(page: Page, errors: list[str]) -> None:
    if page.path.parent != WIKI:
        errors.append(f"{page.label}: compiled pages must live directly in wiki/")


def validate_frontmatter(page: Page, errors: list[str]) -> None:
    fields = page.frontmatter
    missing = sorted(REQUIRED_FIELDS - fields.keys())
    if missing:
        errors.append(f"{page.label}: missing frontmatter fields: {', '.join(missing)}")
        return

    page_type = strip_quotes(fields["type"])
    if page_type not in VALID_TYPES:
        errors.append(f"{page.label}: invalid type '{page_type}'")

    status = strip_quotes(fields["status"])
    if status not in VALID_STATUS:
        errors.append(f"{page.label}: invalid status '{status}'")

    confidence = strip_quotes(fields["confidence"])
    if confidence not in VALID_CONFIDENCE:
        errors.append(f"{page.label}: invalid confidence '{confidence}'")

    try:
        importance = int(strip_quotes(fields["importance"]))
        if not 1 <= importance <= 10:
            errors.append(f"{page.label}: importance must be 1-10")
    except ValueError:
        errors.append(f"{page.label}: importance must be an integer")

    if not strip_quotes(fields["thesis"]):
        errors.append(f"{page.label}: thesis must not be empty")

    if not strip_quotes(fields["load_when"]):
        errors.append(f"{page.label}: load_when must not be empty")

    best_links_value = fields["best_linked_pages"].strip()
    if not (best_links_value.startswith("[") and best_links_value.endswith("]")):
        errors.append(f"{page.label}: best_linked_pages must be an inline list")

    if not parse_list(fields["domain"]):
        errors.append(f"{page.label}: domain must contain at least one value")

    if parse_updated(fields["updated"]) is None:
        errors.append(f"{page.label}: updated must be YYYY-MM-DD")

    sources = parse_list(fields["sources"])
    if page_type == "source":
        if len(sources) != 1:
            errors.append(f"{page.label}: source pages must cite exactly one raw source")
        for heading in REQUIRED_SOURCE_AUDIT_SECTIONS:
            if heading not in page.text:
                errors.append(f"{page.label}: source page missing {heading[3:]} section")
    if page_type != "source" and not sources and page_type not in {"synthesis", "question"}:
        errors.append(f"{page.label}: non-source pages must cite at least one raw source")

    for source in sources:
        source_path = ROOT / source
        if not source.startswith("raw/"):
            errors.append(f"{page.label}: source '{source}' must be a raw/ path")
        elif not source_path.exists():
            errors.append(f"{page.label}: source '{source}' does not exist")


def check_links(
    markdown_paths: list[Path],
    target_map: dict[str, Path],
    errors: list[str],
) -> Counter[Path]:
    inbound: Counter[Path] = Counter()

    for path in markdown_paths:
        if path.name.startswith("_") or any(part.startswith("_") for part in path.relative_to(WIKI).parts[:-1]):
            continue

        text = path.read_text(encoding="utf-8")
        for target in extract_link_targets(text):
            resolved = target_map.get(target.lower())
            if not resolved:
                errors.append(f"{rel(path)}: unresolved link [[{target}]]")
                continue
            if not is_system_path(path):
                inbound[resolved] += 1

    return inbound


def check_best_linked_pages(
    pages: list[Page],
    target_map: dict[str, Path],
    errors: list[str],
    warnings: list[str],
) -> None:
    for page in pages:
        raw_links = page.frontmatter.get("best_linked_pages")
        if raw_links is None:
            continue

        links = parse_list(raw_links)
        if not links:
            warnings.append(f"{page.label}: best_linked_pages is empty")
            continue

        for raw_link in links:
            target = normalize_page_reference(raw_link)
            if not target:
                errors.append(f"{page.label}: best_linked_pages contains an empty target")
                continue
            if target.lower() not in target_map:
                errors.append(
                    f"{page.label}: best_linked_pages target '{raw_link}' does not resolve"
                )


def registration_surfaces() -> list[Path]:
    surfaces = [INDEX]
    surfaces.extend(path for path in REGISTRATION_CATALOGS if path.exists())
    return surfaces


def check_page_registration(pages: list[Page], errors: list[str]) -> None:
    if not INDEX.exists():
        errors.append("wiki/index.md is missing")
        return

    registration_targets: set[str] = set()
    for path in registration_surfaces():
        registration_targets.update(
            target.lower() for target in extract_link_targets(path.read_text(encoding="utf-8"))
        )

    surfaces = ", ".join(rel(path) for path in registration_surfaces())
    for page in pages:
        if (
            page.key.lower() not in registration_targets
            and page.path.stem.lower() not in registration_targets
        ):
            errors.append(
                f"{page.label}: compiled page is missing from registration "
                f"surfaces ({surfaces})"
            )


def check_raw_source_coverage(
    pages: list[Page], errors: list[str], warnings: list[str]
) -> None:
    raw_paths = iter_raw_sources()
    raw_sources = [rel(path) for path in raw_paths]
    raw_source_set = set(raw_sources)
    raw_sources_by_video_id = {
        video_id: rel(path)
        for path in raw_paths
        if (video_id := youtube_video_id(path.relative_to(RAW)))
    }
    source_pages: dict[str, list[Page]] = defaultdict(list)

    for page in pages:
        if strip_quotes(page.frontmatter.get("type", "")) != "source":
            continue
        for source in parse_list(page.frontmatter.get("sources", "")):
            source_pages[source].append(page)

            source_path = ROOT / source
            try:
                relative = source_path.relative_to(RAW)
            except ValueError:
                continue

            video_id = youtube_video_id(relative)
            canonical = raw_sources_by_video_id.get(video_id or "")
            if canonical and canonical != source:
                errors.append(
                    f"{page.label}: source '{source}' is superseded by "
                    f"canonical raw source '{canonical}'"
                )
            elif source_path.exists() and is_raw_support_file(source_path):
                errors.append(
                    f"{page.label}: source '{source}' is marked as a support "
                    "artifact, not a canonical raw source"
                )

    for source, covering in sorted(source_pages.items()):
        if len(covering) > 1:
            labels = ", ".join(page.label for page in covering)
            errors.append(f"{source}: expected at most one source page, found {labels}")

    uncovered = sorted(raw_source_set - set(source_pages))
    if uncovered:
        preview = ", ".join(uncovered[:10])
        suffix = (
            "" if len(uncovered) <= 10 else f", ... (+{len(uncovered) - 10} more)"
        )
        warnings.append(
            f"raw source backlog: {len(uncovered)} canonical source(s) without "
            f"source pages: {preview}{suffix}"
        )


def check_source_dates(pages: list[Page], errors: list[str]) -> None:
    for page in pages:
        updated = parse_updated(page.frontmatter.get("updated", ""))
        if updated is None:
            continue

        for source in parse_list(page.frontmatter.get("sources", "")):
            source_path = ROOT / source
            if not source_path.exists():
                continue
            source_mdate = datetime.fromtimestamp(source_path.stat().st_mtime).date()
            if updated < source_mdate:
                errors.append(
                    f"{page.label}: updated {updated.isoformat()} predates source "
                    f"{source} modified {source_mdate.isoformat()}"
                )


def collect_warnings(pages: list[Page], inbound: Counter[Path], warnings: list[str]) -> None:
    tag_counts: Counter[str] = Counter()
    domain_counts: Counter[str] = Counter()

    for page in pages:
        fields = page.frontmatter
        page_type = strip_quotes(fields.get("type", ""))
        status = strip_quotes(fields.get("status", ""))
        thesis = strip_quotes(fields.get("thesis", ""))
        load_when = strip_quotes(fields.get("load_when", ""))
        best_links = parse_list(fields.get("best_linked_pages", ""))
        sources = parse_list(fields.get("sources", ""))
        aliases = parse_list(fields.get("aliases", ""))

        for tag in parse_list(fields.get("tags", "")):
            tag_counts[tag] += 1
        for domain in parse_list(fields.get("domain", "")):
            domain_counts[domain] += 1

        try:
            importance = int(strip_quotes(fields.get("importance", "0")))
        except ValueError:
            importance = 0

        if inbound[page.path] == 0 and page_type != "source":
            warnings.append(f"{page.label}: no inbound links from compiled pages")

        if importance >= 7 and status == "seed":
            warnings.append(f"{page.label}: high-importance page is still seed status")

        if thesis and len(thesis.split()) <= 3:
            warnings.append(f"{page.label}: thesis looks like a label, not a claim")

        if len(load_when) > LOAD_WHEN_STRONG_WARNING_CHARS:
            warnings.append(
                f"{page.label}: load_when is {len(load_when)} chars; strongly "
                f"target <= {LOAD_WHEN_TARGET_CHARS} for first-pass routing"
            )
        elif len(load_when) > LOAD_WHEN_TARGET_CHARS:
            warnings.append(
                f"{page.label}: load_when is {len(load_when)} chars; "
                f"target <= {LOAD_WHEN_TARGET_CHARS} for first-pass routing"
            )

        if len(best_links) > BEST_LINKS_STRONG_WARNING_COUNT:
            warnings.append(
                f"{page.label}: best_linked_pages has {len(best_links)} links; "
                f"strongly target <= {BEST_LINKS_TARGET_COUNT} strongest next loads"
            )
        elif len(best_links) > BEST_LINKS_TARGET_COUNT:
            warnings.append(
                f"{page.label}: best_linked_pages has {len(best_links)} links; "
                f"target <= {BEST_LINKS_TARGET_COUNT} strongest next loads"
            )

        if page_type != "source" and len(sources) > NON_SOURCE_SOURCES_STRONG_WARNING_COUNT:
            warnings.append(
                f"{page.label}: sources has {len(sources)} raw paths; "
                f"strongly target <= {NON_SOURCE_SOURCES_TARGET_COUNT}; "
                "frontmatter should keep only principal raw anchors"
            )
        elif page_type != "source" and len(sources) > NON_SOURCE_SOURCES_TARGET_COUNT:
            warnings.append(
                f"{page.label}: sources has {len(sources)} raw paths; "
                f"target <= {NON_SOURCE_SOURCES_TARGET_COUNT} principal raw anchors"
            )

        if len(aliases) > ALIASES_WARNING_COUNT:
            warnings.append(
                f"{page.label}: aliases has {len(aliases)} entries; "
                "keep only real lookup aliases, not query phrases"
            )

        if page_type == "source":
            if "## Source Snapshot" not in page.text:
                warnings.append(f"{page.label}: source page missing Source Snapshot section")
            if "## Key Claims" not in page.text:
                warnings.append(f"{page.label}: source page missing Key Claims section")
            elif not re.search(r"\*\*S\d+\*\*", page.text):
                warnings.append(f"{page.label}: source page has no S-numbered claim IDs")
            if "## Integration Notes" not in page.text:
                warnings.append(f"{page.label}: source page missing Integration Notes section")
            if inbound[page.path] == 0:
                warnings.append(
                    f"{page.label}: source page has no inbound links from compiled pages"
                )
        elif not sources:
            if "## Dependencies" not in page.text:
                warnings.append(
                    f"{page.label}: sources: [] page missing Dependencies section"
                )
            if not extract_link_targets(page.text):
                warnings.append(
                    f"{page.label}: sources: [] page has no compiled-page links"
                )

    singleton_tags = sorted(tag for tag, count in tag_counts.items() if count == 1)
    if singleton_tags:
        warnings.append("singleton tags: " + ", ".join(singleton_tags))

    total_pages = len(pages)
    if total_pages >= 5:
        for tag, count in sorted(tag_counts.items()):
            if count / total_pages > 0.4:
                warnings.append(f"tag '{tag}' covers {count}/{total_pages} pages; consider domain or retirement")

    for domain, count in sorted(domain_counts.items()):
        if count > 30:
            warnings.append(f"domain '{domain}' has {count} pages; consider synthesis or sub-indexing")


def check_index_opening_budget(warnings: list[str]) -> None:
    if not INDEX.exists():
        return

    text = INDEX.read_text(encoding="utf-8")
    marker = re.search(r"(?m)^## Open Questions\b", text)
    if marker:
        opening = text[: marker.start()]
        label = "opening through Open Questions"
    else:
        opening = text
        label = "opening"

    if len(opening) > INDEX_OPENING_TARGET_CHARS:
        warnings.append(
            f"{rel(INDEX)}: {label} is {len(opening)} chars; "
            f"target <= {INDEX_OPENING_TARGET_CHARS} for first-read routing"
        )


def load_pages(errors: list[str]) -> list[Page]:
    pages: list[Page] = []

    for path in iter_compiled_page_paths():
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            errors.append(f"{rel(path)}: missing YAML frontmatter")
            continue
        page = Page(path=path, frontmatter=frontmatter, text=text)
        validate_flat_page(page, errors)
        validate_frontmatter(page, errors)
        pages.append(page)

    return pages


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not WIKI.exists():
        errors.append("wiki/ directory is missing")
    if not RAW.exists():
        errors.append("raw/ directory is missing")

    markdown_paths = iter_markdown()
    pages = load_pages(errors) if WIKI.exists() else []

    target_map = build_target_map(markdown_paths, pages) if markdown_paths else {}
    inbound = check_links(markdown_paths, target_map, errors) if markdown_paths else Counter()
    check_best_linked_pages(pages, target_map, errors, warnings)
    check_page_registration(pages, errors)
    check_raw_source_coverage(pages, errors, warnings)
    check_source_dates(pages, errors)
    collect_warnings(pages, inbound, warnings)
    check_index_opening_budget(warnings)

    if errors:
        print(f"Wiki lint found {len(errors)} invariant error(s):")
        for error in errors:
            print(f"- {error}")
    else:
        print(
            f"OK: {len(pages)} compiled page(s), "
            f"{len(iter_raw_sources())} raw source(s) checked."
        )

    if warnings:
        print("\nDiagnostics:")
        for warning in warnings:
            print(f"- {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
