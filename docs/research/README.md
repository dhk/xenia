# Research: credential provisioning prior-art scan

This folder holds the research pass that feeds back into RFC-0001 (PR #2)
before it moves out of Draft. Read these in order:

1. [`credential-provisioning-research-brief.md`](credential-provisioning-research-brief.md)
   — the frozen input. Every researcher (human or tool) works from this
   exact file. Do not edit it mid-scan; if the scope needs to change, that's
   a new brief revision and a new round.
2. [`findings/`](findings/) — one file per independent researcher, each
   answering the brief's six questions in the same structure. See
   [`findings/README.md`](findings/README.md) for the submission format.
3. `credential-provisioning-synthesis.md` (added once findings are in) — the
   reconciled result: where findings agree, where they conflict, what's
   still open. This is the artifact that actually gets linked back into
   RFC-0001 review — the raw findings are inputs, not the deliverable.

## Why findings stay separate before synthesis

Each researcher works from the brief independently, without seeing the
other's output first. That's deliberate — it avoids one tool anchoring on
the other's framing, and it means the synthesis step can show genuine
agreement/disagreement instead of one tool just echoing the other.

## Starting a new research pass

This folder is laid out flat because it was the first research pass in the
repo. Later topics should live under their own `docs/research/<topic-slug>/`
subfolder instead, so multiple concurrent passes don't collide in one
shared `findings/` directory. See
[`commissioning-prompt-template.md`](commissioning-prompt-template.md) for a
fill-in-the-blanks prompt that runs this whole process end to end, or run
`/commission-research <design-doc> <topic-slug> [branch]`.
