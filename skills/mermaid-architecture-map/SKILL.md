---
name: mermaid-architecture-map
description: Create concise Mermaid diagrams for architecture, data flow, request sequence, lifecycle state, dependencies, or trust boundaries in Markdown. Use when prose hides flow or ownership, user asks for Mermaid, repository needs GitHub-rendered diagram, or system boundary must be explicit.
license: MIT
---

Create smallest diagram that makes one relationship clear.

## Scope

Use for exact flow, sequence, state, dependency, and boundary diagrams. Use `excalidraw-system-sketch` for fuzzy spatial exploration, swimlanes, or rough before-and-after thinking.

## Inputs

- Diagram question and audience.
- Verified components, actors, states, and edges.
- External systems, trust boundaries, secrets, and user-data paths.
- Target Markdown file or standalone `.mmd` path.

User or repository owns architecture facts. Label inference and unknowns.

## Workflow

1. State one question diagram answers.
2. Pick simplest type:
   - `flowchart LR`: architecture, ownership, boundaries.
   - `sequenceDiagram`: ordered request or agent flow.
   - `stateDiagram-v2`: lifecycle and transitions.
   - `graph TD`: dependency hierarchy.
3. Include only nodes needed for question.
4. Group system and trust boundaries.
5. Label external services and secret/user-data entry points. Never include secret values.
6. Use short node labels and verb-led edges.
7. Save `.mmd`; embed in Markdown when requested.

## Fallbacks

- Missing facts: draw verified subset and list unknown edges.
- Diagram becomes dense: split by question, not arbitrary file count.
- Spatial grouping matters more than exact flow: route to Excalidraw.
- Renderer lacks feature: use simpler supported syntax.

## Verify

- Mermaid syntax renders.
- Brackets and quotes balanced.
- Labels avoid unsupported Markdown.
- Direction and edge labels readable.
- Boundaries and external systems explicit.
- Diagram fits PR review without excessive detail.
- No secrets or private values present.

## Output

Return `.mmd` or embedded Mermaid block plus short assumptions/open-questions note when needed.
