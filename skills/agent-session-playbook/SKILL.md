---
name: agent-session-playbook
description: Runs a clean coding-agent session from context gathering through implementation and verification. Use when starting non-trivial code work.
---

# Agent Session Playbook

## Workflow

1. Read repo instructions.
2. Inspect relevant files, callers, tests, and docs.
3. State assumptions and success criteria.
4. Make a small plan for non-trivial work.
5. Edit only the files needed.
6. Run the narrowest useful verification first.
7. Broaden verification if the change touched shared behavior.
8. Summarize changed files, verification, and residual risk.

## Success Criteria

The session is not complete until:

- the requested behavior is implemented or the blocker is clear
- relevant tests or checks have been run, or skipped with reason
- no unrelated user changes were reverted
- risky areas are called out

## Checkpoint Rule

After a meaningful step, record:

```text
Done:
Verified:
Remaining:
Risk:
```

Use checkpoints to prevent long agent sessions from drifting.

## Anti-Patterns

- Editing before reading.
- Refactoring adjacent code for taste.
- Reporting success without verification.
- Hiding skipped checks.
- Blending conflicting codebase patterns.

