# Skills

Each folder contains a standalone `SKILL.md` that can be copied into a Codex, Claude, or local skills setup.

## Routing Guardrail

Use `skill-router` before loading other skills.

- Default to one skill.
- Use at most three skills per pass.
- Summarize before adding another skill.
- Prefer inspecting the repo over loading more instructions.

## Suggested Bundles

For a new repo:

- `skill-router`
- `grill-the-repo`
- `static-text-hygiene`
- `repo-readiness-audit`
- `agent-session-playbook`

For architecture work:

- `skill-router`
- `grill-the-architecture`
- `mermaid-architecture-map`
- `excalidraw-system-sketch`
- `docs-grounded-recon-report`

For AI apps and tools:

- `skill-router`
- `mcp-composio-workflow`
- `secrets-and-env-review`

For prompt and Claude Code workflows:

- `skill-router`
- `skill-authoring`
- `prompt-library-maintenance`
- `claude-code-workflow`

For creating new skills:

- `skill-router`
- `skill-authoring`

## Naming Rule

Skills should be named for the job they perform, not the tool they happen to use.

Good:

- `grill-the-repo`
- `secrets-and-env-review`
- `docs-grounded-recon-report`

Less good:

- `my-claude-prompt`
- `cool-agent-helper`
- `general-ai-thing`
