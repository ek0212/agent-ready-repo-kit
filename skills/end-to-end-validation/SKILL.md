---
name: end-to-end-validation
description: Verify changed functionality with build, manual flow checks, and desktop/mobile UI checks when applicable.
when_to_use: Invoke before calling user-visible changes complete, especially after UI, auth, routing, data, integration, or behavior changes.
---

# End-To-End Validation

## When To Invoke This Skill

- Before calling a feature or fix complete.
- After UI, auth, data, routing, or integration changes.
- When a change affects user-visible behavior.
- When automated tests are insufficient to prove the affected flow works.

## Inputs

- Changed files.
- Build, test, and run commands.
- Description of affected user flows.

## Procedure

### Step 1: Build

Run the project build if available. It must succeed with zero errors before completion.

### Step 2: Test Changed Functionality

Manually test the affected flow or run the closest automated end-to-end test. Focus on the behavior the user asked to change.

### Step 3: Check UI Sizes

For UI changes, check desktop and basic mobile sizes. Confirm layout, text fit, and primary interaction still work.

### Step 4: Record Gaps

If a verification step cannot be run, state why and what risk remains.

## Outputs

- Build result.
- Manual or end-to-end test notes.
- UI size checks when applicable.
- Residual verification gaps.
