# Public Atlas — Editorial Plan

*An implementation brief for a full editorial pass on `public-atlas/`. Written for an executing agent (Codex) with no token budget; the human's directions are upstream of this and load-bearing. Follow the intent, not just the letter — but where this document is specific, it is specific on purpose.*

---

## 0. The one-sentence mandate

The atlas already **covers** Shinzen's system. It does not yet **transmit** it. Close that delta: convert the compiler's machine-shape into a human-shape — a living, walkable path in an alive register — **without losing the calibrated honesty that makes it trustworthy.** The honesty is not the obstacle to aliveness; in Shinzen's system the disinflation *is* the no-self, and it is the most reachable thing in the whole edifice. Keep it. Stop smearing it.

---

## 1. Diagnosis — what the delta actually is

The atlas is rich in coverage and dead in delivery. The problem is **not** missing content. It is that the public face inherited the internal compiler's form (the seven-page-type schema, confidence tiers, and routing surface from `AGENTS.md`) and wore it on the outside. Seven concrete failures, each with a fix in §3–§6:

- **D1 · Template tyranny.** All ~70 pages run one rigid skeleton: *Why This Matters → Core Distinction → [Working Model] → Practice Meaning → Common Confusions → Safety and Scope → Source Posture → Source Trail → Next Reading.* Seventy teachings read as seventy rows of one spreadsheet. No page is allowed the shape its own content wants.
- **D2 · Defensive saturation.** The identical safety sentence — *"Meditation language does not replace medical care, therapy, emergency support, consent, ordinary ethics, relationship repair, or qualified guidance"* — repeats near-verbatim across ~50 pages, plus a "Safety and Scope" + "Common Confusions" block on nearly every page. The atlas spends roughly a third of its words defending itself. A retreat-grade reader feels *managed*, not met. Safety becomes an incantation the eye learns to skip — which means it stops protecting anyone.
- **D3 · Negation-first definitions.** Pages define by what a thing is *not* before letting it be what it *is* ("Complete experience is not intensity. It is not endurance. It is not liking pain…"). Calibration-correct, transmission-dead. The taste never arrives.
- **D4 · In-band evidence machinery.** "Source Posture / Source Trail / *Shinzen says* / *Compiled synthesis* / *Speculative extension*" sits in the body of every page. This is the compiler's confidence-tier system worn on the skin. `how-to-read-this-site.md` itself says this should *not* happen ("point onward rather than burying the reader under transcript archaeology") — yet every page does it.
- **D5 · No spine, flat altitude.** Seventy sibling pages, all 600–900 words, all equal weight, all cross-linking sideways. The six load-bearing pillars (CCE · complete experience · Flow/Gone · no-self · Source/Zero · behavior-test) are formally indistinguishable from capillary pages (Zooming, Focus Coverage, Effort Regulation). A human cannot feel what is central, and there is no arc — no journey from *you arrive* to *you go deep* to *you come back*.
- **D6 · The front door is a routing wall.** `index.md` is a ~40-row "if you are trying to…" lookup table + 6 reader-path rows + "Three Doors" + a full section dump. It is the agent index lightly dressed. A human landing here bounces.
- **D7 · Bloodless voice.** Everything is third-person description *about* the teaching ("Complete experience is the idea that…"), never the teaching *delivered*. Shinzen's living idiolect is paraphrased into beige. The repo-root pieces (`Shinzen - The Living Throughline.md`, `Shinzen - For a Clear Hour.md`) prove the identical content can reach a reader. The atlas never reaches.

**Root cause:** the atlas was optimized, like the compiler, for *random access by a machine that needs every claim stamped and every page self-defending.* A human needs the opposite: a front door, a spine to walk, weight they can feel, a voice that trusts them, and rigor concentrated where it bites rather than smeared where it numbs.

---

## 2. Target architecture — spine, organs, capillaries

Replace the flat 70-page mesh with **three explicit altitude tiers**, marked in frontmatter (`tier: pillar | practice | boundary`) and reflected in *form*. Pillars are read top-to-bottom; everything else is read on demand and hangs off a pillar.

### 2.1 The Spine — ~10 Pillar pages (read in order)

A single canonical front-to-back read-through that delivers the whole living throughline. Adapt the substance and register of `Shinzen - The Living Throughline.md` into these. Each pillar **owns a cluster** of capillary pages and ends by pointing down into them.

| # | Pillar page (target) | Absorbs / fronts these existing pages |
|---|---|---|
| 1 | **The One Move** (complete experience as the whole gesture) — also the homepage's spine entry | `what-shinzens-system-is`, `complete-experience`, `signs-and-non-signs-of-completion` |
| 2 | **The Three Skills** (CCE, as three independent axes with tastes) | `mindfulness-as-cce`, `concentration-power`, `sensory-clarity`, `equanimity` |
| 3 | **The Sensory Interface** (See/Hear/Feel, the grid, Feel/Image/Talk) | `see-hear-feel-and-the-sensory-grid`, `sensory-grid`, `feel-image-talk`, `inner-sensory-system` |
| 4 | **The Routes** (Five Ways / how you actually start; one route can train the whole path) | `basic-mindfulness-system`, `five-ways`, `main-practice-routes`, `choosing-a-practice-route` |
| 5 | **Impermanence** (Flow, Gone, Expansion–Contraction, dissolution) | `impermanence`, `rest-flow-gone`, `flow-and-gone`, `expansion-and-contraction`, `dissolution-and-bhanga`, `spaciousness` |
| 6 | **No-Self Without Erasing the Person** (de-coagulation, not erasure; say yes to the self) | `no-self-without-erasing-personality`, `self-inquiry-and-turn-back`, `deconstruction-and-reconstruction` |
| 7 | **Source, Zero, and the Honest Edge** (afterglow boundary; intimacy without overclaim) | `source-zero-and-speculation`, `source-science-and-analogy`, `source-and-claim-tiers` (claim-tier mechanics move to §4) |
| 8 | **The Return** (operational enlightenment; the marketplace, not the mountaintop; behavior as the uncounterfeitable test) | `operational-enlightenment`, `behavior-and-service-test`, `surface-to-source-path-map` |
| 9 | **The Aim** (Total Happiness; condition-independent happiness; love and service) | `total-happiness`, `total-happiness-aim-structure`, `condition-independent-happiness`, `source-service-and-bodhicitta`, `way-of-human-goodness` |
| 10 | **Going Deep Safely** (one honest chapter — the void's evil twin, the pit, intensity, bypass) | `safety-scope-and-accountability`, `dpdr-and-the-pit-of-the-void`, `completion-versus-bypass-and-intensity`, `intensity-and-embodiment-safety`, `altered-phenomena-and-dissolution-safety` |

> The teacher/lineage material (`shinzens-teaching-method`, `lineage-translation`, `mastery-without-guru-inflation`) becomes a short standalone **"About the Teacher and the Lineage"** appendix linked from the homepage footer — interesting, not on the critical path.

### 2.2 The Organs — ~30 Practice pages (`tier: practice`)

The actual techniques and tunings — `noting`, `do-nothing`, `focus-on-rest`, `nurture-positive`, `auto-output-practice`, `zooming`, `effort-regulation`, `focus-coverage-strategies`, `calming-and-clarifying`, `equanimity-training-ladder`, `recycle-the-reaction`, `turn-toward-and-turn-away`, the `way-of-*` pages, etc. Crisp, operational, "here is how you do it, here is the failure mode it fixes, here is how it itself goes wrong." Light on caveats. Each links *up* to its pillar and *sideways* only where genuinely useful.

### 2.3 The Reference shelf — ~10 Boundary/Reference pages (`tier: boundary`)

`glossary`, `source-and-claim-tiers`, `guidance-scope-and-accountability`, `practice-method-safety`, `applied-life-boundaries`, `how-to-read-this-site`, the teacher appendix. **This is where rigor is allowed to concentrate** — careful, honest, fully caveated. That is appropriate *here* and nowhere else.

### 2.4 Consolidation

The merges in 2.1 reduce ~70 pages to a cleaner set. **Do not delete content** — fold it. When a capillary page is absorbed into a pillar, either (a) keep it as a short "deeper cut" page if it carries operational detail a practitioner would want in isolation, or (b) merge it fully and leave a redirect stub. Default to **keeping practice pages standalone** (they're looked up by problem) and **merging the thin synthesis/overview pages** (they're read once). Flag any merge that would lose a Shinzen distinction and keep the page instead.

---

## 3. Global editorial rules — apply to **every** page

These are mechanical enough to sweep across all 70 files in one pass, before the deep pillar rewrites.

1. **Kill the mandatory skeleton.** Delete the requirement for fixed headings. Specifically:
   - **Delete** every "Why This Matters" section — its content either folds into the opening or is cut. *Show the stakes; never announce them.*
   - **Delete** "Core Distinction" *as a heading* — fold the distinction into the prose where it lands hardest.
   - **Delete** "Practice Meaning" *as a heading* — the whole page must be practice-meaningful; if a page has a separate "practice meaning" section, the rest of the page has failed.
   - **Delete** "Source Posture" and "Source Trail" sections from page bodies (relocate per §4).
   - **Keep** tables, "signs vs non-signs," and routing/"when it's not working" content where it is genuinely useful — these are the strongest existing material. Just stop burying them under preamble.
2. **Lead with the live thing.** Every page's first sentence is the teaching itself, delivered — not "X is the idea that…" and not a meta-justification. The reader should feel the thing in the first three lines.
3. **Define forward, not by negation.** State what it *is* first, in its own taste. Bring in "what it is not" only after the thing is alive, and only the one or two confusions that actually bite.
4. **Strip the disclaimer incantation.** Remove the repeated "Meditation language does not replace medical care…" boilerplate from all teaching pages. Safety survives *only* where it is load-bearing for that specific page, and then as one sharp, specific sentence — not a generic block (see §5).
5. **Cut the meta.** Remove sentences that describe the atlas describing the teaching ("This page maps…", "The atlas treats…", "This is one of the heart ideas of Shinzen's system"). Say the teaching.
6. **Preserve Shinzen's idiolect verbatim.** These exact phrases must survive and should be *used*, not paraphrased: *complete experience · concentration, sensory clarity, equanimity · See / Hear / Feel · Flow · Gone · Rest · the Five Ways · "you don't have to like it, you just have to feel it" · "no longer need to make an object out of self or world" · Source · Zero · Total Happiness · the tastes of CCE · "today's enlightenment is tomorrow's mistake."* Idiolect is the transmission; generic-Buddhism paraphrase is the leak.
7. **Trim length to fit register, not a target.** Most pages will get *shorter* as boilerplate and meta come out, even as voice comes in. Do not pad to hit a word count.

---

## 4. Relocate the rigor — don't delete it, concentrate it

The claim-tier honesty is the crown jewel. It moves from *everywhere, in-band, dulling* to *once, centrally, plus sharp inline marks where it matters.*

- **Explain the convention once.** In `how-to-read-this-site.md`, keep the five-tier idea (*Shinzen says / compiled synthesis / editorial inference / speculative / not established*) explained well, in voice.
- **Delete the per-page "Source Posture" + "Source Trail" sections.** They become invisible by default.
- **Mark only what's actually speculative, inline, sparingly.** When (and only when) a page makes a claim that leaves Shinzen's direct teaching — Source metaphysics, neuroscience, category-theory/entropy analogies, clinical thresholds — drop a single light callout exactly there, e.g.:
  > *Speculative — Shinzen's imagination, not established science:* the category-theory and entropy parallels are analogy for analyzing consciousness, not proof about physics.
- **Net effect:** the 90% of sentences that are just Shinzen's teaching read clean and unstamped; the 10% that overreach are flagged precisely. The honesty becomes *more* visible by being rare.

---

## 5. Relocate safety — from incantation to scalpel

- **One honest chapter** (Pillar #10, "Going Deep Safely") carries the real safety transmission: the pit of the void, the void's evil twin, DPDR vs. no-self, intensity/embodiment limits, bypass vs. completion. Make this page *excellent and unhedged* — written like someone who has watched it go wrong and respects the reader enough to be plain. This is where the genuinely load-bearing warnings live and breathe.
- **Two or three boundary/reference pages** (`practice-method-safety`, `guidance-scope-and-accountability`, `applied-life-boundaries`) hold the careful operational detail for those who need it.
- **On all other pages:** safety appears *only when this specific teaching carries this specific risk*, as one concrete sentence placed where it bites. Examples: Source/Zero genuinely needs the pit warning → keep it, sharp. Noting does not need the medical disclaimer → cut it. "If the emptiness turns cold and you can't function, that's the place to stop and get help" belongs on the no-self/Source pages, not on the breathing-technique page.
- **The test:** a deleted safety sentence should be one a careful reader would never miss because it didn't apply. A kept one should make a real practitioner slow down.

---

## 6. Rebuild the front door (`index.md`)

The homepage must make a human want to read on, in under a screen-and-a-half. Structure:

1. **A short voiced invitation** (4–6 sentences): the one move under everything; who this is for (serious practitioners who already know the taste); what it promises and refuses. No table in the first screen.
2. **The Path** — the numbered spine (§2.1, pillars 1→10) presented as a walk, each with a one-line lure, not a bare link.
3. **A small "start by problem" entry** — 6–8 of the most common live problems, *not* the 40-row table.
4. **Footer:** links to the teacher appendix, the full map, the glossary.
5. **Move the giant routing table out** to a separate `map.md` ("Full Index — every page, by problem") for people who want lookup. Keep it; just stop making it the front door.

`how-to-read-this-site.md` shrinks to: the claim-tier convention (once), the one-paragraph safety posture (once), and "read The Path in order, or jump by problem." Delete the six-row reader-doorway matrix — the spine replaces it.

---

## 7. Calibration — before / after (the most important section)

This is the register target. Match the *temperature*, not the exact prose. It is **alive and clear, not purple or devotional** — devotional would betray the honesty. The voice is someone who has actually practiced this telling you straight, leading with the live thing, trusting you, and naming stakes plainly.

**BEFORE** — `complete-experience.md`, current opening:
> Complete experience is the idea that sensory events contacted with enough CCE over time can become less binding, more fulfilling, and more learning-bearing.
> ## Why This Matters
> This is one of the heart ideas of Shinzen's system. It explains why the system does not merely chase calm or special states. Ordinary experience itself can become the path when it is met with concentration, sensory clarity, and equanimity.
> ## Core Distinction
> Complete experience is not intensity. It is not endurance. It is not liking pain. It is not dramatic phenomena…

**AFTER** — target register (same content, delivered):
> There is one move under everything Shinzen teaches. Meet what is actually happening — the felt fact of it, not the story about it — with a little steadiness, a little clarity, and a willingness not to interfere. Stay with it to the end. When you do, the experience **completes**: it arises and passes without ever quite hardening into a thing.
>
> Hear what completion is, because nearly everyone gets it wrong. It is not the experience going away. The pain still hurts; the grief still grieves; the pleasure still pleases. What drains out is the *something-ness* — the hardness, the grip, the sense that this has you. The experience becomes **more** vivid and **less** binding at the same time. That double motion is the tuning fork for the whole path: if a practice is making you duller, number, farther away, that is not completion. That is hiding.

Then the page keeps its genuinely good existing material — the four-part working model (Contact · Clarity · Equanimity · Time) and the signs/non-signs table — but as the *body* under a living opening, not as the whole page. The repo-root files `Shinzen - The Living Throughline.md` (register for pillars) and `Shinzen - For a Clear Hour.md` (temperature ceiling — pillars should run a touch cooler/more operational than this) are the canonical anchors. Read both before rewriting any pillar.

---

## 8. Guardrails — what must **not** be lost

1. **The calibrated honesty.** Disinflation, "the maps are poor," "today's enlightenment is tomorrow's mistake," intimacy-without-overclaim. Relocated (§4), never softened into either false certainty *or* mushy reverence.
2. **Shinzen's distinctions.** Every phenomenological fork the compiler preserves (Flow vs. Gone; no-self vs. DPDR; completion vs. suppression; de-reification vs. disappearance; afterglow vs. Source itself; simultaneous Expansion–Contraction). If a rewrite blurs one to read smoother, the rewrite is wrong.
3. **The behavior/service test as the spine of trust.** Never let the alive register tip into state-glorification. The uncounterfeitable test is conduct over time. This is the safety rail that lets the rest go deep.
4. **The non-imitation boundaries** on advanced material (e.g., the "Weird Meditation" no-objectification report, terror-as-Flow). Keep them as one clean sentence, not a disclaimer wall.
5. **Source-groundedness.** Stay paraphrase-based and rights-clean; no long quotations. Alive register comes from *delivery*, not from quoting more.

---

## 9. Execution order (phased)

1. **Phase 0 — Scaffold.** Add `tier:` to frontmatter on all pages per §2. Create `map.md` and move the big routing table there. Stand up the 10 pillar files (can start as the existing absorbed pages renamed/stubbed).
2. **Phase 1 — Global mechanical sweep (all ~70 pages).** Apply §3 rules 1, 4, 5 and §4 deletions: strip the fixed skeleton headings, the disclaimer boilerplate, the meta-sentences, and the in-band Source Posture/Trail blocks. This alone removes most of the deadness. *Do not yet rewrite voice.*
3. **Phase 2 — Rewrite the spine (10 pillars).** Deep alive-register rewrites per §3, §7, anchored to the repo-root pieces. This is the highest-value phase; spend the most care here.
4. **Phase 3 — Front door + safety chapter.** Rebuild `index.md` (§6) and write Pillar #10 "Going Deep Safely" (§5) as standout pages.
5. **Phase 4 — Practice pages (organs).** Medium-touch pass: lead with the live move, ensure each is operational, link up to its pillar, place only load-bearing safety.
6. **Phase 5 — Reference shelf + consolidation.** Tidy glossary/boundary pages (rigor allowed here), execute the §2.4 merges/redirects, fix all internal links, verify nothing orphaned.
7. **Phase 6 — Coherence pass.** Read the spine front-to-back as one human would. Check: does it walk? Does weight feel right? Does any page still smell like the machine? Fix.

---

## 10. Confirmed decisions — **execute directly, no further confirmation needed**

All three open calls are resolved by the human. Codex should treat these as final directives:

1. **Pillar count: 10.** Keep all ten pillars as specified in §2.1. "The Return" (Pillar #8) stays its own page — the inversion from void to marketplace is the most important correction for a serious practitioner and must not be folded into Source/Zero.

2. **Capillary handling: keep practice pages standalone.** Fold only thin overview/synthesis pages (e.g., `what-shinzens-system-is`, `basic-mindfulness-system` collapse into the relevant pillar introductions). All pages with genuine operational technique detail (`noting`, `do-nothing`, `focus-on-rest`, `nurture-positive`, `effort-regulation`, `zooming`, `equanimity-training-ladder`, the `way-of-*` pages, etc.) survive as standalone practice pages, linked from their owning pillar.

3. **Teacher/lineage material: appendix.** `shinzens-teaching-method`, `lineage-translation`, and `mastery-without-guru-inflation` become a single short appendix page titled something like **"The Teacher and the Lineage"** — linked from the homepage footer, not on the critical path, not a pillar.

Everything in this document is a final decision. Execute it directly.

---

## 11. Execution state

- **2026-06-04:** Phase 0 scaffold is complete. Added `tier:` to public atlas
  frontmatter, created `public-atlas/map.md`, replaced the homepage with a
  short front door, stood up ten pillar scaffold pages, and created
  `public-atlas/teacher-and-lineage.md` as the teacher/lineage appendix.
- **2026-06-04:** A bounded Phase 1 mechanical sweep is complete. Removed
  per-page `Source Posture` and `Source Trail` sections, stripped the repeated
  generic "Meditation language does not replace..." sentence, and removed the
  most rigid `Why This Matters`, `Core Distinction`, and `Practice Meaning`
  headings while preserving their body content for later voice rewrites.
- **2026-06-04:** First Phase 2 spine rewrite is complete. The ten pillar
  pages now read as draft spine chapters rather than placeholders, with deeper
  links preserved to the existing practice and boundary pages.
- **2026-06-04:** Phase 4 practice-page pass is complete. Forty-nine
  then-current practice pages received path-chapter `Next Reading` up-links;
  after Phase 5 consolidation, the active public set stands at 47 practice
  pages. High-friction openings in complete experience, condition-independent
  happiness, bhanga, Expansion-Contraction, CCE, Source/service, route choice,
  and the Surface-to-Source map were rewritten away from meta-description and
  toward live practice use.
- **2026-06-04:** Phase 5 reference/consolidation is complete. The thin
  `what-shinzens-system-is` and `basic-mindfulness-system` overview pages now
  function as redirect stubs into the ten-part path. `shinzens-teaching-method`,
  `lineage-translation`, and `mastery-without-guru-inflation` are folded into
  `teacher-and-lineage.md`, with legacy stubs preserved for old links. The
  full map, glossary, and README now route to the path chapters and single
  teacher appendix.
- **2026-06-04:** Phase 6 front-to-back coherence read is complete. The ten
  path chapters were read in order, self-links and duplicate navigation
  introduced by consolidation were removed, and the full map now registers the
  legacy redirect stubs explicitly.
- **Status:** the first `ATLAS - Editorial Plan.md` workstream (register and
  transmission) is complete through front-to-back coherence. That axis is not
  the same as the information-value axis below.

- **2026-06-05 (information-value / depth pass - a different axis):** The
  register work above made the atlas *read* well; a separate question is what
  it *contains*. The prior compiler-to-atlas audits closed breadth - a page
  and a route for each reader job - and reasonably declared that complete. Re-
  reading against the user's goal ("close the information value delta... what
  important points/claims are missing") surfaced a depth gap instead: specific
  high-resolution teachings the compiler holds that the register pass had
  smoothed out or never surfaced. These are invisible to a routing audit
  because they are knowledge, not reader-jobs. An empirical probe of the atlas
  for ~20 load-bearing compiler concepts found clear absences. Closed the
  highest-value ones this pass, in protected public register:
  - `source-service-and-bodhicitta.md` - added the four/five-source love map
    (natural/uncovered, compassion-from-one's-own-suffering, relative Focus-Out
    I-Thou merging, absolute shared-Source), from [[Where Does Love Come In]].
  - `focus-on-rest.md` - replaced the vague rest list with Shinzen's six named
    flavors (Relaxation, Light, Silence, Peace, Blank, Quiet) and added the
    jhana/shamatha reworking, the pleasant-rest biofeedback loop, and the
    do-not-camp-in-tranquility boundary, from [[Jhanas and Focus on Rest]].
  - `self-inquiry-and-turn-back.md` - added the three meanings of non-dual
    awareness and the no-place-to-stand decentering move with its figure-ground
    reversal and CCE-capacity precondition, from [[Non-Dual Awareness]] and
    [[No Place to Stand]].
  - new `good-place-traps.md` - the six good-place traps (map, fundamentalism,
    tranquility, realms-of-power, enlightenment, observer) with antidotes, from
    [[Six Common Traps on the Path to Enlightenment]]; wired into the full map,
    operational-enlightenment, going-deep-safely, focus-on-rest, and
    self-inquiry. This also surfaces the previously-thin powers/intermediate-
    realm material as ordinary sensory practice rather than status.
  Mechanical checks after the pass: non-ASCII scan clean, wikilink/claim-ID
  leak scan clean, all relative links resolve, new page registered in the map.

- **2026-06-05 (information-value / depth pass, round 2 - transformation
  mechanism):** Raised the system's causal core to compiler resolution where
  the register pass had left slogans. An empirical probe confirmed
  `insight-and-purification.md` stated the formula (CCE + time -> insight +
  purification) but not the *mechanism*, and that the "why formal practice
  works" rationale was absent from the pages that should carry it. Closed, in
  protected register, mechanically verified:
  - `insight-and-purification.md` - the trackable-implies-tractable mechanism
    (suffering as a multiplying tangle; sensory clarity as discriminate +
    detect; insight = seeing half, purification = releasing half; named the
    Fundamental Theorem of Mindfulness), plus the motivation model (taste of
    purification -> positive feedback loop, hockey-stick non-linearity) with
    its shape-not-schedule boundary.
  - `equanimity.md` - how equanimity is *learned*: the body-level feedback loop
    (interference = suffering, noninterference = relief), with the Skinnerian /
    "reptilian brain" analogy bounded as teaching device, never self-punishment.
  - `practice-cycles-and-life-architecture.md` - why formal sits and retreats
    earn their place (environmental simplification for immediate feedback;
    retreat = the same laboratory enlarged, not endurance).
  Cross-wired the three pages; cut two redundant vague lines. Mechanical checks
  clean: non-ASCII, wikilink/claim-ID leak, and all relative links resolve.

- **2026-06-05 (information-value / depth pass, round 3 - primal Feel):**
  Empirical probe found "primordial Feel" named once, in a list, in
  `altered-phenomena-and-dissolution-safety.md` and taught nowhere (the
  applied-life hit was a false positive on "infant care"). The teaching is
  substantial, self-contained, and was homeless - distinct from bhanga
  (breakup of order) and from the DPDR/pit cold void - so it earned a new
  page, in protected register, mechanically verified:
  - new `primal-feel.md` - the hot, chaotic, infant-like body emotion ("pure
    heat of Feel") beneath emptiness; the recognition tell (big provocations
    stop landing while a tiny trigger detonates); the strata mechanism (a
    layer integrates, its grip shrinks, a more primitive stratum is exposed,
    so local weirdness is not global decline); the live router (correlation
    check, dominant sensory channel, include Feel-vanishings in Gone, recycle
    the reaction, manageable doses, reconstruction); terror-as-Flow held with
    the non-imitation boundary; the compassion face; and the hot-vs-cold
    differential against DPDR. The infant-origin / cosmic-parents / Zero-
    polarity frame is kept as Shinzen's teaching image, not developmental
    psychology, neuroscience, or a clinical reparenting protocol.
  Wired into `map.md` (problem-row + Phenomenology) and six neighbors; the
  impermanence pillar gained a parallel "vanishing turns hot" routing row and
  altered-phenomena's bare list-mention became a real pointer. Mechanical
  checks clean: non-ASCII, wikilink/claim-ID/tier-stamp leak, all relative
  links resolve, new page registered in the map.

- **2026-06-05 (information-value / depth pass, round 4 - ox-herding depth):**
  Took the recommended steer after re-running the probe to confirm it. The
  `surface-to-source-path-map.md` Ox-Herding Parallel was a 5-row table that
  collapsed the distinctions the compiler keeps, so a first taste read as
  arrival, surrender read as "relaxing," and the final triad read as one
  ending. Enriched the existing parallel in place - no new page (near-zero
  bloat), in protected register, mechanically verified:
  - `surface-to-source-path-map.md` - the parallel now keeps all ten pictures
    as three distinct movements. The opening four are held apart (searching ->
    footprints as inspiration -> glimpse / "a little vipassana" -> catching as
    first no-self/stream-entry/kensho with the ox still wild) so a first taste
    is not mistaken for arrival - the front-end-not-one-attainment point the
    compiler is explicit about. The middle three turn on surrender proper:
    riding-the-ox-backward as giving up the need for orientation, faith as
    releasing the demand to know where experience is going (not "relaxing"),
    kept distinct from taming (stabilization) and coming-home (repose). The
    final triad is split into no substance / ordinary appearance (mountains,
    cherry blossoms) / marketplace service, with service as the final cause
    (one's Source is everyone's Source) so the map cannot end at private
    emptiness. Calibration kept: diagnostic not status-ladder; riding backward
    needs CCE + functioning + support or it becomes passivity/dissociation/
    fatalism; marketplace "teaching" is not self-certifying (readiness, consent,
    feedback, anti-dependency are separate); the map stays provisional, not a
    final taxonomy or verified history.
  No new page, so map.md wiring is unchanged (the page is already routed from
  the cross-tradition path, the Transformation section, and a problem row).
  Mechanical checks clean: non-ASCII, wikilink/claim-ID/tier-stamp leak, all
  relative links resolve.

- **2026-06-05 (information-value / depth pass, round 5 - serious illness /
  healing, reader-probe):** Switched probe direction per the round-5 plan:
  instead of grepping the atlas for a compiler term (supply-side), brought a
  hard reader question and tried to answer it at compiler resolution from the
  atlas alone. Probe 1 - "I have a serious diagnosis: what do I do, and what
  should I not expect?" - failed. The atlas carried serious illness only as one
  boundary row (turn toward/away; medical gate first) plus a severe-Wall
  pointer; a grep across all 90 pages for the router language (suffering
  reduction, objective healing, non-consensual retreat) returned empty, and the
  "what should I not expect" half was entirely absent. The teaching is
  substantial (three cancer/healing parts plus the sickness talk), self-
  contained, and homeless, so it earned a new page, in protected register,
  mechanically verified:
  - new `serious-illness-and-healing.md` - the two-aim router (objective
    healing vs suffering reduction, with suffering reduction as Shinzen's
    default *because* it does not depend on a disease-course effect - "your
    physical discomfort does not go away, but your suffering can"); the
    "non-consensual retreat" reframe paired with the anti-austerity correction
    (rest, sleep, breaks, treatment are method, not failure); the sensory-
    challenge decomposition (local / global physical, emotional body, image,
    talk); the turn-away branch with background permission and the ten-minute
    floor; the healthy turn-toward branch (divide-and-conquer - fused channels
    multiply, separated they add, equanimity drains resistance - "the miracle
    of mindfulness"), marked as trained rather than a crisis improvisation; and
    the "no place to turn" safeguard. Calibration kept: no cure-promise; no
    patient-blame (the mind-body link is conditional only); suffering reduction
    never displaces oncology, pain relief, or palliative care; objective-
    healing imagery is optional and unproven; the numerical analogy is a
    teaching device, not measurement.
  Wired into `map.md` (problem-row + Safety section) and four neighbors
  (applied-life-boundaries gains a body pointer + Go Deeper edge,
  windows-and-walls the severe-illness row, and turn-toward, physical-senses,
  and condition-independent-happiness their Go Deeper edges). Mechanical checks
  clean on all changed files: non-ASCII, wikilink/claim-ID/tier-stamp leak, all
  relative links resolve, new page registered in the map. (Observation, not
  this round's job: `windows-and-walls.md` still carries a pre-existing
  `## Source Trail` heading the invariant scan flags - it predates round 5.)

- **Remaining depth gaps (next iteration, not yet closed):** the applied-life
  branches still thin in the atlas (childbirth, sleep, sexuality, lucid
  dreaming, stimulants) from the compiler's Gate 9 - cancer/healing was the
  highest-value one and is now closed (round 5) - each to stay one clean
  sensory-coaching read with its scope boundary, not a clinical guide; and the intermediate-realm / powers depth (only lightly
  surfaced via good-place-traps), which the compiler holds mostly in its
  speculative tier, so port the practice-handle and the boundary, not the
  metaphysics. The atlas is deliberately **not** declared complete on the
  information-value axis; this is four strong iterations in, not a closeout.

- **2026-06-05 (register / safety scalpel pass - D1/D2 closure):** Executed the
  section-3/5 "scalpel" the original plan called for but the first register
  pass had left half-done. The two standing defensive sections the diagnosis
  named - `Common Confusions` (63 pages) and `Safety and Scope` (52 pages, plus
  one `Safety And Scope` casing variant the count had missed) - were dissolved
  into a single page-specific failure-mode section per page (e.g. "Counterfeits
  of Completion", "When To Stop and Get Help", "Reading the Hot Layer Safely"),
  with the bare "X is not Y" negation stacks de-listed into prose. Conservative
  on content: every page-specific safety line was kept; only genuinely generic
  disclaimer boilerplate was cut, on six pages - full cut on
  `concentration-power`, `equanimity`, and `way-of-flow` (the "does not replace
  medical care, therapy, emergency support..." incantation wearing a per-page
  prefix), compression on `nurture-positive`, `total-happiness`, and
  `way-of-human-goodness`. Also fixed a malformed collapsed heading on
  `safety-scope-and-accountability` ("## Safety and Scope If risk is
  active..."), removed the six leftover `Source Trail` sections on the boundary
  pages flagged earlier (only one of which the round-5 note had caught), and
  trimmed residual meta-phrases ("In this atlas", "the atlas reading", "red or
  yellow safety page"). Separately reconciled the public README counts (82 ->
  90 content pages; 47 -> 51 practice, 24 -> 28 boundary; validation-check
  expected count 82 -> 90). Mechanical checks clean: 0 residual skeleton
  headings (case-insensitive), 0 `Source Trail`/`Posture`, all relative links
  resolve, non-ASCII scan clean, no empty sections or triple-blank artifacts,
  content page count 90. This closes the D1/D2 "template tyranny / defensive
  saturation" axis the register pass had only partly addressed; the safety
  transmission is now scalpel, not incantation, per section 5.
