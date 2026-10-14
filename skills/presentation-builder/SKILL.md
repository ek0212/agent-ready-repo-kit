---
name: presentation-builder
description: Build spoken presentations as PowerPoint decks through gated steps. Writes one-minute speaker notes per slide, drafts a black-and-white deck of candidate visuals for the user to prune, then renders the final deck strictly in the user's template. Use when user says "make a presentation", "build a slide deck", "turn my talk into slides", "write speaker notes", "PowerPoint for my talk", or "apply my template to this deck".
license: MIT
---

Build a deck the user can speak to. Slides are visual backdrops. The script lives in speaker notes.

## Scope

Use for talks, pitches, lectures, and demos where a person presents live.

Do not use for text-heavy handouts or read-ahead decks, formatting one existing slide, spreadsheet charts, or documents. For a handout request, state that this skill keeps on-slide text minimal and ask before continuing.

## Inputs

Ask only for what is missing:

- Topic, audience, and the one thing they should remember.
- Talk length in minutes. Slide count equals minutes, at about one minute per slide.
- Source material: outline, doc, notes, data, or prior deck.
- Speaking pace if known. Default notes target 100 to 160 words per slide.
- Output folder. Default `deck/` next to the source material. Do not commit deck files unless asked.

User owns the message, facts, visual picks, and template. Do not invent claims or data for notes.

## Rules For Every Slide

- Slide shows a heading of at most 8 words plus visuals. No sentences from the script on the slide.
- Visuals complement what the speaker says at that moment. They never repeat it as text.
- Speaker notes are written to be spoken aloud, about one minute each.
- Short labels on a chart or diagram are fine. Paragraphs are not.

## Workflow

Steps 1, 4, and 5 are user gates. Stop and wait at each gate. Do not skip a gate unless the user explicitly delegates that decision.

### Step 1: Script

1. Outline one slide per minute: proposed heading plus purpose.
2. Write speaker notes per slide, 100 to 160 words, in the user's voice.
3. Present heading and notes per slide.
4. **Gate:** ask the user to approve or edit the script. Iterate until approved.

### Step 2: Candidate Visuals

For each approved slide write exactly 5 candidate visuals.

- Max 2 sentences each.
- Describe what appears and what it signals. Example: `Single upward line on a blank grid, one dot labeled "today". Signals momentum without numbers.`
- Vary type across the 5: icon composition, diagram, chart, photo or illustration, metaphor.
- Each must support the notes without restating them.

### Step 3: Black-And-White Draft Deck

Write `deck/spec.json`:

```json
{"slides": [{"heading": "...", "visuals": ["...", "...", "...", "...", "..."], "notes": "..."}]}
```

Run from repo root:

```bash
uv run skills/presentation-builder/scripts/deck.py draft deck/spec.json deck/draft.pptx
```

Draft has white background, black Arial text, heading as header, 5 candidate visuals as body bullets, and the approved notes under each slide. Fix every `FAIL` line and rerun. Review `WARN` notes-length lines with the user.

### Step 4: User Picks Visuals

**Gate:** send `deck/draft.pptx` and ask the user to open it and delete every visual they do not want, keeping their picks on each slide. Wait for the edited file.

Then run:

```bash
uv run skills/presentation-builder/scripts/deck.py selections deck/draft.pptx > deck/selections.json
```

If any slide reports `no visual selected`, ask the user for that slide. Do not pick for them.

### Step 5: Template

**Gate:** ask for the template file they want used. Require `.pptx`. For `.potx`, Keynote, or Google Slides, ask for a `.pptx` export.

Run:

```bash
uv run skills/presentation-builder/scripts/deck.py inspect path/to/template.pptx > deck/template.json
```

Summarize for the user: theme fonts, allowed sizes, color palette, layouts, and icon inventory.

Strict template rules:

- Template icons are the core visual source. Build each selected visual from them first.
- Use only template colors. Prefer theme color references.
- Use only template fonts and font sizes. Let placeholders inherit where possible.
- Use template layouts and their placeholder grid.
- Native shapes and charts are allowed when styled only with template colors, fonts, and sizes.
- If a selected visual cannot be built this way, ask the user: swap the visual, simplify it, or approve an outside asset by name.

### Step 6: Render Final Deck

Load [render-guide.md](references/render-guide.md) now. Build `deck/final.pptx` from the template file, one slide per entry in `selections.json`, carrying approved notes unchanged.

## Verification

Run:

```bash
uv run skills/presentation-builder/scripts/deck.py check deck/final.pptx path/to/template.pptx --selections deck/selections.json
```

It must print `PASS`. It fails on non-template fonts, sizes, colors, or images, empty notes, and slide-count mismatch. Each approved outside asset will fail the image check; list those as approved exceptions.

Then render slide images and inspect each one for overflow, overlap, unreadable icons, low contrast, leftover template text, and empty placeholders. Confirm every slide's notes match the approved script.

## Fallbacks

- Notes only requested: run Step 1 and stop.
- User declines a template: offer to render picks in the draft black-and-white style. Do not invent a style.
- User delegates visual picks: choose one per slide, give a one-line reason each, and write `selections.json` in the same shape.
- No `uv`: `pip install python-pptx` then `python skills/presentation-builder/scripts/deck.py ...`.
- No slide renderer: run `check`, then ask the user to open the deck and confirm layout.

## Output

At each gate return file paths and one direct question. At the end return `deck/final.pptx`, `check` result, slides reviewed visually, approved exceptions, and open issues.

## Writing

Use direct simple sentences. Skip rhetorical flourishes. Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.
