---
name: grill-the-architecture
description: Stress-tests architecture language, boundaries, and trade-offs, then writes diagrams or ADRs only when useful. Use when planning or documenting system design.
---

# Grill The Architecture

## Use When

- The user has a plan but the boundaries are fuzzy.
- A repo needs an architecture diagram.
- A decision may deserve an ADR.
- Different parts of the codebase use conflicting patterns.

## Workflow

1. Read existing architecture docs, diagrams, ADRs, and relevant code.
2. Ask one question at a time for unresolved design choices.
3. Challenge vague terms:
   - "service"
   - "agent"
   - "workflow"
   - "user"
   - "session"
   - "source of truth"
4. Stress-test with concrete scenarios.
5. Cross-check user claims against code.
6. Create or update diagrams when flow or boundaries matter.
7. Offer ADRs sparingly.

## ADR Test

Create an ADR only when all three are true:

- The decision is hard to reverse.
- It is surprising without context.
- It involved a real trade-off.

## Diagram Choices

- Use Mermaid for architecture, sequence, state, and data-flow diagrams.
- Use Excalidraw for fuzzy product or system sketches.
- Pair every Excalidraw sketch with a short Markdown summary.

## Output

End with:

- resolved decisions
- remaining ambiguities
- diagrams created or suggested
- ADRs created or skipped, with reason

