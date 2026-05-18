# Agent-Ready Repo Kit

Make a repo easier for Claude Code, Codex, Cursor, and other coding agents to understand, edit, verify, and avoid damaging.

This is not a prompt dump. It is a small operating system for repo context:

- `AGENTS.md` templates for durable coding-agent behavior.
- Skills that interview the user, inspect the codebase, and write useful context.
- Mermaid and Excalidraw workflows for diagram-first repo understanding.
- MCP and Composio guidance for tool use without guesswork.
- Static text hygiene rules so agent docs do not rot.
- Lightweight safety review for secrets, auth, MCP boundaries, and risky tool access.

## Why This Exists

Coding agents work much better when the repo tells them:

- what conventions are stable
- what commands verify work
- what mistakes have happened before
- what domain terms mean
- what diagrams explain the system shape
- what tools are allowed
- what context is too volatile to memorialize

Most repos either have no agent context or have a giant stale instruction file. This kit aims for the middle: short, durable, practical context that agents can actually follow.

## Quick Start

1. Start with `skills/skill-router`.
2. Copy one template from `templates/` into a target repo.
3. Run the smallest useful skill set, usually `skills/grill-the-repo` plus `skills/static-text-hygiene`.
4. Add `CONTEXT.md` only if the repo has domain-specific language.
5. Add ADRs only for decisions that are hard to reverse, surprising without context, and trade-off driven.
6. Add diagrams when prose hides boundaries or flow.

Recommended first files for a repo:

```text
AGENTS.md
CONTEXT.md
docs/diagrams/architecture.mmd
docs/adr/0001-example-decision.md
```

## Skill Index

Routing:

- `skill-router` - selects the smallest useful skill set and prevents context overload.

Core setup:

- `grill-the-repo` - interrogates a repo and creates or improves agent context.
- `static-text-hygiene` - keeps agent docs durable by stripping volatile details.
- `repo-readiness-audit` - checks whether a repo is ready for coding-agent work.
- `agent-session-playbook` - runs a clean agent session from context gathering to verification.

Docs and diagrams:

- `grill-the-architecture` - stress-tests architectural language and creates diagrams or ADRs.
- `mermaid-architecture-map` - produces concise Mermaid diagrams.
- `excalidraw-system-sketch` - plans Excalidraw sketches for fuzzy system thinking.
- `docs-grounded-recon-report` - creates a report with receipts, inspired by dataset-scout style output.

Tools and prompts:

- `skill-authoring` - creates new modular skills only when a real procedural know-how gap exists.
- `mcp-composio-workflow` - documents and safely uses MCP or Composio tool access.
- `prompt-library-maintenance` - curates reusable prompt libraries and suffixes.
- `claude-code-workflow` - converts practical Claude Code lessons into repo rules.

Security-adjacent:

- `secrets-and-env-review` - reviews `.env`, config, and build output risk.

## Positioning

The simplest public framing:

> Turn any repo into a workspace coding agents can actually work in.

The more technical framing:

> Durable AGENTS.md files, context docs, diagrams, and MCP workflows for agent-assisted engineering.

## Relationship To Exemplary Claude

The public gist `EXEMPLARY-CLAUDE.md` is included under `references/` as the guiding baseline. This kit generalizes that idea into reusable repo templates and skills.

## Principles

- Keep instructions short enough to be read.
- Do not load the whole skill kit for every task.
- Default to one skill and use at most three skills per pass.
- Store stable constraints, not stale implementation facts.
- Prefer code inspection over user memory when the code can answer.
- Make diagrams when relationships matter.
- Use ADRs sparingly.
- Verify changes with repo-specific commands.
- Treat MCP and connector tools as capabilities with boundaries, not magic.
