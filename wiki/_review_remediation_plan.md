# Review Remediation Plan

Seeded 2026-05-12 from
`gpt-pro-review/GPT review output/shinzen_wiki_agent_memory_audit.md`.

This is a maintenance plan for restoring the compiler's routing efficiency
without damaging its accumulated practice model. It is not a Shinzen content
page and should not be cited as evidence for domain claims.

## Purpose

The review's central diagnosis is that the wiki's compiled content is mostly
strong, but the routing layer is starting to behave like an archive again.
Remediation should therefore prioritize cheaper first loads, clearer safety
and guidance routing, tighter frontmatter, and better backlog triage before
adding more synthesis prose.

## Operating Guardrails

- Preserve source fidelity and existing content value. Do not compress away
  practice handles, teaching moves, tensions, uncertainty, or safety caveats.
- Prefer small, reviewable edits over broad rewrites. A pass that touches more
  than five content pages needs an explicit old-to-new mapping and validation
  note.
- Treat router pages as load-bearing infrastructure. Edit `wiki/index.md`,
  `[[Current Model]]`, `[[Practice Guidance Toolkit]]`, and
  `[[Complete Experience Safety Boundary]]` only after reading the relevant
  opening, key points, and routing sections.
- Do not use automated bulk frontmatter rewrites. Compress one page or one
  coherent batch at a time, then run lint.
- Keep claims calibrated. Source, science, clinical, metaphysical,
  teacher-competence, and behavior-improvement claims must keep their source
  posture.
- Safety overrides technique optimization. Any routing change for live
  guidance should make red flags easier to notice, not merely make the index
  shorter.
- Each phase ends with `tools\wiki_lint.cmd` and a short log entry when wiki
  files change.

## Phase 0 - Planning And Baseline

Status: in progress.

Goal: turn the external audit into an internal plan before editing content.

Steps:

1. Record the audit source, core diagnosis, and conservative guardrails here.
2. Run a router simulation before major index surgery.
3. Capture baseline diagnostics from lint.
4. Decide the first content-edit batch only after the simulation shows which
   routing failures are most costly.

Validation:

- Plan exists as a system artifact.
- `wiki/log.md` records the planning pass.
- Lint still passes after plan/log edits.

Stop condition:

- If lint now treats this file as a compiled page, either rename the file or
  add the minimum required registration deliberately.

## Phase 1 - First-Load Router And Safety Visibility

Goal: make the first screen answer "what should I load next?" without moving
large bodies of content yet.

Small candidate edits:

1. Add a compact live-guidance rule near the top of `wiki/index.md`:
   concrete practitioner report -> load `[[Practice Guidance Toolkit]]`;
   red flags -> load `[[Complete Experience Safety Boundary]]` before
   technique optimization.
2. Add or tighten a short safety override rule in `wiki/_operations.md` if the
   router simulation shows future agents could miss it.
3. Add a small "what to load next" table to the index opening only if it
   replaces existing bulk rather than adding more startup text.
4. Clean any stale integration phrasing found during the pass only when the
   page is already being read for another reason.

Validation:

- Index opening becomes more discriminating without growing materially.
- No source claims change.
- Lint passes.

Stop condition:

- If index editing starts requiring domain-list moves, stop and promote Phase
  2 instead of doing an ad hoc partial refactor.

## Phase 2 - Router Simulation Benchmark

Goal: test the compiler as future agents actually use it.

Run 8 to 12 representative queries and record:

- query;
- first page loaded;
- second page loaded;
- whether safety/source posture appears soon enough;
- where the answer would become overconfident or under-evidenced.

Initial query set:

1. A practitioner reports strong physical pain in sitting.
2. A practitioner reports emotional eruption and fear during noting.
3. A practitioner reports no-self or "paper-thin world" distress.
4. Someone asks which Shinzen method they should use first.
5. Someone asks whether Source is literally real or scientifically supported.
6. A teacher's behavior or pressure seems suspect.
7. A practitioner says practice feels profound but behavior is not improving.
8. A source-level provenance question asks where a specific claim came from.
9. A future ingest asks what raw source should be next.

Output target:

- a short `review` log entry or a dedicated section in this file;
- a ranked list of the top routing changes worth making.

## Phase 3 - Catalog Delegation And Index Surgery

Goal: make `wiki/index.md` a router again while keeping full lists findable.

Candidate artifacts:

- `[[Sources Catalog]]` or a system catalog if it should not be a content page.
- practice architecture/routes catalog surface.
- transformation mechanisms catalog surface.
- safety/frontiers catalog surface.
- teaching/service catalog surface.

Conservative sequence:

1. Create the catalog surface first.
2. Move one domain's long list at a time.
3. Leave a short index summary and the highest-value entries.
4. Run lint after each domain move.
5. Only then trim the long gate chronology from the index opening.

Stop condition:

- If link registration rules make the main index unreadable, refactor the
  registration/lint mechanism before forcing more content into the index.

## Phase 4 - Current Model Card

Goal: keep the whole-system model available without requiring future agents
to load the full evidence/gate chronology.

Preferred first attempt:

- Add a strict `## Current Model Card` at the top of `[[Current Model]]`.
- Preserve the detailed page below it.
- Do not split the page until the card has proven useful and the router
  simulation shows the detailed page is still too expensive.

Card should include:

- one-sentence current model;
- 4 to 6 routing rules;
- confidence tiers;
- top safety and evidence frontiers;
- links to `[[Practice Guidance Toolkit]]` and
  `[[Complete Experience Safety Boundary]]`.

Stop condition:

- If card drafting duplicates half the page, split to a separate evidence page
  instead of creating another mini-book.

## Phase 5 - Safety Matrix And Accountability Surface

Goal: convert existing safety visibility into executable routing.

Candidate edits:

- Add a red/yellow/green safety matrix to
  `[[Complete Experience Safety Boundary]]`.
- Promote `[[Guidance Scope and Accountability Boundary]]` if router
  simulation shows teacher/accountability questions need a first-tier surface.
- Create `[[Behavior Verification and Teacher Accountability]]` only if the
  existing pages cannot own the conduct, feedback, role clarity, referral,
  repair, and anti-dependency criteria cleanly.

Stop condition:

- Do not create a new page just because the review named it. First check
  whether an existing page can be strengthened without fragmentation.

## Phase 6 - Frontmatter Compression

Goal: restore frontmatter as a triage card, not a hidden evidence map.

Order:

1. Pages already flagged by lint: `[[Equanimity]]`, `[[Flow]]`,
   `[[No-Self And Personality]]`, `[[Sensory Clarity]]`,
   `[[Source And Polarities]]`, and `[[Total Happiness]]`.
2. Near-threshold routers: `[[Basic Mindfulness Practice Architecture]]`,
   `[[See Hear Feel Introduction - Practice Organization and System Transition]]`,
   `[[Turn Toward and Turn Away]]`, and `[[Practice Guidance Toolkit]]`.

Rules:

- Keep only principal source anchors in non-source frontmatter.
- Move exhaustive evidence maps into body sections or source-anchor lists.
- Keep `load_when` discriminating and short.
- Keep `best_linked_pages` to the strongest next loads.

Validation:

- Lint advisories decrease.
- The opening and key points still carry enough context to route.

## Phase 7 - Lint Safeguards

Goal: make drift visible before it becomes structural debt.

Small checks to add first:

- warn at `load_when > 320` and strongly warn above the current high threshold;
- warn at `best_linked_pages > 8`;
- warn at non-source `sources > 8`;
- warn when the index opening through `Open Questions` exceeds the agreed
  budget;
- detect stale future-tense `Integration target` phrasing when completed
  `Integration Notes` are present.

Later checks:

- large-page advisories by type;
- safety-risk keywords without safety-boundary links;
- duplicate `Dependencies`/`Related` links;
- unresolved source claim IDs;
- YouTube source page required-section checks.

## Phase 8 - Backlog Triage

Goal: make the 77-source backlog less likely to distort confidence.

Triage by future practice-reasoning value and safety/accountability risk, not
by ingest order alone.

Risk buckets:

- safety/clinical;
- teacher/accountability;
- practice routing/dosage;
- altered phenomena/dissolution;
- Source/metaphysics/science speculation;
- service/behavior verification;
- future science/neurotechnology.

Output target:

- a backlog triage table with a next-source recommendation and a reason;
- index dashboard updated only with a compact summary.

## Current Next Step

After Phase 0 validation, the next conservative move is Phase 2 router
simulation, then a minimal Phase 1 index/safety router edit based on the
simulation. Major index surgery, owner-page splits, and backlog re-ranking
should wait until those smaller checks show exactly what is failing.
