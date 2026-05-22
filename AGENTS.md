# Project Agent Instructions

Keep this file under 200 lines. Put standards in `rules/` and procedures in `skills/`.

## Project Commands
Fill this out once you've settled on the project standards:
```bash
# Install

# Run

# Test

# Lint / format

# Build
```

## Always-On Rules

@rules/skill-routing-constraints.md
@rules/coding-constraints.md
@rules/writing-constraints.md
@rules/static-text-constraints.md
@rules/structure-constraints.md
@rules/change-safety-constraints.md
@rules/security-constraints.md

## Optional Path-Scoped Rules

Keep only the optional rule files that match this repo:

- `rules/web-app-constraints.md`
- `rules/python-cli-constraints.md`
- `rules/chrome-extension-constraints.md`
- `rules/vscode-extension-constraints.md`

## Skills

- Use `skill-router` before loading other skills.
- Use `coding-process` for implementation, refactors, tests, and verification.
- Use `writing-process` for prose, docs, summaries, and public explanations.
- Use `static-text-hygiene` for deeper stale comment, docstring, and Markdown cleanup.
- Use `secrets-and-env-review` for keys, tokens, env vars, auth config, and bundled output checks.
- Use `mermaid-architecture-map` or `excalidraw-system-sketch` for diagrams.
- Use `skill-authoring` when creating or revising a skill.
