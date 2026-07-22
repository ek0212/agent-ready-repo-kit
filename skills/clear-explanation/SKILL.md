---
name: clear-explanation
description: Explain complex ideas clearly for a specific audience using the CLEAR filter: Calibrate, Link, Envision, Abstract, Repeat. Use when user asks to "explain this clearly", "simplify this", "translate this for non-technical stakeholders", "make this easier to understand", "explain this to a beginner", or rewrite dense jargon into plain language.
license: MIT
---

# Clear Explanation

Turn complex ideas into audience-fit explanations. Use CLEAR: Calibrate, Link, Envision, Abstract, Repeat.

## Scope

Use for explanations, rewrites, teaching notes, stakeholder summaries, beginner-friendly descriptions, and jargon translation.

Do not use for narrative craft, academic literature synthesis, outreach email, newsletter strategy, or visual UI design unless explanation clarity is main job.

## Inputs

- Topic or draft.
- Audience and their familiarity.
- Desired channel: spoken, email, doc, slide, comment.
- Length limit, if any.
- Must-keep terms, facts, caveats, or legal/security constraints.

If audience missing, infer only when safe. Otherwise ask one calibration question.

## Workflow

### Step 1: Calibrate

Set audience level before explaining.

- Beginner: no jargon. Define needed terms.
- General professional: use common business/technical words.
- Specialist: keep field terms, remove needless complexity.
- Mixed audience: explain in layers, simple first, details after.

If interactive, ask: "How familiar are they with this topic?" If not interactive, state assumed level.

### Step 2: Link

Connect unknown to known.

Use one analogy, metaphor, or familiar comparison when it reduces effort. Keep link close to audience world. Drop analogy if it hides important differences.

Pattern:

```text
Think of [complex thing] like [known thing]. The important similarity: [shared structure]. The limit: [where analogy stops].
```

### Step 3: Envision

Make shape visible when words alone strain memory.

Use one simple model:

- 3-step flow.
- Before/after.
- Cause/effect chain.
- Small table.
- ASCII sketch.
- Named stages.

Skip visual model for short direct answers.

### Step 4: Abstract

Boil idea to simplest useful form.

- Replace jargon with plain words unless audience needs exact term.
- Cut acronyms or define once.
- Prefer concrete nouns and active verbs.
- Keep one idea per sentence.
- Keep caveats that change decisions.
- Remove detail that does not help audience act or understand.

Use this test: if listener could not repeat core idea after one hearing, simplify more.

### Step 5: Repeat

Close loop. Restate core idea in one line.

Use:

```text
In short: [one-sentence takeaway].
```

For longer explanations, end with what user should remember or do next.

## Output Shape

Default:

1. **Assumption:** audience level, if not supplied.
2. **Plain explanation:** short, direct explanation.
3. **Link:** analogy or comparison, if useful.
4. **Shape:** model, steps, table, or diagram, if useful.
5. **In short:** one-line takeaway.

For rewrite requests, return rewritten version first. Add short notes only when needed.

## Quality Checks

- Audience level named or known.
- No needless jargon.
- Jargon kept only when useful and defined once.
- Analogy helps and includes limit if risk of overreach.
- Structure visible for complex ideas.
- Core idea repeatable in one sentence.
- Accuracy preserved over simplicity.

## Writing

Use direct simple sentences. Skip rhetorical flourishes. Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.
