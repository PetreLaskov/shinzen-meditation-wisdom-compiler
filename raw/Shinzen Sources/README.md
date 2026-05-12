# Raw Sources

Drop source documents here. The agent reads them; it does not modify them.
This directory is **immutable input**: source code, in compiler terms.

What goes here:

- Articles, papers, transcripts, reports, internal memos, interview notes,
  long emails, structured datasets exported as text or CSV, anything else
  the wiki should be compiled *from*.
- Markdown is preferred when the source is text. PDFs, images, and other
  binaries go in `raw/assets/` and are referenced from a markdown stub
  here when they need a source page.

What does **not** go here:

- Anything you intend to edit later. If a "source" is going to be revised
  by you, it is a wiki page — put it in `wiki/`.
- Quick notes, todos, scratch thoughts. The wiki is for compiled
  knowledge; raw notes belong in your notes app.
- Generated content (LLM outputs, search-result dumps without curation).
  These compile into a wiki of laundered claims with no provenance.

---

## What makes a usable raw source

The lint script does not check source quality — but the agent's output
inherits it. Garbage in, garbage out. Before adding a file, ask:

### One topic per file

A 50-page document covering ten unrelated topics will produce a source
page that tries to compress all ten, or ten weak source pages that
duplicate the file. **Split the document by topic before adding it.**
One file, one cohesive thesis or scope.

If you have a transcript or interview that genuinely covers many topics,
keep it whole — but expect the source page to focus on the topic most
relevant to the wiki, with the rest summarized briefly. Re-ingest with a
sharper focus if a different topic becomes important later.

### Identifiable provenance

The source page records: author / origin, date, format, reliability,
scope. The raw file should make these answerable. Either:

- Encode them in the filename (`2024-09-Acemoglu-WhyNationsFail-Ch3.md`).
- Include them in a header at the top of the file.
- Or make them obvious from the file's natural metadata (a paper's
  title and authors at the top; a memo's "From / To / Date" header).

A raw file with no recoverable provenance can still be ingested, but
the source page will have to flag the gap. That's fine for some sources
(folk wisdom, anonymous quotes) and a problem for others (a contested
claim with no attribution).

### Datestamp

The file's mtime drives re-ingest detection. If you replace a raw file
with a corrected version, **bump its mtime** (touch, save, or replace)
so the agent knows to re-ingest. If you only want to fix typos, edit in
place and save — the mtime advances and re-ingest will run on the next
`/lint` cycle.

If the source has its own publication date (not the same as when you
added it), include that in a header inside the file. The source page's
Date field should be the source's publication date, not the file's
mtime.

### Not duplicating an existing source

Before adding a file, scan `wiki/index.md` for existing source pages
that already cover this material. Re-ingesting the same content under
a different filename produces two source pages claiming the same
territory — a contradiction the lint script will not catch but the
review will.

If the new source genuinely revises or extends an existing one,
either:
- Replace the old raw file (mtime advances → re-ingest), or
- Add the new file alongside and let the next `/ingest` reconcile
  them — the source pages will end up referencing each other, with one
  superseding or extending the other.

### Reasonable size

The agent reads the whole file. A 200-page PDF takes a long time to
ingest and produces a source page with weaker compression. If the
source is large:

- Excerpt the relevant sections into a focused source file
  (`PaperX-pages-12-28.md`), and put the full PDF in `raw/assets/` for
  reference.
- Or split the source by topic into several smaller files.

Aim for raw sources in the 500–10,000 word range. Anything substantially
larger should be split or excerpted.

---

## Filename conventions

- Title Case With Spaces or Author-Year-Topic patterns both work.
  Pick one and stay consistent.
- `.md` for text. `.pdf`, `.png`, `.jpg` etc. live in `raw/assets/`.
- No spaces in filenames if you'll script around the directory; use
  spaces freely if you only operate via Claude Code.

---

## Asset handling

- `raw/assets/` holds binaries (images, PDFs, audio).
- A binary that needs its own source page is referenced from a
  markdown stub in `raw/`. Example:

      raw/
        Smith 2024 Institutional Reform.md   ← short stub naming the asset
        assets/
          smith-2024-institutional-reform.pdf

  The stub contains: title, author, date, abstract, and a link to the
  PDF. The agent ingests the stub (which is the source page's basis)
  but treats the PDF as supporting material.

- Inline images in wiki pages: `![alt](../raw/assets/file.png)`.
- PDF references in wiki pages: `[[../raw/assets/file.pdf]]` or just
  link in prose.
