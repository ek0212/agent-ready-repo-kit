# Agent-Ready Repo Kit

Small, modular skills and thin `AGENTS.md` templates for making coding agents behave better in real repositories.

The repo is intentionally not its own agent-configured project. There is no root `AGENTS.md`. Copy a template from `templates/` into the repo you want to configure.

## What This Contains

- Thin `AGENTS.md` templates.
- Focused `SKILL.md` workflows.
- Mermaid and Excalidraw diagram skills.
- Static text hygiene for comments, docstrings, and Markdown.
- Eve's writing rules as a reusable skill and AGENTS template.

## Quick Start

1. Copy [templates/AGENTS.base.md](templates/AGENTS.base.md) into a target repo as `AGENTS.md`.
2. Use [skills/skill-router](skills/skill-router/SKILL.md) to choose the smallest useful skill set.
3. Use at most three skills per pass.
4. Keep project-specific facts in the target repo, not this kit.

## Kept Skills

Routing and authoring:

- [skill-router](skills/skill-router/SKILL.md)
- [skill-authoring](skills/skill-authoring/SKILL.md)

Writing and static text:

- [writing-style](skills/writing-style/SKILL.md)
- [static-text-hygiene](skills/static-text-hygiene/SKILL.md)

Coding workflow:

- [working-code-first](skills/working-code-first/SKILL.md)
- [development-flow](skills/development-flow/SKILL.md)
- [code-standards](skills/code-standards/SKILL.md)
- [module-structure](skills/module-structure/SKILL.md)
- [testing-standards](skills/testing-standards/SKILL.md)
- [feature-flags-and-debug](skills/feature-flags-and-debug/SKILL.md)
- [end-to-end-validation](skills/end-to-end-validation/SKILL.md)

Diagrams and safety:

- [mermaid-architecture-map](skills/mermaid-architecture-map/SKILL.md)
- [excalidraw-system-sketch](skills/excalidraw-system-sketch/SKILL.md)
- [secrets-and-env-review](skills/secrets-and-env-review/SKILL.md)

## Templates

- [AGENTS.base.md](templates/AGENTS.base.md) - thin wrapper with writing rules and skill routing.
- [AGENTS.writing-style.md](templates/AGENTS.writing-style.md) - minimal AGENTS template for prose-heavy repos.
- [AGENTS.web-app.md](templates/AGENTS.web-app.md)
- [AGENTS.python-cli.md](templates/AGENTS.python-cli.md)
- [AGENTS.chrome-extension.md](templates/AGENTS.chrome-extension.md)
- [AGENTS.vscode-extension.md](templates/AGENTS.vscode-extension.md)

## Guardrail

Do not load every skill. Use `skill-router`, choose one primary skill, and add at most two more only when the task has a distinct second or third mode.
