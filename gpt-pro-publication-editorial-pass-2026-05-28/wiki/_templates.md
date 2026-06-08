# Templates

Copy the relevant scaffold, replace placeholders, then prune any section that
does not earn its place. Empty headings are template sludge.

Conventions:

- Set `updated:` to today's date on creation or meaningful revision.
- Keep frontmatter lists inline: `domain: [primary]`.
- Cite load-bearing claims through source pages and raw paths in
  `sources:`.
- Put first-pass routing in frontmatter: `load_when:` for the cue and
  `best_linked_pages:` for quoted wikilinks to the most useful neighbors.
- Keep routing frontmatter bounded. It is a triage card, not a whole map:
  `load_when:` should be one discriminating sentence, target 160-320
  characters; `best_linked_pages:` should usually list 3-8 strongest next
  loads; non-source `sources:` should keep only principal raw anchors unless
  the page is a source interface; `aliases:` should contain real lookup
  aliases, not every query phrase. Move exhaustive routing detail to the
  opening, `## Key Points`, `## Dependencies`, `## Related`, or source-page
  citations in the body.
- Use source claim IDs such as `S1`, `S2`, `S3` when a source is dense,
  contested, or likely to be cited repeatedly.
- Source pages must keep the audit spine: `Weakest Claims`, `Important
  Omissions`, and `Contradictions/Tensions`, even when the entries are brief.
- Use `Integration target` in `Model Delta` for the pages or questions the
  source warrants. Use `Integration Notes` for the work actually completed, so
  finished source pages do not read like open todo lists.
- For Shinzen primary teaching talks, preserve the teaching move before
  abstracting it: what he asks the practitioner to notice, do, stop doing, or
  re-understand. Use `Model Delta` as a model/practice delta when a talk
  changes routing, technique choice, phenomenological discrimination, safety,
  service, or teaching posture.

---

## source

One-to-one interface between a raw file and the compiled wiki.

```markdown
---
type: source
thesis: "[What this source claims or contains, and why it matters.]"
status: working
domain: [primary]
importance: 5
confidence: established
tags: []
aliases: []
sources: [raw/filename.ext]
load_when: "[When source-level evidence from this raw file matters.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

[One sentence locating the source: origin, author, date, format, and scope.]

## Source Snapshot
- **Path**: `raw/filename.ext`
- **Origin**: [author, publisher, organization, URL, or internal source]
- **Date**: [publication or creation date]
- **Format**: [article, paper, transcript, memo, dataset, book chapter]
- **Reliability**: [primary, secondary, tertiary; agenda, bias, limits]
- **Scope**: [what it covers and what it does not cover]

## Key Claims
- **S1**: [Claim stated by the source.]
- **S2**: [Claim stated by the source.]
- **S3**: [Inference from the source, marked as inference.]
- **S4**: [Claim that contradicts or updates an existing page.]

## Summary
[Faithful 1 to 3 paragraph compression of the source.]

## Source Frame
[Separate what the source observes from what it interprets. State what the
source wants the reader to believe, what assumptions or incentives shape that
frame, what it omits, and what a strong critic would challenge.]

## Model Delta
- **Confirmed**: [Existing page, claim, or model this source strengthens.]
- **Changed**: [Existing page, claim, or model this source revises.]
- **Challenged**: [Existing page, claim, or model this source pressures.]
- **No material change**: [What the source adds without changing the current model.]
- **Integration target**: [Pages, index/dashboard, or questions warranted by the source; record completed work in Integration Notes.]

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
- **Confidence changes**: [what shifted and why]
- **Low-signal material excluded**: [what was left out deliberately]

## Related
- [[Page]] - why this source bears on it
```

---

## source - YouTube lecture

Use for Shinzen teaching transcripts, especially oral talks, Q&A, live
coaching, advanced maps, warnings, lineage translations, guided practice, or
service teachings. Keep the required source audit spine, but center the
compiled value on transmission fidelity and practice reasoning.

```markdown
---
type: source
thesis: "[What this talk teaches and why it matters for Shinzen's system.]"
status: working
domain: [sources, primary]
importance: 5
confidence: established
tags: []
aliases: ["[Talk title] (YouTube)", "[video_id]"]
sources: [raw/Shinzen Sources/yt transcripts/[canonical-file].md]
load_when: "[When this talk's teaching move, practice handle, or source-level evidence matters.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

[One or two sentences locating the talk, its register, and its central
teaching contribution.]

## Source Snapshot
- **Path**: `raw/Shinzen Sources/yt transcripts/[canonical-file].md`
- **Origin**: Shinzen Young YouTube talk, URL or video ID.
- **Date**: [upload date if known, otherwise unknown]
- **Format**: YouTube transcript; note whether root, edited, or retranscribed.
- **Reliability**: Primary evidence for Shinzen's teaching, idiolect, and
  practice routing; calibrate transcript quality and any non-practice claims.
- **Scope**: [What the talk covers and what it does not cover.]

## Teaching Register
[Instruction, Q&A, live coaching, advanced map, warning, lineage translation,
confession, speculative analogy, guided practice, or service teaching. State
how the oral setting shapes interpretation.]

## Why This Talk Matters
[The durable value for future practice reasoning, phenomenological
discrimination, teaching transmission, safety, or service.]

## Key Claims
- **S1**: [Precise claim, instruction, distinction, warning, or routing move.]
- **S2**: [Practice handle or phenomenological distinction.]
- **S3**: [Idiolect, phrase, analogy, or teaching posture worth preserving.]

## Load-Bearing Teaching Moves
- **S1**: [Why this claim, instruction, distinction, warning, or routing move is load-bearing.]
- **S2**: [What this practice handle or phenomenological distinction changes.]
- **S3**: [Why this idiolect, analogy, or teaching posture should be preserved.]

## Practice Handles
[What a practitioner or guide could actually do differently because of this
talk.]

## Summary
[Faithful 1 to 3 paragraph compression of the talk.]

## Source Frame
[Separate Shinzen's observed instructions from interpretation, analogy,
scientific/metaphysical extension, or oral emphasis. State what the talk is
trying to make possible for practice.]

## Model Delta
- **Practice handle added/sharpened**: [Technique, distinction, or routing move.]
- **Confirmed**: [Existing page, claim, or model this talk strengthens.]
- **Changed**: [Existing page, claim, or model this talk revises.]
- **Challenged**: [Existing page, claim, or model this talk pressures.]
- **Transmission note**: [Voice, idiolect, analogy, or live-teaching move to preserve.]
- **Integration target**: [Pages, index/dashboard, or questions warranted by the talk; record completed work in Integration Notes.]

## Weakest Claims
- [Broad, under-supported, overcompressed, speculative, or source-limited claims.]

## Important Omissions
- [Missing safety, dosage, context, sequence, clinical, ethical, or practice-readiness detail.]

## Contradictions/Tensions
- [Internal tensions, conflicts with existing pages, or interpretive pressure points.]

## Easily Misused Claims
- [Where reverence, metaphysics, science analogy, no-self, Source, powers,
  intensity, teacher authority, or service language could go wrong.]

## Integration Notes
- **Pages created**: [[Page]]
- **Pages updated**: [[Page]]
- **Teaching-transmission pages affected**: [[Page]]
- **Contradictions opened**: [[Question or Thesis]]
- **Confidence changes**: [what shifted and why]
- **Low-signal material excluded**: [what was left out deliberately]

## Related
- [[Page]] - why this talk bears on it
```

---

## entity

A real-world thing that recurs, anchors claims, or changes routing.

```markdown
---
type: entity
thesis: "[What this entity is and why it matters here.]"
status: seed
domain: [primary]
importance: 5
confidence: probable
tags: []
aliases: []
sources: [raw/source.md]
load_when: "[Routing cue.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

[One or two sentence definition and role.]

## Key Points
- **Core claim**: [What matters most about this entity.]
- **Why this matters**: [What changes downstream.]
- **Key tensions**: [Conflicts, uncertainty, or none.]
- **Source posture**: [How strong or limited the evidence is.]

## Profile
[Aggregated account across sources. Distinguish observed facts, source
claims, and inferences.]

## Relationships
- [[Page]] - [relationship and why it matters]

## Boundaries
[What this page does not cover, adjacent entities, and common confusions.]

## Related
- [[Page]] - [semantic edge]
```

---

## concept

A reusable abstraction, mechanism, distinction, pattern, or term.

```markdown
---
type: concept
thesis: "[Single-sentence definition plus why this concept is load-bearing.]"
status: seed
domain: [primary]
importance: 5
confidence: probable
tags: []
aliases: []
sources: [raw/source.md]
load_when: "[Questions or pages that need it.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

[Plain-language definition in one or two sentences.]

## Key Points
- **Core claim**: [What the concept explains.]
- **Why this matters**: [What future reasoning it improves.]
- **Key tensions**: [Where it breaks, competes, or gets misused.]
- **Source posture**: [Evidence strength and limits.]

## Model
[The mechanism, distinction, causal chain, taxonomy, or state model.]

## Boundaries
[Adjacent concepts, scope conditions, counterexamples, failure modes.]

## Implications
[What follows if this concept is right.]

## Related
- [[Page]] - [boundary, dependency, or application]
```

---

## thesis

An argued position. The wiki is making a claim, so evidence and
counter-considerations are mandatory.

```markdown
---
type: thesis
thesis: "[The argument in one sentence.]"
status: working
domain: [primary, secondary]
importance: 7
confidence: probable
tags: []
aliases: []
sources: [raw/source-a.md, raw/source-b.md]
load_when: "[Routing cue.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

[One or two sentences setting the claim and stakes.]

## Key Points
- **Core claim**: [Thesis compressed.]
- **Why this matters**: [What it changes.]
- **Key tensions**: [Counter-considerations.]
- **Source posture**: [Evidence base and confidence.]

## Argument
[Full case, grouped by claim rather than source order.]

## Evidence
- **E1**: [Evidence and citation to source page or source claim.]
- **E2**: [Evidence and citation.]

## Counter-Considerations
[Strong rival interpretations, missing evidence, or contradictions.]

## What Would Change The Model
[Concrete evidence that would lower, raise, or contest confidence.]

## Related
- [[Page]] - [support, rivalry, dependency, or boundary]
```

---

## synthesis

A map of a domain or cluster. Do not create one without a through-line.

```markdown
---
type: synthesis
thesis: "[What this synthesis maps and the through-line that holds it together.]"
status: working
domain: [primary]
importance: 8
confidence: probable
tags: []
aliases: []
sources: []
load_when: "[Routing cue.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

[One paragraph naming the territory, through-line, and limits. If
`sources: []`, explicitly state which compiled pages this synthesis depends
on.]

## Key Points
- **Core claim**: [Through-line.]
- **Why this matters**: [What it makes easier to understand.]
- **Key tensions**: [Unresolved contradictions or boundaries.]
- **Source posture**: [Direct sources or compiled-page dependency.]

## Landscape
- **Sub-area A** ([[Page]], [[Page]]) - [what this cluster contributes]
- **Sub-area B** ([[Page]]) - [what this cluster contributes]

## Through-Line
[The organizing argument. If this becomes a list, stop and re-distill.]

## Tensions And Frontiers
- [[Question]] - [why it matters]

## Dependencies
- [[Page]] - [why this page is part of the synthesis]

## Related
- [[Page]] - [adjacent synthesis, concept, thesis, or question]
```

---

## analysis

A reusable answer to a query, comparison, or investigation.

```markdown
---
type: analysis
thesis: "[Question plus conclusion in one sentence.]"
status: working
domain: [primary]
importance: 5
confidence: probable
tags: []
aliases: []
sources: [raw/source.md]
load_when: "[Routing cue.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

**Question:** [Original or normalized question.]

**Answer:** [One or two sentence answer.]

## Key Points
- **Core claim**: [Answer compressed.]
- **Why this matters**: [What it resolves.]
- **Key tensions**: [Limits or alternatives.]
- **Source posture**: [Evidence quality.]

## Reasoning
[Steps from question to answer. Cite evidence and distinguish inference.]

## Confidence And Limits
[What is known, missing, contested, or speculative.]

## Filing Notes
[Why this answer was durable enough to file.]

## Related
- [[Page]] - [used in answer, resolved question, or adjacent analysis]
```

---

## question

A durable open frontier. Questions are first-class wiki pages.

```markdown
---
type: question
thesis: "[Precise question plus why answering it matters.]"
status: seed
domain: [primary]
importance: 5
confidence: speculative
tags: []
aliases: []
sources: []
load_when: "[Routing cue.]"
best_linked_pages: ["[[Page]]", "[[Page]]"]
updated: YYYY-MM-DD
---

**Question:** [Precise form of the question.]

**Why it matters:** [What changes downstream if this is answered.]

## Key Points
- **Core claim**: [What gap or contradiction this page tracks.]
- **Why this matters**: [What future reasoning depends on it.]
- **Key tensions**: [Competing hypotheses or evidence gaps.]
- **Source posture**: [What evidence exists and what is missing.]

## What We Know
- [[Page]] - [how it bears on the question]

## Competing Hypotheses
- **Hypothesis A**: [Claim and support.]
- **Hypothesis B**: [Claim and support.]

## Evidence Needed
- **Evidence type**: [Specific evidence that would move confidence.]

## Dependencies
- [[Page]] - [how this page would change if answered]

## Status
Open. Link a resolving `analysis`, `thesis`, or `synthesis` when one exists.

## Related
- [[Page]] - [adjacent question, concept, or thesis]
```
