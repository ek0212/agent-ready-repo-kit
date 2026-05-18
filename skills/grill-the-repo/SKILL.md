---
name: grill-the-repo
description: Interrogate a repository and produce durable agent context such as AGENTS.md, CONTEXT.md, ADRs, and diagram TODOs. Use before relying on a coding agent in a repo.
---

# Grill The Repo

## Use When

- A repo needs an `AGENTS.md` or `CLAUDE.md`.
- Existing agent instructions are too long, stale, or vague.
- The user wants to make a repo easier for Claude Code, Codex, Cursor, or Copilot.
- The repo has repeated agent mistakes that should be captured.

## Workflow

1. Inspect existing docs first: `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `docs/`, package files, and test commands.
2. Ask one question at a time when the answer cannot be inferred from code.
3. For each answer, decide where it belongs:
   - `AGENTS.md`: stable agent behavior, commands, conventions, mistakes to avoid.
   - `CONTEXT.md`: domain language only.
   - `docs/adr/`: hard-to-reverse decisions with trade-offs.
   - `docs/diagrams/`: architecture, flow, or tool boundaries.
   - nowhere: volatile implementation detail.
4. Update files as decisions become clear. Do not batch every insight until the end.
5. Keep `AGENTS.md` short enough to be read.

## Questions To Ask

Ask only what code and docs cannot answer:

- What does this repo do in one sentence?
- What commands prove the repo still works?
- What conventions has the agent violated before?
- What should the agent never change without asking?
- Which terms are domain-specific and often confused?
- What diagrams would help a new contributor understand boundaries?
- Which facts are likely to rot within a month?

## Static Text Rule

Put durable constraints in agent docs. Do not memorialize file inventories, temporary TODOs, current implementation status, or facts the agent can cheaply rediscover.

## Output

End with:

- files created or changed
- facts intentionally omitted because they are volatile
- unresolved questions
- suggested next skill, if any

