# Agent-Ready Repo Kit

Small, modular skills and thin `AGENTS.md` templates for making coding agents behave better in real repositories.

The repo is intentionally not its own agent-configured project. There is no root `AGENTS.md`. Copy a template from `agents-md-templates/` into the repo you want to configure.

## What This Contains

- Thin `AGENTS.md` templates.
- Focused `SKILL.md` workflows.
- Mermaid and Excalidraw diagram skills.
- Static text hygiene for comments, docstrings, and Markdown.
- Always-on AGENTS rules for durable static text and MECE structure.
- Eve's writing rules as a reusable skill and AGENTS template.

## Quick Start

1. Copy [agents-md-templates/AGENTS.base.md](agents-md-templates/AGENTS.base.md) into a target repo as `AGENTS.md`.
2. Append one domain template only when the repo needs it.
3. Use [skills/skill-router](skills/skill-router/SKILL.md) to choose the smallest useful skill set.
4. Use at most three skills per pass.
5. Keep project-specific facts in the target repo, not this kit.

## Kept Skills

Routing and authoring:

- [skill-router](skills/skill-router/SKILL.md)
- [skill-authoring](skills/skill-authoring/SKILL.md)

Writing and static text:

- [writing-style](skills/writing-style/SKILL.md)
- [static-text-hygiene](skills/static-text-hygiene/SKILL.md)

Coding workflow:

- [coding-workflow](skills/coding-workflow/SKILL.md)

Diagrams and safety:

- [mermaid-architecture-map](skills/mermaid-architecture-map/SKILL.md)
- [excalidraw-system-sketch](skills/excalidraw-system-sketch/SKILL.md)
- [secrets-and-env-review](skills/secrets-and-env-review/SKILL.md)

## AGENTS.md Templates

- [AGENTS.base.md](agents-md-templates/AGENTS.base.md) - default always-on wrapper with skill routing, durable static text, MECE structure, and writing rules.
- [AGENTS.writing-style.md](agents-md-templates/AGENTS.writing-style.md) - minimal AGENTS template for prose-heavy repos.
- [AGENTS.web-app.md](agents-md-templates/AGENTS.web-app.md) - add-on for frontend app repos.
- [AGENTS.python-cli.md](agents-md-templates/AGENTS.python-cli.md) - add-on for Python CLI repos.
- [AGENTS.chrome-extension.md](agents-md-templates/AGENTS.chrome-extension.md) - add-on for Chrome extension repos.
- [AGENTS.vscode-extension.md](agents-md-templates/AGENTS.vscode-extension.md) - add-on for VS Code extension repos.

## Guardrail

Do not load every skill. Use `skill-router`, choose one primary skill, and add at most two more only when the task has a distinct second or third mode.
