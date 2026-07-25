# Xenia

**Hospitality for tools.**

Xenia is an open credential-provisioning contract and reference implementation for tools that need third-party API access. It lets a tool declare what credentials it requires while the host platform decides how to satisfy that requirement using a trial token, a user-provided key, or a managed credential.

> Any host. Any tool. One credential contract.

## Why Xenia

Tool authors should not have to build bespoke credential setup, storage, fallback, and error handling for every host. Hosts should not have to reverse-engineer each tool's assumptions. Xenia creates a vendor-neutral boundary between them.

The core design principle is simple:

> Credentials are a platform concern, not a tool concern.

## Credential modes

- **Trial** — a limited platform- or provider-funded token used for evaluation and onboarding.
- **BYOK** — a key supplied and controlled by the user or organization.
- **Managed** — a credential provisioned and governed by the host platform.

A tool declares the modes it supports. The host resolves an eligible credential according to user choice, organizational policy, availability, and explicit fallback rules.

## Repository contents

- [`docs/rfcs/0001-credential-provisioning-contract.md`](docs/rfcs/0001-credential-provisioning-contract.md) — initial design proposal
- [`PRINCIPLES.md`](PRINCIPLES.md) — non-negotiable project principles
- [`GOVERNANCE.md`](GOVERNANCE.md) — governance and decision-making
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow
- [`SPEC-LICENSE.md`](SPEC-LICENSE.md) — CC BY 4.0 licensing notice for specifications

## Project status

Xenia is at the RFC stage. The manifest schema, resolution engine, SDKs, and conformance suite are not yet implemented.

## Licensing

Reference code and SDKs are licensed under the MIT License. Specifications are licensed under Creative Commons Attribution 4.0 International. Project names and compatibility marks are governed separately; see the RFC and governance documents.
