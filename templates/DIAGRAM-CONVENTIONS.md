# Diagram Conventions

Use diagrams when prose hides shape, ownership, or flow.

## Mermaid

Use Mermaid for diagrams that should live in Markdown:

- architecture maps
- data flow
- sequence diagrams
- state machines
- tool boundary maps

Keep Mermaid diagrams small enough to review in a PR.

## Excalidraw

Use Excalidraw for fuzzy or spatial thinking:

- product flows
- agent workspace maps
- rough system sketches
- before/after architecture
- diagrams that benefit from hand-drawn grouping

Pair Excalidraw with a short Markdown summary so future agents can understand the sketch without visual parsing.

## File Names

```text
docs/diagrams/architecture.mmd
docs/diagrams/data-flow.mmd
docs/diagrams/mcp-boundaries.mmd
docs/diagrams/system-sketch.excalidraw
docs/diagrams/system-sketch.md
```

## Rules

- Diagrams should show boundaries, not every file.
- Label trust boundaries and external services.
- Label where secrets enter or leave the system.
- Avoid implementation details that change weekly.

