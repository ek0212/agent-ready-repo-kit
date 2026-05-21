---
name: development-flow
description: Guide non-trivial feature work through requirements, a short plan, incremental implementation, tests, and verification.
when_to_use: Invoke when a task touches multiple files, has ambiguous requirements, adds a feature, or needs an implementation plan before coding.
---

# Development Flow

## When To Invoke This Skill

- For non-trivial feature work.
- When a task touches multiple files or has ambiguous requirements.
- When implementation should proceed incrementally.

## Inputs

- User request.
- Relevant repo files and docs.
- Existing tests or verification commands.

## Procedure

### Step 1: Understand Requirements

Restate the requested behavior and note assumptions. Ask only when a missing answer would make a reasonable implementation risky.

### Step 2: Outline A Short Plan

For non-trivial tasks, write a brief plan with the files or areas likely to change. Keep the plan small enough to revise.

### Step 3: Implement Incrementally

Make one coherent change at a time. Avoid bundling unrelated cleanup into the same pass.

### Step 4: Add Tests For Critical Logic

Add or update tests when introducing new critical logic or fixing a bug with clear expected behavior. Match the repo's existing test style.

### Step 5: Verify

Run the most relevant test, lint, build, or manual check.

## Outputs

- Short plan, if needed.
- Incremental implementation.
- Tests or explanation for why tests were not added.
- Verification result.

## Why This Matters

Incremental work gives agents fewer places to drift and gives humans clearer review points.
