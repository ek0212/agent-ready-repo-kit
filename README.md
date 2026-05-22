# Agent-Ready Repo Kit

Small, modular rules and skills for making coding agents behave better in real repositories.

The root `AGENTS.md` is the reusable template. Copy it, along with the `rules/` and `skills/` you want, into the target repo.

## What This Contains

- One thin `AGENTS.md` template.
- Composable always-on and path-scoped rules.
- Focused `SKILL.md` procedures.
- Mermaid and Excalidraw diagram skills.
- Static text hygiene for comments, docstrings, and Markdown.
- MECE structure and durable static text rules.
- Eve's writing rules as reusable constraints and a writing skill.

## Quick Start

1. Copy [AGENTS.md](AGENTS.md) into the target repo as `AGENTS.md`.
2. Copy [rules/](rules/) into the target repo and keep only the optional path-scoped rules that apply.
3. Use [skills/skill-router](skills/skill-router/SKILL.md) to choose the smallest useful skill set.
4. Use at most three skills per pass.
5. Keep project-specific facts in the target repo, not this kit.

## Layers

- `AGENTS.md`: the entrypoint and rule manifest at the repo root.
- `rules/`: standards and constraints. Some files are path-scoped.
- `skills/`: on-demand procedures that point back to rules.

## Connection Map

```text
AGENTS.md
  |-- imports always-on constraints from rules/
  |     |-- skill-routing-constraints.md
  |     |-- coding-constraints.md
  |     |-- writing-constraints.md
  |     |-- static-text-constraints.md
  |     |-- structure-constraints.md
  |     |-- change-safety-constraints.md
  |     `-- security-constraints.md
  |
  |-- keeps optional path-scoped constraints nearby
  |     |-- web-app-constraints.md
  |     |-- python-cli-constraints.md
  |     |-- chrome-extension-constraints.md
  |     `-- vscode-extension-constraints.md
  |
  `-- routes task work to skills/
        |-- coding-process
        |-- writing-process
        |-- static-text-hygiene
        |-- secrets-and-env-review
        |-- mermaid-architecture-map
        |-- excalidraw-system-sketch
        |-- frontend-design
        |-- skill-authoring
        `-- skill-router
```

## Skills

Routing and authoring:

- [skill-router](skills/skill-router/SKILL.md)
- [skill-authoring](skills/skill-authoring/SKILL.md)

Writing and static text:

- [writing-process](skills/writing-process/SKILL.md)
- [static-text-hygiene](skills/static-text-hygiene/SKILL.md)

Coding process:

- [coding-process](skills/coding-process/SKILL.md)
- [frontend-design](skills/frontend-design/SKILL.md)

Diagrams and safety:

- [mermaid-architecture-map](skills/mermaid-architecture-map/SKILL.md)
- [excalidraw-system-sketch](skills/excalidraw-system-sketch/SKILL.md)
- [secrets-and-env-review](skills/secrets-and-env-review/SKILL.md)

## AGENTS.md Template

- [AGENTS.md](AGENTS.md) - the only reusable AGENTS template. It imports always-on rules and lists the available skills.

## Rules

Always-on:

- [skill-routing-constraints](rules/skill-routing-constraints.md)
- [coding-constraints](rules/coding-constraints.md)
- [writing-constraints](rules/writing-constraints.md)
- [static-text-constraints](rules/static-text-constraints.md)
- [structure-constraints](rules/structure-constraints.md)
- [change-safety-constraints](rules/change-safety-constraints.md)
- [security-constraints](rules/security-constraints.md)

Path-scoped:

- [web-app-constraints](rules/web-app-constraints.md)
- [python-cli-constraints](rules/python-cli-constraints.md)
- [chrome-extension-constraints](rules/chrome-extension-constraints.md)
- [vscode-extension-constraints](rules/vscode-extension-constraints.md)

## Guardrail

Do not load every skill. Use `skill-router`, choose one primary skill, and add at most two more only when the task has a distinct second or third mode.

## Extending The Kit

When you copy this kit into a target repo and want to add your own rules or skills alongside the kit's:

1. Drop your rule into `rules/your-rule.md` and add `@rules/your-rule.md` under the `## Local Rules` section of `AGENTS.md`. Do not edit the `## Kit Rules` block, so future syncs from this kit stay conflict-free.
2. Drop your skill into `skills/your-skill/SKILL.md` and add a `- Use your-skill for ...` bullet under the `## Local Skills` section of `AGENTS.md`.
3. Add a routing row for your skill under `## Local Routes` in `skills/skill-router/SKILL.md`.
4. Re-syncing this kit later overwrites only the `Kit` blocks, so your `Local` additions persist.

Skills auto-list at runtime, so a new `skills/your-skill/SKILL.md` is discoverable even without the bullet, but the bullet and routing row tell the agent when to reach for it.

## File Size

Keep every `AGENTS.md`, rule file, and `SKILL.md` under 200 lines.
