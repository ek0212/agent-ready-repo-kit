# Quickstart

Use this process to add the kit to another repo.

## 1. Pick An AGENTS Template

Choose one:

- `templates/AGENTS.base.md`
- `templates/AGENTS.writing-style.md`
- `templates/AGENTS.web-app.md`
- `templates/AGENTS.python-cli.md`
- `templates/AGENTS.chrome-extension.md`
- `templates/AGENTS.vscode-extension.md`

Copy it into the target repo as `AGENTS.md`.

## 2. Route The Task

Use `skills/skill-router` before loading other skills.

Default to one skill. Use at most three skills per pass.

## 3. Keep AGENTS Thin

The target repo's `AGENTS.md` should contain:

- commands
- stable constraints
- writing rules
- ask-before-changing boundaries
- pointers to selected skills

Do not add exhaustive file maps, temporary TODOs, or current implementation status.

## 4. Use Section Skills

Use the skill that matches the moment:

- code change: `working-code-first`
- non-trivial feature: `development-flow`
- code quality: `code-standards`
- module layout: `module-structure`
- tests: `testing-standards`
- flags/debug: `feature-flags-and-debug`
- writing: `writing-style`
- validation: `end-to-end-validation`
- static docs/comments: `static-text-hygiene`
- diagrams: `mermaid-architecture-map` or `excalidraw-system-sketch`

