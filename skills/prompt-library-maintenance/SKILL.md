---
name: prompt-library-maintenance
description: Curates reusable prompt libraries, suffixes, and backlog prompts. Use when maintaining Prompt Garden, promptbooks, or shared agent instructions.
---

# Prompt Library Maintenance

## Use When

- The user has a pile of prompts.
- A prompt library needs cleanup.
- Prompt Garden or a similar tool needs better organization.
- A team needs reusable agent instructions.

## Organize By Job

Prefer job-based categories:

- build
- debug
- refactor
- review
- explain
- design
- write
- research
- verify

Avoid organizing only by tool name. Prompts should survive tool churn.

## Prompt Shape

Use this compact structure:

```text
Context:
Task:
Constraints:
Output:
Verification:
```

For agent prompts, add:

```text
Success criteria:
Files or scope:
Things to avoid:
```

## Suffix Rules

Good suffixes are short and stable:

- Be concise.
- Cite files or sources used.
- State assumptions.
- Tell me what you verified.

Bad suffixes are long, tool-specific, or contradictory.

## Maintenance Workflow

1. Deduplicate near-identical prompts.
2. Rename prompts by outcome, not clever title.
3. Split giant prompts into reusable parts.
4. Remove stale product or file references.
5. Add examples only when output shape matters.
6. Export to JSON or Markdown for backup.

## Output

Return:

- cleaned prompt list
- suggested categories
- reusable suffixes
- prompts that should become skills instead

