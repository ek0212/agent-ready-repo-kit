# Skill Routing

The kit is modular. Loading every skill wastes context and makes agents blend workflows.

## Guardrail

Use `skill-router` before other skills.

- Default to one skill.
- Use at most three skills per pass.
- Summarize before adding another skill.
- Inspect code and docs before adding more instructions.

## Route Shape

```text
request -> skill-router -> one primary skill -> repo inspection -> action -> verification
```

## Common Routes

### Small Code Change

Use:

- `working-code-first`
- `end-to-end-validation` if behavior changed

### Feature Work

Use:

- `development-flow`
- `working-code-first`
- `testing-standards`

### Docs Or Comments

Use:

- `static-text-hygiene`
- `writing-style`

### Diagram

Use one:

- `mermaid-architecture-map`
- `excalidraw-system-sketch`

### Skill Creation

Use:

- `skill-authoring`

Add `static-text-hygiene` only if the new skill is documentation-heavy.

