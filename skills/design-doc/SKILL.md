---
name: design-doc
description: Write compact software design docs, architecture plans, alternatives analyses, API surfaces, rollout plans, and testing plans before multi-module work.
---

# Design Doc

## Use When

- A change touches multiple modules, services, teams, or data stores.
- There are meaningful architectural alternatives.
- The work needs an API contract, migration plan, rollout plan, or risk review.
- The user asks for a design doc, tech spec, architecture plan, or implementation plan.

Skip the doc for small, self-contained changes.

## Procedure

1. Identify the audience and decision the doc must support.
2. Inspect the current code, commands, docs, and integration points before proposing architecture.
3. Define the smallest version users would actually want, not only the smallest version that runs.
4. Compare at least one alternative unless the user explicitly wants a lightweight plan.
5. Include verification before implementation: tests, manual checks, rollout gates, and observability.
6. Keep unresolved decisions in Open Questions, not hidden in prose.

## Template

```markdown
# <Feature Or Project>

## Background

## Problem

## Goals

## Non-Goals

## Proposed Design

## Architecture

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Chosen: <name> |  |  |

## API Or Data Surface

## Rollout And Migration

## Testing And Verification

## Risks

## Open Questions
```

## Diagram Guidance

Use a Mermaid diagram when prose hides ownership, data flow, or system boundaries. Use `mermaid-architecture-map` for the diagram itself if available.

## Output

Return the design doc, then list assumptions that need confirmation.
