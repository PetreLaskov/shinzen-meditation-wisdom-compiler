# Shinzen Meditation Wisdom Compiler

A compiled, calibrated, navigable model of **Shinzen Young's** meditation and
contemplative-wisdom system - distilled from more than 500 primary sources into
a sourced knowledge graph you put an AI agent in front of, with a human-readable
practice atlas for when you would rather just read.

This is not a transcript dump, a RAG chatbot, or a generic wiki. It is a
*compiled understanding*: the recurring practice handles, phenomenological
distinctions, technique-routing logic, transformation mechanisms, and safety
boundaries of one of the most systematic meditation teachers alive, with
provenance kept, contradictions preserved, and every load-bearing claim graded
by how well it is actually supported.

It is built for three kinds of reader:

1. **Serious practitioners working with an AI agent** - the primary use. Bring
   your live practice to the compiler and let an agent route it through
   Shinzen's actual distinctions, without the inflation, hallucination, or
   tradition-blending a generic model produces.
2. **AI agents** - a knowledge base to reason from, and a compiler to extend.
3. **Future models** - high-fidelity, de-inflated training data for one complete
   contemplative system (see [the end of this page](#for-training-and-future-models)).

> This is an independent, unofficial compilation. It does not replace direct
> instruction, a teacher, therapy, or medical care, and it is not endorsed by
> Shinzen Young or Unified Mindfulness. See [Sources, attribution, and
> rights](#sources-attribution-and-rights).

---

## Pick your path

| You are... | Start here |
| --- | --- |
| Here to **put an agent on it** (the main path) | [The fastest way to get value](#the-fastest-way-to-get-value-practice--an-ai-agent), then [`USING-WITH-AN-AGENT.md`](USING-WITH-AN-AGENT.md) |
| A practitioner who just wants to **read it** | The atlas at **[petrelaskov.xyz/shinzen](https://petrelaskov.xyz/shinzen/)** (or [`public-atlas/`](public-atlas/index.md)) - the path, the problem router, the glossary |
| An **AI agent** asked to operate or extend this repo | [`AGENTS.md`](AGENTS.md), then [For AI agents](#for-ai-agents-operating-or-extending-the-compiler) |
| Here to **reuse the compiler** on your own corpus | [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| Training or evaluating a **model** on this | [For training and future models](#for-training-and-future-models) |

---

## What this actually is

A compiled model of Shinzen's whole system, in three layers, designed to be
reasoned over by an AI agent.

### The corpus (`raw/`)

The immutable evidence lives in [`raw/`](raw/): treated as read-only. It
includes 500+ transcribed talks, retreat sessions, and Q&As, plus the core
long-form material - the *Five Ways* manual and the *See Hear Feel*
introduction. Raw sources are never edited; they are only compiled from and
cited.

### The knowledge (`wiki/`) - where the real value is

[`wiki/`](wiki/) is the compiled working memory: a linked knowledge graph of
400+ pages, and **the place the accumulated understanding actually lives.** It
uses seven epistemic page types (`source`, `entity`, `concept`, `thesis`,
`synthesis`, `analysis`, `question`); every page carries structured frontmatter
(claim, confidence, importance, routing cues); every load-bearing claim traces
to a source; contradictions are kept rather than smoothed; and source pages
carry explicit audit sections (weakest claims, important omissions, tensions).
You do not read 400 pages - **you put an agent in front of it** and let it
navigate the graph for your live question, with provenance and calibration
intact. This is the layer that makes the compiler more than a summary.

### The reading layer (`public-atlas/`) - optional

[`public-atlas/`](public-atlas/index.md) is the Shinzen Practice Atlas (~90
pages): a clean, human-readable distillation of the wiki, written for reading
rather than querying. Use it **only if you want the reading experience** - a
curated walk through the system. It is organized three ways at once: a ten-page
**path** you can read straight through, a **problem router** ("if this is live,
start here"), and a **reference shelf** (full map + glossary). It is the same
material as the wiki, made comfortable for a human; the wiki is still where the
depth and the receipts are.

### The one idea it is organized around

Everything routes back to a single move. *Meet what is actually happening - the
felt fact, not the story of it - with **concentration, sensory clarity, and
equanimity**, and stay with it until the experience can complete.* When an
experience can arise and pass without hardening into something that owns you,
Shinzen calls that **complete experience**. The Five Ways, See / Hear / Feel,
the Sensory Grid, Flow / Gone / Rest, no-self, Source language, Total Happiness,
and the behavior-and-service test are all that one move in another gear.

> **Want the machinery, not the meditation?** How the compiler works - the page
> types, the schema, the invariant, the audit surfaces - and how to point it at
> a different corpus is in [`ARCHITECTURE.md`](ARCHITECTURE.md).

---

## The fastest way to get value: practice + an AI agent

The highest-leverage use of this repository is **a serious practitioner plus an
AI agent plus this compiled wiki.** Here is the problem it solves.

Ask a general-purpose model about Shinzen's system and it will blend traditions,
inflate private states into proof, invent citations, lose his specific idiolect,
and reach for reassurance over calibration. Point that same model at this wiki
and it stops guessing: it routes your situation through Shinzen's actual
distinctions, tells you what is his teaching versus a compiled synthesis versus
an editorial inference, preserves the safety boundaries, and refuses to turn a
meditation experience into a medical, metaphysical, or teacher-authority claim
it cannot support.

The path is **agent + the wiki**, because the wiki is where the real accumulated
knowledge lives. Clone the repo and point a coding/agent tool at it:

```bash
git clone https://github.com/PetreLaskov/shinzen-meditation-wisdom-compiler.git
```

Claude Code, Cursor, or any agent with filesystem access can read the wiki
directly. Then give it its **rules of engagement** - reason from the wiki, cite
the pages and their sources, respect the claim tiers, do not inflate, hold the
safety posture, and say so when the wiki does not cover something. That one
paste is the difference between a grounded guide and a confident hallucinator.

**The full playbook is in [`USING-WITH-AN-AGENT.md`](USING-WITH-AN-AGENT.md):**
the rules-of-engagement block to paste, the six core workflows (route a live
situation, plan a block of practice, decode a term, stress-test an experience
against inflation, study the system, check provenance), and how to stop
scripting and let the agent route on its own. The posture in one line: treat it
as a **map room, not an oracle.**

---

## Reading it yourself (no agent needed)

If you would rather just read, the atlas is published as a website at
**[petrelaskov.xyz/shinzen](https://petrelaskov.xyz/shinzen/)** - the most
comfortable way in. The same pages live in
[`public-atlas/`](public-atlas/index.md). Three ways through it:

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

Read [`AGENTS.md`](AGENTS.md) first - it is the canonical operating contract -
and [`ARCHITECTURE.md`](ARCHITECTURE.md) for the layer model and reuse. Short
version:

- **Route before reading.** Read [`wiki/index.md`](wiki/index.md) for routing
  and current shape, skim recent [`wiki/log.md`](wiki/log.md), then descend:
  index -> frontmatter -> page card -> body -> raw source. Load raw sources only
  when the task needs source-level evidence.
- **Work in one mode per turn:** `ingest`, `query`, `synthesize`, `lint`,
  `review`, `refactor`. The playbooks are in [`commands/`](commands/).
- **Cite load-bearing claims, preserve contradictions, keep claims calibrated.**
  The governing invariant is *maximize future practice-reasoning quality,
  phenomenological discrimination, and transmission fidelity per token loaded.*
- **Verify mechanically.** Run the linter after structural changes:
  ```bash
  python tools/wiki_lint.py
  ```
  It is dependency-free and checks frontmatter, link resolution, source-page
  coverage, citation discipline, and required audit sections.

**Extending the corpus:** drop a new Shinzen source into `raw/`, then run an
`ingest`. **Forking the machinery for another corpus:** see
[`ARCHITECTURE.md`](ARCHITECTURE.md) - the compiler is corpus-agnostic.

---

## For training and future models

Beyond serving practitioners, this corpus is meant to be unusually good signal
for one complete contemplative system, for reasons that matter to a trainer:

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

There is a second signal here beyond the Shinzen content: the **method** itself.
The repository is a worked example of compiling a contested, partly tacit corpus
into calibrated, provenance-kept, routeable form. That pattern is the
transferable part, and it is legible in [`ARCHITECTURE.md`](ARCHITECTURE.md),
[`DESIGN.md`](DESIGN.md), and the page schemas.

**The one rule for using it well:** respect the tiers and the boundaries. Do not
launder "Shinzen says" into established science, medicine, metaphysics, or
teacher authority; do not present the wiki's syntheses as his exact words; and
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
| [`wiki/`](wiki/) | The compiled knowledge graph (400+ linked pages with provenance and calibration). **The real knowledge; put an agent on it.** |
| [`public-atlas/`](public-atlas/) | The human-readable Shinzen Practice Atlas (~90 pages). Optional reading layer. |
| [`raw/`](raw/) | Immutable source corpus. Read-only; cite, do not edit. |
| [`USING-WITH-AN-AGENT.md`](USING-WITH-AN-AGENT.md) | Full practitioner playbook for using the wiki with an AI agent. |
| [`AGENTS.md`](AGENTS.md) | Canonical operating contract for any agent working this repo. |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | How the compiler works, and how to reuse it on another corpus. |
| [`DESIGN.md`](DESIGN.md) | Full design rationale, complexity budget, and rejected alternatives. |
| [`CLAUDE.md`](CLAUDE.md) | Small compatibility adapter pointing to `AGENTS.md`. |
| [`commands/`](commands/) | Agent-neutral playbooks for each mode (ingest, query, lint, ...). |
| [`tools/`](tools/) | `wiki_lint.py`, the dependency-free structural invariant checker. |
| [`ATLAS - Editorial Plan.md`](ATLAS%20-%20Editorial%20Plan.md) | The editorial plan behind the public atlas. |
| [`archive/`](archive/) | Earlier drafts and reference material kept for history. |

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
