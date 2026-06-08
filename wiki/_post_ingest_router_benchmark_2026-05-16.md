# Post-Ingest Router Benchmark - 2026-05-16

Initial Phase 1 benchmark for `wiki/_post_ingest_knowledge_health_plan.md`.
This is a system review note, not evidence for Shinzen claims.

## Scope

- Startup surfaces read: `wiki/index.md` opening through `Open Questions`,
  recent `wiki/log.md`, `wiki/_operations.md`, and
  `wiki/_post_ingest_knowledge_health_plan.md`.
- Benchmarked compiled routing only. Raw sources were not re-read because the
  question is whether the compiled wiki points future agents to the right next
  load.
- Refreshed lint first. After a small pure-analysis dependency repair, lint
  passes with expected backlog, source-list-size, and large-domain diagnostics.

## Baseline

- Mechanical lint after the retreat-portfolio removal: OK, 289 compiled pages
  and 225 raw sources checked.
- Page types: 223 source, 49 concept, 9 synthesis, 7 question, 1 thesis.
- Remaining canonical raw backlog diagnostics: `IntroToUltra_ver4.8.pdf` and
  the plan-skipped duplicate welcome transcript.
- No `_page_catalog.md` or `_sources_catalog.md` exists yet.
- Largest active routing costs remain `wiki/index.md`, [[Source And
  Polarities]], [[Total Happiness]], [[Current Model]], [[Expansion And
  Contraction]], [[Flow]], [[Complete Experience]], [[No-Self And
  Personality]], [[Lineage Translation]], [[Insight and Purification]],
  [[Shinzen's Teaching Method]], [[Nurture Positive]], [[Guidance Scope and
  Accountability Boundary]], [[Altered Phenomena and Dissolution Safety
  Boundary]], and [[Equanimity]].

## Findings

- Practice routing is the strongest surface. [[Practice Guidance Toolkit]]
  already has an agent contract, minimum inputs, fast algorithm, decision
  table, safety gates, and applied-domain rows.
- General safety routing is also strong. [[Complete Experience Safety
  Boundary]] exposes a child-page map and red/yellow/green routing early
  enough for high-risk practitioner reports.
- The main index is still too much of a chronology/register. It is useful but
  expensive as a first load, and there is no catalog layer to let it shrink
  safely.
- Whole-system routing is expensive. [[Current Model]] has useful key points
  but no strict card, and its opening still carries gate chronology.
- Source/metaphysics routing is expensive. [[Source And Polarities]] has good
  early posture, but science, time-space, Source, afterglow, polarity, and
  service details live in one 799-line owner page with source-heavy
  frontmatter.
- Teacher/accountability and behavior-mismatch routing surfaces safety early
  but still require loading large pages without an executable decision table.
- The impermanence branch lacks a compact hub for Flow, Gone, Spaciousness,
  Expansion-Contraction, bhanga, and Source afterglow, so related queries can
  force sibling-page loading.

## Query Results

| Query Type | Observed Route | Safety/Source Posture | Cost And Failure Mode | Refactor Implication |
| --- | --- | --- | --- | --- |
| Strong physical pain in sitting | `index` -> [[Practice Guidance Toolkit]] -> [[Turn Toward and Turn Away]] or [[Intensity and Embodiment Safety Boundary]] | Early enough | Good first route; focused stop/support criteria still distributed | Later safety criteria pass, not first split |
| Emotional eruption and fear during noting | `index` -> [[Practice Guidance Toolkit]] -> emotion row/source or [[Turn Toward and Turn Away]] | Early enough | Good route; trauma/self-harm scope remains generic | Add executable criteria in safety pass |
| No-self, paper-thin world, void, or DPDR-like distress | `index` -> [[Complete Experience Safety Boundary]] -> [[DPDR and the Pit of the Void]] | Strong | Good route; cost is acceptable because risk is high | Preserve this safety-first route |
| Which Shinzen method should be used first | `index` -> [[Practice Guidance Toolkit]] -> [[Practice Entry and Method Choice]] | Adequate | Practice Entry is long but routable | No initial-phase split |
| Whether Source is literally real or scientifically supported | `index` -> [[Source And Polarities]] -> [[Reality & Sensory Experience]] or science/time source pages | Early but expensive | Source page mixes practice, metaphysics, science analogy, time, and service | Split Source/science/time/service branches |
| Teacher pressure, charismatic authority, or suspect behavior | `index` -> [[Complete Experience Safety Boundary]] -> [[Guidance Scope and Accountability Boundary]] | Early | Guidance page is long and lacks a compact decision table | Add guidance/accountability matrix |
| Practice feels profound but behavior is not improving | `index` -> [[Practice Guidance Toolkit]] -> behavior row, [[Complete Experience Safety Boundary]], [[Total Happiness]], or [[Guidance Scope and Accountability Boundary]] | Early but scattered | Behavior verification is distributed across major pages | Safety/accountability pass before Total Happiness split |
| Retreat aftershock, sleep disruption, or spillover | `index` -> [[Practice Guidance Toolkit]] -> [[Practice Cycles]], [[What to Expect and Do After a Mindfulness Retreat]], sleep source, or safety hub | Early but branchy | Good source pages, but no compact retreat-aftershock decision matrix | Safety criteria pass or retreat-aftercare card |
| Sexuality, birth, illness, caffeine, or dream practice | `index` -> [[Practice Guidance Toolkit]] applied-domain rows -> source pages | Strong | Good for single domains; no applied-domain catalog for overview | Catalog/index work before new applied page |
| Equanimity cannot be generated | `index` -> [[Practice Guidance Toolkit]] -> [[Equanimity]] and second-order equanimity source | Strong | Route is clean; Equanimity is a useful pilot, not urgent debt | Use as low-risk hub-pattern pilot |
| Flow, Gone, spaciousness, or Expansion-Contraction is reported | `index` -> individual owner pages | Mixed | No impermanence/space hub; sibling loading likely | Create an impermanence practice index or hub |
| Positive practice exposes fear or sadness | `index` -> [[Practice Guidance Toolkit]] -> [[The Happy Wanderer]] or [[Nurture Positive]] | Adequate | Route is good; Nurture Positive remains long | Defer until after higher-load hubs |
| Source provenance question | Owner page source anchors -> source pages | Good after route | Finding the owner/source cluster depends on index/search because no catalog exists | Registration/catalog architecture |
| Domain overview request | `index` -> domain entries or [[Current Model]] | Too expensive | Index and Current Model both carry too much chronology/body for quick overview | Index surgery plus Current Model card |
| Future agent asks whether a page should split | Plan criteria + lint diagnostics + line counts | Adequate | Good criteria, but no standard benchmark note existed before this file | Keep benchmark notes as review artifacts |
| Concise current whole-system model | `index` -> [[Current Model]] | Adequate but verbose | Key points help, but no strict current-model card or next-load table | Add Current Model card before broader splits |

## Ranked First Refactors

1. **Registration/catalog architecture plus index proof-of-concept.**
   Highest gain because the startup index is still bearing chronology,
   registration, and routing at once. Create `_page_catalog.md` or equivalent,
   update lint registration rules, then slim one domain section as proof.
2. **Current Model card.** Add the strict top card proposed in Phase 4 before
   splitting the page. This directly improves whole-system and overview
   queries.
3. **Source And Polarities hub-and-child split.** Keep the parent as a
   decision surface, then separate Source/Zero afterglow, science/mathematics
   analogy limits, time-space speculation, and service language if the mapping
   stays clean.
4. **Guidance/accountability and behavior-verification decision matrix.**
   Start with a compact executable table rather than a large split. This
   addresses teacher pressure, behavior mismatch, retreat aftershock, and
   high-stakes support routing.
5. **Impermanence practice hub or index.** Route Flow, Gone, Spaciousness,
   Expansion-Contraction, bhanga, and Source afterglow without forcing sibling
   page loading.

[[Equanimity]] remains a good low-risk pilot for the hub-and-child pattern,
but this benchmark found higher immediate routing gain in catalog/index,
Current Model, Source, accountability, and impermanence routing.

## Next Move

Begin Phase 2 with catalog-backed registration. Do not perform major index
surgery until lint can register compiled pages through catalog surfaces as
well as `wiki/index.md`.
