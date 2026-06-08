# Compiler Health Source Anchor And Domain Review - 2026-05-31

System note for Workstream C of `wiki/_compiler_health_multisession_plan.md`.
This is not evidence for Shinzen claims. No raw sources were ingested, and no
excluded backlog classes were entered.

## Scope

Workstream C addressed the current lint source-anchor advisories and reviewed
the remaining broad-domain warnings after Workstreams A and B had already
completed.

## Source-Anchor Outcomes

All eight non-source pages that lint reported above the principal-anchor target
were brought to eight or fewer raw paths in frontmatter:

- [[Expansion And Contraction]]: kept the manual, Source chapter, four-part
  Expansion-Contraction series, and Sasaki polarity anchors in frontmatter;
  kept [[Three Dances of Self and World]] as a body-level source anchor.
- [[Guidance Scope and Accountability Boundary]]: kept live guidance,
  authority, clinical/dark-night, behavior, ethics, qualifications, and wording
  anchors in frontmatter; kept [[Journey to True Spirituality]] in the body
  accountability cluster.
- [[Lineage Translation]]: added a `Source Anchors` section and moved
  Christian-poetic and Great Dharma whole-system evidence into body-level
  secondary anchors.
- [[Mysticism As Concentration]]: added a `Source Anchors` section and moved
  lineage-gratitude plus true-spirituality whole-system evidence into
  body-level secondary anchors.
- [[No-Self And Personality]]: kept the book-level and direct no-self/DPDR
  anchors in frontmatter; retained Great Dharma no-self and returning-self
  branches in the existing body `Source Anchors`.
- [[Source And Polarities]]: added a `Source Anchors` section and kept later
  Great Dharma, springy-void, and three-dances material as body-level
  extensions.
- [[Source Science And Analogy Boundary]]: added a `Source Anchors` section
  and kept [[The Spring of the Void]] plus [[Three Dances of Self and World]]
  as secondary examples rather than first-load anchors.
- [[Total Happiness Behavior And Service Test]]: added a `Source Anchors`
  section and kept [[Journey to True Spirituality]] as the body-level blunt
  behavior/accountability bridge.

Result: `tools\wiki_lint.cmd` no longer reports principal-source-count
advisories.

## Broad-Domain Review

The remaining broad-domain warnings were reviewed as routing advisories, not
automatic refactor commands:

| Domain | Current posture | Residual risk |
| --- | --- | --- |
| `practice` | Accepted residual. Startup routes already point to [[Practice Guidance Toolkit]], [[Practice Entry and Method Choice]], [[Basic Mindfulness Practice Architecture]], [[See Hear Feel]], and method owner pages. | Future route tests may still justify a smaller method-family sub-index, but creating one now would duplicate existing hubs. |
| `primary` | Accepted residual. This is too broad to use as a topical router; first-load routing should use the index task table and catalog primary-domain register. | Future agents could mistake it for a load path; the catalog note now warns against that use. |
| `safety` | Accepted residual. The current safety router stack is [[Complete Experience Safety Boundary]], child safety boundaries, [[Guidance Scope and Accountability Boundary]], and [[Practice Guidance Toolkit]]. | Splitting safety again without a concrete failure could hide stop/referral criteria. |
| `service` | Accepted residual. Service routes are covered by [[Total Happiness]], [[Total Happiness Behavior And Service Test]], [[Source And Service Boundary]], and [[Guidance Scope and Accountability Boundary]]. | Behavior-verification standards remain incomplete as evidence, but a new index would not solve that. |
| `sources` | Accepted residual. One source page per substantive raw source is expected; use `wiki/_page_catalog.md` for source lookup instead of the startup index. | A separate source catalog may become useful only if `_page_catalog.md` becomes too slow or noisy for provenance tasks. |
| `teaching` | Accepted residual. Teaching and authority questions route through [[Lineage Translation]], [[Shinzen's Teaching Method]], [[Teaching A Path]], and [[Guidance Scope and Accountability Boundary]]. | Cross-tradition, ritual, and authority material can still overmerge if not routed through the boundary pages first. |
| `transformation` | Accepted residual. Whole-system and transformation routing is currently held by [[Current Model]], [[Impermanence Flow Gone And Source]], [[Complete Experience]], [[Insight and Purification]], [[No-Self And Personality]], and [[Source And Polarities]]. | The domain is broad by design; future splits should be triggered by route-test failures rather than count alone. |

No new sub-index was created in this pass. The existing index, catalog, and
hub pages already give first-load routes for the warned domains, and a new
router without a concrete query failure would add another page to maintain
without lowering current load cost.

## Ranked Residual Routing Risks

1. **Broad-domain warnings remain active lint diagnostics**. They are accepted
   residuals, but future agents need to know they are not a hidden ingest queue
   or an automatic mandate to create sub-indexes.
2. **The source domain is intrinsically large**. The catalog is currently
   adequate for provenance lookup; a dedicated source catalog should wait for
   measured catalog friction.
3. **Transformation and practice hubs remain high-load surfaces**. Their
   current routing is serviceable, but future route tests may justify smaller
   child routers around method families or transformation mechanisms.
4. **Service and safety standards remain evidence-incomplete**. More routing
   pages would not fix missing behavioral, clinical, or governance evidence;
   future work should preserve referral and accountability boundaries.

## Validation

`tools\wiki_lint.cmd` exits OK with accepted residual diagnostics only:

- 72 raw-source backlog paths outside this automation's scope.
- Broad-domain warnings for `practice`, `primary`, `safety`, `service`,
  `sources`, `teaching`, and `transformation`.
