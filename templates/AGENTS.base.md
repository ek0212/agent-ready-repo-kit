# Project Agent Instructions

## Project Shape

Briefly describe what this repo is for in 1-3 sentences.

## Stable Constraints

- List constraints that are unlikely to change.
- Include product, platform, privacy, compatibility, deployment, or performance constraints.
- Do not include current feature status or temporary TODOs.

## Development Commands

```bash
# Install

# Run

# Test

# Lint / format

# Build
```

## Code Conventions

- Match surrounding code before introducing new patterns.
- Keep changes scoped to the requested behavior.
- Prefer existing helpers, components, and utilities.
- Add abstractions only when they remove real duplication or clarify boundaries.

## Agent Workflow

1. Read relevant files before editing.
2. State assumptions when behavior is unclear.
3. Make the smallest reasonable change.
4. Run the most relevant verification command.
5. Report what changed and what was not verified.

## Mistakes To Avoid

- Do not rewrite unrelated files.
- Do not introduce a second pattern when one already exists.
- Do not hardcode secrets, tokens, API keys, user data, or environment-specific values.
- Do not update docs with volatile implementation facts that will rot.

## When To Ask

Ask before:

- changing public APIs
- changing auth, permissions, billing, or data deletion behavior
- adding new dependencies
- running destructive commands
- making broad refactors

