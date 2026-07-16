---
name: excalidraw-system-sketch
description: Plan or create Excalidraw sketches for fuzzy architecture, product flows, trust boundaries, before-and-after designs, or system maps. Use when user asks for an Excalidraw diagram, rough system sketch, spatial grouping, swimlanes, or visual exploration that Mermaid cannot express well.
license: MIT
---

Create one readable spatial sketch plus durable Markdown summary.

## Scope

Use when placement, grouping, swimlanes, or exploration matters. Use Mermaid for exact sequence, state, dependency, or GitHub-rendered architecture.

## Inputs

- Diagram purpose and audience.
- Components, actors, systems, and flows.
- Trust boundaries, secrets, user data, and external services.
- Existing `.excalidraw` file or visual conventions, if any.

User or repository owns system facts. Mark inferred nodes and unresolved flows.

## Workflow

1. State one diagram question.
2. List boxes, groups, arrows, boundaries, and annotations.
3. Choose layout: left-to-right flow, swimlanes, nested zones, or before/after.
4. Separate internal, external, trusted, and untrusted areas.
5. Label secret and user-data entry points without including secret values.
6. Create or update `.excalidraw` when compatible tooling exists.
7. Write companion `.md` summary with purpose, components, boundaries, flows, and open questions.

## Drawing Rules

- One concept per sketch.
- Short labels. Verb-led arrows.
- Color encodes one stable meaning or stays decorative-free.
- Boundaries visible without color alone.
- Avoid file-level detail unless diagram question requires it.
- Keep uncertain elements labeled `Assumption` or `Open`.

## Fallbacks

- No Excalidraw tooling: return exact sketch plan and companion Markdown. State visual file not created.
- Flow already precise: route to `mermaid-architecture-map`.
- Missing system facts: create partial sketch with open questions; do not invent architecture.

## Verify

- Diagram answers stated question.
- Main flow readable without zoom.
- Trust boundaries and external systems explicit.
- No secrets or private data embedded.
- Companion summary matches visual.
- Open questions named.

## Output

- `.excalidraw` file when tooling permits.
- Companion `.md` summary always.
- Assumptions and unresolved items.
