# Public Atlas Completion Audit - 2026-06-05

This is an internal completion audit for the public atlas/compiler-delta
workstream. It is not evidence for Shinzen claims. It records whether the
current `public-atlas/` draft satisfies the user's objective: use the strong
internal compiler to make the public atlas much more valuable for serious
meditation practitioners while preserving a human-readable public register.

## Problem Representation

The strongest representation is:

> Turn the compiler's source-calibrated practice intelligence into a public
> practitioner decision interface.

The compiler's value is not that it contains many pages. Its value is that it
knows how to route live practice questions: what to notice, which method or
boundary applies, what claim tier is active, when to stop optimizing
meditation, when to ask for help, and how behavior and service test private
experience.

The atlas succeeds when a serious practitioner can enter with a real problem,
find a public page that preserves the relevant Shinzen-specific distinction,
and leave with a wiser next move without being exposed to internal source
machinery.

## Evidence Read

- `AGENTS.md` defines the compiler objective: prioritize practice handles,
  phenomenological distinctions, technique routing, teaching moves,
  transformation mechanisms, safety/service boundaries, and source-use tiers.
- `wiki/index.md` identifies the internal current model and live guidance
  routing surfaces.
- `wiki/_public_atlas_orientation.md` records the atlas architecture,
  editorial passes, reader-route tests, source/citation trust pass, and the
  final Asking for Guidance pass.
- `wiki/_public_atlas_compiler_to_atlas_gap_audit_2026-06-05.md` identifies
  and closes the last explicit compiler-to-atlas gap from the focused audit.
- `public-atlas/index.md`, `public-atlas/map.md`, and
  `public-atlas/glossary.md` provide first-load, lookup, and term-first
  routing evidence.
- Selected path and boundary pages were sampled for public register and
  decision-surface quality: `the-one-move.md`, `the-three-skills.md`,
  `impermanence-path.md`, `no-self-without-erasing-the-person.md`,
  `going-deep-safely.md`, `source-and-claim-tiers.md`, and
  `how-to-read-this-site.md`.

## Completion Requirements

| Requirement from objective | Current evidence | Finding |
| --- | --- | --- |
| Restate the problem in a stronger representation | This audit states the objective as translating compiler practice intelligence into a public practitioner decision interface. | Satisfied. |
| Transfer compiler value rather than merely summarize Shinzen | The atlas now has 87 public content pages: 1 home, 10 pillars, 48 practice pages, and 28 boundary/reference pages. It covers practice handles, method choice, CCE, See/Hear/Feel, Five Ways, Flow/Gone, no-self, Source, Total Happiness, behavior/service, guidance, safety, applied life, and source tiers. | Satisfied for current public atlas scope. |
| Preserve serious-practitioner usefulness | Homepage problem rows, full-map rows, and glossary route checks cover live practitioner jobs: method choice, weekly planning, pain/intensity, equanimity versus suppression, Flow/Gone/dissolution, retreat aftercare, no-self/void, Walls/Windows, behavior non-change, asking for guidance, teacher claims, and source/claim trust. | Satisfied by route evidence. |
| Preserve public human-readable register | Sampled public pages open with practice meaning and decision surfaces, not internal audit prose. Leak scans show no internal frontmatter fields, claim IDs, Obsidian wikilinks, or source-audit machinery in public pages. | Satisfied mechanically and by sample read. |
| Identify and close missing pages or important claims | The 2026-06-05 gap audit closed Windows and Walls, Practice Report Check, Practice Planning Loop, Retreat and Aftercare, Behavior Change Escalation, Source/Claim Trust, and Asking for Guidance. It now says no new page should be added without a fresh route failure. | Satisfied by current audit chain. |
| Keep claims calibrated | `source-and-claim-tiers.md` and `how-to-read-this-site.md` now name source families, compact source trails, quotation posture, and tiers: Shinzen says, compiled synthesis, editorial inference, speculative extension, and not established here. | Satisfied for the current Markdown draft. |
| Preserve safety, scope, behavior, service, and teacher boundaries | Public pages route safety through `going-deep-safely.md`, `safety-scope-and-accountability.md`, `practice-method-safety.md`, `guidance-scope-and-accountability.md`, DPDR/dissolution/intensity pages, behavior/service tests, and the new guidance-prep page. | Satisfied by route and page evidence. |
| Avoid turning the atlas into an encyclopedia or transcript archive | Current atlas pages are organized around practice routes, mechanisms, boundary pages, and reader jobs; the final gap audit explicitly rejects generic Buddhist-topic or transcript-derived noun expansion. | Satisfied for current content. |
| Plan, execute, and check | The orientation and log record the plan/execution chain. Validation checks after the final pass showed page count 87, relative links OK, internal-leak scan OK, non-ASCII scan OK, and `tools\wiki_lint.cmd` OK with expected diagnostics. | Satisfied. |

## Reader Route Tests

| Reader job | Public route evidence | Result |
| --- | --- | --- |
| "I want the whole system in human order." | `index.md` routes through the ten-part path beginning with `the-one-move.md`. | Pass. |
| "I am choosing or tuning a practice." | `index.md` routes to `the-routes.md`, then `choosing-a-practice-route.md`, `practice-report-check.md`, and `practice-method-safety.md`. | Pass. |
| "I want a sane week or month." | `index.md` and `map.md` route to `practice-planning-loop.md`, practice cycles, route choice, and report check. | Pass. |
| "I need to ask a teacher or helper without handing over judgment." | `index.md`, `map.md`, and `glossary.md` route to `asking-for-guidance.md`, with report, guidance-scope, and teacher-lineage companions. | Pass. |
| "Equanimity feels like numbness or force." | `index.md` routes to the skills chapter, suppression boundary, and equanimity ladder. | Pass. |
| "Flow, Gone, vibration, or dissolution is showing up." | `index.md` routes to the impermanence pillar, Flow/Gone, dissolution/bhanga, and altered-phenomena safety. | Pass. |
| "A retreat or long sit changed something." | `index.md`, `map.md`, and `glossary.md` route to `retreat-and-aftercare.md` with reaction recycling, safety, and planning companions. | Pass. |
| "No-self, void, or Source feels powerful or destabilizing." | `index.md` routes through no-self, Source/Zero, and Going Deep Safely; glossary routes no-self/void terms to DPDR and claim tiers. | Pass. |
| "A life event feels like a Wall or Window." | `index.md`, `map.md`, and `glossary.md` route to safety, Windows/Walls, applied-life boundaries, and guidance scope. | Pass. |
| "Insight appears, but behavior is not changing." | `index.md`, `map.md`, and `glossary.md` route to `behavior-change-escalation.md`, behavior/service test, guidance scope, and report check. | Pass. |
| "Is this sourced, synthesized, inferred, speculative, proof, or authority?" | `index.md`, `map.md`, `glossary.md`, and `how-to-read-this-site.md` route to `source-and-claim-tiers.md` and source/science boundaries. | Pass. |
| "Can I trust a teacher, attainment, transmission, or service claim?" | `map.md` and `glossary.md` route through teacher/lineage, asking for guidance, guidance scope, behavior/service, and source tiers. | Pass. |

## Negative Checks

- No public page should expose internal wiki machinery. Leak scan after the
  final guidance-prep pass returned OK.
- No public page should rely on Obsidian wikilinks. Relative Markdown link
  check returned OK.
- No public page should drift into Unicode punctuation by accident. Non-ASCII
  scan returned OK.
- Internal wiki invariants should still pass after internal audit-note edits.
  `tools\wiki_lint.cmd` returned OK with the expected raw backlog and broad
  domain diagnostics.
- The user explicitly said not to worry about README. This audit does not
  treat `public-atlas/README.md` as part of the content completion claim.

## Residual Non-Goals

This audit does not claim that the atlas is legally or commercially ready for
publication, that external readers have user-tested it, that formal citation
style and rights policy are final, that the site has a static framework, or
that the atlas can provide individualized medical, clinical, legal, crisis,
or teacher-credentialing guidance.

Those are publication and governance questions. They are not remaining
compiler-to-atlas information-value gaps unless a future user asks for public
release readiness.

## Verdict

The core compiler-to-atlas objective is complete in the current Markdown
atlas. The atlas now functions as a public practitioner decision interface
rather than a thin summary or an exposed internal compiler. No
high-confidence missing public page or important compiler-derived claim
remains from the current audits.

Future work should be user-directed and should start from a concrete route
failure, external reader feedback, formal citation/rights requirements, or
site-readiness requirements rather than automatic expansion.
