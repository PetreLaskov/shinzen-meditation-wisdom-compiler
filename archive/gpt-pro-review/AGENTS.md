# Agentic Knowledge Compiler

You are not maintaining a wiki as an archive. You are maintaining the wiki as
your durable working memory: the current best compiled understanding future
agent instances must think from, including its uncertainty, contradictions,
source frames, open questions, and reusable analyses. Raw sources remain
immutable evidence; the wiki is the agent-maintained compiled layer. The
central product is not page count or source coverage. The central product is
better future judgment.

The central invariant is:

> Maximize future practice-reasoning quality, phenomenological
> discrimination, and transmission fidelity per token loaded, while keeping
> claims calibrated.

Route before reading. Cite load-bearing claims. Keep the primitive layer
simple. Improve durable artifacts instead of letting useful answers die in
chat.

## Domain Purpose

This instantiation compiles Shinzen Young's meditation practice and
contemplative-wisdom system into a durable working model for future practice
reasoning. Prioritize practice handles, phenomenological distinctions,
technique routing, teaching moves, transformation mechanisms,
safety/service boundaries, and source-use tiers. Treat empirical, clinical,
metaphysical, scientific, and comparative claims as calibrated extensions,
not as the center of the work.

Do not treat the wiki as a general Buddhism encyclopedia, Shinzen biography
archive, transcript archive, clinical guide, or comparative religion survey
except where those frames materially clarify Shinzen's teaching system.

Prefer Shinzen-load-bearing mechanism pages over generic Buddhist-term pages.
Do not create a page for every tradition, person, or technical term unless it
changes interpretation of Shinzen's system.

## First Read

At the start of each material session, keep the startup load lean:

1. Read `wiki/index.md` for routing and current shape. When the index is
   large, read the opening through `Open Questions` first, then use headings,
   search, and targeted domain sections instead of loading every page entry.
2. Skim recent `wiki/log.md` entries only. Do not load the full append-only
   log unless the task is historical audit.
3. Read `wiki/_operations.md` when a workflow is in scope.
4. Read `wiki/_templates.md` before creating pages.
5. Read raw sources only when the task requires source-level evidence.

For Shinzen YouTube lectures, read `wiki/_yt_lecture_ingest.md`, then read
only the current-position, canonical-path, gate-rule, relevant-gate, and
output-contract sections of `wiki/_yt_ingestion_implementation_plan.md`
unless the task is to review the plan itself.

Descent order: index opening -> index entry or search result -> frontmatter
-> opening/card -> relevant body sections -> raw source. Skip levels only
when the task explicitly targets that level.

## Bootstrap Orientation

Until this wiki has its own `[[Current Model]]`, read
`raw/Shinzen Sources/Previous wiki compiler - current_model.md` after
`wiki/index.md` and `wiki/log.md` for domain orientation. Treat it as
inherited synthesis and routing context, not primary evidence. Do not cite it
as load-bearing support for Shinzen claims unless the claim is explicitly
about the previous compiler's state.

## Layout

- `raw/` - immutable input sources. Read only.
- `raw/assets/` - binaries referenced by raw source stubs.
- `raw/README.md` - source intake rules.
- `wiki/` - compiled markdown pages. Content pages stay flat.
- `wiki/index.md` - first-read routing surface.
- `wiki/log.md` - append-only operation chronology.
- `wiki/_*.md` - system files: templates, operations, shape guidance.
- `tools/wiki_lint.py` - dependency-free structural invariant checker.
- `tools/wiki_lint.cmd` - Windows helper that uses bundled Python when
  `python` is not on PATH.
- `commands/` - agent-neutral playbooks for the major modes.

## Workflow Authority

`AGENTS.md` is the concise operating contract. `wiki/_operations.md` is the
canonical workflow manual. `commands/` are adapters and must not introduce
behavior that contradicts `_operations.md`.

## Frontmatter

Every compiled page in `wiki/` has YAML frontmatter:

```yaml
---
type: source | entity | concept | thesis | synthesis | analysis | question
thesis: "Single sentence claim plus significance."
status: seed | working | mature | evergreen
domain: [primary, secondary]
importance: 5
confidence: established | probable | speculative | contested
tags: []
aliases: []
sources: [raw/source.md]
load_when: "Questions or tasks that should route here."
best_linked_pages: ["[[Page A]]", "[[Page B]]"]
updated: YYYY-MM-DD
---
```

- `thesis` is a claim, not a topic label.
- `status` tracks development: `seed`, `working`, `mature`, `evergreen`.
- `importance` is 1-10, relative to the wiki's purpose.
- `confidence` is calibrated to evidence, not polish.
- `domain` organizes the index.
- `tags` are analytical facets, not domains, types, or statuses.
- `aliases` resolve alternate link names.
- `sources` lists raw files. Pure synthesis may use `sources: []` only when
  the body explicitly names its compiled-page dependencies.
- `load_when` is the first-pass routing cue future agents should use before
  reading the body.
- `best_linked_pages` lists the highest-value semantic neighbors as quoted
  wikilinks; the body `Related` section keeps the reasons.
- `updated` is the last meaningful revision date.

Do not add schema fields unless they improve future routing or audit value.

## Page Types

- `source` - one-to-one interface between a raw file and the compiled wiki;
  source pages must include `Weakest Claims`, `Important Omissions`, and
  `Contradictions/Tensions` as audit sections, plus a `Model Delta` section
  that states what the source changed, confirmed, challenged, or failed to
  change.
- `entity` - a real-world thing: person, organization, system, project,
  place, event, dataset, product, or institution.
- `concept` - a reusable abstraction, mechanism, distinction, pattern, or
  term.
- `thesis` - an argued position with support, counter-considerations,
  confidence, and evidence that would change the model.
- `synthesis` - a map of a domain or cluster with a real through-line.
- `analysis` - a reusable answer to a query, comparison, or investigation.
- `question` - a durable open frontier, gap, or unresolved contradiction.

Use these seven types unless they genuinely fail.

## Current Model Convention

When enough evidence exists to justify a domain-level best understanding,
create or update `[[Current Model]]` as a normal `type: synthesis` page. Do
not add a new page type or create it before the wiki has a real model to
compress. This page should state what the wiki currently believes, why, the
strongest tensions, and what evidence would change the model.

## Page Shape

Pages use progressive disclosure:

1. Frontmatter: maximum compression.
2. Opening: one or two sentences of context and central claim.
3. `## Key Points`: skimmable decision surface.
4. Body: full reasoning, evidence, boundaries, tensions, and citations.
5. `## Related`: durable semantic edges with a reason.

Finished pages should expose their relevance in the first 30 to 60 lines.
`load_when` and `best_linked_pages` carry frontmatter routing; do not
duplicate them as body bullets. Short pages may collapse the card into three
dense bullets. Mature pages should usually include:

```markdown
## Key Points
- **Core claim**: ...
- **Why this matters**: ...
- **Key tensions**: ...
- **Source posture**: ...
```

## Page Creation

Create a page when it will improve future routing, explanation, synthesis,
contradiction handling, or reuse. Good triggers:

- The subject will recur across sources or queries.
- It carries an independent model, mechanism, entity, thesis, or question.
- It preserves a recurring Shinzen-specific teaching handle, idiolect, or
  practice distinction that improves future practice reasoning.
- It prevents an existing page from doing multiple durable jobs.
- It clarifies a contradiction or frontier.
- It creates a stable target for future links.

Do not create a page just because a noun appeared. Do not bury a recurring
idea in a source page if a useful stub would route better. When uncertain
between one bloated page and two coherent linked pages, prefer the split.
Prefer Shinzen idiolect that routes practice over generic Buddhist or
scientific terminology when the local phrase is doing the real teaching work.

## Links And Citations

Links are semantic edges, not mentions. Link when reading the target would
materially change interpretation of the current page.

Use links for conceptual dependency, contradiction, evidence relationships,
adjacent mechanisms, cross-domain analogy, and durable entity/concept/thesis
relationships. Avoid linking every named entity or repeating the same target
throughout a page.

Every load-bearing claim must trace to a source page or be explicitly marked
unsupported, speculative, or inferred. Source pages should use local claim IDs
such as `S1`, `S2`, `S3` once a source is dense or contested.

Contradictions are preserved, not smoothed. Attribute both sides, mark central
disagreement as `confidence: contested`, and create or update a `question`
when the wiki lacks enough evidence to resolve it.

## Source Posture

Sources are evidence, not authorities. Do not inherit a source's frame as the
wiki's frame. Separate observed facts, source claims, source interpretations,
agent inferences, omissions, incentives, and rival explanations.

For Shinzen primary teachings, treat the source as authoritative evidence for
how Shinzen teaches, routes, and frames his own system. Do not flatten master
instruction into generic propositions. Preserve what the teaching asks a
practitioner to notice, do, stop doing, or re-understand. Separately
calibrate claims about objective science, medicine, metaphysics, history, or
other traditions.

When source agendas or institutional contexts affect interpretation, record
that pressure directly. Do not launder stakeholder claims, consensus language,
or confident rhetoric into established wiki claims without evidence.

## Modes

Run one primary mode per turn:

- `ingest` - raw source to source page plus warranted derived pages.
- `query` - answer from the compiled wiki first; file reusable answers.
- `synthesize` - create a synthesis or thesis from existing pages.
- `lint` - run `python tools/wiki_lint.py` or `tools\wiki_lint.cmd`, then
  add semantic review.
- `review` - inspect health, debt, graph quality, questions, and index shape.
- `refactor` - split, merge, rename, or move pages.

If a request is ambiguous, name the mode you would run and ask one focused
question. If clear, do the work.

## Ingest

1. Read `AGENTS.md`, the routing-relevant portions of `wiki/index.md`, and
   recent `wiki/log.md` entries only. For Shinzen YouTube lectures, also read
   `wiki/_yt_lecture_ingest.md` and the relevant sections of
   `wiki/_yt_ingestion_implementation_plan.md`.
2. Read the source fully enough to produce a faithful source page.
3. Extract claims, evidence, source frame, weakest claims, important
   omissions, contradictions/tensions, and, for teaching talks, the teaching
   register, practice handles, live routing moves, and idiolect worth future
   reuse.
4. Create exactly one source page for each substantive raw file.
5. Create or update concept/entity/thesis/question pages only when warranted.
6. Update semantic `Related` edges.
7. Update `wiki/index.md` and append one `wiki/log.md` entry.
8. Run `python tools/wiki_lint.py` or `tools\wiki_lint.cmd`.

## Query

Use the compiled wiki first. Read raw sources only when compiled pages are
insufficient, stale, contested, or provenance is the question.

A reusable answer should not die in chat. If a query resolves a recurring
question, compares durable concepts, changes confidence, exposes a gap, or
creates a reusable explanation, file it as `analysis`, `thesis`,
`synthesis`, or `question` unless edits are disallowed. If edits are
disallowed, name the durable artifact it would deserve.

If the wiki should be able to answer but cannot, treat that as knowledge:
create or update a `question` page when edits are allowed, or surface the
missing frontier explicitly.

## Corrections

When the user corrects the agent, treat the correction as durable evidence
about the system. Ask what page, assumption, preference, question, or workflow
should change so the same mistake is less likely later.

If the correction affects only the current answer, acknowledge it. If it
affects future reasoning, update the relevant wiki artifact and log the
change when edits are allowed.

## Lint

`tools/wiki_lint.py` enforces mechanical invariants. On this Windows/Codex
workspace, `tools\wiki_lint.cmd` finds the bundled Python runtime when
`python` is not on PATH.

- Required frontmatter exists and enum values are valid.
- Frontmatter routing fields exist and `best_linked_pages` resolve.
- Links resolve to page filenames or aliases.
- Every raw source has exactly one source page.
- Every compiled page appears in `wiki/index.md`.
- Non-source pages cite raw sources unless explicitly pure synthesis.
- Dates are ISO formatted and source-backed pages are not stale.
- Source pages include the required audit sections: `Weakest Claims`,
  `Important Omissions`, and `Contradictions/Tensions`.

Agent review still handles judgment-heavy checks: weak theses, link spam,
page bloat, contradiction smoothing, uncited load-bearing claims, vague index
entries, and pages doing too many jobs.

## Index

`wiki/index.md` must remain skim-readable. It contains:

- Shape paragraph: scope, through-line, maturity, next leverage.
- Recent shape changes: 3 to 5 entries that affect routing, scope, open
  questions, or maintenance priority.
- Operating dashboard: source backlog, page counts, epistemic debt, next
  step.
- Open questions: top active frontiers.
- Domain sections: page entries grouped by primary domain.

The index is a routing surface, not a full chronology or source catalog. If
page-registration rules pressure the index to become unreadable, prefer a
refactor of the registration/catalog mechanism over adding more startup
bulk.

Entry shape:

```markdown
- [[Page]] - thesis or card-level one-liner (importance, status, confidence)
```

## Log

`wiki/log.md` is append-only, newest first:

```markdown
## [YYYY-MM-DD] op | Subject
Summary of what changed. Pages touched: [[P1]], [[P2]]. Assumptions, open
issues, validation notes, or deferred work when they matter.
```

Use one entry per session-bounded operation. Do not dump chat history. During
startup, read only the newest relevant entries unless the task is log audit.

## Voice

Wiki prose is third person, calibrated, direct, and source-grounded. Avoid
maintenance prose inside content pages. Avoid hedge stacking. Do not import
the compiler metaphor into domain pages. Earn every wikilink. Attribute
claims directly and mark uncertainty where it changes interpretation.

## Final Rule

Each material session should leave the wiki more grounded, navigable,
compressed, honest, or generative. If a change does none of those, do less.
