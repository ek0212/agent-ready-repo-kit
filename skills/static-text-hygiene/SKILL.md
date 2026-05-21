---
name: static-text-hygiene
description: Audit and fix comments, docstrings, Markdown docs, and AGENTS instructions so static text stays accurate as code changes.
---

# Static Text Hygiene

## When To Invoke This Skill

- Before merging any PR that adds or modifies Markdown docs, docstrings, or inline comments.
- When reviewing a file and noticing comments that describe "what" rather than "why".
- When a knowledge-base doc references specific metrics, row counts, timing data, or temporary status.
- After any behavioral change to code that has associated docstrings or Markdown references.
- When `AGENTS.md`, `CLAUDE.md`, comments, docstrings, or docs have become noisy or stale.

## Inputs

- The file or folder being changed or reviewed.
- Surrounding codebase context: function signatures, callers, constants, tests, and linked docs.

## Procedure

### Step 1: Classify Each Piece Of Static Text

For every comment, docstring, or Markdown section, ask:

```text
If the underlying reality changed tomorrow, would this text cause an agent to make a wrong decision?
```

Classify into:

| Category | Keep? | Examples |
|---|---|---|
| Contract | Yes | Args, Returns, Raises, API expectations |
| Trap | Yes | "author values differ between tables: `human`/`ai` vs `user`/`bot`" |
| Decision rationale | Yes | "dynamic not string because Kusto auto-parses JSON arrays" |
| Security or compliance constraint | Yes | "This module is only intended for Security usage" |
| Current metric | Remove | row counts, timing, fill rate, cache hit rate |
| Narrative context | Remove | investigation story, historical motivation |
| Code restatement | Remove | `# increment counter` above `counter += 1` |
| Temporal qualifier | Remove or rewrite | "currently", "as of", "for now" |

### Step 2: Fix Docstrings

1. Describe contracts, not current state.
2. Delete data volumes, row counts, timing measurements, and "currently" or "as of" qualifiers.
3. When changing a signature, update the docstring in the same diff.
4. Prefer no docstring over a wrong docstring.

### Step 3: Fix Inline Comments

1. If renaming a variable makes the comment unnecessary, rename and delete the comment.
2. Keep only security decisions, non-obvious workarounds, regulatory constraints, and gotchas.
3. Delete code restatements, TODOs without linked work items, and commented-out code.

### Step 4: Fix Markdown And Knowledge-Base Docs

1. Keep traps and schema facts.
2. Remove specific metrics and capacity projections unless the doc is explicitly a dated report.
3. State facts and decisions, not investigation stories.
4. Do not duplicate guidance that belongs at the code call site.
5. Use relative paths only. Do not include machine-specific absolute paths.
6. Name docs for the thing they describe, not the feature that prompted the investigation.
7. Avoid "Last updated" timestamps or PR references in durable docs.

### Step 5: Check For Stale References

After any behavioral change:

1. Search for the changed function, class, constant, route, event, or setting across Markdown, comments, and docstrings.
2. Update or delete stale mentions.
3. If a checklist has completed items with no ongoing relevance, remove them.
4. Keep unchecked work only when it is still active and belongs in docs rather than an issue tracker.

### Step 6: Rewrite Volatile Facts As Stable Constraints

```text
Bad: The auth code lives in src/auth/session.ts and uses function createMagicLinkToken.
Good: Reuse the existing auth module. Do not add a second token flow without asking.
```

```text
Bad: The app currently has 11 pages.
Good: New routes should follow the existing routing and layout patterns.
```

```text
Bad: This dataset currently has about 5.8M rows and 94% label fill rate.
Good: Do not assume row counts or label coverage; validate them from the current source before analysis.
```

### Step 7: Verify

For each remaining piece of static text, confirm:

- It describes a contract, trap, decision rationale, or durable constraint.
- It would still be accurate if data volumes doubled or halved.
- It does not duplicate information available by reading nearby code.
- It uses relative paths only.
- It does not include "currently", "as of", or temporary status language.

## Outputs

- Cleaned files with only durable static text remaining.
- List of stale references found and fixed, if any.
- List of volatile claims removed or rewritten.

## Why This Matters

Stale static text is unusually dangerous for LLM agents because agents often trust comments and docs over code. A wrong comment, stale docstring, or obsolete Markdown section can become a future bad edit. Durable docs should preserve contracts, traps, constraints, and decision rationale, not fossilized implementation state.
