# shf-ingest-next

Use when the user asks to "run next in SHF ingestion plan".

1. Read `wiki/_shf_ingestion_plan.md`.
2. Select the first row in `Unit Queue` whose status is `pending`.
3. Ingest exactly that one raw unit file using the standard `commands/ingest.md` workflow.
4. Update the source page, warranted owner pages, `wiki/index.md`, `wiki/log.md`, and the status row in `wiki/_shf_ingestion_plan.md`.
5. Run `tools\wiki_lint.cmd` and report expected staged-source errors plus any new target errors.

The original PDF is the verification parent. Do not ingest it as one blob while this unit plan is active.
