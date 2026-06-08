# Operations

Extended playbooks for the Knowledge Compiler. `AGENTS.md` is the operating
contract; this file is the canonical workflow manual. `commands/` are
adapters and must not introduce behavior that contradicts this manual.

## Context Hygiene

Startup context is a scarce resource. The goal is to load the best routing
surface, not every recent fact.

- Treat `wiki/index.md` as a map. Start with the opening through `Open
  Questions`, then jump by headings, search, frontmatter, or domain entry.
- Treat `wiki/log.md` as append-only evidence. For normal startup, read only
  the newest relevant entries, roughly the first 80-140 lines or matching
  headings. Load the full log only for historical audit.
- For YouTube ingestion, read `wiki/_yt_lecture_ingest.md` plus only the
  current-position, canonical-path, gate-rule, relevant-gate, and
  output-contract sections of `wiki/_yt_ingestion_implementation_plan.md`.
- Read page frontmatter and the opening/card before full bodies. If
  frontmatter has become a manifest, use the opening and `## Key Points`,
  then leave a refactor note.
- Prefer `rg` and heading scans for discovery over loading broad files into
  chat context.
- When updating system files, remove obsolete chronology instead of copying
  the same status into index, log, plan, and owner pages.

## Ingest

Ingest turns a raw source into durable compiled wiki value.

### Route

1. Read `AGENTS.md`.
2. Read the routing-relevant portions of `wiki/index.md`.
3. Skim recent entries in `wiki/log.md`; do not load the full log unless the
   operation is log audit.
4. Inspect likely page frontmatter, especially `load_when` and
   `best_linked_pages`, before reading full bodies.
5. Treat frontmatter as a triage card. If `load_when`, `best_linked_pages`,
   `aliases`, or non-source `sources` have become exhaustive maps, route from
   the opening and `## Key Points` instead and leave a refactor note.
6. Identify affected source, entity, concept, thesis, synthesis, analysis,
   and question pages.

### Read Source

Read the source fully enough to produce a faithful source page. Extract:

- Source claims.
- Observations versus inferences.
- Evidence and examples.
- For Shinzen primary teaching talks: teaching register, practice handles,
  live routing moves, phrases or idiolect worth preserving, and what the talk
  asks a practitioner to notice, do, stop doing, or re-understand.
- Source frame, agenda, discipline, incentives, and omissions.
- Model delta: what the source confirms, changes, challenges, or fails to
  change in the current wiki model.
- Practice delta: what the source sharpens in technique choice,
  phenomenology, coaching, safety, service, or transmission.
- Weakest claims that should not be overpromoted.
- Important omissions that change interpretation.
- Contradictions or tensions with the source itself or existing pages.
- Reusable entities, concepts, theses, or questions.

### Allocate Pages

Always create or update exactly one `source` page for a substantive raw file.

Create derived pages only when they improve future routing, explanation,
synthesis, contradiction handling, or reuse. Prefer a useful stub over
burying a recurring idea. Prefer a richer existing page over a noun page.

Create a `synthesis` only when a real through-line is visible. If no
through-line exists, create or update a `question`.

Create or update `[[Current Model]]` only once the wiki has enough evidence
to justify a compact best-understanding page. It remains a normal
`type: synthesis` page, not a new primitive.

### Compile

1. Write or update the source page from `wiki/_templates.md`, preserving the
   required audit sections and a clear `Model Delta`. For practice-heavy
   sources, interpret `Model Delta` as model/practice delta.
   Use the YouTube lecture scaffold in `wiki/_templates.md` and the current
   method note in `wiki/_yt_lecture_ingest.md` when ingesting Shinzen
   teaching transcripts.
2. Integrate important claims into durable pages.
3. Mark contradictions explicitly and preserve both sides.
4. Exclude low-signal material deliberately.
5. Keep frontmatter bounded: one discriminating `load_when` sentence, the
   strongest few `best_linked_pages`, principal raw anchors in non-source
   `sources`, and only true lookup `aliases`.
6. Update `wiki/index.md` entries and dashboard.
7. Append one `wiki/log.md` entry.
8. Run `python tools/wiki_lint.py` or `tools\wiki_lint.cmd`.

## Query

Queries use compiled knowledge first.

1. Read `wiki/index.md`.
2. Choose candidate pages by domain, thesis, importance, confidence, and
   frontmatter routing fields.
3. For concrete practitioner reports, route through [[Practice Guidance
   Toolkit]] first. If medical or clinical risk, severe dissociation or void
   distress, self-harm or harm risk, coercive teacher pressure, practice
   worsening, or insight without behavior improvement appears, load
   [[Complete Experience Safety Boundary]] and, for teacher/conduct issues,
   [[Guidance Scope and Accountability Boundary]] before technique
   optimization.
4. Read relevant page bodies.
5. Read raw sources only when compiled pages are insufficient, stale,
   contested, or provenance is the question.
6. Answer with calibrated confidence and citations.
7. If the answer is reusable, file it as `analysis`, `thesis`, `synthesis`,
   or `question`.
8. If the wiki should be able to answer but cannot, treat that as knowledge:
   create or update a `question` page when edits are allowed, or surface the
   missing frontier explicitly.
9. Log only when the wiki changes.

A reusable answer should not die in chat. If a query resolves a recurring
question, compares durable concepts, changes confidence, exposes a gap, or
creates a reusable explanation, file it as `analysis`, `thesis`,
`synthesis`, or `question` unless edits are disallowed. If edits are
disallowed, name the durable artifact it would deserve.

## Synthesize

Synthesis maps a cluster once a through-line has emerged.

Use synthesis when:

- A domain has roughly five or more substantive pages.
- A recurring query now has a durable answer.
- A thesis crystallizes from accumulating evidence.
- Review finds a domain with good pages but no map.

Procedure:

1. Pull relevant page cards and bodies.
2. Name the through-line in one sentence.
3. Stop if the result is only a page list.
4. Write a synthesis with landscape, through-line, tensions, dependencies,
   and related pages.
5. Add semantic Related edges on touched pages.
6. Update index and log.
7. Run lint.

## Lint

Run:

```bash
python tools/wiki_lint.py
```

On this Windows/Codex workspace, `tools\wiki_lint.cmd` uses the bundled
Python runtime when `python` is not on PATH.

The script enforces mechanical checks:

- Frontmatter required fields and enum values.
- Frontmatter routing fields and `best_linked_pages` resolution.
- Link resolution against filenames and aliases.
- Raw source coverage by exactly one source page.
- Registration for every compiled page through `wiki/index.md` or approved
  catalog surfaces such as `wiki/_page_catalog.md`.
- Source references exist.
- Oversized routing frontmatter is surfaced as an advisory diagnostic.
- Dates are valid and source-backed pages are not stale.

After the script, add semantic diagnostics:

- Orphan pages.
- High-importance stubs.
- Pages doing multiple jobs.
- Bloated pages that should split.
- Topic-label theses.
- Link spam.
- Smoothed contradictions.
- Uncited load-bearing claims.
- Source pages missing frame, integration notes, or required audit sections.
- Source pages missing a clear model delta.
- Shinzen teaching talks flattened into generic propositions without
  preserving practice handles, teaching moves, or useful idiolect.
- Index entries too vague to route.
- Frontmatter doing the job of a whole map instead of a routing card.

Surface findings. Do not auto-fix broad structural issues during lint.

## Review

Review is periodic maintenance. Run every few dozen ingests, when the wiki
feels structurally off, or when the user asks.

Checklist:

- Orphans and weak inbound links.
- Duplicate pages and near-synonyms.
- High-importance `seed` pages.
- Pages over roughly 600 to 900 words with visible internal divisions.
- Source pages not integrated anywhere.
- Stale pages affected by recent ingests.
- Singleton or over-broad tags.
- Domains swelling without syntheses.
- Contested pages that no longer preserve both sides.
- Questions that should become analyses or theses.
- Analyses that should become syntheses.
- Shape paragraph drift.

Review may safely fix small local issues. Large refactors should leave a
review note, old-to-new mapping, and validation plan.

## Refactor

Refactor changes wiki structure.

### Split

Split a page when it is doing multiple durable jobs or has grown too large
for one coherent thesis.

1. Identify the boundary.
2. Create one or more pages with independent theses.
3. Move content and tighten each page.
4. Preserve or replace the original as appropriate.
5. Update inbound links, index entries, related sections, and log.
6. Run lint.

### Merge

Merge pages when they express the same model under different names.

1. Pick the canonical title.
2. Merge evidence without smoothing contradictions.
3. Add the old title to `aliases:`.
4. Update links when practical.
5. Update index and log.
6. Run lint.

### Rename

Rename when the page name no longer fits the content.

1. Rename the file.
2. Add the old title to `aliases:`.
3. Update inbound links.
4. Update index and log.
5. Run lint.

If a refactor touches more than five content pages, make it legible with a
clear mapping and validation note.

## Lifecycles

- `seed`: valid stub with routing value.
- `working`: enough body, evidence, and links to answer adjacent questions.
- `mature`: evidence, boundaries, and links have survived review.
- `evergreen`: stable entry point unlikely to shift without major sources.

Demotion is healthy when new evidence weakens a page.

Questions progress from open to partial to resolved. Resolved questions stay
as history and link to the resolving page.

Contradictions preserve both claims, cite both sides, mark affected pages
`contested` when central, and often create or update a `question`.

## Style

The wiki voice is third person, calibrated, direct, and source-grounded.

Use these corrections:

- Lead with the claim, not the classification.
- Hedge once, with intent.
- Keep maintenance prose out of content pages.
- Strip compiler workflow vocabulary from domain prose.
- Use contrast only when the misconception is real.
- Prefer direct attribution over vague framework language.
- Name missing evidence instead of saying uncertainty remains.
- Earn every wikilink.
- Preserve Shinzen's local practice language when it performs a teaching
  function; translate it only after the local handle is clear.

After drafting a page, scan for:

- "the wiki should" or "this page should"
- stacked hedges
- passive uncertainty with no named missing evidence
- five-item comma chains
- repeated links to the same target
- thesis sentences that are only topic labels
- uncited load-bearing claims
- master instruction reduced to abstract epistemic summary

## Tag Governance

Tags are analytical facets. They are not domains, types, statuses, or personal
bookkeeping.

- Do not introduce a singleton tag unless at least one other page could
  plausibly use it soon.
- Retire singleton tags during review if they never earn reuse.
- If a tag appears on more than 40 percent of pages, it is probably a domain
  or too broad to help.
- Keep tags sparse. More than five tags usually means the page is doing too
  many jobs.

## Index Scaling

Keep the main index readable at every scale.

- Under 50 pages: flat domain sections.
- 50 to 200 pages: add domain abstracts.
- 200 to 500 pages: domain syntheses or catalog surfaces carry full page
  lists; the main index routes to them and keeps only the highest-value
  entries.
- Above 500 pages: add generated system sub-indexes under `_indexes/` only
  when the main index can no longer route cleanly.

Do not add folders for content pages until the flat model fails in practice.
