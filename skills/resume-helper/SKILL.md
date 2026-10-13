---
name: resume-helper
description: Audit, tailor, rewrite, and validate resumes against a target role using verifiable evidence, cross-version consistency, ATS-readable structure, quantified impact, and inspectable proof. Use for resume reviews, job-description matching, application sets, bullet rewrites, and PDF resume validation; do not trigger for standalone cover letters or interview coaching.
---

# Resume Helper

Build a resume that parses cleanly and remains credible under recruiter and interview scrutiny. Tailor emphasis to the role without changing facts.

## Choose the Mode

- **Resume plus job description:** model the role, map evidence, then produce or revise the resume.
- **Resume only:** audit evidence, readability, ordering, consistency, and unsupported claims. State that role-fit analysis needs a job description.
- **Job description plus rough notes:** build a fact bank before drafting.
- **Single bullet or section:** preserve surrounding voice, chronology, and claim scope.
- **Several applications for one candidate:** build a shared claim ledger before tailoring.
- **PDF or document:** inspect extracted text, rendered layout, and embedded links.

## Evidence Rules

- Never invent or silently strengthen metrics, dates, scope, tools, job titles, ownership, publications, outcomes, or AI use.
- Every keyword must map to work the candidate actually did and can explain naturally in an interview.
- Tailoring may change emphasis, ordering within a role, and vocabulary. It must not change team, dates, ownership, product identity, metric, time period, or public-proof status.
- Do not manufacture a missing qualification. Find overlooked evidence, label coursework or tutorials honestly, or state the gap.
- Match wording to public proof. An issue or proposal is not merged code, an acceptance is not a paper or talk, a preview is not adoption, and a service quota is not achieved performance.
- Distinguish personal contribution from team outcome. Use `led`, `owned`, or `built` only when supported.
- Protect private and proprietary information. Generalize customer details, security signals, and internal implementation details when needed.

## Workflow

### 1. Model the role

Extract:

- problems the employer needs this hire to solve;
- required and preferred qualifications;
- recurring responsibilities and outcomes;
- domain, scale, and seniority signals;
- truthful keywords;
- mapped candidate evidence and genuine gaps.

Prioritize evidence-backed fit over keyword coverage. Do not rewrite bullets before this brief exists.

### 2. Build a fact bank

For each relevant accomplishment, capture:

- result or change;
- candidate contribution;
- method or decision;
- scale and difficulty;
- dates and responsible team;
- metric definition and period;
- public-safe wording;
- proof URL or private source;
- relevance to the target role.

Separate verified facts, assumptions, missing evidence, and wording ideas.

### 3. Create a claim ledger for application sets

For every claim reused across resumes, record its canonical team, dates, ownership, description, approved metrics, time periods, and proof status. Treat these as invariants. Recruiters may see every version on one candidate profile.

Before finalizing, compare all variants for:

- changing customer or user counts;
- exact values versus conflicting ranges or rounded values;
- accomplishments moved between teams;
- one product framed as different products;
- different ownership verbs;
- inconsistent dates, titles, or years-of-experience calculations;
- links whose labels promise more than their destination proves.

### 4. Audit metrics

Choose numbers that prove business value, operating value, meaningful scale, difficulty, or trust. Remove decorative activity counts.

- State the period for money claims, such as monthly or annual.
- Prefer exact before-and-after values. Do not add a rounded percentage that conflicts with the arithmetic.
- Distinguish launch milestones from adoption or outcome metrics.
- Treat vendor quotas and provisioned capacity as context, not impact, unless the candidate improved or sustained them.
- Use one approved value everywhere.
- Never back-solve or invent a missing metric.

### 5. Select and rewrite evidence

Rank evidence by relevance, recency, strength, and distinctiveness. Lead each experience with the strongest role-relevant result.

Use a compact structure:

`Outcome + defensible measure or scale + action or method + useful context`

Keep each bullet focused on one outcome and at most one or two mechanisms. Cut noun chains. Replace soft verbs such as `helped`, `supported`, or `championed` with the precise action only when evidence supports it. A meaningful qualitative result may remain without a number.

Translate proprietary names and unexplained acronyms into language an outside recruiter can understand. Explain only enough technical detail to establish value and complexity.

### 6. Apply the role lens

- **PM:** product strategy, customer problem, prioritization, roadmap, requirements, success metrics, launch, adoption, and business outcome.
- **TPM:** program plan, dependencies, governance, risk retirement, launch readiness, operating cadence, technical trade-offs, and alignment.
- **SWE:** architecture, implementation, testing, reliability, observability, performance, security, and technical leadership.
- **Career bridge:** use one factual explanation when silence would create confusion. Keep reverse chronology and do not move work between teams. If experience totals include research, internships, or part-time work, make the calculation explainable.

### 7. Prove AI work

Show the problem, why AI was appropriate, what the candidate built or changed, how output quality was checked, and what improved. Prefer workplace evidence. Use personal projects only when they are original, inspectable, and labeled accurately.

Do not use a course exercise to satisfy production, enterprise, cloud, retrieval, or vector-database requirements. A public repository proves only what its code and history show.

### 8. Validate the artifact

For every final resume, verify:

- target fit is clear in the first scan;
- every claim and number traces to approved evidence;
- repeated claims match the application-set ledger;
- section order and chronology are honest;
- wording is concise and human;
- text extracts in sensible reading order;
- rendered pages have no clipping or unexpected wrapping;
- the candidate can defend every line aloud.

Validate links at three layers:

1. visible text clearly looks like a link;
2. the exported file contains the correct hyperlink annotation or relationship;
3. the destination resolves, while known anti-bot responses are reported accurately.

Use direct project, publication, credential, and press URLs when exact proof exists. Click-test every exported link. Email clients do not interpret Markdown link syntax, so use rich-text anchors or plain URLs for email copy.

## Output Contract

Lead with the highest-impact finding. For a full review, provide:

1. ATS and credibility verdict;
2. role brief with mapped evidence and real gaps;
3. critical changes before optional polish;
4. claim ledger when multiple applications are in scope;
5. metric audit separating verified numbers from missing evidence;
6. revised bullets or a clean final artifact, as requested;
7. artifact and link validation results.

Label assumptions and unverified claims. If the user asks for edits, produce the edited artifact when possible rather than stopping at advice.
