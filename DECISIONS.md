# Decisions

## 2026-10-14: presentation-builder ships a helper script

- **Decision:** `skills/presentation-builder` includes `scripts/deck.py` (python-pptx, run via `uv run`) for draft validation, selection readback, template inspection, and final-deck compliance checks.
- **Context:** The workflow needs a fixed draft format and a strict "template only" rule for fonts, sizes, colors, and icons. Prose instructions alone cannot verify those.
- **Alternatives considered:** Instructions only, with the agent writing python-pptx code each time. Rejected because drafts would vary between runs and template compliance would rest on model judgment.
- **Status:** ACTIVE

## 2026-10-14: presentation-builder draft is markdown

- **Decision:** The candidate-visuals draft is `deck/draft.md` (heading, 5 visual bullets, speaker notes per slide). The user deletes unwanted bullets, and `deck.py selections` reads the pruned file.
- **Context:** User asked for the headers, candidate visuals, and speaker notes as markdown.
- **Alternatives considered:** Black-and-white draft `.pptx` built by `deck.py draft`, pruned in PowerPoint. BACKTRACKED by user request. Producing both formats was also rejected to keep one editable source.
- **Status:** ACTIVE

## 2026-10-20: presentation-builder scripts use CLEAR bullets for newcomers

- **Decision:** Script writing starts by asking what the user wants to say. Notes are bullet points built with CLEAR (Calibrate, Link, Envision, Abstract, Repeat), assuming the audience has no background. `deck.py validate` requires bullet notes and an `In short:` bullet on the last slide.
- **Context:** User asked for bullet-point scripts using the `clear-explanation` framework and a no-background audience.
- **Alternatives considered:** Prose notes (previous behavior), rejected by user request. Asking for audience familiarity each time, rejected because the user set newcomers as the default.
- **Status:** ACTIVE

## 2026-10-20: presentation-builder notes are talking points with bold key terms

- **Decision:** Speaker notes are 5 to 8 talking points per slide, max 12 words each, phrase form, with key terms bolded as `**term**`. `deck.py validate` fails long points and warns on sentence-style points, point counts outside 5 to 8, and slides with no bold term. Replaces the 100 to 160 word, one-sentence-per-bullet rule.
- **Context:** User asked for points to cover instead of full sentences, with key terms bolded.
- **Alternatives considered:** Full-sentence bullets (previous rule), rejected by user request.
- **Status:** ACTIVE
