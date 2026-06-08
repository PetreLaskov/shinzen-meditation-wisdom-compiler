# Public Atlas Handoff

Created: 2026-05-28

This folder is a Markdown-only public draft of the Shinzen Practice Atlas. It
is separate from the internal `wiki/` compiler layer. The internal wiki is
the agent-facing compiled memory system; this folder is the human-facing
public branch draft.

For detailed chronology, use `../wiki/_public_atlas_orientation.md` and
`../wiki/log.md`. This README is the compact operational handoff.

## Current State

- 90 public-facing Markdown pages exist, plus this handoff README.
- Current tier count: 1 home, 10 pillar pages, 51 practice pages, and 28
  boundary/reference pages including legacy redirect stubs.
- The ten-part path is the public spine:
  `index.md`, `the-one-move.md`, `the-three-skills.md`,
  `the-sensory-interface.md`, `the-routes.md`, `impermanence-path.md`,
  `no-self-without-erasing-the-person.md`,
  `source-zero-and-the-honest-edge.md`, `the-return.md`, `the-aim.md`, and
  `going-deep-safely.md`.
- `map.md` is the full lookup shelf. `glossary.md` is the term-first route.
  `how-to-read-this-site.md` holds the public claim-tier and safety posture.
- The completed human-delta coverage work brought forward the major
  compiler-to-atlas deltas: Total Happiness aim structure, teaching as
  service, Auto Output, discrimination/unification, applied-life boundaries,
  Surface-to-Source path mapping, and mindfulness/mysticism clarifications.
- The completed editorial-transmission passes strengthened reader paths,
  foundation pages, practice examples, adept-reader boundaries, and
  source/safety posture.
- On 2026-06-05, `windows-and-walls.md` was added as a public boundary page
  for Shinzen's Wall/Window guidance frame. It routes life openings,
  obstacles, severe events, behavior problems, and "life as monastery"
  language through objective situation, objective behavior, sensory
  challenge, support, safety, and accountability before technique enthusiasm.

## Next Best Work

- **Register / voice thorough pass (ACTIVE)**: removing the one uniform
  editorial template across ~90 pages. Step 0 (ASCII policy) is settled and the
  three gold exemplars are complete as of 2026-06-05 - `the-one-move.md`,
  `noting.md`, and `equanimity-versus-suppression.md` - now the live few-shot
  anchor. The register's deepened section, "Carry the movement through to the
  cut", governs the rest: cut safety language to the failure mode that bites,
  but keep reference and decision density via progressive disclosure (thesis and
  cut first, the exhaustive table or taxonomy beneath for the careful reader),
  and aim for a direct pointing-out only at the rare pages where the material
  opens. Phase 2 (the spine: home + ten pillars) is complete as of 2026-06-05 -
  `index.md` and nine pillars fully voice-rewritten, `the-one-move.md` kept as
  the Step 1 anchor, validation clean (ASCII, no leaks, 90 pages, links OK).
  Phase 3 (the long tail, 77 pages) RE-SCOPED 2026-06-06: bring every tail page to
  the same bar the spine got - a full voice-rewrite passing all four probe
  questions, openers and body prose in scope - not the mechanical tic-fixes
  (closer + tables + safety) the long tail was first given. The tic-pass ran
  across clusters A-F (39 pages) and reaches only the grid-and-coda surface; it
  never touches the opener or the flat body sentences (probe Q1 mold-reshape and
  Q2 skim-test stayed dormant). So all 77 tail pages now need the deepening bar:
  re-deepen A-F (opener + body only; their tables/safety are done), then
  full-treat G-K. 90 pages stay stable (voice and shape only; the editorial
  plan's page-merge architecture is not reopened). Start at
  `../wiki/_atlas_register.md`; read the deepened "Carry the movement through to
  the cut" section, the gold triad, and the re-scoped Step 3 block (two-layer
  method + per-cluster progress) before editing, and do not re-flatten the
  spine's deliberate variety. Do this before the source or site work below.
- **Source/citation/rights pass**: decide quote policy, source citation
  style, and public source posture before internet publication.
- **Site-readiness pass**: decide static-site framework, metadata,
  navigation, and public launch posture after substance and source policy are
  stable.
- **Scenario/example pass**: continue only when a real reader route still
  feels ambiguous. Do not reopen broad expansion merely because an internal
  concept exists.

## Validation Checks

Run these after atlas edits:

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

rg -n --glob '!README.md' "load_when|best_linked_pages|Model Delta|Integration Notes|Agent Use Contract|\[\[|\]\]|agent-facing|compiler wiki|source-audit machinery|claim ID|S[0-9]+:" public-atlas

rg -n "[^\x00-\x7F]" public-atlas wiki/_public_atlas_orientation.md wiki/_public_atlas_editorial_release_deepening_plan_2026-06-01.md
```

If internal `wiki/` files change, also run:

```powershell
tools\wiki_lint.cmd
```

Expected results:

- content page count is 90;
- relative Markdown link check prints `OK`;
- internal-leak search prints no matches;
- non-ASCII search prints no matches unless a future editor intentionally
  adds Unicode;
- wiki lint is OK with the expected raw backlog and broad-domain diagnostics.

## Boundaries

- Do not edit `raw/` for public-atlas work.
- Do not turn the internal `wiki/` into the public atlas.
- Do not add a static-site framework until Markdown content is worth
  publishing.
- Do not publish long quotations or raw transcript text until rights and
  quotation policy are settled.
- Do not hide safety, source tier, behavior, consent, teacher accountability,
  clinical/medical scope, or service boundaries.
