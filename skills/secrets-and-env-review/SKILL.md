---
name: secrets-and-env-review
description: Review secrets, environment variables, config files, client bundles, and build outputs for accidental exposure.
when_to_use: Invoke when a repo uses API keys, OAuth, tokens, .env files, cloud credentials, extension manifests, deployment config, or provider keys.
---

# Secrets And Env Review

## Use When

- A repo uses API keys, OAuth, tokens, `.env`, or cloud credentials.
- A web app, extension, or static site may bundle secrets.
- An AI app uses provider keys or tool credentials.
- The user asks for lightweight security review.

## Review Areas

### Files

- `.env`
- `.env.example`
- config files
- build output
- static assets
- GitHub Actions workflows
- extension manifests
- deployment config

### Code

- client-side environment access
- server-only secrets
- logging
- error messages
- API proxy routes
- OAuth callback handling

## Rules

- Never hardcode secrets.
- Use `.env` files that are gitignored, or server/runtime environment variables only.
- Public env vars are public.
- Do not log tokens, prompts with private data, auth headers, or raw provider responses.
- `.env.example` should show names, not real values.
- Build artifacts should not contain provider keys.
- After auth or data changes, check build outputs for accidental exposure.

## Output

Return findings ordered by risk:

```markdown
## Findings

- High: ...
- Medium: ...
- Low: ...

## Fixes

## Verification
```

If no issues are found, say so and list what was checked.
