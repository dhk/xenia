# Evidence register

Verified dates record a direct review of the linked primary source, not endorsement of a research conclusion. “Time-sensitive” entries require revalidation before a specification decision. Model-generated findings remain non-authoritative even when an underlying source is verified.

| Claim or topic | Primary source | Verified on | Status | Supports / limits |
|---|---|---:|---|---|
| MCP authorization uses OAuth authorization-server behavior and Protected Resource Metadata discovery | [MCP Authorization specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) | 2026-08-07 | **Verified primary-source fact; time-sensitive specification version** | Supports treating MCP authorization as an adjacent mechanism. Does not establish Xenia's mode taxonomy or require a static Xenia manifest. |
| RFC 9728 defines OAuth 2.0 Protected Resource Metadata | [IETF RFC 9728](https://www.rfc-editor.org/rfc/rfc9728) | 2026-08-07 | **Verified primary-source fact** | Supports the MCP discovery description. |
| OpenAPI defines named security schemes and requirements, including OAuth scopes | [OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1.html#security-scheme-object) | 2026-08-07 | **Verified primary-source fact; version-specific** | Supports investigating a mapping. Does not prove Xenia should extend OpenAPI. |
| SPIFFE specifies workload identities using short-lived X.509 or JWT SVIDs | [SPIFFE concepts](https://spiffe.io/docs/latest/spiffe/concepts/) | 2026-08-07 | **Verified primary-source fact; living documentation** | Supports workload-identity comparison. Does not make an SVID equivalent to every proposed credential handle. |
| IETF WIMSE is an active workload-identity working group spanning multiple service platforms | [IETF WIMSE charter](https://datatracker.ietf.org/group/wimse/about/) | 2026-08-07 | **Verified primary-source fact; time-sensitive WG state** | Supports tracking adjacent standards work; does not establish compatibility with Xenia. |
| FIDO certification includes cross-implementation interoperability testing | [FIDO interoperability testing](https://fidoalliance.org/certification/interoperability-testing/) | 2026-08-07 | **Verified primary-source fact; program details time-sensitive** | Supports considering interop testing as one governance precedent, not adopting it automatically. |
| CNCF runs a Kubernetes conformance program based on submitted test results | [CNCF Certified Kubernetes conformance](https://www.cncf.io/training/certification/software-conformance/) | 2026-08-07 | **Verified primary-source fact; program details time-sensitive** | Supports considering public conformance results and neutral administration. |
| Composio / Arcade / Nango share Xenia's requirement-and-resolution shape | Official product documentation not reviewed in this pass | — | **Unverified research lead** | Preserved from model findings; must be checked product-by-product before RFC citation. |
| OpenRouter has a particular BYOK allowance, fee, or trial conversion model | Official pricing/program documentation not reviewed in this pass | — | **Unverified, volatile research lead** | Do not rely on quoted numbers without same-day revalidation. |
| No existing specification combines Xenia's proposed features | No authoritative source can prove an exhaustive absence | — | **Researcher interpretation; bounded search only** | At most supports a provisional novelty hypothesis, not a universal claim. |
| OpenAI, Anthropic, Replicate, RapidAPI trial or abuse-control mechanics | No current primary source verified in this pass | — | **Unverified, volatile research lead** | Must not be stated as current product fact. |

## Evidence classes

- **Verified primary-source fact:** directly checked against the responsible standards body, project, or vendor.
- **Researcher interpretation:** an inference that may combine facts but is not itself stated by a source.
- **Unverified research lead:** retained for follow-up, not suitable as a project claim.
- **Time-sensitive:** may change and must be rechecked before reliance.
