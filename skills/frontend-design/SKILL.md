---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use when user says "build a landing page", "design a dashboard", "create a component", "make a web app", "build me a UI", or asks to build web components, pages, applications, or interfaces. Generates creative, polished code that avoids generic AI aesthetics.
license: MIT
---

Build distinctive, production-grade frontend interfaces. Avoid generic "AI slop" aesthetics. Produce real working code with exceptional attention to aesthetic details and creative choices.

## Workflow

### Step 1: Understand Context
- **Purpose**: What problem does this interface solve? Who uses it?
- **Constraints**: Framework, performance, accessibility requirements.
- **Differentiation**: What makes this UNFORGETTABLE?

### Step 2: Commit to an Aesthetic Direction
Pick a clear tone: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. Bold maximalism and refined minimalism both work — the key is intentionality, not intensity.

### Step 3: Implement
Produce working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

### Step 4: Refine
Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate animations and effects. Minimalist designs need restraint, precision, and careful spacing/typography.

## Aesthetics Guidelines

- **Typography**: Distinctive, characterful font choices. Never generic (Arial, Inter, Roboto, system fonts). Pair a display font with a refined body font.
- **Color & Theme**: Cohesive palette via CSS variables. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Follow the 60-30-10 rule (see below).
- **Motion**: Prioritize CSS-only for HTML, Motion library for React. Focus on high-impact moments: one well-orchestrated page load with staggered reveals beats scattered micro-interactions. Scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Texture**: Atmosphere and depth, not solid colors. Gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, grain overlays.

**NEVER**: Overused fonts (Inter, Roboto, Space Grotesk, Arial), cliched purple-gradient-on-white, predictable layouts, cookie-cutter design. Every generation must vary theme, fonts, and aesthetic. No convergence on common choices.

## Color Psychology

Use color associations to reinforce the emotional tone of the interface. Choose dominant colors that align with the product's purpose.

| Color | Associations |
|---|---|
| Red | passion, love, anger, danger, warning |
| Orange | warmth, energy, happiness, enthusiasm |
| Yellow | sunshine, happiness, joy, intellect, caution |
| Green | nature, growth, health, harmony, money |
| Blue | calmness, trust, loyalty, wisdom, mystery |
| Purple | royalty, luxury, creativity, mystery |
| Pink | innocence, femininity, compassion, love |
| Black | power, sophistication, mystery, evil |
| White | purity, innocence, cleanliness, peace |
| Brown | earthiness, reliability, dependability, friendliness |
| Silver | modernity, sophistication, industrial, cold |
| Gold | luxury, wealth, success, prestige, glamor |

## The 60-30-10 Color Rule

Distribute color by visual weight:

- **60% Dominant** — Neutral or primary color. Base of the design (backgrounds, large surfaces).
- **30% Secondary** — Medium components: headlines, cards, graphic elements.
- **10% Accent** — Highlights: CTA buttons, pop-ups, key interface elements.

## CTA Button Color Guide

Choose button colors based on the action's intent and emotional response needed.

| Color | Effect | Common Use |
|---|---|---|
| Yellow | Optimistic, youthful | Grabbing attention, window shoppers |
| Red | Energy, urgency, increases heart rate | Clearance sales, time-sensitive actions |
| Blue | Trust, security | Banks, businesses, sign-ups |
| Green | Wealth, easy to process, relaxing | Stores, financial products |
| Orange | Aggressive, action-driving | Subscribe, buy, sell CTAs |
| Pink | Romantic, soft, youthful | Lifestyle, beauty products |
| Black | Powerful, sleek | Luxury product marketing |
| Purple | Soothing, calm | Beauty, anti-aging products |

## Laws of UX

Apply these principles when making design decisions. They are constraints on how humans perceive and interact with interfaces.

### Perception & Grouping
- **Law of Proximity**: Objects near each other are perceived as grouped.
- **Law of Similarity**: Similar elements are perceived as a complete picture, shape, or group, even when separated.
- **Law of Common Region**: Elements sharing an area with a clearly defined boundary are perceived as grouped.
- **Law of Uniform Connectedness**: Visually connected elements are perceived as more related than unconnected ones.
- **Law of Prägnanz**: People interpret ambiguous or complex images as the simplest form possible, because it requires the least cognitive effort.

### Cognition & Decision
- **Cognitive Load**: Minimize the mental resources needed to understand and interact with an interface.
- **Cognitive Bias**: Account for systematic errors of thinking that influence perception and decision-making.
- **Hick's Law**: Decision time increases with the number and complexity of choices. Reduce options where possible.
- **Miller's Law**: Working memory holds 7 (plus or minus 2) items. Chunk information accordingly.
- **Selective Attention**: Users focus only on a subset of stimuli, usually those related to their goals. Guide attention to what matters.

### Interaction & Behavior
- **Fitts's Law**: Time to acquire a target is a function of distance to and size of the target. Make key actions large and close.
- **Goal-Gradient Effect**: Motivation to approach a goal increases with proximity to the goal. Show progress.
- **Doherty Threshold**: Productivity soars when interaction pace stays under 400ms. Neither user nor system should wait on the other.
- **Paradox of the Active User**: Users never read manuals; they start using software immediately. Design for immediate use.
- **Flow**: Support the state of energized focus and full immersion. Minimize interruptions and friction.

### Design Strategy
- **Aesthetic-Usability Effect**: Users perceive aesthetically pleasing design as more usable. Beauty is functional.
- **Jakob's Law**: Users prefer your site to work the same way as sites they already know. Leverage familiar patterns.
- **Chunking**: Break information into meaningful groups for easier processing.
- **Occam's Razor**: Among designs that work equally well, prefer the one with the fewest assumptions and elements.
- **Pareto Principle**: Roughly 80% of effects come from 20% of causes. Focus effort on the critical 20%.
- **Tesler's Law** (Conservation of Complexity): Every system has irreducible complexity. Decide whether the user or the system bears it.
- **Postel's Law**: Be liberal in what you accept, conservative in what you send. Tolerate varied input, produce consistent output.

### Memory & Experience
- **Mental Model**: Users carry compressed models of how systems work. Align with their expectations.
- **Peak-End Rule**: People judge experiences by how they felt at the peak and at the end, not the average. Nail the high points and the finish.
- **Von Restorff Effect** (Isolation Effect): Among similar objects, the one that differs is most likely remembered. Make key elements distinctive.
