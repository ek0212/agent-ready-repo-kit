# Chrome Extension Agent Instructions

Append this to `AGENTS.base.md` for Manifest V3 browser extensions.

## Stable Constraints

- Keep permissions minimal.
- Prefer local processing over remote calls when possible.
- Preserve Manifest V3 compatibility.
- Treat content scripts, background service workers, popup UI, and options pages as separate boundaries.

## Commands

```bash
npm install
npm run build
npm run lint
```

Adjust commands to match the repo.

## Review Checklist

- `manifest.json` permissions are necessary and specific.
- No API keys or tokens are bundled into the extension.
- Content scripts only touch expected pages and selectors.
- Messaging between content scripts and service worker validates message shape.
- Storage use is documented: local, sync, Gist, or remote service.

## Mistakes To Avoid

- Do not request broad host permissions without explaining why.
- Do not inject remote scripts.
- Do not assume popup state persists.
- Do not put user data into logs.
