---
name: commission-research
description: Scaffold and run a prior-art/competitive research pass for a design doc or RFC in this repo — writes a brief, a findings submission structure, and a handoff prompt for other tools, then runs an independent findings pass and later a synthesis pass. Use when the user says "commission research on X", "start a research pass for RFC-Y", "scaffold research for the design doc", "run a prior-art scan", or asks to set up research following the docs/research process.
---

# Commission research

This repo's convention for de-risking a design doc/RFC before it leaves
Draft: scaffold a research pass, get two or more independent sources (this
session plus at least one other tool or person) to answer the same
structured brief without seeing each other's work, then synthesize.

## Inputs needed from the user

- Which design doc / RFC / PR to research (path or link).
- A short topic slug (hyphenated, e.g. `credential-provisioning`).
- Which branch to work on (create it, or reset it from `main` first if that
  branch's last PR already merged — see this repo's merged-PR convention).

If any of these is missing or ambiguous, ask before scaffolding anything.

## Process

1. **Read the design doc.** Pull its open questions, explicit non-goals, and
   any "we're not trying to reinvent X" disclaimers — these become the
   research questions. Don't invent questions the doc doesn't motivate.
2. **Write the brief** at `docs/research/<topic-slug>/brief.md`. Every
   question must trace back to a specific section of the design doc — no
   open-ended "look around" scans.
3. **Scaffold the findings structure**:
   - `docs/research/<topic-slug>/README.md` — read-order index (brief →
     findings → handoff-prompt → synthesis) and a short note on why findings
     stay independent until synthesis (avoids one source anchoring on
     another's framing).
   - `docs/research/<topic-slug>/findings/README.md` — naming convention
     (`<source-slug>-findings.md`), format rules, and how to submit with or
     without repo write access.
   - `docs/research/<topic-slug>/findings/TEMPLATE.md` — one section per
     brief question, in the same order, each with a table
     (`Entry | What it is | <design-doc> concept overlap | Verdict`) plus a
     Notes block, and a final `## Open gaps` section. Lock in two rules,
     stated explicitly in both the template and its README:
     - Verdict is a closed set: `adopt/reference` / `differentiate` /
       `ignore` — no invented labels, no rationale appended inline (put
       rationale in Notes instead).
     - No empty tables — a "found nothing" result gets a `none found` row
       with the reason in Notes, not silence.
4. **Write the handoff prompt** at `docs/research/<topic-slug>/handoff-prompt.md`
   — the brief and output format bundled into one copy-pasteable,
   self-contained prompt for a tool or person with no repo access.
5. **Run your own findings pass.** Research the brief yourself and write
   `docs/research/<topic-slug>/findings/claude-findings.md`, following the
   template exactly — don't special-case your own output or leave rationale
   in verdict cells.
6. **Commit and push after each stage** (brief; scaffold; handoff prompt;
   own findings) to the working branch. Don't open a PR unless asked.
7. **When other findings arrive** (pasted back by the user, or committed
   directly by another tool with repo access), read every file in
   `findings/` and write `docs/research/<topic-slug>/synthesis.md`: per
   question, where sources agree, where they conflict and which is more
   credible, what only one source caught, and what's genuinely
   unanswered — mapped back to the design doc's actual open questions.
8. **Report where the process broke** — any template ambiguity, missing
   convention, or judgment call required — at every stage, not saved up for
   the end.

## Convention note

This repo's first research pass (credential provisioning, informing
RFC-0001) predates the subfolder convention above and lives flat at
`docs/research/*.md` with a shared `findings/`. Leave it as-is — don't
retroactively migrate it. Every topic after it uses the
`docs/research/<topic-slug>/` subfolder shape.
