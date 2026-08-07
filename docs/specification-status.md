# Specification status and recommendation register

This register separates research recommendations from specification decisions. Publishing RFC-0001 does not accept it or any recommendation below. Status changes require a pull request with rationale under the [governance process](../GOVERNANCE.md#rfc-lifecycle).

Status vocabulary:

- **Accepted into draft:** reflected in current draft text, without implying RFC acceptance.
- **Rejected:** declined with recorded rationale.
- **Pending:** design decision remains open.
- **Needs verification:** evidence is insufficient, volatile, or not yet checked against primary sources.

## Reconciliation of synthesis recommendations

| Synthesis recommendation | Status | Rationale / next decision |
|---|---|---|
| Relate OAuth-capable handles to OAuth 2.1; track SPIFFE and IETF WIMSE | **Pending** | The relationship is plausible and primary sources were checked, but prescribing an OAuth access token may conflict with the draft's intentionally opaque, mechanism-neutral handle. Requires security and transport design review. |
| State that Xenia sits above pluggable vault backends and is not a vault | **Accepted into draft** | RFC-0001 already says it does not replace secret managers and that provider adapters may perform secret injection. README now makes this boundary explicit; no backend is selected. |
| Name Composio, Arcade, and Nango as prior art; adopt the pattern but differentiate governance | **Needs verification** | Research inputs disagree on verdict framing and the product claims were not re-verified in this publication pass. Preserve as leads until official product documentation is reviewed and dated. |
| Cite OpenRouter pricing/trial mechanics and targeted fraud controls | **Needs verification** | Pricing and program mechanics are volatile. No current primary-source verification was performed in this publication pass. |
| Define an OpenAPI `securitySchemes` mapping and treat mode/mechanism as orthogonal; consider MCP discovery | **Pending** | OpenAPI and MCP primary sources verify the adjacent mechanisms. The mapping itself is a design proposal and requires field-level analysis. |
| Define conformance administration, published results, and possible cross-implementation testing | **Pending** | FIDO and CNCF provide verified adjacent precedents, but Xenia has no conformance suite or governing body. A future RFC must decide applicability. |

## RFC-0001 open decisions

The draft's own five open questions remain **Pending**: handle transport, disclosure fields, provider identifiers, compound requirements, and minimum trial controls. Publication adds no resolution by implication.

## Decision record rules

Each status change must identify the affected recommendation, cite primary evidence where the decision relies on external fact, preserve dissenting research inputs, update RFC text when appropriate, and link the reviewing issue or pull request. Rejection must include rationale. Time-sensitive evidence must be revalidated at decision time.
