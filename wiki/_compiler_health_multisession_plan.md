# Compiler Health Multi-Session Plan

Created 2026-05-31 after the selected ShinzenVideos `series-candidate` and
`audit-needed` queues reached zero.

This is a system plan, not evidence for Shinzen claims. It gives the
`shinzen-compiler-health-loop` automation a bounded post-ingest job and a
clear stop condition.

## Purpose

Run a thorough, multi-session compiler-health pass now that the active
ShinzenVideos ingest loop is done. The work should improve future agent
judgment, routing, safety calibration, and context efficiency without opening
new source-ingest scope.

Do not ingest `practice-wisdom-backlog`, `defer-query-driven`,
`skip-manifest-only`, or `upgrade-existing` items under this plan.

## Status Board

| Workstream | Status | Completion test |
| --- | --- | --- |
| A. Broad route and structure review | complete | Completed 2026-05-31 in `wiki/_compiler_health_route_review_2026-05-31.md`; top routing failures were ranked, the Source/science startup route and long-retreat analysis discoverability were fixed, and larger refactors were deferred to B/C. |
| B. Judgment surface pass | complete | Completed 2026-05-31 in `wiki/_compiler_health_judgment_surface_review_2026-05-31.md`; the high-load judgment pages were route-tested and patched where needed, mainly by routing Source/science/AI/ultrasound proof claims through [[Source Science And Analogy Boundary]] before practice, safety, service, or guidance inference. |
| C. Source-anchor and domain-bloat pass | complete | Completed 2026-05-31 in `wiki/_compiler_health_source_anchor_domain_review_2026-05-31.md`; all principal-source-count advisories were resolved by trimming frontmatter to eight or fewer raw anchors and preserving secondary anchors in body `Source Anchors`, while broad-domain warnings were recorded as accepted residual routing advisories. |
| Stop automation | complete | A-C are complete, `tools\wiki_lint.cmd` passes with only accepted residual diagnostics, memory was updated, and `C:\Users\Urgen\.codex\automations\shinzen-compiler-health-loop\automation.toml` is already `PAUSED`; no new source scope was opened. |

## Per-Run Rules

1. Orient leanly from `AGENTS.md`, the opening/dashboard of `wiki/index.md`,
   recent `wiki/log.md`, this plan, and the relevant section of
   `wiki/_post_ingest_knowledge_health_plan.md`.
2. Read the automation memory at
   `C:\Users\Urgen\.codex\automations\shinzen-compiler-health-loop\memory.md`
   when available.
3. Work the first non-complete workstream in the status board. Do not jump
   ahead unless the current workstream's completion test is already satisfied.
4. Keep each run bounded to one coherent batch: one review note, one router
   surface cluster, one source-anchor cluster, or one domain-routing cluster.
5. Preserve claims, source posture, contradictions, practice handles,
   teaching moves, and safety boundaries before compressing prose.
6. Update this status board after material progress. Update `wiki/index.md`,
   `wiki/_page_catalog.md`, and affected pages only when routing or page
   registration changes.
7. Append one newest-first `wiki/log.md` entry when wiki state changes.
8. Run `tools\wiki_lint.cmd` and report diagnostics.

## Workstream A - Broad Route And Structure Review

Goal: thoroughly test the compiler as a future agent would use it before
making another large refactor.

Minimum scope:

- Re-run a representative route benchmark across practitioner reports,
  safety red flags, whole-system questions, Source/science questions,
  service/behavior questions, provenance questions, and domain-overview
  questions.
- Inspect current lint diagnostics, largest or most-loaded pages, no-inbound
  pages, broad domains, index/dashboard shape, and catalog discoverability.
- Rank the top routing failures by future judgment cost.
- Apply only small, obvious routing fixes during the review run; defer larger
  refactors to B or C.

Preferred output:

- A dated system note such as
  `wiki/_compiler_health_route_review_YYYY-MM-DD.md`.
- A ranked "next fixes" section with evidence from route tests.

Completion note - 2026-05-31:

- Created `wiki/_compiler_health_route_review_2026-05-31.md`.
- Benchmarked practitioner reports, safety red flags, whole-system questions,
  Source/science claims, service/behavior questions, provenance questions, and
  domain-overview questions against the startup index, catalog, lint
  diagnostics, largest pages, no-inbound page, broad-domain warnings, and
  high-load judgment surfaces.
- Applied small routing fixes only: added a direct
  [[Source Science And Analogy Boundary]] startup route, linked
  [[Yearlong Solitary Retreat Carrying Text]] from [[Practice Cycles]], and
  compressed the index dashboard backlog wording so lint's 72 raw-source
  residuals are visible without becoming this automation's ingest queue.
- Deferred judgment-page edits to Workstream B and principal-source-count plus
  broad-domain cleanup to Workstream C.

## Workstream B - Judgment Surface Pass

Goal: separately strengthen the pages future agents will lean on when a real
practice or safety judgment is at stake.

Primary pages:

- [[Current Model]]
- [[Practice Guidance Toolkit]]
- [[Complete Experience Safety Boundary]]
- [[Guidance Scope and Accountability Boundary]]

Minimum scope:

- Route-test concrete cases before editing: ordinary method choice, physical
  pain, emotional eruption, no-self/void distress, teacher pressure, behavior
  not improving, Source/science overclaim, and applied-life/medical-adjacent
  reports.
- Tighten openings, decision maps, stop/refer criteria, source posture, and
  related links where route tests expose friction.
- Keep this pass separate from broad source-anchor cleanup so safety and
  judgment quality stay central.

Completion note - 2026-05-31:

- Created `wiki/_compiler_health_judgment_surface_review_2026-05-31.md`.
- Route-tested ordinary method choice, physical pain, emotional eruption,
  no-self/void distress, teacher pressure, behavior-not-improving,
  Source/science overclaim, and applied-life/medical-adjacent reports against
  [[Current Model]], [[Practice Guidance Toolkit]], [[Complete Experience
  Safety Boundary]], and [[Guidance Scope and Accountability Boundary]].
- The first six and the applied-life/medical-adjacent route passed with no
  structural edit needed; the Source/science overclaim route needed explicit
  evidence-tier links inside the judgment pages.
- Patched those pages so science, AI, ultrasound, neurotechnology, physics,
  mathematics, energy, cure, safety-guarantee, and evidence-proof claims route
  through [[Source Science And Analogy Boundary]] before technique, safety,
  service, or guidance authority is inferred.
- Deferred principal-source-count cleanup and broad-domain warnings to
  Workstream C.

## Workstream C - Source-Anchor And Domain-Bloat Pass

Goal: comprehensively handle the current structural lint debt without
pretending every advisory must become a content page.

Current source-anchor advisory targets:

- [[Expansion And Contraction]]
- [[Guidance Scope and Accountability Boundary]]
- [[Lineage Translation]]
- [[Mysticism As Concentration]]
- [[No-Self And Personality]]
- [[Source And Polarities]]
- [[Source Science And Analogy Boundary]]
- [[Total Happiness Behavior And Service Test]]

Minimum scope:

- For each advisory still present, decide whether to trim frontmatter to
  eight or fewer principal raw anchors and move secondary anchors into a body
  `Source Anchors` section, or justify the exception in this plan.
- Recheck broad-domain warnings for `practice`, `primary`, `safety`,
  `service`, `sources`, `teaching`, and `transformation`.
- Create or update sub-index/router surfaces only when they improve first-load
  routing. Otherwise record the residual warning as accepted debt with a
  reason.

Completion note - 2026-05-31:

- Created `wiki/_compiler_health_source_anchor_domain_review_2026-05-31.md`.
- Resolved the principal-source-count advisories for [[Expansion And
  Contraction]], [[Guidance Scope and Accountability Boundary]], [[Lineage
  Translation]], [[Mysticism As Concentration]], [[No-Self And Personality]],
  [[Source And Polarities]], [[Source Science And Analogy Boundary]], and
  [[Total Happiness Behavior And Service Test]].
- Added or refreshed body `Source Anchors` so secondary evidence remains
  discoverable without making frontmatter act as a bibliography.
- Rechecked broad-domain warnings for `practice`, `primary`, `safety`,
  `service`, `sources`, `teaching`, and `transformation`; no new sub-index was
  created because the existing index, catalog, and hubs already provide
  first-load routes and the remaining warnings are accepted residual
  diagnostics rather than current routing failures.
- `tools\wiki_lint.cmd` exits OK with accepted residual diagnostics only: 72
  raw-source backlog paths and the seven broad-domain warnings above.

## Terminal Stop Condition

When A, B, and C are complete:

1. Mark all rows in this plan complete.
2. Run `tools\wiki_lint.cmd`.
3. Update the automation memory with the final status.
4. Pause `shinzen-compiler-health-loop` if automation tooling or filesystem
   permission allows it.
5. Report completion and stop. Do not continue into raw-source ingest or the
   `practice-wisdom-backlog`.

Completion note - 2026-05-31:

- Rows A, B, C, and Stop automation are complete.
- `tools\wiki_lint.cmd` exits OK with only accepted residual diagnostics.
- The automation memory was updated in the final run.
- `tool_search` did not expose an `automation_update` tool in this session;
  the local automation file at
  `C:\Users\Urgen\.codex\automations\shinzen-compiler-health-loop\automation.toml`
  already has `status = "PAUSED"`.
- No source ingest, `practice-wisdom-backlog`, `defer-query-driven`,
  `skip-manifest-only`, or `upgrade-existing` work was opened.
