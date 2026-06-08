# Shinzen Compiler Wiki Audit

## Scope note

I audited the bundle as an agent-maintained working-memory system. I treated the compiled wiki as the primary reasoning layer, and checked raw-to-compiled fidelity only for the four included raw/source-page pairs. I did **not** assume missing raw sources are available.

Overall verdict: **the operating contract is unusually coherent, and the sampled source pages are high-fidelity, but the system is starting to fail its own “fewest useful tokens” invariant.** The main debt is not bad content; it is router bloat, oversized synthesis/owner pages, permissive lint thresholds, and safety/accountability criteria that are visible but not yet executable enough.

---

## Top 10 audit findings, ordered by impact

### 1. `wiki/index.md` is no longer a lean first-read router

The contract says startup should read the index opening through `Open Questions`, not the whole index (`AGENTS.md:41-45`; `wiki/_operations.md:12-13`). The shape file says the opening shape paragraph should be a first routing surface in “three to five sentences” (`wiki/_shape.md:3-5`). The index itself even says it “should stay a skim surface” (`wiki/index.md:9-14`).

But the actual index forces a future agent through a long status narrative before the routing surface stabilizes: the gate chronology starts at `wiki/index.md:41`, `Recent Shape Changes` only appears at line 186, `Operating Dashboard` at line 206, and `Open Questions` at line 222. Then the `Sources` domain alone runs from line 254 to the next domain at line 926, and safety does not begin until line 1203 (`wiki/index.md:254-260`; `wiki/index.md:900-926`; `wiki/index.md:1203-1220`).

**Impact:** every future task pays a large token tax before it reaches the right page. This is the biggest obstacle to calibrated practice judgment per token.

**Fix:** split the index into a short “Start Here” router plus catalog surfaces. Move detailed gate chronology to a status page or log-derived page. Move the long source list to `Sources Catalog` or `_indexes/sources.md`.

### 2. `Current Model.md` is valuable, but too bloated to serve as the default compression layer

`Current Model.md` has the right ingredients: strong key points, practice routing, confidence tiers, and explicit frontiers. The problem is density and role overload. Its thesis is already a whole-system paragraph in frontmatter (`wiki/Current Model.md:1-12`). The “Self, Source, and enlightenment” landscape bullet becomes a very long multi-source synthesis (`wiki/Current Model.md:32`). Gate 6A then repeats a large operational-enlightenment summary in one paragraph (`wiki/Current Model.md:142`). The best agent-facing material is later: practice routing at `wiki/Current Model.md:158-171` and confidence tiers at `wiki/Current Model.md:175-179`.

**Impact:** future agents are likely to load a 5,000-word page when they need a 700- to 1,000-word operating card. That encourages over-reading and makes it harder to distinguish core model, evidence map, and current ingestion chronology.

**Fix:** create either a top-level `## Current Model Card` capped to one screen, or split into:

- `Current Model.md` — short operating model and routing card.
- `Current Model - Evidence and Gate Deltas.md` — detailed gate chronology and source-support map.

### 3. The 77-source canonical backlog is the biggest evidence-posture risk

Lint reports 212 compiled pages and 225 checked raw sources, but also 77 canonical raw sources without source pages (`lint-output-2026-05-12.txt:1-4`). The index dashboard names the same backlog and lists the unresolved clusters: practice-selection/dosage, teacher competence, clinical/medical boundaries, behavior verification, turn-toward/turn-away stop criteria, altered-phenomena differentials, no-self/Gone/dissolution support, purification/intensity criteria, power-service ethics, teaching-transmission routing, and future neurotechnology evidence (`wiki/index.md:208-220`).

**Impact:** the compiled model may look mature while high-risk source territory remains uncompiled. A future agent could over-trust synthesis pages because the backlog is visible but not prioritized by risk.

**Fix:** create a backlog triage page sorted by **practice-reasoning value and safety risk**, not ingest order. The next source should be chosen by whether it changes live guidance, safety calibration, teacher/accountability boundaries, or source-use tiers.

### 4. Frontmatter is becoming a hidden evidence map instead of a triage card

The templates say `load_when` should be one discriminating sentence, target 160–320 characters; `best_linked_pages` should usually list 3–8 strongest next loads; non-source `sources` should keep only principal raw anchors (`wiki/_templates.md:14-21`). But lint only warns at much looser thresholds: `load_when > 500`, `best_linked_pages > 12`, non-source `sources > 24` (`tools/wiki_lint.py:98-106`).

Lint catches the most extreme source-list cases: `Equanimity`, `Flow`, `No-Self And Personality`, `Sensory Clarity`, `Source And Polarities`, and `Total Happiness` each have 25–37 raw paths in frontmatter (`lint-output-2026-05-12.txt:5-10`). But other pages have already drifted without being flagged. For example, `Basic Mindfulness Practice Architecture` has a very long source list, long `load_when`, and 11 best links (`wiki/Basic Mindfulness Practice Architecture.md:10-12`). The SHF Unit 08 source page has a 479-character `load_when`, just under the current lint warning despite being well above the template target (`wiki/See Hear Feel Introduction - Practice Organization and System Transition.md:10-12`).

**Impact:** future agents cannot trust frontmatter as cheap routing. They must read body cards anyway, defeating the whole schema.

**Fix:** lower lint warning thresholds to match the contract: warn at `load_when > 320`, `best_linked_pages > 8`, non-source `sources > 8`, and issue stronger diagnostics at the existing larger thresholds.

### 5. Safety is visible and sophisticated, but not yet executable enough

The safety hub is strong. It routes to focused child pages for bypass, method safety, intensity/embodiment, altered phenomena, DPDR, guidance/accountability, and operational enlightenment (`wiki/Complete Experience Safety Boundary.md:24-31`). It gives cross-cutting clarity, equanimity, embodiment, behavior, and support tests (`wiki/Complete Experience Safety Boundary.md:33-46`).

But the same page admits that the wiki still lacks operational stop rules for pain, strong determination, kriyas, bhanga, dark-night reactions, DPDR, depression, anxiety, medication/substance effects, mania/psychosis risk, medical pain, retreat aftershock, teacher competence, referral, and behavior verification (`wiki/Complete Experience Safety Boundary.md:48-53`). `Practice Guidance Toolkit` has useful safety gates (`wiki/Practice Guidance Toolkit.md:97-107`), but those gates should be made impossible to miss from the index and current model.

**Impact:** the system can say “route to safety,” but a future agent may still lack a compact red/yellow/green decision matrix for live guidance.

**Fix:** promote a `Safety Decision Matrix` into `Complete Experience Safety Boundary`, `Practice Guidance Toolkit`, and the index opening. It should separate emergency/ordinary-support routing, meditation-optimization routing, and source-level uncertainty.

### 6. The four sampled source pages show strong fidelity, but workflow drift appears in integration notes

The good news: the sampled source pages preserve teaching moves, practice handles, weak claims, omissions, and tensions well.

- `Science of Enlightenment Chapter 5 - Insight and Purification` accurately preserves the CCE-plus-time theorem, purification model, therapy boundary, and science-rhetoric caution (`wiki/Science of Enlightenment Chapter 5 - Insight and Purification.md:26-41`; raw formula at `raw/Shinzen Sources/science-of-enlightenment/05-insight-and-purification.md:139-141`; therapy boundary at `raw/.../05-insight-and-purification.md:169`; science rhetoric at `raw/.../05-insight-and-purification.md:201-203`).
- `Basic Mindfulness Chapter 12 - The Big Picture` correctly marks the visual sutra, guidance toolkit, turn-toward/turn-away strategy families, speculative science-spirituality frame, and layout-loss caveat (`wiki/Basic Mindfulness Chapter 12 - The Big Picture.md:26-41`; `wiki/Basic Mindfulness Chapter 12 - The Big Picture.md:62-80`; raw toolkit at `raw/Shinzen Sources/five-ways/12-big-picture.md:723-760`; raw uncertainty at `raw/.../12-big-picture.md:1235-1240`).
- `See Hear Feel Introduction - Practice Organization and System Transition` accurately preserves practice rhythm, retreat/coach claims, method-choice principles, old/new interface transition, optional Gone, and unchanged Do Nothing (`wiki/See Hear Feel Introduction - Practice Organization and System Transition.md:26-38`; raw support at `raw/Shinzen Sources/see-hear-feel-introduction/08-practice-organization-and-system-transition.md:21-45`).
- `A Mindfulness Path Arising Between Empowering Contrasts` is a model YouTube source page: it preserves the racy/spacey label switch, “medicine wrong place” warning, lute-tuning metaphor, practice handles, and misuse risks (`wiki/A Mindfulness Path Arising Between Empowering Contrasts.md:45-84`; `wiki/A Mindfulness Path Arising Between Empowering Contrasts.md:132-166`; raw support at `raw/Shinzen Sources/yt transcripts/A Mindfulness Path Arising Between Empowering Contrasts ~ Shinzen Young_ncGiwqCZ7rg.md:11-89`).

The problem is workflow drift: source pages sometimes retain “Integration target” language after the integration has already happened. The template explicitly distinguishes future `Integration target` from completed `Integration Notes` so finished source pages do not read like open todo lists (`wiki/_templates.md:24-28`). But the Chapter 5 page still says the safety boundary “should now include” the therapy/12-step/social-feedback boundary while Integration Notes say the safety boundary and index were already updated (`wiki/Science of Enlightenment Chapter 5 - Insight and Purification.md:57-63`; `wiki/Science of Enlightenment Chapter 5 - Insight and Purification.md:85-90`).

**Impact:** future agents may waste review effort redoing completed integration or misunderstand the page’s freshness.

**Fix:** add lint for stale `Integration target` language when `Integration Notes` already lists pages updated.

### 7. Domain scaling has crossed the threshold where flat domain sections are harmful

The operations manual says that at 200–500 pages, domain syntheses or catalog surfaces should carry full page lists; the main index should route to them and keep only highest-value entries (`wiki/_operations.md:305-313`). Lint says the wiki has large domains: `practice` 91 pages, `primary` 94, `safety` 38, `sources` 148, and `transformation` 52 (`lint-output-2026-05-12.txt:11-15`).

**Impact:** the index is doing catalog work and router work at the same time. That hides the high-value next loads inside a long list of valid but non-startup entries.

**Fix:** create sub-indexes or catalog surfaces:

- `Sources Catalog`
- `Practice Architecture Index`
- `Practice Routes Index`
- `Transformation Mechanisms Index`
- `Safety Frontiers Index`
- `Teaching and Service Index`

The main index should link to these and keep only the top few decision surfaces.

### 8. High-value synthesis pages are mostly well-calibrated, but they are becoming mini-books

Several owner pages have excellent source posture but are too large for routing:

- `Source And Polarities` correctly says Source/Zero/polarity language is strong as Shinzen’s interpretive frame and speculative as objective reality (`wiki/Source And Polarities.md:16-22`), and it preserves the crucial afterglow boundary that Source/Zero is not directly experienced as an object (`wiki/Source And Polarities.md:210-212`). But it is large, has 37 raw sources in frontmatter, and covers practice, metaphysics, science analogy, bhanga, service, and comparative language.
- `Total Happiness` clearly marks its universal-happiness theory as Shinzen’s aim structure, not established universal theory (`wiki/Total Happiness.md:18-22`), and its boundaries are unusually strong (`wiki/Total Happiness.md:300-365`). But it has 26 sources in frontmatter and bundles aim structure, service, behavior verification, teaching, Source service, and ordinary/deep happiness.
- `Complete Experience` has safety-critical boundaries buried deep in the page (`wiki/Complete Experience.md:220-344`).
- `Operational Enlightenment` has an excellent anti-overclaim posture but compresses many safety/ethics/clinical/teacher-boundary claims into very long bullets (`wiki/Operational Enlightenment.md:18-22`).

**Impact:** the pages are trustworthy once loaded, but they are expensive and hard to partially load. Future agents may skip them or overconsume them.

**Fix:** preserve the owner pages, but add short cards and split the buried decision criteria into focused pages.

### 9. `Practice Guidance Toolkit` is the best live-practice router and should be promoted

This page already defines itself as the “agent-facing decision surface” (`wiki/Practice Guidance Toolkit.md:1-3`). It has an excellent use contract: context, branch, quality, and loop (`wiki/Practice Guidance Toolkit.md:24-32`). Its fast routing algorithm is exactly what future agents need for live reports (`wiki/Practice Guidance Toolkit.md:45-50`), and its safety gates are concrete enough to operationalize (`wiki/Practice Guidance Toolkit.md:97-107`).

**Impact:** this page should often be loaded before `Current Model` when the task is “what should this practitioner do?” Right now it is listed in the index opening, but it does not have “primary live guidance router” status.

**Fix:** add an index-start rule:

> Live practitioner report → load `Practice Guidance Toolkit` first; if any red flag → load `Complete Experience Safety Boundary` before technique optimization.

### 10. Behavior verification and teacher/accountability boundaries are present but fragmented

The system repeatedly recognizes that practice claims need behavior and service verification. `Current Model` asks for behavior commitment, relationship repair, service action, support checks, or ordinary practical steps as the life test (`wiki/Current Model.md:171`). It names service and teaching verification as unresolved (`wiki/Current Model.md:188`). `Total Happiness` says behavior verification is still needed because a practitioner can feel improved while behavior remains unchanged (`wiki/Total Happiness.md:343-353`). The safety hub routes teacher competence, referral, crisis language, power-service ethics, and accountability to `Guidance Scope and Accountability Boundary` (`wiki/Complete Experience Safety Boundary.md:30`).

**Impact:** these concerns are exactly where future agents are most likely to overclaim: “practice helped,” “service follows,” “teacher is qualified,” “insight improved conduct.” The wiki knows this, but the verification layer is not yet a single strong decision surface.

**Fix:** create or promote a dedicated page such as `Behavior Verification and Teacher Accountability`. It should own observable conduct, feedback loops, repair, consent, role clarity, referral, supervision, and anti-dependency.

---

## Specific optimization recommendations

### Optimize for routing surfaces, not more synthesis prose

The operating contract is already correct: maximize practice-reasoning quality and fidelity per token (`AGENTS.md:11-18`). The next optimization should be **token discipline**:

1. A short index opening.
2. A short current-model card.
3. A live-practice router.
4. A safety matrix.
5. Domain catalogs outside the main index.
6. Source pages that preserve fidelity but do not keep stale integration tasks.

### Make the system answer “what do I load next?” in one screen

| Task type | First load | Second load |
|---|---|---|
| Whole-system orientation | `Current Model Card` | detailed `Current Model` only if needed |
| Live practice report | `Practice Guidance Toolkit` | `Turn Toward and Turn Away`, `Practice Entry and Method Choice`, or safety hub |
| Safety/destabilization | `Complete Experience Safety Boundary` | relevant child page |
| Source-level evidence | `Sources Catalog` or exact source page | raw source only if fidelity/provenance needed |
| Source/Zero/metaphysics | `Source And Polarities` card | detailed split pages |
| Teacher/service/behavior | `Behavior Verification and Teacher Accountability` | `Teaching A Path`, `Operational Enlightenment`, `Total Happiness` |

### Treat mechanical lint pass as necessary but insufficient

The current lint passes mechanically while diagnostics already show structural debt. Lint should start surfacing semantic router failures: page size, index bloat, stale integration targets, source posture gaps, safety visibility, and unresolved claim-ID checks.

---

## Suggested file/page changes

### Quick wins

1. **Trim `wiki/index.md` opening.** Keep scope, current through-line, current counts, highest-leverage next step, and 4–6 task routes. Move lines 41–184 of gate chronology into a status page or log-derived page.

2. **Move the long Sources domain out of the main index.** Keep only a short `Sources` summary and link to `Sources Catalog`.

3. **Promote `Practice Guidance Toolkit` in the index opening.** Mark it as the first page for live practitioner reports.

4. **Promote `Complete Experience Safety Boundary` in the index opening.** Add a rule that safety gates override technique optimization.

5. **Compress frontmatter on flagged owner pages.** Start with `Source And Polarities`, `Total Happiness`, `Equanimity`, `Flow`, `No-Self And Personality`, and `Sensory Clarity`, because lint already flags them for oversized `sources` lists.

6. **Shorten near-threshold `load_when` fields.** `See Hear Feel Introduction - Practice Organization and System Transition`, `Basic Mindfulness Practice Architecture`, `Turn Toward and Turn Away`, and `Total Happiness` all read more like micro-manifests than triage cues.

7. **Clean stale `Integration target` language.** When Integration Notes already list the update, change “should now include” to “Integrated into.”

8. **Add a small “Source backlog by risk” table to the dashboard.** Categories: safety/clinical, teacher/accountability, practice routing/dosage, altered phenomena, Source/metaphysics, service/behavior, future science.

### Medium refactors

1. **Create `Current Model Card`.** Either as the top section of `Current Model.md` or a separate page. Cap it strictly.

2. **Create `Sources Catalog`.** Move the full source-page list there. Main index keeps only source-domain routers and high-value source anchors.

3. **Refactor `Practice Entry and Method Choice`.** Its provisional routing checklist is useful (`wiki/Practice Entry and Method Choice.md:92-120`), but should become a compact decision table. Keep the detailed Gate 1 evidence map separately.

4. **Split `Complete Experience`.** Suggested split:
   - `Complete Experience` — core mechanism.
   - `Complete Experience Diagnostics` — CCE, critical mass, one taste, transformation criteria.
   - `Complete Experience Failure Modes` — bypass, intensity, pain, dissociation, medical neglect, behavior non-improvement.

5. **Split `Source And Polarities`.** Suggested split:
   - `Source Afterglow Boundary`
   - `Expansion-Contraction Practice`
   - `Gone and Source Contact`
   - `Bhanga and Dissolution Boundary`
   - `Science/Mathematics Speculation Boundary`

6. **Split or sub-index `Total Happiness`.** Suggested split:
   - `Total Happiness Aim Structure`
   - `Behavior Verification`
   - `Service and Teaching Boundary`
   - `Ordinary and Extraordinary Happiness`

7. **Promote `Guidance Scope and Accountability Boundary`.** It is named as a safety child page, but the bundle suggests its concerns are central enough to be a first-tier router.

### Major refactors

1. **Rebuild the main index according to the 200–500 page scaling rule.** The index should route to catalogs, not carry catalogs itself.

2. **Implement semantic lint.** Add body size, index size, stale integration, source posture, safety visibility, and unresolved claim-ID checks.

3. **Backlog triage pass.** Re-rank the 77 uncompiled canonical raw sources by practice-routing impact and safety/accountability risk.

4. **Build a query-simulation benchmark.** Use 8–12 representative questions and measure how many pages/tokens a future agent must load before a calibrated answer is possible.

---

## Missing review criteria and lint checks to add

### Add to `AGENTS.md`

- **Startup budget rule:** index opening through Open Questions should stay below a fixed line/token budget. If it exceeds the budget, treat it as routing debt.
- **Live-practice rule:** for concrete practitioner reports, load `Practice Guidance Toolkit` before whole-system synthesis unless the query is purely theoretical.
- **Safety override rule:** if medical, clinical, dissociation, coercion, abuse, teacher-pressure, or repeated-worsening signals appear, route through the safety hub before technique optimization.
- **Behavior verification rule:** claims of insight, service, teacher competence, or transformation need observable behavior/support criteria, not only internal reports.
- **Backlog humility rule:** current synthesis must not imply full coverage when canonical raw sources remain uncompiled in high-risk domains.

### Add to `wiki/_operations.md`

- **Router audit workflow:** simulate common queries and record pages loaded before an answer.
- **Index health metric:** warn when index opening through Open Questions exceeds 80–100 lines.
- **Catalog delegation rule:** when a domain exceeds 30–50 entries, move the full list to a catalog page and keep the main index selective.
- **Stale integration cleanup step:** after ingest, remove future-tense integration targets that were completed.
- **Backlog triage cadence:** every review pass should rank uncompiled canonical sources by safety/practice impact.
- **Frontmatter refactor pass:** when `load_when`, `best_linked_pages`, or `sources` become exhaustive, move detail to body/source anchors.

### Add to `wiki/_templates.md`

- Add optional `## Load Path` and `## Do Not Load For` sections for high-importance router pages.
- Add `## Evidence Posture` tables for synthesis/concept pages with many sources: established, probable synthesis, source-attributed, speculative, unresolved safety.
- Add `## Easily Misused Claims` not only for YouTube lecture pages but for any source involving pain, death, strong determination, Source, no-self, powers, teacher authority, service, or clinical-neighbor material.
- Add a diagram/layout caveat field for source pages where raw conversion loses visual structure.
- Add a template instruction: when `Integration Notes` are completed, do not leave `Integration target` phrased as an open action.

### Add to `tools/wiki_lint.py`

Highest-value additions:

1. Warn at `load_when > 320`; strong warning at `> 500`.
2. Warn at `best_linked_pages > 8`; strong warning at `> 12`.
3. Warn at non-source `sources > 8`; strong warning at `> 24`.
4. Warn when concept/synthesis/analysis pages exceed 1,500 words; strong warning above 3,000; urgent above 5,000 unless allowlisted.
5. Warn when `wiki/index.md` exceeds budget, when Open Questions appears too late, or when a domain list dominates the index.
6. Detect stale `Integration target` plus completed `Integration Notes`.
7. Detect unresolved source claim references like `S7` where the cited source page lacks `**S7**`.
8. Detect pages with safety-risk keywords but no link to a relevant safety boundary.
9. Detect duplicate `Dependencies`/`Related` links.
10. Detect frontmatter `load_when` with too many comma-separated clauses or “or” branches.
11. Require YouTube source pages to include Teaching Register, Load-Bearing Teaching Moves, Practice Handles, and Easily Misused Claims.
12. Check local wiki path references inside backticks when they look like required system pages.

---

## Pages most deserving action

### Split or compress first

1. `wiki/index.md` — highest-impact router debt.
2. `wiki/Current Model.md` — compress into a current-model card plus detailed evidence page.
3. `wiki/Source And Polarities.md` — split Source/Zero, Gone, Expansion-Contraction, bhanga/dissolution, science-speculation, service.
4. `wiki/Total Happiness.md` — split aim structure, behavior verification, service/teaching boundary.
5. `wiki/Complete Experience.md` — split core mechanism from diagnostics and failure modes.
6. `wiki/Practice Entry and Method Choice.md` — convert checklist into compact router table.
7. `wiki/Operational Enlightenment.md` — separate identity-elasticity model from teacher/accountability and clinical-differential boundaries.

### Compress frontmatter

- `Equanimity`
- `Flow`
- `No-Self And Personality`
- `Sensory Clarity`
- `Source And Polarities`
- `Total Happiness`
- `Basic Mindfulness Practice Architecture`
- `See Hear Feel Introduction - Practice Organization and System Transition`
- `Turn Toward and Turn Away`

### Promote

- `Practice Guidance Toolkit`
- `Complete Experience Safety Boundary`
- `Turn Toward and Turn Away`
- `Guidance Scope and Accountability Boundary`
- `Teaching A Path`
- a new or promoted `Behavior Verification and Teacher Accountability`

### Strengthen source posture

- `Source And Polarities` — metaphysics/science/comparative-language posture.
- `Total Happiness` — universal happiness, behavior, service, teaching claims.
- `Operational Enlightenment` — enlightenment, DPDR, teacher qualification, map authority.
- `Complete Experience` — pain, illness, strong determination, trauma-adjacent practice.
- `Practice Guidance Toolkit` — professional-scope, consent, referral, privacy, teacher pressure.

---

## Concise next-best review pass plan

1. **Router simulation:** run 8 representative queries and record first page loaded, second page loaded, and where safety/source posture appears.
2. **Index surgery:** reduce `wiki/index.md` to a true first-read surface and move full source/domain lists to catalogs.
3. **Current Model card:** create a strict short version preserving practice routing, confidence tiers, and top safety frontiers.
4. **Safety matrix:** turn existing safety gates into red/yellow/green routing criteria.
5. **Frontmatter cleanup:** apply tighter thresholds to top 15 router/owner pages.
6. **Backlog triage:** rank the 77 uncompiled sources by risk and future practice-reasoning value.
7. **Semantic lint pass:** implement the small lint checks that prevent this same drift from recurring.

The wiki’s core contract is sound. The immediate problem is that the compiled layer is starting to behave like an archive again. The next best work is not more coverage; it is restoring fast, calibrated routing.
