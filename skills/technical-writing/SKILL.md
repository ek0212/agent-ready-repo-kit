---
name: technical-writing
description: Draft, revise, structure, and verify reader-centered technical documents that help people act, decide, understand a process, or use a system. Use when user asks for technical writing, documentation, instructions, SOPs, runbooks, manuals, technical descriptions or definitions, incident or progress reports, project proposals, recommendation reports, executive summaries, plain-language summaries, or technical workplace correspondence.
license: CC-BY-NC-SA-4.0
---

# Technical Writing

Create technical documents that are clear, coherent, concise, concrete, correct, complete, and courteous.

## Scope

Use for task-oriented or decision-oriented documents, including software and engineering documentation, instructions, SOPs, runbooks, manuals, technical descriptions, definitions, reports, proposals, summaries, memos, and technical email.

Do not use for:

- Explanation-only requests with no document deliverable. Use `clear-explanation`.
- Narrative articles, profiles, or essays. Use `creative-writing`.
- Literature reviews or research synthesis. Use `stanford-research`.
- AI-pattern cleanup when structure and technical usability are already sound. Use `no-ai-slop`.
- Spoken presentation decks. Use `presentation-builder`.

## Inputs

- Audience, expertise, needs, and likely objections.
- Purpose and action or decision the document must support.
- Document type, channel, length, template, and style requirements.
- Verified facts, evidence, source material, terminology, and constraints.
- Safety, legal, privacy, accessibility, or operational requirements.
- Existing draft and required sections, when revising.

Ask one focused question only when a missing fact changes safety, scope, document type, or the required outcome. Otherwise state a narrow assumption.

## Workflow

### Step 1: Frame The Rhetorical Situation

Write a private one-line brief:

```text
For [audience], this [document type] will help them [task or decision] in [context], using [required evidence or constraints].
```

Identify:

- What readers already know.
- What they need before they can act.
- What success looks like after reading.
- Which terms need definition.
- Which concerns, risks, or resistance need coverage.

### Step 2: Choose The Document Pattern

Select the smallest document type that fits the purpose. Follow an existing template or required specification before a generic pattern.

Load [references/document-types.md](references/document-types.md) when the request names a genre or the structure is uncertain.

### Step 3: Map The Information

Before drafting, order the material around reader use:

1. Main point, task, recommendation, or expected outcome.
2. Context and prerequisites.
3. Steps, parts, evidence, or findings.
4. Risks, limits, alternatives, and troubleshooting.
5. Next action or decision.

Separate verified facts, interpretations, assumptions, and unknowns. Do not invent missing specifications, results, quotes, incidents, costs, or citations.

### Step 4: Draft For Reader Action

- Put the main message where readers need it, usually early.
- Give each paragraph one central idea and a clear topic sentence.
- Use active voice when the actor matters.
- Use direct commands for procedures.
- Keep one primary action per numbered step.
- Use parallel wording for headings, steps, and list items.
- Prefer concrete nouns, precise verbs, measured quantities, and defined conditions.
- Define necessary jargon on first use. Keep established terms for specialist readers.
- Use purposeful repetition when consistency matters more than variety.
- Keep tone professional, respectful, inclusive, and proportionate to the evidence.
- Qualify claims when evidence is limited. Avoid unsupported certainty.

For persuasive documents, connect each claim to a reason and credible evidence. Address material counterarguments fairly.

### Step 5: Integrate Evidence

- Cite quoted, paraphrased, summarized, and adapted material.
- Explain how each source or data point supports the surrounding claim.
- Check evidence for accuracy, sufficiency, relevance, completeness, currency, and authority.
- Preserve exact wording only when quotation is necessary.
- Use facts and observations only in incident reports. Label unresolved information.

### Step 6: Design For Navigation

- Use descriptive headings that expose the document structure.
- Use numbered lists for sequence or priority. Use bullets for unordered items.
- Use tables for exact values or comparison. Use figures for patterns, processes, or spatial relationships.
- Introduce each visual in the text, place it near the relevant passage, and add an informative label, caption, source, and accessible text alternative.
- Apply contrast, alignment, repetition, proximity, and size consistently.
- Keep related elements together and preserve enough white space for scanning.
- Never rely on color alone to convey meaning.

### Step 7: Verify Through The Reader's Task

Run the checks that fit the document:

- Can the named audience find the main point quickly?
- Can a reader complete the task or make the decision without hidden prerequisites?
- Are steps complete, ordered, testable, and safe?
- Are warnings placed before the related hazard and repeated at the relevant step?
- Are claims supported and limitations visible?
- Are headings, lists, tables, figures, labels, units, and terms consistent?
- Are source uses cited and traceable?
- Does every section serve the stated purpose?
- Is the document free of ambiguity, bias, avoidable jargon, grammar errors, and formatting drift?

For instructions, simulate the procedure or have a representative user test it when practical. Record observed failure points and revise.

## Applicability And Fallbacks

Use the full workflow for new, multi-section, high-stakes, safety-relevant, or evidence-heavy documents.

For a short low-risk edit, preserve the existing structure and run Steps 1, 4, and 7 only.

If evidence or requirements are incomplete, produce a labeled outline, questions, or placeholders. Do not turn assumptions into facts.

If a mandated template, regulator, publisher, or organization standard conflicts with this skill, follow the authoritative specification and note the conflict.

## Output

Return the requested document first.

Then include only what the user needs to finish it:

- Assumptions.
- Evidence or source gaps.
- Required verification or user testing.
- Alternate structure only when it materially changes usability.

## Source

This skill adapts a human-authored technical writing handbook. Read [references/source-and-license.md](references/source-and-license.md) for attribution and license terms.

