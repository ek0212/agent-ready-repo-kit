---
name: skill-authoring
description: Create or revise modular agent skills using the Agent Skills format and Claude Code skill conventions. Use when a repeated workflow should become a SKILL.md instead of more AGENTS.md text.
when_to_use: Invoke when creating a new skill, splitting a broad skill, converting repeated prompt text into a reusable workflow, or deciding whether guidance belongs in AGENTS.md, a knowledge doc, or a skill.
---

# Skill Authoring

## Inputs

- The workflow, checklist, or prompt to encode.
- Examples of correct and incorrect execution, if available.
- Existing skills for style reference.

## Procedure

### Step 1: Identify The Know-How Gap

Ask:

```text
What does an expert do here that a generic agent gets wrong?
```

Create a skill when:

- The workflow is repeated across sessions or repos.
- The task has multiple steps with judgment points.
- The user keeps pasting the same instructions into chat.
- A section of `AGENTS.md` has become a procedure instead of a stable fact.
- A custom command needs supporting files, frontmatter, or better invocation control.
- The body should load only when relevant, not in every session.

Do not create a skill when:

- One sentence in `AGENTS.md` would solve it.
- The content is declarative knowledge, not procedure.
- The workflow is a one-off.
- The guidance is mostly volatile project state.

### Step 2: Choose The Skill Type

Classify the skill before writing it:

| Type | Use For | Invocation |
|---|---|---|
| Reference | Conventions, style guides, domain rules | Claude can auto-invoke |
| Task | Deploy, commit, release, run a checklist | Consider manual-only |
| Tool-aided | Needs scripts, dynamic context, or shell output | Keep commands explicit |
| Forked | Research or isolated analysis | Use `context: fork` only with a complete task |

### Step 3: Define The Boundary

Answer:

- Name: What is the verb or job? Use lowercase kebab-case.
- Trigger: What user request should activate it?
- Inputs: What must be known before starting?
- Outputs: What does it produce?
- Scope: What is explicitly out of scope?

Keep the boundary tight. A broad skill is easy to invoke and hard to follow.

### Step 4: Write Concise Frontmatter

Use this template:

```markdown
---
name: kebab-case-name
description: Key use case first. Say what the skill does and when it applies.
when_to_use: Optional extra triggers, kept short.
---
```

Rules:

- Put the most important trigger words in `description`.
- Keep `description` and `when_to_use` concise because skill listings have a context budget.
- Add `disable-model-invocation: true` for workflows the user should trigger manually, such as deploy, publish, commit, or send.
- Add `user-invocable: false` only for background knowledge that should not appear as a slash command.
- Avoid `allowed-tools` unless the skill is trusted and tool access should be pre-approved.
- Use `context: fork` only when the skill contains a full standalone task for a subagent.
- Use `argument-hint` and `arguments` when the skill is command-like and expects user input.

### Step 5: Write Procedural Body Content

Use concrete action verbs:

- classify
- search
- compare
- rewrite
- delete
- verify
- update

Each step should include decision criteria. Avoid generic instructions like "be careful" or "think deeply".

### Step 6: Keep SKILL.md Small

Once a skill loads, its content stays in context for the session. Keep `SKILL.md` focused.

Move bulky material into supporting files in the same directory:

```text
skill-name/
  SKILL.md
  reference.md
  examples.md
  scripts/
    helper.sh
```

Reference supporting files from `SKILL.md` and explain when to load or run them.

### Step 7: Use Dynamic Context Only When It Pays For Itself

Claude Code supports shell injection such as:

```markdown
!`git diff HEAD`
```

Use dynamic context for live state, such as diffs or environment checks. Do not use it for facts the agent can cheaply inspect during normal work. Avoid dynamic commands with side effects.

For command-like skills, use `$ARGUMENTS` or named arguments when the user needs to pass a target:

```markdown
Review $ARGUMENTS using the procedure below.
```

### Step 8: Place The Skill

Common locations:

```text
~/.claude/skills/<skill-name>/SKILL.md
.claude/skills/<skill-name>/SKILL.md
skills/<skill-name>/SKILL.md
```

For this repo, use:

```text
skills/<skill-name>/SKILL.md
```

### Step 9: Validate

Check:

- Modular: works independently.
- Procedural: encodes how to do the task.
- Scoped: specific trigger conditions.
- Durable: no volatile project state.
- Actionable: steps use concrete verbs.
- Testable: the result can be checked.
- Concise: does not load reference material unnecessarily.
- Safe: manual-only for side-effect-heavy workflows.

## Outputs

- A new or revised `SKILL.md`.
- Optional supporting files in the same skill directory.
- A short note explaining why this belongs in a skill instead of `AGENTS.md` or a knowledge doc.

## Why This Matters

Skills keep procedural know-how out of always-loaded repo instructions. Good skills load only when useful, stay concise once loaded, and preserve the expert judgment generic agents tend to miss.
