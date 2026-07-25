# Project Principles

Xenia is guided by the following non-negotiable principles.

## Credentials are a platform concern

Tools declare requirements. Hosts resolve, protect, and govern credentials. Tool authors should not rebuild secret-management systems.

## User choice is explicit

Trial, BYOK, and managed modes may differ in billing, privacy, retention, capability, and policy. Material transitions require disclosure and consent.

## Secrets stay out of model context

Durable credentials do not belong in prompts, conversation history, manifests, ordinary logs, analytics, or test fixtures.

## Determinism over magic

Credential resolution must be predictable, explainable, testable, and auditable. Hidden fallback is a bug.

## Least privilege by default

Credentials and handles should be limited by scope, audience, tool, tenant, region, and lifetime.

## Open interoperability

The specification, reference implementation, and conformance process should enable multiple independent hosts and tool ecosystems.

## Vendor neutrality

No provider, host, or implementation receives privileged treatment in the specification or compatibility program.

## Progressive adoption

A tool can begin with static API-key support and evolve toward delegated or workload credentials without abandoning the contract.

## Honest trials

Trials are for evaluation and onboarding. They must have clear limits, attribution, revocation, and no silent conversion to paid usage.

## Compatibility is earned

Compatibility claims should correspond to published profiles and conformance tests, not marketing language alone.
