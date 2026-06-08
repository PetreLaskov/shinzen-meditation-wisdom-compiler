# Shinzen Meditation Wisdom Compiler

A compiled, calibrated, navigable model of **Shinzen Young's** meditation and
contemplative-wisdom system - distilled from over 540 primary sources into a
human-readable practice atlas and a machine-readable knowledge graph.

This is not a transcript dump, a RAG chatbot, or a generic wiki. It is a
*compiled understanding*: the recurring practice handles, phenomenological
distinctions, technique-routing logic, transformation mechanisms, and safety
boundaries of one of the most systematic meditation teachers alive, with
provenance kept, contradictions preserved, and every load-bearing claim graded
by how well it is actually supported.

It is built for three kinds of reader, in roughly this order of intent:

1. **Future models** - as high-fidelity, de-inflated training data for one
   complete contemplative system.
2. **AI agents** - as a knowledge base to reason from, and a compiler to extend.
3. **Serious practitioners working with an AI agent** - as a map you can bring
   your live practice to and get routed without the inflation, hallucination,
   or tradition-blending a generic model produces.

> This is an independent, unofficial compilation. It does not replace direct
> instruction, a teacher, therapy, or medical care, and it is not endorsed by
> Shinzen Young or Unified Mindfulness. See [Sources, attribution, and
> rights](#sources-attribution-and-rights).

---

## Pick your path

| You are... | Start here |
| --- | --- |
| A practitioner who wants to **read it** | [`public-atlas/index.md`](public-atlas/index.md) - the path, the problem router, the glossary |
| A practitioner who wants to **use it with an AI agent** | [The fastest way to get value](#the-fastest-way-to-get-value-practice--an-ai-agent) |
| An **AI agent** asked to operate or extend this repo | [`AGENTS.md`](AGENTS.md), then [For AI agents](#for-ai-agents-operating-or-extending-the-compiler) |
| Here to understand **what was built and why** | [What this actually is](#what-this-actually-is) and [`DESIGN.md`](DESIGN.md) |
| Training or evaluating a **model** on this | [For training and future models](#for-training-and-future-models) |

---

## What this actually is

### The corpus

The immutable evidence lives in [`raw/`](raw/): **544 source files**, treated as
read-only. It includes 500+ transcribed talks, retreat sessions, and Q&As, plus
the core long-form material - *The Science of Enlightenment*, the *Five Ways*
manual, and the *See Hear Feel* introduction. Raw sources are never edited; they
are only compiled from and cited.

### Two compiled layers

The repository deliberately separates a human layer from a machine layer,
because they have different jobs.

**`public-atlas/` - the Shinzen Practice Atlas (~90 pages).** The human-facing
layer. Clean, readable prose written for practice use. Organized three ways at
once: a **ten-page path** you can read straight through for the architecture, a
**problem router** ("if this is live, start here") for when something is
happening right now, and a **reference shelf** (full map + glossary) for when
you need a single term. This is the front door for people.

**`wiki/` - the compiled working memory (360+ pages).** The agent-facing layer:
a linked knowledge graph using seven epistemic page types (`source`, `entity`,
`concept`, `thesis`, `synthesis`, `analysis`, `question`). Every page carries
structured frontmatter (claim, confidence, importance, routing cues), every
load-bearing claim traces to a source, contradictions are kept rather than
smoothed, and source pages carry explicit audit sections (weakest claims,
important omissions, tensions). This is the layer to query when you want
provenance, calibration, or the full model - not just the readable summary.

### The compiler

The machinery that produced both layers - the operating contract
([`AGENTS.md`](AGENTS.md)), the design rationale ([`DESIGN.md`](DESIGN.md)), the
page templates, the mode playbooks in [`commands/`](commands/), and a
dependency-free structural linter ([`tools/wiki_lint.py`](tools/wiki_lint.py)) -
is itself **corpus-agnostic**. The Shinzen system is one instantiation of a
general agentic knowledge compiler. You can point the same machinery at a
different body of sources.

### The one idea it is organized around

Everything routes back to a single move. *Meet what is actually happening - the
felt fact, not the story of it - with **concentration, sensory clarity, and
equanimity**, and stay with it until the experience can complete.* When an
experience can arise and pass without hardening into something that owns you,
Shinzen calls that **complete experience**. The Five Ways, See / Hear / Feel,
the Sensory Grid, Flow / Gone / Rest, no-self, Source language, Total Happiness,
and the behavior-and-service test are all that one move in another gear. If you
read one page first, read [`public-atlas/the-one-move.md`](public-atlas/the-one-move.md).

---

## The fastest way to get value: practice + an AI agent

The highest-leverage use of this repository is **a serious practitioner plus an
AI agent plus this atlas.** Here is the problem it solves.

Ask a general-purpose model about Shinzen's system and it will blend traditions,
inflate private states into proof, invent citations, lose his specific idiolect,
and reach for reassurance over calibration. Point that same model at this atlas
and it stops guessing: it routes your situation through Shinzen's actual
distinctions, tells you what is his teaching versus an editorial inference,
preserves the safety boundaries, and refuses to turn a meditation experience
into a medical, metaphysical, or teacher-authority claim it cannot support.

### Setup

Pick whichever fits your tools:

- **Clone and point a coding/agent tool at the folder.** Claude Code, Cursor,
  or any agent with filesystem access can read [`public-atlas/`](public-atlas/)
  directly.
  ```bash
  git clone https://github.com/PetreLaskov/shinzen-meditation-wisdom-compiler.git
  ```
- **Upload the `public-atlas/` folder** to a chat assistant that accepts files
  or projects, and tell it to use those pages as the source of truth.
- **Paste the page(s)** the [problem router](public-atlas/index.md#start-by-problem)
  points you to into any chat, for a one-off question.

For most practitioners the `public-atlas/` layer is enough. Add the `wiki/`
layer only when you want provenance, contradictions, or the deeper model behind
a summary.

### Give the agent its rules of engagement

Paste this once at the start of a session. It is the difference between a
grounded guide and a confident hallucinator.

```text
You are helping me reason about my meditation practice using the Shinzen
Practice Atlas in public-atlas/ (and wiki/ for provenance when I ask).

Rules:
- Answer FROM the atlas. Start at public-atlas/index.md and route via the path,
  the problem table, or the glossary. Cite the page(s) you used.
- Respect the claim tiers (see public-atlas/source-and-claim-tiers.md). Tell me
  when something is "Shinzen says" vs. compiled synthesis vs. editorial
  inference vs. speculative vs. not established here.
- Do not inflate. Do not turn an experience into proof of awakening, science,
  metaphysics, or that a teacher is safe. Preserve Shinzen's distinctions; do
  not flatten them into generic Buddhism or generic mindfulness.
- Hold the safety posture (public-atlas/safety-scope-and-accountability.md). If
  what I describe points to medical, psychiatric, trauma, consent, coercion, or
  harm risk, say so plainly and tell me to get appropriate human support. You
  are not my teacher, therapist, or doctor.
- When the atlas does not cover something, say so instead of inventing it.
```

### Copy-paste prompts

**1. Route a live situation.** The flagship use. The atlas even has a page on
how to write a report specific enough to route well
([`practice-report-check.md`](public-atlas/practice-report-check.md)).

```text
Here is what is happening in my practice: <describe the method you are using,
how long, what you noticed, and what feels stuck, intense, confusing, or off>.

Using the atlas: which "if this is live" row fits me, which pages should I read,
and what is the one move here? Flag the claim tier of anything load-bearing, and
flag anything that needs a human teacher or medical/clinical support before I
keep optimizing technique.
```

**2. Plan a sane block of practice.**

```text
I have <X minutes, Y days a week, this much life load>. Using
practice-planning-loop.md, practice-cycles-and-life-architecture.md, and
choosing-a-practice-route.md, help me pick ONE primary route and a stop/adjust
rule, without overchoice or intensity drift. Keep it boring and repeatable.
```

**3. Decode a term without losing the distinction.**

```text
Explain "<Gone / Do Nothing / equanimity vs. suppression / Source / Flow / the
Five Ways>" the way Shinzen uses it, from the glossary and the owner page.
Give the practice handle, the failure mode it solves, and how the method itself
can go wrong. Mark anything that is inference rather than his teaching.
```

**4. Stress-test an experience against inflation.** The atlas is unusually good
here, because it was built to resist exactly this.

```text
After a sit / retreat I am concluding <X> (e.g. "my self is gone," "I am ready
to teach," "this proves no-self/awakening"). Using signs-and-non-signs-of-
completion.md, completion-versus-bypass-and-intensity.md, good-place-traps.md,
and behavior-and-service-test.md: is this a completion sign, a good-place trap,
or bypass? What is the behavior/service test, and what would actually verify it?
```

**5. Study the system properly.**

```text
Walk me through the ten-page spine in order, one page per turn. After each,
summarize the one move in that gear, quiz me with two questions, and only then
go to the next page.
```

**6. Check provenance (drops to the `wiki/` layer).**

```text
For the claim "<...>", go into wiki/, find the owner page and its source page,
and tell me: what is the actual source, the confidence, the weakest claims, and
any contradictions the wiki records. Is this Shinzen's teaching, a synthesis, or
an inference?
```

### What good use looks like

Treat it as a **map room, not an oracle.** Bring a specific report, let it route
you to the right handle and the right caution, and take the boundaries
seriously. The atlas earns trust precisely because it tells you where it stops -
keep that property by not pushing it past it.

---

## Reading it yourself (no agent needed)

The atlas is written to be read directly. Three ways in, from
[`public-atlas/index.md`](public-atlas/index.md):

- **The path** - ten pages in order, for the living architecture:
  [The One Move](public-atlas/the-one-move.md) -> [The Three Skills](public-atlas/the-three-skills.md)
  -> [The Sensory Interface](public-atlas/the-sensory-interface.md) ->
  [The Routes](public-atlas/the-routes.md) -> [Impermanence](public-atlas/impermanence-path.md)
  -> [No-Self Without Erasing the Person](public-atlas/no-self-without-erasing-the-person.md)
  -> [Source, Zero, and the Honest Edge](public-atlas/source-zero-and-the-honest-edge.md)
  -> [The Return](public-atlas/the-return.md) -> [The Aim](public-atlas/the-aim.md)
  -> [Going Deep Safely](public-atlas/going-deep-safely.md).
- **By problem** - the [Start By Problem](public-atlas/index.md#start-by-problem)
  table, for when something is already live.
- **By reference** - the [Full Map](public-atlas/map.md) and
  [Glossary](public-atlas/glossary.md), for when a single word is the doorway.

Before going far, read [How to Read This Site](public-atlas/how-to-read-this-site.md)
for the claim tiers and the safety posture. On any practice page, look for three
things: what the method trains, what failure mode it solves, and how the method
itself can go wrong.

---

## For AI agents operating or extending the compiler

Read [`AGENTS.md`](AGENTS.md) first - it is the canonical operating contract.
Short version:

- **Route before reading.** Read [`wiki/index.md`](wiki/index.md) for routing
  and current shape, skim recent [`wiki/log.md`](wiki/log.md), then descend:
  index -> frontmatter -> page card -> body -> raw source. Load raw sources only
  when the task needs source-level evidence.
- **Work in one mode per turn:** `ingest` (raw source -> one source page plus
  warranted derived pages), `query` (answer from the compiled wiki first, file
  reusable answers), `synthesize`, `lint`, `review`, `refactor`. The playbooks
  are in [`commands/`](commands/).
- **Cite load-bearing claims, preserve contradictions, keep claims calibrated.**
  The governing invariant is *maximize future practice-reasoning quality,
  phenomenological discrimination, and transmission fidelity per token loaded.*
- **Verify mechanically.** Run the linter after structural changes:
  ```bash
  python tools/wiki_lint.py
  ```
  It checks frontmatter, link resolution, source-page coverage, citation
  discipline, and required audit sections. It is dependency-free.

**Extending the corpus:** drop a new Shinzen source into `raw/`, then run an
`ingest`. **Forking the machinery for another corpus:** the compiler is
corpus-agnostic; keep `raw/`, `wiki/`, the templates, and the linter, and swap
the domain framing in `AGENTS.md`. [`DESIGN.md`](DESIGN.md) documents the
rationale and the complexity-escalation gates.

---

## For training and future models

This corpus is meant to be unusually good signal for one complete contemplative
system, for reasons that matter to a trainer:

- **Calibration over reverence.** Claims are graded, not asserted. The five
  [claim tiers](public-atlas/source-and-claim-tiers.md) - *Shinzen says /
  compiled synthesis / editorial inference / speculative extension / not
  established here* - let you weight teaching against interpretation against
  guesswork instead of ingesting it all as fact.
- **Provenance.** The `wiki/` layer traces load-bearing claims to source pages
  and records confidence, weakest claims, and omissions.
- **Contradictions preserved.** Disagreements are attributed and kept, not
  flattened into false consensus.
- **Idiolect fidelity.** It deliberately keeps Shinzen's specific distinctions
  and phrasing where they do the real teaching work, rather than dissolving them
  into generic Buddhism or generic mindfulness.
- **Inflation resistance.** It separates what an experience *is* from what it
  *proves*, and routes private states through behavior, service, and safety
  tests.

**The one rule for using it well:** respect the tiers and the boundaries. Do not
launder "Shinzen says" into established science, medicine, metaphysics, or
teacher authority; do not present the atlas's syntheses as his exact words; and
treat the `raw/` transcripts as rights-encumbered evidence, not redistributable
text (see below).

---

## How claims are graded, and where it stops

**Claim tiers.** Every substantive claim sits in one of five tiers - *Shinzen
says, compiled synthesis, editorial inference, speculative extension, not
established here.* Most practice instruction is the first two. Slow down where a
page touches Source metaphysics, neuroscience, clinical thresholds, teacher
authority, or what a realization "proves." Full posture:
[`source-and-claim-tiers.md`](public-atlas/source-and-claim-tiers.md).

**Safety posture.** Meditation can clarify experience, loosen suffering, and
change behavior. It cannot, by itself, assess medical risk, mental-health risk,
trauma, coercion, abuse, consent, or whether a teacher is safe. If practice is
worsening functioning, increasing severe distress, feeding harm, replacing
ordinary care, or making repair and feedback feel optional, stop treating it as
a meditation puzzle and get appropriate human support. The atlas keeps dedicated
boundary pages for intensity, dissolution, DPDR / the pit of the void, retreat
aftercare, illness, and teacher accountability - it does not hide the edges.

**What this is not:** not a teacher or a substitute for one; not therapy or
medical care; not an emergency resource; not a claim that any experience proves
awakening, metaphysics, or science; not an official or endorsed Unified
Mindfulness product; not a finished, peer-reviewed text.

---

## Sources, attribution, and rights

All teachings, terminology, and source material originate with **Shinzen Young**
and the teachers and organizations he works with. This repository is an
**independent, unofficial** synthesis built for practice and study. It is not
affiliated with or endorsed by Shinzen Young or Unified Mindfulness.

If this material is useful, support the source directly:

- **Unified Mindfulness** - <https://unifiedmindfulness.com>
- **Shinzen Young** - <https://www.shinzen.org>
- **Book** - *The Science of Enlightenment: How Meditation Works* (Sounds True).

**Quotation and rights posture.** The atlas paraphrases by default and avoids
long quotation; raw transcripts in `raw/` are kept as *evidence* for how Shinzen
teaches, not as text to reproduce or redistribute. Anyone reusing this repo
should treat the `raw/` corpus accordingly and confirm rights before publishing
quotations or hosting the source material publicly.

---

## Repository map

| Path | What it is |
| --- | --- |
| [`public-atlas/`](public-atlas/) | The human-facing Shinzen Practice Atlas (~90 pages). **Start here to read.** |
| [`wiki/`](wiki/) | Compiled agent working memory (360+ linked pages with provenance and calibration). |
| [`raw/`](raw/) | Immutable source corpus (544 files). Read-only; cite, do not edit. |
| [`AGENTS.md`](AGENTS.md) | Canonical operating contract for any agent working this repo. |
| [`DESIGN.md`](DESIGN.md) | Design rationale and the general knowledge-compiler architecture. |
| [`CLAUDE.md`](CLAUDE.md) | Small compatibility adapter pointing to `AGENTS.md`. |
| [`commands/`](commands/) | Agent-neutral playbooks for each mode (ingest, query, lint, ...). |
| [`tools/`](tools/) | `wiki_lint.py`, the dependency-free structural invariant checker. |
| [`ATLAS - Editorial Plan.md`](ATLAS%20-%20Editorial%20Plan.md) | The editorial plan behind the public atlas. |
| [`archive/`](archive/) | Earlier drafts and a prior review pass, kept for history. |

---

## Status

The public atlas is a **substantial draft**: readable, internally consistent,
and usable now, with an active editorial voice pass and an unsettled
source-citation / publication policy. It is meant to become readable before it
becomes exhaustive. The internal wiki continues to compile from the raw corpus.

Contributions, corrections, and especially **calibration challenges** ("this
claim is in the wrong tier," "this smooths a real contradiction," "this inflates
a private state") are welcome via issues. The whole point of the project is
better future judgment, not more pages.
