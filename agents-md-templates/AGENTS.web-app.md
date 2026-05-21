# Web App Agent Instructions

Use this template for React, Next.js, Vite, Astro, Remix, or similar web apps.

Prefer copying [rules-templates/web-app.md](../rules-templates/web-app.md) into `.claude/rules/` when the agent supports path-scoped rules. Use this `AGENTS.md` template when the whole repo is a web app or the tool only supports an always-loaded file.

## Stable Constraints

- UI must work on desktop and basic mobile widths.
- Prefer existing design tokens, components, icons, and layout patterns.
- Do not add decorative UI that makes workflows slower or less scannable.
- Never expose secrets in client-side bundles.

## Commands

```bash
npm install
npm run dev
npm run lint
npm run test
npm run build
```

Adjust commands to match the repo.

## Frontend Workflow

1. Inspect existing components and styling before creating new ones.
2. Reuse shared UI primitives.
3. Keep text inside buttons, cards, and nav items from overflowing.
4. Verify changed flows in the browser when possible.
5. For visual changes, check desktop and mobile.

## Mistakes To Avoid

- Do not invent a second design system.
- Do not put secrets or private keys into `NEXT_PUBLIC_*`, Vite public env vars, static JSON, or generated HTML.
- Do not create giant landing pages when the user asked for a tool or app.
- Do not rely on screenshots, generated assets, or remote images without checking they render.
