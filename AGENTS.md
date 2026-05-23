# Agent Instructions

Keep this file under 200 lines. Only genuine multi-step procedures belong in `skills/`.

## Rules

### Coding

- Prioritize working, correct code over perfect process.
- Make the smallest reasonable change that satisfies the request.
- Match surrounding code style, naming, structure, and error handling.
- Keep functions small and single-purpose.
- Use clear domain-specific names.
- Declare named constants for meaningful strings, numbers, labels, and config values.
- Centralize shared constants in an existing constants or config file.
- Refactor only after behavior is verified.
- Add or update tests for new critical logic and bug fixes.
- Use feature flags for experimental, debug, incomplete, or risky rollout behavior.
- Verify with the narrowest relevant command before reporting completion.

### Change Safety

Ask before: changing public APIs, changing auth/permissions/billing/data-deletion, adding new dependencies, running destructive commands, making broad refactors.

### Security

- Never hardcode secrets, keys, tokens, or credentials.
- Use gitignored `.env` files or server/runtime environment variables for secrets.
- Treat public env vars as public.
- Do not log tokens, auth headers, raw private data, or provider responses containing private data.
- Keep `.env.example` values fake.
- Check generated bundles and static output after auth, env, or provider-key changes.

### Writing

- Be direct and concise. State assumptions and limitations clearly.
- Use plain English.
- No "This isn't X. It's Y." contrast patterns, self-answering rhetorical questions, em-dashes (use commas), three-part alliterative phrases, vague inspirational pivots, unsourced claims, or unverified quotes.

### Static Text

- Keep comments, docstrings, docs, and repo instructions durable.
- Preserve contracts, traps, constraints, and decision rationale.
- Remove volatile metrics, temporal qualifiers, stale references, code restatements, and narrative history.
- Prefer relative paths in durable docs. Prefer no comment over a wrong one.

### Structure

- Use MECE structure for categories, plans, issue breakdowns, diagrams, and option sets.
- Make buckets mutually exclusive and collectively exhaustive.
- Name unknowns or create an explicit `Other / unresolved` bucket.
- Prefer links and references over duplicating content.

## Procedures

### Coding Process

Use for: bug fixes, feature work, refactors, test updates, verification.

1. **Pin down behavior.** Restate the request and assumptions. Ask only when missing info would make implementation risky.
2. **Inspect before editing.** Read nearby code, tests, docs, config. Prefer local conventions.
3. **Smallest correct change.** One coherent change at a time. No broad rewrites or speculative abstractions.
4. **Update tests and static text.** Add tests for critical logic. Update comments/docstrings only when they preserve durable contracts.
5. **Verify.** Run the narrowest relevant command. For UI changes, check desktop and basic mobile.

Gotchas: do not turn deterministic operations into LLM calls, do not create duplicate config/flag/routing systems, do not ship behavior that relies on debug flags.

### Writing Process

Use for: drafting or editing docs, comments, summaries, reports, public explanations.

1. **Identify the job.** Classify as drafting, editing, summarizing, explaining, or auditing claims.
2. **Structure.** Use MECE sections/bullets for categories, options, plans, tradeoffs. Name unknowns.
3. **Tighten.** Make text direct, concise, plain. Remove banned patterns from writing rules.
4. **Check durability.** Remove stale/volatile text. Cite factual claims or mark as assumptions.

### Static Text Hygiene

Use for: auditing comments, docstrings, Markdown docs before merge, after behavioral changes, when docs have metrics/timestamps/stale references.

1. **Classify each piece:** contract (keep), trap (keep), decision rationale (keep), security constraint (keep), current metric (remove), narrative context (remove), code restatement (remove), temporal qualifier (remove/rewrite).
2. **Fix docstrings:** describe contracts not state, delete volatile metrics, prefer no docstring over wrong one.
3. **Fix inline comments:** keep only security decisions, non-obvious workarounds, gotchas. Delete code restatements and orphan TODOs.
4. **Fix Markdown:** keep traps and schema facts, remove specific metrics, state facts not investigation stories, use relative paths.
5. **Check stale references:** search for changed functions/constants across docs, update or delete.
6. **Rewrite volatile facts as stable constraints.**

### Secrets and Env Review

Use for: repos with API keys, OAuth, tokens, .env, cloud credentials, extension manifests, deployment config.

1. **Check files:** `.env`, `.env.example`, config files, build output, static assets, CI workflows, manifests, deployment config.
2. **Check code:** client-side env access, server-only secrets, logging, error messages, API proxy routes, OAuth callbacks.
3. **Report findings** ordered by risk (high/medium/low) with fixes and verification steps.

## Path-Scoped Rules

Load these only when working on files matching the specified paths.

### Python (`**/*.py`, `pyproject.toml`, `uv.lock`)

- Keep command output deterministic where practical.
- Prefer stdlib unless an existing dependency covers it.
- Separate pure logic from I/O for testability.
- Specific type hints on all function signatures.
- Google-style docstrings with Args, Returns, Raises.
- Keep CLI argument parsing thin.
- Do not silently skip failed records.
- Do not call an LLM for deterministic transforms, routing, retries, or status-code handling.

### Chrome Extension (`manifest.json`, `**/*.{js,ts,jsx,tsx}`)

- Preserve Manifest V3 compatibility.
- Keep permissions minimal. No remote script injection. No bundled API keys.
- Treat content scripts, service workers, popup, options as separate boundaries.
- Validate message shapes between content scripts and service workers.

### VS Code Extension (`package.json`, `**/*.ts`, `.vscode/**`)

- Keep activation events narrow. No blocking synchronous work in extension host.
- Store data only in approved VS Code storage APIs.
- Webviews must sanitize rendered content. Do not assume workspace trust.

### Web App (`**/*.{jsx,tsx,vue,svelte,astro,css,scss}`)

- UI must work on desktop and basic mobile widths.
- Reuse existing design tokens, components, layout patterns.
- Keep text in buttons/cards/nav from overflowing.
- Verify changed flows in browser. Never expose secrets in client bundles.

## Skills

Load from `skills/<name>/SKILL.md` only when the task matches.

| Skill | Use when |
|---|---|
| `skill-authoring` | Creating a new skill, splitting a broad skill, converting repeated prompt text into a reusable workflow, or deciding whether guidance belongs in AGENTS.md vs a skill. |
| `frontend-design` | Building distinctive web components, pages, or applications where design quality and creative aesthetics matter. |
| `mermaid-architecture-map` | Prose hides flow or ownership, repo needs a GitHub-renderable diagram, or a system boundary should be explicit. |
| `excalidraw-system-sketch` | Mermaid is too rigid, the user thinks visually, or the system needs grouping, swimlanes, or rough sketching. |

### Skill Loading Rules

- Default to zero skills. The procedures above cover most tasks.
- Load at most one skill per pass unless the task spans multiple domains.
- Prefer reading code and docs over loading more instructions.
