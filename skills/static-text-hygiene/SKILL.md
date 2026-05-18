---
name: static-text-hygiene
description: Reviews agent docs and removes stale, volatile, or overly specific text. Use when AGENTS.md, CLAUDE.md, CONTEXT.md, or docs have become noisy.
---

# Static Text Hygiene

## Use When

- Agent instructions are long and low-signal.
- Docs include implementation facts that change often.
- A repo has repeated stale comments or outdated architecture notes.
- The user wants constraints and conventions instead of brittle summaries.

## Keep

- Stable repo purpose.
- Verification commands.
- Naming, style, and architecture conventions.
- Mistakes agents should avoid repeating.
- Hard boundaries: auth, data, secrets, destructive commands, public APIs.
- Domain vocabulary and relationships in `CONTEXT.md`.

## Remove Or Rewrite

- Exhaustive file maps.
- "Currently" statements that will expire.
- Feature status.
- Bug lists.
- Detailed dependency versions unless they are constraints.
- Implementation claims that code can answer.
- Long examples that cause the agent to overfit.

## Rewrite Pattern

Turn volatile facts into stable constraints:

```text
Bad: The auth code lives in src/auth/session.ts and uses function createMagicLinkToken.
Good: Reuse the existing auth module. Do not add a second token flow without asking.
```

```text
Bad: The app currently has 11 pages.
Good: New routes should follow the existing routing and layout patterns.
```

## Workflow

1. Read the doc being cleaned.
2. Mark each paragraph as keep, rewrite, move, or remove.
3. Move domain terms to `CONTEXT.md`.
4. Move hard architectural decisions to ADRs only if they pass the ADR test.
5. Keep the final doc short and action-oriented.

## Output

Provide:

- what was removed
- what was rewritten as durable guidance
- what was moved elsewhere
- any missing verification commands

