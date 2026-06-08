# YouTube Retreat Stream Transcript Scrape Plan

This plan covers the long retreat video stream playlist supplied on
2026-05-18:

`https://www.youtube.com/watch?v=kfU_XjT32Yg&list=PLjRQFjS1OrSy3q69a9femKVKH1SiywGwu`

It extends, but does not replace, `wiki/_yt_lecture_ingest.md` and
`wiki/_yt_ingestion_implementation_plan.md`. The existing channel transcript
corpus was compiled from `@expandcontract/videos`; this playlist should be
treated as a new source-acquisition target until enumeration proves overlap.

## Aim

Acquire durable, provenance-rich transcripts for Shinzen's long retreat
streams without turning the wiki into a transcript archive. The scrape should
produce stable raw transcript files and a manifest. Ingestion remains
separate: one source page per substantive video, owner-page updates only where
the retreat streams improve practice routing, phenomenological
discrimination, safety, service, or teaching transmission.

## Planning-Time Local State

- The existing YouTube corpus manifest is
  `raw/Shinzen Sources/yt transcripts/_MANIFEST.md`, scraped 2026-04-28 from
  `https://www.youtube.com/@expandcontract`.
- No local raw or wiki file currently mentions playlist
  `PLjRQFjS1OrSy3q69a9femKVKH1SiywGwu` or video `kfU_XjT32Yg`.
- `yt-dlp` and `ffmpeg` are not currently on PATH in this Windows workspace.
- Plain `python` is not on PATH, but `py` exists and the Codex bundled Python
  is available at
  `C:\Users\Urgen\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.
- Public web search/open did not expose reliable playlist metadata in this
  session, so enumeration should be the first networked implementation step.

## Applied Acquisition Status - 2026-05-18

The acquisition phase has been applied. `tools/scrape_retreat_stream_transcripts.py`
installed and used scratch-local dependencies under
`C:\tmp\shinzen_retreat_stream_scrape\pydeps`, enumerated the playlist with
`yt-dlp`, wrote the manifest at
`raw/Shinzen Sources/yt transcripts/retreat streams/_MANIFEST.md`, and
created six new transcript files in the same folder.

Enumeration found seven videos. One was already covered by the existing
`@expandcontract` corpus: `0ifHks5EYZU`, `What to Expect and Do After a
Mindfulness Retreat`. Five missing items had YouTube auto captions and are
quality `B`. One item, `TKqJL3AroLc`, had no English caption or auto-caption
track and was transcribed locally with `faster-whisper tiny.en` on CPU with
VAD; it is quality `C`.

The transcript files now awaiting source-page ingest are:

- `raw/Shinzen Sources/yt transcripts/retreat streams/Shinzen Young Retreat at the Monastic Academy 05.27.2017_kfU_XjT32Yg.md`
- `raw/Shinzen Sources/yt transcripts/retreat streams/Shinzen Young Day-Long Retreat at the Monastic Academy - July 22, 2017_TKqJL3AroLc.md`
- `raw/Shinzen Sources/yt transcripts/retreat streams/Four Ways Forward (June Shinzen Retreat)_DzmdDcvqK0A.md`
- `raw/Shinzen Sources/yt transcripts/retreat streams/Shinzen April Daylong Retreat Four Quadrant Training_3odXCN29SBc.md`
- `raw/Shinzen Sources/yt transcripts/retreat streams/Appreciate the Senses, Transcend the Self, Express the Source_hnyl4qYY8V8.md`
- `raw/Shinzen Sources/yt transcripts/retreat streams/GUIDED MEDITATION of EXPANSION & CONTRACTION ~ by SHINZEN YOUNG_pg6PTbZ9hDw.md`

Spot checks sampled first, middle, and late transcript lines. The quality-B
files are adequate for routing and triage but have auto-caption errors,
especially specialist terms, names, chants, and quiet/silent practice
periods. The quality-C STT file is usable only with stronger source-page
spot checks against the audio before exact citation.

## Target Raw Layout

Use the existing YouTube transcript tree so lint can continue to deduplicate
by 11-character video ID:

```text
raw/Shinzen Sources/yt transcripts/retreat streams/
  _MANIFEST.md
  <sanitized title>_<video_id>.md
```

Use scratch space outside `raw/` for VTT files, audio downloads, JSON output,
logs, and failed attempts:

```text
C:\tmp\shinzen_retreat_stream_scrape\
```

Only the final curated `.md` transcript files and `_MANIFEST.md` belong in
`raw/`. Do not place intermediate `.vtt`, `.json`, `.m4a`, or logs in `raw/`
unless a later decision makes one of them a cited source artifact.

## Transcript File Format

Each final transcript file should keep the established corpus shape and add
retreat-stream fields:

```markdown
# <title>

- **Video ID:** <11-char id>
- **URL:** https://www.youtube.com/watch?v=<id>
- **Playlist:** PLjRQFjS1OrSy3q69a9femKVKH1SiywGwu
- **Playlist position:** <n if known>
- **Source:** youtube captions | youtube auto captions | faster-whisper (<model>, <device>, <compute>)
- **Length:** <duration if known>
- **Scrape date:** YYYY-MM-DD
- **Transcript quality:** A | B | C | D
- **Notes:** <caption availability, silence, attribution, failures, or caveats>

---

## Transcript

[00:00:00] <text when timestamps are available>
```

For long retreat streams, preserve coarse timestamps. They are worth the
extra tokens because they make source audit, spot checks, and future excerpt
navigation possible.

## Quality Tiers

- **A - official or human-edited captions**: ingest-ready after light
  formatting and spot checks.
- **B - YouTube auto captions**: usable for practice routing, but mark exact
  wording and specialist vocabulary as transcript-limited.
- **C - local STT fallback**: usable only after sample audit. Prefer
  silence-aware transcription, and watch for hallucinated speech in quiet
  retreat periods.
- **D - no usable transcript**: create a manifest row only, or a brief raw
  note if the video is silent, chant-only, inaccessible, private, deleted, or
  not Shinzen-primary.

## Acquisition Sequence

1. **Enumerate the playlist.** Install or locate `yt-dlp`, then run a
   flat-playlist enumeration into scratch. Capture video ID, title, duration,
   uploader/channel, availability, and playlist position. Write a curated
   `_MANIFEST.md` before transcript fetching.
2. **Deduplicate.** Compare enumerated IDs against existing files under
   `raw/Shinzen Sources/yt transcripts/` and aliases/source paths in `wiki/`.
   Reuse existing canonical transcripts where they exist; do not create
   duplicate raw files for the same video ID.
3. **Caption-first fetch.** For each missing ID, try listed English subtitles
   and auto-captions before downloading audio. Convert captions to the final
   Markdown format with timestamps and metadata.
4. **Local STT fallback.** For videos without usable captions, download best
   audio to scratch and transcribe locally with `faster-whisper` or another
   local Whisper backend. Use VAD or silence filtering where possible because
   retreat streams may contain long sits.
5. **Spot-check quality.** For each long stream, sample the first speech
   segment, one middle segment, one late segment, and any dense Q&A section.
   Record obvious vocabulary or attribution problems in the transcript notes
   and manifest.
6. **Normalize and freeze raw files.** Write final transcript Markdown files
   only after the source, quality tier, duration, and caveats are known.
   Afterward, treat them as immutable evidence.
7. **Triage for ingestion.** Do not ingest the whole playlist blindly. Rank
   videos by practice-routing value, retreat-specific instruction, Q&A
   density, safety material, and novelty relative to existing owner pages.
8. **Pilot ingest one stream.** Apply `wiki/_yt_lecture_ingest.md` and the
   YouTube source-page scaffold from `wiki/_templates.md` to the highest-value
   stream. Decide after the pilot whether the playlist needs a series
   synthesis or only individual source pages plus owner-page updates.

## Implementation Notes

- Networked dependency setup will probably require user approval in this
  sandboxed Codex session.
- Prefer commands and scripts that are idempotent by video ID. Existing
  filename convention depends on the final `_<video_id>.md` suffix.
- Avoid Kome or other transcript proxy services unless direct captions and
  local STT both fail or prove much worse; the old corpus used Kome because
  YouTube timed-text access hit HTTP 429.
- Do not use browser scraping for transcript text unless tool-based caption
  and STT paths fail. Browser scraping is brittle and weaker for provenance.
- Do not use account cookies unless the user explicitly provides them and the
  video is legitimately accessible to the user.
- Do not download or retain full videos in the repo. Keep audio/video
  intermediates in scratch only when needed for transcription or audit.

## Ingestion Gate

Before the first retreat stream source page is created, the workspace should
have:

- A playlist `_MANIFEST.md` with video IDs, titles, duration, availability,
  source path or failure status, and quality tier.
- At least one completed transcript file in the target raw layout.
- A quality note proving whether captions or local STT are adequate for this
  playlist.
- A dedupe report showing overlap or non-overlap with the existing 2026-04-28
  YouTube corpus.

After each ingestion wave, follow the existing per-gate output contract:
source pages, owner-page updates, one synthesis/thesis/question update only
when warranted, `wiki/index.md`, `wiki/log.md`, and `tools\wiki_lint.cmd`.

For the sequential ingest order, decomposition policy, and pilot/source-page
sequence, use `wiki/_yt_retreat_stream_ingestion_plan.md`.
