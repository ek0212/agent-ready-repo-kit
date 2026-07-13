---
name: stanford-research
description: Analyze academic or research papers as rigorous literature synthesis. Use when user says "stanford research", asks for research protocol, literature synthesis, paper intake, contradiction finder, citation chain, gap scanner, methodology audit, assumption killer, knowledge map, or "so what" summary across uploaded papers.
license: MIT
---

# Stanford Research

Synthesize uploaded papers into claims, disputes, methods, gaps, assumptions, meaning. Use only uploaded papers unless user authorizes outside sources.

## Workflow

### Step 1: Intake Protocol

Before substance, map set.

1. Table every paper: author(s), year, core claim, thesis in 20 words or fewer. If thesis absent, infer from conclusions.
2. Group into 2-5 clusters by shared assumptions/frameworks. Name cluster. Explain basis in 1-2 sentences.
3. Flag direct contradictions as `Paper A vs. Paper B: contested claim`.

Do not summarize paper-by-paper. Focus table, clusters, contradictions.

### Step 2: Contradiction Finder

Find genuine mutually exclusive claims about same issue. Exclude emphasis, scope, framing, terminology differences.

Table columns:

- Contested claim
- Position A, paper and year
- Position B, paper and year
- Root cause of disagreement

Root cause: methodology, dataset, time period, term definition, or other. Explain other. Aim 5-10 contradictions. If fewer, list all.

### Step 3: Citation Chain

Find 3 recurring/debated/built-upon concepts.

For each:

- Concept name
- Origin: first introduction/definition in set
- Challenge: papers questioning it and how
- Refinement: papers modifying/extending it and how
- Current status: settled, contested, evolving

Use structured outline. If no challenge/refinement, state it.

### Step 4: Gap Scanner

Find 5 major gaps papers acknowledge, imply, or miss.

For each:

- **Gap:** unanswered question in 1-2 sentences. Cause: methodology barrier, missing data, niche topic, assumed but untested, ethical/logistical constraint.
- **Closest paper:** closest paper plus shortfall.
- **Path to resolution:** method, data, resources, or other need.

Rank most to least significant. State criterion: theory, practical impact, feasibility, or other. If fewer than 5, list all and explain limit.

### Step 5: Methodology Audit

Compare methods.

First table:

- Paper, author and year
- Methodology type
- Data source
- Sample size, if stated
- Key limitation noted by authors

Use best-fit type. Add categories as needed. Suggested: survey, experiment, randomized controlled trial, quasi-experiment, simulation, meta-analysis, case study, computational or machine learning, literature review, ethnography, secondary data analysis.

Then synthesize:

- Most common method type?
- Why, from stated rationale?
- Relevant method absent/rare?

Finally name methodologically weakest paper. Evaluate sample size, confounds, replicability, reporting transparency. State clearest failed criterion.

### Step 6: Master Synthesis

Use uploaded papers only. Synthesize across literature. Do not summarize individual papers.

Structure:

1. Established consensus, about 100 words. Field agreement. Cite at least 2 papers per claim.
2. Active debates, about 100 words. Meaningful disagreement. Name positions, not individual papers.
3. Strongest evidence, about 100 words. Most consistent, replicated, robust claims.
4. Key open question, about 80 words. Unanswered question whose resolution most changes field.

Max 400 words. No hedging like "it seems" or "some argue." If evidence cannot fill section, say so.

### Step 7: Assumption Killer

Find 5-8 consequential assumptions shared by most papers but not tested, justified, or named.

Focus:

- Foundational to conclusions.
- Plausibly false or context-dependent.

For each:

- **Assumption:** declarative claim, e.g. `X causes Y under all conditions`.
- **Shared by:** 2-3 papers relying on it most.
- **Risk level:** low, medium, high, based on damage if false.
- **Consequence:** what changes.

Rank most to least consequential.

### Step 8: Knowledge Map Builder

Clean outline only. No prose paragraphs.

Use:

- Central claim: single proposition field supports/challenges/refines. If none, name 2 competing centers.
- Supporting pillars, 3-5: `[Claim] supported by [paper 1], [paper 2]`.
- Contested zones, 2-3: `[Issue]: [Position A] vs. [Position B]`.
- Frontier questions, 1-2: explicit unanswered questions.
- Newcomer reading list, 3 papers: `[Author, year]`, why read first.

Select for foundational value, not citation count.

### Step 9: "So What" Test

Explain literature to smart non-expert in exactly 3 numbered points. Each point 2-3 sentences max.

1. What has been proven: strongest reliable finding. Direct claim, no hedging. Do not use "suggests" or "may indicate."
2. What remains unknown: biggest unresolved thing, honest.
3. Why it matters: key real-world implication. If none, biggest theoretical consequence.

Rules: no jargon, no citations, no weak qualifications. If confidence unjustified, say so. Do not fabricate certainty.

## Output Rules

- Full Stanford research protocol runs all steps.
- Named subtask runs only named step, e.g. "contradiction finder" or "so what test."
- Use tables where required, outlines where required, short prose only where required.
- Every claim traceable to uploaded papers. Mark uncertainty/missing evidence.
