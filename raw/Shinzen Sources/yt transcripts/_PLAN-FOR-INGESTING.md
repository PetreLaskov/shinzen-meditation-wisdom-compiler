# PLAN FOR INGESTING — YT Transcript Corpus

Written 2026-04-30. Companion to `_EDITING_PROGRESS.md` (the editorial-cleanup audit) and the wiki's [2026-04-29] log entry that named the eight initial deliverables. This plan curates a highest→lowest priority ingestion sequence for the ~205 YouTube transcripts at this folder.

---

## State of the wiki at plan time

**4 sources ingested (39 mature pages):**

- *What Is Mindfulness?* (Young, ver1.5) — full
- *Five Ways to Know Yourself* (Young, ver1.6) — full
- *The Science of Enlightenment* (Young, Sounds True 2016) — chs. 2-5 + 8-9 done; chs. 1, 6-7, 10-11 queued
- **YT pilot:** *"Do Nothing" Meditation* (cZ6cdIaUZCA) → `source-yt-do-nothing-meditation-young.md`

**The pilot validated the lean YT-source-page format:** frontmatter (type=source, transcript tag, videoID alias) + opening + "Where it sits in the arc" + numbered load-bearing claims + register/stance + lineage + related. Use it for every transcript.

**Audit-named deliverables (target wiki pages):**

- New: [[Expansion and Contraction]], [[Discrimination and Unification]], [[Enlightenment (Operational Definition)]], [[DPDR and the Pit of the Void]], [[Ten Ox-Herding Pictures]], [[Bodhicitta and the Way of Service]]
- Stub promotion: [[Self-Inquiry]] 🌱→🌿
- Existing-page expansion: [[Sensory Grid]]

---

## Disambiguation — which version of each transcript to read

| Status | Count | Canonical location | Rule |
|---|---|---|---|
| **edited/** (manually cleaned) | 56 | `raw/yt transcripts/edited/` | Use this version |
| **retranscribed/** (whisper redo of tiny.en) | 10 done + 1 running + 5 pending | `raw/yt transcripts/retranscribed/` | Use once `_run.log` confirms |
| **raw-fine** (originals were good as-is) | ~134 | `raw/yt transcripts/` (root) | Use directly |
| **Skip** | 7 header-only stubs (<800B) + 4 Khalsa standalones | — | Do not ingest |

Both `edited/` and `retranscribed/` contain **copies**; originals remain at root. Only file double-covered: `Humility to the Vanishing Point` (Nwmj37W-NR8) — once retranscription completes, `retranscribed/` supersedes `edited/`.

**Operational gate:** retranscription is in flight. Critically, `A Life of Practice and Service Shinzen at 80` (53KB, the corpus's single largest and highest-value transcript) is currently re-running on large-v3. **Do not ingest it from edited/ until the retranscribed/ version lands.** Five other tiny.en pendings need identification before Wave 3 — run `grep -l "faster-whisper (tiny.en" *.md` (or scan the Source frontmatter of root files) to enumerate them.

---

## Wave 1 — The five new pages (25 transcripts, the load-bearing wave)

Sequenced for compounding: each new page is anchored by its densest single transcript, then deepened by series/secondaries. The third source on a given page reorganizes the first two. **E-C opens** because it is already a phantom term across many existing pages — establishing the dedicated page first means subsequent ingestion compounds into existing cross-references rather than backfilling them.

### 1.1 [[Expansion and Contraction]] (10 transcripts)

| # | Transcript | Size | Role |
|---|---|---|---|
| 1 | Born Between Expansion and Contraction (b2ZTR9mhBWk) | 16.2KB | **Anchor** — establishes page |
| 2 | E-C Part 1: Kenotic Christianity and Shuniya (M28c-8VfVjQ) | 5.4KB | Series — cross-traditional framing |
| 3 | E-C Part 2: Zen Metaphors and Three Tastes (DbKlB-0eORs) | 5.9KB | Series — Zen mapping |
| 4 | E-C Part 3: Surrendering, Nirvana (DTPWNtGgp6A) | 4.8KB | Series — soteriology |
| 5 | E-C Part 4: Heaven, Hell, Three Tastes of Freedom (Hsgj-5yCLGU) | 4.6KB | Series — integration close |
| 6 | The Theme of Expansive and Contractive Flow (wWtZMYi0wnM) | 8.8KB | Sasaki spatial-Flow bridge |
| 7 | Paradigms of Change: Impermanence, Flow, E-C, Arising-Passing (uco6mSHmwJA) | 7.0KB | Bridges to anicca |
| 8 | Mindfulness Momentum, Arising→Simultaneous E-C (LlglNS_rg5g) | 6.3KB | The "becoming subtle Flow" reversal |
| 9 | E-C and the Breath Cycle (z9LgdG3O94Y) | 3.0KB | Body-anchored E-C |
| 10 | Three-Dimensional Shape of Simultaneous E-C (rzwkB4QWU_s) | 2.1KB | Geometric register |

**Cross-page extensions to expect:** [[Way of Flow]] (Sasaki spatial vs. temporal), [[The Power of Gone]] (the *smooth E-C creates time and space; abrupt contractive Gone destroys them* claim), [[Return to the Source]] (E-C cosmology as practice-form of stages 8-10), [[The Real No Self]] (self-as-particle vs. self-as-wave), [[Big Picture]] (the polar forces of practice).

### 1.2 [[Discrimination and Unification]] (4 transcripts — ingest as a unit in one session)

| # | Transcript | Size | Role |
|---|---|---|---|
| 11 | D&U Part 1 (yX6WZwdBWTY) | 5.5KB | Anchor |
| 12 | D&U Part 2 (BuMSvui-6Kc) | 5.2KB | Series |
| 13 | D&U Part 3 (g34a09qDbfU) | 6.7KB | Series — densest |
| 14 | D&U Part 4 (IAudwp77vf8) | 3.5KB | Series close |

**Cross-page extensions:** [[Sensory Clarity]] (discrimination as sub-skill), [[Way of Physical Senses]] (merge-with-sound limit phenomenology), [[Four-Component Sensory Parsing]] (the parsing/unifying dialectic).

### 1.3 [[Ten Ox-Herding Pictures]] (4 transcripts — standalone first, series deepens)

| # | Transcript | Size | Role |
|---|---|---|---|
| 15 | Enlightenment and the Ten Zen Ox Herding Pictures (Vt68YJCe_YA) | 12.9KB | **Anchor** — full standalone |
| 16 | Zen Ox-Herding Pics Part 1 (x8aN9O73lgg) | 3.9KB | Series |
| 17 | Zen Ox-Herding Pics Part 2 (0PQonSiGkVE) | 3.8KB | Series |
| 18 | Zen Ox-Herding Pics Part 3 (Ozca_5ifwQ0) | 5.0KB | Series — return-to-marketplace |

**Cross-page extensions:** Cross-traditional path-map artifact; bridges [[The Real No Self]] (stage 8 — empty circle) ↔ [[Way of Human Goodness]] (stage 10 — return). Strong candidate to also seed [[Bodhicitta and the Way of Service]] before that page is anchored in Wave 2.

### 1.4 [[Enlightenment (Operational Definition)]] (7 transcripts)

This page is unusual — no single transcript is fully sufficient; the operational definition is built across ~10 short-to-medium talks. The wiki already has [[Happiness Independent of Conditions]] as Young's soteriological-claim page; the new page complements it (HIC = the felt aim; Enlightenment = the structural claim).

| # | Transcript | Size | Role |
|---|---|---|---|
| 19 | Towards a Balanced Enlightenment (wgvr-f0p0Ms) | 13.9KB | **Anchor** — densest single articulation |
| 20 | After Enlightenment, What's Left (ptkH0uK1uXM) | 5.8KB | Post-realization phenomenology |
| 21 | Six Common Traps on the Path to Enlightenment (i288Lnb7NOk) | 7.1KB | Bridges to [[Dark Night]] |
| 22 | Enlightenment Maps and Models (whnGgq4O3jM) | 4.6KB | Cross-traditional landmarks |
| 23 | Classical Enlightenment Healing the World (hBDqTY1W8Dk) | 2.9KB | Bodhicitta bridge |
| 24 | Enlightenment Downsides (qoAbCgmhqdM) | 3.4KB | Calibration |
| 25 | What is Enlightenment (Qu_GvP2pfGc) | 1.5KB | Compressed restatement |

### 1.5 [[DPDR and the Pit of the Void]] (2 transcripts — small but high-impact)

| # | Transcript | Size | Role |
|---|---|---|---|
| 26 | Enlightenment, DPDR & Falling Into the Pit of the Void (9zIKQCwDXsA) | 6.8KB | Anchor |
| 27 | Classic Dark Night or Clinical Issues (BQ5B70ac_9M) | 4.7KB | Differential-diagnosis pair |

**Cross-page extensions:** [[Dark Night]] gets substantial expansion. Companion to the [[The Power of Gone]] dissolution-side already mature. Likely seeds a contemplative-clinical differential register the wiki lacks.

---

## Wave 2 — Stub promotion + audit-named extensions (9 transcripts)

After Wave 1 the wiki has five new pages; Wave 2 promotes [[Self-Inquiry]] and pushes the audit's expansion targets.

| # | Transcript | Size | Target |
|---|---|---|---|
| 28 | Self-Enquiry & Mindfulness Meditation (pHUajtPXPDw) | 5.5KB | [[Self-Inquiry]] 🌱→🌿 (anchor) |
| 29 | A Deeper Freedom: Experiences of Selflessness (Hfw_tHC0A9w) | 2.4KB | [[Self-Inquiry]] / [[The Real No Self]] |
| 30 | Bodhicitta and the Bodhisattva Ideal (5kBiqluARdU) | 2.8KB | **Anchor** [[Bodhicitta and the Way of Service]] |
| 31 | The Final Stage and Service (b2anxOUgl1A) | 5.8KB | [[Bodhicitta and the Way of Service]] |
| 32 | Becoming a High-Wattage Broadcaster of Human Positivity (-KFJYzPYDfA) | 4.1KB | [[Bodhicitta and the Way of Service]] / [[Way of Human Goodness]] |
| 33 | A Mindfulness Path Arising Between Empowering Contrasts (ncGiwqCZ7rg) | 3.1KB | [[Way of Human Goodness]] / [[Big Picture]] |
| 34 | 6 Buddhist Consciousnesses & the 12 Sensory States (PDUvTid4hxk) | 4.9KB | [[Sensory Grid]] expansion (anchor) |
| 35 | Mindfulness & the Categories of Sensory Experience (Skl5LE7Uucg) | 5.7KB | [[Sensory Grid]] expansion |
| 36 | Dynamic Aspects of the Sensory System (8rSXFUWMoak) | 2.9KB | [[Sensory Grid]] expansion |

---

## Wave 3 — Long-form retrospectives + dialogs (8 transcripts; partly gated)

Highest value-per-transcript items, but most need Waves 1-2 to land first because they cross-reference nearly every page; ingesting earlier means the cross-references can't be wired. One is gated on retranscription completion.

| # | Transcript | Size | Notes |
|---|---|---|---|
| 37 | A Life of Practice and Service Shinzen at 80 (YghW4NNTxAo) | 53KB | **GATED: retranscription large-v3 in flight.** Massive biographical/synthesis. Touches [[Big Picture]], [[Total Happiness]], [[Way of Human Goodness]], [[Historical Influences]], [[Shinzen Young]] entity, possibly anchors a [[Sasaki Roshi]] entity page |
| 38 | Advanced Meditators Experience of Time (ouKeo7_TEAE) | 22KB | Three-way dialog (Khalsa + Mertz). Likely establishes new [[Phenomenology of Time]] page; deepens [[Penetration]], [[The Real No Self]], [[The Power of Gone]] |
| 39 | What to Expect and Do After a Mindfulness Retreat (0ifHks5EYZU) | 16.5KB | Substantially deepens [[Insight and Purification]] (integration register); pairs with upcoming SoE chs. 6-7 |
| 40 | Sasaki Roshi & Burmo-Japanese Mindfulness Fusion (-pMyY6Abi4g) | 6.0KB | Anchors [[Sasaki Roshi]] entity; deepens [[Historical Influences]] |
| 41 | Leonard Cohen, Sasaki Roshi & Love Itself Pt 1 | ~5.7KB | [[Sasaki Roshi]] biography; *le coup du vide est l'Amour Pur* lineage |
| 42 | Leonard Cohen, Sasaki Roshi & Love Itself Pt 2 | ~5.5KB | Same |
| 43 | Sasaki Roshi, Complex Number System & the Source of Love (hvFOe_JmSCw) | 3.6KB | Deepens [[Big Picture]] complex-field math claim |
| 44 | Humility to the Vanishing Point (Nwmj37W-NR8) | 6.4KB | **Use retranscribed/ version when complete** (not edited/). [[The Real No Self]], [[Return to the Source]] |

---

## Wave 4 — Specialized / cross-traditional / applied (~22 transcripts)

Fills specific gaps the book corpus pointed at but didn't fully treat. Most establish small new pages or substantial single-section extensions.

**Cross-traditional gaps (4-5 transcripts):**
- Jhanas and Focus on Rest (A-72haqjl4o, 6.6KB) — likely creates [[Jhana]] page or extends [[Way of Tranquility]]
- Jewish Mysticism & Mindfulness Meditation (ZfNdNA580yk, 5.3KB) — Kabbalah deepening of [[Mysticism in World Culture]]
- The Native American Sweat Lodge Pts 1-2 (~10.5KB combined) — indigenous-ceremony register
- The Secret of Archetypal Deity Yoga (6WtPrOE1JSk, 3.9KB) — tantric visualization extending [[Nurture Positive]]
- On Rites, Rituals, and Ceremonies (u9pgbO-N5QQ, 5.7KB) — ritual register for [[Mysticism in World Culture]]

**Energy body / Realm of Power (anticipated by SoE ch. 7):**
- Kriyas & Complete Experiences (e9AHh9MvgyQ, 6.6KB) — anchors [[Kriyas]] / [[Realm of Power]]
- Kriyas & the Cloud of Unknowing (aTaDZqB_RY8, 4.9KB) — kriyas + Christian apophatic bridge

**Applied mindfulness (recommend a small applied-domain cluster):**
- Mindfulness, Cancer & Healing Pts 1-3 (~23KB combined, Sat Dharam Kaur interview)
- Mindful Birth and Zen Parenting Pts 1-2 (~13KB combined)
- Mindfulness & Psychotherapy (ghBxjliqIPY, 6.2KB)
- Sleep Interruption & A Good Night's Rest (DUQFw2jNf7s, 5.7KB)
- Mindfulness and Behavioural Change (bGy2PdVzNMU, 7.0KB)

**Theory deepenings (single-page extensions):**
- The Trickle-Down Paradigm of Transformation (FdkODyvYxRg, 5.4KB) → [[Penetration]]
- Maximizing Psycho-Spiritual Growth (Windows & Walls) (5t3mHTtKfWk, 7.0KB) → CCE optimization
- The Reptilian Brain, Skinnerian Training & God (KlpXGXZ_dT0, 4.1KB) → [[Suffering Equation]]
- Bhanga (Dissolution) Interactive Pts 1-3 (~17KB combined) → [[Insight and Purification]] / [[Way of Flow]]
- Dissolution & T.S. Eliot (a344llNU15Y, 5.8KB) → [[Insight and Purification]]
- Equanimity and the Taste of Purification Pts 1-2 (~8KB) → [[Equanimity]] / [[Insight and Purification]]
- Growth and Tastes of CCE (ED0pXThS_nc, 6.6KB) → [[Surface and Deep CCE]]
- Ordinary Consciousness is the Way Pts 1-3 (~18.6KB) → [[Way of Flow]] / [[Big Picture]]
- Non-Dual Awareness (mwOccTTAcVw, 5.7KB) → [[The Real No Self]]
- Abrupt Flow Diminishings, Vanishings, Noting Gone (L-7LXHjGHfM, 9.5KB) → [[Gone]] / [[The Power of Gone]]

---

## Wave 5 — Defer or skip

- **7 header-only stubs (<800B) — skip entirely.** Identified in `_EDITING_PROGRESS.md`.
- **Khalsa standalone files** (NS7_uN8F6P8, jex0giLXNAs, 6XJN3TjhSZ8, Meqvr2zGn2U) — skip per audit policy.
- **~25-30 short guided sits / chants / silent sits** — defer; ingest only if the wiki develops a "Practice Recordings" register.
- **~50 RAW-OK files marked optional in the audit's Wave 5** — defer; revisit once the new-page architecture is mature. The audit doc explicitly flags these as optional and not blocking.

---

## Per-transcript ingestion methodology (validated by pilot)

Each ingestion uses the lean format from `wiki/source-yt-do-nothing-meditation-young.md`:

### Source page (one per video, in `wiki/`)

- Filename: `source-yt-{slug}-young.md` (or include co-speakers in slug if not solo Shinzen)
- Frontmatter:
  - `type: source`
  - `tags: [source, transcript, ...]` (additional tags reflect the talk's content)
  - `aliases: ["Talk Name (YouTube)", "videoID"]`
  - `sources: [raw/yt transcripts/{filename}.md]` — point at the canonical version (edited/ if cleaned, retranscribed/ if redone, root if raw-fine)
  - `confidence`, `importance`, `status`, `domain` per CLAUDE.md
- Body sections:
  - 1-2 sentence opening (the talk in miniature)
  - **Where it sits in the arc** — what existing wiki pages it relates to and what it sharpens
  - **Numbered load-bearing claims** — the actual work; phenomenological precision; primary-voice quotes; technical vocabulary the book treatment leaves implicit. The pilot's #1-7 numbered claims are the target compression.
  - **Register and stance** — what kind of talk this is, what's compressed, what's left out
  - **Lineage** — recording metadata, length, multi-part series position
  - **Related** — cross-links

### Wiki-page work (concept/thesis/synthesis pages)

- **For new pages:** create on the **anchor** transcript; subsequent series transcripts restructure as needed.
- **For extensions:** edit existing pages to add the new load-bearing claims; never overwrite — augment with attribution.
- **For series:** cross-link source pages among themselves AND to the wiki page they feed.

### Per-wave (not per-transcript)

- Update `index.md`: add new page entries; revise the wiki's shape paragraph if center moved.
- Append a single batched entry to `log.md` describing the wave (per-transcript log entries would degrade signal).

---

## Open decisions (confirm before kickoff)

1. **Retranscription gate** — confirm Wave 3 transcript #37 (Life of Practice at 80) waits until `retranscribed/_run.log` shows complete. Identify the 5 unnamed pendings before reaching them.
2. **Series strategy** — for E-C 4-part, D&U 4-part, Ox-Herding 3-part, Bhanga 3-part, Cancer 3-part: **one source page per video** (per pilot, recommended) or **one combined source page per series**?
3. **Wave granularity for human review** — checkpoint after each wave, or push through Waves 1-2 in sequence and surface the result?
4. **Edit-then-ingest iteration** — for raw-fine root files (Wave 1+ includes some), make a cleanup pass before ingestion or read directly?
5. **Per-wave logging** — recommend one log.md entry per wave for signal density. OK?

---

## Scoreboard (running tally — update as waves complete)

- Wave 1: 0/27 transcripts ingested · 0/5 new pages created
- Wave 2: 0/9 transcripts ingested · 0/2 new pages, 0/2 stub-promotions, 0/1 expansions
- Wave 3: 0/8 transcripts ingested · 0/1 entity page, 0/1 phenomenology page
- Wave 4: 0/~22 transcripts ingested
- Total ingested: 0/~66 priority transcripts (out of ~205 in corpus)

---

*This plan is the curation. Execution begins on user confirmation of the five open decisions above.*
