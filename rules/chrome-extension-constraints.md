---
paths:
  - "manifest.json"
  - "public/manifest.json"
  - "**/*.{js,ts,jsx,tsx}"
---
# Chrome Extension Constraints

- Preserve Manifest V3 compatibility.
- Keep permissions minimal and specific.
- Do not inject remote scripts.
- No API keys or tokens should be bundled into the extension.
- Treat content scripts, background service workers, popup UI, and options pages as separate boundaries.
- Validate message shapes between content scripts and service workers.
- Do not assume popup state persists.
