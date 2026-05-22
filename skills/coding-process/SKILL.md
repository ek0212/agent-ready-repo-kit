---
name: coding-process
description: Guides the coding process with small correct edits, local conventions, tests, feature flags, and verification. Use when fixing, building, refactoring, or validating code.
when_to_use: Invoke for bug fixes, feature work, refactors, source-file changes, test updates, feature flags, debug code, or final verification before calling a coding task done.
---

# Coding Process

## Rules To Apply

- `rules/coding-constraints.md`
- `rules/static-text-constraints.md`
- `rules/structure-constraints.md`
- `rules/change-safety-constraints.md`
- Path-scoped repo rules that match changed files.

## Inputs

- User request.
- Relevant source files, tests, commands, and nearby conventions.

## Procedure

### Step 1: Pin Down The Behavior

Restate the requested behavior and assumptions. Ask only when missing information would make implementation risky.

### Step 2: Inspect Before Editing

Read nearby code, tests, docs, and config. Prefer local conventions over generic preferences.

### Step 3: Make The Smallest Correct Change

Implement one coherent change at a time. Avoid broad rewrites, adjacent cleanup, and new abstractions unless they directly reduce real complexity.

### Step 4: Update Tests And Static Text

Add or update tests for critical logic and bug fixes. Update comments, docstrings, and docs only when they preserve durable contracts, traps, constraints, or rationale.

### Step 5: Verify

Run the narrowest relevant command first. For user-visible changes, build and manually test the affected flow when possible. For UI changes, check desktop and basic mobile sizes.

## Gotchas

- Do not turn a deterministic operation into an LLM call.
- Do not create a second config, flag, routing, or design system when one already exists.
- Do not ship behavior that relies on debug flags being enabled.

## Outputs

- Scoped code change.
- Tests or reason tests were not added.
- Verification result and residual risk.
