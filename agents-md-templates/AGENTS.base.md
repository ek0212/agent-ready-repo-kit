# Project Agent Instructions

This file is an always-loaded contract. Keep it short. Do not use it as a repo summary.

## Instruction Budget

- Keep stable constraints and core commands here.
- Put path-specific guidance in `.claude/rules/`.
- Put repeatable procedures, checklists, examples, and reference material in `.claude/skills/`.
- Inspect current code and docs before relying on any summary.

## Project Commands

```bash
# Install

# Run

# Test

# Lint / format

# Build
```

## Default Coding Rules

- Prioritize working, correct code over perfect process.
- Make the smallest reasonable changes.
- Match the style of surrounding code.
- Understand requirements before coding.
- Implement incrementally.
- Add tests for new critical logic or bug fixes.
- Verify with the most relevant command before reporting completion.
- Do not load extra skills or docs when direct repo inspection is enough.

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
