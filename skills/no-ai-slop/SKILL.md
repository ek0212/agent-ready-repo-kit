---
name: no-ai-slop
description: Edit existing drafts into sharper human writing while preserving writer voice, or detect AI-slop patterns without rewriting. Use when user asks to make writing clearer, more direct, more opinionated, less AI-sounding, more human, or asks whether a draft reads like AI.
license: MIT
---

Edit existing drafts with minimum effective change. Report visible AI-writing patterns without guessing authorship.

## Scope

Use for existing drafts: posts, essays, explanations, emails, docs, captions, and sections. Use `creative-writing` when user needs narrative structure, scenes, title options, or longform craft. Use `outreach-email` for outcome-driven one-to-one email drafting. Use `newsletter-growth` for recurring newsletter strategy. Use `clear-explanation` when main job is making a complex idea easier to understand.

Do not use for first drafts from notes, fiction, research synthesis, product UI copy, or factual verification unless user also wants an AI-pattern edit.

## Inputs

- Draft text.
- Audience and publication surface.
- Desired reader action or feeling.
- Constraints: length, voice, formality, terms, claims, examples to keep.

If draft missing, ask user to paste it. If audience or surface unclear, ask one question. If goal unclear and edit would change meaning, ask what reader should think, feel, or do.

## Jobs

### Edit

Default when user asks to fix, sharpen, humanize, de-AI, make less AI-sounding, or improve an existing draft.

Return edited draft and short **What changed** section. Use minimum effective edit. Preserve real voice: vocabulary, cadence, bluntness, humor, uncertainty, digressions, roughness, and level of polish.

### Detect

Use when user asks whether writing is AI slop, AI-sounding, generic, robotic, or asks to audit, scan, or flag without rewriting.

Return pattern findings. For each: pattern name, short quote, and fix direction. Do not rewrite, score, or guess whether AI wrote it. Offer edit only after report.

## Workflow

1. Read full draft.
2. Identify core point and 3-5 voice signals to preserve. Keep note internal.
3. If core point is unclear, ask before editing.
4. For detect request, report findings and stop.
5. For edit request, cut AI patterns, repetition, errors, tangled passages, and unsupported puffery.
6. Leave strong human lines alone even if imperfect.
7. Run quality checks. Revise once more if checks fail.
8. Output full edited draft plus **What changed**.

## Editing Rules

- Preserve user's meaning. Do not invent claims, examples, stats, opinions, quotes, or sources.
- Keep useful edge: strong opinions, blunt language, humor, profanity, self-interruptions, and honest admissions when they belong.
- Lead with point when setup adds nothing. Keep personal aside, story, or admission when it adds context, tension, or character.
- Front-load only when clarity improves. Do not force every paragraph into same shape.
- Open it up; do not dumb it down. Keep nuance and precision while removing jargon, tangled structure, and abstract filler.
- Use active voice. Do not let inanimate things do human verbs.
- Make verbs work. Replace weak verb phrases with direct verbs.
- Make each sentence earn place. Cut empty qualifiers and throat-clearing. Keep `I think`, `maybe`, or `to be honest` when they carry real uncertainty or spoken rhythm.
- Untangle sentences without flattening cadence. Split hard sentences. Keep longer spoken sentences, fragments, and pace shifts when clear.
- Protect specific facts. Do not smooth useful detail into generic importance.
- Keep structure unless it hurts piece. If you reorganize, say why in **What changed**.
- Use concrete nouns, names, numbers, dates, mechanisms, and examples when supplied.
- Repeat clear word when right. Do not rotate synonyms for style.
- Remove formatting decoration: emoji headings, random bold, tiny over-headered sections, and bullet lists that should be prose.
- Avoid em dashes as default rhythm. In short copy, use none. In long drafts, keep only when clearer than comma, period, or parenthesis.

## Cut List

Banned when used as generic polish: `delve`, `foster`, `leverage`, `utilize`, `facilitate`, `empower`, `streamline`, `robust`, `cutting-edge`, `paradigm shift`, `game changer`, `this is huge`, `this changes everything`, `tapestry`, `realm`, `beacon`, `multifaceted`, `meticulous`, `intricate`, `paramount`, `transformative`, `elevate`, `embark`, `supercharge`, `harness`, `ever-evolving`.

Usually cut when empty: `just`, `literally`, `honestly`, `simply`, `actually`, `truly`, `fundamentally`, `importantly`, `crucially`, `inherently`, `inevitably`.

Usually cut when delaying point: `it is worth noting`, `it is important to note`, `at the end of the day`, `when it comes to`, `at its core`, `in today's world`, `in the age of`, `in the world of`, `the reality is`, `the truth is`, `in terms of`, `with regard to`, `in order to`, `going forward`, `in this article`, `let's dive in`.

Keep any listed word or phrase only when it carries real meaning, contrast, uncertainty, or recognizable voice.

## Pattern Checks

- Binary contrast: `not X, but Y`, `not just X`. State main claim directly.
- Throat clearing: `Here's the thing`, `Let me be clear`, `I'll be honest`. Cut and state point.
- Faux insight: `what most people miss`, `what nobody tells you`. Make claim stand alone.
- Colon reveal: dramatic noun phrase plus colon. Rewrite as plain sentence. Keep colons for labels, lists, quotes, and code.
- Superficial analysis: trailing `highlighting`, `underscoring`, `reflecting`, `showcasing`. Replace with mechanism or cut.
- Importance puffery: `stands as a testament`, `marks a pivotal moment`, `plays a vital role`, `solidifies its position`. State fact.
- Weasel attribution: `experts agree`, `industry reports suggest`, `many argue`, `widely regarded`, `studies show`. Name source or cut/flag.
- Fake-strong verbs: `serves as`, `acts as`, `stands as`. Prefer `is`, `has`, or concrete verb.
- Negative listing: `Not a X. Not a Y. A Z.` Say Z.
- Dramatic fragments: stacked punch fragments or `That's it. That's the whole thing.` Use complete sentence.
- Robotic rhythm: repeated sentence shapes, same paragraph template, stacked punchy fragments. Vary only when useful.
- Rhetorical setup: `What if I told you`, `Think about it`, `Plot twist`, or self-answered question. Drop setup.
- Fake-profound kicker: final cute metaphor, aphorism, or mic-drop line. End on clearest concrete point or next action.
- Recap ending: `In conclusion`, `Ultimately`, `Overall`, or final summary. End on concrete point, takeaway, or next action.

## Quality Checks

- Core point clear.
- Meaning, facts, and voice preserved.
- Minimum effective changes made.
- AI patterns removed or named.
- Specific details kept.
- No invented claims, examples, stats, opinions, quotes, or sources.
- Rhythm human and varied.
- Output matches requested job: edit or detect.
- Any assumptions or source gaps stated.

## Output

For edit: edited draft first, then **What changed** with 3-5 bullets. For detect: findings by pattern with quote and fix direction. State questions only when answer is needed before safe edit.
