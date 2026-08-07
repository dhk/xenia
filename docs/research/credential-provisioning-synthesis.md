# Synthesis: credential provisioning prior-art scan

> **Non-authoritative synthesis of model-generated research inputs.** This document preserves agreement, disagreement, and leads. It is not a specification decision. See the [recommendation register](../specification-status.md) for accepted/pending/needs-verification status and the [evidence register](evidence-register.md) for primary-source checks.

Status: reconciles two independent findings passes into recommendations for
RFC-0001 review.

Sources:
- [`findings/claude-findings.md`](findings/claude-findings.md) — Claude (claude-sonnet-5), 2026-07-25
- [`findings/perplexity-findings.md`](findings/perplexity-findings.md) — Perplexity AI Research Assistant, 2026-07-26

Brief: [`credential-provisioning-research-brief.md`](credential-provisioning-research-brief.md)

## 1. Provider abstraction / non-goals boundary

**Agreement**: Both sources independently concluded RFC-0001's non-goals
disclaimer (not replacing OAuth/OIDC/secret managers/provider-native keys)
is the right posture, and that `credential_handle` is functionally an OAuth
2.1-style short-lived, scoped token — the RFC should say so explicitly
rather than leave the relationship implicit. Both also flagged SPIFFE/SPIRE
as the closest workload-identity analogue and AWS STS/GCP Workload Identity
Federation as evidence the "opaque handle" pattern is already solved
per-cloud, sharpening (not undermining) the case for a vendor-neutral layer.

**Unique to Perplexity**: the IETF WIMSE working group — an emerging
standardization effort for workload identity across multi-service
environments. Neither the RFC nor my own pass mentioned it; worth watching
as the standardization trajectory this space is already moving toward, and
a candidate to name in RFC-0001's Extensibility section.

**Unique to me**: naming MCP's authorization spec specifically in this
section (Perplexity placed MCP auth under section 3 instead) — a
placement difference, not a substantive disagreement; both sources agree on
what MCP's spec actually mandates (OAuth 2.1 + PKCE + Protected Resource
Metadata).

**Recommendation for RFC-0001**: in Provider abstraction / Non-goals, state
explicitly that a resolved handle for an OAuth-capable provider SHOULD be an
OAuth 2.1 access token, and add SPIFFE/SVID and the IETF WIMSE trajectory to
Extensibility as compatible/watchable future credential kinds.

## 2. Credential vault / secret lifecycle

**Agreement**: Full agreement, no divergence. Both sources landed on
Vault/Secrets Manager/Doppler/Infisical as adopt/reference, and both
independently reported that the secret managers they surveyed did not model
the trial/BYOK/managed three-way mode taxonomy. That bounded finding suggests
a possible contribution for RFC-0001; it does not establish an exhaustive
absence across all secret managers.

**Recommendation for RFC-0001**: add a short explicit statement (likely in
BYOK controls or Security model) that Xenia is a resolution/brokering layer
that sits above pluggable vault backends, rather than a vault itself.

## 3. AI-tool-specific prior art (most important)

**Agreement**: Both sources agree this is the strongest area of overlap —
Composio, Arcade.dev, and Nango-style platforms already broker scoped,
auditable AI-tool credentials commercially, and MCP's auth spec is the
substrate Xenia will most likely run on top of.

**Genuine disagreement — Composio's verdict**: I called Composio
`differentiate` (closest functional competitor; RFC-0001 should justify why
an open contract is needed when a platform like this exists). Perplexity
called it `adopt/reference` (Composio's Auth Config ≈ Xenia's credential
requirement, Connected Account ≈ resolved credential source — a shape to
mirror). Both are correct about different aspects: Xenia should *adopt* the
requirement/resolved-source conceptual shape Composio already validated,
while *differentiating* on being an open, portable contract instead of a
single-vendor platform. Read as "adopt the pattern, differentiate the
governance," not a real conflict.

**Same pattern with Zapier/Make/n8n**: I said `differentiate` (UI-driven,
no trial-mode concept); Perplexity said `adopt/reference` (validates the
requirement-scoped-credential-object pattern). Same reconciliation applies.

**Unique to Perplexity**: explicit rows for Anthropic's and OpenAI's own MCP
connector implementations (OAuth-only, no trial/BYOK modeling at the
platform level) — a useful, concrete data point I didn't independently
check. Also more precisely cites the exact standards MCP's auth spec builds
on (RFC 9728 Protected Resource Metadata, RFC 7591 Dynamic Client
Registration, RFC 8414 Authorization Server Metadata).

**Recommendation for RFC-0001**: name Composio, Arcade.dev, and Nango
explicitly as prior art in the Motivation or Provider abstraction section,
with the differentiation stated precisely as "same requirement/resolution
shape, open and portable instead of single-vendor."

## 4. Trial-mode controls

**Agreement**: Both sources landed on adopt/reference throughout, and are
complementary rather than overlapping — I found generic industry
fraud-prevention patterns (risk-based signup scoring, targeted phone
verification per Mistral, multi-axis rate limiting), while Perplexity found
a concrete, well-sourced pricing-mechanics precedent: OpenRouter's actual
BYOK-plus-credits model, which operationalizes RFC-0001's "no silent
conversion to paid" requirement with real numbers (1M free BYOK
requests/month, separate credit-purchase and BYOK-surcharge fees).

**Shared limitation**: both sources flagged the same gap — neither could
independently verify OpenAI's, Anthropic's, or Replicate's specific internal
trial-abuse mechanics from public sources. This is a confirmed, not just
suspected, information gap.

**Recommendation for RFC-0001**: cite OpenRouter's BYOK-plus-credits model
as concrete validating precedent alongside the general risk-scoring/targeted-friction
pattern in the Trial controls section.

## 5. Manifest format precedent

**Agreement**: Both sources independently landed on OpenAPI's
`securitySchemes` vocabulary as the strongest candidate for RFC-0001 to
extend or explicitly map onto, rather than inventing a new shape from
scratch.

**Genuine disagreement — ChatGPT plugin manifest's verdict**: I called it
`differentiate` (its `auth` field models mechanism, not mode — "mode" and
"mechanism" are orthogonal axes). Perplexity called it `adopt/reference`
(direct structural precedent for co-locating a declarative auth
requirement with a tool manifest). Same reconciliation as section 3: adopt
the "declare in a manifest" pattern, differentiate on the mode-vs-mechanism
distinction — both true, different sub-aspects of the same artifact.

**Perplexity is more precise on MCP's server auth model**: where I only
noted an ad hoc per-tool env-var convention (and called it `ignore` — not
prior art, just evidence of the gap), Perplexity correctly identified that
MCP servers actually advertise auth via dynamic discovery (OAuth 2.0
Protected Resource Metadata, RFC 9728) at a well-known endpoint — a
genuinely different mechanism from RFC-0001's static manifest declaration,
and worth RFC-0001 addressing explicitly as an alternative resolution path
rather than dismissing. This is the one place Perplexity's finding
supersedes mine rather than just complementing it.

**Recommendation for RFC-0001**: define an explicit mapping/extension
relationship to OpenAPI's `securitySchemes` vocabulary for the `kind`
field; state that "mode" (trial/BYOK/managed) and "mechanism" (OAuth/API
key/etc.) are orthogonal and both need declaring; and note MCP's dynamic
discovery model as a possible future alternative to static manifest
declaration, not just an implementation detail to ignore.

## 6. Governance/conformance precedent

**Agreement**: Both sources independently converged on OpenID Foundation
and CNCF Certified Kubernetes as the credible templates — self-certification
backed by a free, versioned conformance suite, administered by a neutral
foundation rather than the spec's original authors.

**Unique to Perplexity — the standout finding of this whole synthesis**:
FIDO Alliance's certification program requires an actual **cross-vendor
interoperability testing step**, not just self-attestation against a
written spec. RFC-0001's current Conformance section lists only unilateral,
self-testable categories (manifest validation, resolution determinism,
etc.) with no cross-implementation interop step. This is a concrete,
actionable gap neither the RFC nor my own pass had identified.

**Unique to me**: CNCF's Certified Kubernetes AI Conformance program
(launched November 2025) as the most current and closely analogous
case — a neutral foundation extending an existing conformance model into
the AI space at the same moment Xenia is attempting something similar for
AI credential provisioning.

**Recommendation for RFC-0001**: the Conformance section should specify (a)
who administers the suite, (b) how results and a certified-implementations
registry are published, and (c) — per FIDO's precedent — whether a
cross-implementation interoperability test is required, not just
self-certification. Cite CNCF's Kubernetes AI Conformance program as the
most current comparable case of a neutral foundation doing this exact move
in an adjacent domain.

## Consolidated open gaps

Both sources agree these remain unresolved by prior art and need first-party
design decisions, not more searching:

- **RFC-0001 open question 3** (provider-identifier registry vs.
  reverse-domain naming) — neither source evaluated this in depth; flagged
  by both as needing dedicated follow-up.
- **RFC-0001 open question 4** (compound/multi-provider fallback
  representation) — no prior art found by either source across any
  surveyed manifest format. Both independently concluded this looks like
  genuinely novel RFC-0001 design work, not something to borrow.
- **Trial-abuse specifics at OpenAI/Anthropic/Replicate** — both sources
  hit the same wall (no public documentation); general industry pattern
  (Stripe, Mistral, OpenRouter) is the best available public proxy.
- **No vendor-neutral foundation was identified in the surveyed sources
  specifically for AI credential/secrets provisioning** (one researcher's
  finding) — CNCF's and OpenID's
  precedents are adjacent, not identical, domains. Perplexity's framing of
  this same point: the surveyed sources did not identify a spec combining OpenAPI-style static
  declaration, MCP-style dynamic discovery, and a trial/BYOK/managed
  three-way resolution model in one place — RFC-0001's actual white space.
- **Nango, Paragon, and Merge.dev** were not independently verified in
  depth by either source (Perplexity flagged this explicitly) — spot-check
  before citing them with the same confidence as Composio/Arcade.

## Top-line recommendation

Within the bounded sources and search methods used by these two passes, the
researchers did not identify an equivalent specification combining the
three features they examined: a portable declaration, explicit
trial/BYOK/managed mode semantics, and normative trial controls. This is a
provisional novelty hypothesis, not proof that no equivalent work exists.

The synthesis recommends evaluating cross-vendor interoperability testing
before RFC-0001 leaves Draft, drawing on FIDO as an adjacent precedent.
That recommendation remains **Pending**; applicability, governance, and the
existence of any future conformance program require separate decisions.
