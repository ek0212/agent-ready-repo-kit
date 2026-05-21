# Skills

Each folder contains one standalone `SKILL.md`.

Copy only the skills a target repo needs. Skill descriptions are the always-visible part, while the body should load only when the skill is invoked or selected by the agent.

## Context Guardrail

- Default to no skill for tiny tasks.
- Use one skill for normal tasks.
- Use at most three skills per pass.
- Summarize before adding another skill.
- Prefer inspecting the repo over loading more instructions.

## Configuration Skills

- `skill-router`
- `skill-authoring`
- `prompt-crafting`

## Coding And Planning

- `coding-workflow`
- `design-doc`

## Writing And Hygiene

- `static-text-hygiene`
- `writing-style`

## Diagram And Safety Skills

- `mermaid-architecture-map`
- `excalidraw-system-sketch`
- `secrets-and-env-review`
