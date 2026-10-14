# Decisions

## 2026-10-14: presentation-builder ships a helper script

- **Decision:** `skills/presentation-builder` includes `scripts/deck.py` (python-pptx, run via `uv run`) for draft build, selection readback, template inspection, and final-deck compliance checks.
- **Context:** The workflow needs a fixed draft format and a strict "template only" rule for fonts, sizes, colors, and icons. Prose instructions alone cannot verify those.
- **Alternatives considered:** Instructions only, with the agent writing python-pptx code each time. Rejected because drafts would vary between runs and template compliance would rest on model judgment.
- **Status:** ACTIVE
