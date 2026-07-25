# Submitting findings

Each independent researcher (human or tool) produces one file here.

## Filename

`<source-slug>-findings.md` — lowercase, hyphenated, identifies the tool or
person. Examples: `claude-findings.md`, `chatgpt-findings.md`,
`gpt-5-findings.md`. One file per source; don't append to someone else's.

## Format

Copy [`TEMPLATE.md`](TEMPLATE.md) and fill it in. Keep the six section
headers and the table columns exactly as given, in the same order as the
brief's six research questions — that's what lets the synthesis step diff
findings across sources mechanically instead of re-reading free-form prose.
Within a table cell, write as much as you need; just don't rename, reorder,
or drop columns/sections.

Two rules that keep this mechanically diffable — see `TEMPLATE.md` for
where they apply:

- Verdict is a closed set: `adopt/reference`, `differentiate`, or `ignore`.
  Don't invent new labels.
- No empty tables. If a question turns up nothing, add a `none found` row
  and explain why in Notes, so it reads as "looked, found nothing" rather
  than "skipped."

Fill in the frontmatter at the top (source name, date, and the brief file
you worked from) so the synthesis step can cite where each finding came
from.

## How to get it into the repo

- **If you have direct write access to this repo/branch**: commit the
  completed file directly to `docs/research/findings/<source-slug>-findings.md`
  on this branch (or open a PR against it).
- **If you don't** (e.g. you're a tool or chat session without repo write
  access): paste the completed markdown back into the conversation with
  Claude, and it will be committed on your behalf.

## What happens next

Once findings from all sources are in, a synthesis pass reads all files in
this folder and produces `../credential-provisioning-synthesis.md`. You
don't need to reconcile with other sources yourself — just answer the brief
as thoroughly as you can from your own research.
