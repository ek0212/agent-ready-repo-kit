# Agent-Ready Repo Kit

Small rule and skill kit for coding agents in real repos.

Copy `AGENTS.md` and the `skills/` you need into the target repo.

## What This Contains

- One self-contained [`AGENTS.md`](AGENTS.md): rules, procedures, path-scoped rules, skill routing.
- Focused skills in [`skills/`](skills/).

## Quick Start

1. Copy [`AGENTS.md`](AGENTS.md) into the target repo root.
2. Copy [`skills/`](skills/) into the target repo. Remove skills you do not need.
3. Keep project facts in the target repo, not this kit.

## Structure

```text
AGENTS.md                           # Rules, procedures, path rules, skill table
skills/
  skill-authoring/SKILL.md          # Create or split skills
  frontend-design/SKILL.md          # Distinctive web UI
  mermaid-architecture-map/SKILL.md # GitHub-renderable diagrams
  excalidraw-system-sketch/SKILL.md # Freeform system sketches
  creative-writing/SKILL.md         # Narrative nonfiction
  dataset-triage/SKILL.md           # Tabular data sanity checks
  stanford-research/SKILL.md        # Literature synthesis
```

## AGENTS.md

[`AGENTS.md`](AGENTS.md) is the entrypoint. It contains:

- **Rules:** coding, safety, security, writing, static text, structure, model choice, agent communication.
- **Procedures:** coding, writing, static text hygiene, secrets/env review.
- **Path rules:** Python, Chrome Extension, VS Code Extension, Web App.
- **Skill table:** task type to skill.

## Skills

| Skill | Use when |
|---|---|
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | Create, split, or route skills. |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Build web UI where design quality matters. |
| [`mermaid-architecture-map`](skills/mermaid-architecture-map/SKILL.md) | Need GitHub-renderable diagrams or explicit boundaries. |
| [`excalidraw-system-sketch`](skills/excalidraw-system-sketch/SKILL.md) | Need grouping, swimlanes, or rough visual thinking. |
| [`creative-writing`](skills/creative-writing/SKILL.md) | Draft or edit nonfiction with narrative craft. |
| [`dataset-triage`](skills/dataset-triage/SKILL.md) | Check tabular data before analysis or modeling. |
| [`stanford-research`](skills/stanford-research/SKILL.md) | Synthesize research papers. |

### Skill Loading Rules

- Default to zero skills.
- Load at most one skill per pass unless the task spans domains.
- Prefer reading code and docs over loading more instructions.

## Extend

1. Add `skills/your-skill/SKILL.md`.
2. Add a routing row in `AGENTS.md`.
3. Add path-scoped rules directly to `AGENTS.md`.
4. Keep `AGENTS.md` and every `SKILL.md` under 200 lines.
