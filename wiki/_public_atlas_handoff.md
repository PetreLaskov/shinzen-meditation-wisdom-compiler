# Public Atlas - Working Handoff (read this first)

This is the living handoff for the iterative atlas workstream. It is internal
memory, not evidence for Shinzen claims. Each round, the working instance
updates this file. If a better frame than the one below exists, adopt it - the
human's standing instruction is "restate the problem in whatever representation
YOU find most powerful; discard mine if a better one exists. I'll give feedback
on the gap, never on the path."

## The goal (verbatim intent)

Use the strong internal **compiler** (`wiki/`) to make the public **atlas**
(`public-atlas/`) maximally valuable for the *serious meditation practitioner*,
while protecting the atlas's public, human-readable register. Close the
information-value delta between compiler and atlas: what pages are missing, what
important points/claims are missing.

Prime directive: **ship real atlas value this round, then verify it.** Judged on
the gap (the result), not the path (your method). You have full autonomy on method.

## Orientation (do this in ~2 minutes)

- `AGENTS.md` - the compiler's operating contract and objective.
- `wiki/index.md` - the compiler's routing surface (368 compiled pages).
- `wiki/Current Model.md` - the compiler's distilled whole-system synthesis;
  the densest single artifact of accumulated value. Skim it to feel what the
  compiler *knows*.
- `public-atlas/index.md` + `public-atlas/map.md` - the atlas front door and
  full map (~89 pages: home, 10 pillars, ~48 practice, ~28 boundary/reference).
- `archive/Shinzen - The Living Throughline.md` - the densest register/voice
  reference in the repo: the whole system written in the living register. Read
  it early and match its voice when porting; its sections map to most depth
  gaps (e.g. its part IV supplied this round's primal-Feel language).
- `ATLAS - Editorial Plan.md` (tail, section 11) - execution state for both
  axes; read the four 2026-06-05 depth-pass entries (round 4 is the latest state).

## The reframe (load-bearing - do not lose this)

The atlas is a **lossy compression of the compiler.** It has TWO orthogonal
gaps, historically conflated:

1. **Transmission loss** - does it *read* like a living path vs a machine?
   CLOSED by the `ATLAS - Editorial Plan.md` register pass (spine, voice, front
   door, safety-as-scalpel) for the spine; do not re-litigate that part. NOTE
   (2026-06-05): the register *tic-pass* is mid-flight, NOT fully closed -
   `wiki/_atlas_register.md` "Step 3 IN PROGRESS" is applying mechanical
   tic-fixes (closer de-templating / table-audit / safety-as-contact) across the
   ~77 long-tail pages, route-cluster by cluster (A-E done, 44 left). If you
   edit a long-tail page for the information axis, read that file's Step 3 block
   first and keep its method, so the two passes do not fight.
2. **Information loss** - does it still *carry* the compiler's high-resolution
   teachings? THIS is the live axis. Prior audits mis-measured it as *breadth*
   ("a page and a route for each reader-job"), found yes, and prematurely
   declared the whole objective complete. The real delta is *depth*: specific
   load-bearing distinctions/maps/mechanisms the register pass smoothed out or
   never surfaced. They are invisible to a routing audit because they are
   knowledge, not reader-jobs.

Closing the delta = recover the lost high-resolution teachings INTO the readable
form. Raise fidelity without lowering readability. Add *teaching content*, never
caveats/meta/boilerplate (that was the old deadness the register pass removed).

## The method that works (reusable engine)

1. **Probe for absence empirically** - do not trust any "complete" verdict or
   your own hunch. From `public-atlas/`, grep for high-value compiler concepts
   and see what is absent/thin:
   ```
   cd public-atlas && grep -rilE "PATTERN" . --include=*.md
   ```
   Pull candidate concepts from `wiki/Current Model.md` and `wiki/index.md`.
   0-2 hits (or glossary-only) = candidate gap.
2. **Verify the gap** - read the atlas page that *should* carry it; confirm it
   is actually missing (grep can mislead; a concept may be present under other
   words).
3. **Source it** - read the compiler source page (`wiki/<Title>.md`) for the
   teaching. Note the load-bearing distinction, the idiolect to preserve, and
   the calibration boundary that must survive.
4. **Port into protected register** - enrich an existing page where a natural
   home exists; add a page only when the teaching is substantial, self-contained,
   and currently has no home (then wire it into `map.md` + 2-4 neighbor pages).
5. **Verify mechanically** (the atlas's own invariants):
   ```
   cd public-atlas && FILES="<changed files>"
   grep -nP "[^\x00-\x7F]" $FILES        # non-ASCII: must be empty
   grep -nF "[[" $FILES                  # wikilink leak: must be empty
   grep -nE "\b(S[0-9]+|Source Posture|Source Trail|load_when|best_linked_pages)\b" $FILES
   # plus: confirm every ](file.md) target exists, and any new page is in map.md
   ```
6. **Update this handoff** and the `ATLAS - Editorial Plan.md` execution state.
   Do NOT declare the information-value axis complete.

## Hard constraints (the register is the product too)

- Pure **ASCII** only (em-dash -> " - ", straight quotes). The audit scans this.
- **Relative markdown links** `[Text](file.md)`, never Obsidian `[[wikilinks]]`.
- **No internal machinery in public pages**: no claim IDs (S1/S2), no tier
  stamps ("compiled synthesis"/"Source Posture"/"Source Trail"), no frontmatter
  audit fields, no compiler metaphor.
- **Preserve Shinzen idiolect verbatim** - the idiolect is the transmission;
  generic-Buddhism paraphrase is the leak. (CCE; See/Hear/Feel; Flow; Gone;
  Rest; complete experience; Source; Zero; "today's enlightenment is tomorrow's
  mistake"; etc.)
- **Calibration must survive** - every recovered teaching keeps its boundary.
  No overclaim, no devotional drift, no state-glorification. The behavior/service
  test is the spine of trust.
- Lead with the live thing; define forward not by negation; no template tyranny;
  trim to register, not to a word count.
- The editorial plan's confirmed decisions still hold (10 pillars; practice
  pages standalone; teacher/lineage is an appendix).

## Done last round (2026-06-05, round 5 - serious illness / healing, reader-probe)

Switched probe direction per the round-5 plan - brought a reader's hard
question instead of grepping the menu. Probe 1 (serious diagnosis: what do I
do, and what should I not expect?) failed at compiler resolution: the atlas
held serious illness as one boundary row plus a severe-Wall pointer, and a grep
across all 90 pages for the router language (suffering reduction, objective
healing, non-consensual retreat) came back empty - the whole "what should I not
expect" half was missing. The teaching is substantial (three cancer/healing
parts + the sickness talk), self-contained, and homeless, so it earned a new
page - the same bar primal-feel met in round 3:
- new `serious-illness-and-healing.md` - the two-aim router (objective healing
  vs suffering reduction; suffering reduction is Shinzen's default *because* it
  pays out even if the disease course does not change - "your physical
  discomfort does not go away, but your suffering can"). That router IS the
  answer to "what should I not expect": not a cure, not a substitute for
  treatment. Plus the "non-consensual retreat" reframe with its anti-austerity
  correction (rest, sleep, breaks, care are method, not failure); the
  sensory-challenge decomposition (local/global physical, emotional body,
  image, talk); turn-away with background permission and the ten-minute floor;
  trained turn-toward (divide-and-conquer: fused multiplies, separated adds,
  equanimity drains resistance - "the miracle of mindfulness"); and the "no
  place to turn" safeguard. Calibration kept: no cure-promise, no patient-blame
  (the mind-body link is conditional only), suffering reduction never displaces
  oncology or pain relief, objective-healing imagery is optional and unproven,
  the numbers are a teaching device not measurement.
- Wired into `map.md` (problem-row + Safety section) and four neighbors
  (applied-life-boundaries pointer + Go Deeper, windows-and-walls
  severe-illness row, and turn-toward / physical-senses /
  condition-independent-happiness Go Deeper). Mechanical checks clean on all
  changed files (non-ASCII / wikilink / claim-ID / tier-stamp / link
  resolution; new page registered in the map). Pre-existing wart noted, not
  fixed this round: a `## Source Trail` heading still sits in
  `windows-and-walls.md` (predates round 5).

## Prior rounds

### Round 4 (ox-herding depth pass)

Took the recommended steer (re-ran the probe first to confirm it - the gap was
real). `surface-to-source-path-map.md` carried the Ten Ox-Herding Pictures as a
5-row table that collapsed the distinctions the compiler keeps, so a first taste
read as arrival, surrender read as "relaxing," and the final triad read as one
ending. Enriched the existing parallel in place - no new page (near-zero bloat):
- `surface-to-source-path-map.md` - the parallel now keeps all ten pictures as
  three distinct movements. Opening four held apart (searching -> footprints =
  inspiration -> glimpse = "a little vipassana" -> catching = first no-self /
  stream-entry / kensho, ox still wild) so a first taste is not mistaken for
  arrival (the front-end-is-not-one-attainment point the compiler is explicit
  about). Middle three turn on surrender proper: riding-the-ox-backward = giving
  up the need for orientation, faith as releasing the demand to know where
  experience is going (not "relaxing"), kept distinct from taming
  (stabilization) and coming-home (repose). Final triad split into no substance
  / ordinary appearance (mountains, cherry blossoms) / marketplace service, with
  service as the final cause (one's Source is everyone's Source) so the map
  cannot end at private emptiness. Calibration kept: diagnostic not
  status-ladder; riding backward needs CCE + functioning + support or it becomes
  passivity / dissociation / fatalism; marketplace "teaching" is not
  self-certifying (readiness, consent, feedback, anti-dependency are separate);
  map stays provisional, not a final taxonomy or verified history.
- No map.md change needed (page already routed from the cross-tradition path,
  the Transformation section, and a problem row). Mechanical checks clean
  (non-ASCII / wikilink / claim-ID / tier-stamp / link resolution).

### Round 3 (primal Feel)

Closed the hot-stratum gap a deep practitioner is most likely to misread.
Probe: "primordial Feel" appeared once, in a list, in
`altered-phenomena-and-dissolution-safety.md` and was taught nowhere (the
applied-life "hit" was a false positive on "infant care"). Substantial,
self-contained, genuinely homeless (distinct from bhanga = breakup of order,
and from DPDR/pit = the *cold* void), so it earned a new page:
- new `primal-feel.md` - hot, chaotic, infant-like body emotion ("pure heat
  of Feel") beneath emptiness; the recognition tell (big provocations stop
  landing while a tiny trigger detonates = the floor becoming visible); the
  strata mechanism (a layer integrates -> its grip shrinks -> a more primitive
  stratum is exposed, so local weirdness != global decline); the live router
  (correlation check -> dominant channel -> include Feel-vanishings in Gone ->
  recycle the reaction -> manageable doses + reconstruction); terror-as-Flow
  with the non-imitation boundary; the compassion face; the hot-vs-cold
  differential against DPDR. Calibration kept: infant-origin / cosmic-parents
  / Zero-polarity frame is Shinzen's teaching image, not developmental
  psychology, neuroscience, or a clinical reparenting protocol.
- Wired into `map.md` (problem-row + Phenomenology) and six neighbors (the
  impermanence pillar gained a parallel "vanishing turns hot" routing row;
  altered-phenomena's bare list-mention became a real pointer). Mechanical
  checks clean.

### Round 2 (transformation-mechanism)

Closed the causal core a serious practitioner most wants - *why* CCE-over-time
transforms anything, and *why* the practice has the form it does - at compiler
resolution, register-protected and mechanically verified. Enriched existing
pages (no new page; lower bloat risk):
- `insight-and-purification.md` - delivered the mechanism the formula was
  missing: suffering as a multiplying tangle of body/image/talk; sensory
  clarity as discriminate + detect; "trackable implies tractable"; insight =
  the seeing half, purification = the releasing half; named the Fundamental
  Theorem ([[Science of Enlightenment Chapter 5 - Insight and Purification]]).
  Added the motivation model on the same page: taste of purification ->
  positive feedback loop + hockey-stick non-linearity, held with its
  shape-not-schedule / not-universal boundary ([[The Hockey Stick Metaphor and
  Exponential Growth on the Spiritual Path]]). Cut two now-redundant vague
  lines as the mechanism replaced them.
- `equanimity.md` - how equanimity is *learned*: the body-level feedback loop
  (interference = suffering, noninterference = relief), the trained behavior is
  noninterference, Skinnerian / "reptilian brain" bounded as teaching device,
  not neuroscience, never self-punishment ([[The Reptilian Brain, Skinnerian
  Training & the Experience of God]]).
- `practice-cycles-and-life-architecture.md` - why formal sits and retreats
  earn their place: environmental simplification gives that feedback clean,
  immediate signal; retreat = the same laboratory enlarged, not endurance;
  intensity/isolation/hours are not the active ingredient.
- Cross-wired insight-and-purification <-> equanimity <-> practice-cycles.

Prior round (2026-06-05, round 1) closed: source-service love map, focus-on-rest
six rest flavors, self-inquiry non-dual / no-place-to-stand, and the new
good-place-traps page.

## Next round - probe from the reader, not the menu

Four rounds closed single compiler concepts the atlas was missing (supply-side
probe: grep the atlas for a compiler term, find it thin, port it). That vein is
thinning, and it never measured the delta - every steer, including the last one,
was a prior. So switch probe direction. Probe from the reader: take a hard
question a serious practitioner would actually bring, try to answer it at
compiler resolution using ONLY the public atlas, and close the first place the
atlas cannot carry the answer. A reader-probe can only be satisfied by depth, so
it cannot be gamed by adding pages or routes - this also kills the old
breadth-vs-depth confusion at the root.

**Ship-first rule.** Run the probes in order; the FIRST that exposes a
compiler-resolution gap, close it THIS round (enrich-in-place by default). Close
one, log the rest, ship. Do not run all five then plan - that is the documented
over-planning failure.

**Round-5 probe set** (1-3 aim at the regions still suspected thin; 4-5 are
differentials that single-concept porting cannot have fixed):
1. [CLOSED round 5 -> `serious-illness-and-healing.md`] Cancer / serious-illness
   diagnosis: what exactly do I do, and what should I not expect?
   (applied-life: healing-vs-suffering-reduction default; Gate 9)
2. Powers / siddhis / intermediate-realm phenomena are showing up: the practice
   read without status or woo. (port the handle + boundary, NOT the metaphysics;
   the compiler holds this mostly speculative)
3. In labor, or sleep-wrecked with a newborn: how do I actually practice?
   (applied-life: birth / sleep; Gate 9)
4. Body buzzing / dissolving: how do I tell Flow vs vibration vs bhanga vs
   primal Feel apart, and does the difference change what I do? (a differential
   living BETWEEN flow-and-gone, dissolution-and-bhanga, primal-feel,
   altered-phenomena)
5. How do I tell genuine no-self / equanimity from dissociation or DPDR in my
   own case? (a differential between no-self, equanimity-vs-suppression, dpdr)

The differentials are the likely high-value residual now: after four rounds of
porting single concepts onto single pages, the pages may be individually deep
but not COMPOSE into the either/or answer a practitioner actually needs, and a
concept-grep cannot see that. (Transferable move: once the single concepts are
in, value migrates to the differentials between them - probe the reader's "is
this X or Y, and what do I do differently?")

**Coverage ledger** - append one line per probe run (probe -> verdict
present/thin/absent -> action). This inline ledger IS the delta measurement; do
NOT spawn a separate audit doc.
- round 5: probe 1 (serious diagnosis - what do I do / not expect) -> ABSENT
  (router language empty across all 90 pages; the "what not to expect" half
  missing entirely) -> closed with new `serious-illness-and-healing.md`. Probes
  2-5 logged, not run (ship-first rule).
- round 6: (fill in) - resume at probe 2 (powers/siddhis), then 3 (labor/
  newborn sleep), then the differentials 4-5 (still the suspected high-value
  residual).

Already closed (quick history; full per-round detail in `ATLAS - Editorial
Plan.md` section 11): round 2 = CCE+time -> insight+purification mechanism
["trackable implies tractable"] + "why formal practice works" + taste-of-
purification motivation; round 3 = primal/primordial Feel hot stratum
(`primal-feel.md`); round 4 = Ten Ox-Herding depth collapse (enriched
`surface-to-source-path-map.md` to ten pictures in three movements). Lower
priority unless you judge it higher-value than depth: publication-readiness
(citation/rights, static-site prep).

## Failure modes to avoid

- Declaring the axis "complete" / grading your own homework. The human re-issued
  the goal once already because of exactly this. The dual failure is the
  unfalsifiable forever-loop ("never complete," no stop). Honest terminus test:
  when two consecutive probe batches (>=5 reader-probes each, including fresh
  differentials) find ZERO compiler-resolution gaps, say so - "near-complete by
  reader-probe; remaining work is maintenance, not delta" - and stop opening
  rounds. Terminus is earned by probe-misses, never self-graded.
- Writing another audit/plan doc *instead of* shipping atlas changes. The repo
  is over-planned; the deliverable is the atlas.
- Breadth-thinking (counting pages/routes) instead of depth (claims/distinctions).
- Damaging the register to add content (re-bloating with caveats/meta).
- Porting a compiler claim without its calibration boundary.
