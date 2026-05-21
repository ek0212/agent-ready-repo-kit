---
name: excalidraw-system-sketch
description: Plan Excalidraw sketches for fuzzy architecture, product flows, system maps, swimlanes, trust boundaries, or before-and-after layouts.
---

# Excalidraw System Sketch

## Use When

- The user thinks visually.
- The system needs grouping, swimlanes, or rough sketching.
- Mermaid feels too rigid.
- The goal is exploration, not final documentation.

## Workflow

1. Identify the sketch purpose: architecture, user flow, agent workflow, system boundary, or before/after design.
2. List the boxes, groups, arrows, and annotations.
3. Decide what belongs inside or outside the trust boundary.
4. Create or update an `.excalidraw` file if tooling is available.
5. Always write a companion `.md` summary.

## Companion Summary Format

```markdown
# Diagram Summary

## Purpose

## Main Components

## Boundaries

## Flows

## Open Questions
```

## Rules

- Do not rely on the visual file alone.
- Keep labels short.
- Use color meaningfully if colors are used.
- Prefer one sketch per concept.
