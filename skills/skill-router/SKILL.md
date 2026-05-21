---
name: skill-router
description: Route agent guidance into AGENTS.md, CLAUDE.md, path-scoped rules, skills, hooks, settings, or repo docs while minimizing context load.
---

# Skill Router

## Purpose

Decide where guidance belongs. Keep always-loaded context small and avoid turning `AGENTS.md` into a stale repo wiki.

## Placement Rules

| Need | Put It In |
|---|---|
| Every agent should always know it | `AGENTS.md` |
| Claude Code needs a tiny wrapper or import | `CLAUDE.md` |
| Applies only to certain paths or file types | `.claude/rules/<topic>.md` with `paths:` |
| Repeatable procedure, checklist, examples, or scripts | `.claude/skills/<name>/SKILL.md` |
| Must be enforced regardless of model judgment | Hook, settings, CI, tests, or permissions |
| Human-readable architecture or product context | Repo docs |

## Daily Task Routing

Default to no skill for tiny tasks and one skill for normal tasks. Add another skill only when the task has a distinct second mode.

| User Need | Primary Skill | Optional Add-On |
|---|---|---|
| Make a code change | `coding-workflow` | `static-text-hygiene` |
| Implement a non-trivial feature | `coding-workflow` | `secrets-and-env-review` |
| Review code quality | `coding-workflow` | `static-text-hygiene` |
| Clean up comments, docstrings, or docs | `static-text-hygiene` | `writing-style` |
| Apply Eve's prose rules | `writing-style` | none |
| Write a design doc or architecture plan | `design-doc` | `mermaid-architecture-map` |
| Improve a prompt or agent instruction | `prompt-crafting` | `skill-authoring` |
| Make a Mermaid diagram | `mermaid-architecture-map` | none |
| Make an Excalidraw sketch | `excalidraw-system-sketch` | none |
| Review secrets or env vars | `secrets-and-env-review` | `static-text-hygiene` |
| Create a new skill | `skill-authoring` | `static-text-hygiene` |

## Budget Rules

- Do not load the whole kit.
- Use at most three skills in one pass.
- Prefer current repo inspection over more instructions.
- Summarize what was learned before adding another skill.
- Remove or path-scope rules that do not justify always-on context.
- Split broad skills when their subprocedures trigger in different tasks.

## Stop Conditions

Stop routing and start working when:

- one skill clearly matches the task
- the next skill would only add generic advice
- code inspection can answer the question
- the task is small enough to do directly

## Output

When routing configuration, return:

```text
AGENTS.md:
Rules:
Skills:
Hooks/settings/CI:
Repo docs:
Remove:
```
