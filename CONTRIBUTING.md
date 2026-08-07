# Contributing to Xenia

Thank you for helping build an interoperable credential-provisioning contract for tools.

## Workflow

All substantive changes must be made on a branch and submitted through a pull request. Do not commit directly to `main`.

1. Open or identify a GitHub issue.
2. Create a descriptive branch, such as `feature/manifest-schema`, `docs/threat-model`, or `fix/resolution-error`.
3. Keep the change focused on the issue.
4. Add or update tests and documentation where applicable.
5. Open a draft pull request early.
6. Link the issue and explain the design and validation performed.
7. Resolve review feedback before requesting merge.

## RFCs

Changes to the credential contract, security model, compatibility requirements, governance, or public extension points should use a numbered RFC under `docs/rfcs/`.

An RFC should include motivation, goals, non-goals, terminology, proposed design, security and privacy implications, alternatives, open questions, and licensing or governance implications where relevant.

Contract changes should also update the relevant status or decision register. Do not present a research recommendation as accepted merely because it appears in an RFC discussion or synthesis.

## Prior art, evidence, and challenges

Prior-art submissions and challenges to project assumptions are welcome. Preserve conflicting findings rather than forcing consensus. For each external claim, prefer the responsible standards body, project, or vendor as the source and record the URL, verification date, and whether the claim is verified, interpreted, unverified, or time-sensitive. Search results and model output can identify leads but are not authoritative evidence.

When proposing an RFC change:

- identify which current statement or decision is affected;
- distinguish sourced facts from your interpretation;
- explain alternatives and security, privacy, billing, and interoperability tradeoffs;
- flag product, pricing, program, and evolving-standard claims for revalidation; and
- disclose relevant employment, funding, vendor relationships, or other affiliations that a reasonable reviewer could view as a conflict.

Good-faith disagreement is useful. A rejected recommendation should retain its rationale and provenance.

## Commit and pull-request quality

- Use focused, descriptive commits.
- Avoid mixing unrelated cleanup with the intended change.
- Never include credentials, tokens, production data, or secrets.
- Explain externally observable behavior changes.
- Include diagrams or examples when they materially improve understanding.
- Run `python scripts/check_docs.py` for documentation changes.

## Review priorities

Reviews emphasize security, explicit user choice, deterministic behavior, interoperability, backwards compatibility, testability, and operational clarity.

## Code of conduct

A formal code of conduct will be adopted before broader community participation. Until then, contributors are expected to communicate professionally, critique ideas rather than people, and make space for differing implementation contexts.
