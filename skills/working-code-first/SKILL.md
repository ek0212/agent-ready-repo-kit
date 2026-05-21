---
name: working-code-first
description: Make the smallest correct style-matching code change before optimizing process, polish, or architecture.
when_to_use: Invoke before practical implementation, bug fixes, small improvements, or any moment where the agent may over-plan or over-refactor.
---

# Working Code First

## When To Invoke This Skill

- Before making code changes in an unfamiliar repo.
- When an agent is tempted to refactor, redesign, or over-plan.
- When the user asks for a practical implementation, bug fix, or small improvement.

## Inputs

- User request.
- Relevant source files.
- Existing repo style and nearby patterns.

## Procedure

### Step 1: Identify The Smallest Correct Change

State the smallest change that would satisfy the request. Prefer direct fixes over broad rewrites.

### Step 2: Match Surrounding Style

Inspect nearby code before editing. Match naming, structure, error handling, formatting, and abstractions already present.

### Step 3: Avoid Process Theater

Do not add process artifacts, new abstractions, or documentation unless they help the requested change work correctly or prevent a known mistake.

### Step 4: Verify

Run the narrowest relevant check available. If no check exists, explain the manual verification used or the verification gap.

## Outputs

- A scoped code change.
- Verification result or clear verification gap.
- Short note describing why the change is the smallest reasonable one.

## Why This Matters

Agents often turn small tasks into architecture exercises. This skill keeps the agent anchored on working, correct code that fits the repo.
