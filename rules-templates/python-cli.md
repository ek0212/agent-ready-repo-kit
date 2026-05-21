---
paths:
  - "**/*.py"
  - "pyproject.toml"
  - "uv.lock"
  - "requirements*.txt"
---

# Python CLI Rules

- Prefer standard library tools unless the repo already has a suitable dependency.
- Keep CLI argument parsing thin and move reusable logic into testable functions.
- Use specific type hints on public functions when the repo uses typing.
- Keep command output deterministic where practical.
- Do not silently skip failed records.
- Do not log secrets or raw private data.
- Do not use an LLM for deterministic transforms, routing, retries, or status-code handling.
