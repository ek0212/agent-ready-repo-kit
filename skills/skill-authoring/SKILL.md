---
name: skill-authoring
description: Create or revise agent skills using Agent Skills format. Use when user says "create a skill", "build a skill", "write a SKILL.md", "split this skill", "convert this to a skill", or asks whether guidance belongs in AGENTS.md vs a skill.
license: MIT
---

Create focused Agent Skills.

## Workflow

### Step 1: Need Skill?

Create skill when:

- Workflow repeats across sessions/repos.
- Task has multiple steps plus judgment.
- User repeats same prompt text.
- AGENTS.md section became procedure.
- Body should load only when relevant.

Do not create skill when:

- One AGENTS.md sentence solves it.
- Content is declarative knowledge, not procedure.
- Workflow one-off.
- Guidance is volatile project state.

### Step 2: Classify

| Category | Use for | Example |
|---|---|---|
| Document & Asset Creation | Repeatable docs, designs, code, decks | frontend-design |
| Workflow Automation | Multi-step method | skill-creator |
| MCP Enhancement | Workflow over MCP tools | sentry-code-review |

### Step 3: Bound

Answer first:

- **Name:** verb/job, lowercase kebab-case.
- **Trigger:** user asks that activate it.
- **Inputs:** facts needed.
- **Outputs:** files/response produced.
- **Scope:** excluded work.

Broad skill easy to trigger, hard to follow. Keep boundary tight.

### Step 4: Frontmatter

Required:

```yaml
---
name: kebab-case-name
description: What it does. Use when user says "trigger phrase", "another phrase", or asks to [action]. Mention relevant file types if applicable.
---
```

Optional:

```yaml
license: MIT
allowed-tools: "Bash(python:*) WebFetch"
compatibility: Requires Node 18+
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: server-name
```

Rules:

- `name`: kebab-case, no spaces/caps, matches folder.
- `description`: what plus when. Under 1024 chars. Include trigger phrases. No XML angle brackets.
- Do not use "claude" or "anthropic" in skill names.

### Step 5: Body

Use concrete verbs: classify, search, compare, rewrite, delete, verify, update. Each step gets decision criteria.

Template:

```markdown
[Brief job statement]

## Workflow

### Step 1: [Major Step]
Decision criteria and action.

### Step 2: [Next Step]
...

## Examples (optional)
Example 1: [common scenario]

## Troubleshooting (optional)
Error: [common error]
Solution: [fix]
```

Avoid vague guidance like "be careful" or "think deeply".

### Step 6: Progressive Disclosure

Loading levels:

1. **Frontmatter:** always loaded, tells when.
2. **SKILL.md body:** loaded when relevant.
3. **Linked files:** loaded on demand.

Keep `SKILL.md` focused and under 5,000 words. Move bulk material:

```
skill-name/
  SKILL.md          # Required, main instructions
  scripts/          # Optional executable code
  references/       # Optional docs loaded as needed
  assets/           # Optional templates, fonts, icons
```

Reference support files and load criteria.

No `README.md` inside skill folder.

### Step 7: Place

Common paths:

```
~/.claude/skills/<skill-name>/SKILL.md    # User-global
.claude/skills/<skill-name>/SKILL.md      # Project-local
skills/<skill-name>/SKILL.md              # Repo skills directory
```

This repo uses `skills/<skill-name>/SKILL.md`.

### Step 8: Validate

Check:

- Triggers on obvious and paraphrased tasks.
- Does not trigger on unrelated tasks.
- Works beside other skills.
- Procedure has decision criteria.
- Description has specific triggers.
- No volatile state or stale refs.
- Concrete verbs.
- Reference material loads only when needed.
- Works across Claude.ai, Claude Code, API.

Undertriggers: add trigger phrases. Overtriggers: narrow description or add negative triggers.

## Outputs

- New/revised `SKILL.md`.
- Optional support files in same skill dir.
- Updated `AGENTS.md` skill table when needed.
