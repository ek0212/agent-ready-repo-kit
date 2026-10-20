---
name: presentation-builder
description: Build spoken presentations as PowerPoint decks through gated steps. Writes bullet-point speaker notes for a newcomer audience using the CLEAR framework, about one minute per slide, drafts a markdown file of headings, candidate visuals, and notes for the user to prune, then renders the final deck strictly in the user's template. Use when user says "make a presentation", "build a slide deck", "turn my talk into slides", "write speaker notes", "PowerPoint for my talk", or "apply my template to this deck".
license: MIT
---

Build a deck the user can speak to. Slides are visual backdrops. The script lives in speaker notes.

## Scope

Use for talks, pitches, lectures, and demos where a person presents live.

Do not use for text-heavy handouts or read-ahead decks, formatting one existing slide, spreadsheet charts, or documents. For a handout request, state that this skill keeps on-slide text minimal and ask before continuing.

## Inputs

Ask only for what is missing:

- What the user wants to say. Always ask first (Step 1).
- Talk length in minutes. Slide count equals minutes, at about one minute per slide.
- Source material: outline, doc, notes, data, or prior deck.
- Speaking pace if known. Default notes total 100 to 160 words per slide.
- Output folder. Default `deck/` next to the source material. Do not commit deck files unless asked.

Audience: assume newcomers with no background in the topic. Do not ask about familiarity. Change this only if the user explicitly names a more expert audience.

User owns the message, facts, visual picks, and template. Do not invent claims or data for notes.

## Rules For Every Slide

- Slide shows a heading of at most 8 words plus visuals. No sentences from the script on the slide.
- Visuals complement what the speaker says at that moment. They never repeat it as text.
- Speaker notes are bullet points, one spoken sentence each, about one minute per slide.
- Short labels on a chart or diagram are fine. Paragraphs are not.

## Workflow

Steps 1, 2, 5, and 6 are user gates. Stop and wait at each gate. Do not skip a gate unless the user explicitly delegates that decision.

### Step 1: Ask What They Want To Say

**Gate:** before writing anything, ask the user:

- What are the main points you want to make?
- What is the one thing the audience should remember?
- Which facts, numbers, stories, or examples must be included?

Wait for answers. Use only facts the user gives or source material confirms.

### Step 2: Script With CLEAR

Outline one slide per minute: proposed heading plus purpose. Then write speaker notes per slide as 5 to 8 bullets, 100 to 160 words total. Apply CLEAR (same framework as the `clear-explanation` skill) for a newcomer audience:

- **Calibrate:** audience has no clue about the topic. No jargon. Define each needed term once, in plain words, the first time it appears.
- **Link:** introduce each new concept with one everyday analogy. State where the analogy stops if it could mislead.
- **Envision:** give each slide one simple shape the listener can hold: 3-step flow, before/after, cause and effect, or named stages. Step 3 visuals should show this shape.
- **Abstract:** one idea per bullet. Concrete nouns, active verbs. Cut detail that does not help the audience understand or act. Keep caveats that change decisions. Test: could a newcomer repeat the slide's point after one hearing? If not, simplify.
- **Repeat:** the last slide ends with a bullet starting `In short:` that states the core idea in one sentence, followed by what to remember or do next.

Present heading and bullet notes per slide.

**Gate:** ask the user to approve or edit the script. Iterate until approved. Accuracy wins over simplicity.

### Step 3: Candidate Visuals

For each approved slide write exactly 5 candidate visuals.

- Max 2 sentences each.
- Describe what appears and what it signals. Example: `Single upward line on a blank grid, one dot labeled "today". Signals momentum without numbers.`
- At least one candidate shows the slide's Envision shape. Another can picture the Link analogy.
- Vary type across the 5: icon composition, diagram, chart, photo or illustration, metaphor.
- Each must support the notes without restating them.

### Step 4: Markdown Draft

Write `deck/draft.md` in this exact shape, one block per slide:

```markdown
# Talk Title

## Slide 1: Proposed heading

### Visuals
- Candidate visual 1, max 2 sentences.
- Candidate visual 2.
- Candidate visual 3.
- Candidate visual 4.
- Candidate visual 5.

### Speaker notes
- Approved note bullet, one spoken sentence.
- Next bullet.
```

Run from repo root:

```bash
uv run skills/presentation-builder/scripts/deck.py validate deck/draft.md
```

Fix every `FAIL` line and rerun. Review `WARN` notes-length lines with the user.

### Step 5: User Picks Visuals

**Gate:** send `deck/draft.md` and ask the user to delete every visual bullet they do not want, keeping their picks under each slide. Wait for the edited file.

Then run:

```bash
uv run skills/presentation-builder/scripts/deck.py selections deck/draft.md > deck/selections.json
```

If any slide reports `no visual selected`, ask the user for that slide. Do not pick for them.

### Step 6: Template

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

### Step 7: Render Final Deck

Load [render-guide.md](references/render-guide.md) now. Build `deck/final.pptx` from the template file, one slide per entry in `selections.json`, carrying approved notes unchanged.

## Verification

Run:

```bash
uv run skills/presentation-builder/scripts/deck.py check deck/final.pptx path/to/template.pptx --selections deck/selections.json
```

It must print `PASS`. It fails on non-template fonts, sizes, colors, or images, empty notes, and slide-count mismatch. Each approved outside asset will fail the image check; list those as approved exceptions.

Then render slide images and inspect each one for overflow, overlap, unreadable icons, low contrast, leftover template text, and empty placeholders. Confirm every slide's notes match the approved script.

## Fallbacks

- Notes only requested: run Steps 1 and 2, then stop.
- User declines a template: offer a plain deck with a white background, black text, the heading, the chosen visuals, and notes. Do not invent a style.
- User delegates visual picks: choose one per slide, give a one-line reason each, and write `selections.json` in the same shape.
- No `uv`: `pip install python-pptx` then `python skills/presentation-builder/scripts/deck.py ...`.
- No slide renderer: run `check`, then ask the user to open the deck and confirm layout.

## Output

At each gate return file paths and one direct question. At the end return `deck/final.pptx`, `check` result, slides reviewed visually, approved exceptions, and open issues.

## Writing

Use direct simple sentences. Skip rhetorical flourishes. Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.
