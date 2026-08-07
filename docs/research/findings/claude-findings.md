---
source: Claude (claude-sonnet-5)
date: 2026-07-25
brief: docs/research/credential-provisioning-research-brief.md
---

# Findings: credential provisioning prior-art scan — Claude (claude-sonnet-5)

> **Non-authoritative model-generated research input.** Product, pricing, program, and evolving-standards claims may be stale or incomplete. This file preserves the original independent finding and disagreement; see the [evidence register](../evidence-register.md) before relying on a claim.

## 1. Provider abstraction / non-goals boundary

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OAuth 2.1 + PKCE | Client/resource-server model where a client exchanges credentials for a short-lived, scoped access token | Directly overlaps `credential_handle` — RFC-0001's handle is functionally an access token; the RFC doesn't need to define token issuance/refresh itself | adopt/reference |
| SPIFFE/SPIRE | Workload identity standard issuing short-lived X.509/JWT SVIDs (~60 min TTL) across clusters/clouds without static IAM roles | Overlaps "opaque, short-lived credential handles" and "least privilege" — the non-human/workload analogue of what RFC-0001 wants for tool→provider handles | adopt/reference |
| AWS STS/IRSA, GCP Workload Identity Federation | Cloud-native short-lived credential exchange for workloads, siloed per cloud | Overlaps the managed-credential lifecycle; shows "opaque handle" is already solved per-cloud but not cross-cloud/vendor-neutral | differentiate |
| MCP Authorization spec (introduced 2025-06-18, revised in the 2026-07-28 release candidate) | Mandates OAuth 2.1 + PKCE + OAuth 2.0 Protected Resource Metadata for MCP servers exposing tools/resources | Directly adjacent: already standardizes "how a client obtains a token to call a tool," one layer below RFC-0001's "which credential mode resolves for this tool" | adopt/reference |

Notes:
- RFC-0001's own non-goals disclaimer is warranted: none of the above compete with Xenia, they sit underneath it. Recommend the RFC say explicitly that a resolved handle for an OAuth-capable provider SHOULD be an OAuth 2.1 access token, rather than leaving `credential_handle`'s relationship to OAuth tokens implicit.
- SPIFFE/SPIRE's relevance is mainly for managed-mode server-to-server flows, not BYOK/trial.
- AWS STS/IRSA and GCP Workload Identity Federation are good supporting evidence for RFC-0001's own motivation: they prove "opaque short-lived handle" is a solved problem per-cloud, which sharpens the case for a cross-cloud, vendor-neutral layer.
- MCP's authorization spec should be cited explicitly in RFC-0001 — MCP is Xenia's most likely deployment substrate, and its 2026-07-28 revision is current.

## 2. Credential vault / secret lifecycle

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| HashiCorp Vault | Self-hosted/enterprise secrets engine; true dynamic secrets (generated on demand, auto-expiring) plus deep audit logging | Overlaps "credential vault," rotation, and audit sections | adopt/reference |
| AWS Secrets Manager | Rotation-based (not fully dynamic) secret store; native CloudTrail audit trail | Same overlap, weaker rotation model than Vault | adopt/reference |
| Infisical | Open-source secrets manager; added dynamic secret generation for databases/cloud providers in early 2026, narrowing the gap with Vault | Overlaps vault/rotation/audit; likely low-cost self-hosted backing store for smaller Xenia hosts | adopt/reference |
| Doppler | Hosted secrets manager, mainly rotation + distribution rather than dynamic issuance | Same overlap, lighter-weight | ignore |

Notes:
- None of these define a "tool declares requirement, host resolves by mode" layer — they're all "where secrets physically live," not "which mode a tool should get." Confirms the manifest+resolution layer in RFC-0001 is additive, not duplicative. Recommend the RFC state explicitly that Xenia is vault-agnostic — a resolution layer that can sit in front of Vault, Secrets Manager, or Infisical rather than picking a winner.
- HashiCorp Vault is the reference-grade backing store for managed mode (most mature dynamic-secrets story); AWS Secrets Manager is the common target a Xenia resolver would sit in front of on AWS-native stacks; Doppler is lighter-weight and only worth an optional mention, not a reference implementation.

## 3. AI-tool-specific prior art

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| Composio | Hosted managed-OAuth + tool catalog (250+ integrations) targeting fast prototyping; handles auth and observability for agent tool calls | Overlaps "managed credential" mode and much of the manifest/resolution concept, but scoped to Composio's own catalog, not a vendor-neutral contract | differentiate |
| Nango | Open-source-friendly integration layer: tool definitions as code deployed to Nango's runtime, which owns auth/retries/rate-limiting; strongest observability (OpenTelemetry) | Overlaps resolution + handle + audit; code-first and open is architecturally close to what a Xenia reference implementation could look like | adopt/reference |
| Arcade.dev | MCP-focused runtime; per-user OAuth with a managed token vault; "just-in-time permissions" model; smaller catalog (~112 integrations) | Overlaps "opaque short-lived handle" and "explicit user choice" (per-user delegated grants) almost exactly | adopt/reference |
| Zapier / Make / n8n "connections" | iPaaS-style per-integration stored credential, chosen by the workflow author at build time | Overlaps BYOK/managed UX (a picker at setup time), but no trial-mode concept and no declarative manifest — UI-driven, not contract-driven | differentiate |
| ChatGPT plugin manifest (`ai-plugin.json`, deprecated) | Declarative manifest with an `auth` field (`none`/`service_http`/`user_http`/`oauth`) alongside an OpenAPI spec | Directly overlaps the manifest concept — closest historical precedent for "tool declares an auth requirement in a manifest" | adopt/reference |

Notes:
- This is the strongest area of overlap. Composio/Nango/Arcade collectively prove the underlying problem (agents need brokered, scoped, auditable credentials) is already being solved commercially — but each is a single-vendor hosted platform, not a portable contract multiple hosts implement. That's a legitimate gap RFC-0001 can fill, but the RFC should name these platforms explicitly as prior art (and potential conformance-suite test subjects or early adopters), and should clarify that a Xenia-conformant host could implement the contract *by delegating to* one of these under the hood rather than needing to differ from them architecturally.
- Composio is the closest functional competitor overall — RFC-0001 should say plainly why an open contract is needed when platforms like this already exist (portability across hosts, no single-vendor lock-in).
- Nango's code-first, open-source pattern is the closest implementation-pattern precedent for a Xenia reference implementation.
- Arcade.dev's per-user JIT-permission model is the closest prior art for RFC-0001's resolution-result shape and scoping model — worth studying directly.
- The ChatGPT plugin manifest is reference-worthy as a format precedent, but it's deprecated (MCP effectively superseded it) — worth asking why it didn't survive before copying its shape wholesale.

## 4. Trial-mode controls

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| Risk-based signup scoring (email reputation, IP, device, behavioral signals) before granting a trial | Pre-trial fraud-screening pattern used broadly across SaaS/AI trial issuance | Directly overlaps RFC-0001's trial abuse-control requirements | adopt/reference |
| Targeted phone verification for the highest-risk segment only (e.g. Mistral, per public reporting) | Apply friction (e.g. phone verification) only to a small high-risk slice of signups rather than all users | Overlaps the RFC's "honest trials" principle and conversion concerns | adopt/reference |
| Rate limiting by credential/device/behavioral-session, not just by IP | Multi-axis limiting so one abused account can't extract unlimited value even after signup | Overlaps quota-visibility and abuse-control requirements | adopt/reference |

Notes:
- Could not find public, specific documentation of OpenAI's, Anthropic's, or Replicate's own internal trial-abuse mechanics (proprietary/undocumented). The above is the general industry pattern (Stripe's public guidance, Mistral's reported phone-verification approach) used as the best available public proxy — flagged as an open gap below.
- Recommend RFC-0001's abuse-control bullet cite: (a) scoring signals *before* minting a trial credential rather than only rate-limiting after, and (b) applying friction like phone verification only to the highest-risk segment rather than universally, to avoid hurting legitimate-user conversion.

## 5. Manifest format precedent

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OpenAPI 3.x `securitySchemes` (apiKey / http / oauth2 / openIdConnect, `security` requirement objects with OR-of-schemes semantics) | Standard, widely-tooled vocabulary for declaring "this API needs this kind of credential" at the endpoint/operation level | Close overlap with RFC-0001's `credentials[].kind`/`scopes` | adopt/reference |
| ChatGPT plugin manifest `auth` field | Declarative per-plugin auth descriptor (`none`/`service_http`/`user_http`/`oauth`) | Same conceptual slot as RFC-0001's `accepted_modes`, but modeled around auth *mechanism*, not credential *mode* (trial/BYOK/managed) | differentiate |
| MCP server auth config (implementation-level env vars per tool, e.g. the `MY_API_KEY_API_KEY`-style convention used by tools like Gram/openapi-mcp) | Ad hoc, per-tooling-vendor convention rather than a spec; not standardized across MCP hosts | Confirms there's no existing standard at the exact layer RFC-0001 targets | ignore |

Notes:
- No single existing format cleanly covers both "auth mechanism" (OpenAPI/plugin-manifest territory) and "credential mode + trial/BYOK/managed policy" (RFC-0001's actual contribution). Recommend the RFC cite OpenAPI's securityScheme vocabulary explicitly as the layer it composes with — consider reusing it for the `kind` field instead of inventing new enum values — rather than appearing to reinvent it from scratch.
- The ChatGPT plugin manifest's `auth` field models mechanism, not mode; RFC-0001 should state explicitly that "mode" (who pays/owns) and "mechanism" (how the token is obtained) are orthogonal and both may need declaring.
- The MCP server env-var convention isn't prior art to build on, but it's useful evidence of the gap: no existing standard covers RFC-0001's exact layer.

## 6. Governance/conformance precedent

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OpenID Foundation self-certification ("OpenID Certified" mark) | Free, open-source conformance suite; implementers self-test and self-certify; independent accredited labs supplementing self-certification starting Q2 2026 | Directly overlaps RFC-0001's planned compatibility mark + conformance suite | adopt/reference |
| CNCF Certified Kubernetes program | Vendor-submitted conformance test results reviewed by a CNCF working group; 100+ certified distributions across every major vendor | Overlaps the "no privileged vendor" governance goal plus the conformance-mark mechanism | adopt/reference |
| CNCF Certified Kubernetes AI Conformance (launched November 2025) | Newest extension of the same conformance-mark model, applied specifically to AI workloads on Kubernetes | Closely analogous, and current — a neutral foundation extending an existing conformance program into the AI space at the same moment Xenia is attempting something similar for AI credential provisioning | adopt/reference |

Notes:
- Common thread across both precedents: credibility came from (a) a free/open self-test suite lowering the barrier to entry, and (b) a neutral, multi-stakeholder foundation — not the spec's original authors — administering certification. GOVERNANCE.md currently doesn't say who would administer Xenia's future compatibility mark; that's the biggest gap relative to precedent.
- OpenID's self-certify-first, accredited-labs-later staged rollout is a proven path Xenia could copy directly.
- CNCF's Kubernetes AI Conformance program (Nov 2025) is worth citing directly as the most current comparable case — same moment, adjacent problem (interoperability/portability of AI-adjacent infrastructure), different domain (compute conformance vs. credential provisioning).

## Open gaps

- No public documentation found for OpenAI's/Anthropic's/Replicate's specific internal trial-abuse mechanics (proprietary); relied on general industry practice (Stripe, Mistral) as a proxy. A follow-up pass would need primary-source or first-party interviews rather than public search.
- Found no vendor-neutral foundation specifically for AI credential/secrets provisioning (as opposed to Kubernetes or identity). CNCF's AI conformance program is adjacent but a different domain — Xenia's governance model may have no direct precedent, only adjacent ones. Worth flagging back to RFC-0001/GOVERNANCE.md rather than assuming a template exists.
- Did not evaluate provider-identifier registry approaches in depth (RFC-0001 open question 3: central registry vs. reverse-domain naming). Would need a dedicated follow-up comparing IANA-style registries against npm/Maven-style reverse-domain precedent.
- Compound/multi-provider fallback representation (RFC-0001 open question 4) wasn't answered by any prior art found — none of the surveyed manifest formats (OpenAPI, ChatGPT plugin, MCP) model multi-provider fallback for a single requirement. This looks like a genuinely novel piece of RFC-0001, not something to borrow.
