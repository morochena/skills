# Skills

Personal skills for agent-led software development.

This is an opinionated workflow package for working with coding agents while keeping the human in charge of taste, scope, and direction. The skills are designed for a style of development where the agent does more of the mechanical work, while the developer keeps the important judgment calls visible: what problem is being solved, what complexity is worth introducing, what should be verified, and which project truths should become durable context.

## Rationale

Agent-led development works best when the agent has enough structure to move quickly, but not so much process that every task turns into ceremony.

These skills aim for a few defaults:

- **Explicit invocation.** Skills should be called when they are useful, not constantly inferred in the background.
- **Code as communication.** Implementation should be optimized for future readers, not just for getting a diff to pass.
- **Minimize complexity.** Prefer straightforward code, clear names, and local patterns. Avoid abstractions that add more cognitive load than they remove.
- **Pragmatic verification.** Tests and checks should buy confidence. They are tools, not rituals.
- **Canon over sediment.** Durable project truth belongs in `docs/canon/`. Temporary plans, ADR drafts, roadmaps, and generated notes should not quietly become permanent instructions.
- **Parallel where useful.** Medium and large work should be shaped into independent streams when possible, with one coordinating agent session delegating to worker agents when the platform supports it.

The intended value is a calmer workflow: clarify the work, preserve the important context, plan for parallel execution when it helps, implement with readable defaults, and clean up the documentation surface afterward.

## Skills

| Skill | Use |
| --- | --- |
| `start-work` | Choose the right workflow for a task. |
| `brainblast` | Explore ideas from multiple angles before shaping or planning. |
| `shape-work` | Clarify fuzzy work and settle durable domain language. |
| `plan-work` | Create a parallelizable implementation plan for one coordinating agent. |
| `do-work` | Execute a plan, using worker agents in the current workspace where useful. |
| `review-work` | Review implementation quality, clarity, scope, tests, and polish. |
| `debug-work` | Diagnose broken, flaky, slow, or surprising behavior. |
| `canonize` | Normalize `docs/canon/` and remove planning sediment. |
| `canonize-mark` | Normalize canon while preserving and marking non-canonical docs. |

## Intended Usage

Start with the smallest useful workflow.

For clear tasks, ask the agent to do the work directly. For fuzzy implementation work, use `start-work` or `shape-work` first. For medium and large implementation work, use `plan-work` to expose independent streams, blocking edges, integration points, and verification strategy before running `do-work`.

```txt
start-work
  -> direct action for trivial/small clear tasks
  -> shape-work for fuzzy medium/large work
  -> plan-work for coordinated or parallelizable work
  -> do-work for implementation
  -> review-work for post-build quality review
  -> canonize for documentation hygiene
```

`brainblast` and `debug-work` sit outside the main implementation workflow. Use `brainblast` before shaping when the idea is still exploratory. Use `debug-work` when the problem is broken behavior rather than planned product work.

The suite is explicit-invocation by default. Each skill opts out of implicit invocation so the agent does not pull in extra workflow unless you ask for it.

## Routing Logic

`start-work` routes implementation work by complexity and clarity, not by a fixed process checklist.

```mermaid
flowchart TD
  A["Implementation task context"] --> B{"How complex is it?"}
  B -->|"Trivial"| T["Do directly"]
  B -->|"Small"| S1["Brief chat plan"]
  S1 --> D1["Do directly"]
  B -->|"Medium"| M{"Are requirements settled?"}
  M -->|"No"| SH["shape-work"]
  M -->|"Yes"| P["plan-work"]
  B -->|"Large"| SH
  SH -->|"Ready to execute"| P
  P --> DW["do-work"]
  DW --> R{"Need quality pass?"}
  R -->|"Yes"| RW["review-work"]
  R -->|"No"| C{"Durable docs changed?"}
  RW --> C
  C -->|"Yes"| CZ["canonize"]
  C -->|"No"| Done["Done"]
  CZ --> Done
```

| Branch | Use when | Default next move |
| --- | --- | --- |
| Trivial | The task is obvious, local, and low-risk. | Do it directly. |
| Small | Requirements are clear, but a short assumption check helps. | Brief chat plan, then implement. |
| Medium | Several files, domain terms, or design choices are involved. | `shape-work` if fuzzy; otherwise `plan-work`. |
| Large | Multiple areas, blocking edges, or parallel streams are likely. | `shape-work`, then `plan-work`, then `do-work`. |

Adjacent modes:

| Mode | Use when | How it rejoins |
| --- | --- | --- |
| `brainblast` | The idea may be interesting, but is not requirements yet. | Hand off to `shape-work` or `plan-work` only if the idea becomes concrete. |
| `debug-work` | Something is broken, slow, flaky, or surprising. | Fix directly when obvious; otherwise hand off to `shape-work`, `plan-work`, or `do-work` depending on what the diagnosis reveals. |

## Agent Compatibility

The core skill instructions live in `SKILL.md` and are written to be agent-neutral. They assume only that an agent can read files, inspect a codebase, edit files when asked, and optionally coordinate worker agents when the host platform supports that.

Some skill directories include `agents/openai.yaml` metadata for UI labels and invocation policy in OpenAI-compatible skill environments. Other agent runtimes can ignore that metadata and use the `SKILL.md` files directly.

## Workflow Shape

### `start-work`

Use this when the path is unclear. It classifies the task and recommends the smallest workflow that fits: direct action, shaping, planning, debugging, reviewing, or documentation cleanup.

`start-work` works best after the agent has at least a little context. You can invoke it at the beginning with a rough idea, or after chatting for a while when the conversation starts turning into real work.

Example:

```txt
User: I'm thinking about adding team invites. I want people to invite coworkers,
but I don't want to accidentally build a whole enterprise org model.

Agent: <asks a few clarifying questions or discusses tradeoffs>

User: Use $start-work to decide how we should approach this.

Agent: Recommendation: this is medium product/engineering work. Use $shape-work
first to settle the domain language and boundaries, then $plan-work once the
invite flow is clear. Keep the plan in chat unless it grows into a broader
account/team model change.
```

You can also start with it directly:

```txt
User: Use $start-work. I want to add team invites without overbuilding the
account model.
```

### `brainblast`

Use this when an idea is interesting but not ready to become requirements. It reads product context when available, explores the idea through several lenses, synthesizes promising directions, and asks which thread to pull next. It stays chat-first and does not write canon, create plans, or start implementation by default.

### `shape-work`

Use this when the idea is still fuzzy. The agent interviews one decision at a time, recommends answers, looks up codebase facts instead of asking for them, and updates `docs/canon/language.md` only when durable language has actually settled.

### `plan-work`

Use this when the work needs coordination. The plan identifies scope, non-goals, parallel streams, blocking edges, integration points, verification strategy, and a full-scope check so important work is not silently deferred.

Small and medium plans usually stay in chat. Large plans may be written to:

```txt
docs/plans/<slug>.md
```

Those files should use temporary frontmatter and later be absorbed or removed by `canonize`.

### `do-work`

Use this to execute a plan. The main agent session acts as coordinator and final integrator. Worker agents can handle independent streams in the current workspace when the platform supports them, but shared interfaces, architecture, and final verification stay with the coordinator.

Branches or worktrees are not the default. Use them when you explicitly want checkout isolation.

### `review-work`

Use this after implementation or when reviewing a diff. It focuses on correctness, scope fidelity, readability, complexity, naming, abstraction quality, pragmatic test coverage, performance, polish, and edge cases.

### `debug-work`

Use this for broken, flaky, slow, or surprising behavior. It is a diagnosis loop: state the claim, gather facts, reproduce or narrow the signal, localize the fault, test hypotheses, then fix or brief the fix.

### `canonize` and `canonize-mark`

Use these to keep project documentation trustworthy. `canonize` absorbs durable truth into `docs/canon/` and removes stale planning sediment. `canonize-mark` keeps non-canonical docs in place but marks them so agents know they are not trusted canon.

## Install

This is a multi-skill package intended for use with [skills](https://skills.sh).

From GitHub:

```bash
# List skills
npx skills add morochena/skills --list

# Install all skills globally
npx skills add morochena/skills -g --skill '*' -y

# Install one skill globally
npx skills add morochena/skills -g --skill start-work
```

From a local checkout while developing:

```bash
npx skills add /Users/morochena/projects/skills --list
npx skills add /Users/morochena/projects/skills -g --skill '*' -y
```

Omit `-g` to install into the current project only. Use `-a <agent>` to target a specific agent ecosystem.
