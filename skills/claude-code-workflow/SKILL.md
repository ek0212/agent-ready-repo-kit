---
name: claude-code-workflow
description: Converts practical Claude Code lessons into durable repo instructions and session workflows. Use when configuring Claude Code, Codex, Cursor, or similar coding agents.
---

# Claude Code Workflow

## Use When

- A repo needs a `CLAUDE.md` or `AGENTS.md`.
- Claude Code keeps making the same mistakes.
- The user wants a better agent setup.
- A workflow needs verification and checkpoints.

## Rules To Encode

- Read before writing.
- Match existing conventions.
- Keep changes scoped.
- Ask before changing public APIs, auth, permissions, data deletion, or dependencies.
- Define success criteria before non-trivial work.
- Verify with project commands.
- Fail loud when anything was skipped.
- Do not average conflicting patterns.
- Do not add single-use abstractions.

## Rules To Avoid

- "Be careful."
- "Act like a senior engineer."
- Long motivational language.
- Huge examples that bury the real constraints.
- File maps that will rot.

## Session Pattern

```text
Understand:
Plan:
Implement:
Verify:
Report:
```

For complex work, checkpoint:

```text
Done:
Verified:
Remaining:
Risk:
```

## Output

Create one of:

- `CLAUDE.md`
- `AGENTS.md`
- a short "agent workflow" section in existing docs

Keep it short. If it passes 200 lines, split context into `CONTEXT.md`, ADRs, or diagrams.

