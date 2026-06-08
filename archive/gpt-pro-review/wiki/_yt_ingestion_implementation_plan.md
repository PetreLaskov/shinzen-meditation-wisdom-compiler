# YouTube Ingestion Implementation Plan

This is the execution plan for the next Shinzen YouTube lecture phase. It is
ordered from current-model leverage, not scrape order. Use it with
`wiki/_yt_lecture_ingest.md`, `wiki/_templates.md`, `wiki/index.md`, and
`wiki/Current Model.md`.

## Readiness Answer

The previous YouTube plan was not ready for the next phase by itself. It was
a valuable curation handoff, but it did not yet give a current-model-based
sequence with mandatory synthesis gates. This file is the durable
implementation plan.

## Governing Aim

Each gate must improve future ingestion. Do not merely accumulate source
pages. At each meaningful boundary, compress what was learned into owner
pages, a synthesis/thesis/question when warranted, and `[[Current Model]]`
when the whole-system center moves.

The gate question is:

> What did these talks make future agents able to notice, route, explain, or
> protect that they could not handle as well before?

## Current Position

As of 2026-05-12 review, the YouTube plan is midway through Gate 7. Gates 3,
4, 5, 6A, and 6B have completed their source sequences or synthesis
checkpoints; Gate 7 items 1-9 are complete. The next queued source is:

`raw/Shinzen Sources/yt transcripts/The Big Picture as I See It ~ Shinzen Young_DJkvNfDHbks.md`

Current load targets:

- Gate 4 is compressed by [[Impermanence Flow Gone And Source]].
- Gate 5 is compressed by [[Discrimination and Unification]] plus the sensory
  clarity owner pages.
- Gate 6A is compressed by [[Operational Enlightenment]] and the safety
  boundary pages.
- Gate 6B is compressed by [[Ten Ox-Herding Pictures]], [[Self-Inquiry]],
  [[No-Self And Personality]], and [[Source And Polarities]].
- Gate 7 currently routes through [[Total Happiness]], [[Teaching A Path]],
  [[Bodhicitta and the Way of Service]], [[Way of Human Goodness]], and
  [[Deconstruction-Reconstruction Balance]].

Do not expand this section into per-item chronology. Completed item detail
belongs in `wiki/log.md`, source pages, and owner pages. For normal startup,
read this section, `Canonical Path Rule`, `Gate Rules`, the current target
gate, and `Per-Gate Output Contract`; load the full plan only when reviewing
the plan itself.

## Canonical Path Rule

Use the most edited reliable version available:

1. Prefer `raw/Shinzen Sources/yt transcripts/retranscribed/` when the target
   transcript exists there and the manifest marks it usable.
2. Else prefer `raw/Shinzen Sources/yt transcripts/edited/` when available.
3. Else use the root transcript if it is not known tiny.en-degraded,
   header-only, silent, chant-only, or non-Shinzen-primary.
4. If a planned file is quality-gated, do not ingest it until the better
   transcript exists or the user explicitly accepts the lower-quality source.

Create exactly one source page per substantive video. If both root and edited
copies exist, cite only the canonical path chosen by this rule.

## Gate Rules

After each gate:

- Update every affected owner page before moving on.
- Create the named gate synthesis only when the through-line is real; if not,
  create or update the named question instead.
- Update `wiki/index.md` and `wiki/log.md`.
- Run `tools\wiki_lint.cmd`; raw-coverage errors are expected until the
  transcript backlog is ingested, but structural errors must not be added.
- Re-read the gate synthesis before starting the next gate.

## Gate 0 - Calibration: Shinzen As Oral Master-Teacher

Purpose: tune the compiler to Shinzen's oral teaching posture before heavy
content ingestion.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/Shinzen Young ~ My Primary Mission A Deep, Broad, and Subtle Formulation_HcEidBghfOA.md`
2. `raw/Shinzen Sources/yt transcripts/What are your specialties as a teacher ~ Shinzen Young_ilBcFuRNszA.md`
3. `raw/Shinzen Sources/yt transcripts/Three Reasons Why Shinzen Young is a Lousy Teacher_JPkA9oMPKDw.md`
4. `raw/Shinzen Sources/yt transcripts/edited/Towards a Balanced Enlightenment ~ Shinzen Young_wgvr-f0p0Ms.md`
5. `raw/Shinzen Sources/yt transcripts/Do Nothing Meditation ~ Shinzen Young_cZ6cdIaUZCA.md`

Gate synthesis:

- Create or update `[[Shinzen's Teaching Method]]`.
- Create or update `[[Mastery Without Guru Inflation]]` if the balanced
  enlightenment and teacher-accountability material warrants a separate page.
- Update `[[Do Nothing]]`, `[[Practice Guidance Toolkit]]`, `[[Complete
  Experience Safety Boundary]]`, and `[[Current Model]]` only where the
  calibration changes routing.

Proceed only when the wiki can explain why Shinzen's complexity, precision,
interactive coaching, irreverence, anti-guru posture, and Do Nothing method
matter for reading the rest of the corpus.

## Gate 1 - Practice Entry And Method Choice

Purpose: stabilize beginner/intermediate practice routing before advanced
impermanence, no-self, and Source material.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/Why Meditate ~ Shinzen Young_f1TnEQlbPwg.md`
2. `raw/Shinzen Sources/yt transcripts/retranscribed/Beginner FAQs Why Are We Doing This Why Meditate ~ Shinzen Young_MNoDhIKDb0w.md`
3. `raw/Shinzen Sources/yt transcripts/edited/Five Basic Assumptions in Mindfulness Practice ~ Shinzen Young_s1QWEk9c0D4.md`
4. `raw/Shinzen Sources/yt transcripts/The Best Path ~ Shinzen Young_WTUEinAs42I.md`
5. `raw/Shinzen Sources/yt transcripts/Focus Methods in Mindfulness Advantages and Disadvantages ~ Shinzen Young_nHETuhITils.md`
6. `raw/Shinzen Sources/yt transcripts/Three Ways to Set Up Your Basic Mindfulness Session ~ Shinzen Young_2y13blvPkv0.md`
7. `raw/Shinzen Sources/yt transcripts/How to do Labeling and Noting During Meditation, 1 of 2 Parts ~ Shinzen Young_StBTuX0tqU8.md`
8. `raw/Shinzen Sources/yt transcripts/How to do Labeling and Noting During Meditation, Part 2 of 2, Zooming ~ Shinzen Young_KGcpzuHgrQk.md`
9. `raw/Shinzen Sources/yt transcripts/retranscribed/Forcing Spoken Labels ~ Shinzen Young_cRPfi_Bw1pQ.md`
10. `raw/Shinzen Sources/yt transcripts/Bear Down or Ease Up in Meditation ~ Shinzen Young_dfDTAqlZ7dc.md`
11. `raw/Shinzen Sources/yt transcripts/Parts & Wholes, Efforting & Do-Nothing A Certain Momentum ~ Shinzen Young_VFsVc-mMn7s.md`
12. `raw/Shinzen Sources/yt transcripts/A.D.D. & the Do Nothing Technique ~ Shinzen Young_YNV6Y_JlhoA.md`
13. `raw/Shinzen Sources/yt transcripts/Focus on Rest - Standard (Relative Rest) and Advanced (Do Nothing) ~ Shinzen Young_-nco9isReoA.md`

Gate synthesis:

- Create or update `[[Practice Entry and Method Choice]]` if warranted.
- Update `[[Noting]]`, `[[Do Nothing]]`, `[[Focus on Rest]]`, `[[See Hear
  Feel]]`, `[[Practice Cycles]]`, and `[[Practice Guidance Toolkit]]`.
- Add unanswered routing gaps to `[[Complete Experience Safety Boundary]]`.

Proceed only when a future agent can route a practitioner among labeling,
zooming, method choice, effort level, Rest, Do Nothing, and support needs.

## Gate 2 - Guidance, Live Routing, And Walls/Windows

Purpose: compile Shinzen's practical coaching moves before high-intensity
practice and transformation claims.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/Intermediate FAQ Practice In Daily Life Micro-Hits & Challenge Sequences ~ Shinzen Young_wSq9vKkLu4s.md`
2. `raw/Shinzen Sources/yt transcripts/Maximizing Psycho-Spiritual Growth with an Algorithmic Approach (Windows & Walls) ~ Shinzen Young_5t3mHTtKfWk.md`
3. `raw/Shinzen Sources/yt transcripts/Turn Towards Physical Discomfort Sequence & The Taste of Purification ~ Shinzen Young_LZ0L7_lEFqk.md`
4. `raw/Shinzen Sources/yt transcripts/retranscribed/Turn Towards, Turn Away, Focus on Flow w Physical Discomfort ~ Shinzen Young Interactive - 1 of 4_QkI4S9IqrXI.md`
5. `raw/Shinzen Sources/yt transcripts/Turn Towards Flow (Change) Using the Labeling Gears & Options - 2 of 4 ~ Shinzen Young Interactive_8Zz_BfTdp4E.md`
6. `raw/Shinzen Sources/yt transcripts/Turn Towards the Soothing Flow of Poison Ivy, See Flow in Rest ~ Shinzen Young Interactive - 3 of 4_Xb8yiNwFBtA.md`
7. `raw/Shinzen Sources/yt transcripts/Hear-In to Mental Talk Space, Feel Flow in Body Space ~ Shinzen Young Interactive - 4 of 4_WVzuhfc1wF4.md`
8. `raw/Shinzen Sources/yt transcripts/Turn Towards Difficult Emotion and Challenging Feel-Image-Talk Eruptions - 1 of 2 ~ Shinzen Young_F8k4UiDwSJw.md`
9. `raw/Shinzen Sources/yt transcripts/Turn Towards Difficult Emotion and Challenging Feel-Image-Talk Eruptions - 2 of 2 ~ Shinzen Young_TILyiv8UsSU.md`
10. `raw/Shinzen Sources/yt transcripts/Turn Towards, Turn Away Working with the Agitation Flavor in Meditation ~ Shinzen Young_cKfkNWDG170.md`
11. `raw/Shinzen Sources/yt transcripts/Using Turn Away and Background Equanimity w. Sensory Challenges ~ Shinzen Young_R-Zo74I7H9E.md`
12. `raw/Shinzen Sources/yt transcripts/Open Up and Turn Towards Challenging Letting Go States ~ Shinzen Young_oTcGmoaLyv0.md`
13. `raw/Shinzen Sources/yt transcripts/Evoking and Working Through Challenging Material ~ Shinzen Young_dG1_nyUxj2w.md`
14. `raw/Shinzen Sources/yt transcripts/Finding Feel Good in Emotional Body Space - Shinzen Young Guides a Student_WLzTRHay_Tw.md`

Gate synthesis:

- Mature or split `[[Practice Guidance Toolkit]]`.
- Create or update `[[Turn Toward and Turn Away]]` if it becomes too large
  for the guidance page.
- Update `[[Way of Physical Senses]]`, `[[Way of Thoughts and Emotions]]`,
  `[[Flow]]`, `[[Nurture Positive]]`, and `[[Complete Experience Safety
  Boundary]]`.

Proceed only when future agents can distinguish contact, grounding,
background equanimity, Flow routing, positive reconstruction, and support
escalation in live practice.

## Gate 3 - Complete Experience, Purification, And Intensity

Purpose: deepen the central transformation hinge before Source and full
enlightenment-map ingestion.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/edited/Zero and One - Part 1 of 4 Complete Experiences ~ Shinzen Young_IH-BopkX53Q.md`
2. `raw/Shinzen Sources/yt transcripts/edited/Zero and One - Part 2 of 4 Complete Experiences Cont'd, Strong Determination Sits ~ Shinzen Young_MENPoNVg3bA.md`
3. `raw/Shinzen Sources/yt transcripts/edited/Zero and One - Part 3 Strong Determination Challenges, Benefits, and Tasting Purification ~ Shinzen_kO-PvZWM1f0.md`
4. `raw/Shinzen Sources/yt transcripts/edited/Zero and One - Part 4 of 4 Complete Experiences, Unifications & Integrations ~ Shinzen Young_mSEuHTXJ3SA.md`
5. `raw/Shinzen Sources/yt transcripts/edited/Equanimity and the Taste of Purification - Part 1 of 2 ~ Shinzen Young_1HPObyaLB68.md`
6. `raw/Shinzen Sources/yt transcripts/edited/Equanimity and the Taste of Purification - Part 2 of 2 ~ Shinzen Young_OsyekyUsImc.md`
7. `raw/Shinzen Sources/yt transcripts/edited/Purification and Fulfilment Four Formulas ~ Shinzen Young_9u9nuSf9g1g.md`
8. `raw/Shinzen Sources/yt transcripts/edited/The Trickle-Down Paradigm of Transformation ~ Shinzen Young_FdkODyvYxRg.md`
9. `raw/Shinzen Sources/yt transcripts/Strong Determination Meditation Sits ~ Shinzen Young_EHI1aPUxs4s.md`
10. `raw/Shinzen Sources/yt transcripts/What to Expect and Do After a Mindfulness Retreat ~ Shinzen Young_0ifHks5EYZU.md`
11. `raw/Shinzen Sources/yt transcripts/Kriyas & Complete Experiences ~ Shinzen Young_e9AHh9MvgyQ.md`
12. `raw/Shinzen Sources/yt transcripts/Kriyas & the Cloud of Unknowing ~ Shinzen Young_aTaDZqB_RY8.md`
13. `raw/Shinzen Sources/yt transcripts/edited/Dissolution (Bhanga), and T.S. Eliot ~ Shinzen Young_a344llNU15Y.md`
14. `raw/Shinzen Sources/yt transcripts/edited/Experiences of the Dissolution (Bhanga) Process ~ Shinzen Young Interactive - 1 of 3_MUryO_vJT1o.md`
15. `raw/Shinzen Sources/yt transcripts/edited/Experiences of the Dissolution (Bhanga) Process ~ Shinzen Young Interactive - 2 of 3_KEit-DtWQ38.md`
16. `raw/Shinzen Sources/yt transcripts/edited/Experiences of the Dissolution (Bhanga) Process ~ Shinzen Young Interactive - 3 of 3_r78uUarpGsI.md`

Gate synthesis:

- Update `[[Complete Experience]]`, `[[Insight and Purification]]`,
  `[[Equanimity]]`, `[[Dissolution]]`, and `[[Complete Experience Safety
  Boundary]]`.
- Create or update `[[Taste of Purification]]` or `[[Strong Determination]]`
  only if the sources create independent routing value.
- Update `[[Current Model]]` if complete experience shifts from theorem to
  richer practice-diagnostic model.

Proceed only when future agents can distinguish complete experience,
purification taste, intensity, kriyas, retreat aftermath, and bhanga risks.

## Gate 4 - Impermanence, Flow, Gone, And Source

Purpose: compile the high-value impermanence/Source core after safety and
completion are better grounded.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/edited/Born Between Expansion and Contraction Responding to the Needs of Your Larger Identity ~ Shinzen_b2ZTR9mhBWk.md`
2. `raw/Shinzen Sources/yt transcripts/edited/Expansion and Contraction - Part 1 Kenotic Christianity and Shuniya ~ Shinzen Young_M28c-8VfVjQ.md`
3. `raw/Shinzen Sources/yt transcripts/edited/Expansion and Contraction - Part 2 Zen Metaphors and Three Tastes ~ Shinzen Young_DbKlB-0eORs.md`
4. `raw/Shinzen Sources/yt transcripts/edited/Expansion and Contraction - Part 3 Surrendering to Life & Death, Nirvana ~ Shinzen Young_DTPWNtGgp6A.md`
5. `raw/Shinzen Sources/yt transcripts/edited/Expansion and Contraction - Part 4 Heaven, Hell, Integration & 3 Tastes of Freedom ~ Shinzen Young_Hsgj-5yCLGU.md`
6. `raw/Shinzen Sources/yt transcripts/edited/Expansion, Contraction and the Breath Cycle ~ Shinzen Young_z9LgdG3O94Y.md`
7. `raw/Shinzen Sources/yt transcripts/edited/The Theme of Expansive and Contractive Flow ~ Shinzen Young_wWtZMYi0wnM.md`
8. `raw/Shinzen Sources/yt transcripts/Paradigms of Change Impermanence, Flow, Expansion & Contraction, Arising & Passing ~ Shinzen Young_uco6mSHmwJA.md`
9. `raw/Shinzen Sources/yt transcripts/Mindfulness Momentum, Arising and Passing to Simultaneous Expansion and Contraction ~ Shinzen Young_LlglNS_rg5g.md`
10. `raw/Shinzen Sources/yt transcripts/The Three-Dimensional Shape of Simultaneous Expansion and Contraction ~ Shinzen Young_rzwkB4QWU_s.md`
11. `raw/Shinzen Sources/yt transcripts/Abrupt Flow Diminishings, Vanishings and Noting Gone ~ Shinzen Young_L-7LXHjGHfM.md`
12. `raw/Shinzen Sources/yt transcripts/Flow, Gone & a Figure-Ground Reversal ~ Shinzen Young_rKm-WXRH2IQ.md`
13. `raw/Shinzen Sources/yt transcripts/Tri-Modal Rest & Flow Thinning Out into Nirvana ~ Shinzen Young_BOLuaPltorA.md`
14. `raw/Shinzen Sources/yt transcripts/The 'Focus on Flow' Theme ~ Shinzen Young_xtZTL5mV478.md`
15. `raw/Shinzen Sources/yt transcripts/Untangling Sensory Experience Leads to Flow, Unifications, and Dynamic Doing ~ Shinzen Young_g0v70wPcs0c.md`
16. `raw/Shinzen Sources/yt transcripts/Zen, Vipassana, & Becoming Impermanence ~ Shinzen Young_eJ15Y6WrDTE.md`
17. `raw/Shinzen Sources/yt transcripts/From Surface to Source & the Gold Standard for Spiritual Maturity ~ Shinzen Young_ncQGlYfvO0Q.md`
18. `raw/Shinzen Sources/yt transcripts/Fulfilling the Pythagorean Agenda ~ Shinzen Young_8TdC2vT0r48.md`

Gate synthesis:

- Mature or split `[[Expansion And Contraction]]`.
- Update `[[Impermanence]]`, `[[Flow]]`, `[[Gone]]`, `[[Source And
  Polarities]]`, `[[Dissolution]]`, `[[Total Happiness]]`, and `[[Complete
  Experience Safety Boundary]]`.
- Create or update `[[Surface To Source]]` if the sources make it the better
  route than keeping everything under Source/polarities.

Proceed only when future agents can route ordinary change, Flow, Gone,
simultaneous Expansion-Contraction, Source afterglow, and service without
collapsing practice into metaphysics.

## Gate 5 - Sensory Clarity, Discrimination, And Unification

Purpose: deepen the sensory grammar and discrimination/unification dialectic
that makes advanced material precise rather than vague.

Sequence:

1. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/6 Buddhist Consciousnesses & the 12 Sensory States ~ Shinzen Young_PDUvTid4hxk.md`
2. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/Mindfulness & the Categories of Sensory Experience ~ Shinzen Young_Skl5LE7Uucg.md`
3. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/Dynamic Aspects of the Sensory System ~ Shinzen Young_8rSXFUWMoak.md`
4. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Discrimination and Unification - Part 1 of 4 ~ Shinzen Young_yX6WZwdBWTY.md`
5. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Discrimination and Unification - Part 2 of 4 ~ Shinzen Young_BuMSvui-6Kc.md`
6. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Discrimination and Unification - Part 3 of 4 ~ Shinzen Young_g34a09qDbfU.md`
7. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Discrimination and Unification - Part 4 of 4 ~ Shinzen Young_IAudwp77vf8.md`
8. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Depth & Breadth of Concentration - Part 1 of 3 ~ Shinzen Young_lq1IL_DnC98.md`
9. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Depth & Breadth of Concentration - Part 2 of 3 ~ Shinzen Young_E-jZE9jDfKQ.md`
10. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/edited/Depth & Breadth of Concentration - Part 3 of 3 ~ Shinzen Young_-AoNrGM0MBY.md`
11. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/Growth and Tastes of Concentration, Sensory Clarity and Equanimity ~ Shinzen Young_ED0pXThS_nc.md`
12. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/Sensory Clarity - 1 of 2 - No Self As Thing ~ Shinzen Young_1ZKgyqdiAKI.md`
13. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/Sensory Clarity - 2 of 2 - No Self As Thing ~ Shinzen Young_MB96tQi_08s.md`
14. Complete 2026-05-08: `raw/Shinzen Sources/yt transcripts/Sensory Clarity Insight Through Monitoring Ordinary and Restful States ~ Shinzen Young_PNetIhxFinw.md`
15. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Sensory Clarity Untangle and Be Free ~ Shinzen Young_1gXoGMrGH34.md`
16. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Natural Sensory Space Combinations ~ Shinzen Young_ON9nSWAaiWM.md`
17. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Sight Space How Detecting Shifts Can Lead to Flow ~ Shinzen Young_KJu-dgfAwE0.md`
18. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/retranscribed/Working with Images and Image Space ~ Shinzen Young_g7BXI0odxP4.md`

Gate synthesis:

- Create or update `[[Discrimination and Unification]]`.
- Update `[[Sensory Grid]]`, `[[Sensory Clarity]]`, `[[Mindfulness Skill
  Triad]]`, `[[Inner Sensory System]]`, `[[No-Self And Personality]]`, and
  `[[See Hear Feel]]`.

Proceed only when future agents can explain how discrimination and
unification cooperate instead of treating them as rival path styles.

## Gate 6A - Operational Enlightenment, Ethics, And Safety

Purpose: compile the enlightenment definition, anti-perfection boundary,
teacher accountability, and clinical/dark-night differentials before path-map
romance takes over.

Sequence:

1. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/What is Enlightenment ~ Shinzen Young_Qu_GvP2pfGc.md`
2. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Enlightenment Maps and Models ~ Shinzen Young_whnGgq4O3jM.md`
3. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/After enlightenment, what's left, what's the point ~ Shinzen Young_ptkH0uK1uXM.md`
4. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Enlightenment Downsides ~ Shinzen Young_qoAbCgmhqdM.md`
5. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Six Common Traps on the Path to Enlightenment ~ Shinzen Young_i288Lnb7NOk.md`
6. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Classical Enlightenment Healing the World and Screw-ups ~ Shinzen Young_hBDqTY1W8Dk.md`
7. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Enlightenment, DPDR & Falling Into the Pit of the Void ~ Shinzen Young_9zIKQCwDXsA.md`
8. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Classic Dark Night or Clinical Issues ~ Shinzen Young_BQ5B70ac_9M.md`
9. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Advanced FAQs Regarding Emptiness ~ Shinzen Young_812I4KYLMF8.md`
10. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Meditation Teacher's Qualifications and Liberation Experiences ~ Shinzen Young_tF96pTDYEAU.md`
11. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Spiritual Teachers' Behaviour Feedback & Ethics ~ Shinzen Young_-_mppU0j58c.md`
12. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Teacher's or Student's Issues Impeding Spiritual Progress ~ Shinzen Young_XBItqGFYVSI.md`

Gate synthesis:

- Create or update `[[Operational Enlightenment]]`.
- Create or update `[[Classical Enlightenment]]` only if it does different
  work than operational enlightenment.
- Create or update `[[DPDR and the Pit of the Void]]` if the clinical
  differential becomes independently reusable.
- Update `[[Mastery Without Guru Inflation]]`, `[[Complete Experience Safety
  Boundary]]`, `[[No-Self And Personality]]`, and `[[Total Happiness]]`.

Proceed only when future agents can discuss enlightenment without implying
perfection, clinical certainty, or automatic ethical maturity.

## Gate 6B - No-Self, Witness, And Path Maps

Purpose: compile selflessness, witness, ox-herding, and return-to-life maps
after the operational/safety frame is in place.

Sequence:

1. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Non-Dual Awareness ~ Shinzen Young_mwOccTTAcVw.md`
2. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Self-Enquiry & Mindfulness Meditation ~ Shinzen Young_pHUajtPXPDw.md`
3. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/The Absolute Witness ~ Shinzen Young_drLxJSpeb8c.md`
4. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/A Deeper Freedom Experiences of Selflessness ~ Shinzen Young_Hfw_tHC0A9w.md`
5. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Humility to the Vanishing Point No Self Around the World ~ Shinzen Young_Nwmj37W-NR8.md`
6. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/No Place to Stand ~ Shinzen Young_EyZPoIVOBS4.md`
7. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Enlightenment and the Ten Zen Ox Herding Pictures ~ Shinzen Young_Vt68YJCe_YA.md`
8. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Zen Ox-Herding Pics - Part 1 of 3 ~ Shinzen Young_x8aN9O73lgg.md`
9. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Zen Ox-Herding Pics - Part 2 of 3 ~ Shinzen Young_0PQonSiGkVE.md`
10. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Zen Ox-Herding Pics - Part 3 of 3 ~ Shinzen Young_Ozca_5ifwQ0.md`

Gate synthesis:

- Complete 2026-05-09: create or update `[[Ten Ox-Herding Pictures]]`.
- Create or update `[[Self-Inquiry]]` if it becomes a useful Shinzen-specific
  practice bridge.
- Update `[[No-Self And Personality]]`, `[[Source And Polarities]]`,
  `[[Total Happiness]]`, and `[[Complete Experience Safety Boundary]]`.

Note: prefer a future `retranscribed/` version of Humility if one appears;
otherwise use the edited path above and do not double-ingest the root copy.

## Gate 7 - Total Happiness, Service, And Human Goodness

Purpose: compile the life/service aim so advanced realization remains
accountable to behavior, care, and teaching a path.

Sequence:

1. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Total Happiness - 1 of 5 - May Happiness Be ~ Shinzen Young_A0A6Rw7KnvA.md`
2. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Total Happiness - 2 of 5 - Ordinary & Extraordinary ~ Shinzen Young_uEW2WnAeKdc.md`
3. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Total Happiness - 3 of 5 - Don't Know Mind ~ Shinzen Young_BcTqXAD7pvM.md`
4. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Total Happiness - 4 of 5 - Self and Others ~ Shinzen Young_YAoDyijHDtg.md`
5. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Total Happiness - 5 of 5 - The Activity of Teaching ~ Shinzen Young_L_24Qy77Rko.md`
6. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/edited/Bodhicitta, and the Bodhisattva Ideal, with a Short, Guided Meditation ~ Shinzen Young_5kBiqluARdU.md`
7. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/The Final Stage and Service ~ Shinzen Young_b2anxOUgl1A.md`
8. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/Becoming a High-Wattage Broadcaster of Human Positivity ~ Shinzen Young_-KFJYzPYDfA.md`
9. Complete 2026-05-09: `raw/Shinzen Sources/yt transcripts/A Mindfulness Path Arising Between Empowering Contrasts ~ Shinzen Young_ncGiwqCZ7rg.md`
10. `raw/Shinzen Sources/yt transcripts/The Big Picture as I See It ~ Shinzen Young_DJkvNfDHbks.md`
11. `raw/Shinzen Sources/yt transcripts/How the Endeavor of Improve Supports Transcend ~ Shinzen Young_G9f9BjcE3lo.md`
12. `raw/Shinzen Sources/yt transcripts/Mindfulness and Behavioural Change ~ Shinzen Young_bGy2PdVzNMU.md`
13. `raw/Shinzen Sources/yt transcripts/The True Beauty of Your Soul ~ Shinzen Young_K50i1AYPl7w.md`
14. `raw/Shinzen Sources/yt transcripts/Nurturing the Positive Creating, Holding and Radiating Positive Subjective States ~ Shinzen Young_IzRq0iRibv0.md`
15. `raw/Shinzen Sources/yt transcripts/The Focus on Positive Theme ~ Shinzen Young_88au4ZberSI.md`
16. `raw/Shinzen Sources/yt transcripts/retranscribed/Hold Positive Feel_JNZRKbFlsaY.md`
17. `raw/Shinzen Sources/yt transcripts/Creating Feel Good in Emotional Body Space - 1 of 2 - Introduction ~ Shinzen Young_abRaPYjb6mA.md`
18. `raw/Shinzen Sources/yt transcripts/Creating Feel Good in Emotional Body Space - 2 of 2 - A Guided Meditation ~ Shinzen Young_u41_dSjKGtA.md`

Gate synthesis:

- Create or update `[[Bodhicitta and the Way of Service]]` if warranted.
- Create or update `[[Teaching A Path]]` and `[[Practice Description as
  Service]]` if the Total Happiness series supports them.
- Update `[[Total Happiness]]`, `[[Way of Human Goodness]]`,
  `[[Nurture Positive]]`, `[[Deconstruction-Reconstruction Balance]]`,
  `[[Suffering Distortion Cycle]]`, and `[[Complete Experience Safety
  Boundary]]`.

Proceed only when future agents can explain how fulfillment, behavior,
positive reconstruction, teaching, and service test realization.

## Gate 8 - Lineage Translation And Cross-Traditional Bridges

Purpose: compile Shinzen's way of translating traditions without letting
comparative material become the wiki's center.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/Which teachers have influenced how you teach ~ Shinzen Young_WoUJPcWBgXk.md`
2. `raw/Shinzen Sources/yt transcripts/Authority, Opinions and the Buddhist Canon ~ Shinzen Young_CfEFSRNHL5s.md`
3. `raw/Shinzen Sources/yt transcripts/edited/Sasaki Roshi & Burmo-Japanese Mindfulness Fusion ~ Shinzen Young_-pMyY6Abi4g.md`
4. `raw/Shinzen Sources/yt transcripts/edited/Leonard Cohen, Sasaki Roshi, & Love Itself - Part 1 of 2 ~ Shinzen Young_eSv5ELuujjs.md`
5. `raw/Shinzen Sources/yt transcripts/edited/Leonard Cohen's Love Itself - Part 2 of 2 ~ Shinzen Young_p3MgjpMbADA.md`
6. `raw/Shinzen Sources/yt transcripts/edited/Sasaki Roshi, the Complex Number System & the Source of Love ~ Shinzen Young_hvFOe_JmSCw.md`
7. `raw/Shinzen Sources/yt transcripts/The Dharma Name Shinzen ~ Shinzen Young_ri2daqYL7mU.md`
8. `raw/Shinzen Sources/yt transcripts/Jewish Mysticism & Mindfulness Meditation ~ Shinzen Young_ZfNdNA580yk.md`
9. `raw/Shinzen Sources/yt transcripts/Jhanas and Focus on Rest ~ Shinzen Young_A-72haqjl4o.md`
10. `raw/Shinzen Sources/yt transcripts/The Secret of Archetypal Deity Yoga ~ Shinzen Young_6WtPrOE1JSk.md`
11. `raw/Shinzen Sources/yt transcripts/The Native American Sweat Lodge Ceremony - Part 1 of 2 ~ Shinzen Young_n4u-5BSZH64.md`
12. `raw/Shinzen Sources/yt transcripts/The Native American Sweat Lodge - Part 2 of 2 ~ Shinzen Young_by7veja2WHc.md`
13. `raw/Shinzen Sources/yt transcripts/On Rites, Rituals, and Ceremonies ~ Shinzen Young_u9pgbO-N5QQ.md`
14. `raw/Shinzen Sources/yt transcripts/Is Buddhist meditation compatible with other religions ~ Shinzen Young_5lbFes1HMz8.md`
15. `raw/Shinzen Sources/yt transcripts/Om Mani Padme Hum Meaning and Some Mindful Strategies When Chanting ~ Shinzen Young_VpG3HaCFPbo.md`
16. `raw/Shinzen Sources/yt transcripts/The Dark Night by St. John of the Cross (recited in Spanish & English) ~ Shinzen Young_PcRDzOBWkPc.md`

Gate synthesis:

- Update `[[Mysticism As Concentration]]`, `[[Source And Polarities]]`,
  `[[Expansion And Contraction]]`, `[[Nurture Positive]]`, and `[[Complete
  Experience Safety Boundary]]`.
- Create an entity page such as `[[Sasaki Roshi]]` only if it materially
  changes interpretation of Shinzen's teaching system.
- Create or update `[[Lineage Translation]]` only if it improves routing
  more than the existing comparative frame.

Proceed only when future agents can preserve Shinzen's translation genius
without treating cross-tradition parallels as proof of sameness.

## Gate 9 - Applied Domains And Special Cases

Purpose: ingest applied talks after the core model can distinguish practice
guidance from clinical, relational, medical, and life-domain advice.

Sequence:

1. `raw/Shinzen Sources/yt transcripts/Mindfulness & Psychotherapy ~ Shinzen Young_ghBxjliqIPY.md`
2. `raw/Shinzen Sources/yt transcripts/retranscribed/Mindfulness, Cancer & Healing - 1 of 3 ~ Sat Dharam Kaur, N.D. Interviews Shinzen Young_bYwSAR8BF9Y.md`
3. `raw/Shinzen Sources/yt transcripts/retranscribed/Mindfulness, Cancer & Healing - 2 of 3 ~ Sat Dharam Kaur, N.D. Interviews Shinzen Young_jxFyyTOIyTA.md`
4. `raw/Shinzen Sources/yt transcripts/Mindfulness, Cancer & Healing - 3 of 3 ~ Sat Dharam Kaur, N.D. Interviews Shinzen Young_5MRz7VapI5w.md`
5. `raw/Shinzen Sources/yt transcripts/A Mindful Birth and Zen Parenting, Part 1 of 2 ~ Shinzen Young_2gpdWdoCqVo.md`
6. `raw/Shinzen Sources/yt transcripts/A Mindful Birth and Zen Parenting, Part 2 of 2 ~ Shinzen Young_mUGigTkD20g.md`
7. `raw/Shinzen Sources/yt transcripts/Sleep Interruption & A Good Night's Rest ~ Shinzen Young_DUQFw2jNf7s.md`
8. `raw/Shinzen Sources/yt transcripts/Do You Think Sex is Dirty ~ Shinzen Young_drzPr3PsVJ4.md`
9. `raw/Shinzen Sources/yt transcripts/Lucid Dreaming and Five Ways Mindfulness Meditation ~ Shinzen Young_GwctdxAn9v4.md`
10. `raw/Shinzen Sources/yt transcripts/Tea, Coffee and Meditation ~ Shinzen Young__ZudmkA4iEM.md`
11. `raw/Shinzen Sources/yt transcripts/retranscribed/Shinzen Young's Welcome to New Viewers_100q5smtZIw.md`
12. `raw/Shinzen Sources/yt transcripts/Shinzen Young's Welcome to New Viewers_Pvk99BRxlPw.md`
13. `raw/Shinzen Sources/yt transcripts/The Science of Enlightenment Audio Series ~ Shinzen Young_Nk1VPN5lugw.md`
14. `raw/Shinzen Sources/yt transcripts/Shinzen Young - The Science of Enlightenment (Book Trailer)_iEjUb2b4RMM.md`
15. `raw/Shinzen Sources/yt transcripts/Reality & Sensory Experience ~ Shinzen Young_qbNHTDE1iYg.md`
16. `raw/Shinzen Sources/yt transcripts/Consciously Decoupling, Dropping Out & Eadem Mutata Resurgo ~ Shinzen Young_Wr7ghLGmm3U.md`
17. `raw/Shinzen Sources/yt transcripts/The Reptilian Brain, Skinnerian Training & the Experience of God ~ Shinzen Young_KlpXGXZ_dT0.md`

Gate synthesis:

- Update `[[Complete Experience Safety Boundary]]`, `[[Practice Guidance
  Toolkit]]`, `[[Total Happiness]]`, and any applied pages that already
  exist.
- Create applied-domain pages only when the source gives reusable Shinzen
  practice routing, not merely a topic appearance.

Proceed only when future agents can say what Shinzen's system can and cannot
responsibly claim in therapy, illness, parenting, sleep, sexuality, and
ordinary life.

## Gate 10 - Quality-Gated Long Retrospectives And Dialogues

Purpose: ingest very high-value long or multi-speaker material only when the
transcript quality and attribution are sufficient.

Sequence after quality gate passes:

1. `raw/Shinzen Sources/yt transcripts/A Life of Practice and Service Shinzen Young at 80_YghW4NNTxAo.md`
2. `raw/Shinzen Sources/yt transcripts/Advanced Meditators Experience of Time ~ Shinzen Young, Har-Prakash Khalsa, Todd Mertz_ouKeo7_TEAE.md`
3. `raw/Shinzen Sources/yt transcripts/retranscribed/The Hockey Stick Metaphor and Exponential Growth on the Spiritual Path ~ Shinzen Young_-pRA9QHVzVg.md`
4. `raw/Shinzen Sources/yt transcripts/Shinzen Young ~ Primal Feel and the Zen Keisaku - 1 of 2_LjzEeSSL4o0.md`
5. `raw/Shinzen Sources/yt transcripts/Shinzen Young and Soryu ~ Primal Feel and the Zen Keisaku - 2 of 2_99h8CpIK8pQ.md`
6. `raw/Shinzen Sources/yt transcripts/Working Through the Primal Feel Strata ~ Shinzen Young_zvcGvR_gnBE.md`
7. `raw/Shinzen Sources/yt transcripts/Reparenting Our Freaked Out Infant - Noting All Vanishings & Gone in Pure Feeling ~ Shinzen Young_Cg-h_MSijDo.md`

Gate synthesis:

- Update `[[Current Model]]` if the retrospective changes the whole-system
  reading.
- Update or split `[[Primordial Feel]]`, `[[Dissolution]]`, `[[No-Self And
  Personality]]`, `[[Total Happiness]]`, and `[[Complete Experience Safety
  Boundary]]`.
- Create an entity page for Shinzen only if the retrospective changes
  teaching-system interpretation rather than supplying biography.

Quality notes:

- For item 1, prefer a future `retranscribed/` version if it appears. The
  current retranscription manifest previously marked it as running, so verify
  before ingest.
- For item 2, extract Shinzen claims carefully because it is a dialogue with
  other speakers.
- For item 3, the retranscribed path is canonical because it exists.

## Defer Or Skip Unless User Redirects

Do not ingest these during the core sequence unless a later review changes
their value:

- `raw/Shinzen Sources/yt transcripts/10 Minute Sit w. Shinzen Just Sitting ~ Shinzen Young_G6npSvMb5XQ.md`
- `raw/Shinzen Sources/yt transcripts/10 Minute Community (Sangha) Sit Chanting Om Mani Padme Hum ~ Shinzen Young_tOYiHaXtwzY.md`
- `raw/Shinzen Sources/yt transcripts/Five Fold Sila in Pali ~ Shinzen Young_Sb7O7LbcYn4.md`
- `raw/Shinzen Sources/yt transcripts/Guided Compassion and Healing the World Meditation ~ Shinzen Young_9LNRpkKzQh8.md`
- `raw/Shinzen Sources/yt transcripts/Noche Oscura - (The Dark Night) by St. John of the Cross (Spanish Only) ~ Shinzen Young_zA1APGkoupM.md`
- `raw/Shinzen Sources/yt transcripts/Welcome to Cultivating the Jewel of Mindfulness Practitioner Training Program ~ Har-Prakash Khalsa_NS7_uN8F6P8.md`
- `raw/Shinzen Sources/yt transcripts/Module One Cultivating the Jewel of Mindfulness Practitioner Training ~ Har-Prakash Khalsa_jex0giLXNAs.md`
- `raw/Shinzen Sources/yt transcripts/Guided See, Hear, Feel Sensory Spaces from Cultivating the Jewel of Mindfulness ~ Har-Prakash Khalsa_6XJN3TjhSZ8.md`
- `raw/Shinzen Sources/yt transcripts/Guided Self-Nurturing Meditation from Cultivating the Jewel of Mindfulness ~ Har-Prakash Khalsa_Meqvr2zGn2U.md`

## Per-Gate Output Contract

Each gate should leave:

- Source pages for every ingested video.
- Owner-page updates for all durable claims.
- One synthesis/thesis/question update that compresses the gate.
- A short `wiki/log.md` entry naming pages touched, assumptions, open issues,
  and validation.
- A decision about whether `[[Current Model]]` changed.

If a gate does not improve future reasoning quality, stop and review before
continuing.
