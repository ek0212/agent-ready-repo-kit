---
paths:
  - "AGENTS.md"
  - "CLAUDE.md"
  - ".claude/**/*.md"
  - ".claude/**/SKILL.md"
  - "skills/**/SKILL.md"
---

# Agent Config Rules

- Keep always-loaded files short and durable.
- Do not store repo summaries in `AGENTS.md` or `CLAUDE.md`; make agents inspect the current repo.
- Put path-specific constraints in `.claude/rules/`.
- Put repeatable procedures, checklists, examples, or reference material in skills.
- In skills, keep `SKILL.md` focused and move bulky reference material into linked supporting files.
- Use hooks, settings, CI, or tests for guardrails that must be enforced.
