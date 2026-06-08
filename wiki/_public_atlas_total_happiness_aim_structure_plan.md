# Public Atlas Total Happiness Aim Structure Implementation Plan

Created: 2026-05-31

Status: complete as of 2026-05-31. This file remains the Phase 1 contract and
handoff record; continue future automation from
`wiki/_public_atlas_human_delta_coverage_plan.md`.

This is an internal implementation plan for the next load-bearing
compiler-to-atlas inclusion. It is not evidence for Shinzen claims. Use the
internal compiled pages named here for source posture, then write public atlas
pages in ordinary Markdown.

Broader governing plan: `wiki/_public_atlas_human_delta_coverage_plan.md`.
This file remains the exact Phase 1 contract for the Total Happiness aim
structure page inside that larger human-facing compiler-delta coverage
program.

## Objective

Promote the internal [[Total Happiness Aim Structure]] model into the public
atlas so readers can understand what Shinzen's system is aiming at before
they interpret technique, transformation, Source/service, or behavior claims.

The public atlas currently says Total Happiness is surface and deep happiness
for self and others. That is true but too compressed. The missing public
delta is the fuller aim architecture:

- three jobs: appreciate self/world, transcend self/world, improve
  self/world;
- four quadrants: surface and deep happiness for self and others;
- five applications: reduce suffering, elevate fulfillment, understand self,
  change behavior, and cultivate or discover love/service;
- ordinary and extraordinary happiness;
- the periodic-table-of-happiness teaching move, kept in a careful claim
  tier;
- the reciprocal rule that improving self/world can support transcendence,
  not only follow it.

## Recommended Product Decision

Create a new public page:

`public-atlas/total-happiness-aim-structure.md`

Keep `public-atlas/total-happiness.md` as the shorter hub. Link the hub to
the new aim-structure page rather than turning the hub into a dense taxonomy
page.

Rationale:

- The aim structure is a durable public job in its own right.
- A separate page keeps `total-happiness.md` readable.
- The atlas already uses compact hub plus specialized page patterns.
- The new page can route readers who ask "what is practice for?" without
  forcing them through behavior/safety pages first.

## Required Inputs

Read in this order:

1. `AGENTS.md`
2. `public-atlas/README.md`
3. `wiki/_public_atlas_orientation.md`
4. `wiki/_public_atlas_loadbearing_delta_review_2026-05-31.md`
5. `wiki/Total Happiness Aim Structure.md`
6. `wiki/Total Happiness.md`
7. `wiki/Total Happiness Behavior And Service Test.md`
8. `wiki/Condition-Independent Happiness.md`
9. `wiki/Source And Service Boundary.md`
10. Target public pages only as needed:
    `public-atlas/total-happiness.md`,
    `public-atlas/behavior-and-service-test.md`,
    `public-atlas/source-service-and-bodhicitta.md`,
    `public-atlas/condition-independent-happiness.md`,
    `public-atlas/way-of-human-goodness.md`,
    `public-atlas/index.md`,
    `public-atlas/glossary.md`.

Do not reopen raw sources unless a public claim needs source-level checking.
The compiled owner pages are the source of judgment for this pass.

## Public Page Contract

Use ordinary Markdown and minimal public frontmatter:

```markdown
---
title: Total Happiness Aim Structure
atlas_type: transformation
status: draft
---
```

Suggested shape:

1. Plain opening claim.
2. Why this matters.
3. The aim map, with one compact table.
4. Three jobs.
5. Four quadrants.
6. Five applications.
7. Ordinary and extraordinary happiness.
8. How it shows up in practice.
9. Common confusions.
10. Safety and scope.
11. Source posture.
12. Source trail.
13. Next reading.

Avoid internal wiki language: no `load_when`, `best_linked_pages`, claim IDs,
Model Delta, Integration Notes, or Obsidian wikilinks.

## Public Claims To Carry

The page should preserve these distinctions in public prose:

- Total Happiness is not one goal but a family of aim maps.
- Appreciating self/world means complete sensory contact with inner and outer
  form, not suppressing life.
- Transcending self/world means Source/Zero/no-self-facing practice, not
  rejection of ordinary conditions.
- Improving self/world means behavior, support, material help, service,
  teaching, repair, and ordinary competence.
- Surface happiness remains legitimate; deep happiness does not make ordinary
  needs expendable.
- Service to others is part of Total Happiness, but service must remain
  consented, competent, feedback-sensitive, and behavior-accountable.
- The five applications make the aim practical: suffering, fulfillment,
  self-understanding, behavior, and love/service should become more workable.
- The periodic-table-of-happiness language is a teaching strategy and
  dimensional map, not empirical proof of a universal happiness science.
- Improvement can support transcendence when formal practice is stuck:
  ethics, lifestyle, reduced conflict, service, exercise, diet, or ordinary
  repair may help practice move again.

## Link Updates

After creating the page, update:

- `public-atlas/total-happiness.md`
  - Add a short section or sentence pointing to the new aim-structure page.
  - Add the new page under `Next Reading`.
- `public-atlas/index.md`
  - Add the new page in the relevant Start-by-problem row for deep happiness,
    behavior/service, or system overview.
  - Add the new page under Transformation in `Main Sections`.
- `public-atlas/glossary.md`
  - Expand the Total Happiness entry or add `Total Happiness aim structure`.
  - Add route-check support if needed.
- `public-atlas/behavior-and-service-test.md`
  - Add the new page under `Next Reading`.
- `public-atlas/source-service-and-bodhicitta.md`
  - Add the new page under `Next Reading`.
- `public-atlas/what-shinzens-system-is.md`
  - If the architecture table or life-test paragraph feels too thin, add the
    new page as a life-test or transformation link.

Optional, only if natural:

- `public-atlas/condition-independent-happiness.md`
- `public-atlas/way-of-human-goodness.md`
- `public-atlas/deconstruction-and-reconstruction.md`

Do not add links where they do not improve the reader's next move.

## Reader Route Tests

After edits, simulate these reader starts from `index.md` and `glossary.md`:

1. "What is the whole system actually for?"
2. "Is Shinzen saying ordinary happiness matters or only deep happiness?"
3. "How do behavior change and service fit meditation?"
4. "Can improving life conditions help transcendence?"
5. "Does Source contact prove love, ethics, or service?"

Expected result:

- A reader can reach `total-happiness-aim-structure.md` within one or two
  clicks for questions 1-4.
- Question 5 routes through `source-service-and-bodhicitta.md`,
  `behavior-and-service-test.md`, or `source-and-claim-tiers.md`, with the
  new aim-structure page supporting but not replacing those boundaries.

## Validation

Run:

```powershell
(Get-ChildItem -File public-atlas -Filter *.md | Where-Object { $_.Name -ne 'README.md' } | Measure-Object).Count

$files = Get-ChildItem -File public-atlas -Filter *.md | Where-Object { $_.Name -ne 'README.md' }
$known = @{}
foreach ($f in $files) { $known[$f.Name] = $true }
$bad = @()
foreach ($f in $files) {
  $text = Get-Content -LiteralPath $f.FullName -Raw
  $matches = [regex]::Matches($text, '\[[^\]]+\]\(([^)]+)\)')
  foreach ($m in $matches) {
    $target = $m.Groups[1].Value
    if ($target -match '^(https?:|mailto:|#)') { continue }
    $path = $target.Split('#')[0]
    if (-not $known.ContainsKey($path)) { $bad += "$($f.Name) -> $target" }
  }
}
if ($bad.Count) { $bad | Sort-Object -Unique } else { 'OK' }

rg -n --glob '!README.md' "load_when|best_linked_pages|Model Delta|Integration Notes|Agent Use Contract|\[\[|\]\]|agent-facing|compiler wiki|source-audit machinery" public-atlas

rg -n "[^\x00-\x7F]" public-atlas wiki/_public_atlas_orientation.md wiki/_public_atlas_total_happiness_aim_structure_plan.md

tools\wiki_lint.cmd
```

Expected results:

- public atlas content count is 66 after the new page is deliberately added;
- relative Markdown link check prints `OK`;
- internal-leak scan prints no matches;
- non-ASCII scan prints no matches unless intentionally added;
- `tools\wiki_lint.cmd` is OK with expected diagnostics.

## Log And Handoff Updates

After implementation:

- Append one newest-first `wiki/log.md` entry.
- Update `public-atlas/README.md` current state to say the Total Happiness
  aim-structure inclusion is complete.
- Update `wiki/_public_atlas_orientation.md` current state and priority queue.
- If this plan is complete, mark the completion status in this file rather
  than deleting it.

## Completion Criteria

This plan is complete only when:

- `public-atlas/total-happiness-aim-structure.md` exists and carries the
  three jobs, four quadrants, five applications, ordinary/extraordinary
  happiness, periodic-table caution, and improve-supports-transcend rule.
- The hub and route pages link to it where reader navigation requires it.
- Reader route tests show the page is reachable from `index.md` and
  `glossary.md` for the main aim questions.
- Validation checks pass with expected diagnostics.
- Handoff surfaces and log are updated.

Completion note, 2026-05-31: `public-atlas/total-happiness-aim-structure.md`
was created and linked from the hub, index, glossary, system overview,
behavior/service, Source/service, condition-independent happiness, and Human
Goodness pages. The next active delta is Teaching As Service Ladder under the
broader human-delta coverage plan.

## Next Deltas After This Plan

Do not start these until the Total Happiness aim-structure inclusion is
complete and validated:

1. Teaching as service ladder.
2. Auto Output practice family.
3. Discrimination and unification / empowering contrasts.
4. Applied life boundaries.
