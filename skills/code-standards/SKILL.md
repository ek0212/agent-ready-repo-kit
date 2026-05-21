---
name: code-standards
description: Apply code quality standards while editing or reviewing code. Use for function size, names, constants, simple refactors, type hints, docstrings, and UI coherence.
when_to_use: Invoke when adding code, reviewing maintainability, introducing names or constants, changing typed APIs, or touching UI that must remain coherent.
---

# Code Standards

## When To Invoke This Skill

- When adding or modifying source code.
- When reviewing code for maintainability.
- When a change introduces names, constants, functions, classes, or UI behavior.

## Inputs

- Changed files.
- Nearby code conventions.
- Existing type and docstring standards.

## Procedure

### Step 1: Keep Units Small

Keep functions small and single-purpose. Split only when it clarifies real responsibilities or removes meaningful duplication.

### Step 2: Use Domain-Specific Names

Prefer names from the domain over vague names. Rename instead of adding comments when a better name makes intent obvious.

### Step 3: Centralize Reused Values

Extract repeated strings, numbers, labels, and config into existing constants or config locations. Do not centralize one-off values.

### Step 4: Prefer Simple Solutions

Use the simplest approach that satisfies the behavior. Refactor only after the behavior is verified.

### Step 5: Keep Comments Necessary

Remove unnecessary comments. Keep comments that explain traps, constraints, non-obvious decisions, or security rationale.

### Step 6: Match Typing And Docstring Standards

If the repo uses type hints, add specific argument and return types. If the repo uses Google-style docstrings, include Args, Returns, and Raises where applicable.

### Step 7: Check UI Coherence

For UI changes, check desktop and basic mobile sizes. Text should not overflow or collide with surrounding elements.

## Outputs

- Code that matches repo standards.
- Notes about any standards intentionally not applied.
- UI verification notes when UI changed.
