# Raw Sources

Drop source documents here. The agent may read them, cite them, and compile
from them, but it must not modify them. Treat `raw/` as immutable evidence.

## Good Raw Sources

Good sources have:

- One cohesive topic or scope per file.
- Recoverable provenance: author, origin, publication date, URL, meeting,
  organization, or other source context.
- Enough substance to support claims, not just impressions.
- A stable filename that can be cited from source pages.

Markdown is preferred for text. If the source is a PDF, image, audio file, or
other binary, place the binary in `raw/assets/` and create a markdown stub in
`raw/` that records title, author or origin, date, format, summary, and a
path to the asset.

## What Not To Put Here

- Scratch notes, todos, or half-formed personal thoughts.
- Generated summaries without provenance.
- Files the agent is expected to edit.
- Search-result dumps with no curation.
- Duplicate copies of already-ingested sources.

## Source Size

The agent reads the source closely. Prefer focused sources. If a document is
very large or covers many unrelated topics, split it into focused excerpts or
create several source stubs that point to the relevant asset sections.

## Naming

Use names that a future reader can understand. Either Title Case or
date-author-topic patterns are fine:

```text
raw/2026-04-Internal Strategy Memo.md
raw/Smith 2024 Institutional Reform Chapter 3.md
```

Do not rely on folder structure for meaning. The compiled wiki uses
frontmatter, links, and index placement for routing.

## Assets

Place binaries under `raw/assets/`. Example:

```text
raw/
  Smith 2024 Institutional Reform.md
  assets/
    smith-2024-institutional-reform.pdf
```

The markdown stub is the source the agent ingests. The asset is supporting
evidence referenced by the stub.
