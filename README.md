# Agent-Ready Repo Kit

Copyable templates for keeping agent instructions small, durable, and useful in real repositories.

This repo is intentionally not configured as its own agent project. There is no root `AGENTS.md`, `CLAUDE.md`, or `.claude/` directory. Copy the pieces you want into the target repo.

## Core Model

Use each layer for the kind of context it handles best:

| Layer | Loads | Put Here | Avoid |
|---|---|---|---|
| `AGENTS.md` | Every session | Stable constraints, core commands, "always do" rules | Repo summaries, long playbooks, stale architecture notes |
| `CLAUDE.md` | Claude Code sessions | A small Claude-specific wrapper, often importing `AGENTS.md` | Duplicating `AGENTS.md` |
| `.claude/rules/` | Every session or when matching files are opened | Path-specific coding, docs, security, and agent-config rules | Unscoped files that silently become always-on context |
| `.claude/skills/` | On demand | Repeatable workflows, checklists, reference material, scripts | Constraints that should apply to every edit |

This mirrors Anthropic's Claude Code guidance: keep persistent memory concise, move file-specific constraints into rules, and move procedures into skills.

## Quick Start

1. Copy [agents-md-templates/AGENTS.base.md](agents-md-templates/AGENTS.base.md) into the target repo as `AGENTS.md`.
2. If using Claude Code, copy [claude-md-templates/CLAUDE.import-agents.md](claude-md-templates/CLAUDE.import-agents.md) into the target repo as `CLAUDE.md`.
3. Copy relevant files from [rules-templates](rules-templates/) into `.claude/rules/`.
4. Copy only the needed folders from [skills](skills/) into `.claude/skills/` or your agent tool's skill directory.
5. Keep `AGENTS.md` short. If it grows into a playbook, move that section to a skill. If it only applies to some files, move it to a path-scoped rule.

## Templates

- [agents-md-templates](agents-md-templates/) has thin `AGENTS.md` starters for general, prose, web app, Python CLI, Chrome extension, and VS Code extension repos.
- [claude-md-templates](claude-md-templates/) has a Claude Code wrapper that imports `AGENTS.md`.
- [rules-templates](rules-templates/) has copyable `.claude/rules/` files with `paths:` frontmatter.

## Skills

Configuration and authoring:

- [skill-router](skills/skill-router/SKILL.md) decides whether guidance belongs in `AGENTS.md`, rules, skills, hooks, or settings.
- [skill-authoring](skills/skill-authoring/SKILL.md) creates or revises focused `SKILL.md` workflows.
- [prompt-crafting](skills/prompt-crafting/SKILL.md) rewrites rough requests into stronger prompts or agent instructions.

Coding and planning:

- [coding-workflow](skills/coding-workflow/SKILL.md) combines build, debug, review, refactor, optimize, test, and verification habits.
- [design-doc](skills/design-doc/SKILL.md) writes compact software design docs and architecture plans.

Writing and hygiene:

- [writing-style](skills/writing-style/SKILL.md) applies concise prose rules.
- [static-text-hygiene](skills/static-text-hygiene/SKILL.md) keeps comments, docstrings, Markdown, and agent instructions durable.

Diagrams and safety:

- [mermaid-architecture-map](skills/mermaid-architecture-map/SKILL.md)
- [excalidraw-system-sketch](skills/excalidraw-system-sketch/SKILL.md)
- [secrets-and-env-review](skills/secrets-and-env-review/SKILL.md)

## Practical Guardrails

- Do not load every skill.
- Default to no skill for tiny tasks and one skill for normal tasks.
- Use two or three skills only when the task has distinct modes, such as code plus docs, or implementation plus secrets review.
- Prefer inspecting the current repo over trusting a consolidated summary.
- Treat prompt instructions as guidance, not enforcement. Use hooks, settings, or CI checks for rules that must always hold.

## References

- [Claude Code memory and rules](https://code.claude.com/docs/en/memory)
- [Claude Code extension overview](https://code.claude.com/docs/en/features-overview)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
