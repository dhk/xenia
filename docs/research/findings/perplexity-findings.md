---
source: Perplexity AI Research Assistant
date: 2026-07-26
brief: docs/research/credential-provisioning-research-brief.md
---

# Findings: credential provisioning prior-art scan — Perplexity AI Research Assistant

## 1. Provider abstraction / non-goals boundary

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OAuth 2.1 | IETF draft authorization framework; access tokens are explicitly designed to be short-lived to reduce blast radius of a leaked token [web:18] | Directly overlaps with `credential_handle`'s "short-lived, audience-bound handle" property; OAuth already standardizes token issuance, expiry, and scope | adopt/reference |
| OIDC | Identity layer on top of OAuth 2.0 for authentication | Not directly addressed in RFC-0001 body; RFC's non-goals explicitly exclude "defining a universal identity protocol" [cite:3] | ignore |
| SPIFFE/SPIRE | CNCF-graduated workload identity framework issuing short-lived, audience-bound SVIDs (X.509 or JWT) via a local Workload API, with automatic rotation before expiry [web:8][web:9] | Nearly identical value proposition to `credential_handle`: "no secrets on disk, no tokens in environment variables, automatic rotation" | adopt/reference |
| AWS STS / GCP Workload Identity Federation | Cloud-native mechanisms exchanging external identity assertions for short-lived, keyless cloud credentials (used underneath SPIFFE-to-cloud bridges) [web:5][web:6][web:15] | Same "durable secret → short-lived scoped token" pattern the RFC lists as a non-goal to replace | differentiate |
| IETF WIMSE working group | Emerging standardization effort for workload identity in multi-service environments, unifying SPIFFE/OIDC bridge patterns [web:9] | Not mentioned in RFC-0001; represents the standardization trajectory this space is already moving toward | adopt/reference |

Notes:
- RFC-0001's Non-goals section already disclaims "replacing OAuth, OIDC, cloud secret managers, or provider-native key systems" [cite:3], which is the correct posture — the risk is not conceptual duplication but insufficiently explicit layering language around `credential_handle` vs. STS/SPIFFE tokens.
- The RFC's "Provider abstraction" section states "Xenia does not normalize provider APIs... Provider adapters MAY implement OAuth exchange, token refresh" [cite:3], which is consistent with treating OAuth 2.1/WIF as the substrate, not a competitor.
- OAuth 2.1: RFC-0001 should cite it as the mechanism many BYOK/managed sources will use under the hood, not redefine it.
- OIDC: RFC already scopes this out correctly.
- SPIFFE/SPIRE: RFC-0001's Extensibility section should explicitly list SPIFFE/SVID as a compatible future credential kind rather than let `credential_handle` look like a reinvention.
- AWS STS / GCP WIF: RFC-0001 should clarify that `credential_handle` operates at the tool-invocation layer (host↔tool), while STS/WIF operate at the workload↔cloud-provider layer; these compose rather than compete.
- IETF WIMSE: flag as a forward-looking dependency to watch, since Xenia's "future credential kinds" section overlaps its scope.

## 2. Credential vault / secret lifecycle

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| HashiCorp Vault | Control plane for dynamic secrets, auth methods, policies, leases, audit logs; supports KV, database, cloud, and transit secret engines with rotation and revocation [web:60][web:52] | Directly overlaps with RFC's "Credential Vault" component in the runtime flow diagram and BYOK controls ("encrypted storage using a secret manager or equivalent") [cite:3] | adopt/reference |
| AWS/GCP/Azure Secrets Manager | Cloud-native managed secret storage with rotation and IAM-scoped access | Same overlap as Vault; especially relevant to the RFC's "Managed" credential mode, which the host governs for rotation and billing attribution [cite:3] | adopt/reference |
| Doppler / Infisical / 1Password Secrets Automation | Developer-focused secret managers with rotation, environment sync, and audit trails | Overlaps with BYOK control requirements: "rotation and revocation," "audit events without secret values" [cite:3] | adopt/reference |

Notes:
- RFC-0001 already correctly avoids re-specifying rotation/audit mechanics in depth, deferring to "an appropriate secret system" for BYOK storage [cite:3] — this is the right boundary, but the RFC would benefit from a short explicit statement that Xenia is a resolution/brokering layer sitting above existing vault products rather than a vault itself.
- No existing secret manager natively models the "trial vs BYOK vs managed" three-way mode taxonomy — this is the genuine novel contribution of RFC-0001 within this domain.
- HashiCorp Vault: RFC-0001 should explicitly say the Credential Vault role can be satisfied by Vault (or equivalent) rather than imply Xenia invents vault mechanics.
- Doppler/Infisical/1Password: RFC-0001 could explicitly note these as acceptable pluggable vault backends in a future implementation guide, without RFC text itself needing changes.

## 3. AI-tool-specific prior art

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| MCP Authorization spec | MCP servers MUST implement OAuth 2.0 Protected Resource Metadata (RFC 9728); MCP clients use OAuth 2.1 + PKCE, Dynamic Client Registration (RFC 7591), Authorization Server Metadata (RFC 8414) [web:19][web:24][web:28] | Overlaps heavily with RFC-0001's "Resolution model" and manifest concept, but MCP's auth spec is scoped to a single mode (OAuth), not trial/BYOK/managed | differentiate |
| ChatGPT plugin manifest auth types (`none`/`service_http`/`user_http`/`oauth`) | Legacy `ai-plugin.json` manifest declares one of four auth types per plugin [web:32][web:33][web:27] | Direct precedent for RFC-0001's manifest `accepted_modes` field, but plugin manifests only support a single static auth type per plugin, no multi-mode fallback/resolution model | adopt/reference |
| Composio | Unified auth platform; "Auth Config" is a blueprint defining auth method (OAuth2/bearer/API key), scopes, and per-user "Connected Accounts" [web:34][web:36][web:38] | Nearly identical conceptual shape to RFC-0001: Composio's Auth Config ≈ Xenia's credential requirement; Connected Account ≈ resolved credential source | adopt/reference |
| Arcade.dev | Tool-authorization layer for MCP tools; handles user authorization via OAuth providers, "Authorized Tool Calling" pattern [web:45][web:48] | Overlaps with RFC's "Missing-credential experience" (structured action states) and BYOK controls | adopt/reference |
| Nango / Paragon / Merge.dev | iPaaS-style unified integration connection managers (not directly retrieved in this pass; well-known category) | Same "declare requirement, host resolves connection" pattern as Composio/Arcade | adopt/reference |
| n8n / Zapier / Make (iPaaS connection models) | Workflow platforms with per-node "credential" objects reusable across workflow steps | Overlaps with RFC's manifest requirement `id` per credential and reuse across tool invocations | adopt/reference |
| Anthropic MCP connector | Claude's Messages API MCP connector supports remote MCP servers with per-server OAuth, `mcp_servers` config entries [web:90][web:92] | Overlaps with RFC's runtime flow (Host→Resolver→Tool→Provider) but is OAuth-only and lacks trial/BYOK explicit modeling | differentiate |
| OpenAI MCP and Connectors | OpenAI-maintained connectors for remote MCP servers and tool-calling credential injection [web:93] | Same category as Anthropic's connector; injects credentials at platform level without trial/BYOK distinction | differentiate |

Notes:
- This is the strongest area of genuine prior art collision: Composio, Arcade, and iPaaS platforms already implement "tool declares a requirement, platform resolves a credential" as a product pattern, just not as an open, vendor-neutral spec.
- RFC-0001's unique angle versus all of these is (a) the open/portable manifest format independent of any single platform, and (b) explicit normative language around trial abuse control and no-silent-conversion — none of Composio/Arcade/Nango treat trial-vs-paid transition as a spec-level concern.
- MCP's authorization spec is the most likely target for future alignment or explicit interop mapping, since both operate in the same ecosystem and MCP is already gaining momentum as the interoperability layer for tool-calling [web:20][web:23].
- MCP Authorization spec: RFC-0001 is broader (covers non-OAuth static keys, trial semantics, multi-mode resolution) than MCP auth, which only standardizes the OAuth handshake between client and server. Xenia could be pitched as a superset/complement to MCP auth rather than a competitor.
- ChatGPT plugin manifest: the four-type taxonomy is a useful naming precedent, but Xenia's multi-mode-per-requirement design with host-side resolution is genuinely more advanced (the plugin format was deprecated in favor of Custom GPTs/MCP anyway).
- Composio: closest existing commercial analog; RFC-0001 should acknowledge Composio (and similar unified-auth platforms) as evidence the pattern is viable, and consider whether Xenia is standardizing what Composio already does proprietarily.
- Arcade.dev: evidence base for the missing-credential UX flow patterns RFC-0001 proposes.
- Nango/Paragon/Merge.dev: same verdict as Composio; treat as corroborating prior art, not a source RFC-0001 must extend.
- n8n/Zapier/Make: validates the requirement-scoped-credential-object pattern but these tools don't have trial/BYOK/managed as first-class modes.
- Anthropic MCP connector / OpenAI MCP and Connectors: RFC-0001's mode taxonomy exceeds what Anthropic/OpenAI currently expose at the platform level.

## 4. Trial-mode controls

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OpenRouter BYOK model | Offers 1,000,000 free BYOK requests per month, plus a credit-purchase fee and a BYOK surcharge; free tier and pay-as-you-go coexist without silent conversion [web:62][web:50][web:56] | Direct precedent for RFC's "no silent conversion to paid" requirement and the BYOK/trial coexistence model [cite:3] | adopt/reference |
| OpenRouter free tier / rate limits | Documented free tier with usage limits enforced per account [web:51][web:58] | Overlaps with RFC's trial control requirements: "rate and spend limits," "clear quota reporting" [cite:3] | adopt/reference |
| RapidAPI trial/rate-limiting | Not retrieved with full detail in this pass; known industry pattern of per-key rate limiting and quota tiers on API marketplaces | Overlaps with "per-user or per-organization attribution" and "abuse controls" in RFC-0001's Trial controls section [cite:3] | adopt/reference |
| Anthropic/OpenAI trial credits | Known industry pattern of onboarding credits with expiration, not independently re-verified via search in this pass | Overlaps with RFC's "expiration and revocation" and "provider-specific terms surfaced before activation" [cite:3] | adopt/reference |

Notes:
- The clearest, best-sourced precedent found is OpenRouter's explicit BYOK-plus-credits model, which already operationalizes RFC-0001's "no silent conversion" principle at the pricing-mechanics level.
- Could not independently re-verify RapidAPI's or Anthropic/OpenAI's specific trial-abuse mechanics with fresh sources in this pass; called out under Open gaps rather than asserted from memory.
- RapidAPI row: could not fully verify current abuse-control specifics in this session; flagged as an open gap.
- Anthropic/OpenAI trial credits row: not independently re-confirmed this session; treated as consistent with general industry norm, flagged as unverified.

## 5. Manifest format precedent

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OpenAPI security schemes | OpenAPI 3.0/3.1 defines `apiKey`, `http`, `oauth2`, `mutualTLS`, `openIdConnect` security scheme types declared in a `securitySchemes` object [web:64][web:67][web:73] | Overlaps with RFC-0001's manifest `kind` field (e.g., `api-key`) and `scopes` list; OpenAPI already has a mature, widely-tooled schema for exactly this declaration | adopt/reference |
| ChatGPT plugin manifest (`ai-plugin.json`) | JSON manifest requiring an `auth` object with `type` and provider-specific fields; sits alongside an OpenAPI spec for the actual API surface [web:32][web:33] | Directly overlaps with RFC-0001's `accepted_modes` and `user_message` fields; both are host-facing declarative credential descriptions co-located with a tool description | adopt/reference |
| MCP server auth config | MCP servers advertise OAuth 2.0 Protected Resource Metadata per RFC 9728, discoverable via well-known endpoints rather than a static manifest field [web:19][web:28] | RFC-0001's manifest declares modes statically per requirement; MCP instead does dynamic discovery via metadata endpoints — different mechanism, same goal | differentiate |

Notes:
- The strongest recommendation across all six sections: RFC-0001's YAML manifest shape (`id`, `provider`, `kind`, `accepted_modes`, `scopes`, `constraints`) has enough structural overlap with OpenAPI `securitySchemes` that the spec should explicitly define a mapping or extension relationship, rather than leave the manifest looking like an independent invention.
- The RFC's Open Questions section already asks "Should provider identifiers use a central registry or reverse-domain names?" [cite:3] — OpenAPI and the plugin manifest precedent both suggest namespaced/reverse-domain identifiers are the common convention worth adopting directly.
- OpenAPI security schemes: strong candidate for RFC-0001 to extend rather than invent a new shape; the RFC's YAML `credentials` block could map fields like `kind`/`scopes` directly onto OpenAPI's `securitySchemes` vocabulary for interoperability with existing OpenAPI tooling.
- ChatGPT plugin manifest: useful naming/structure precedent but now largely deprecated in favor of MCP, so not worth extending as the primary spec target.
- MCP server auth config: RFC-0001's manifest is closer to OpenAPI/plugin-manifest style (static declaration) than MCP's dynamic discovery model; the RFC should note this distinction explicitly since a future revision may want to support MCP-style dynamic discovery as an alternative resolution path.

## 6. Governance/conformance precedent

| Entry | What it is | RFC-0001 concept overlap | Verdict (adopt/reference / differentiate / ignore) |
|---|---|---|---|
| OpenID Foundation certification | Self-certification program with conformance test suites; recently expanded to independent conformance testing for new profiles (e.g., OpenID for Verifiable Credentials) [web:76][web:78] | Directly analogous to RFC-0001's planned "future compatibility mark," gated on passing a conformance suite [cite:3] | adopt/reference |
| FIDO Alliance certification (Functional + Interoperability Testing) | Two-track program: Functional Certification measures spec compliance, Interoperability Testing is a required, remotely-run cross-vendor test step before certification is granted [web:79][web:80][web:89] | Same "conformance suite gates use of a mark" structure RFC-0001 proposes [cite:3] | adopt/reference |
| CNCF Certified Kubernetes | Vendors submit conformance test results (Sonobuoy-based) for CNCF review; requires four submission files and public, versioned conformance test definitions tied to each Kubernetes release [web:65][web:66][web:68] | Same "test suite + registry of certified implementations" pattern | adopt/reference |

Notes:
- Across all three precedents, credibility hinges on three ingredients RFC-0001 should make explicit: (1) a versioned, publicly available, automatable conformance test suite (not just prose requirements); (2) an actual cross-implementation interoperability testing step (FIDO's strongest differentiator) rather than isolated self-certification; (3) a neutral governance body distinct from any single vendor holding trademark/mark rights, which RFC-0001 already gestures at ("no privileged vendor implementation," marks "governed by transparent conformance requirements") [cite:3].
- RFC-0001's current Conformance section lists test categories but does not yet specify who administers the suite, how results are published, or whether cross-implementation interop testing (vs. solo self-testing) will be required — this is the main gap versus FIDO/CNCF/OIDF precedent.
- OpenID Foundation: OIDF's model of self-certification backed by a public, versioned test suite and a public certified-implementations registry is a credible template for Xenia's mark.
- FIDO Alliance: the key credibility lesson is that FIDO requires actual cross-vendor interoperability testing, not just self-attestation against a written spec; RFC-0001's conformance section currently lists only unilateral test categories (manifest validation, resolution determinism, etc.) without a cross-implementation interop step.
- CNCF Certified Kubernetes: the credibility factor here is transparent, automatable, machine-checkable conformance tests plus a public registry of who has passed, tied to a governance body distinct from any single vendor.

## Open gaps

- Could not independently re-verify current RapidAPI trial/rate-limiting mechanics or Anthropic/OpenAI/Replicate trial-credit abuse controls with fresh sources in this pass; these were referenced only at a general industry-pattern level and should be re-checked directly against current provider documentation.
- Nango, Paragon, and Merge.dev were not individually retrieved with source-level detail in this session (search coverage focused on Composio/Arcade as representative unified-auth platforms); their specific auth/connection models should be spot-checked before treating the "unified-auth platform" verdict as fully validated across all five named vendors.
- No direct evidence was found of any existing spec that already combines OpenAPI-style static security-scheme declaration with MCP-style dynamic discovery and a trial/BYOK/managed three-way resolution model — this appears to be RFC-0001's genuine white space, but this absence-of-evidence conclusion should be treated as provisional given search-based methodology.
- The RFC's own Open Questions (credential-handle transport standardization, mandatory manifest fields for billing/privacy disclosure, central registry vs. reverse-domain provider identifiers, compound/multi-provider fallback representation, minimum trial-support controls) were not independently resolved by this research pass and remain genuinely open design decisions rather than prior-art gaps.
