# Agentic Knowledge Compiler Design

## 1. Executive Thesis

We are building a markdown-native agentic knowledge compiler: a persistent
system that transforms raw sources and useful conversations into a routeable,
auditable, progressively disclosed body of compiled understanding.

The system is not a file dump, a RAG chatbot, or a generic wiki. Raw sources
remain immutable evidence. The wiki is the agent-maintained compiled layer:
source pages, concepts, entities, theses, syntheses, analyses, questions,
links, contradictions, confidence judgments, and open frontiers.

The agent has full autonomy to maintain the wiki, but that autonomy is
operational rather than theatrical. It reads the routing surfaces first,
loads only what the task needs, improves durable artifacts instead of
letting insights die in chat, and uses the user's taste and judgment as a
natural part of the loop when the structure of the knowledge graph is at
stake.

The central invariant is:

> Maximize future reasoning quality per token loaded.

This means route before reading, cite load-bearing claims, distribute depth
across intelligently linked pages, and keep architectural primitives austere
even as the wiki itself becomes richly navigable.

## 2. Non-Goals

This project is not:

- A generic wiki where pages are manually maintained.
- A RAG chatbot that retrieves source chunks at query time.
- An exhaustive source archive.
- A personal note hoarder.
- A generic PKM template.
- A vector database MVP.
- An embedding-first search system.
- A multi-agent framework MVP.
- A background daemon or autonomous scheduler MVP.
- A complex knowledge-graph application.
- A page-count maximizer.
- A one-page-per-book summarizer.
- A synthesis engine that launders weak evidence into strong claims.

The system may eventually use search, graph inspection, digest checks,
eval fixtures, or even embeddings, but each tool must earn its place by
solving a demonstrated failure of the markdown/index/page-card approach.

## 3. Design Taste And Working Assumptions

These are the local preferences that should steer implementation.

### Agent Autonomy

The agent should be trusted to act. It should create, update, split, link,
and file pages when the evidence warrants it. The user is inevitably in the
loop through source curation, questions, review, and taste feedback, so the
design should not overcorrect into conservative paralysis.

Large refactors should still leave visible artifacts: a log entry, a review
note, or a clear old-to-new mapping. The point is not to ask permission for
ordinary maintenance. The point is to make consequential changes legible.

### Depth Without Bloat

Progressive disclosure is the answer to page bloat. A page should serve:

- Skimmers: frontmatter, thesis, opening, card/key points, index entry.
- Deep readers: dense body sections, evidence, contradictions, links,
  footnotes or collapsible detail when the medium supports them.

Depth should be distributed across pages when the subject naturally has
multiple durable concepts, entities, questions, or theses. Prior failures
that compressed whole books into sparse pages are explicitly not the target.

### Parsimony At The Primitive Layer

Parsimony applies to the architecture, not to the knowledge graph's richness.
The primitives should stay few: markdown, frontmatter, page cards, index,
log, source pages, links, templates, and small deterministic tools. Within
that simple substrate, the agent should build a balanced, well-linked graph.

The bad extremes are:

- Underfitting: a few bloated pages with weak links.
- Overfitting: a page for every named noun.

The target is a navigable middle: create pages when they improve future
routing, explanation, synthesis, contradiction handling, or reuse.

### Usefulness With Skepticism

Bias toward usefulness. Do not turn every page into a caveat machine. But
where sources conflict, agendas matter, evidence is weak, or claims are
inferred rather than observed, mark that clearly.

Skepticism belongs where it changes interpretation. It should sharpen the
reader's model, not merely signal virtue.

### Reader Profile

Pages should serve intelligent generalists who may not be specialists.
They should support overview-first reading and deeper study:

- Clear structure.
- Precise abstracts or cards.
- Strong first paragraphs.
- Dense but readable key points.
- Rich internal links.
- Comprehensive citations for load-bearing claims.
- Durable insights over ephemeral commentary.

### Citation Burden

Every load-bearing claim should be cited. A page may contain orientation
prose without citation, but claims that support an argument, update a model,
resolve a question, or affect confidence must trace to a source page or be
explicitly marked as unsupported/speculative.

## 4. Relationship To The Existing Implementation

The existing "previous working implementation - wiki compiler" is the right
backbone and should be respected.

Preserve:

- `raw/` as immutable input.
- `wiki/` as compiled output.
- `wiki/index.md` as first-read routing surface.
- `wiki/log.md` as append-only chronology.
- Flat `wiki/` content pages for Obsidian-friendly linking.
- Seven epistemic page types: `source`, `entity`, `concept`, `thesis`,
  `synthesis`, `analysis`, `question`.
- Compression gradient: frontmatter, opening, key points, body, related.
- The distinction between links, domains, and tags.
- The lifecycle model from source coverage to synthesis to maintenance.
- `wiki/_templates.md`, `wiki/_operations.md`, `wiki/_shape.md`.
- `tools/wiki_lint.py` as a dependency-free invariant checker.
- The style guidance that prevents compiler voice drift.

Change or clarify:

- Do not let "parsimony" mean page starvation.
- Make page creation balanced and adaptive rather than conservative by
  default.
- Treat page splitting as a normal health move when a page starts doing
  multiple durable jobs.
- Strengthen source-frame and contradiction handling.
- Make `AGENTS.md` the eventual canonical Codex-facing operating contract;
  `CLAUDE.md` can be a small compatibility adapter or mirror.
- Consider claim IDs, source digests, search, graph reports, and evals as
  earned upgrades, not automatic MVP scope.

The existing upgrade design document contains valuable ideas, especially
claim-level provenance and deterministic inspection. Its risk is adopting
too many second-order tools at once. This design keeps those as explicit
escalation paths.

## 5. Core Architecture

The minimal architecture is:

```text
AGENTS.md
CLAUDE.md
README.md

raw/
  README.md
  assets/
  source files...

wiki/
  index.md
  log.md
  _templates.md
  _operations.md
  _shape.md
  content pages...

tools/
  wiki_lint.py
```

Optional, earned later:

```text
wiki/_schema.md
wiki/_style.md
wiki/_reviews/
wiki/_indexes/
wiki/_migrations/

tools/wiki_search.py
tools/wiki_graph.py
tools/wiki_eval.py

evals/fixtures/
commands/
```

Content pages should remain flat in `wiki/` until scale forces generated
sub-indexes. Directories such as `wiki/concepts/` or `wiki/sources/` are
not needed for the MVP because type and domain are already represented in
frontmatter and index placement. Folders should be added only if they solve
a concrete navigation or tooling failure.

## 6. Layer Model

### Raw Source Layer

Location: `raw/`

Purpose: immutable evidence.

Owner: human/source curator.

Agent rule: read, cite, and compile from raw sources, but do not modify
them.

### Compiled Wiki Layer

Location: `wiki/` content pages.

Purpose: the agent's durable best model of what the sources mean.

Owner: agent.

Agent rule: maintain this layer aggressively but honestly. Update it after
meaningful ingests, queries, reviews, and syntheses.

### Routing Layer

Location: `wiki/index.md`, page frontmatter, page cards/key points,
`wiki/log.md`.

Purpose: decide what to load next without reading everything.

Owner: agent.

Agent rule: every meaningful change must preserve or improve routing.

### Governing Layer

Location: `AGENTS.md`, optional `CLAUDE.md`, `_operations.md`,
`_templates.md`, `_shape.md`.

Purpose: durable operating contract and page conventions.

Owner: mixed, but changes are deliberate and logged.

Agent rule: do not silently drift schema or workflow.

### Deterministic Tooling Layer

Location: `tools/`.

Purpose: enforce invariants too mechanical to entrust to prose.

Owner: mixed.

Agent rule: add tools only when they reduce context load, catch recurring
failures, or make validation materially more reliable.

## 7. Page Types

Use seven page types unless they genuinely fail.

### `source`

One-to-one interface between a raw source and the compiled wiki. It is not
the final synthesis. It records provenance, source frame, strongest claims,
weakest claims, important omissions, contradictions/tensions, limitations,
and integration notes. The `Weakest Claims`, `Important Omissions`, and
`Contradictions/Tensions` sections are required audit surfaces for source
pages.

### `entity`

A real-world thing: person, organization, system, project, place, event,
dataset, product, institution. Create when the entity recurs, anchors
multiple claims, or materially changes routing.

### `concept`

A reusable abstraction, mechanism, distinction, pattern, or term. Create
when the idea carries explanatory load across pages or must be distinguished
from nearby ideas.

### `thesis`

An argued position. This is the wiki making a claim from evidence. A thesis
must include support, counter-considerations, confidence, and what would
change the model.

### `synthesis`

A map of a domain or cluster. It names the through-line, the sub-areas, the
tensions, and the frontier. A synthesis is not a page listing. If no
through-line is visible, create or update a question instead.

### `analysis`

A reusable answer to a query, comparison, or investigation. Lighter than a
thesis but more durable than a chat answer.

### `question`

A durable open frontier. Questions are first-class because gaps, unresolved
contradictions, and needed evidence are part of the compiled model.

## 8. Minimal Page Schema

The existing schema is mostly right:

```yaml
---
type: source | entity | concept | thesis | synthesis | analysis | question
thesis: "Single sentence claim plus significance."
status: seed | working | mature | evergreen
domain: [primary, secondary]
importance: 1
confidence: established | probable | speculative | contested
tags: []
aliases: []
sources: [raw/source.md]
updated: YYYY-MM-DD
---
```

Implementation may keep the existing emoji status values if desired, but
the design meaning should be explicit:

- `seed`: a valid stub with routing value.
- `working`: enough body and links to answer adjacent questions.
- `mature`: evidence, boundaries, and links have survived review.
- `evergreen`: stable entry point unlikely to shift without major sources.

Fields should remain few enough that agents actually use them. New fields
must pass the "future routing or audit value" test.

Possible earned additions:

- `source_digest`: for source pages, if mtime re-ingest proves brittle.
- `depends_on`: for synthesis/question pages that draw from compiled pages
  rather than direct raw sources.
- `schema_version`: only once schema migration becomes real.

## 9. Page Card Pattern

Every page should expose its relevance in the first 30 to 60 lines. The
existing "opening plus Key Points" pattern already does this. For clarity,
finished pages should effectively contain this card even if the heading is
called `Key Points`.

```markdown
## Key Points
- **Core claim**: ...
- **Why this matters**: ...
- **Load this page when**: ...
- **Key tensions**: ...
- **Best linked pages**: ...
- **Source posture**: ...
```

This card is not bureaucratic metadata. It is the page's skimmable decision
surface. It lets an agent or human decide whether to read the body.

For short pages, collapse the card into three dense bullets. For mature
pages, keep it explicit. The invariant is progressive disclosure, not a
mandatory heading count.

## 10. Page Creation Rule

Create a new page when one or more of these are true:

- The subject will recur across sources or queries.
- It changes how future agents should route.
- It carries an independent model, mechanism, entity, thesis, or question.
- It prevents an existing page from doing multiple jobs.
- It clarifies a contradiction or frontier.
- It creates a reusable answer or synthesis.
- It provides a stable target for future links.

Do not create a new page when:

- The concept is mentioned once and has no expected reuse.
- The page would only restate a source summary.
- The page would duplicate an existing model under a synonym.
- The claim fits naturally as a section or paragraph in an existing page.
- The page exists only because a noun appeared in a source.

Bias correction: when uncertain between one bloated page and two coherent
linked pages, prefer the split. When uncertain between a useful stub and
burying a recurring idea in a source page, prefer the stub. When uncertain
between a page for every noun and a richer existing page, prefer the richer
existing page.

## 11. Link Semantics

Links are not mentions. A link earns its existence when reading the target
would materially change interpretation of the current page.

Use links for:

- Conceptual dependency.
- Contradiction or rivalry.
- Evidence relationship.
- Adjacent mechanism.
- Cross-domain analogy or tension.
- Entity/concept/thesis relationships that future queries will traverse.

Avoid:

- Linking every named entity.
- Re-linking the same target repeatedly.
- Turning citations into generic related links.
- Creating bidirectional links mechanically when the relation is one-way.

`Related` sections should contain durable semantic edges with a reason.
Inline links can be lighter. Citation links should remain citation-shaped.

Cross-domain links are especially valuable because they reveal transferable
mechanisms, analogies, and tensions. They are one of the main differences
between a compiled knowledge system and a folder of notes.

## 12. Source Page Schema

Every substantive raw source should have exactly one source page.

Required source-page structure:

```markdown
---
type: source
thesis: "What this source claims or contains, and why it matters."
status: working
domain: [primary]
importance: 5
confidence: established
tags: []
aliases: []
sources: [raw/source.md]
updated: YYYY-MM-DD
---

[One sentence locating the source.]

## Source Snapshot
- **Path**: `raw/source.md`
- **Origin**: author, publisher, organization, URL, or internal source
- **Date**: publication or creation date
- **Format**: article, book chapter, transcript, memo, paper, dataset
- **Reliability**: primary, secondary, tertiary, agenda, bias, limits
- **Scope**: what it covers and what it does not cover

## Key Claims
- **S1**: Claim stated by the source. Cite location if available.
- **S2**: Claim stated by the source.
- **S3**: Inference from the source, marked as inference.
- **S4**: Claim that contradicts or updates an existing page.

## Summary
[Faithful 1 to 3 paragraph compression of the source.]

## Source Frame
[What frame, agenda, discipline, incentive, or omission shapes the source.]

## Weakest Claims
- [Broad, under-supported, overcompressed, or source-limited claims.]

## Important Omissions
- [Missing evidence, deferred detail, scope limits, or excluded cases that change interpretation.]

## Contradictions/Tensions
- [Internal tensions, conflicts with existing pages, or interpretive pressure points.]

## Integration Notes
- **Pages created**: [[Page]]
- **Pages updated**: [[Page]]
- **Contradictions opened**: [[Question or Thesis]]
- **Confidence changes**: ...
- **Low-signal material excluded**: ...

## Related
- [[Page]] - why this source bears on it
```

Claim IDs such as `S1`, `S2`, and `S3` are optional for the smallest MVP but
strongly recommended as soon as sources become dense or contested. They are
local, readable anchors, not a database.

## 13. Ingestion Workflow

Ingest is where the wiki compounds.

### Route

1. Read `AGENTS.md` or the governing contract.
2. Read `wiki/index.md`.
3. Skim `wiki/log.md` for recent context.
4. Inspect relevant page cards/key points before full bodies.
5. Identify likely affected source, entity, concept, thesis, synthesis, and
   question pages.

### Read Source

1. Read the raw source fully enough for a faithful source page.
2. Extract source claims, evidence, frame, agenda, weakest claims, important
   omissions, and contradictions/tensions.
3. Mark observation, source claim, inference, and agent synthesis distinctly.
4. Note contradictions with existing pages.
5. Note reusable concepts/entities/questions/theses that deserve pages.

### Allocate Pages

Create:

- One source page always.
- New entity/concept/question/thesis pages when warranted.
- A synthesis only when a real through-line is visible.

Update:

- Existing pages that the source changes.
- Related sections for durable semantic edges.
- The index and log.

The agent should be balanced and adaptive here. It should neither compress
a whole book into one swollen page nor explode every paragraph into stubs.

### Compile

1. Write or update the source page.
2. Integrate claims into durable pages.
3. Add contradictions, rival explanations, or open questions where they
   matter.
4. Preserve uncertainty without flattening disagreement.
5. Exclude low-signal material deliberately.
6. Update the index with new entries and refreshed dashboard/shape details
   when the wiki's shape changes.
7. Append one log entry.

### Verify

1. Run deterministic lint when available.
2. Check every new link resolves.
3. Check every new page appears in the index.
4. Check every load-bearing claim has a citation or explicit uncertainty.
5. Check no page is doing too many jobs.
6. Check no new page exists only as a noun index.
7. Check index/log changed when the wiki changed.

## 14. Query Workflow

Queries should use the compiled wiki first.

1. Read `wiki/index.md`.
2. Use domain, type, importance, confidence, tags, and thesis/card text to
   choose candidate pages.
3. Read page cards before full bodies.
4. Read relevant full page bodies.
5. Read raw sources only when:
   - the compiled page is insufficient,
   - provenance is the question,
   - a claim is contested,
   - the compiled page appears stale,
   - the citation/source-link is not enough.
6. Answer with calibrated confidence and citations.
7. If the answer is reusable, file it as `analysis`, `synthesis`, `thesis`,
   or `question`.
8. If the query reveals a gap, update or create a `question` page.
9. Append a log entry if the wiki changed.

Good answers should compound. Chat is not a graveyard for durable insight.

## 15. Contradictions And Source Agendas

Contradictions are not mess. They are information.

When sources disagree:

- Preserve both claims.
- Attribute each claim.
- Mark affected pages `contested` when the disagreement changes the page's
  central claim.
- Link the rival pages.
- Create a `question` when the disagreement is unresolved.
- Create or update a `thesis` when the wiki has enough evidence to argue a
  position.
- Explain what evidence would resolve or weaken each side.

When source agendas matter:

- Record the source frame on the source page.
- Do not import the source's frame as the wiki's voice.
- Distinguish what the source proves from what it assumes.
- Note omissions when they change interpretation.
- Avoid laundering a stakeholder claim into an established fact.

Use skepticism where warranted, but keep the page useful. The reader should
come away with a better model, not just a longer disclaimer.

## 16. Depth And Progressive Disclosure

The page should become more detailed only after the reader chooses to dwell.

Layer order:

1. Index entry: route-level one-liner.
2. Frontmatter thesis: maximum compression.
3. Opening: 1 to 2 sentences of context.
4. Key points/card: skimmable spine.
5. Body: full model, evidence, mechanisms, boundaries.
6. Related: durable graph edges.
7. Raw source: only when necessary.

Depth is preserved by:

- Better distinctions.
- Rich but earned links.
- Dense source pages.
- Separate pages for independent concepts, entities, theses, and questions.
- Synthesis pages that map clusters.
- Footnotes or collapsible details when useful and supported by the medium.

Depth is not:

- Long pages by default.
- Repeating source order.
- Generic "insights."
- Decorative taxonomies.
- One giant summary per book.

## 17. Index Design

`wiki/index.md` is the main routing surface.

It should contain:

- Shape paragraph: scope, through-line, maturity, next leverage.
- Recent activity: 5 to 10 entries.
- Operating dashboard: awaiting ingest, compiled page counts, maintenance
  debt, highest-leverage next step.
- Open questions: top active questions.
- Domain sections: page entries grouped by primary domain.

Entry format:

```markdown
- [[Page]] - thesis or card-level one-liner (importance, status, confidence)
```

The index should be rich enough to route and skim, not exhaustive in prose.
At larger scale, domain sections should gain short abstracts and eventually
point to synthesis pages or generated sub-indexes. The main index must never
become a 1,000-line dump that agents must read in full.

## 18. Log Design

`wiki/log.md` is append-only, newest first.

Entry shape:

```markdown
## [YYYY-MM-DD] op | Subject
Summary of what changed. Pages touched: [[P1]], [[P2]]. Assumptions,
open issues, validation notes, or deferred work when they matter.
```

Use one entry per session-bounded operation. Do not dump chat history. The
log should let a future agent understand what changed and why.

## 19. Lint And Health Workflow

Start with the existing `tools/wiki_lint.py`.

Hard checks:

- Required frontmatter exists.
- Type/status/confidence/importance values are valid.
- All wikilinks resolve.
- Every raw source has exactly one source page.
- Every compiled page appears in the index or approved sub-index.
- Non-source pages cite sources or explicitly declare synthesis dependency.
- `updated` dates are valid.

Semantic checks:

- Orphan pages.
- Pages doing too many jobs.
- Bloated pages that should split.
- High-importance stubs.
- Topic-label theses.
- Uncited load-bearing claims.
- Smoothed contradictions.
- Contested claims without reciprocal representation.
- Weak source pages not integrated anywhere.
- Page bodies that no longer match their frontmatter/card.
- Index entries too vague to route.
- Question pages with no dependencies.
- Source pages whose frame/agenda is missing despite obvious stakes.

The tool should enforce what is mechanical. The agent should review what
requires judgment.

## 20. Review Workflow

Run review periodically or when the wiki feels structurally off.

Review should inspect:

- Orphans.
- Duplicate pages.
- Pages over about 600 to 900 words with visible internal divisions.
- Stale pages affected by recent ingests.
- Tag drift.
- Domain swelling.
- Weak cards.
- Missing links.
- Link spam.
- Contradiction handling.
- Source coverage.
- Questions that should become analyses/theses.
- Analyses that should be promoted into syntheses.
- Shape paragraph drift.

Review may safely fix small local issues. Larger refactors should be
logged with an old-to-new map and verified after change.

## 21. Context Hygiene Protocol

Context hygiene is an invariant, not a suggestion.

Default read order:

1. Governing instruction file.
2. `wiki/index.md`.
3. Recent `wiki/log.md` entries.
4. Page frontmatter and cards/key points.
5. Relevant page bodies.
6. Raw sources only just in time.

Use targeted search before broad reading. Prefer `rg`, filename lists,
frontmatter scans, and index entries over loading raw sources. Do not
solve context problems by adding embeddings, databases, agents, daemons, or
servers before the markdown/index/card approach has demonstrably failed.

Route-before-read checklist:

- What mode is this: ingest, query, synthesize, lint, review, refactor?
- What routing surface answers where to look?
- Which pages are likely relevant by thesis/card?
- What is the minimum body set needed?
- Is raw source access justified?
- What durable artifact should change if the answer is valuable?
- What index/log update will preserve continuity?

## 22. Verification And Evals

Manual evals come before tool-heavy automation.

Initial eval scenarios:

- Ingest one source that creates a source page and two to five justified
  derived pages.
- Ingest a source that contradicts an existing thesis.
- Answer a query from index plus one page.
- Answer a query requiring multiple pages but no raw source.
- Verify a contested claim by descending to raw source.
- Detect a bloated page that should split.
- Detect a noun page that should merge into an existing page.
- Refresh an index whose shape paragraph is stale.
- Run lint and catch broken links/source coverage.
- File a reusable chat answer as an analysis page.

Scoring should reward:

- Future reasoning value.
- Citation traceability.
- Balanced page creation.
- Link quality.
- Contradiction preservation.
- Index usefulness.
- Lack of unnecessary machinery.

Scoring should punish:

- Page count for its own sake.
- Sparse book summaries.
- Source laundering.
- Forced synthesis.
- Link spam.
- Chat answers not filed when reusable.

## 23. Complexity Budget And Escalation Rules

Complexity is allowed when it earns its keep.

### Search Script

Justified when:

- Index and targeted `rg` stop finding relevant pages reliably.
- Wiki exceeds roughly 100 to 200 content pages.
- Query setup spends too much context scanning page lists.

Minimal version:

- Deterministic keyword/BM25-like local search over wiki pages.
- Compiled pages searched before raw sources.

### Source Digests

Justified when:

- mtime-based re-ingest is unreliable.
- Sources are copied, synced, or touched frequently.
- Stale source detection matters.

Minimal version:

- `source_digest` on source pages and lint comparison.

### Claim IDs

Justified when:

- Sources are dense.
- Claims are contested.
- Auditing exact support becomes difficult.
- Derived pages cite the same source for multiple different claims.

Minimal version:

- Local `S1`, `S2`, `S3` bullets on source pages.
- Derived pages cite source page plus claim ID when needed.

### Graph Tool

Justified when:

- Orphans, hubs, link spam, or unreciprocated Related edges become hard to
  inspect manually.

Minimal version:

- Parse wikilinks and Related sections.
- Report orphans, high-degree hubs, broken Related reciprocity, and
  domain/tag counts.

### Review Reports

Justified when:

- Review findings exceed what a single log entry can responsibly hold.
- The wiki has recurring deferred maintenance.

Minimal version:

- `wiki/_reviews/YYYY-MM-DD-review.md` linked from `log.md`.

### Eval Harness

Justified when:

- Multiple agents or versions need comparison.
- Regressions recur.
- Page distribution quality needs repeatable testing.

Minimal version:

- Small fixture directories plus markdown rubrics.

### Embeddings Or Vector DB

Justified only after:

- Index, page cards, `rg`, and deterministic search fail at scale.
- The failure mode is retrieval, not poor page writing.
- The embedding layer can be treated as cache, never source of truth.

Minimal version:

- Local cache over compiled pages.
- No raw-source-first behavior.

### Subagents, MCP, Daemons, Custom UI

Deferred. They are not MVP primitives. Add only after a concrete workflow
cannot be made reliable through markdown, scripts, and agent discipline.

## 24. Smallest Implementation That Works Well

The smallest strong implementation is:

- `AGENTS.md`: concise operating rules.
- `CLAUDE.md`: compatibility adapter or mirror.
- `README.md`: quickstart and concept.
- `raw/README.md`: source quality and immutability.
- `wiki/index.md`: route map.
- `wiki/log.md`: chronology.
- `wiki/_templates.md`: seven page templates.
- `wiki/_operations.md`: workflows.
- `wiki/_shape.md`: index shape guide.
- `tools/wiki_lint.py`: deterministic structural checks.

This is enough to ingest sources, create balanced linked pages, answer
queries from the wiki, file durable analyses, run lint, and review health.

Claim IDs and source digests are the first upgrades to consider because they
increase auditability without changing the medium.

## 25. Implementation Plan

### Phase 0: Inspect And Decide

- Read GPT Pro instructions.
- Read existing implementation.
- Preserve the working backbone.
- Record local taste corrections: balanced page creation, full autonomy,
  progressive disclosure, every load-bearing claim cited.

### Phase 1: Design Document

- Create `DESIGN.md`.
- Make tradeoffs explicit.
- Mark complexity gates.
- Define page creation and routing rules that correct underfitting.

### Phase 2: Operating Contract

- Rewrite or adjust `AGENTS.md` as the canonical concise contract.
- Keep `CLAUDE.md` as a compatibility file.
- Keep long procedures in `_operations.md`, not `AGENTS.md`.

### Phase 3: Templates

- Update templates to emphasize page cards, source frames, load-bearing
  citations, and balanced page distribution.
- Add optional source claim IDs where useful.
- Remove template sludge and type-duplicating tags.

### Phase 4: Index And Log

- Refine `index.md` conventions.
- Preserve operating dashboard and open questions.
- Make recent activity and shape paragraph update rules explicit.

### Phase 5: Lint

- Keep the existing dependency-free linter.
- Add checks only for recurring mechanical failures.
- Avoid schema sprawl before real content exists.

### Phase 6: Evals

- Run manual evals on a small sample corpus.
- Test contradiction handling, page distribution, and query filing.
- Add automated fixtures only once manual evals stabilize.

### Phase 7: Escalate Tools If Needed

- Add search, graph, digest, or eval tools only after observed failure.
- Keep markdown pages as source of truth.

## 26. Design Decisions

### Decision: Keep Flat Content Pages

Flat pages preserve Obsidian compatibility and simple wikilinks. Type and
domain already provide organization. Add generated sub-indexes before nested
content folders.

### Decision: Keep Seven Page Types

The seven existing types map to distinct epistemic moves. More types would
probably encode taste prematurely.

### Decision: Bias Toward Balanced Page Creation

Prior GPT-style implementations overcorrected toward few pages and bloated
summaries. This design explicitly prefers splitting when a recurring idea,
entity, thesis, or question earns independent routing value.

### Decision: Cite Every Load-Bearing Claim

Citation discipline is part of the truth-seeking contract. The system may
still use graceful prose, but claims that matter must trace.

### Decision: Treat Tools As Earned Prosthetics

Tools are welcome when they reduce context or improve verification. They are
not architectural status symbols.

## 27. Rejected Alternatives

### Embedding-First RAG

Rejected because it makes the wiki secondary and forces the model to
rediscover knowledge at query time.

### Database-Backed Knowledge Graph

Rejected for MVP because it sacrifices markdown legibility, Obsidian
compatibility, and low-friction editing.

### Extreme Page Parsimony

Rejected because it hides complexity inside bloated pages and harms routing.

### Page For Every Concept

Rejected because it produces ontology sprawl and weak pages without future
use.

### Full Claim Ledger Everywhere

Rejected for MVP because it can make markdown feel like a database. Use
claim IDs first on source pages and contested/load-bearing evidence.

## 28. Open Questions

The remaining user-level decisions are:

- Whether source claim IDs should be mandatory immediately or introduced
  after the first dense/contested corpus.
- Whether status should stay as the existing emoji values or move to
  ASCII values such as `seed`, `working`, `mature`, `evergreen`.
- Whether to keep `CLAUDE.md` as a full mirror or make it a tiny adapter
  pointing to `AGENTS.md`.
- Whether early implementation should start from the previous repo as a
  template copy or modify it in place.

My recommendation: implement the markdown backbone first, with source claim
IDs as a lightweight convention in source pages, and defer digests/search/
graph/eval tooling until actual content reveals the first bottleneck.
