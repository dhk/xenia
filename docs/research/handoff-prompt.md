# Research handoff prompt: credential provisioning prior-art scan

Copy everything below this line and hand it to any tool or person doing an
independent research pass. It's self-contained — no repo access required to
do the research, only to submit the result.

---

You're doing a prior-art research pass for RFC-0001 (the Xenia Credential
Provisioning Contract — a vendor-neutral spec for how tools declare
credential requirements and hosts resolve them via trial, BYOK, or managed
credentials). Repo: `dhk/xenia`, RFC at
`docs/rfcs/0001-credential-provisioning-contract.md` on `main`.

## Research brief

Answer these six questions; each maps to a specific part of RFC-0001.

1. **Provider abstraction / non-goals boundary** — Where do OAuth 2.1, OIDC,
   and workload-identity federation (SPIFFE, AWS STS, GCP Workload Identity
   Federation) already cover "short-lived, audience-bound handle instead of
   a durable secret"? Does RFC-0001's `credential_handle` duplicate or sit
   on top of these?
2. **Credential vault / secret lifecycle** — What do existing secret
   managers (Vault, AWS/GCP/Azure Secrets Manager, Doppler, Infisical,
   1Password Secrets Automation) already provide for rotation, audit, and
   least-privilege scoping that the RFC should reference rather than
   re-specify?
3. **AI-tool-specific prior art (most important)** — Existing
   credential-brokering layers for AI tools/agents: Model Context Protocol
   (MCP) authorization spec, ChatGPT plugin manifest auth types
   (`none`/`service_http`/`user_http`/`oauth`), unified-auth platforms
   (Composio, Arcade.dev, Nango, Paragon, Merge.dev), iPaaS connection
   models (Zapier, Make, n8n), and how Anthropic/OpenAI/Google handle
   tool-calling credential injection.
4. **Trial-mode controls** — How do existing trial/free-tier systems
   (RapidAPI, OpenRouter's BYOK-plus-credits, Replicate/Anthropic/OpenAI
   trial credits) handle abuse control, attribution, and "no silent
   conversion to paid"?
5. **Manifest format precedent** — Does RFC-0001's proposed YAML manifest
   overlap with OpenAPI security schemes, the ChatGPT plugin manifest, or
   MCP server auth config closely enough that it should extend one instead
   of inventing a new shape?
6. **Governance/conformance precedent** — RFC-0001 plans a future
   compatibility mark. What made comparable marks (OpenID Foundation
   certification, FIDO/WebAuthn, CNCF "Certified Kubernetes") credible vs.
   purely aspirational?

## Output format

Return one markdown file, structured exactly as:

```markdown
---
source: <your tool/model name>
date: <YYYY-MM-DD>
brief: docs/research/credential-provisioning-research-brief.md
---
# Findings: credential provisioning prior-art scan — <source>

## 1. Provider abstraction / non-goals boundary
| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|

Notes:
-
```

...repeated for all 6 sections in this exact order, plus a final
`## Open gaps` section. Keep headers and table columns identical — don't
rename, reorder, or drop them; this lets independent findings get diffed
mechanically against another tool's output later. Work independently —
don't look up or reconcile against any other tool's findings.

Two rules that keep this mechanically diffable:

- **Verdict is a closed set**: use exactly one of `adopt/reference`,
  `differentiate`, or `ignore` per row — don't invent new labels, and don't
  append rationale after the verdict (put rationale in that section's Notes
  instead).
- **No empty tables.** If a question turns up no prior art, add a single row
  with `none found` in the Entry column and explain why in Notes, rather
  than leaving the table empty.

**Return the completed markdown as your output.** It will be saved as
`docs/research/findings/<your-name>-findings.md` in the repo.

---

## For whoever is relaying the result back

If the researcher has no repo write access, take the markdown they return
and commit it as `docs/research/findings/<their-name>-findings.md` on their
behalf. See [`findings/README.md`](findings/README.md) for the naming and
format rules this template follows.
