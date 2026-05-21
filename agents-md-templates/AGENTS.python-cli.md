# Python CLI Agent Instructions

Use this template for Python command-line tools, data pipelines, and local automation.

Prefer copying [rules-templates/python-cli.md](../rules-templates/python-cli.md) into `.claude/rules/` when the agent supports path-scoped rules. Use this `AGENTS.md` template when the whole repo is a Python CLI or the tool only supports an always-loaded file.

## Stable Constraints

- Keep command output deterministic where practical.
- Prefer standard library tools unless an existing dependency already covers the job.
- Separate pure logic from I/O so it can be tested.
- Do not call an LLM for deterministic transforms, routing, retries, or status-code handling.

## Commands

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format .
```

Adjust commands to match the repo.

## Code Conventions

- Use specific type hints on public functions.
- Keep CLI argument parsing thin.
- Put reusable logic behind functions or classes that tests can call.
- Preserve lazy imports if the repo uses them to keep CLI startup fast.

## Mistakes To Avoid

- Do not silently skip failed records.
- Do not log secrets or raw private data.
- Do not turn a deterministic operation into an LLM call.
- Do not add global mutable state unless the repo already uses it deliberately.
