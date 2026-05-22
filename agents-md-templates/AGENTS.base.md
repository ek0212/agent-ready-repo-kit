# Project Agent Instructions

This file is a thin wrapper. Keep procedural detail in skills, not here.

## Project Commands

```bash
# Install

# Run

# Test

# Lint / format

# Build
```

## Skill Routing

- Start with `skill-router`.
- Default to one skill.
- Use at most three skills per pass.
- Prefer reading code and docs over loading more instructions.

## Default Coding Rules

- Prioritize working, correct code over perfect process.
- Make the smallest reasonable changes.
- Match the style of surrounding code.
- Understand requirements before coding.
- Implement incrementally.
- Add tests for new critical logic or bug fixes.
- Verify with the most relevant command before reporting completion.

## Durable Text And Structure

- Keep comments, docstrings, docs, and repo instructions durable. Preserve contracts, traps, constraints, and decision rationale.
- Remove or rewrite volatile metrics, temporal qualifiers, stale references, code restatements, and narrative history.
- Use MECE structure for categories, plans, issue breakdowns, and option sets: no overlapping buckets and no missing cases.
- If a structure cannot be fully MECE yet, name the unknowns or create an explicit "Other / unresolved" bucket instead of forcing false precision.

## Writing Style

- Be direct and concise. State assumptions and limitations clearly.
- Use plain English.
- No "This isn't X. It's Y." contrast patterns.
- No self-answering rhetorical questions.
- No em-dashes, use commas instead.
- No three-part alliterative phrases.
- No vague inspirational pivots.
- No unsourced claims or unverified quotes.

## Ask Before

- Changing public APIs.
- Changing auth, permissions, billing, or data deletion behavior.
- Adding new dependencies.
- Running destructive commands.
- Making broad refactors.
