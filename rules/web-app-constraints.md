---
paths:
  - "**/*.{jsx,tsx,vue,svelte,astro,css,scss}"
  - "package.json"
  - "vite.config.*"
  - "next.config.*"
  - "astro.config.*"
---
# Web App Constraints

- UI must work on desktop and basic mobile widths.
- Prefer existing design tokens, components, icons, and layout patterns.
- Reuse shared UI primitives before creating new ones.
- Keep text inside buttons, cards, and nav items from overflowing.
- Verify changed flows in the browser when possible.
- Never expose secrets in client-side bundles or public env vars.
