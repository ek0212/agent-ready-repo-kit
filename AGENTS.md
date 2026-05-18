# Agent-Ready Repo Kit Instructions

This repo contains templates and skills for making other repositories easier for coding agents to work in.

## Core Rules

- Keep examples practical and copy-pasteable.
- Favor durable constraints over volatile implementation summaries.
- Do not create giant instruction files. Short files that agents read beat comprehensive files they skim.
- Do not load every skill for every task. Use `skills/skill-router/SKILL.md` to choose the smallest useful skill set.
- Default to one skill and use at most three skills in a single pass.
- Use plain Markdown for skills and templates.
- Keep file names lowercase with hyphens except conventional files such as `AGENTS.md`, `CONTEXT.md`, and `README.md`.
- When adding a skill, create a folder under `skills/<skill-name>/SKILL.md`.
- When adding a template, put it under `templates/`.

## Skill Format

Each skill uses:

```markdown
---
name: skill-name
description: One sentence describing when to use it.
---

# Skill Name

## Use When

...

## Workflow

...
```

## Static Text Hygiene

Agent instructions should contain stable guidance:

- conventions
- constraints
- verification commands
- mistake patterns
- workflow rules
- boundaries and ownership

Avoid volatile content:

- exhaustive file maps
- current implementation status
- recent TODOs that will expire
- package versions unless they are constraints
- claims that can be discovered by reading code

## Verification

This repo is documentation-only for now. Verification means:

- all skill folders contain `SKILL.md`
- Markdown headings are coherent
- templates are internally consistent
- no template encourages hardcoding secrets or skipping verification
