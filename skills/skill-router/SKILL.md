---
name: skill-router
description: Selects the smallest useful set of skills for a repository task. Use before loading other skills from this kit.
---

# Skill Router

## Purpose

Prevent context overload. Do not load the whole kit. Route the task to the smallest useful skill set.

## Routing Rules

- Default to one skill.
- Use two skills when one handles the main task and one handles a clear risk.
- Use three skills only for broad repo onboarding or multi-part audits.
- Never load more than three skills in one pass.
- Summarize what was learned before loading another skill.
- Prefer code and docs inspection over loading more instructions.

## Fast Route Table

| User Need | Primary Skill | Optional Add-On |
|---|---|---|
| Make this repo agent-ready | `grill-the-repo` | `static-text-hygiene` |
| Audit whether agents can work here | `repo-readiness-audit` | `secrets-and-env-review` |
| Clean up AGENTS.md or CLAUDE.md | `static-text-hygiene` | `claude-code-workflow` |
| Create better Claude/Codex rules | `claude-code-workflow` | `static-text-hygiene` |
| Understand architecture | `grill-the-architecture` | `mermaid-architecture-map` |
| Make a diagram | `mermaid-architecture-map` | `excalidraw-system-sketch` |
| Sketch fuzzy product/system flow | `excalidraw-system-sketch` | none |
| Write a repo report with receipts | `docs-grounded-recon-report` | `repo-readiness-audit` |
| Configure MCP or Composio | `mcp-composio-workflow` | `ai-app-prompt-injection-review` |
| Review secrets or env vars | `secrets-and-env-review` | none |
| Review an LLM app | `ai-app-prompt-injection-review` | `mcp-composio-workflow` |
| Maintain prompt library | `prompt-library-maintenance` | `claude-code-workflow` |
| Run a coding session | `agent-session-playbook` | task-specific skill |

## Default Bundles

### New Repo Onboarding

Use:

- `grill-the-repo`
- `static-text-hygiene`
- `repo-readiness-audit`

Stop after these. Create follow-up tasks for diagrams, MCP, or security review.

### AI App With Tools

Use:

- `ai-app-prompt-injection-review`
- `mcp-composio-workflow`
- `secrets-and-env-review`

### Documentation Cleanup

Use:

- `static-text-hygiene`
- `docs-grounded-recon-report` only if claims need source receipts

### Architecture Pass

Use:

- `grill-the-architecture`
- `mermaid-architecture-map`

Add `excalidraw-system-sketch` only if the user wants a rough spatial sketch.

## Stop Conditions

Stop routing and start working when:

- one skill clearly matches the task
- the next skill would only add generic advice
- code inspection can answer the question
- the task is small enough to do directly

## Output

Before starting work, state:

```text
Using: <skill names>
Skipping: <obvious but unnecessary skills>
Reason: <one sentence>
```

