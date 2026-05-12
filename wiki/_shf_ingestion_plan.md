# SHF Ingestion Plan

Durable queue for focused ingestion of `raw/Shinzen Sources/SeeHearFeelIntroduction_ver1.8.pdf`.

Use this when the user says: "run next in SHF ingestion plan".

## Run-Next Rule

1. Read `AGENTS.md`, `wiki/index.md`, recent `wiki/log.md`, `wiki/_operations.md`, and `wiki/_templates.md`.
2. Open this plan and choose the first unit whose status is `pending`.
3. Read only that unit file, the listed owner pages, and the original PDF only when extraction/layout needs verification.
4. Ingest exactly one unit in the normal `ingest` workflow:
   - Create exactly one `type: source` page for that unit raw file.
   - Use local source claim IDs such as `S1`, `S2`, `S3`.
   - Include `Weakest Claims`, `Important Omissions`, `Contradictions/Tensions`, and `Model Delta`.
   - Update only the owner pages warranted by that unit.
   - Update `wiki/index.md` only for new compiled source pages or meaningful routing changes.
   - Append one `wiki/log.md` entry.
5. Mark the unit status in this plan as `done` and add the resulting source page name.
6. Run `tools\wiki_lint.cmd`; report the expected staged-source errors and any new target errors.

Do not ingest the original PDF as one source page while this plan is active. The source-unit files are the ingestable raw sources; the PDF remains the verification parent.

## Unit Queue

| Status | Unit | Raw file | Intended source page | Primary delta | Owner pages |
|---|---:|---|---|---|---|
| done | 01 | `raw/Shinzen Sources/see-hear-feel-introduction/01-source-frame-and-happiness-rationale.md` | `[[See Hear Feel Introduction - Source Frame and Happiness Rationale]]` | SHF rationale through total happiness, focus range, and applied situations. | `[[Total Happiness]]`, `[[Practice Cycles]]`, `[[Mindfulness Skill Triad]]` |
| done | 02 | `raw/Shinzen Sources/see-hear-feel-introduction/02-cce-and-labeling-as-skill-support.md` | `[[See Hear Feel Introduction - CCE and Labeling as Skill Support]]` | Label pace, wording, and equanimity voice as concrete CCE support. | `[[Mindfulness Skill Triad]]`, `[[Noting]]`, `[[Equanimity]]` |
| done | 03 | `raw/Shinzen Sources/see-hear-feel-introduction/03-simple-and-flexible-labels.md` | `[[See Hear Feel Introduction - Simple and Flexible Labels]]` | Modern flexible labeling: `See`, `Hear`, and `Feel` change meaning by focus range. | `[[Noting]]`, `[[Sensory Grid]]`, `[[Sensory Clarity]]` |
| done | 04 | `raw/Shinzen Sources/see-hear-feel-introduction/04-starting-focus-ranges.md` | `[[See Hear Feel Introduction - Starting Focus Ranges]]` | Standardized beginner entry through Focus on See, Hear, Feel, and Everything. | `[[Sensory Grid]]`, `[[Noting]]`, `[[Basic Mindfulness Practice Architecture]]` |
| done | 05 | `raw/Shinzen Sources/see-hear-feel-introduction/05-four-okays-and-required-vs-allowed.md` | `[[See Hear Feel Introduction - Four Okays and Required vs Allowed]]` | Minimum correct practice, anti-perfectionism, and optional intensification. | `[[Noting]]`, `[[Complete Experience Safety Boundary]]`, `[[Equanimity]]` |
| done | 06 | `raw/Shinzen Sources/see-hear-feel-introduction/06-five-themes-space-and-depth-boundary.md` | `[[See Hear Feel Introduction - Five Themes Space and Depth Boundary]]` | Adds Space/Spaciousness and frames clarity-depth integration. | `[[Sensory Grid]]`, `[[Focus on Rest]]`, `[[Calming-Clarifying Balance]]` |
| done | 07 | `raw/Shinzen Sources/see-hear-feel-introduction/07-noting-nutshell-and-faq.md` | `[[See Hear Feel Introduction - Noting Nutshell and FAQ]]` | Noting mini-manual: modes, emphasis, re-noting, zooming, stance, Gone, FAQ. | `[[Noting]]`, `[[Gone]]`, `[[Practice Guidance Toolkit]]` |
| done | 08 | `raw/Shinzen Sources/see-hear-feel-introduction/08-practice-organization-and-system-transition.md` | `[[See Hear Feel Introduction - Practice Organization and System Transition]]` | Practice rhythm and old Basic Mindfulness to new Unified Mindfulness transition. | `[[Practice Cycles]]`, `[[Nurture Positive]]`, `[[Basic Mindfulness Practice Architecture]]` |

## Intended Ingest Sequence

Run the units in queue order. Although Unit 03 has the largest conceptual delta, Unit 01 should go first because it establishes the source frame, page-level provenance, and the SHF rationale that later unit pages can cite.

## Integration Guardrails

- Keep each session to one unit unless the user explicitly requests batching.
- Treat the source as primary evidence for Shinzen's Unified Mindfulness teaching frame, not as clinical, historical, or empirical proof.
- Preserve the old/new-system tension: the new SHF interface simplifies and extends the old grid, while the old bisyllabic labels remain valid shorthand and optional practice labels.
- Do not create a standalone `[[Spaciousness]]` page until Unit 06 shows that the concept needs independent routing beyond `[[Sensory Grid]]`.
- `[[See Hear Feel]]` was created after Unit 08 as the compact route for the completed SHF interface; earlier units remain integrated through `[[Noting]]` and `[[Sensory Grid]]`.
