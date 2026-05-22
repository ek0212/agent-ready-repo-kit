---
paths:
  - "**/*.py"
  - "pyproject.toml"
  - "uv.lock"
---
# Python CLI Constraints

- Keep command output deterministic where practical.
- Prefer standard library tools unless an existing dependency already covers the job.
- Separate pure logic from I/O so it can be tested.
- Use specific type hints on public functions.
- Keep CLI argument parsing thin.
- Do not silently skip failed records.
- Do not call an LLM for deterministic transforms, routing, retries, or status-code handling.
