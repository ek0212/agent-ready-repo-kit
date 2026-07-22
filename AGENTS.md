# Agent Instructions

Use Full mode for all repo work and communication.

## Full Mode

Applies to agent messages, plans, docs, comments, docstrings, skill instructions, commit/PR text, and repo-authored user-facing prose.

- Drop articles when meaning stays clear.
- Fragments OK.
- Prefer shortest precise word.
- No filler, hedging, pleasantries, or decorative transitions.
- No tool-call narration. Report result, decision, blocker, or next action.
- No decorative tables or emoji. Use table only when it compresses real comparison or mapping.
- No long raw error-log dumps unless asked. Quote decisive lines. Preserve exact error text.
- Standard acronyms OK. No invented abbreviations.
- Preserve exact technical terms, code, commands, APIs, file paths, identifiers, and user language.
- Use full sentences for security warnings, irreversible confirmations, and order-sensitive steps. Resume Full mode after clear warning.

Merge all worktrees into main after worktree work completes.

## Rules

### Coding

- Ship correct working code.
- Smallest complete change.
- Match nearby style, names, structure, errors.
- Small single-purpose functions.
- Domain names clear.
- Name meaningful strings, numbers, labels, config.
- Shared constants live in existing constants/config.
- Refactor after behavior verified.
- Tests for critical logic and bug fixes.
- Feature flags for experimental, debug, incomplete, risky behavior.
- Verify with narrowest relevant command.

### Change Safety

Ask before public APIs, auth, permissions, billing, data deletion, dependencies, destructive commands, broad refactors.

### Security

- No hardcoded secrets, keys, tokens, credentials.
- Secrets in gitignored `.env` or runtime/server env vars.
- Public env vars are public.
- No logging tokens, auth headers, private data, private provider responses.
- Enable row-level security before client-accessible DB launch.
- Least-privilege DB policies per role and operation.
- Service-role/admin keys server-only. Never expose to client bundles, browser env, logs, examples.
- `.env.example` values fake.
- Check bundles/static output after auth, env, provider-key changes.

### Writing

- Follow Full mode.
- Direct, concise. State assumptions and limits.
- Plain English.
- Use simple sentences. Skip rhetorical flourishes.
- Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.

### Static Text

- Durable comments, docstrings, docs, repo instructions.
- Preserve contracts, traps, constraints, rationale.
- Remove volatile metrics, temporal qualifiers, stale refs, code restatements, narrative history.
- Prefer relative paths.
- Comments rare. Wrong/redundant comment worse than none.

### Structure

- MECE buckets for categories, plans, issues, diagrams, options.
- Buckets mutually exclusive and collectively exhaustive.
- Name unknowns or add `Other / unresolved`.
- Prefer links/refs over duplicated content.

### Model Selection

- Design work uses Claude when model choice exists. Prefer Opus, then Sonnet, then non-Claude. Applies to UX, visual, product, architecture, frontend-design.

### Agent Communication

- Agent-to-agent messages use Full mode.
- If slash commands work, start with `/caveman full`; else put instruction in prompt.
- Do not announce mode. No normal recap.
- Pattern: `[thing] [action] [reason]. [next step].`

## Procedures

### Coding Process

Use for bugs, features, refactors, tests, verification.

1. **Pin behavior.** Restate ask and assumptions. Ask only when missing info makes implementation risky.
2. **Inspect.** Read nearby code, tests, docs, config. Follow local patterns.
3. **Scope.** List affected variants: deploy modes, lifecycle states, entry points, platforms. Widen partial fixes or state limit. Too many ad hoc branches means missing abstraction.
4. **Change.** One coherent smallest-correct change. No broad rewrites, no speculative abstractions.
5. **Update.** Tests for critical logic. Static text only for durable contracts.
6. **Verify.** Narrowest relevant command. UI: desktop plus basic mobile.

Gotchas: no LLMs for deterministic work, no duplicate config/flag/routing systems, no behavior depending on debug flags.

### Writing Process

Use for drafts, edits, summaries, explanations, claim audits.

1. **Classify.** Name writing job.
2. **Structure.** MECE sections/bullets. Name unknowns.
3. **Tighten.** Direct, concise, plain. Remove banned patterns.
4. **Check durability.** Remove stale/volatile text. Cite facts or mark assumptions.

### Static Text Hygiene

Use for comments, docstrings, Markdown before merge, after behavior changes, or docs with metrics, timestamps, stale refs.

1. **Classify:** contract, trap, rationale, security constraint, metric, narrative, code restatement, temporal qualifier.
2. **Docstrings:** contracts, not state. Delete volatile metrics. Prefer none over wrong.
3. **Inline comments:** keep security decisions, non-obvious workarounds, gotchas. Delete restatements and orphan TODOs.
4. **Markdown:** keep traps and schema facts. Remove metrics and investigation stories. Use relative paths.
5. **Refs:** search changed functions/constants in docs. Update or delete stale refs.
6. **Rewrite:** volatile facts become stable constraints.

### Secrets and Env Review

Use for API keys, OAuth, tokens, `.env`, cloud creds, extension manifests, deployment config.

1. **Files:** `.env`, `.env.example`, config, build output, static assets, CI, manifests, deploy config.
2. **Code:** client env access, server-only secrets, logging, errors, proxy routes, OAuth callbacks.
3. **DB:** row-level security, role policies, public key limits, server-only service keys.
4. **Report:** high/medium/low findings with fixes and verification.

## Path-Scoped Rules

Load only for matching paths.

### Python (`**/*.py`, `pyproject.toml`, `uv.lock`)

- Deterministic command output when practical.
- Prefer stdlib unless existing dependency fits.
- Split pure logic from I/O.
- Specific type hints on every function signature.
- Google-style docstrings with Args, Returns, Raises.
- Thin CLI parsing.
- Do not silently skip failed records.
- No LLM for deterministic transforms, routing, retries, status-code handling.

### Chrome Extension (`manifest.json`, `**/*.{js,ts,jsx,tsx}`)

- Preserve Manifest V3.
- Minimal permissions.
- No remote script injection.
- No bundled API keys.
- Treat content scripts, service workers, popup, options as separate boundaries.
- Validate content-script to service-worker messages.

### VS Code Extension (`package.json`, `**/*.ts`, `.vscode/**`)

- Narrow activation events.
- No blocking sync work in extension host.
- Use approved VS Code storage APIs only.
- Sanitize webview content.
- Do not assume workspace trust.

### Web App (`**/*.{jsx,tsx,vue,svelte,astro,css,scss}`)

- Desktop and basic mobile work.
- Reuse existing design tokens, components, layouts.
- Prevent button/card/nav text overflow.
- Verify changed flows in browser.
- Never expose secrets in client bundles.
