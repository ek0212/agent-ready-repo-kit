---
name: skill-authoring
description: Create or revise agent skills using the Agent Skills format. Use when user says "create a skill", "build a skill", "write a SKILL.md", "split this skill", "convert this to a skill", or when deciding whether guidance belongs in AGENTS.md vs a skill.
license: MIT
---

Create well-structured, effective skills that follow the Agent Skills specification.

## Workflow

### Step 1: Decide If a Skill Is Needed

Create a skill when:
- The workflow is repeated across sessions or repos.
- The task has multiple steps with judgment points.
- The user keeps pasting the same instructions into chat.
- A section of AGENTS.md has grown into a procedure.
- The body should load only when relevant, not every session.

Do NOT create a skill when:
- One sentence in AGENTS.md would solve it.
- The content is declarative knowledge, not procedure.
- The workflow is a one-off.
- The guidance is mostly volatile project state.

### Step 2: Classify the Skill Category

| Category | Use For | Example |
|---|---|---|
| Document & Asset Creation | Consistent output: docs, designs, code, presentations | frontend-design |
| Workflow Automation | Multi-step processes with consistent methodology | skill-creator |
| MCP Enhancement | Workflow guidance on top of MCP tool access | sentry-code-review |

### Step 3: Define the Boundary

Answer before writing:
- **Name**: The verb or job. Lowercase kebab-case.
- **Trigger**: What user request should activate it?
- **Inputs**: What must be known before starting?
- **Outputs**: What does it produce?
- **Scope**: What is explicitly out of scope?

A broad skill is easy to invoke and hard to follow. Keep boundaries tight.

### Step 4: Write Frontmatter

Required fields:

```yaml
---
name: kebab-case-name
description: What it does. Use when user says "trigger phrase", "another phrase", or asks to [action]. Mention relevant file types if applicable.
---
```

Optional fields:

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
- `name`: kebab-case, no spaces or capitals, must match folder name.
- `description`: MUST include WHAT it does AND WHEN to use it. Under 1024 chars. Include specific trigger phrases users would say. No XML angle brackets.
- Do not use "claude" or "anthropic" in skill names (reserved).

### Step 5: Write the Skill Body

Structure the body with clear steps using concrete action verbs (classify, search, compare, rewrite, delete, verify, update). Each step should include decision criteria.

Recommended structure:

```markdown
[Brief statement of what the skill does]

## Workflow

### Step 1: [First Major Step]
Clear explanation with decision criteria.

### Step 2: [Next Step]
...

## Examples (optional)
Example 1: [common scenario]

## Troubleshooting (optional)
Error: [common error]
Solution: [how to fix]
```

Avoid generic instructions like "be careful" or "think deeply".

### Step 6: Apply Progressive Disclosure

Skills use a three-level system to minimize token usage:

1. **Frontmatter** (always loaded): Enough for Claude to know WHEN to use the skill.
2. **SKILL.md body** (loaded when relevant): Full instructions and guidance.
3. **Linked files** (loaded on demand): Reference docs, examples, scripts.

Keep SKILL.md focused and under 5,000 words. Move bulky material into supporting files:

```
skill-name/
  SKILL.md          # Required — main instructions
  scripts/          # Optional — executable code
  references/       # Optional — docs loaded as needed
  assets/           # Optional — templates, fonts, icons
```

Reference supporting files from SKILL.md and explain when to load them.

Do NOT include a README.md inside the skill folder.

### Step 7: Place the Skill

Common locations:

```
~/.claude/skills/<skill-name>/SKILL.md    # User-global
.claude/skills/<skill-name>/SKILL.md      # Project-local
skills/<skill-name>/SKILL.md              # Repo skills directory
```

For this repo, use `skills/<skill-name>/SKILL.md`.

### Step 8: Validate

Check:
- **Triggers correctly**: Loads on obvious tasks AND paraphrased requests, does NOT load on unrelated queries.
- **Modular**: Works independently alongside other skills.
- **Procedural**: Encodes how to do the task with decision criteria.
- **Scoped**: Specific trigger conditions in description.
- **Durable**: No volatile project state or stale references.
- **Actionable**: Steps use concrete verbs.
- **Concise**: Does not load reference material unnecessarily.
- **Portable**: Works across Claude.ai, Claude Code, and API.

If the skill undertriggers, add more trigger phrases and keywords to the description. If it overtriggers, be more specific or add negative triggers.

## Outputs

- A new or revised SKILL.md.
- Optional supporting files in the same skill directory.
- Updated AGENTS.md skill table entry if applicable.
