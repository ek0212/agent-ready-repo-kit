# Security Constraints

- Never hardcode secrets, keys, tokens, or credentials.
- Use gitignored `.env` files or server/runtime environment variables for secrets.
- Treat public env vars as public.
- Do not log tokens, auth headers, raw private data, or provider responses containing private data.
- Keep `.env.example` values fake.
- Check generated bundles and static output after auth, env, or provider-key changes.
