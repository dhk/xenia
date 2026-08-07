# Governance

Xenia is an open, vendor-neutral project focused on interoperable credential provisioning for tools.

## Decision-making

Substantive technical changes begin as GitHub issues and, when they affect the contract or architecture, as numbered RFCs. Decisions are made in public through review and documented rationale.

Maintainers seek rough consensus, with particular weight given to security, interoperability, implementation experience, and conformance impact. When consensus cannot be reached, maintainers record the alternatives and make an explicit decision.

## Change process

1. Open an issue describing the problem and intended outcome.
2. Create a branch linked to the issue.
3. Submit changes through a pull request.
4. Obtain review and satisfy applicable checks.
5. Merge through GitHub; do not push substantive changes directly to `main`.

Small editorial corrections may skip a standalone RFC but still use a pull request.

## RFC lifecycle

The normal path is **Research → Draft → In review → Accepted → Experimental implementation → Stable**.

- **Research:** prior art, problem framing, and evidence collection; no normative proposal.
- **Draft:** a numbered proposal is published for iteration. RFC-0001 is currently here.
- **In review:** maintainers explicitly request a decision after evidence and open questions are ready.
- **Accepted:** the project agrees to the specified direction. Acceptance does not imply implementation.
- **Experimental implementation:** one or more implementations test the accepted design; compatibility is not yet stable.
- **Stable:** the contract and applicable conformance expectations are suitable for compatibility commitments.

An RFC may instead become **Rejected**, **Withdrawn**, or **Superseded**. A status changes only through a pull request that updates the RFC header, records rationale and dissent, links the deciding issue or pull request, and updates any recommendation register. Research synthesis, publication, implementation, or maintainer commentary does not change status implicitly.

## Maintainers

Maintainers are responsible for repository administration, release integrity, security response, review quality, and faithful application of these governance rules. Maintainer status should reflect sustained, constructive contribution and may be granted or removed through a documented maintainer decision.

## Vendor neutrality

No organization receives privileged control over the specification, conformance profiles, or compatibility marks. Provider-specific functionality must be expressed through general extension points whenever practical.

## Compatibility marks

The project name, logo, and compatibility marks are governed separately from the MIT and CC BY 4.0 licenses. A compatibility mark may be used only by implementations that satisfy the applicable published conformance profile. Requirements will be objective, public, and equally available.

## Security

Potential vulnerabilities should not be disclosed in a public issue until coordinated disclosure is complete. A private reporting process will be added before the first executable release.

## Amendments

Changes to this document require a pull request with a clear rationale and maintainer approval.
