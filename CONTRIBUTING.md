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

## Commit and pull-request quality

- Use focused, descriptive commits.
- Avoid mixing unrelated cleanup with the intended change.
- Never include credentials, tokens, production data, or secrets.
- Explain externally observable behavior changes.
- Include diagrams or examples when they materially improve understanding.

## Review priorities

Reviews emphasize security, explicit user choice, deterministic behavior, interoperability, backwards compatibility, testability, and operational clarity.

## Code of conduct

A formal code of conduct will be adopted before broader community participation. Until then, contributors are expected to communicate professionally, critique ideas rather than people, and make space for differing implementation contexts.
