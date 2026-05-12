# ingest

Use when compiling one or more raw sources into the wiki.

1. Read `AGENTS.md`, the routing-relevant portions of `wiki/index.md`, and
   recent `wiki/log.md` entries only.
2. Read the source fully.
3. Create or update exactly one `type: source` page for each raw file.
4. Extract source claims, source frame, weakest claims, important omissions,
   contradictions/tensions, model delta, and integration notes. Source pages
   must include those audit sections explicitly and say what the source
   changed, confirmed, challenged, or failed to change.
   For Shinzen YouTube lectures, also read `wiki/_yt_lecture_ingest.md` and
   the relevant sections of `wiki/_yt_ingestion_implementation_plan.md`;
   preserve teaching register,
   practice handles, live routing moves, and idiolect worth future reuse.
5. Create or update derived pages only when they improve future routing,
   practice reasoning, or teaching-transmission fidelity.
6. Update `wiki/index.md` and `wiki/log.md`.
7. Run `python tools/wiki_lint.py`, or `tools\wiki_lint.cmd` on this
   Windows/Codex workspace.

Do not create pages for every noun. Do not hide recurring ideas inside a
source page when a useful stub would route better.
