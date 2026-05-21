---
name: prompt-crafting
description: Rewrite rough requests into structured prompts, agent instructions, task briefs, and evaluation criteria using concise context-task-format guidance.
---

# Prompt Crafting

## Use When

- The user wants a better prompt.
- A task request is vague and needs structure.
- Agent instructions need clearer scope, constraints, outputs, or success criteria.
- A repeated prompt should become an `AGENTS.md` rule, path-scoped rule, or skill.

## Quick Framework

Use Context, Task, Format for most prompts:

| Part | Include |
|---|---|
| Context | Audience, domain, source material, constraints |
| Task | The exact action and target artifact |
| Format | Structure, length, tone, sections, examples |

## Full Framework

For complex or high-stakes agent work, add only the pieces that change the outcome:

- Role or expertise.
- Desired outcome.
- Success criteria.
- Source material.
- Constraints and non-goals.
- Output format.
- Examples or counterexamples.
- Verification method.

## Repair Weak Prompts

| Symptom | Fix |
|---|---|
| Too generic | Add audience, domain, and source material |
| Disorganized | Split into ordered steps and outputs |
| Wrong tone | Add a short target example |
| Too verbose | Add a length or section limit |
| Hallucinated claims | Restrict sources or require citations |
| Agent wandered | Add non-goals and success criteria |

## Coding Agent Prompt Shapes

- Build: ask for current architecture, smallest useful implementation, tests, and verification.
- Debug: provide observed behavior, expected behavior, reproduction path, logs, and verification target.
- Refactor: ask for boundaries, duplication, coupling, testability, and staged migration.
- Optimize: require a bottleneck, measurement plan, expected improvement, and regression check.
- Explain: ask for a module map, data flow, or annotated artifact when prose would hide structure.

## Output

Return the improved prompt and a short note naming the assumptions you made.
