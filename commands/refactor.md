# refactor

Use for split, merge, rename, or move operations.

1. Identify the structural problem.
2. Preserve evidence and contradictions.
3. Keep old-to-new mapping legible.
4. Add aliases for renamed or merged pages.
5. Update inbound links, index entries, Related sections, and log.
6. Run `python tools/wiki_lint.py`, or `tools\wiki_lint.cmd` on this
   Windows/Codex workspace.

If the refactor touches more than five content pages, make the risk explicit
and leave a validation note.
