---
name: skill-authoring
description: Procedure for creating new agent skills that are modular, procedural, and domain-specific, following the AISP skill format.
---

# Skill Authoring

## When To Invoke This Skill

- When a recurring multi-step workflow is identified that agents repeatedly get wrong or leave incomplete.
- When domain judgment is needed beyond what a generic prompt can reliably provide.
- When the user asks to create a new skill.
- When an existing skill is too broad and should be split.

## Inputs

- The domain problem or workflow to encode.
- Examples of correct and incorrect execution, if available.
- Existing skills in `.agents/skills/` or `skills/` for format reference.

## Procedure

### Step 1: Identify The Know-How Gap

Ask:

```text
What does an expert do here that a generic agent gets wrong?
```

A skill is warranted when:

- The task requires multi-step reasoning with domain-specific decision points.
- Agents repeatedly make the same mistake without explicit guidance.
- The knowledge is procedural, meaning how to do something, not just what something is.

A skill is not warranted when:

- A single sentence in `AGENTS.md` would suffice.
- The task is a one-off with no reuse.
- The guidance is just a list of facts. Use a knowledge-base doc instead.

### Step 2: Define The Skill Boundary

| Element | Question To Answer |
|---|---|
| Name | What is the verb or action? Use kebab-case. |
| Trigger | When should an agent invoke this? Be specific. |
| Inputs | What does the skill need to start? |
| Outputs | What does the skill produce when done? |
| Scope | What is explicitly out of scope? |

Keep the boundary tight. A skill that tries to cover too much will be invoked when irrelevant and will dilute context.

### Step 3: Write The Procedure

Structure as numbered steps. Each step should include:

1. A clear action verb, such as classify, search, delete, rewrite, compare, verify, or update.
2. Decision criteria embedded in the step.
3. Domain judgment for places where the agent must choose.

Rules:

- Each step should be independently verifiable.
- Avoid rigid scripts that break on edge cases.
- Include concrete examples for categories or decision points.
- If a step needs sub-steps, keep to one level of nesting.

### Step 4: Write `SKILL.md`

Use this template:

```markdown
---
name: kebab-case-name
description: One sentence. What the skill does and when it applies.
---

# Skill Name

## When To Invoke This Skill

- Specific trigger conditions.

## Inputs

- What the skill needs to start.

## Procedure

### Step 1: Action Verb

Steps with embedded decision criteria.

### Step N: Verify

How to confirm the skill was applied correctly.

## Outputs

- What the skill produces when done.

## Why This Matters

One paragraph explaining what goes wrong without this skill.
```

### Step 5: Validate The Skill

Check:

- Modular: can be invoked independently.
- Procedural: encodes multi-step reasoning, not just facts.
- Scoped: clear trigger conditions prevent irrelevant invocation.
- Durable: no timestamps, metrics, or volatile state.
- Actionable: every step has a concrete verb.
- Testable: each step can be verified as done or not done.
- Self-contained: an agent reading only this file can execute the skill.

### Step 6: Place The File

Create one skill per directory:

```text
.agents/skills/{skill-name}/SKILL.md
```

For this repo, use:

```text
skills/{skill-name}/SKILL.md
```

Add supporting scripts or resources in the same directory if needed.

## Outputs

- A new `SKILL.md` file.
- Optional supporting resources in the same directory.
- A short note explaining why this should be a skill instead of an `AGENTS.md` rule or knowledge-base doc.

## Why This Matters

Generic prompts fragment as instruction sets grow, causing attention competition and reduced performance. Skills decouple procedural know-how from execution context, loading only the relevant workflow when needed. A poorly written skill is worse than no skill because it adds context load without adding judgment.
