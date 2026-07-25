---
description: Scaffold and run a prior-art research pass for a design doc/RFC (brief, findings structure, handoff prompt, own findings)
argument-hint: <design-doc-path-or-PR> <topic-slug> [branch-name]
---

Commission a research pass following the `commission-research` skill
(load it with the Skill tool if it isn't already active), for: $ARGUMENTS

Treat the arguments in order as: the design doc/RFC/PR to research, a short
hyphenated topic slug, and optionally the branch to work on. If any of these
is missing, ask before scaffolding anything — don't guess a topic slug or
branch name.
