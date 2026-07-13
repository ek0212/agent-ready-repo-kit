---
name: frontend-design
description: Create distinctive, production-grade frontend UI. Use when user says "build a landing page", "design a dashboard", "create a component", "make a web app", "build me a UI", or asks for web components, pages, apps, or interfaces.
license: MIT
---

Build memorable production UI. Act as studio design lead. Specific point of view. One justified aesthetic risk. Working code.

## Workflow

### Step 1: Ground Brief

If subject vague, choose concrete subject, audience, page job. State choice. Use user preferences and project context. Pull cues from subject world: materials, tools, artifacts, language, rituals, constraints.

Use real content. Placeholder copy feels templated.

### Step 2: Plan Direction

Before code, create compact plan:

- **Palette:** 4-6 named hex values with roles.
- **Type:** display face, body face, optional utility face.
- **Layout:** concept plus ASCII wireframe when useful.
- **Signature:** one remembered element.
- **Risk:** one deliberate move, why it fits.

Reject plan if it fits any similar product.

### Step 3: Kill Defaults

Use defaults only when brief asks:

- Warm cream near `#F4F1EA`, contrast serif, terracotta.
- Near-black plus acid green/vermilion.
- Broadsheet, hairline rules, zero radius, dense columns.
- Big number, small label, stats, gradient accent.
- 01 / 02 / 03 markers when content not sequence.
- Purple gradient, SaaS cards, overused fonts.

Generic choice found. Revise and say why.

### Step 4: Build

Use existing stack: HTML/CSS/JS, React, Vue, or repo framework.

- Derive color, type, layout, motion from plan.
- Hero is thesis. Lead with subject's most characteristic thing.
- Structure is information. Labels/dividers/numbering/sections encode meaning.
- Motion serves subject. One orchestrated moment beats scattered effects.
- Complexity matches vision. Maximalist needs depth. Minimalist needs precision.
- Watch CSS specificity. Avoid generic class vs element selector collisions.

### Step 5: Refine

Spend boldness in one place. Keep rest disciplined. Cut decoration not serving brief.

Quality floor:

- Mobile responsive.
- Visible keyboard focus.
- Reduced motion respected.
- Button/card/nav text no overflow.
- Screenshot/browser check when possible.

## Aesthetics

- **Typography:** type carries personality. Avoid Arial, Inter, Roboto, Space Grotesk, generic system stacks unless constrained. Make type memorable.
- **Color:** cohesive CSS variables. Dominant, secondary, accent weighting.
- **Motion:** page-load, scroll reveal, hover, or ambient motion only when useful.
- **Layout:** asymmetry, overlap, diagonal flow, broken grids, or deliberate calm.
- **Texture:** gradient mesh, noise, pattern, transparency, shadow, grain, tactile detail when fit.
- **Restraint:** one signature element, not many decorations.

## Copy In UI

Words are design material. Help users understand and act.

- Write from user's side.
- Name controls by user task, not implementation.
- Active voice, sentence case.
- Action name consistent across button, toast, state.
- Failures explain cause and fix. No apology. No vague error.
- Empty states invite action.
- Each text element one job: label, hint, example, error, action.

## Color

Use color for emotional fit.

| Color | Associations |
|---|---|
| Red | passion, anger, danger, warning |
| Orange | warmth, energy, enthusiasm |
| Yellow | joy, intellect, caution |
| Green | nature, growth, health, money |
| Blue | calm, trust, wisdom, mystery |
| Purple | royalty, luxury, creativity |
| Pink | innocence, compassion, love |
| Black | power, sophistication, mystery |
| White | purity, cleanliness, peace |
| Brown | earth, reliability, friendliness |
| Silver | modern, industrial, cold |
| Gold | luxury, wealth, prestige |

## 60/30/10 Rule

| Weight | Use |
|---|---|
| 60% dominant | Backgrounds, large surfaces |
| 30% secondary | Headlines, cards, graphics |
| 10% accent | CTAs, highlights, key controls |

## CTA Color

| Color | Effect | Use |
|---|---|---|
| Yellow | optimistic, attention-grabbing | browsing |
| Red | urgent, energetic | time-sensitive actions |
| Blue | trusted, secure | sign-ups, finance |
| Green | easy, relaxing | stores, money |
| Orange | action-driving | subscribe, buy, sell |
| Pink | soft, youthful | lifestyle, beauty |
| Black | powerful, sleek | luxury |
| Purple | calm, soothing | beauty, wellness |

## UX Laws

| Area | Laws |
|---|---|
| Perception | Proximity groups nearby items. Similarity groups similar items. Common Region groups bounded items. Uniform Connectedness links connected items. Pragnanz favors simplest interpretation. |
| Cognition | Minimize cognitive load. Account for bias. Hick's Law: more choices slow decisions. Miller's Law: chunk memory. Selective Attention: guide focus. |
| Interaction | Fitts's Law: key targets large and close. Goal-Gradient: show progress. Doherty Threshold: keep interactions under 400ms. Active User: design for immediate use. Flow: reduce interruption. |
| Strategy | Aesthetic-Usability: beauty improves perceived usability. Jakob's Law: reuse familiar patterns. Chunking helps processing. Occam: prefer fewer assumptions. Pareto: focus on highest impact. Tesler: place irreducible complexity deliberately. Postel: accept varied input, produce consistent output. |
| Memory | Mental Model: match expectations. Peak-End: nail high point and finish. Von Restorff: make key items distinctive. |
