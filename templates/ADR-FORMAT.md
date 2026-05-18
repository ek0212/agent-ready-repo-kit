# ADR Format

ADRs live in `docs/adr/` and use sequential numbering:

```text
0001-short-slug.md
0002-another-decision.md
```

## Template

```markdown
# {Short Decision Title}

{One to three sentences: what was the context, what was decided, and why.}
```

Optional sections:

```markdown
## Status

accepted

## Considered Options

- Option A
- Option B

## Consequences

- Positive consequence.
- Trade-off or cost.
```

## Create An ADR Only When All Three Are True

- Hard to reverse: changing later has meaningful cost.
- Surprising without context: future readers would wonder why.
- Trade-off driven: there were real alternatives.

If the decision is obvious, easy to reverse, or purely tactical, skip the ADR.

