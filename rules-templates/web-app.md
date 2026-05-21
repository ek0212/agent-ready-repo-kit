---
paths:
  - "**/*.{js,jsx,ts,tsx,css,scss,html,astro,svelte,vue}"
  - "package.json"
  - "vite.config.*"
  - "next.config.*"
---

# Web App Rules

- Reuse existing components, design tokens, icons, routes, and layout patterns.
- Keep UI usable on desktop and basic mobile widths.
- Do not invent a second design system.
- Do not add decorative UI that slows repeated workflows or makes data harder to scan.
- Prevent text overflow in buttons, nav items, cards, panels, and tables.
- Never expose secrets in client-side bundles, public env vars, static JSON, or generated HTML.
- For visual changes, verify the affected flow in a browser when possible.
