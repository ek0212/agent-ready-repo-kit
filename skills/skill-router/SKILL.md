---
name: skill-router
description: Select the smallest useful skill set for a repository task and prevent context overload.
when_to_use: Invoke before loading other skills, when several skills might apply, or when deciding whether one, two, or three skills are enough.
---

# Skill Router

## Purpose

Prevent context overload. Do not load the whole kit. Route the task to the smallest useful skill set.

## Routing Rules

- Default to one skill.
- Use two skills when one handles the main task and one handles a clear risk.
- Use three skills only for broad or multi-mode work.
- Never load more than three skills in one pass.
- Summarize what was learned before loading another skill.
- Prefer code and docs inspection over loading more instructions.

## Fast Route Table

| User Need | Primary Skill | Optional Add-On |
|---|---|---|
| Make a code change | `coding-workflow` | `static-text-hygiene` |
| Implement a non-trivial feature | `coding-workflow` | `secrets-and-env-review` |
| Review code quality | `coding-workflow` | `static-text-hygiene` |
| Clean up comments, docstrings, or docs | `static-text-hygiene` | `writing-style` |
| Apply Eve's prose rules | `writing-style` | none |
| Organize imports, module layout, or tests | `coding-workflow` | none |
| Add experimental or debug behavior | `coding-workflow` | `secrets-and-env-review` |
| Validate a user-facing change | `coding-workflow` | none |
| Make a Mermaid diagram | `mermaid-architecture-map` | none |
| Make an Excalidraw sketch | `excalidraw-system-sketch` | none |
| Review secrets or env vars | `secrets-and-env-review` | `static-text-hygiene` |
| Create a new skill | `skill-authoring` | `static-text-hygiene` |

## Default Bundles

### Small Code Change

Use:

- `coding-workflow`

### Feature Work

Use:

- `coding-workflow`
- `secrets-and-env-review` only when auth, env vars, provider keys, or deployment config are touched.
- `static-text-hygiene` only when comments, docstrings, or docs are changed.

### Prose Or Docs

Use:

- `writing-style`
- `static-text-hygiene`

### Repo Diagram

Use one:

- `mermaid-architecture-map`
- `excalidraw-system-sketch`

### Skill Creation

Use:

- `skill-authoring`
- `static-text-hygiene` only if the new skill is documentation-heavy.

## Stop Conditions

Stop routing and start working when:

- one skill clearly matches the task
- the next skill would only add generic advice
- code inspection can answer the question
- the task is small enough to do directly

## Output

Before starting work, state:

```text
Using: <skill names>
Skipping: <obvious but unnecessary skills>
Reason: <one sentence>
```
