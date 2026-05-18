# CONTEXT.md Format

`CONTEXT.md` is a glossary and relationship map. It is not a spec, scratchpad, file map, or implementation summary.

## Template

```markdown
# {Context Name}

One or two sentences describing what this context is and why it exists.

## Language

**Canonical Term**: One-sentence definition of what it is.
_Avoid_: ambiguous synonym, overloaded word

**Another Term**: One-sentence definition.
_Avoid_: weaker alias

## Relationships

- A **Canonical Term** belongs to exactly one **Another Term**.
- A **Thing** can produce zero or more **Events**.

## Example Dialogue

> **Developer:** "When a **Thing** changes, do we create an **Event**?"
> **Domain expert:** "Only when the change crosses a user-visible boundary."

## Flagged Ambiguities

- "account" was used to mean both **User** and **Organization**. Resolution: use **User** for login identity and **Organization** for billing/workspace ownership.
```

## Rules

- Define project-specific language only.
- Keep definitions to one sentence.
- Pick canonical terms and list aliases to avoid.
- Flag conflicts explicitly.
- Show relationships when cardinality or ownership matters.
- Create `CONTEXT.md` lazily, only when a real term is resolved.

