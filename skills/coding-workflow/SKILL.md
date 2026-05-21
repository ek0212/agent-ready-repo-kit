---
name: coding-workflow
description: Implement code changes with small correct edits, local conventions, tests, feature-flag discipline, and validation.
when_to_use: Invoke for bug fixes, feature work, refactors, source-file changes, test updates, feature flags, debug code, or final verification before calling a coding task done.
---

# Coding Workflow

## Inputs

- User request.
- Relevant source files, tests, and repo commands.
- Existing conventions near the changed code.

## Procedure

### Step 1: Understand The Requested Behavior

Restate the behavior and assumptions. Ask only when missing information would make a reasonable implementation risky.

### Step 2: Choose The Smallest Correct Change

Prefer direct fixes. Avoid broad rewrites, adjacent cleanup, process artifacts, or new abstractions unless they help the requested change work correctly or prevent a known mistake.

### Step 3: Match Local Conventions

Inspect nearby files before editing. Match naming, structure, error handling, formatting, typing, docstrings, tests, UI patterns, and existing abstractions.

### Step 4: Keep Modules Predictable

When creating or reorganizing modules, follow the repo's file-order convention. If no convention exists, use copyright or license header, imports, constants, classes, functions, then executable entrypoint.

Group imports as standard library, third-party packages, then local or relative imports. Keep imports at the top unless the repo deliberately uses lazy imports.

### Step 5: Keep Code Standards

- Keep functions small and single-purpose.
- Use clear domain-specific names.
- Centralize repeated strings, numbers, labels, and config in existing constants or config locations.
- Prefer simple solutions. Refactor only after behavior is verified.
- Remove unnecessary comments. Keep comments for traps, constraints, non-obvious decisions, or security rationale.
- If the repo uses type hints, add specific argument and return types.
- If the repo uses Google-style docstrings, include Args, Returns, and Raises where applicable.
- For UI changes, check desktop and basic mobile sizes.

### Step 6: Handle Tests

Add or update tests for critical logic, regression fixes, and behavior with clear expected outcomes. Match the local test framework and style.

For Python projects without a stronger convention:

- Name test files `test_*.py`, usually one test file per source module.
- Name test functions `test_<what>_<condition>_<expected_result>`.
- Add short test docstrings if the repo expects them.
- Use `unittest.mock.Mock` with `spec=` when mocking known interfaces.

### Step 7: Gate Debug Or Risky Work

Use existing feature-flag or config patterns for experimental, debug, incomplete, or risky rollout behavior. Do not create a parallel flag system.

Disable debug or experimental behavior in production builds unless the release plan explicitly says otherwise. Document active flags in the repo's central config, README, or flag registry.

### Step 8: Verify

Run the narrowest relevant check first. For user-visible changes, build and manually test the affected flow when possible. For UI changes, check desktop and basic mobile sizes.

If verification cannot be run, state the reason and the remaining risk.

## Outputs

- Scoped code change.
- Tests or reason tests were not added.
- Verification result and residual risk.
