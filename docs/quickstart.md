# Quickstart

Use this process to make an existing repo agent-ready.

## 1. Pick A Template

Choose the closest template:

- `templates/AGENTS.base.md`
- `templates/AGENTS.web-app.md`
- `templates/AGENTS.python-cli.md`
- `templates/AGENTS.chrome-extension.md`
- `templates/AGENTS.vscode-extension.md`
- `templates/AGENTS.mcp-enabled.md`

Copy it into the target repo as `AGENTS.md`.

## 2. Grill The Repo

Use `skills/grill-the-repo` to fill only the durable parts:

- stable constraints
- commands
- conventions
- mistakes to avoid
- ask-before-changing boundaries

Do not add exhaustive file maps or temporary feature status.

## 3. Add Context Only If Needed

Create `CONTEXT.md` only when the repo has domain language that agents keep misunderstanding.

Use `templates/CONTEXT-FORMAT.md`.

## 4. Add Diagrams When Shape Matters

Use Mermaid for clean technical diagrams:

```text
docs/diagrams/architecture.mmd
docs/diagrams/data-flow.mmd
docs/diagrams/mcp-boundaries.mmd
```

Use Excalidraw for rough system sketches and pair it with a Markdown summary.

## 5. Add ADRs Sparingly

Use `templates/ADR-FORMAT.md`.

Create ADRs only for decisions that are:

- hard to reverse
- surprising without context
- trade-off driven

## 6. Audit Readiness

Run `skills/repo-readiness-audit` and fix the top three issues.

## Done Means

- agents know how to install, run, test, and build
- risky boundaries are explicit
- docs are short and durable
- diagrams show important flows
- volatile details are left out

