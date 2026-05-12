# Agentic Knowledge Compiler

A markdown-native knowledge compiler. You drop durable sources into `raw/`;
an agent compiles them into a linked wiki under `wiki/`; deterministic tools
check the structural invariants.

This is not a RAG chatbot or a file dump. The wiki is the working memory:
source pages, concepts, entities, theses, syntheses, analyses, questions,
links, contradictions, and confidence judgments that compound over time.

## Quick Start

```bash
python tools/wiki_lint.py
```

On this Windows/Codex workspace, `tools\wiki_lint.cmd` uses the bundled
Python runtime when `python` is not on PATH.

An empty install should report zero compiled pages and zero raw sources.

Then:

1. Add source files to `raw/`.
2. Ask an agent to ingest one source.
3. Review the created source page and any derived pages.
4. Run `python tools/wiki_lint.py` or `tools\wiki_lint.cmd`.
5. Repeat. After several sources, refresh the shape paragraph in
   `wiki/index.md`.

Good first prompt:

```text
Read AGENTS.md, wiki/index.md, and wiki/log.md. Ingest raw/<file>. Create
exactly one source page for it, promote reusable concepts/entities/questions
where justified, update index and log, then run lint.
```

## Files

| Path | Purpose |
|---|---|
| `AGENTS.md` | Canonical agent operating contract. |
| `CLAUDE.md` | Small compatibility adapter pointing to `AGENTS.md`. |
| `DESIGN.md` | Design rationale and implementation philosophy. |
| `raw/` | Immutable source corpus. |
| `raw/assets/` | Binary assets referenced by raw source stubs. |
| `raw/README.md` | Source intake and quality guide. |
| `wiki/index.md` | Main routing surface. Read first every session. |
| `wiki/log.md` | Append-only operation history, newest first. |
| `wiki/_templates.md` | Seven page templates. |
| `wiki/_operations.md` | Workflow manual. |
| `wiki/_shape.md` | Shape paragraph guide for the index. |
| `tools/wiki_lint.py` | Dependency-free invariant checker. |
| `tools/wiki_lint.cmd` | Windows helper that uses bundled Python when needed. |
| `commands/` | Agent-neutral playbooks for each mode. |

## Modes

- `ingest`: raw source to source page plus warranted derived pages.
- `query`: answer from the compiled wiki first; file reusable answers.
- `synthesize`: create a domain map or argued thesis.
- `lint`: run deterministic checks and surface semantic debt.
- `review`: consolidate health, graph quality, questions, and index shape.
- `refactor`: split, merge, rename, or move pages.

Use one primary mode per turn. The system improves fastest when each session
leaves durable wiki artifacts and a clear log entry.

## Design Commitments

- Raw sources remain immutable.
- Compiled pages stay flat in `wiki/` for Obsidian-friendly linking.
- The seven page types carry distinct epistemic moves.
- Every load-bearing claim is cited or explicitly marked unsupported.
- Page creation is balanced: avoid both bloated summary pages and noun spam.
- Tools are earned guardrails, not the center of the system.
