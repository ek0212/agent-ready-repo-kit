# Agent Hygiene

Agent context should make good behavior easier without turning into a stale encyclopedia.

## Durable Context

Good agent instructions describe:

- how to verify changes
- what conventions to follow
- what mistakes to avoid
- what boundaries require confirmation
- what domain terms mean
- where to put new decisions

## Rot-Prone Context

Avoid:

- current file inventories
- temporary implementation status
- lists of active bugs
- recent roadmap items
- exact package versions unless compatibility depends on them
- generated summaries of code that can be rediscovered cheaply

## The Main Rule

If a fact changes more often than the repo's conventions, do not put it in `AGENTS.md`.

## Better Alternatives

| Volatile Thing | Better Home |
|---|---|
| current TODO | issue tracker or project board |
| exact implementation status | code |
| domain term | dedicated glossary doc in the target repo, if needed |
| hard architectural decision | ADR |
| flow or boundary | diagram |
| repeated agent mistake | `AGENTS.md` |
| verification command | `AGENTS.md` |

## Good Instruction Shape

```text
When doing X, follow existing Y pattern and verify with Z.
```

## Bad Instruction Shape

```text
The current implementation has files A, B, C, D, and E, and file C currently does most of the work.
```

That may be true today. It will become fossil dust tomorrow.
