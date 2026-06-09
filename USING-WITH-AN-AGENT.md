# Using the compiler with an AI agent

The full practitioner playbook for putting an AI agent in front of this compiled
Shinzen wiki. The [README](README.md) has the short version; this is the
complete one - setup, the rules-of-engagement block to paste, the core
workflows, and how to let the agent route on its own.

The highest-leverage use of this repository is **a serious practitioner plus an
AI agent plus the compiled wiki.** Here is the problem it solves.

Ask a general-purpose model about Shinzen's system and it will blend traditions,
inflate private states into proof, invent citations, lose his specific idiolect,
and reach for reassurance over calibration. Point that same model at this wiki
and it stops guessing: it routes your situation through Shinzen's actual
distinctions, tells you what is his teaching versus a compiled synthesis versus
an editorial inference, preserves the safety boundaries, and refuses to turn a
meditation experience into a medical, metaphysical, or teacher-authority claim
it cannot support.

The knowledge lives in `wiki/` - a calibrated, sourced knowledge graph of 400+
pages. `public-atlas/` is the same material made human-readable, for when you
(or the agent) want a clean explanation rather than the full receipts.

## Setup

Pick whichever fits your tools:

- **Clone and point a coding/agent tool at the folder.** Claude Code, Cursor,
  or any agent with filesystem access can read [`wiki/`](wiki/) and
  [`public-atlas/`](public-atlas/) directly.
  ```bash
  git clone https://github.com/PetreLaskov/shinzen-meditation-wisdom-compiler.git
  ```
- **Upload the folder** to a chat assistant that accepts files or projects, and
  tell it to use the wiki as the source of truth (and the atlas for readable
  explanations).
- **Paste the page(s)** the agent or the [problem router](public-atlas/index.md#start-by-problem)
  points you to - from this repo or the [atlas
  website](https://petrelaskov.xyz/shinzen/) - into any chat, for a one-off
  question.

For a quick read, the `public-atlas/` pages are enough. For the real depth -
provenance, confidence, contradictions, the full model behind a summary - have
the agent work the `wiki/`.

## Give the agent its rules of engagement

Paste this once at the start of a session. It is the difference between a
grounded guide and a confident hallucinator.

```text
You are helping me reason about my meditation practice using this compiled
Shinzen wiki. The real knowledge is in wiki/ (a calibrated, sourced knowledge
graph); public-atlas/ is the human-readable version of the same material.

Rules:
- Reason FROM the wiki. Read AGENTS.md and wiki/index.md first, route by the
  frontmatter (thesis, load_when, confidence) to the relevant pages, and cite
  the page(s) and their source pages. Use public-atlas/ when I want a clean,
  readable explanation.
- Respect calibration. Tell me a claim's confidence (established / probable /
  speculative / contested) and whether it is "Shinzen says" vs. compiled
  synthesis vs. editorial inference vs. not established here. Do not present a
  synthesis as his exact words.
- Do not inflate. Do not turn an experience into proof of awakening, science,
  metaphysics, or that a teacher is safe. Preserve Shinzen's distinctions; do
  not flatten them into generic Buddhism or generic mindfulness.
- Hold the safety posture. If what I describe points to medical, psychiatric,
  trauma, consent, coercion, or harm risk, say so plainly and tell me to get
  appropriate human support. You are not my teacher, therapist, or doctor.
- When the wiki does not cover something, say so instead of inventing it.
```

## The main workflows

Six recurring jobs cover most of what practitioners need. The prompts below are
copy-paste *starting points* - scaffolds, not scripts. Once your agent has the
rules of engagement above and the wiki in context, it is already a competent
router, so feel free to strip these right down (see [Let the agent
cook](#let-the-agent-cook)). The named pages below are the readable atlas
entry points; tell the agent to pull provenance and calibration from the wiki.

**1. Route a live situation.** The flagship use. The atlas even has a page on
how to write a report specific enough to route well
([`practice-report-check.md`](public-atlas/practice-report-check.md)).

```text
Here is what is happening in my practice: <describe the method you are using,
how long, what you noticed, and what feels stuck, intense, confusing, or off>.

Work the wiki: route my situation to the relevant pages, tell me what the one
move is here, and flag the confidence/claim tier of anything load-bearing. Flag
anything that needs a human teacher or medical/clinical support before I keep
optimizing technique.
```

**2. Plan a sane block of practice.**

```text
I have <X minutes, Y days a week, this much life load>. Using the wiki's
practice-planning and route-choice pages, help me pick ONE primary route and a
stop/adjust rule, without overchoice or intensity drift. Keep it boring and
repeatable.
```

**3. Decode a term without losing the distinction.**

```text
Explain "<Gone / Do Nothing / equanimity vs. suppression / Source / Flow / the
Five Ways>" the way Shinzen uses it, from the wiki's owner page and glossary.
Give the practice handle, the failure mode it solves, and how the method itself
can go wrong. Mark anything that is inference rather than his teaching, and cite
the source page.
```

**4. Stress-test an experience against inflation.** The compiler is unusually
good here, because it was built to resist exactly this.

```text
After a sit / retreat I am concluding <X> (e.g. "my self is gone," "I am ready
to teach," "this proves no-self/awakening"). Using the wiki's pages on signs of
completion, completion vs. bypass, good-place traps, and the behavior-and-
service test: is this a completion sign, a good-place trap, or bypass? What is
the behavior/service test, and what would actually verify it?
```

**5. Study the system properly.**

```text
Walk me through the ten-page spine in order, one page per turn. After each,
summarize the one move in that gear, quiz me with two questions, and only then
go to the next page.
```

**6. Check provenance.**

```text
For the claim "<...>", find the owner page and its source page in the wiki, and
tell me: what is the actual source, the confidence, the weakest claims, and any
contradictions the wiki records. Is this Shinzen's teaching, a synthesis, or an
inference? Descend to the raw source only if the citation is not enough.
```

## Let the agent cook

The prompts above are training wheels. With the rules of engagement loaded and
the wiki in context, the agent can choose the pages, the depth, and the order
better than a fill-in-the-blank template can - and over-specifying often boxes
it in. The skill to develop is handing it the real situation and trusting it to
route, tier, and flag safety on its own.

**Orientation is the first thing to hand off.** You do not need to know the map
before you start; that is the agent's job:

```text
I'm new to Shinzen's system. Read the wiki and orient me - where should I start,
given <a sentence or two about me and why I'm here>?
```

```text
I don't even know what to ask yet. Here's roughly where I am: <a few sentences>.
Read the wiki and tell me what I should be looking at, and what I'm probably
missing.
```

**Then let it cook.** Minimal, plain-language prompts are often enough:

- "Here's what's going on: <plain language>. Help me."
- "Something shifted in my last sit and I can't name it. Walk with me through it."
- "I keep bouncing between techniques and getting nowhere. Sort me out."
- "Teach me this system the way you'd teach a sharp friend over coffee. Start
  wherever makes sense and check I'm actually following."
- "Push back on me: I think <X> about my practice. Is that what the wiki would
  actually say, or am I inflating?"

Name specific pages or output formats only when you want to pin the agent down.
The rest of the time, let it work - and when it drifts off the wiki, inflates,
or skips a boundary, say so. Catching that is itself good practice, and it makes
the next answer better.

## What good use looks like

Treat it as a **map room, not an oracle.** Bring a specific report, let it route
you to the right handle and the right caution, and take the boundaries
seriously. The compiler earns trust precisely because it tells you where it
stops - keep that property by not pushing it past it.
