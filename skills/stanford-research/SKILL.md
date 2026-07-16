---
name: stanford-research
description: Analyze academic papers as rigorous literature synthesis across claims, contradictions, citation chains, gaps, methods, assumptions, knowledge maps, and practical meaning. Use when user says "stanford research", requests literature synthesis, paper intake, contradiction finder, gap scan, methodology audit, assumption audit, knowledge map, or plain-language "so what" summary.
license: MIT
---

Synthesize paper set into evidence, disputes, methods, gaps, assumptions, and meaning. Trace every claim.

## Scope

Use supplied papers only unless user authorizes outside research. Named subtask runs only that module. `stanford research` or full protocol runs all modules. Do not use for narrative essay drafting or single-paper copyedit.

## Inputs

- Full paper text or readable files.
- Research question and intended audience.
- Citation style and output depth.
- Permission boundary for outside sources.

Authors own claims. User owns paper set and research question. Mark unavailable text, missing metadata, inference, and unresolved ambiguity.

## Workflow

### Step 1: Intake

For each paper capture author, year, research question, method, data, core claim, and stated limits. Write thesis in 20 words or fewer; label inference when abstract/conclusion lacks explicit thesis.

Cluster papers by shared question, framework, method, or assumption. Name basis. Flag candidate contradictions.

### Step 2: Test Contradictions

Keep only mutually incompatible claims about same issue. Exclude differences caused only by scope, emphasis, wording, population, or outcome definition.

For each contradiction state positions, papers, evidence, and root cause: method, dataset, period, definition, population, or unresolved cause.

### Step 3: Trace Concepts

For recurring concepts, map origin within supplied set, challenge, refinement, and current status: settled in set, contested, evolving, or unsupported. Do not claim historical origin beyond available corpus.

### Step 4: Find Gaps

Separate:

- Author-acknowledged gap.
- Gap implied by method or data.
- Analyst-proposed gap.

For each, name closest paper, shortfall, why gap matters, and method/data needed. Rank by stated criterion: theoretical impact, practical impact, or feasibility.

### Step 5: Audit Methods

Compare design, data source, sample, measures, identification strategy, controls, reproducibility, and author-stated limits. Use method labels that fit papers; do not force preset taxonomy.

Name strongest and weakest evidence for specific claim, not globally strongest or weakest paper. Explain criterion.

### Step 6: Synthesize

Organize by claim, not paper:

1. Consensus supported by at least two papers when available.
2. Active debates and reason for disagreement.
3. Strongest evidence and why it is stronger.
4. Open question whose answer most changes field.

Use calibrated language. `Proves` requires design that supports causal certainty. Distinguish absence of evidence from evidence of absence.

### Step 7: Audit Assumptions

Find consequential assumptions shared by multiple papers but not tested or justified. For each, state relying papers, risk if false, and affected conclusions. Rank by consequence, not novelty.

### Step 8: Build Knowledge Map

Return outline:

- Central claim or competing centers.
- Three to five supporting pillars with papers.
- Two or three contested zones when present.
- One or two frontier questions.
- Three-paper newcomer path selected for foundation and sequence, not citation count.

### Step 9: Explain Meaning

For non-expert summary, answer:

1. Best-supported finding.
2. Largest unresolved question.
3. Why it matters in practice or theory.

Use plain language. Keep uncertainty. No jargon or unsupported certainty.

## Fallbacks

- Missing full text: limit claims to available sections and say so.
- Small set: report all supported contradictions/gaps; do not pad counts.
- Incomparable papers: split by population, method, or outcome before synthesis.
- Outside research not authorized: stop at supplied corpus.

## Verify

- Every substantive claim traces to paper.
- Direct quote and paraphrase distinguished.
- Contradictions compare same construct and scope.
- Gaps labeled by source type.
- Method judgments cite criteria.
- Certainty matches design and evidence.
- Missing evidence and corpus limits explicit.

## Output

Return requested module or full protocol. Use compact comparison tables only where they improve cross-paper mapping. Include citations and corpus-limit note.
