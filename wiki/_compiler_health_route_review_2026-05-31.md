# Compiler Health Route Review - 2026-05-31

This is a system review note for the `shinzen-compiler-health-loop`
automation. It is not evidence for Shinzen claims. The run did not ingest raw
sources and did not enter `practice-wisdom-backlog`, `defer-query-driven`,
`skip-manifest-only`, or `upgrade-existing` source work.

## Inputs Checked

- Startup surfaces: `AGENTS.md`, the opening/dashboard of `wiki/index.md`,
  recent `wiki/log.md`, `wiki/_compiler_health_multisession_plan.md`, and the
  router/health portions of `wiki/_post_ingest_knowledge_health_plan.md`.
- Structural diagnostics: `tools\wiki_lint.cmd`, largest page scan,
  no-inbound diagnostic, high-load wikilink counts, broad-domain warnings, and
  the opening of `wiki/_page_catalog.md`.
- High-load judgment surfaces were sampled for route behavior, not edited:
  [[Current Model]], [[Practice Guidance Toolkit]], [[Complete Experience
  Safety Boundary]], [[Guidance Scope and Accountability Boundary]],
  [[Source Science And Analogy Boundary]], and [[Total Happiness]].

## Current Structural Readout

- Initial lint exited OK for 368 compiled pages and 361 raw sources.
- Initial residual diagnostics were advisories, not blockers: 72 canonical raw
  source paths without source pages, eight principal-source-count advisories,
  one no-inbound page, and broad-domain warnings for `practice`, `primary`,
  `safety`, `service`, `sources`, `teaching`, and `transformation`. Final lint
  after the small routing fixes no longer reports the no-inbound diagnostic;
  the remaining residuals are raw-source backlog, principal-source-count, and
  broad-domain advisories.
- Largest non-system content pages by line count remain [[Lineage
  Translation]] (587), [[No-Self And Personality]] (561), [[Current Model]]
  (550), [[Expansion And Contraction]] (499), [[Flow]] (460), [[Shinzen's
  Teaching Method]] (433), [[Complete Experience]] (430), [[Guidance Scope and
  Accountability Boundary]] (423), and [[Practice Cycles]] (408).
- High-load link counts confirm the expected router surfaces:
  [[Complete Experience Safety Boundary]] (~560 inbound mentions),
  [[Source And Polarities]] (~479), [[Practice Guidance Toolkit]] (~446),
  [[Total Happiness]] (~416), [[Lineage Translation]] (~366), and
  [[Current Model]] (~362).
- `wiki/_page_catalog.md` is discoverable from the index opening and gives a
  usable exhaustive register, but it remains archival rather than a first-load
  decision surface.

## Route Benchmark

| Query family | First route tested | Result | Fix or defer |
| --- | --- | --- | --- |
| Concrete practitioner report | [[Practice Guidance Toolkit]] from the index opening and table | Pass. It exposes context gathering, scope gate, branch choice, method tuning, and follow-up. | Defer detailed judgment-page tightening to Workstream B. |
| Safety red flag: medical, dissociation, teacher pressure, worsening, behavior mismatch | [[Complete Experience Safety Boundary]] first, then focused child boundary | Pass. Red/yellow/green triage and child routes appear early. | Defer criteria sharpening to Workstream B. |
| Whole-system overview | [[Current Model]] | Pass with cost. The opening card routes well, but the page remains one of the largest and carries phase-closeout chronology. | Defer opening/decision-surface cleanup to Workstream B. |
| Source/science/AI/ultrasound/physics analogy | Previously split between [[Lineage Translation]], [[Impermanence Flow Gone And Source]], and source-domain entries | Friction. The correct owner, [[Source Science And Analogy Boundary]], was present but not explicit in the startup task table. | Fixed in `wiki/index.md` by adding a direct Source/science route. |
| Service, behavior verification, teaching, or Total Happiness | [[Total Happiness]] | Pass. The hub has a decision map and routes to behavior/service/accountability boundaries. | No A-scope edit. |
| Provenance, source frame, omissions, exact teaching register | Relevant source page or `wiki/_page_catalog.md` | Pass. The index opening distinguishes first-load routing from catalog registration. | No A-scope edit. |
| Domain overview or broad scan | `wiki/_page_catalog.md`, then index domain sections | Partial pass. Catalog discovery is clear; broad-domain lint warnings show that sub-index/router surfaces may still be needed. | Defer to Workstream C. |
| Long solitary retreat carrying artifact | [[Practice Cycles]] should own retreat-cycle routing | Friction. [[Yearlong Solitary Retreat Carrying Text]] had no inbound links despite being a high-importance practice/safety analysis. | Fixed by adding a Practice Cycles decision-map row and Related link. |

## Ranked Routing Failures

1. **Source/science claims were not a first-load route.** Future agents could
   reach the right owner page only by searching or descending through lineage,
   Source, or source-domain entries. This risks overpromoting Shinzen's
   science, mathematics, AI, ultrasound, physics, or energy language before
   evidence-tier sorting. Fixed by adding [[Source Science And Analogy
   Boundary]] to the index startup table.
2. **The yearlong-retreat analysis was orphaned.** The page was registered in
   the catalog but had no inbound compiled links, so a future long-retreat
   query could miss the durable practice-governor artifact. Fixed by routing
   it from [[Practice Cycles]].
3. **The dashboard mixed current automation scope with ingest chronology.**
   Lint now reports 72 raw-source residuals, while the dashboard emphasized
   two query-driven non-channel items plus a long closed-ingest chronology.
   Fixed by making the 72 residual diagnostic explicit and keeping it outside
   this health-loop ingest scope.
4. **Broad-domain warnings remain real discoverability debt.** The catalog
   prevents registration failure, but `practice`, `primary`, `safety`,
   `service`, `sources`, `teaching`, and `transformation` are still broad
   enough that future domain-overview questions may require search rather than
   a targeted router. Defer to Workstream C.
5. **Principal-source-count advisories remain context-efficiency debt.** The
   eight pages named by lint still ask frontmatter to carry too much source
   routing. Defer to Workstream C so source-anchor trimming is handled as one
   coherent pass.
6. **The high-load judgment pages are strong but still expensive.** [[Current
   Model]], [[Practice Guidance Toolkit]], [[Complete Experience Safety
   Boundary]], and [[Guidance Scope and Accountability Boundary]] all route
   correctly in opening sections, but their decision surfaces should be
   route-tested against concrete cases before further edits. Defer to
   Workstream B.

## Applied Small Fixes

- Added a direct Source/science/AI/ultrasound/physics/energy/mathematics
  route in `wiki/index.md` to [[Source Science And Analogy Boundary]].
- Added a long-retreat practice-governor row and Related link from
  [[Practice Cycles]] to [[Yearlong Solitary Retreat Carrying Text]].
- Compressed the index dashboard backlog posture so accepted raw-source
  residual diagnostics are visible without reopening source ingest.

## Deferred Work

- Workstream B should route-test and tighten [[Current Model]], [[Practice
  Guidance Toolkit]], [[Complete Experience Safety Boundary]], and [[Guidance
  Scope and Accountability Boundary]] across ordinary method choice, physical
  pain, emotional eruption, no-self/void distress, teacher pressure, behavior
  mismatch, Source/science overclaim, and applied-life or medical-adjacent
  reports.
- Workstream C should resolve or justify the current principal-source-count
  advisories and decide whether broad-domain warnings deserve sub-index/router
  surfaces or accepted residual-risk notes.
