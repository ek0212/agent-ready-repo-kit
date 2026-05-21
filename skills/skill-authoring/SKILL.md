---
name: skill-authoring
description: Create, revise, split, or evaluate modular agent skills and decide when guidance belongs in AGENTS.md, rules, skills, hooks, settings, or docs.
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
- The content is a path-specific constraint better handled by `.claude/rules/`.
- The content is declarative knowledge that belongs in docs.
- The workflow is a one-off.
- The guidance is mostly volatile project state.

### Step 2: Choose The Right Layer

| Layer | Use For |
|---|---|
| `AGENTS.md` | Always-loaded constraints, core commands, stable "ask before" rules |
| `CLAUDE.md` | Claude-specific wrapper, often importing `AGENTS.md` |
| `.claude/rules/` | File-type or directory-specific constraints with `paths:` frontmatter |
| Skill | Repeatable procedures, optional reference material, examples, scripts |
| Hook, settings, CI | Enforced behavior that must not rely on model compliance |
| Repo docs | Human-readable architecture, product, or process documentation |

### Step 3: Choose The Skill Type

| Type | Use For | Invocation |
|---|---|---|
| Reference | Conventions, style guides, domain rules | Agent can auto-invoke |
| Task | Deploy, commit, release, run a checklist | Consider manual-only |
| Tool-aided | Needs scripts, dynamic context, or shell output | Keep commands explicit |
| Forked | Research or isolated analysis | Use only with a complete standalone task |

### Step 4: Define The Boundary

Answer:

- Name: What is the verb or job? Use lowercase kebab-case.
- Trigger: What user request should activate it?
- Inputs: What must be known before starting?
- Outputs: What does it produce?
- Scope: What is explicitly out of scope?

Keep the boundary tight. A broad skill is easy to invoke and hard to follow.

### Step 5: Write Concise Frontmatter

Use this template:

```markdown
---
name: kebab-case-name
description: Key use case first. Say what the skill does and when it applies.
---
```

Rules:

- Put the most important trigger words in `description`.
- Keep `description` concise because skill listings have a context budget.
- Add `disable-model-invocation: true` for workflows the user should trigger manually, such as deploy, publish, commit, or send.
- Avoid tool pre-approval unless the skill is trusted and the tool access is necessary.
- Use arguments when the skill is command-like and expects a target.

### Step 6: Write Procedural Body Content

Use concrete action verbs:

- classify
- search
- compare
- rewrite
- delete
- verify
- update

Each step should include decision criteria. Avoid generic instructions like "be careful" or "think deeply".

### Step 7: Keep SKILL.md Small

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

### Step 8: Use Dynamic Context Only When It Pays For Itself

Use dynamic context for live state such as diffs or environment checks. Do not use it for facts the agent can cheaply inspect during normal work. Avoid dynamic commands with side effects.

### Step 9: Place The Skill

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

### Step 10: Validate

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
- A short note explaining why this belongs in a skill instead of `AGENTS.md`, rules, hooks, settings, or repo docs.
