# Post-Ingest Knowledge Health And Refactor Plan

Created 2026-05-16 after completion of the substantive canonical YouTube
transcript-video ingest set.

This is a system plan, not a Shinzen content page. It should guide review,
refactor, synthesis, catalog, and lint work after the transcript-ingest era.
Do not cite it as evidence for Shinzen claims.

## Purpose

The wiki's next constraint is no longer source coverage. The next constraint
is durable compiled knowledge health: future agents need cheaper first loads,
clearer progressive disclosure, better domain routing, less redundant prose,
and smaller pages that preserve phenomenological and practice distinctions
without forcing every answer through a monolith.

The governing objective remains:

> Maximize future practice-reasoning quality, phenomenological
> discrimination, and transmission fidelity per token loaded, while keeping
> claims calibrated.

This plan treats refactor work as context engineering. The goal is not to make
the wiki prettier. The goal is to make future agents load the right amount of
knowledge at the right time, know when to descend for more detail, and avoid
overconfident answers from partial context.

2026-05-16 context-engineering update: Anthropic's engineering posts on
effective context engineering and managed agents sharpen the plan's local
meaning of "health." Treat the wiki as a long-term memory system with several
context interfaces: durable evidence, compact working context, just-in-time
retrieval surfaces, and compaction artifacts. The refactor should therefore
optimize not only page shape, but also what enters a future agent's active
context window, when it enters, and what can remain discoverable without being
loaded by default.

## Current Baseline - 2026-05-16

Mechanical lint passes.

Known baseline:

- 298 compiled pages.
- 223 source pages.
- 58 concept pages.
- 9 synthesis pages.
- 7 question pages.
- 1 thesis page.
- 2 remaining raw backlog diagnostics under current lint rules:
  `IntroToUltra_ver4.8.pdf` and the plan-skipped duplicate welcome transcript.
- Large domain diagnostics remain: `sources`, `practice`, `primary`,
  `transformation`, `safety`, `teaching`, and `service`.
- `wiki/index.md` opening through the first domain section is about 11,219
  characters, still within lint target but too chronology-heavy for the
  post-ingest stage.
- Source-heavy non-source frontmatter advisories remain on key owner pages.
- Largest non-system content pages by line count include:
  [[Current Model]], [[Expansion And Contraction]],
  [[Flow]], [[Complete Experience]],
  [[No-Self And Personality]], [[Lineage Translation]],
  [[Insight and Purification]], [[Shinzen's Teaching Method]],
  [[Nurture Positive]], [[Guidance Scope and Accountability Boundary]], and
  [[Altered Phenomena and Dissolution Safety Boundary]].

Interpretation:

- The source layer is broad enough to support real synthesis.
- The compiled layer is still shaped by ingest chronology.
- Several high-importance pages are acting as owner page, synthesis page,
  evidence map, router, safety warning, and source catalog at once.
- The main index is still carrying too much page registration and chronology
  load.
- The wiki needs domain sub-indexes, hub-and-child concept structure, and
  route-tested page decomposition.

## Success Criteria

The refactor succeeds when a future agent can:

- Load `wiki/index.md` and know the next one to three pages to inspect for
  common tasks.
- Use hub pages as decision surfaces instead of mini-books.
- Descend from a hub into a child page only when the task requires that level
  of detail.
- See, beside each child link, why loading that child changes the decision.
- Distinguish source evidence, compiled synthesis, safety frontier, and
  speculative extension without reading every source page.
- Answer practitioner-routing questions with safety posture visible before
  technique optimization.
- Find full page and source registration without bloating the startup index.
- Preserve contradictions and uncertainty while reducing repeated summary
  prose.
- Measure whether each refactor reduces wasted context without reducing
  recall of evidence, safety boundaries, practice handles, and uncertainty.

## Operating Principles

- **Router first**: a hub page should answer "what should I load next?" before
  it answers the whole domain.
- **Progressive disclosure**: the first 30 to 60 lines of important pages must
  expose the page's claim, use case, confidence, safety posture, and next-load
  map.
- **Decision relevance**: every child link on a hub should say what decision,
  distinction, or risk it helps resolve.
- **Split by durable job**: split when sections serve different future tasks,
  not merely because a page is long.
- **Preserve source fidelity**: do not compress away teaching moves, practice
  handles, idiolect, contradictions, or source posture.
- **Safety overrides elegance**: never shrink or split a page in a way that
  makes medical, clinical, teacher, conduct, or destabilization boundaries
  harder to notice.
- **Flat files, conceptual nesting**: content pages remain flat in `wiki/`;
  nesting is expressed by hub pages, child-page names, `load_when`, and
  decision tables.
- **No bulk rewrites**: one coherent batch at a time, with old-to-new mapping,
  lint, and a log entry.
- **No orphan details**: moved material must retain citations, related links,
  and a clear route back to the hub.
- **Durable record, lean working context**: logs, source pages, raw sources,
  and catalogs preserve the record; index pages, hub cards, frontmatter, and
  decision maps decide what should enter active context now.
- **Recall before compression**: make pages shorter only after preserving
  source posture, contradictions, safety boundaries, claim support, practice
  handles, and old-to-new mappings.
- **Just-in-time descent**: expose enough signal for agents to know when to
  load a child page, source page, or raw source, and when not to.

## Context Budget Rubric

Every hub, child page, catalog, and index section should justify its context
cost. During router benchmarks and refactor reviews, record:

- pages loaded before a confident answer;
- approximate lines or tokens loaded;
- which loaded context changed the answer;
- which loaded context was merely reassuring, duplicated, chronological, or
  non-decision-relevant;
- what should have been loaded earlier but was hidden too deeply;
- whether safety and source posture appeared before advanced interpretation;
- whether the hub's descent triggers made sibling pages unnecessary to load.

A page is bloated when future agents must load many tokens whose marginal
decision value is low for the task that routed there. A page is underbuilt
when it is short but forces agents into broad search, source re-reading, or
overconfident inference.

## Just-In-Time Retrieval Protocol

Default descent order for review, refactor, and query work:

1. `wiki/index.md` route.
2. Hub frontmatter, opening, and `## Key Points`.
3. Hub decision map or child-link table.
4. The relevant child page only.
5. Source page claim IDs and integration notes.
6. Raw source only when provenance, uncertainty, contradiction, or source
   framing requires it.

Do not load sibling child pages merely because they exist. Hubs should expose
enough decision signal for agents to know when a child page is unnecessary.
Search with `rg` before broad reading when the likely answer is a phrase,
claim ID, page title, or link neighborhood.

## Refactor Compaction Contract

When compressing or splitting a page, preserve recall before optimizing
brevity.

A refactor must retain:

- all load-bearing claims;
- source posture and claim IDs;
- contradictions and open questions;
- safety boundaries and stop criteria;
- practice handles, teaching moves, and Shinzen idiolect;
- parent-child navigation and old-to-new mapping;
- evidence that would change the model or lower confidence.

Only after recall is secured should repeated summaries, source chronology,
duplicated mechanism prose, and non-decision prose be removed. The failure
mode to avoid is a page that is cleaner but makes future reasoning less
faithful.

## Goldilocks Altitude For Hubs

Hub pages should avoid two opposite failures:

- **Too abstract**: the hub gives a definition but no routing decisions,
  safety posture, evidence tier, or descent criteria.
- **Too exhaustive**: the hub front-loads every source, caveat, and edge case
  before the agent knows which branch matters.

The right altitude is a compact decision surface with enough mechanism,
guardrail, and child-link information to guide the next load. The hub is not a
miniature version of every child page.

## Page Roles

### Hub Or Index Page

A hub page is the canonical first load for a concept or domain. It should be
short enough to scan and strong enough to route.

Target shape:

- Frontmatter with a discriminating `load_when`.
- Opening claim.
- `## Key Points`.
- `## Decision Map` or equivalent table.
- Compact mechanism summary.
- Safety/source posture.
- Links to child pages with decision-relevant annotations.
- `## Related` with reasons.

Target size:

- Usually 80 to 180 lines.
- Up to about 220 lines for load-bearing router pages.
- If the hub needs more, it probably needs child pages.

### Child Page

A child page owns one durable subjob: a mechanism, distinction, practice
handle, safety differential, teaching move, evidence tier, or recurring
question.

Target shape:

- Independent thesis.
- Specific `load_when`.
- Clear parent link in opening or `Related`.
- Enough evidence to stand alone.
- No duplicated mini-version of the whole parent.

Target size:

- Usually 80 to 250 lines.
- Larger only when the page itself is a synthesis or safety boundary with a
  real internal map.

### Source Page

Source pages remain one-to-one interfaces to raw files. Do not split source
pages simply to reduce size. Improve their opening, key points, claim IDs,
integration notes, and audit sections if needed, but keep the source
interface stable.

### System Catalog

System catalogs carry registration, source lists, and mechanical navigation
that should not burden startup context. They may live in underscore files
such as `_page_catalog.md` or `_sources_catalog.md`. They are not evidence for
Shinzen claims.

Catalogs should be stable interfaces, not only lint workarounds. Future
agents should be able to ask "where is the exhaustive register?" and "where is
the first-load router?" without knowing the current implementation details of
`tools/wiki_lint.py`.

## Decision-Relevant Link Pattern

Hub pages should prefer tables like this:

| If the task asks about... | Load | Why it changes the answer | Guardrail |
| --- | --- | --- | --- |
| Generating, losing, or repairing equanimity in a live report | `[[Equanimity]]` or a child page | Chooses intentional support, spontaneous drop, second-order fallback, or method change | Do not confuse equanimity with numbness, compliance, dissociation, or endurance |
| Whether a no-self or void report is liberating or destabilizing | `[[DPDR and the Pit of the Void]]` | Forces valence, function, support, and clinical-differential checks | Do not route distress through enlightenment maps first |
| Whether Source language is practice, metaphysics, or science claim | `[[Source And Polarities]]` or a child page | Separates afterglow, Zero, polarities, metaphor, and speculation | Do not turn math or physics analogies into established evidence |

Every major hub should eventually include this pattern or a close equivalent.

## Equanimity Pilot Pattern

Status: completed 2026-05-16.

The user's suggested "Equanimity index" is the right pattern. [[Equanimity]]
does not need to be huge before it deserves hub treatment, because it is a
central routing concept and a safety-sensitive practice handle.

Candidate hub outcome:

- [[Equanimity]] becomes the first-load page for what equanimity is, why it
  matters, how it interacts with concentration and clarity, and where to go
  next.
- Existing source pages remain source pages.
- New or strengthened child pages may be created only if each owns a real
  decision job.

Candidate child jobs:

- `Equanimity - Intentional And Spontaneous`: when to relax, welcome, accept,
  or wait for spontaneous dropping.
- `Second-Order Equanimity`: what to do when equanimity itself cannot be
  generated and tension or judging becomes the object.
- `Equanimity Versus Suppression`: safety differential for numbness,
  compliance, endurance identity, bypass, dissociation, or teacher pressure.
- `Equanimity In Pain And Strong Determination`: how equanimity functions
  under intensity without making intensity the criterion.
- `Equanimity And Purification Taste`: how equanimity becomes motivational
  feedback without becoming state chasing or proof of attainment.

The hub's child-link table should tell agents when each child changes the
decision, not merely list subtopics.

## Phase 0 - Post-Ingest Baseline And Freeze

Status: ready.

Goal: prevent ingest momentum from hiding the new maintenance priority.

Steps:

1. Treat substantive canonical YouTube transcript-video ingest as complete.
2. Keep `IntroToUltra` and the duplicate welcome transcript out of the main
   work queue unless a query or route audit proves they matter.
3. Record current lint diagnostics, largest-page candidates, domain pressures,
   and index opening size.
4. Update stale plan surfaces that still recommend gate-order ingestion.

Output:

- This plan.
- A log entry.
- Lint validation.

## Phase 1 - Post-Ingest Router Benchmark

Status: initial benchmark completed 2026-05-16. See
`wiki/_post_ingest_router_benchmark_2026-05-16.md`.

Goal: test the wiki as future agents will use it before splitting pages.

Run 12 to 16 representative queries:

1. Strong physical pain in sitting.
2. Emotional eruption and fear during noting.
3. No-self, paper-thin world, void, or DPDR-like distress.
4. Which Shinzen method should be used first.
5. Whether Source is literally real or scientifically supported.
6. Teacher pressure, charismatic authority, or suspect behavior.
7. Practice feels profound but behavior is not improving.
8. Retreat aftershock, sleep disruption, or practice intensity spillover.
9. Sexuality, birth, illness, caffeine, or dream practice as applied domains.
10. Equanimity cannot be generated.
11. Flow, Gone, spaciousness, or Expansion-Contraction is reported.
12. Positive practice exposes fear or sadness.
13. A source provenance question asks where a claim came from.
14. A future agent asks what to load for a domain overview.
15. A future agent asks whether a page should be split.
16. A query needs a concise current whole-system model.

Record:

- first page loaded;
- second page loaded;
- whether safety/source posture appears early enough;
- whether the agent must load too much to answer;
- whether a child page, domain index, or hub table would reduce load;
- whether overclaim risk appears;
- context cost: pages, lines, or rough token load needed for the answer;
- wasted context: what was loaded but did not change the answer;
- missed context: what should have been loaded earlier;
- descent trigger quality: whether the hub made the next load obvious;
- compaction opportunity: what repeated prose, chronology, or source list
  could be moved, summarized, or cataloged.

Output:

- A benchmark section in this plan or a new dated review note.
- Ranked list of the first five refactors by expected routing gain.

## Phase 2 - Registration And Catalog Architecture

Status: initial architecture completed 2026-05-16.

Goal: let `wiki/index.md` become a router without violating page-registration
invariants.

Problem:

The current lint model pressures every compiled page to appear in
`wiki/index.md`. That keeps registration simple, but it makes the index behave
like an archive.

Preferred solution:

1. Create a system page register, likely `wiki/_page_catalog.md`.
2. Optionally create `wiki/_sources_catalog.md` for full source-page
   registration and source-cluster routing.
3. Update `tools/wiki_lint.py` so compiled pages may be registered in
   `wiki/index.md` or approved catalog files.
4. Keep `wiki/index.md` responsible for first-load routing, dashboard, open
   questions, and top domain hubs.
5. Keep domain and source catalogs responsible for exhaustive listings.

Validation:

- Lint still catches unregistered compiled pages.
- `wiki/index.md` can drop long source/domain lists without hiding pages.
- Startup load decreases.
- The catalog/register layer preserves exhaustive discoverability while the
  index remains a first-load router.

Stop condition:

- If the lint change becomes complex, do not move domain lists yet. Keep the
  main index intact until registration remains mechanically safe.

Implementation note - 2026-05-16:

- Created `wiki/_page_catalog.md` as the exhaustive compiled-page registration
  catalog, grouped by primary domain and carrying page type, importance,
  status, confidence, and thesis for each compiled page.
- Updated `tools/wiki_lint.py` so compiled pages may be registered through
  `wiki/index.md` or approved catalog files (`wiki/_page_catalog.md` and
  `wiki/_sources_catalog.md` when present).
- Repaired `tools/wiki_lint.cmd` so invariant errors from Python lint runs
  propagate as command failures.
- Slimmed only `## Domain: Sources` in `wiki/index.md` as the proof of
  concept, replacing the full source-page archive with first-load source
  routing and a pointer to the catalog.
- Result: the index is 607 lines, and the opening through `Open Questions` is
  about 10,867 characters. Broader startup compression remains Phase 3 work.
- Residual risk: the optional `_sources_catalog.md` does not exist yet, and
  catalog entries are a registration surface, not semantic inbound links or
  evidence citations.

## Phase 3 - Main Index Surgery

Status: completed 2026-05-16.

Goal: make `wiki/index.md` a post-ingest routing surface.

Target index shape:

- Scope paragraph.
- Live guidance safety rule.
- "Load next by task" table.
- Current model pointer.
- Operating dashboard.
- Top open questions.
- Domain hub list, not full page catalog.
- Link to catalog/register surfaces.

Remove or relocate:

- Gate chronology that belongs in log or YouTube plan.
- Long source-page lists.
- Exhaustive domain entries.
- Repeated "recent additions" that no longer affect first-load routing.

Targets:

- Keep the opening through `Open Questions` under about 7,500 characters if
  possible.
- Keep the whole index skim-readable.
- Preserve enough routing information that a future agent does not need to
  search blindly.
- Move durable chronology, exhaustive page registration, and source coverage
  accounting into durable record surfaces rather than the working context
  surface.

Implementation note - 2026-05-16:

- Rewrote `wiki/index.md` around a compact scope statement, live guidance
  safety rule, "Load Next By Task" routing table, current-model pointer,
  operating dashboard, top open questions, curated domain hub lists, source
  routing, and explicit delegation to `wiki/_page_catalog.md` for exhaustive
  registration.
- Removed most gate chronology, repeated recent-addition prose, and exhaustive
  domain lists from the startup surface without changing compiled-page
  registration.
- Result: the index is 330 lines, and the opening through `Open Questions` is
  about 7,090 characters, under the target of about 7,500 characters.
- Validation: `tools\wiki_lint.cmd` passes with 289 compiled pages and only
  the expected raw-backlog, frontmatter-source-count, and large-domain
  diagnostics.

## Phase 4 - Current Model Card

Status: completed 2026-05-16.

Goal: make the whole-system synthesis usable without loading the full
evidence body.

Edit [[Current Model]] first, before broader synthesis splits.

Add a strict `## Current Model Card` near the top:

- one-sentence model;
- 5 to 7 routing rules;
- confidence tiers;
- safety and evidence frontiers;
- what would change the model;
- next-load links for practice, transformation, safety, service, lineage, and
  Source questions.

Then evaluate whether the rest of [[Current Model]] should split into:

- `Current Model - Evidence Base`;
- `Current Model - Transformation Mechanism`;
- `Current Model - Safety And Scope`;
- or another smaller set if router benchmark proves the split is needed.

Stop condition:

- If a card solves the routing problem, do not split the page just because it
  is long.

Implementation note - 2026-05-16:

- Added `## Current Model Card` near the top of [[Current Model]], including
  the one-sentence model, seven routing rules, confidence tiers, safety and
  evidence frontiers, model-change criteria, and next-load links for practice
  architecture, transformation, safety, service/life test, lineage/teaching,
  and Source/polarity/speculation questions.
- Tightened the opening to reflect completed Gates 0-10 and post-Gate-10
  triage without replaying ingest chronology.
- Stop-condition decision: no split was created in this phase. The card now
  handles first-load routing, while the long body remains available as the
  evidence and dependency layer. Reconsider a split only if a later router
  benchmark shows agents still need to load the body for ordinary whole-model
  questions.
- Validation: `tools\wiki_lint.cmd` passes with 289 compiled pages and only
  the expected raw-backlog, frontmatter-source-count, and large-domain
  diagnostics.

## Phase 5 - Monolith Decomposition Pilots

Goal: convert the most expensive owner pages into hub-and-child structures.

Selection criteria:

- page is high-importance and frequently loaded;
- page exceeds about 300 lines or contains several durable jobs;
- page has source-heavy frontmatter or evidence-map bloat;
- page mixes practice routing, mechanism, safety, and speculative extension;
- split would reduce future load without hiding safety or source posture.

Pilot order should be chosen after Phase 1, but the current candidates are:

1. [[Source And Polarities]]
   - likely children: Source/Zero afterglow boundary, polarities and
     Expansion-Contraction, science/mathematics analogy limits, time-space
     speculation, Source in service language.
2. [[Total Happiness]]
   - completed 2026-05-16 as an aim hub with child pages for aim structure,
     condition-independent happiness, and behavior/service verification.
3. [[Equanimity]]
   - completed 2026-05-16 as a hub with child pages for training ladder,
     suppression differential, and purification taste.
4. [[Flow]], [[Gone]], [[Impermanence]], [[Expansion And Contraction]]
   - possible domain index: `Impermanence Practice Index` or similar, with
     Flow, Gone, spaciousness, Expansion-Contraction, bhanga, and Source
     afterglow routed separately.
5. [[Complete Experience]] and [[Insight and Purification]]
   - split mechanism, signs of completion, purification taste, and bypass or
     intensity differentials only if safety visibility improves.
6. [[No-Self And Personality]]
   - likely children: Feel/Image/Talk selfing, witness, no-place-to-stand,
     weak ego versus no-self, healthy personality re-arising.
7. [[Lineage Translation]]
   - likely children: authority/scripture, ritual/mantra, comparative
     religion compatibility, Sasaki/Burmese fusion, science-analogy boundary.
8. [[Shinzen's Teaching Method]] and [[Guidance Scope and Accountability
   Boundary]]
   - split only if teacher/accountability queries still require too much
     loading after safety-index work.

Per-page split workflow:

1. Read frontmatter, opening, key points, headings, related links, and source
   anchor cards.
2. Identify durable jobs currently mixed together.
3. Draft old-to-new mapping before editing.
4. Create only child pages with independent theses and future routing value.
5. Move or summarize detail rather than duplicating it.
6. Make the parent a hub with decision-relevant child links.
7. Update inbound links when the child page is now the better target.
8. Update index/catalog/register surfaces.
9. Append a log entry.
10. Run lint.

Implementation note - 2026-05-16:

- Began Phase 5 with the [[Source And Polarities]] pilot because the router
  benchmark identified it as the highest-gain post-Phase-4 monolith.
- Rewrote [[Source And Polarities]] as a hub with a decision map and bounded
  frontmatter instead of a source-heavy evidence anthology.
- Created three child pages with independent jobs: [[Source Afterglow
  Boundary]] for direct-object and after-representation claims, [[Source
  Science And Analogy Boundary]] for science/mathematics/nature/time-space
  speculation, and [[Source And Service Boundary]] for shared-Source service
  and self-certification risks.
- Updated targeted inbound routes from the altered-phenomena safety page and
  three high-leverage source pages so future agents descend directly to the
  child boundary when afterglow, time-space analogy, complex-number analogy,
  or service claims are the live question.
- Next pilot candidates: an impermanence practice hub/index for Flow, Gone,
  Spaciousness, Expansion-Contraction, bhanga, and Source afterglow; or a
  compact guidance/accountability decision matrix. [[Equanimity]] remains the
  smaller low-risk hub-pattern pilot.

Implementation note - 2026-05-16, impermanence practice index:

- Promoted [[Impermanence Flow Gone And Source]] from compact Gate 4 synthesis
  to the impermanence practice index, with alias support for "Impermanence
  Practice Index."
- Added a decision map that routes ordinary changingness, Flow, Gone,
  Spaciousness, Expansion-Contraction, bhanga, Source afterglow, safety, and
  service claims to their owner pages without loading all siblings.
- Added sibling-load rules so future agents descend only when the live report
  depends on movement/energy, vanishings, Space, force-patterns, bhanga,
  Source object claims, or safety differentials.
- The next major move should shift from Phase 5 pilots toward Phase 6 safety
  criteria unless a route audit identifies another unusually expensive
  monolith.

Implementation note - 2026-05-16, total happiness decomposition:

- Rewrote [[Total Happiness]] as a bounded decision hub instead of a large
  source-heavy aim anthology.
- Created [[Total Happiness Aim Structure]] for the three jobs, four
  quadrants, five applications, ordinary/extraordinary distinction, and
  self/other aim map.
- Created [[Condition-Independent Happiness]] for the CCE-based fulfillment,
  suffering, Don't Know, and complete-sensory-experience mechanism.
- Created [[Total Happiness Behavior And Service Test]] for behavior change,
  external accountability, improve/transcend reinforcement, service, and
  teaching verification.
- Next move should be a concrete Phase 6 safety row unless a route audit
  identifies another unusually expensive monolith.

Implementation note - 2026-05-16, continued:

- Converted [[Equanimity]] into a first-load hub with a decision map for
  practice repair, suppression/numbness differential, purification taste,
  background equanimity, pain/intensity, and safety routing.
- Created [[Equanimity Training Ladder]] for intentional body/talk supports,
  equanimity voice, spontaneous-drop recognition, second-order equanimity,
  and background equanimity.
- Created [[Equanimity Versus Suppression]] for the safety differential
  between noninterference, apathy, stuffing down, identification, calm
  performance, dissociation, passivity, and unsafe endurance.
- Created [[Equanimity And Purification Taste]] for equanimity-as-purifier,
  resistance formulas, reward taste, Strong Determination, kriyas, and
  anti-ascetic limits.
- Phase 5 now has four completed pilots: [[Source And Polarities]],
  [[Impermanence Flow Gone And Source]], [[Total Happiness]], and
  [[Equanimity]]. The best next phase is Phase 6 safety criteria, beginning
  with the row that most often blocks live guidance.

## Phase 6 - Safety Criteria Pass

Goal: turn open safety debt into executable routing.

Starting pages:

- [[Complete Experience Safety Boundary]]
- [[Completion Versus Bypass Safety Boundary]]
- [[Practice Method Safety Boundary]]
- [[Intensity and Embodiment Safety Boundary]]
- [[Altered Phenomena and Dissolution Safety Boundary]]
- [[DPDR and the Pit of the Void]]
- [[Guidance Scope and Accountability Boundary]]

Work product:

- red/yellow/green matrices where useful;
- "continue, simplify, pause, refer, stop" criteria;
- specific route tables for pain, emotional flooding, no-self/void, teacher
  pressure, behavior mismatch, medical contexts, sleep, sexuality, caffeine,
  birth/parenting, dream practice, retreat intensity, and future AI/ultrasound
  hopes;
- clear distinction between Shinzen-internal practice guidance and ordinary
  medical, clinical, legal, relational, ethical, or organizational support.

Rule:

Safety subpages should be narrower and more executable, not another giant
warning anthology.

Implementation note - 2026-05-16:

- Began Phase 6 with [[Guidance Scope and Accountability Boundary]] because
  the router benchmark found teacher pressure, behavior mismatch, and support
  scope had early routing but too little executable criteria.
- Added a top-level decision matrix covering routine guidance, behavior
  change, applied-life domains, clinical/medical scope, weak ego or boundary
  collapse, bhanga and altered phenomena, ritual adjacency, teacher conduct,
  and Source/service claims.
- Added a role ladder and stop/refer/protect criteria so future agents can
  distinguish ordinary support, practice reminders, Shinzen-style coaching,
  terrain-specific support, and qualified care or protection before giving
  technique.
- Updated [[Practice Guidance Toolkit]], [[Complete Experience Safety
  Boundary]], and [[Mastery Without Guru Inflation]] so teacher/coach scope,
  consent, referral, behavior accountability, and protection questions route
  directly to the matrix.
- Next safety pass should target [[Completion Versus Bypass Safety Boundary]]
  or [[Intensity and Embodiment Safety Boundary]], depending on which live
  guidance row is blocking decisions.

Implementation note - 2026-05-16, continued:

- Added an executable green/yellow/red decision matrix to [[Completion Versus
  Bypass Safety Boundary]] for pain without suffering, equanimity/no-reaction,
  fulfillment or positive construction, insight/purification, and
  condition-independent happiness claims.
- Added continue, simplify, and stop-first criteria so future agents can
  distinguish Shinzen-style practice optimization from medical, clinical,
  protective, relational, or guidance-accountability needs.
- Routed equanimity and purification branches through the new [[Equanimity
  Versus Suppression]], [[Equanimity And Purification Taste]], and
  [[Condition-Independent Happiness]] pages created during the Phase 5 pilots.
- Next safety pass should target [[Intensity and Embodiment Safety Boundary]]
  if physical pain, retreat aftershock, kriyas, or strong determination are
  the live blocker; otherwise target [[Practice Method Safety Boundary]] for
  technique-choice stop/simplify criteria.

Implementation note - 2026-05-16, intensity and method pass:

- Added executable green/yellow/red decision matrices to [[Intensity and
  Embodiment Safety Boundary]] and [[Practice Method Safety Boundary]].
- The intensity matrix covers physical pain and illness sensations,
  difficult emotion and primal Feel, Strong Determination, ritual heat or
  teacher-mediated intensity, retreat aftershock or global Gone, and kriyas.
- The method matrix covers Noting and labels, Do Nothing and Rest, zooming
  and broad awareness, session setup and micro-hits, sleep or dream practice,
  caffeine or stimulants, and dropout or sudden-Rest cues.
- Added continue, simplify, pause, refer, and stop-first criteria so future
  agents can choose between Shinzen-style practice optimization, method
  simplification, ordinary support, qualified care, and protection.
- Updated [[Complete Experience Safety Boundary]], `wiki/index.md`, and
  `wiki/_page_catalog.md` so the parent hub points to the child matrices
  instead of preserving the older "criteria still absent" posture.
- Phase 6's main safety surfaces now have first-pass criteria. The next
  phase should begin the Phase 7 redundancy and merge-link audit, especially
  old broad links to [[Complete Experience Safety Boundary]] that now deserve
  narrower child-boundary targets.

## Phase 7 - Redundancy And Merge Audit

Goal: reduce unnecessary bloat without flattening real distinctions.

Audit for:

- near-synonym concept pages;
- repeated mechanism summaries copied across owner pages;
- source-page details re-explained in several hubs;
- pages whose thesis is only a topic label;
- links that are merely mentions;
- child pages that would be better as sections;
- sections that would be better as child pages;
- old ingest chronology that no longer helps routing.

Actions:

- Merge pages only when they do the same durable job.
- Add old titles to `aliases`.
- Replace duplicated paragraphs with one link plus a decision-relevant reason.
- Preserve contradictory frames where they actually change interpretation.

Implementation note - 2026-05-16:

- Began Phase 7 with a small merge-link audit rather than a page merge.
- Updated [[Kriyas]], [[Strong Determination]], [[Turn Toward and Turn
  Away]], and [[Way of Physical Senses]] so bodily-intensity and spontaneous-
  movement safety routes point to [[Intensity and Embodiment Safety
  Boundary]] instead of only the broad [[Complete Experience Safety
  Boundary]] parent.
- Updated [[Practice Entry and Method Choice]] so method-choice safety points
  to [[Practice Method Safety Boundary]] in frontmatter, tensions, and
  related routing.
- Continued Phase 7 by retargeting current routing cues in selected Basic
  Mindfulness chapter source pages: physical sensation now routes to
  [[Intensity and Embodiment Safety Boundary]], rest and Do Nothing to
  [[Practice Method Safety Boundary]], positive cultivation to [[Completion
  Versus Bypass Safety Boundary]], and Flow/Gone dark-night issues to
  [[Altered Phenomena and Dissolution Safety Boundary]].
- Continued Phase 7 with a method-option safety pass: effort regulation, Do
  Nothing, forced spoken labels, and zooming source/owner routes now point to
  [[Practice Method Safety Boundary]] where the issue is method fit, dosage,
  overwhelm, or stop/support criteria rather than the broad parent hub.
- The prior stop-at-Phase-7 instruction has been satisfied; after explicit
  user request, Phase 8 may proceed. Keep any remaining Phase 7 work as
  optional small-cluster cleanup rather than the default next step.
- Next Phase 7 passes should continue with similarly small clusters:
  old broad safety links, duplicated mechanism summaries, and near-synonym
  pages, with merges reserved for pages that truly do the same durable job.

## Phase 8 - Editorial Polish And Maturity Pass

Goal: make high-value pages readable, calibrated, and durable enough to
promote toward `mature`.

Checklist:

- Thesis is a claim, not a topic label.
- Opening explains why the page matters.
- `## Key Points` exposes core claim, use case, tensions, and source posture.
- Body sections are named by decision function, not only by source chronology.
- Load-bearing claims cite source pages or are marked speculative/inferred.
- Related links include reasons.
- Frontmatter remains a routing card, not a map.
- Safety boundaries and source limits appear before advanced interpretation.
- The page can be skimmed without losing the main decision surface.

Promotion rule:

Move a page from `working` to `mature` only after it survives a route test and
no longer has obvious decomposition, citation, or safety-posture debt.

Implementation note - 2026-05-16:

- Started Phase 8 with [[Practice Guidance Toolkit]] because it is a
  first-load router for concrete practitioner reports and carried a
  source-heavy frontmatter advisory.
- Route test: physical discomfort, emotional eruption, teacher/accountability
  concern, sleep/caffeine/dream/sexuality edge cases, and behavior-not-changing
  reports all reached a specific owner/source page plus a safety or
  accountability guardrail without requiring the frontmatter bibliography.
- Trimmed the page's frontmatter to eight principal source anchors and left
  specialized anchors in the body `Source Anchors` section.
- Promoted the page to `mature`; next Phase 8 candidates should be similarly
  route-tested before promotion.
- Continued Phase 8 with [[Guidance Scope and Accountability Boundary]]
  because it is both a first-load accountability/safety router and a
  source-heavy frontmatter advisory.
- Route test: routine coaching, behavior-not-changing, medical/applied-life,
  dark-night or DPDR-like distress, ritual adjacency, teacher-misconduct, and
  Source/service overclaim reports all reached the decision matrix, role
  ladder, stop/referral criteria, and specialized source anchors without
  needing frontmatter to act as a bibliography.
- Trimmed the page's frontmatter to eight principal raw anchors, added a
  compact `Source Anchors` map for specialized applied-domain and ritual
  evidence, compressed open questions/evidence needs into decision clusters,
  and promoted the page to `mature` while keeping `confidence: speculative`.
- Continued Phase 8 with [[Five Ways]] because it is a first-load practice
  route hub and later oral ingests had pushed its frontmatter back over the
  principal-anchor target.
- Route test: emotional eruption, physical anchoring, rest/Do Nothing, Flow
  or dissolution, positive/service cultivation, and session-workout design
  all reached the new route map, the correct Way owner page, and the
  relevant safety or guidance boundary before deeper source descent.
- Trimmed frontmatter back to the eight manual principal anchors, moved oral
  compactors and edge examples into `Source Anchors`, added a first-load
  `Route Map`, trimmed source-heavy `Related` edges, and promoted the page to
  `mature`.
- Continued Phase 8 with [[Sensory Grid]] because it is the high-importance
  label/range router under Basic Mindfulness and SHF, and remained just over
  the principal-anchor target after later oral-source integration.
- Route test: label ambiguity, narrow/wide/cycle choices, inner/outer/rest/
  Flow/Space/Gone classification, grid-based guidance, and old-grid/new-SHF
  compatibility all reached the new decision map, the relevant owner page,
  coverage strategy, or safety boundary before deeper evidence descent.
- Trimmed frontmatter to eight principal raw anchors, kept lucid-dream and
  binary-contrast refinements in the body `Source Anchors` and evidence map,
  shortened the source-heavy `Related` tail, and promoted the page to
  `mature`.
- Continued Phase 8 with [[Do Nothing]] because it is a core method page,
  safety-adjacent, and still carried one extra frontmatter source after
  later edge-case integration.
- Route test: ordinary instruction, covert effort to stop experience,
  spacey/dull drift, racy over-effort, agitation or destabilization, sole-
  method use, pleasant-interest wandering, and broad low-effort awareness all
  reached the new decision map, the right method/source page, and
  [[Practice Method Safety Boundary]] or [[Complete Experience Safety
  Boundary]] when risk appeared.
- Trimmed frontmatter to eight principal raw anchors, kept [[The Happy
  Wanderer]] as a body-level source anchor, added a first-load `Decision
  Map`, routed method safety to [[Practice Method Safety Boundary]], trimmed
  the source-heavy `Related` section, and promoted the page to `mature`.
- Continued Phase 8 with [[Nurture Positive]] because it is the constructive
  counterpart to Noting and Do Nothing, had the heaviest remaining
  method-page frontmatter, and needs positivity-bypass and service checks
  visible before the evidence body.
- Route test: ABCISO/ABCD theme choice, finding already-present positive
  Feel, triggering positive Feel, spontaneous positive content, void-side
  reconstruction, behavior/service claims, ritual/archetype practice, and
  forced or clinically loaded positivity all reached the new decision map,
  the right owner/source page, and the focused safety or accountability
  boundary before deeper source descent.
- Trimmed frontmatter to eight principal raw anchors, compressed the long
  source anthology into grouped `Source Anchors`, added a first-load
  `Decision Map`, routed behavior/service and positivity-bypass cases to
  [[Total Happiness Behavior And Service Test]], [[Guidance Scope and
  Accountability Boundary]], and [[Completion Versus Bypass Safety Boundary]],
  trimmed the source-heavy `Related` section, and promoted the page to
  `mature`.
- Continued Phase 8 with [[Mindfulness Skill Triad]] because it is the
  central CCE architecture page and still carried narrow oral anchors in
  first-load frontmatter.
- Route test: mindfulness-definition ambiguity, weak or overemphasized
  skill, labels and focus ranges, complete experience or purification,
  reward taste and plateau, altered phenomena or Source language, and
  mindfulness-sufficiency claims all reached the new decision map, the
  relevant skill/method owner, and the safety or accountability boundary
  when scope exceeded the triad.
- Trimmed frontmatter to eight principal raw anchors, compressed source
  anchors into definition/transformation, SHF/labeling, manual/reward, oral
  bridge, and boundary groups, added a first-load `Decision Map`, shortened
  the source-heavy `Related` tail, and promoted the page to `mature`.
- Continued Phase 8 with [[Practice Cycles]] because it is the maintained-
  practice implementation router and still carried retreat-entry/exit detail
  in first-load frontmatter.
- Route test: inconsistent daily practice, life practice as aspiration,
  formal-session setup, retreat or yearly support, post-retreat aftercare,
  crisis-as-monastery framing, low motivation or plateau, and accelerator
  use all reached the new decision map, the relevant source/owner page, and
  the method, intensity, guidance, or parent safety boundary before deeper
  evidence descent.
- Trimmed frontmatter to eight principal raw anchors, grouped source anchors
  into daily/yearly cycles, life practice, session setup, retreat/continuity,
  and motivation/accelerator clusters, added a first-load `Decision Map`,
  shortened the source-heavy `Related` tail, updated the index backlog count
  for the new retreat-stream raw files, and promoted the page to `mature`.

## Phase 9 - Lint And Health Tooling

Goal: make structural drift visible early.

Candidate lint or auxiliary health checks:

- large page advisory by type and importance;
- index opening budget and total index budget;
- pages with many raw sources in non-source frontmatter;
- pages with too many best links;
- pages with very long `load_when`;
- high-importance pages missing `## Key Points`;
- pages over threshold with no decision map;
- safety-risk keywords without a safety-boundary link;
- source pages missing model/practice delta;
- duplicate or circular Related sections;
- unregistered pages across index/catalog/register files.

Tooling should advise before it blocks. Hard failures should remain reserved
for mechanical invariants.

## Batch Size And Cadence

Default batch:

- one hub page plus up to three child pages; or
- one domain catalog/register change; or
- one safety matrix pass; or
- one redundancy/merge cluster.

Each batch must include:

- scoped objective;
- old-to-new mapping when pages move or split;
- affected pages list;
- lint output;
- log entry;
- short note on residual risk.

Avoid touching more than five content pages in one refactor unless there is a
clear mapping and validation plan.

## First Three Recommended Work Sessions

1. **Build registration/catalog architecture.** Completed 2026-05-16.
   `_page_catalog.md` now carries exhaustive compiled-page registration,
   lint recognizes approved registration files, and the source domain is the
   first slimmed proof section.
2. **Add the Current Model Card.**
   This directly addresses whole-system and domain-overview query cost before
   broader synthesis splits.
3. **Choose the first decomposition pilot from benchmark evidence.**
   Completed the first pilot for [[Source And Polarities]] on 2026-05-16.
   Completed the compact [[Guidance Scope and Accountability Boundary]]
  decision matrix on 2026-05-16, the impermanence practice index, and the
  [[Total Happiness]] hub-plus-children pilot, and the [[Equanimity]]
  hub-pattern pilot. Current follow-on ranking favors a Phase 6 safety
  criteria page before broader monolith surgery.

## Stop Rules

Stop and reassess when:

- a split hides safety posture;
- a child page lacks an independent thesis;
- a page is shorter but future routing is worse;
- citations or claim IDs become detached from the moved claim;
- index surgery requires disabling registration checks;
- the refactor starts optimizing page count rather than future judgment;
- a source-level uncertainty is being smoothed into a clean synthesis.

## Relationship To Earlier Remediation Plan

`wiki/_review_remediation_plan.md` remains useful history for the first
router/safety/frontmatter remediation pass. This file supersedes it for the
post-ingest stage. The new center of gravity is no longer "which source next?"
but "which structure lets future agents think from the compiled corpus with
the least unnecessary context and the least overclaim risk?"
