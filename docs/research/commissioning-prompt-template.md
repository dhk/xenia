# Prompt template: commissioning a research pass

Copy this, fill in the three blanks, and hand it to Claude (or run
`/commission-research <design-doc> <topic-slug> [branch]` — see
`.claude/commands/commission-research.md`, which follows the same process
via the `commission-research` skill).

---

Commission a research pass for this design doc/RFC: **\<link or path to the
design doc/RFC/PR\>**

Topic slug: **\<short-hyphenated-topic, e.g. credential-provisioning\>**

Branch to work on: **\<branch name — create or reset from `main` if that
branch's last PR already merged\>**

Do the following, committing and pushing after each stage:

1. Read the design doc. Pull out its open questions, explicit non-goals, and
   any "we're not trying to reinvent X" disclaimers — turn each into a
   numbered research question a prior-art scan should answer. Write it to
   `docs/research/<topic-slug>/brief.md`.
2. Scaffold the findings structure under `docs/research/<topic-slug>/`:
   `README.md` (read-order index), `findings/README.md` (naming convention,
   format rules, submission instructions with/without repo access), and
   `findings/TEMPLATE.md` (one section per brief question, each with a
   table — Entry / What it is / concept overlap / Verdict — plus Notes, and
   a final Open Gaps section). Lock in: verdict is a closed set
   (`adopt/reference` / `differentiate` / `ignore`, no invented labels), and
   no empty tables (a "found nothing" result gets a `none found` row and an
   explanation in Notes, not silence).
3. Write `docs/research/<topic-slug>/handoff-prompt.md` — the brief and
   output format bundled into one self-contained, copy-pasteable prompt for
   handing to another tool or person with no repo access.
4. Run your own findings pass and write
   `docs/research/<topic-slug>/findings/claude-findings.md`, following the
   template exactly — don't special-case your own output.
5. Tell me where the process broke — anything ambiguous, any judgment call
   you had to make — at every stage, not just the end.
6. Once other findings land (I'll paste them back, or another tool commits
   directly), read every file in `findings/` and write
   `docs/research/<topic-slug>/synthesis.md`: per question, where sources
   agree, where they conflict and which is more credible, what only one
   source caught, and what's genuinely still open — mapped back to the
   design doc's actual open questions.

Don't open a PR unless I ask for one.

---

**Convention note**: this repo's first research pass (credential
provisioning, informing RFC-0001) predates this subfolder convention and
lives flat at `docs/research/*.md` with a shared `findings/`. Leave that one
as-is — it's not worth migrating. Every topic after it uses the
`docs/research/<topic-slug>/` subfolder shape described above.
