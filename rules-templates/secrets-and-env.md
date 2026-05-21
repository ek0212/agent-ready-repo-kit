---
paths:
  - ".env"
  - ".env.*"
  - "**/*.env"
  - "**/*.env.*"
  - "**/manifest.json"
  - ".github/workflows/*.{yml,yaml}"
  - "**/*config*.{js,ts,json,yml,yaml,toml}"
  - "**/*secret*"
---

# Secrets And Environment Rules

- Never hardcode API keys, OAuth secrets, tokens, private keys, or cloud credentials.
- Public environment variables are public.
- `.env.example` should contain variable names and safe placeholders only.
- Do not log tokens, auth headers, prompts with private data, or raw provider responses.
- Keep server-only secrets out of client bundles, static assets, extension manifests, and generated HTML.
- After auth, environment, or build changes, check generated output for accidental exposure.
