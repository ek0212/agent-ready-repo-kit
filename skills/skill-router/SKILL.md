---
name: skill-router
description: Selects the smallest useful set of skills for a repository task. Use before loading other skills from this kit.
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
| Make a small code change | `working-code-first` | `end-to-end-validation` |
| Implement a non-trivial feature | `development-flow` | `working-code-first` |
| Review code quality | `code-standards` | `module-structure` |
| Clean up comments, docstrings, or docs | `static-text-hygiene` | `writing-style` |
| Apply Eve's prose rules | `writing-style` | none |
| Organize imports or module layout | `module-structure` | `code-standards` |
| Add or review tests | `testing-standards` | `end-to-end-validation` |
| Add experimental or debug behavior | `feature-flags-and-debug` | `end-to-end-validation` |
| Validate a user-facing change | `end-to-end-validation` | none |
| Make a Mermaid diagram | `mermaid-architecture-map` | none |
| Make an Excalidraw sketch | `excalidraw-system-sketch` | none |
| Review secrets or env vars | `secrets-and-env-review` | `static-text-hygiene` |
| Create a new skill | `skill-authoring` | `static-text-hygiene` |

## Default Bundles

### Small Code Change

Use:

- `working-code-first`
- `end-to-end-validation`

### Feature Work

Use:

- `development-flow`
- `working-code-first`
- `testing-standards`

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

