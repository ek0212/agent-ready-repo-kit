---
name: stanford-research
description: Analyze a set of academic or research papers as a rigorous literature synthesis. Use when the user says "stanford research", asks for a research protocol, literature synthesis, paper intake, contradiction finder, citation chain, gap scanner, methodology audit, assumption killer, knowledge map, or "so what" summary across multiple uploaded papers.
license: MIT
---

# Stanford Research

Use this skill to synthesize a body of uploaded research papers into claims, disagreements, methods, gaps, assumptions, and practical meaning. Use only the uploaded papers unless the user explicitly authorizes outside sources.

## Workflow

### Step 1: Intake Protocol

Before answering substantive questions, build the map of the paper set.

1. List every paper in a table with columns: author(s), year, core claim, and one-sentence thesis of 20 words or fewer. If a paper has no explicit thesis, infer the central argument from its conclusions.
2. Group the papers into 2-5 clusters based on shared theoretical assumptions or frameworks. Name each cluster and explain in 1-2 sentences what unites the papers in it.
3. Flag direct contradictions where two or more authors make mutually exclusive claims about the same phenomenon. Format each as: `Paper A vs. Paper B: contested claim`.

Do not summarize each paper individually. Focus on the table, clusters, and contradictions.

### Step 2: Contradiction Finder

Across all uploaded papers, identify the most significant genuine contradictions. Include only mutually exclusive claims about the same issue. Exclude differences that are only emphasis, scope, framing, or terminology.

Present findings as a table with columns:

- Contested claim
- Position A, paper and year
- Position B, paper and year
- Root cause of disagreement

For root cause, choose from methodology, dataset, time period, definition of terms, or other. If using other, explain it. Aim for 5-10 contradictions. If fewer exist, list all genuine contradictions found.

### Step 3: Citation Chain

Identify the 3 concepts that appear most frequently across multiple papers, referenced by name, debated, or built upon.

For each concept, trace its intellectual history using only evidence in the uploaded papers:

- Concept name
- Origin: who first introduced or defined it within this set
- Challenge: which paper or papers questioned or challenged it, and how
- Refinement: which paper or papers modified or extended it, and how
- Current status: settled, contested, or still evolving based on this literature

Present each concept as a structured outline. If a concept lacks a clear challenge or refinement in these papers, state that explicitly rather than guessing.

### Step 4: Gap Scanner

Identify the 5 most significant research gaps the papers collectively acknowledge, imply, or fail to address.

For each gap:

- Gap: state the unanswered question in 1-2 sentences. Explain why it exists. Choose from methodological barrier, lack of data, topic too niche, assumed but untested, or ethical/logistical constraint. Explain briefly.
- Closest paper: name the uploaded paper that came closest to addressing it and where it fell short.
- Path to resolution: state what would be needed to close the gap, such as methodology, data, resources, or other requirements.

Rank the 5 gaps from most to least significant, and briefly explain the ranking criterion, such as theoretical importance, practical impact, or feasibility of resolution. If fewer than 5 genuine gaps exist, list all identified gaps and explain why the set is limited.

### Step 5: Methodology Audit

Compare the research methodologies used across all uploaded papers.

First, create a classification table with columns:

- Paper, author and year
- Methodology type
- Data source
- Sample size, if stated
- Key limitation noted by the authors

Use the methodology type that best fits each paper. Do not force papers into preset categories. Add new categories as needed. Suggested types include survey, experiment, randomized controlled trial, quasi-experiment, simulation, meta-analysis, case study, computational or machine learning, literature review, ethnography, and secondary data analysis.

Then synthesize:

- Which methodology type appears most frequently?
- Why, based on the papers' stated rationale?
- Which methodology is absent or rare despite being relevant to the research questions?

Finally, identify the paper whose methodology is most vulnerable to criticism. Evaluate it using sample size adequacy, control for confounds, replicability, and transparency of reporting. State which criterion it fails most clearly.

### Step 6: Master Synthesis

Using the uploaded papers as the only source, write a synthesis of the body of literature. Do not summarize individual papers. Write across the entire literature.

Use this structure:

1. Established consensus, around 100 words: what does this field collectively agree on? Cite at least 2 papers that support each claim made here.
2. Active debates, around 100 words: what do researchers in this field meaningfully disagree about? Name the disagreeing positions without naming individual papers.
3. Strongest evidence, around 100 words: what claims are supported by the most consistent, replicated, or methodologically robust evidence?
4. The key open question, around 80 words: end with the single most important unanswered question in this field, the one whose resolution would most change the others.

Total length is 400 words maximum. Do not use hedging phrases like "it seems" or "some argue." State clearly. If the papers lack sufficient consensus to populate a section, say so explicitly.

### Step 7: Assumption Killer

Identify the 5-8 most consequential assumptions that the majority of the papers share but never explicitly test, justify, or acknowledge as assumptions.

Focus on assumptions that are:

- Foundational to the conclusions drawn
- Plausibly false or context-dependent

For each assumption:

- Assumption: state it as a declarative claim, such as `X causes Y under all conditions`.
- Shared by: name 2-3 papers that rely on it most heavily.
- Risk level: rate it low, medium, or high based on how much of the literature would be undermined if the assumption is false.
- Consequence: explain what would change, such as conclusions needing revision, key findings becoming invalidated, or the research paradigm collapsing.

Rank assumptions from most to least consequential.

### Step 8: Knowledge Map Builder

Create a structured knowledge map of the literature. Present it as a clean outline with no prose paragraphs.

Use this structure:

- Central claim: the single proposition that most of the field's work tries to support, challenge, or refine. If no single claim unifies the field, name 2 competing centers instead.
- Supporting pillars, 3-5: well-established subclaims with strong evidentiary support across multiple papers. For each: `[Claim] supported by [paper 1], [paper 2]`.
- Contested zones, 2-3: areas of genuine active disagreement. For each: `[Issue]: [Position A] vs. [Position B]`.
- Frontier questions, 1-2: questions this literature raises but cannot yet answer. State them as explicit questions.
- Newcomer reading list, 3 papers: for each paper, state `[Author, year]`, why a newcomer should read it first.

Selection criterion: foundational to understanding the field, not just most cited.

### Step 9: The "So What" Test

Summarize the entire body of research for a smart non-expert who has never read any of it. Respond in exactly 3 numbered points. Each point should be 2-3 sentences maximum.

Write as if speaking to an intelligent person with no domain knowledge.

1. What has been proven: the strongest, most reliable finding from this literature. State it as a direct claim with no hedging. Do not use "suggests" or "may indicate."
2. What is still unknown: the most significant thing this field has not yet figured out, stated honestly without minimizing the uncertainty.
3. Why it matters: the single most important real-world implication. If no direct application exists, state the biggest theoretical consequence instead.

Rules: no jargon, no citations, and no qualifications that weaken the core point. If a statement cannot be made confidently based on the papers, say so. Do not fabricate certainty.

## Output Rules

- Default to running all steps when the user asks for the full Stanford research protocol.
- Run only the requested step when the user asks for a named subtask, such as "contradiction finder" or "so what test."
- Use tables where requested, concise outlines where requested, and short prose only where requested.
- Keep every claim traceable to uploaded papers. Mark uncertain or missing evidence explicitly.
