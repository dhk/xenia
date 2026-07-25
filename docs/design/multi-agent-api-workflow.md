# Multi-agent, API-driven workflow — discussion doc

Status: **discussion only** — no implementation planned yet. This doc exists to
capture the idea, the options, and the open questions so we can decide later
whether (and how) to build it.

## Problem

Work happens across a lot of concurrent, unrelated threads (job search,
finances, side projects, admin, etc.), and the Claude Code / Claude Chat
interface is built around **one conversation at a time**. There's no native
way to:

- run several independent agent workflows concurrently
- check in on them asynchronously instead of babysitting a single chat
- schedule recurring agent work (nightly triage, weekly reports, etc.)
- build a custom view over "what's running / what's done / what needs me"

## Goals

- Understand what an API-driven, multi-agent setup would actually look like
  before committing to building it.
- Identify which parts Anthropic already hosts vs. what we'd have to build
  and maintain ourselves.
- Produce a short list of open questions to resolve before writing any code.

## Non-goals (for now)

- No implementation. No repo scaffolding beyond this doc.
- No commitment to a specific tech stack for the eventual client.

## Comparison

| | Claude Code (this interface) | Claude Chat | Custom API client (Managed Agents) |
|---|---|---|---|
| Interface | Fixed, terminal/session-oriented | Fixed, chat-oriented | Whatever we build |
| Concurrency | One conversation at a time | One conversation at a time | N independent sessions/threads natively |
| Tool execution | Local machine / this sandbox | Anthropic-hosted, limited | Anthropic-hosted container per session, or self-hosted |
| Scheduling | None native | None | Scheduled deployments (cron-triggered sessions) |
| Persistence across runs | Session-based | No | Memory stores, versioned agent configs |
| Effort to get value | Zero | Zero | We own the client (auth, session lifecycle, UI); Anthropic runs the agent loop + sandbox |

The trade-off in one sentence: **Managed Agents removes the "one thing at a
time" constraint, but we own the interface.** Anthropic still runs the agent
loop and the tool-execution sandbox — we're not building an agent runtime,
just the orchestration and UI around it.

## Proposed building blocks (Anthropic Managed Agents API)

- **Agent** — a persisted, versioned config: model, system prompt, tools, MCP
  servers, skills. Created once, referenced by ID from every session.
- **Environment** — a reusable sandbox template (networking rules, etc.)
  that sessions run in.
- **Session** — one running instance of an agent against an environment.
  Produces an event stream (`agent.message`, `agent.tool_use`,
  `session.status_idle`, ...) and accepts events in (`user.message`,
  `user.tool_confirmation`, ...).
- **Multi-agent coordination** — one "coordinator" agent can delegate to a
  roster of sub-agents, each running in its own thread with its own context.
  Threads persist, so a sub-agent can be revisited later rather than
  re-spawned from scratch.
- **Outcomes** — instead of a plain chat loop, define a rubric ("what does
  done look like") and let the harness iterate → grade → revise until it
  passes or hits a limit. Fits fire-and-forget background work.
- **Scheduled deployments** — cron-triggered sessions (e.g. nightly triage,
  weekly compliance scan) with per-firing run records.
- **Webhooks** — Anthropic can push session state changes to an HTTPS
  endpoint instead of us holding N SSE connections open, which is what makes
  a dashboard-style UI practical at any scale beyond a handful of sessions.

## Sketch of what "our own interface" could look like

A thin service that:
1. Owns a small set of Agent configs (one per recurring activity type, or
   one per "workspace" — job search, finances, etc.), version-controlled as
   YAML.
2. Creates a Session per unit of work, optionally via a scheduled deployment
   for recurring ones.
3. Registers a webhook endpoint to receive state-change notifications
   instead of polling.
4. Renders a simple board/list view: one row per session, status, last
   message, link to the full trace (Anthropic's own Console trace view works
   for free during early stages — `platform.claude.com/workspaces/.../sessions/{id}`).
5. Optionally exposes a "reply" action per session that posts a
   `user.message` event back in.

This is deliberately close to the minimum viable version — a session list
plus a way to nudge one — rather than a bespoke chat UI.

## Open questions to resolve before building anything

- **Scope**: is this for personal/admin workflows only (job search, finances,
  etc.), or does it need to support arbitrary/dev workloads too?
- **Hosting**: where does the thin client/service live — same box as this
  session, a small always-on service, or serverless-triggered?
- **Auth model**: single-user (one API key) is simplest; anything beyond that
  adds real complexity we don't need yet.
- **UI shape**: dashboard/board vs. chat-with-a-picker vs. notifications-only
  (webhook → push notification, no dashboard at all).
- **Cost model**: Managed Agents sessions bill like any other Claude API
  usage (plus container time) — worth a rough usage estimate before
  committing to "always-on" patterns like scheduled deployments.
- **Build vs. wait**: is the gap painful enough today to justify building a
  client, or is this better revisited once a specific recurring workflow
  (e.g. weekly reset, job search triage) proves it needs true concurrency?

## Next steps (not started)

- [ ] Decide on scope and UI shape (see open questions above)
- [ ] Prototype: one Agent + one scheduled Session + webhook → notification,
      no dashboard, to validate the mechanics cheaply
- [ ] Only then consider a dashboard/board UI

See also: the `claude-api` skill's Managed Agents documentation for full API
reference (agents, sessions, environments, events, outcomes, multi-agent,
webhooks, scheduled deployments).
