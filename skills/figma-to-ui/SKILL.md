---
name: figma-to-ui
description: Implement an exact Figma frame, screen, or component in an existing frontend repository and refine it through browser comparison. Use when user provides a Figma selection link, says "turn this Figma into code", "implement this Figma design", "match this Figma frame", or asks to reproduce Figma UI in React, Next.js, Vue, Svelte, or HTML/CSS.
license: MIT
---

Turn one exact Figma selection into repository-native responsive UI. Figma evidence and running page define acceptance.

## Scope

Use for fidelity implementation from exact Figma node. Use `frontend-design` for open-ended visual direction without Figma source.

Requires authenticated Figma access, target repository, and browser or screenshot tool. User owns product behavior and design intent. Do not infer hidden nodes, assets, or interactions as facts.

## Inputs

- Exact Figma selection URL.
- Target route, page, or component when known.
- Required states and interactions.
- Existing repository and run command.

Infer route, breakpoints, and component reuse only from repository and Figma evidence. State inference.

## Workflow

### Step 1: Pin Selection

Confirm URL resolves to intended node, not file root. Record node name, type, reference dimensions, variants, target entry point, and required states.

### Step 2: Pull Evidence

Use authenticated Figma connector. Retrieve exact-node:

- Screenshot and child hierarchy.
- Auto-layout, constraints, grid, and dimensions.
- Components, variants, variables, styles, type, spacing, radius, shadows, and effects.
- Exportable images, SVGs, icons, and prototype links.

Screenshot is visual source. Structured values guide code. Inspect child nodes when parent omits required detail.

### Step 3: Inspect Repository

Identify framework, package manager, routing, run/test commands, components, tokens, type, spacing, breakpoints, icon system, asset paths, and state patterns.

Map each Figma element to:

- Existing component or token: reuse.
- Durable missing variant: extend.
- Design-specific element: create locally.
- Exported visual: store through existing asset convention.

Do not add Tailwind, component library, icon library, or styling system unless repository already uses it or user approves dependency.

### Step 4: Implement

- Preserve routing, data, state, accessibility, and styling conventions.
- Use supplied assets. Do not replace exact icons/images with emoji or unrelated library icons.
- Match content, hierarchy, type, size, spacing, color, radius, borders, shadows, and alignment.
- Implement visible interaction states and in-scope prototype behavior.
- Build fluid layout between known frame sizes. Avoid coordinates valid only at reference viewport.
- Preserve keyboard focus, semantic controls, alt text, and reduced motion.

### Step 5: Compare

Run page. Capture at reference dimensions, representative mobile width, and each supplied breakpoint variant.

Correct in order:

1. Structure, content, assets.
2. Container, grid, alignment, responsive behavior.
3. Component dimensions and spacing.
4. Type and icon size.
5. Color, border, radius, shadow, effects.
6. Hover, focus, pressed, loading, transition behavior.

Reload after material changes. Stop only when visible differences are resolved or named.

## Verify

- Reference layout closely matches screenshot.
- Mobile has no clipping, overflow, or unreadable density.
- Required interactions work.
- Narrow relevant tests, type check, lint, or build pass.
- Remaining differences tied to named constraint.

Do not claim pixel-perfect match without direct comparison.

## Fallbacks

- Figma auth failure: request accessible selection URL or exported screenshot.
- Missing asset/font: use approved repository fallback and name difference.
- No mobile design: derive from repository breakpoints and label responsive assumptions.
- Cannot run browser: implement static pass, state visual verification incomplete.

## Output

Report files changed, route/component, checks run, viewports compared, assumptions, and remaining differences.
