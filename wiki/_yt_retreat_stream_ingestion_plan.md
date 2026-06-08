# YouTube Retreat Stream Ingestion Plan

This plan governs sequential ingestion for the retreat-stream transcripts
acquired from playlist `PLjRQFjS1OrSy3q69a9femKVKH1SiywGwu`.

It depends on:

- `wiki/_yt_lecture_ingest.md` for YouTube lecture/source-page method.
- `wiki/_yt_ingestion_implementation_plan.md` for the one-source-page-per-video
  rule, gate discipline, and per-gate output contract.
- `wiki/_yt_retreat_stream_scrape_plan.md` for acquisition provenance.
- `raw/Shinzen Sources/yt transcripts/retreat streams/_MANIFEST.md` for raw
  transcript paths, quality tiers, and dedupe status.

## Governing Decision

Do not split the six retreat-stream raw transcripts into multiple raw files
or multiple source pages at the outset. Use exactly one `type: source` page
per substantive video, with an internal timestamped teaching arc. The source
page is the compiled interface; the raw transcript remains immutable
evidence.

The long streams should be decomposed operationally, not ontologically:

- Read each 4-6 hour transcript in timestamped blocks.
- Build a compact `Retreat Timeline` or `Teaching Arc` section inside the
  source page.
- Extract only load-bearing teaching moves, practice handles, routing moves,
  safety caveats, transmission notes, and reusable idiolect.
- Exclude or summarize low-signal logistics, refreshments, long silent
  periods, music, chant-only stretches, and Monastic Academy announcements
  unless they clarify practice transition, retreat container, or source frame.

Create derived concept, thesis, synthesis, or question pages only when a
recurring Shinzen-specific handle deserves an independent future route. Do
not create "Part 1/Part 2" source pages merely because a transcript is long.

## Quality Policy

Quality `B` files are YouTube auto captions. They are usable for source-page
ingest and practice-routing triage, but exact wording, Buddhist vocabulary,
names, chants, and specialist terms require spot checks before citation.

Quality `C` files are local STT fallback. They are usable only with stronger
source-page caution. Avoid exact-phrase claims from them unless audio has
been checked or a better transcript is later produced.

For each source page, include the transcript quality in `Source Snapshot`,
`Source Frame`, `Weakest Claims`, and `Important Omissions`.

## Sequence

### R0 - Pilot: Expansion-Contraction Guided Practice

1. `raw/Shinzen Sources/yt transcripts/retreat streams/GUIDED MEDITATION of EXPANSION & CONTRACTION ~ by SHINZEN YOUNG_pg6PTbZ9hDw.md`

Reason: shortest file, quality `B`, and the most concentrated practice handle.
It tests the retreat-stream source-page format without a six-hour load.

Likely owner pages:

- [[Expansion And Contraction]]
- [[Impermanence Flow Gone And Source]]
- [[Flow]]
- [[Source And Polarities]]
- [[Practice Method Safety Boundary]]

Extraction focus:

- Surface expansion-contraction as increase/decrease, pressure, scattering,
  gripping, centering/decentering, and rest.
- The shift from ordinary surface force patterns to possible deep
  Expansion-Contraction.
- How much guessing/groping is accepted in this detection practice.
- Misuse risks around pressure, Source, inscrutable language, and
  overclaiming deep polarity from a guided exercise.

Output decision: after the pilot, decide whether the source-page scaffold
needs a repeatable `Retreat Timeline` subsection for all long streams.

Pilot decision 2026-05-18: R0 created [[Guided Meditation of Expansion and
Contraction]]. For short guided retreat-stream sources, a compact `Teaching
Arc` with timestamps is enough. Keep `Retreat Timeline` for the remaining
4-6 hour streams, where opening/container, practice cycles, Q&A, movement,
and transition blocks need coarse orientation.

### R1 - System Frame: Four Quadrants And Whole-Day Aim

2. Complete 2026-05-18: `raw/Shinzen Sources/yt transcripts/retreat streams/Shinzen April Daylong Retreat Four Quadrant Training_3odXCN29SBc.md`

Reason: quality `B`; title and early scan point to the broad four-quadrant
aim frame, formal/informal retreat instructions, Source/form relation, and
practice-to-life transition. It should orient the remaining daylongs before
their more specialized emphases are read.

Likely owner pages:

- [[Total Happiness Aim Structure]]
- [[Total Happiness]]
- [[Practice Entry and Method Choice]]
- [[Practice Cycles]]
- [[Source And Polarities]]
- [[Shinzen's Teaching Method]]

Extraction focus:

- What "four quadrant" means in this retreat context and whether it confirms,
  revises, or merely repeats the existing Total Happiness quadrant page.
- How Shinzen moves from mindfulness definition to cultivation/application
  without turning the whole day into theory.
- How formal practice, discussion periods, and transition back to driving/life
  are framed.
- Whether the stream adds a durable teaching move for "appreciate /
  transcend / express" or only prepares later streams.

Do not create a new `Four Quadrant Training` concept page unless the source
adds a distinct practice-routing model beyond [[Total Happiness Aim
Structure]].

R1 decision 2026-05-18: created [[Shinzen April Daylong Retreat - Four
Quadrant Training]] as the one source page for the video. The source adds a
daylong body-field scaffold and clarifies that the retreat's
appreciate/transcend/express/nurture quadrants are a practice-organization
variant, not a replacement for the Total Happiness self/other and surface/deep
quadrants. Updated existing owner pages rather than creating a new Four
Quadrant Training concept page. No retreat-stream series synthesis yet; the
gate remains after R2.

### R2 - Threefold Practice Arc: Appreciate, Transcend, Express

3. Complete 2026-05-18: `raw/Shinzen Sources/yt transcripts/retreat streams/Appreciate the Senses, Transcend the Self, Express the Source_hnyl4qYY8V8.md`

Reason: quality `B`; the title names a likely high-value arc linking sensory
appreciation, no-self/transcendence, Source expression, and life practice. It
should be read after the four-quadrant stream so the aim structure is already
calibrated.

Likely owner pages:

- [[Practice Entry and Method Choice]]
- [[See Hear Feel]]
- [[No-Self And Personality]]
- [[Source And Service Boundary]]
- [[Total Happiness]]
- [[Practice Cycles]]

Extraction focus:

- How Shinzen sequences appreciating sensory form, transcending self, and
  expressing Source.
- Note Everything windows/walls, especially the agitation wall around tracking
  everything.
- Micro-hit and life-practice transition material.
- Whether "appreciate / transcend / express" deserves a new concept page as a
  recurring retreat teaching handle. Create it only if this source plus R1 or
  later streams show it routes practice better than existing pages.

R2 decision 2026-05-18: created [[Appreciate the Senses Transcend the Self
Express the Source]] as the one source page for the video. The source mostly
sharpens Note Everything, broad See/Hear/Feel practice, inclusive noting,
re-noting, All/None, practice cycles, complete experience of self, and
pleasure/pain reaction routing. The title's "Source expression" arc is not
developed enough in the available transcript to create a new concept page.
After applying the R0-R2 series synthesis gate, no retreat-stream synthesis
or question was created because R0-R2 currently deepen existing owner pages
more than they establish a stable independent sequence; revisit after R3/R4
if the repeated appreciate/transcend/express/life-practice arc becomes
clearer.

### R3 - Method Menu And Live Routing: Four Ways Forward

4. Complete 2026-05-18: `raw/Shinzen Sources/yt transcripts/retreat streams/Four Ways Forward (June Shinzen Retreat)_DzmdDcvqK0A.md`

Reason: quality `B`; large but scan-rich. It appears to combine method
routing, Note Everything, positive practice, auto-move/speak material, Q&A,
and life-practice discussion. It should follow R1-R2 so its options can be
interpreted against the emerging retreat arc.

Likely owner pages:

- [[Practice Entry and Method Choice]]
- [[Focus Coverage Strategies]]
- [[Nurture Positive]]
- [[Do Nothing]]
- [[Practice Cycles]]
- [[Shinzen's Teaching Method]]

Extraction focus:

- The actual "four ways forward" taxonomy and whether it differs from
  [[Five Ways]], SHF focus ranges, or existing method-choice pages.
- Note Everything walls and how Shinzen routes overwhelm/flooding.
- Positive emotion/body practice and reconstructive moves after
  deconstruction.
- Auto-move, auto-speak, or auto-think references only if they become
  practice handles rather than passing mentions.
- Live Q&A and discussion-routing style.

Create a new question page rather than a concept page if the "four ways"
taxonomy is too transcript-limited or does not resolve cleanly against
existing method menus.

R3 decision 2026-05-18: created [[Four Ways Forward - June Shinzen
Retreat]] as the one source page for the video. The "four ways" taxonomy
resolves as a retreat workout variant of appreciate, transcend/release,
express, and nurture rather than a rival to [[Five Ways]]. Created
[[Auto Move]] because R1 and R3 now make it a recurrent, detailed practice
handle. Updated existing owner pages for method-choice criteria, broad Note
Everything troubleshooting, positive body emotion, Zoom Beyond Space,
Expansion-Contraction, retreat cycles, Source-expression guardrails, and
driving/heavy-machinery safety. No retreat-stream series synthesis or
question was created because the R3 delta is better compressed by [[Auto
Move]] and existing owner pages; revisit after R4 if the Source/chant/life
transition stream creates a sequence-level through-line.

### R4 - Source, Arising-Passing, Chant, And Life Transition

5. `raw/Shinzen Sources/yt transcripts/retreat streams/Shinzen Young Retreat at the Monastic Academy 05.27.2017_kfU_XjT32Yg.md`

Reason: quality `B`; playlist opener but not the best pilot because it is a
long, mixed retreat. Scans show Source, Note Everything, See-Hear-Feel,
arising/passing, auto-chant, and explicit drive/life-practice transition.
Ingest after R1-R3 so repeated retreat moves can be distinguished from new
material.

Likely owner pages:

- [[Source And Polarities]]
- [[Impermanence Flow Gone And Source]]
- [[See Hear Feel]]
- [[Practice Cycles]]
- [[Lineage Translation]]
- [[Om Mani Padme Hum Meaning and Some Mindful Strategies When Chanting]]
- [[Guidance Scope and Accountability Boundary]]

Extraction focus:

- Happiness/self/world/Source framing near the opening.
- Just See / Just Hear / Just Feel / Note Everything sequencing.
- Arising, passing, yes/no/both/rest, and Source-language transitions.
- Auto-speak/auto-chant as motor expression practice; compare with existing
  chant/ritual pages before creating anything new.
- Driving and post-retreat transition safety language.

R4 decision 2026-05-18: created [[Shinzen Young Retreat at the Monastic
Academy 05.27.2017]] as the one source page for the video. The source gives
a Source-facing retreat workout: Just See/Hear/Feel and Note Everything warm
up the field, yes/no/both/rest train arising, passing, simultaneous
arising-passing, and rest across modalities, Auto Chant adds a speech-output
variant of the motor-output family, and the close returns the work to
micro-hits plus sensory driving safety. Updated existing owner pages rather
than creating a retreat-stream synthesis or Auto Chant concept page; R4's
delta is still better compressed by [[Source And Polarities]], [[Expansion
And Contraction]], [[Impermanence Flow Gone And Source]], [[See Hear Feel]],
[[Gone]], [[Lineage Translation]], [[Auto Move]], [[Practice Cycles]], and
[[Practice Method Safety Boundary]]. Revisit a series synthesis only after R5
if the quality-C self/spaciousness stream adds a sequence-level through-line
that existing owners cannot route.

### R5 - Spaciousness, Self, And C-Quality STT Audit

6. `raw/Shinzen Sources/yt transcripts/retreat streams/Shinzen Young Day-Long Retreat at the Monastic Academy - July 22, 2017_TKqJL3AroLc.md`

Reason: longest file and only quality `C` STT transcript. Scans show heavy
self-language, equanimity, sensory clarity, spaciousness, Source, and
life-practice transition. It may be high value, but quality should make it
last unless the user explicitly prioritizes it.

Likely owner pages:

- [[Spaciousness]]
- [[No-Self And Personality]]
- [[Equanimity]]
- [[Mindfulness Skill Triad]]
- [[Source And Polarities]]
- [[Practice Cycles]]
- [[Complete Experience Safety Boundary]]

Extraction focus:

- Definitions or instructions around equanimity as relation to sensory
  experience rather than circumstances.
- The self-understanding ladder from personal/psychological to sensory and
  Source-side parsing.
- Spaciousness and Source claims, with strong transcript-quality caveats.
- Life-practice and driving transition.
- Places where STT has obvious name or vocabulary errors. Do not quote exact
  phrases without audio or better-transcript verification.

If this source becomes load-bearing, consider retranscribing with a stronger
Whisper model before mature integration. Until then, keep claims broad and
quality-limited.

R5 decision 2026-05-18: created [[Shinzen Young Day-Long Retreat at the
Monastic Academy - July 22, 2017]] as the one source page for the video. The
source is usable for broad routing but remains quality `C`: exact wording,
lineage labels, names, Buddhist vocabulary, technical terms, and speaker
attribution require audio or stronger-transcript checks. Updated
[[Spaciousness]], [[No-Self And Personality]], [[Equanimity]],
[[Practice Cycles]], and [[Guidance Scope and Accountability Boundary]] for
the Feel Space procedure, focus range versus representation, fear as
self-rearising after no-self, sensory-equanimity versus objective-action
boundary, micro-hits/background practice/driving transition, and
ethics-feedback-accountability structures. Applied the post-R5 series
synthesis gate and created no retreat-stream synthesis or question because
R0-R5 deepen existing owner pages more than they form a stable independent
sequence. The six retreat-stream source pages are now complete.

## Segmenting Long Streams During Ingest

For each 4-6 hour stream, use a four-pass read:

1. **Map pass**: identify timestamp blocks: opening/container, theory frame,
   instruction cycles, silent practice, Q&A/discussion, movement/life-practice
   transition, closing/logistics.
2. **Claim pass**: extract 8-15 candidate teaching moves with timestamps.
   Keep only those that improve future routing or update an owner page.
3. **Integration pass**: update existing owner pages before creating new
   pages. Prefer narrow owner updates over new pages.
4. **Compression pass**: source page gets a compact teaching arc, key claims,
   practice handles, model/practice delta, audit sections, and Related links.

Suggested source-page additions for these long streams:

```markdown
## Retreat Timeline
- **00:00-00:30**: [container, opening frame, practice setup]
- **00:30-01:30**: [first instruction cycle]
- **01:30-03:00**: [practice/Q&A/movement block]
- **03:00-05:30**: [advanced or integrative block]
- **Closing**: [life-practice transition, safety/logistics]
```

Keep the source page short enough to load: the timeline should orient, not
replace the transcript.

## Series Synthesis Gate

Do not create a retreat-stream synthesis before at least three streams have
source pages. After R0-R2, decide whether a synthesis is warranted. Use this
test:

- If the streams show a stable teaching progression across retreat days,
  create `[[Retreat Stream Practice Arc]]` or a better local title.
- If they mostly deepen existing owner pages, update those owners and skip a
  series synthesis.
- If the main value is unresolved relation among four-quadrant aim,
  appreciate/transcend/express, Source expression, and life-practice
  transition, create a `question` page rather than a synthesis.

Potential synthesis through-line, if earned: Shinzen uses the daylong-retreat
container to move practitioners from sensory appreciation, through
self/world and Source reinterpretation, into expressive life practice, with
method menus and transition safety as the implementation layer.

## Per-Wave Output Contract

For each source or small wave:

- Create exactly one source page per ingested video.
- Update owner pages named by the source page's `Model Delta`.
- Add or update a synthesis/thesis/question only when it compresses durable
  learning.
- Update `wiki/index.md` raw backlog count and routing note.
- Append one `wiki/log.md` entry for the wave.
- Run `tools\wiki_lint.cmd`; raw-backlog warnings should shrink as source
  pages are created, and no structural errors should be added.

## Stop Conditions

Pause and review before continuing if:

- A source page wants to exceed roughly 1,500-2,000 words just to preserve
  all interesting material.
- A transcript-quality issue changes interpretation of a load-bearing claim.
- The same new teaching handle appears in two streams and lacks a good owner
  page.
- Existing owner pages start receiving retreat-stream updates that make their
  frontmatter source-heavy or their first-load surface less clear.
- A long stream appears mostly duplicative after timeline mapping.

The goal is not to ingest all six because they exist. The goal is to improve
future practice reasoning per token loaded.
