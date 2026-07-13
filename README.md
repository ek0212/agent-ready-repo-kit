# Agent-Ready Repo Kit

Small, modular rules and skills for making coding agents behave better in real repositories.

Copy `AGENTS.md` and the `skills/` you need into the target repo.

## What This Contains

- One self-contained [`AGENTS.md`](AGENTS.md) with inline rules, procedures, path-scoped rules, and a skill table.
- Four focused skills in [`skills/`](skills/).

## Quick Start

1. Copy [`AGENTS.md`](AGENTS.md) into the target repo root.
2. Copy [`skills/`](skills/) into the target repo. Remove any skills you don't need.
3. Keep project-specific facts in the target repo, not this kit.

## Structure

```text
AGENTS.md                          # Rules, procedures, path-scoped rules, skill table
skills/
  skill-authoring/SKILL.md         # Creating or splitting skills
  frontend-design/SKILL.md         # Distinctive web UI with creative aesthetics
  mermaid-architecture-map/SKILL.md # GitHub-renderable Mermaid diagrams
  excalidraw-system-sketch/SKILL.md # Freeform Excalidraw system sketches
```

## AGENTS.md

[`AGENTS.md`](AGENTS.md) is the single entrypoint. It contains:

- **Rules**: coding, change safety, security, writing, static text, structure, model selection.
- **Procedures**: coding process, writing process, static text hygiene, secrets/env review.
- **Path-scoped rules**: Python, Chrome Extension, VS Code Extension, Web App.
- **Skill table**: maps task types to skills.

## Skills

| Skill | Use when |
|---|---|
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | Creating a new skill, splitting a broad skill, or deciding whether guidance belongs in AGENTS.md vs a skill. |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Building distinctive web components, pages, or applications where design quality matters. |
| [`mermaid-architecture-map`](skills/mermaid-architecture-map/SKILL.md) | Repo needs a GitHub-renderable diagram or a system boundary should be explicit. |
| [`excalidraw-system-sketch`](skills/excalidraw-system-sketch/SKILL.md) | Mermaid is too rigid, or the system needs grouping, swimlanes, or rough sketching. |

### Skill Loading Rules

- Default to zero skills. The procedures in `AGENTS.md` cover most tasks.
- Load at most one skill per pass unless the task spans multiple domains.
- Prefer reading code and docs over loading more instructions.

## Extending The Kit

1. Add your skill as `skills/your-skill/SKILL.md` and add a routing row to the skill table in `AGENTS.md`.
2. Add path-scoped rules directly to the `Path-Scoped Rules` section in `AGENTS.md`.
3. Keep every file under 200 lines.

## File Size

Keep `AGENTS.md` and every `SKILL.md` under 200 lines.
