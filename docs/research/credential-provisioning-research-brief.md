# Research brief: credential provisioning — prior art scan

Status: **research only** — no implementation planned yet.

Source doc: [RFC-0001, "Xenia Credential Provisioning Contract"](https://github.com/dhk/xenia/blob/feature/bootstrap-repo/docs/rfcs/0001-credential-provisioning-contract.md)
Tracking PR: #2 (draft)

## Why this brief exists

RFC-0001 proposes a vendor-neutral contract for how tools declare credential
requirements and hosts resolve them across trial, BYOK, and managed modes.
Its own **non-goals** section is explicit that Xenia is not meant to replace
OAuth, OIDC, cloud secret managers, or provider-native key systems — which
means the RFC only holds together if we've actually checked what those
existing systems do and where Xenia's boundary sits relative to them.

Several of the RFC's **open questions** (handle-transport standardization,
mandatory manifest fields, provider-identifier registry vs. reverse-domain
naming, compound/multi-provider fallback representation, minimum trial
controls) are really "has someone already solved this" questions. This brief
scopes that scan before the RFC moves from Draft toward In review.

## Research questions

Mapped to RFC-0001 sections:

1. **Provider abstraction / non-goals boundary** — Where exactly do OAuth
   2.1, OIDC, and workload-identity federation (SPIFFE, AWS STS, GCP
   Workload Identity Federation) already cover "short-lived, audience-bound
   handle instead of a durable secret"? Does Xenia's `credential_handle`
   duplicate or sit on top of these?
2. **Credential vault / secret lifecycle** — What do existing secret
   managers (Vault, AWS/GCP/Azure Secrets Manager, Doppler, Infisical,
   1Password Secrets Automation) already provide for rotation, audit, and
   least-privilege scoping that Xenia's spec should just reference rather
   than re-specify?
3. **AI-tool-specific prior art (most important)** — Are there existing
   credential-brokering layers built specifically for AI tool/agent
   ecosystems? This is the area most likely to have direct competitors or
   direct prior art:
   - Model Context Protocol (MCP) authorization spec
   - ChatGPT plugin manifest auth types (`none` / `service_http` /
     `user_http` / `oauth`)
   - Unified-auth-for-agents platforms: Composio, Arcade.dev, Nango,
     Paragon, Merge.dev
   - iPaaS "connection" models: Zapier, Make, n8n credential storage per
     integration
   - Anthropic's own remote-MCP/connector OAuth flow, and how other model
     providers (OpenAI, Google) handle tool-calling credential injection
4. **Trial-mode controls** — How do existing trial/free-tier systems (RapidAPI
   free tiers, OpenRouter's BYOK-plus-credits model, Replicate/Anthropic/OpenAI
   trial credits) handle abuse control, attribution, and the "no silent
   conversion to paid" requirement RFC-0001 lists as a MUST?
5. **Manifest format precedent** — Does the proposed YAML manifest
   (`xenia: "1.0"`, `credentials: [...]`) overlap with existing declarative
   auth-requirement formats — OpenAPI security schemes, the ChatGPT plugin
   manifest, MCP server config `env`/auth blocks — closely enough that Xenia
   should extend one of those instead of inventing a new shape?
6. **Governance/conformance precedent** — RFC-0001 and GOVERNANCE.md plan a
   future compatibility mark tied to a conformance profile. What does that
   look like for comparable vendor-neutral specs — OpenID Foundation
   certification, FIDO Alliance/WebAuthn, CNCF conformance (e.g. "Certified
   Kubernetes")? What made those marks credible vs. purely aspirational?

## What to capture per entry

For each standard, platform, or spec found:

- What it is, one line.
- Which RFC-0001 concept it overlaps with (manifest, resolution, handle,
  vault, trial control, conformance mark).
- Is it a foundation Xenia can build on/reference, or a direct competitor to
  the whole contract?
- Governance model, if relevant (single-vendor vs. multi-stakeholder).
- One-line verdict: adopt/reference, differentiate from, or ignore.

## Deliverable

A findings doc under `docs/research/` — comparison notes per question above —
feeding directly into RFC-0001's "Open questions" section and into whether
the non-goals list needs to be more specific about how Xenia composes with
OAuth/OIDC/secret managers rather than duplicating them.

## Out of scope

- No RFC edits or implementation yet.
- No decision on which registry/naming scheme or handle-transport approach
  to adopt — this pass is prior-art gathering to inform that decision, not
  the decision itself.

## Suggested next step

Run the scan across items 1–6 above, produce the findings doc, and bring it
back to PR #2 / RFC-0001 review before the RFC moves out of Draft.
