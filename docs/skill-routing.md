# Skill Routing

The kit is intentionally modular. Loading every skill would waste context and make the agent slower, less focused, and more likely to blend workflows.

## Guardrail

Use the `skill-router` skill before other skills.

Hard rules:

- default to one skill
- use at most three skills per pass
- summarize before loading another skill
- inspect code and docs before adding more instructions
- split broad audits into follow-up passes

## Why Not Load Everything?

Skills are like tools, not laws of physics. A task about cleaning `AGENTS.md` does not need prompt-library maintenance, Mermaid diagrams, and MCP safety rules in memory.

The router keeps the agent in a narrow lane:

```text
request -> route -> inspect repo -> apply one workflow -> verify -> report
```

## Routing Examples

### "Make this repo agent-ready"

Use:

- `grill-the-repo`
- `static-text-hygiene`
- `repo-readiness-audit`

Defer:

- diagrams
- MCP
- prompt-library work

### "Review this AI app before I connect Gmail through Composio"

Use:

- `mcp-composio-workflow`
- `secrets-and-env-review`

Defer:

- Excalidraw
- prompt library maintenance
- broad architecture grilling

### "Create a new skill for this repeated workflow"

Use:

- `skill-authoring`

Add only if needed:

- `static-text-hygiene` when the skill is about docs, comments, or durable written context

### "Make a diagram of this repo"

Use:

- `mermaid-architecture-map`

Add only if needed:

- `grill-the-architecture` when the architecture is unclear
- `excalidraw-system-sketch` when the user wants a rough visual sketch

## Context Budget Pattern

Start with the smallest useful context:

1. Root `AGENTS.md`
2. Router skill
3. One task skill
4. Relevant code/docs

Only then add another skill if the work has a distinct second mode.
