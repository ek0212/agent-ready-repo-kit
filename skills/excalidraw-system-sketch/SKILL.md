---
name: excalidraw-system-sketch
description: Plan Excalidraw sketches for fuzzy architecture, product flows, or system maps and write a companion Markdown summary.
when_to_use: Invoke when Mermaid is too rigid, user thinks visually, or system needs grouping, swimlanes, rough sketching, or before/after layout.
---

# Excalidraw System Sketch

## Apply

- `rules/structure-constraints.md`
- `rules/security-constraints.md` when secrets, trust boundaries, user data appear.

## Use When

- User thinks visually.
- Grouping, swimlanes, or rough sketching needed.
- Mermaid too rigid.
- Goal exploration, not final docs.

## Workflow

1. Identify purpose: architecture, user flow, agent workflow, boundary, before/after design.
2. List boxes, groups, arrows, annotations.
3. Decide inside/outside trust boundary.
4. Create/update `.excalidraw` if tooling exists.
5. Always write companion `.md` summary.

## Companion Summary

```markdown
# Diagram Summary

## Purpose

## Main Components

## Boundaries

## Flows

## Open Questions
```

## Rules

- Do not rely on visual file alone.
- Short labels.
- Color has meaning if used.
- One sketch per concept.
