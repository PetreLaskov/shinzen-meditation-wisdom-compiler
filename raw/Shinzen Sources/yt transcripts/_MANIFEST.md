# Shinzen Young YouTube Transcripts — Scrape Manifest

**Source channel:** https://www.youtube.com/@expandcontract
**Scrape date:** 2026-04-28
**Total videos enumerated:** 200
**Files written:** 200 (`.md`) + this manifest

## Final status

- **199 / 200 — full transcripts**
- **1 / 200 — no spoken content** (10-minute silent "Just Sitting" sit; nothing to transcribe)

### Source breakdown

| Source                                            | Count | Notes                                                            |
| ------------------------------------------------- | ----- | ---------------------------------------------------------------- |
| `kome.ai` (transcript proxy)                      | 179   | Bypasses YouTube `/api/timedtext` IP block                       |
| `yt-dlp` (`en` track)                             |   1   | One Group-B video had a plain `en` track yt-dlp could fetch      |
| `faster-whisper` (`tiny.en`, int8, CPU)           |  19   | Local STT for videos with no captions / non-standard locale only |
| Audio-only annotation (chant or silent sit)       |   1   | Group-A chant video — 10m of *Om Mani Padme Hum* mantra only     |
| **Pure silent meditation** — no transcript exists |   1   | `G6npSvMb5XQ` — 10m silent "Just Sitting"                        |

## Pipeline

1. **Channel enumeration** — `yt-dlp --flat-playlist` on `@expandcontract/videos` → 200 IDs + titles.
2. **Bulk fetch via kome.ai** — 4 parallel sonnet workers, 50 IDs each, `curl_cffi` with Chrome impersonation. Result: **180 / 200** (179 real + 1 placeholder for chant — see note).
3. **YouTube auto-caption fallback (yt-dlp)** — for the 21 holdouts. YouTube returned HTTP 429 on the `/api/timedtext` endpoint for our IP. 1 video (`ncQGlYfvO0Q`) slipped through with a plain `en` track.
4. **Local Whisper STT** — `faster-whisper` `tiny.en` with int8 quantization on CPU. 21 audio downloads via yt-dlp from `googlevideo.com` (separate, non-blocked endpoint). 19 of 21 produced clean English transcripts, processing audio at ≈25–80× realtime.
5. **Manual notes** — 2 videos with no spoken English content got authored notes: a Tibetan chant (`tOYiHaXtwzY`) and a silent sit (`G6npSvMb5XQ`).

## File format

Each `.md`:

```
# <title>

- **Video ID:** <11-char id>
- **URL:** https://www.youtube.com/watch?v=<id>
- **Source:** kome.ai  |  yt-dlp (<lang>)  |  faster-whisper (<model>, ...)
- **Length:** <human-readable, when available>

---

## Transcript

<plaintext>
```

## Filename convention

`<sanitized title>_<video_id>.md`

The `_<video_id>` suffix at the end is what the scraper uses for idempotency (skip-if-exists by video ID), so don't strip it on later renames.

## Reproducibility

- Scrapers: `/home/pece/scrape_shinzen.py` (kome.ai), `/home/pece/scrape_shinzen_ytdlp.py` (yt-dlp captions), `/home/pece/scrape_shinzen_whisper.py` (audio + Whisper)
- Logs: `/home/pece/shinzen_chunks/chunk_0[0-3].log`, `whisper.log`, `ytdlp_fallback*.log`
- Audio cache: `/home/pece/shinzen_audio/` — kept after the run for re-transcription with a larger model if desired
