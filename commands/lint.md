# lint

Use when checking structural health.

1. Run `python tools/wiki_lint.py`, or `tools\wiki_lint.cmd` on this
   Windows/Codex workspace.
2. Treat script errors as hard structural issues.
3. Add semantic diagnostics manually: weak theses, link spam, uncited claims,
   bloated pages, smoothed contradictions, vague index entries, and pages
   doing too many jobs.
4. Do not auto-fix broad review or refactor work during lint.
5. Log only if the run reveals follow-up work.
