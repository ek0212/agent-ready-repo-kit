# Repo Before And After

This example shows the intended transformation.

## Before

```text
README.md exists.
No AGENTS.md.
No test commands documented.
Architecture lives in the maintainer's head.
Agent keeps adding duplicate utilities.
```

## After

```text
AGENTS.md lists stable commands, conventions, and mistakes to avoid.
CONTEXT.md defines overloaded domain terms.
docs/diagrams/architecture.mmd shows system boundaries.
docs/adr/0001-keep-client-side-processing.md explains a privacy decision.
```

## Why It Matters

The agent no longer has to guess:

- how to verify work
- whether to reuse existing utilities
- which secrets must stay server-side
- why a privacy-sensitive architecture exists

