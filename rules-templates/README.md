# Rules Templates

Copy these files into a target repo's `.claude/rules/` directory.

Rules without `paths:` frontmatter load every session. Rules with `paths:` load only when Claude works with matching files. Prefer path-scoped rules unless the instruction truly applies to every task.

Suggested starting set:

- `agent-config.md` for `AGENTS.md`, `CLAUDE.md`, rules, and skills.
- `coding.md` for source and test files.
- `docs-and-writing.md` for Markdown and documentation.
- Add `web-app.md`, `python-cli.md`, or `secrets-and-env.md` only when the repo needs them.
