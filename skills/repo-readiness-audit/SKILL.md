---
name: repo-readiness-audit
description: Audits whether a repo is ready for coding-agent work. Use before running a long agent session or onboarding agents to an unfamiliar project.
---

# Repo Readiness Audit

## Audit Areas

### Context

- Is there an `AGENTS.md` or equivalent?
- Is it short enough to be read?
- Does it list stable commands and constraints?
- Does it avoid stale implementation facts?

### Verification

- Can the agent install dependencies?
- Can it run tests?
- Can it lint, format, build, or run the app?
- Are the commands documented?

### Boundaries

- Are auth, secrets, payments, data deletion, and public APIs called out?
- Are dangerous commands or migrations gated?
- Are external tools or MCP servers documented?

### Diagrams

- Is the system shape obvious from docs?
- If not, should there be a Mermaid or Excalidraw diagram?

### Common Mistakes

- Are repeated agent failures captured?
- Does the repo tell the agent which patterns to reuse?

## Scoring

Use a lightweight score:

```text
Ready: agent can safely do scoped work.
Partial: agent can work, but needs extra human guidance.
Not ready: agent is likely to guess, drift, or damage unrelated code.
```

## Output

Return:

- readiness score
- top 3 risks
- top 3 fixes
- suggested files to create or edit

