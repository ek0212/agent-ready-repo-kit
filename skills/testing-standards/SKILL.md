---
name: testing-standards
description: Apply test naming, layout, docstring, and mocking standards while respecting local test conventions.
when_to_use: Invoke when adding tests, fixing regressions, reviewing test quality, naming test files, or mocking interfaces.
---

# Testing Standards

## When To Invoke This Skill

- When adding tests.
- When fixing a bug that should not regress.
- When reviewing test quality.
- When a Python repo lacks clear test style.

## Inputs

- Changed behavior.
- Existing test files.
- Test framework and commands.

## Procedure

### Step 1: Match Existing Test Style

Inspect nearby tests first. Follow local conventions if they conflict with this default.

### Step 2: Name Test Files

For Python projects, use `test_*.py`, usually one test file per source module.

### Step 3: Name Test Functions

Use:

```text
test_<what>_<condition>_<expected_result>
```

Names should encode intent, not implementation trivia.

### Step 4: Add Test Docstrings When Expected

If the repo uses test docstrings, every test function should include a short docstring explaining the behavior being protected.

### Step 5: Mock With Specs

Use `unittest.mock.Mock` with `spec=` when mocking objects with known interfaces.

### Step 6: Verify

Run the relevant test file first, then broader tests if the change affects shared behavior.

## Outputs

- Tests that match repo style.
- Clear test names.
- Verification command and result.
