# Research brief: multi-agent, API-driven workflow — landscape scan

Status: **research only** — no implementation planned yet.

Source doc: [`docs/design/multi-agent-api-workflow.md`](https://github.com/dhk/xenia/blob/claude/multi-agent-api-workflow-iev4wq/docs/design/multi-agent-api-workflow.md)
Tracking issue: #3

## Why this brief exists

The design doc sketches a custom, API-driven client built on Anthropic's
Managed Agents API (Agent/Environment/Session/Outcomes/scheduled
deployments/webhooks) to get true concurrency, scheduling, and a
dashboard-style view that Claude Code / Claude Chat don't offer natively.

Before writing any code — and before even committing to the doc's own
"minimal validation prototype" next step — we should find out what already
exists. If a hosted product or open-source framework already solves "run
several agents concurrently, check in async, schedule recurring runs," that
changes the build-vs-wait calculus entirely. This brief scopes that scan; it
is not the scan's findings.

## Research questions

Each maps back to an open question in the design doc:

1. **Scope-fit** — What existing products target personal/admin
   multi-workflow use (job search, finances, admin triage) rather than
   pure software-dev agent orchestration?
2. **Build vs. buy** — Do any hosted dashboards/UIs already sit on top of
   Anthropic's Managed Agents API (or an equivalent Claude-based agent
   runtime) that we could adopt instead of building our own client?
3. **Cost** — What do comparable hosted products charge (flat fee, per-run,
   per-seat), and how does that compare against raw Managed Agents API
   usage plus container time for an "always-on" pattern like scheduled
   deployments?
4. **Scheduling & webhooks** — What patterns do existing tools use for
   cron-triggered agent runs and push-based status updates, so we don't
   reinvent something well-trodden?
5. **UI shape precedent** — What do existing "agent inbox" / board UIs
   actually look like, to help decide dashboard vs. notifications-only vs.
   chat-with-a-picker?

## Areas to survey

**A. Agent orchestration frameworks/runtimes** (open-source, usually
self-hosted): LangGraph + LangGraph Platform, CrewAI + CrewAI Enterprise,
AutoGen/AG2, OpenAI Swarm, Camel-AI, MetaGPT, Agency Swarm — plus
general-purpose durable-execution/scheduling backbones (Temporal, Prefect,
Airflow) as a possible substitute for the doc's own scheduled-deployment
idea.

**B. Hosted multi-agent / "agent inbox" products** (consumer & prosumer):
Lindy.ai, Relevance AI, Gumloop, Zapier Agents/Central, n8n (AI nodes),
Superagent, Composio, Make.com AI, Flowise.

**C. Anthropic-ecosystem specific**: Claude Code on the web / GitHub Actions
integration (i.e., this environment) as a possible "already-hosted"
alternative, Claude Agent SDK reference implementations, any known
third-party dashboards built directly on Managed Agents or the Claude API,
and the Anthropic Console's own session/trace view as a free baseline UI.

**D. Observability/session-management add-ons** that could bolt onto a thin
custom client instead of being built from scratch: LangSmith, AgentOps,
Helicone, Langfuse, Portkey, Humanloop.

**E. Adjacent "personal AI operator" products** worth checking for prior art
on the specific use case (many concurrent personal/admin agents with a
status board): Devin/Cognition's task-board pattern, Factory AI, Multi-On /
Orby, Imbue, Adept.

## What to capture per entry

For each product or framework found:

- What it is, one line.
- Hosted vs. self-hosted.
- Pricing model.
- Native scheduling support (cron/recurring runs)?
- Native webhook/push support, or polling-only?
- Model-agnostic, or tied to a specific vendor (and if so, does it support
  Claude/Anthropic)?
- One-line verdict on relevance to Xenia's use case.

## Deliverable

A findings doc (comparison table plus notes) under `docs/research/`,
feeding back into the design doc's open questions — specifically
"build vs. wait" and "UI shape" — for discussion on issue #3.

## Out of scope

- No implementation or prototyping.
- No vendor selection or recommendation yet — this pass is landscape-gathering
  only; a recommendation is a follow-up once findings are in.

## Suggested next step

Run the scan across areas A–E above, produce the findings doc, and reconvene
on issue #3 before deciding whether the design doc's proposed "minimal
validation prototype" (one Agent + one scheduled Session + a webhook →
notification) is still the right first step or whether an existing product
already covers it.
