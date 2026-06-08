# Review Remediation Plan

Seeded 2026-05-12 from
`gpt-pro-review/GPT review output/shinzen_wiki_agent_memory_audit.md`.

This is a maintenance plan for restoring the compiler's routing efficiency
without damaging its accumulated practice model. It is not a Shinzen content
page and should not be cited as evidence for domain claims.

Post-ingest status note, 2026-05-16: this plan remains useful history for the
first router/safety/frontmatter remediation pass, but the current work is now
governed by `wiki/_post_ingest_knowledge_health_plan.md`. The YouTube
transcript-video ingest set is substantively complete, so the next priority is
compiled knowledge health: router benchmarking, catalog-backed index surgery,
hub-and-child page decomposition, redundancy cleanup, and editorial polish.

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

Status: completed 2026-05-12 for baseline and first router benchmark.

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

Status: minimal first pass applied 2026-05-12 after router simulation; larger
table/catalog work remains pending.

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

Status: first benchmark completed 2026-05-12.

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

### Simulation Run - 2026-05-12

Baseline lint passed before edits with 212 compiled pages and 225 raw sources
checked. Diagnostics retained the expected 77-source backlog, six oversized
frontmatter-source advisories, and large-domain advisories.

| Query | First Page Loaded | Second Page Loaded | Posture Timing | Costliest Failure Mode |
| --- | --- | --- | --- | --- |
| Strong physical pain in sitting | [[Practice Guidance Toolkit]] | [[Intensity and Embodiment Safety Boundary]] or [[Turn Toward and Turn Away]] | Safety is strong once the toolkit loads, but the index did not make the live-report route explicit enough. | Medical, posture, teacher-pressure, or endurance red flags could be optimized as technique too soon. |
| Emotional eruption and fear during noting | [[Practice Guidance Toolkit]] | [[Intensity and Embodiment Safety Boundary]] or [[Practice Method Safety Boundary]] | Adequate after the second page. | Trauma, panic, self-harm, or clinical signs remain under-specified and need safety routing before decomposition advice. |
| No-self or "paper-thin world" distress | [[Complete Experience Safety Boundary]] | [[DPDR and the Pit of the Void]] | Safety should appear immediately, but the pre-edit index could tempt loading [[Operational Enlightenment]] first. | Emptiness content alone could be over-read as realization instead of being classified by valence, function, support, and clinical differential. |
| Which Shinzen method should I use first? | [[Practice Entry and Method Choice]] | [[Practice Guidance Toolkit]] | Good; safety and fit appear early in both pages. | "Whatever works" can become under-evidenced unless outcome, behavior, and support criteria are named. |
| Is Source literally real or scientifically supported? | [[Source And Polarities]] | [[Current Model]] or [[Complete Experience Safety Boundary]] | Good once loaded; Source posture appears in the opening. | The page's oversized frontmatter makes first load expensive, and science/metaphysics claims need continued source-attribution discipline. |
| Teacher behavior or pressure seems suspect | [[Complete Experience Safety Boundary]] | [[Guidance Scope and Accountability Boundary]] | Safety should appear immediately, but pre-edit index visibility was too low. | Teacher depth, liberation signs, or service language could distract from conduct, consent, feedback, and referral criteria. |
| Practice feels profound but behavior is not improving | [[Practice Guidance Toolkit]] | [[Completion Versus Bypass Safety Boundary]] or [[Guidance Scope and Accountability Boundary]] | Adequate after the toolkit; the index needed an explicit behavior-improvement red flag. | State depth could be treated as sufficient evidence without behavior verification or outside feedback. |
| Where did a specific claim come from? | Relevant owner page | Cited source page or raw source if provenance remains unclear | Good for pages with clear body citations; less efficient on frontmatter-heavy owner pages. | Exhaustive source lists in frontmatter obscure principal anchors and should be compressed one page at a time. |
| What raw source should be next? | `wiki/index.md` dashboard | `wiki/_yt_ingestion_implementation_plan.md` | Good; dashboard names the next Gate 7 source. | Backlog confidence remains vulnerable until Phase 8 triage ranks safety/accountability and practice-routing sources. |

### Ranked Routing Changes

1. Add a compact live-guidance and safety override near the top of
   `wiki/index.md`, mirrored in `wiki/_operations.md`. This was applied in the
   same pass.
2. Keep [[Guidance Scope and Accountability Boundary]] visible as the second
   load for teacher pressure, conduct, dependency, feedback, referral, and
   behavior-verification questions.
3. Add a red/yellow/green matrix to [[Complete Experience Safety Boundary]]
   before creating new accountability pages.
4. Add a compact card to [[Current Model]] only if future simulations keep
   loading the full synthesis for routine queries.
5. Compress frontmatter on the six lint-flagged owner pages before broad
   catalog/index surgery.
6. Defer major index surgery until a catalog or lint-registration refactor can
   keep the main index skim-readable without hiding page registration.

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

Status: first safety-matrix pass applied 2026-05-12; new accountability-page
creation remains deferred.

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

Status: completed 2026-05-12 for the six lint-flagged owner pages.

Goal: restore frontmatter as a triage card, not a hidden evidence map.

Order:

1. Pages already flagged by lint: completed with compact body `Source
   Anchors` cards and this frontmatter count map:
   `[[Source And Polarities]]` 37 -> 12, `[[Total Happiness]]` 26 -> 12,
   `[[Sensory Clarity]]` 27 -> 12, `[[Equanimity]]` 25 -> 12, `[[Flow]]`
   25 -> 12, and `[[No-Self And Personality]]` 26 -> 12.
2. Near-threshold routers and high-importance owner pages: `[[Basic
   Mindfulness Practice Architecture]]`, `[[Sensory Grid]]`, `[[Turn Toward
   and Turn Away]]`, `[[Practice Guidance Toolkit]]`, `[[Complete Experience
   Safety Boundary]]`, `[[Mindfulness Skill Triad]]`, `[[Noting]]`, and
   `[[Inner Sensory System]]` have been cleaned to current Phase 7 targets
   where applicable. `[[Gone]]`, `[[Focus on Rest]]`, and `[[Impermanence]]`
   were then cleaned as multi-diagnostic owner follow-ups, reducing all
   active advisory classes on those pages while adding compact `Source
   Anchors` cards. `[[Concentration Power]]` and `[[Expansion And
   Contraction]]` were then cleaned as source-heavy owner follow-ups, reducing
   their non-source frontmatter raw anchors to 8 each with compact source
   cards preserving the broader evidence surface. `[[Insight and
   Purification]]` and `[[See Hear Feel]]` were then cleaned as the next
   source-heavy owner follow-ups, reducing their non-source frontmatter raw
   anchors to 8 each while preserving transformation, safety, and interface
   evidence in compact source cards.

Rules:

- Keep only principal source anchors in non-source frontmatter.
- Move exhaustive evidence maps into body sections or source-anchor lists.
- Keep `load_when` discriminating and short.
- Keep `best_linked_pages` to the strongest next loads.

Validation:

- Lint advisories decrease.
- The opening and key points still carry enough context to route.

## Phase 7 - Lint Safeguards

Status: first advisory-only pass applied 2026-05-12.

Goal: make drift visible before it becomes structural debt.

Small checks to add first:

- warn at `load_when > 320` and strongly warn above the old high threshold;
- warn at `best_linked_pages > 8` and strongly above the old high threshold;
- warn at non-source `sources > 8` and strongly above the old high threshold;
- warn when the index opening through `Open Questions` exceeds the current
  12k-character budget;
- detect stale future-tense `Integration target` phrasing when completed
  `Integration Notes` are present.

Applied notes:

- The first four checks are advisory-only in `tools/wiki_lint.py`.
- The `Integration target` stale-phrasing check is deferred because current
  source-page templates intentionally keep both an `Integration target` line
  and completed `Integration Notes`; a naive detector would flag the normal
  source-page shape rather than genuine stale work.

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

### Backlog Triage - 2026-05-12

Method: title/path-level triage plus current gate context. This is routing
confidence, not source-level evidence; individual source claims still require
normal ingest reading before they can support wiki claims.

| Priority | Bucket | Representative Backlog Sources | Recommendation | Reason |
| --- | --- | --- | --- | --- |
| 1 | Current Gate 7 service/behavior | `The Big Picture as I See It`, `How the Endeavor of Improve Supports Transcend`, `Mindfulness and Behavioural Change`, `The True Beauty of Your Soul`, `Nurturing the Positive...`, `The Focus on Positive Theme`, `Hold Positive Feel` | Continue with `The Big Picture as I See It` unless a safety query forces a detour. | The YouTube plan is already midway through Gate 7; these sources likely clarify behavior, improvement/transcendence, goodness, positive practice, and service accountability. |
| 2 | Safety/clinical/medical | `Mindfulness & Psychotherapy`, `Strengthening a Weak Ego Structure Through Mindfulness`, `Mindfulness, Cancer & Healing` 1-3, `Sleep Interruption & A Good Night's Rest`, `Tea, Coffee and Meditation` | Detour here only for clinical, weak-ego, illness, sleep, substance/caffeine, or therapy-scope questions. | These are high-risk for overclaiming and referral boundaries; they should not be casually absorbed into general practice pages. |
| 3 | Teacher/accountability/transmission | `How do I find a good meditation teacher`, `Which teachers have influenced how you teach`, `Authority, Opinions and the Buddhist Canon`, `A Life of Practice and Service Shinzen Young at 80`, `Lofty, Homey and Quirky Wisdom Voices` | Prioritize if guidance/accountability questions recur after Gate 7. | These sources may sharpen teacher-selection, authority, lineage, voice/style, and service/transmission boundaries. |
| 4 | Practice routing/dosage | `IntroToUltra_ver4.8.pdf`, `A Psycho-Spiritual Workout Routine`, `Vipassana & Mindfulness`, `Jhanas and Focus on Rest`, `Lucid Dreaming and Five Ways`, `Simultaneous Zooming In & Out...` | Use as targeted detours for method-selection, rest/jhana, workout, dream, or zooming questions. | They can improve practice handles, but most are not the main Gate 7 through-line. |
| 5 | Altered phenomena/Source/metaphysics | `Enlightenment; Simultaneous Expansion & Contraction...`, `How Shinzen Uses the Term Spaciousness`, `Reality & Sensory Experience`, `The One True Love of Touch, Sight, & Sound`, `The Reptilian Brain...Experience of God`, `The Secret of Archetypal Deity Yoga`, primal-feel sources | Triage carefully after current Source/safety pages are loaded. | Likely high leverage but high overclaim risk: metaphysics, deity, God-language, primal strata, spaciousness, and altered experience need tight source posture. |
| 6 | Comparative religion/ritual/culture | `Jewish Mysticism & Mindfulness Meditation`, `Is Buddhist meditation compatible with other religions`, `On Rites, Rituals, and Ceremonies`, `Om Mani Padme Hum...`, Native American sweat lodge sources, Leonard Cohen/Sasaki Roshi sources | Deprioritize unless needed for Shinzen's transmission frame. | Useful for translation style and comparative humility, but lower direct practice-routing value than Gate 7, safety, or method sources. |
| 7 | Housekeeping/low routing value | book trailer, audio-series promo, welcome videos, bloopers/out-takes, farewell/welcome retreat fragments, duplicate root/retranscribed-looking viewer welcomes | Defer or ingest only if a specific provenance gap appears. | These are likely low signal for durable practice reasoning relative to the remaining backlog. |

Next-source recommendation: continue Gate 7 with
`raw/Shinzen Sources/yt transcripts/The Big Picture as I See It ~ Shinzen Young_DJkvNfDHbks.md`.
Safety override: if the next user query concerns therapy, weak ego, illness,
teacher choice, or altered/metaphysical phenomena, route to the matching
bucket above before continuing gate order.

## Current Next Step

Phase 0 and the first Phase 2 benchmark are complete. A minimal Phase 1
live-guidance/safety override and the first Phase 5 red/yellow/green safety
matrix have been applied. Phase 6 cleared the original oversized
frontmatter-source advisories while preserving visible source-anchor cards.
Phase 7 now surfaces stricter advisory debt for `load_when`,
`best_linked_pages`, non-source `sources`, and the index opening.
[[Basic Mindfulness Practice Architecture]], [[Sensory Grid]], [[Turn Toward
and Turn Away]], [[Practice Guidance Toolkit]], [[Complete Experience Safety
Boundary]], [[Mindfulness Skill Triad]], [[Noting]], [[Inner Sensory System]],
[[Gone]], [[Focus on Rest]], [[Impermanence]], [[Concentration Power]],
[[Expansion And Contraction]], [[Insight and Purification]], [[See Hear
Feel]], [[Shinzen's Teaching Method]], [[Suffering Distortion Cycle]],
[[Nurture Positive]], [[Total Happiness]], [[Operational Enlightenment]], and
[[Mastery Without Guru Inflation]], [[Recycle The Reaction]], [[Five Ways]],
[[Way of Physical Senses]], [[Way of Thoughts and Emotions]], and [[Sensory
Clarity]], [[Equanimity]], [[Flow]], [[No-Self And Personality]], and
[[Source And Polarities]], [[Complete Experience]], and [[Way of Flow]] have
been cleaned to the current targets where applicable. [[Focus Coverage
Strategies]] and [[Practice Cycles]] have also been cleaned as
practice-implementation follow-ups. [[Guidance Scope and Accountability
Boundary]], [[Altered Phenomena and Dissolution Safety Boundary]],
[[Intensity and Embodiment Safety Boundary]], and [[Practice Method Safety
Boundary]] have been trimmed to eight strongest first-pass safety loads. The
remaining Phase 7 page-level advisories were then cleared by tightening
source-heavy pages, source-page routing strings, and one-link router lists.
As of the latest lint run after index compression, only the expected
raw-source backlog and large-domain advisories remain. Phase 8 now has a
title-level backlog triage: continue Gate 7 with `The Big Picture as I See
It` by default, but detour to safety/clinical, teacher/accountability,
practice-dosage, or altered-phenomena/Source buckets when a query requires
it. The next conservative move is either that Gate 7 ingest or Phase 3
catalog/lint-registration work for the large-domain advisories, not more
owner-page frontmatter cleanup.
