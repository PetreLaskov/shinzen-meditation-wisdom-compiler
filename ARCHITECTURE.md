# Architecture: the knowledge compiler

This repository is one instance of a general, **corpus-agnostic agentic
knowledge compiler** - a method for turning a large, contested, partly tacit
body of sources into a calibrated, navigable, auditable knowledge graph that an
AI agent can reason from. The Shinzen wiki is the payload; the machinery is
reusable. This page is for people who want to understand how it works or
**point it at their own corpus.**

The full rationale and the rejected alternatives are in [`DESIGN.md`](DESIGN.md);
the operating contract agents follow is [`AGENTS.md`](AGENTS.md). This page is
the digestible overview between them.

## The one invariant

Everything follows from a single line:

> **Maximize future reasoning quality per token loaded** - here: practice-
> reasoning quality, phenomenological discrimination, and transmission fidelity -
> while keeping claims calibrated.

From that one principle: route before reading, cite load-bearing claims,
distribute depth across linked pages instead of bloating any one, and keep the
architecture simple even as the knowledge graph grows rich.

## The layers

| Layer | Path | Owner | Job |
| --- | --- | --- | --- |
| Raw evidence | `raw/` | human / curator | immutable sources; cited, never edited |
| Compiled wiki | `wiki/` | agent | the durable, calibrated knowledge graph - the source of truth |
| Reading layer | `public-atlas/` | agent + editor | human-readable distillation of the wiki |
| Governing contract | `AGENTS.md`, `wiki/_*.md` | mixed | operating rules, templates, page conventions |
| Verification | `tools/wiki_lint.py` | mixed | dependency-free mechanical invariant checks |

The wiki is the source of truth. The atlas is a human-readable branch of it. Raw
stays immutable evidence.

## The primitives

- **Seven epistemic page types.** Every compiled page is one of `source`,
  `entity`, `concept`, `thesis`, `synthesis`, `analysis`, or `question` - each a
  distinct epistemic move (evidence interface, real-world thing, reusable
  abstraction, argued position, domain map, reusable answer, open frontier).
  Types are few on purpose.
- **Frontmatter as routing surface.** Each page declares a one-sentence `thesis`
  (a claim, not a topic), plus `status` (seed -> working -> mature -> evergreen),
  `domain`, `importance`, `confidence` (established / probable / speculative /
  contested), and routing cues (`load_when`, `best_linked_pages`). Agents route
  on this *before* opening a body.
- **Required audit surfaces.** Source pages must carry `Weakest Claims`,
  `Important Omissions`, `Contradictions/Tensions`, and a `Model Delta` (what
  the source changed, confirmed, challenged, or failed to change). This is what
  keeps the model calibrated rather than credulous.
- **Progressive disclosure.** A fixed compression gradient - index entry ->
  frontmatter thesis -> opening -> key-points card -> body -> related -> raw
  source - lets a reader stop at the shallowest layer that answers the question.
- **Contradictions preserved, frames recorded.** Disagreements are attributed
  and kept (marked `contested`, opened as a `question`); source agendas are
  noted; stakeholder claims are never laundered into established facts.
- **Deterministic verification.** [`tools/wiki_lint.py`](tools/wiki_lint.py)
  enforces the mechanical invariants - frontmatter validity, link resolution,
  one source page per raw source, index coverage, citation discipline, the
  required audit sections. Judgment-heavy checks stay with the agent.
- **Earned complexity.** Search, source digests, claim IDs, graph tools, and
  embeddings are explicit *escalation gates*, not default scope: each must beat
  the plain markdown / index / page-card baseline before it is added.

## The modes

An agent works the wiki in one mode per turn:

- `ingest` - raw source -> one source page plus warranted derived pages.
- `query` - answer from the compiled wiki first; file reusable answers.
- `synthesize` - create a synthesis or thesis from existing pages.
- `lint` - run the deterministic checker, then add semantic review.
- `review` - inspect health, debt, graph quality, questions, index shape.
- `refactor` - split, merge, rename, or move pages.

The per-mode playbooks live in [`commands/`](commands/).

## Reuse it on your own corpus

The machinery has no Shinzen dependencies. To point it at a different body of
sources:

1. **Keep the backbone:** `raw/`, `wiki/`, the templates
   ([`wiki/_templates.md`](wiki/_templates.md)), the workflow manual
   (`wiki/_operations.md`), the index-shape guide (`wiki/_shape.md`), and
   [`tools/wiki_lint.py`](tools/wiki_lint.py).
2. **Swap the domain framing** in [`AGENTS.md`](AGENTS.md) - the "Domain
   Purpose" and "Source Posture" sections - for your corpus.
3. **Reset content:** clear the `wiki/` content pages (keep `index.md`,
   `log.md`, and the `_*.md` system files), and drop your sources into `raw/`.
4. **Compile:** run an `ingest` per source, let the graph compound, and run the
   linter after structural changes.
5. **Escalate only on demonstrated failure:** add search, digests, claim IDs, or
   graph tooling when the plain markdown baseline actually breaks down - see the
   complexity budget in [`DESIGN.md`](DESIGN.md).

The atlas layer (`public-atlas/`) is optional: build it only if your corpus
deserves a human-readable reading edition on top of the agent-facing wiki.
