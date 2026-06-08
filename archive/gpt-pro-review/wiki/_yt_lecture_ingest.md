# YouTube Lecture Ingest Method

This note governs Shinzen YouTube lecture ingestion after the completed
book/manual/SHF first-pass compile. It supersedes the older raw handoff plan
as workflow guidance without editing that raw file.

For execution order, gate boundaries, and synthesis checkpoints, use
`wiki/_yt_ingestion_implementation_plan.md`. This file defines method; the
implementation plan defines sequence.

## Purpose

The YouTube lectures are primary teaching artifacts, not just transcript
sources. Their durable value often lies in Shinzen's teaching move: the
distinction he reaches for, the practice handle he gives, the warning he
inserts, the analogy he chooses, and the live way he routes confusion,
intensity, no-self, Source, behavior, or service.

For these talks, preserve transmission fidelity before abstraction. Compile
what the teaching asks a practitioner to notice, do, stop doing, or
re-understand. Then calibrate empirical, clinical, metaphysical, historical,
scientific, and comparative claims separately.

## Current Calibration

Before running the main implementation plan, run the calibration pre-wave so
the compiler learns Shinzen's oral teaching posture:

1. `raw/Shinzen Sources/yt transcripts/Shinzen Young ~ My Primary Mission A Deep, Broad, and Subtle Formulation_HcEidBghfOA.md`
2. `raw/Shinzen Sources/yt transcripts/What are your specialties as a teacher ~ Shinzen Young_ilBcFuRNszA.md`
3. `raw/Shinzen Sources/yt transcripts/Three Reasons Why Shinzen Young is a Lousy Teacher_JPkA9oMPKDw.md`
4. `raw/Shinzen Sources/yt transcripts/edited/Towards a Balanced Enlightenment ~ Shinzen Young_wgvr-f0p0Ms.md`
5. `raw/Shinzen Sources/yt transcripts/Do Nothing Meditation ~ Shinzen Young_cZ6cdIaUZCA.md`

The fifth item should become the revised YouTube source-page pilot. The first
four should tune the wiki toward precision, oral teaching, master-level
practice discrimination, anti-guru-inflation, vulnerability, feedback,
interactive coaching, and behavior/service accountability.

## Source Page Method

Create exactly one `type: source` page per substantive video. Use the
`source - YouTube lecture` scaffold in `wiki/_templates.md`.

For each lecture, extract:

- Teaching register: instruction, Q&A, live coaching, advanced map, warning,
  lineage translation, confession, speculative analogy, guided practice, or
  service teaching.
- Load-bearing teaching moves with local claim IDs.
- Practice handles: what a practitioner or guide could do differently.
- Phenomenological distinctions: what becomes easier to notice or parse.
- Routing moves: when to switch technique, widen/narrow range, turn toward,
  turn away, add support, or preserve ordinary action.
- Transmission notes: Shinzen idiolect, phrases, analogies, tone, or
  teaching posture worth future reuse.
- Easily misused claims: reverence, metaphysics, science analogy, no-self,
  Source, powers, intensity, teacher authority, or service language.

Keep the required audit spine: `Model Delta`, `Weakest Claims`, `Important
Omissions`, and `Contradictions/Tensions`. In lecture source pages, interpret
`Model Delta` as model/practice delta.

## Page Allocation

Derived pages are warranted when a recurring Shinzen-specific teaching handle
improves future practice reasoning. Prefer local Shinzen idiolect over generic
Buddhist, psychological, or scientific terms when the local phrase is the
actual practice router.

Expected Teaching Transmission pages include, when supported by ingested
sources:

- `[[Shinzen's Teaching Method]]`
- `[[Operational Enlightenment]]`
- `[[Classical Enlightenment]]`
- `[[Teaching A Path]]`
- `[[Practice Description as Service]]`
- `[[Mastery Without Guru Inflation]]`

Do not create these all at once. Create the first one when a talk gives it
enough independent routing value.

## Series Strategy

Use one source page per video in a series. After two or more videos in a
series are ingested, update the owner concept or synthesis page. Create a
series synthesis only if the sequence itself teaches a progression that would
be lost in isolated source pages.

## Integration Order

For each lecture:

1. Create or update the source page.
2. Update owner pages before creating new pages.
3. Add or revise Teaching Transmission pages only when they improve routing.
4. Update `wiki/index.md`, including the Teaching Transmission domain when a
   page belongs there.
5. Append one batched `wiki/log.md` entry for a calibration wave or series
   wave.
6. Run `tools\wiki_lint.cmd`.

## Raw Plan Status

`raw/Shinzen Sources/yt transcripts/_PLAN-FOR-INGESTING.md` remains a useful
historical curation artifact and transcript-quality handoff. It is stale as a
workflow authority because the current wiki now has a local `[[Current
Model]]`, a completed SHF introduction compile, and a retuned
teaching-transmission posture. Use `wiki/_yt_lecture_ingest.md` for method
and `wiki/_yt_ingestion_implementation_plan.md` for execution order.
