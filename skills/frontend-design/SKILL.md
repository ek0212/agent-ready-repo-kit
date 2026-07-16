---
name: frontend-design
description: Create distinctive production frontend UI with clear visual direction, emotional intent, responsive behavior, and accessible interaction states. Use when user says "build a landing page", "design a dashboard", "create a component", "make a web app", "build me a UI", "make this feel premium", or asks for polished web design without exact Figma source.
license: MIT
---

Build working UI with specific point of view, one justified signature move, and disciplined polish.

## Scope

Use for design-led web pages, components, apps, dashboards, and redesigns. Use `figma-to-ui` when exact Figma selection defines target. Skip backend-only work and tiny visual bug fixes with no design judgment.

## Inputs

- Product, audience, page job, and primary action.
- Existing repository, components, tokens, content, and constraints.
- Brand cues, references, accessibility needs, and supported viewports.
- Required states, data, routing, and interactions.

User and repository own product facts. Use real supplied content. Mark invented sample content.

## Workflow

### Step 1: Ground Brief

If brief vague, choose concrete audience and page job from repository context. State assumption. Pull cues from subject world: materials, tools, artifacts, language, rituals, and constraints.

Name target feeling at entry, core action, success, and failure. Name trust level. High-stakes flows favor calm feedback, visible state, reversible action, and clear confirmation.

### Step 2: Set Direction

Before code, define:

- Palette: four to six colors with roles.
- Type: display, body, optional utility.
- Layout: composition and responsive rule.
- Signature: one remembered element.
- Risk: one deliberate move and why it fits.
- Emotion: target feeling and trust requirement.

Reject direction that fits any similar product. Avoid default purple gradients, generic SaaS cards, ornamental numbering, and copied trend palettes unless brief supports them.

### Step 3: Design Behavior

- First useful screen shows value and next action.
- Early real success precedes optional setup.
- Pending, success, failure, empty, disabled, and recovery states stay explicit.
- Feedback is immediate and proportional.
- Motion explains hierarchy, state, or cause. It never blocks progress.
- Milestone feedback stays brief and skippable.
- No manufactured urgency or engagement pattern against user goal.

### Step 4: Build In Existing Stack

Reuse repository framework, components, tokens, icons, routing, and styling. Ask before new dependency or styling system.

- Derive type, color, layout, texture, and motion from direction.
- Let structure encode meaning.
- Spend boldness in one place; keep rest quiet.
- Keep UI copy active, task-led, and consistent across control and state.
- Explain errors with cause and recovery.
- Preserve semantic HTML, keyboard access, focus, contrast, alt text, and reduced motion.

### Step 5: Refine In Browser

Run page. Check representative desktop and mobile widths. Fix in order:

1. Information hierarchy and primary action.
2. Layout, overflow, and responsive behavior.
3. Type, spacing, alignment, and component states.
4. Color, border, shadow, texture, and motion.

Cut decoration that does not support subject, hierarchy, trust, or feedback.

## Fallbacks

- No brand system: derive one restrained direction from product context; state choices.
- High-stakes or enterprise flow: favor familiar patterns and clarity over aesthetic risk.
- No browser access: implement static pass and mark visual verification incomplete.
- Existing design system conflicts with concept: preserve system unless user approves broader change.

## Verify

- UI works, not mock-only.
- Primary action clear.
- Direction specific to subject.
- Desktop and mobile work.
- No text or navigation overflow.
- Keyboard focus visible.
- Reduced motion respected.
- All lifecycle states in scope handled.
- Browser comparison completed or named as limit.

## Output

Return working code. Report direction, files changed, route, checks, viewports, assumptions, and known limits.
