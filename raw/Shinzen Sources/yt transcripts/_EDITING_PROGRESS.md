# YT Transcripts — Prep Status & Handoff

Working state of the YouTube transcript corpus prep, for the next session. **Ingestion is the next phase, not done yet.** All work below stays in `raw/yt transcripts/` and its `edited/` subdir; nothing has entered `wiki/` yet.

---

## Audit findings (do NOT re-do)

**Corpus**: 200 content transcripts (+ 1 `_MANIFEST.md`, 1 `_whisper_failures.log`). All schema-clean: `# title`, metadata block (Video ID / URL / Source / Length), `---`, `## Transcript`. Filenames consistently `<title>_<11-char videoID>.md`. No duplicate IDs. 52 multi-part series — must ingest as units.

**Two transcription sources, three quality tiers:**

- **`kome.ai`** — 178 files (~88%). Quality varies by audio conditions:
  - ~33% **CLEAN** (paragraphed, punctuated, ingest-ready as-is — no editing needed)
  - ~40% **RAW-OK** (run-on prose but readable; needs punctuation+paragraphing pass)
  - ~23% **RAW-DEGRADED** (run-on + ASR errors on Buddhist/Sanskrit/Pali vocab)
  - ~4% **BROKEN** (severely garbled — re-transcribe)
- **`faster-whisper (tiny.en, int8, CPU)`** — 19 files. **Tier-C: must re-transcribe before any ingestion attempt.** tiny.en systematically mangles Sanskrit/Pali/Tibetan/Vietnamese/Hebrew/Sufi vocabulary and Asian proper names (e.g. *Yogācāra* → "yoga vichara"; Thich Thien-An → "Dr. Tae-Tae-Tae-Tae-Tae-Tae"; *Shingon monk* → "shingling monk").
- **Edge cases**: 3 legitimately silent/chant-only (Om Mani sit, Just Sitting silent, Pali chant unrecoverable); 1 Spanish-only (Noche Oscura recitation); 7 header-only placeholder stubs.

**Vocab error density (kome.ai average)**: ~0.36 mangled technical terms per transcript, spiking to 4–6 on cross-traditional talks (Sufi/Hebrew/Japanese vocabulary). 30–60 minutes of LLM-assisted editing per RAW transcript reaches ingestion quality.

**Curation findings — 4 new wiki pages clearly warranted from corpus alone:**
1. `[[Expansion and Contraction]]` (E-C) — biggest existing wiki gap; 9+ transcripts including 4-part series
2. `[[Discrimination and Unification]]` — 4-part series; bridges Sensory Clarity ↔ Return to the Source
3. `[[Enlightenment (Operational Definition)]]` — 10+ transcripts collectively articulate the operational meaning
4. `[[DPDR and the Pit of the Void]]` — clinical-vs-classical Dark Night differential

**3 additional new pages probable** with full ingestion: `[[Ten Ox-Herding Pictures]]`, `[[Bodhicitta and the Way of Service]]`, expansion of `[[Sensory Grid]]` to ground in classical 6-consciousness model.

**`[[Self-Inquiry]]`** (currently 🌱 stub) gets promoted to 🌿 from a single transcript.

**Non-Shinzen-primary content to defer**: 4 Har-Prakash Khalsa standalone training-module files; the Khalsa+Mertz+Young 3-way time conversation (Shinzen contributions can be extracted but the others should not be ingested as primary). Listed separately at end.

---

## What's been done — editorial wave summary

**55 of 56 dispatched files written** to `edited/` across 4 waves. Method: Sonnet sub-agents with distilled `/enhance-transcript` prompts + Buddhist-vocab correction dictionary, writing direct to disk and returning only short status to keep parent context lean. Originals untouched in `raw/yt transcripts/`. All files preserve the metadata block byte-identical and add a `*Lightly edited from raw kome.ai output...*` editor's-note line above `## Transcript`.

**Verified ratios** (raw → edited size): all in 1.00–1.08 range. No paraphrasing — only punctuation, paragraphing, and named-entity / Sanskrit-Pali-Tibetan vocabulary corrections.

### Edited files (55) — all in `raw/yt transcripts/edited/`

**Wave 1 (8 files)** — top priority anchors for new wiki pages:
- Expansion and Contraction - Part 1 Kenotic Christianity and Shuniya
- Born Between Expansion and Contraction *(was RAW-DEGRADED — 22 fixes)*
- Classic Dark Night or Clinical Issues
- Enlightenment, DPDR & Falling Into the Pit of the Void
- Self-Enquiry & Mindfulness Meditation
- 6 Buddhist Consciousnesses & the 12 Sensory States
- Humility to the Vanishing Point No Self Around the World *(was RAW-DEGRADED — 28 fixes; `fanat`→`fanāʾ` ×5, `me-ayin`, `bittul ha-yesh`, etc.)*
- Discrimination and Unification - Part 1 of 4

**Wave 2 (16 files)** — multi-part series completion + standalones:
- Expansion and Contraction Pts 2, 3, 4 of 4
- Discrimination and Unification Pts 2, 3, 4 of 4
- Depth & Breadth of Concentration Pts 1, 2, 3 of 3
- Bodhicitta and the Bodhisattva Ideal
- The Absolute Witness
- Non-Dual Awareness
- Sasaki Roshi & Burmo-Japanese Mindfulness Fusion
- Sasaki Roshi, the Complex Number System & the Source of Love
- The Trickle-Down Paradigm of Transformation
- Dissolution (Bhanga), and T.S. Eliot

**Wave 3 (16 files)** — multi-part series + RAW-DEGRADED standalones:
- Zero and One Pts 1, 2, 3, 4 of 4
- Five Aspects of the Five Ways Pts 1, 2, 3, 4 of 4
- Zen Ox-Herding Pics Pts 1, 2, 3 of 3 *(Pt 3 was RAW-DEGRADED — Budai/guoshi/daoxin restored)*
- Equanimity and the Taste of Purification Pts 1, 2 of 2
- Leonard Cohen, Sasaki Roshi, & Love Itself Pts 1, 2 of 2
- The Theme of Expansive and Contractive Flow *(was RAW-DEGRADED — `parasu prosciutto`/`sopressata` → `kakuchō`/`shukushō` reconstruction)*

**Wave 4 (15 of 16 files)** — Bhanga interactive series + Enlightenment cluster + extensions:
- Experiences of the Dissolution (Bhanga) Process Pts 1, 2, 3 of 3 (Interactive)
- Ordinary Consciousness is the Way Pts 1, 2, 3 of 3
- What is Enlightenment
- Enlightenment Maps and Models
- Towards a Balanced Enlightenment
- Classical Enlightenment Healing the World and Screw-ups
- A Deeper Freedom Experiences of Selflessness *(stalled but file complete — verified)*
- The Five Ways - A Contemporary Toolkit for Classical Enlightenment
- Five Basic Assumptions in Mindfulness Practice
- Recycle the Reaction - Beginner, Intermediate, & Advanced Examples
- Purification and Fulfilment Four Formulas

---

## What's NOT done — explicit pending list

### 1. ONE editorial retry (rate-limit failure) — DONE 2026-04-29

`Expansion, Contraction and the Breath Cycle ~ Shinzen Young_z9LgdG3O94Y.md` — completed inline (4-min file, edited directly without sub-agent dispatch). Output at `edited/Expansion, Contraction and the Breath Cycle ~ Shinzen Young_z9LgdG3O94Y.md`. Editorial wave is now 56 of 56 dispatched files complete.

### 2. Re-transcription of 19 tiny.en files — UNBLOCKED 2026-04-29

Toolchain status (verified):
- ✅ yt-dlp v2026.02.04 installed
- ✅ faster-whisper v1.2.1 installed
- ✅ **ffmpeg/ffprobe v7.0.2 installed** at `~/.local/bin/` (johnvansickle static x86_64 build, no sudo needed; user lacks sudo password). On PATH.
- ❌ No CUDA GPU — CPU-only (unchanged)

Ready to dispatch the Haiku re-transcription batch.

Once ffmpeg in, dispatch ONE Haiku agent (single agent, not a swarm — re-transcription is CPU-bound, parallel agents would queue). Workflow:
- For each of 19 files (find via `grep -l "faster-whisper (tiny.en" *.md`):
  - `yt-dlp -x --audio-format mp3 -o /tmp/shinzen_audio_scratch/<id>.%(ext)s "https://www.youtube.com/watch?v=<id>"`
  - faster-whisper Python: `model = WhisperModel("medium.en", device="cpu", compute_type="int8")` — DEFAULT model
  - **Escalate to `large-v3`** (multilingual) for 5 heavily cross-traditional files: Humility to the Vanishing Point, Jewish Mysticism & Mindfulness, A Life of Practice and Service Shinzen at 80, Advanced Meditators Experience of Time, How Shinzen Uses the Term Spaciousness. Plus **`large-v3` + `language="pi"`** for Five Fold Sila in Pali.
  - Write to `raw/yt transcripts/retranscribed/<original-filename>` matching existing schema
  - Update Source field to reflect new model
  - Write `_RETRANSCRIPTION_MANIFEST.md` summary
- Expected runtime: 4–8 hours on CPU (medium.en ~5–15× realtime; the 100-min biographical interview alone could take 1–2 hours)
- **Note**: When retranscription completes, the `retranscribed/` version SUPERSEDES the `edited/` version for `Humility to the Vanishing Point` (which was edited as interim measure). Same applies if other tiny.en files were edited; check the overlap.

### 3. Wave 5+ (optional, lower priority) — remaining RAW-OK files

Approximately 50 RAW-OK kome.ai files of secondary priority. None are blocking the priority-20 ingestion path. Candidate clusters if you want fuller coverage before ingestion:
- **Subtler E-C territory**: `Mindfulness Momentum...Simultaneous E-C` (LlglNS_rg5g), `Paradigms of Change` (uco6mSHmwJA), `The Three-Dimensional Shape of Simultaneous E-C` (rzwkB4QWU_s)
- **Flow + Gone extensions**: `Abrupt Flow Diminishings, Vanishings and Noting Gone` (L-7LXHjGHfM), `Flow, Gone & a Figure-Ground Reversal` (rKm-WXRH2IQ), `Tri-Modal Rest & Flow Thinning Out into Nirvana` (BOLuaPltorA)
- **Enlightenment cluster remainders**: `Enlightenment Downsides` (qoAbCgmhqdM), `After enlightenment, what's left` (ptkH0uK1uXM), `Six Common Traps on the Path to Enlightenment` (i288Lnb7NOk), `Meditation Teacher's Qualifications and Liberation Experiences` (tF96pTDYEAU)
- **Reconstructive/Way of Human Goodness**: `Becoming a High-Wattage Broadcaster of Human Positivity` (-KFJYzPYDfA), `From Surface to Source & the Gold Standard for Spiritual Maturity` (ncQGlYfvO0Q), `Reparenting Our Freaked Out Infant` (Cg-h_MSijDo)
- **Method comparisons**: `Focus Methods in Mindfulness Advantages and Disadvantages` (nHETuhITils), `Turn Towards Physical Discomfort Sequence & The Taste of Purification` (LZ0L7_lEFqk), `Enlightenment and the Ten Zen Ox Herding Pictures` (Vt68YJCe_YA — standalone overview separate from the 3-part series already done)
- **Applied-register cluster** (Mindfulness in daily life): Sex/death/parenting/relationships talks — lower individual priority, would constitute a future synthesis page if many ingested

### 4. Files explicitly to SKIP (defer/discard policy)

- 4 Har-Prakash Khalsa standalone files (non-Shinzen primary): `Welcome to Cultivating the Jewel` (NS7_uN8F6P8), `Module One Cultivating the Jewel` (jex0giLXNAs — also tiny.en), `Guided See, Hear, Feel Sensory Spaces` (6XJN3TjhSZ8), `Guided Self-Nurturing Meditation...Khalsa` (Meqvr2zGn2U). Outside wiki's stated scope.
- Pure guided meditations / silent sits: `10 Minute Sit w. Shinzen Just Sitting`, `10 Minute Community Sit Chanting Om Mani Padme Hum`, `Guided Compassion and Healing the World Meditation`, `Five Fold Sila in Pali` (the Pali recitation only, not editable)
- The Spanish-only Noche Oscura recitation (`zA1APGkoupM`)
- The 7 header-only placeholder stubs (`<800 bytes` files identified in audit)

---

## Suggested next-session order

1. **`sudo apt-get install ffmpeg`** (user task; blocks #2)
2. Retry the 1 missing wave-4 file (Expansion, Contraction and the Breath Cycle) — ~3 min, single Sonnet dispatch
3. Dispatch the re-transcription Haiku batch for the 19 tiny.en files — runs in background 4–8 hours
4. **Begin actual ingestion** (the next phase, currently out of scope) — start with `Do Nothing Meditation_cZ6cdIaUZCA.md` from CLEAN tier as the pilot file (verified excellent quality in the deep-read audit), then the Expansion-Contraction 4-part series as the first major new page. See `wiki/index.md` and `CLAUDE.md` for ingestion methodology.
5. Optional wave 5 of editorial work on the ~50 remaining RAW-OK files if/when needed

---

## Reference: vocabulary correction dictionary used

For any future editorial dispatches. ASR commonly mangles these:

**Buddhist (Pali/Sanskrit)**: anicca, anatta, dukkha, samādhi, samatha, vipassanā, jhāna, khaṇikasamādhi, kleśa/klesha, prajñā, dharmakāya, ālayavijñāna, kliṣṭamanas, Yogācāra, Madhyamaka, Nāgārjuna, Buddhaghosa, Visuddhimagga, udayabbaya, satta visuddhi, kaṣāya, śūnyatā/shunyata, bodhicitta, bodhisattva, karuṇā, nirvāṇa, saṃsāra, satori, kenshō, kōan, sati, dharma/dhamma, sandiṭṭhiko, ehipassiko, adhitthana, bhanga, dukkha-ñāṇas, sotapanna, arahant
**Tibetan**: Dzogchen, Mahāmudrā, dagme (dak-me), gomme (gom-me), trekchö, tögal, rigpa, sem
**Zen / Japanese**: Joshu Sasaki Roshi (often "sasaki [random English]"), Yamada Mumon, Shingon, Mount Kōya, Theravāda, Mahayana, tenzo, mu, shikantaza, dokusan, sesshin, Hotei/Budai, Mahasi Sayadaw, kakuchō (拡張), shukushō (縮小)
**Chinese**: Chang'an, niú (ox), guoshi (國師), shíniútú (十牛圖), wú-wéi, Chán, Tang Dynasty
**Vietnamese**: Thich Thien-An (catastrophically mangled by tiny.en)
**Sufi**: fanāʾ (often "fanat"), baqāʾ ("bakau"), dhikr/zikr
**Hebrew/Kabbalah**: Ein Sof, bittul ha-yesh, bri'ah yesh me-ayin, me-ayin, sefirot, Nefesh / Ruach / Neshamah / Chayah / Yechidah, kavanah
**Christian apophatic**: nepsis, catharsis, theosis, hesychia, hesychasm, kenosis, recollectio, Noche Oscura
**Vedantic**: Advaita, atman, Brahman, neti-neti, "I am" / aham, sat-chit-ananda, jnana, sakshi (witness), sabija/nirbija/sahaja samadhi, Ramana Maharshi, Nisargadatta Maharaj

**Critical names**: SHINZEN Young (NEVER "Shenzhen", "Shin sedon")

**Common ASR error patterns to scan for**:
`Bahamut` → about/enlightenment; `Shenzhen`/`Shin sedon` → Shinzen; `shingling monk` → Shingon monk; `South Beast` → Southeast; `Anita` → anicca (Buddhist context); `writing the ox` → riding the ox; `co on`/`kohn` → kōan; `fanat` → fana; `bakau` → baqa; `non duel` → non-dual; `duke ah` → dukkha; `an at a` → anatta; `yoga chara`/`yoga vichara` → Yogācāra; `clistamanas` → kliṣṭamanas; `alaya vichana` → ālayavijñāna; `v suit dhamaka`/`visa dhamaka` → Visuddhimagga; `Buddha cosa` → Buddhaghosa; `zouk chant`/`zog chen` → Dzogchen; `food I abaya` → udayabbaya; `son de Tico` → sandiṭṭhiko; `HEPA cycle` → ehipassiko; `bunga`/`banga`/`fungi` → bhanga.

---

## File-by-file tier classification (for triage reference)

If a future session needs to know any specific file's tier without re-running the audit:

- **Already in `edited/`** (55 files): assumed ingest-ready after light cleanup. The vocab pass + paragraphing already applied.
- **CLEAN tier (no editing needed, ingest as-is)**: any kome.ai file NOT in the `edited/` dir AND not in the tiny.en list. Spot-check examples: `Do Nothing Meditation_cZ6cdIaUZCA.md` (verified gold-standard), `Enlightenment; Simultaneous E-C; Sahej Samadhi_IefgNewLWus.md`. Default assumption for any short kome.ai file with paragraphed appearance.
- **Tier-C re-transcribe**: any file whose `Source:` line contains `faster-whisper (tiny.en` (19 files; full list via the grep command above).

The 23% of kome.ai that's RAW-DEGRADED has been mostly hit by waves 1–4 (priority files); residuals are the lower-priority RAW-OK / RAW-DEGRADED in the wave-5+ candidate list above.
