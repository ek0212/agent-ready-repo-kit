# Paired Evaluation: Technical Writing

- **Skill:** `technical-writing`
- **Date:** 2026-10-26
- **Repository revision:** `9b0be22aa0b44104afe449f4b565c40a12bb9796` plus uncommitted candidate files
- **Model:** Runtime default for both runs; exact routed model was not exposed
- **Harness:** Two clean read-only `explore` agent runs
- **Tools:** Baseline used none; candidate used local reads for `SKILL.md` and linked references
- **Attempts:** One per condition
- **Source inputs:** `evals/cases.yaml` and the user-provided *Handbook for Mindful Technical Writing*, 2026 edition

## Fixed Conditions

Both runs received the same five cases:

1. API signing-key rotation runbook with system details withheld.
2. Incident report with source evidence withheld.
3. Executive migration recommendation with source report withheld.
4. OAuth explanation-only negative case.
5. Sensor proposal boundary case with major planning facts withheld.

The baseline prompt prohibited loading skill files and requested general model behavior. The candidate prompt loaded only `skills/technical-writing/SKILL.md` and references that file explicitly directed it to use. Both prompts required trigger decisions, compact usable drafts, explicit missing facts, no follow-up questions, and no invented data.

## Fixed Rubric

Score each dimension from 0 to 2:

- **Task success:** Produces a useful response for each requested job.
- **Discovery:** Applies the skill to in-scope cases and rejects the negative case.
- **Constraint compliance:** Follows output and non-invention requirements.
- **Evidence handling:** Separates known facts, reported statements, assumptions, and gaps.
- **Usability:** Gives a reader-centered structure that supports action or decision.
- **Efficiency:** Avoids irrelevant process and excessive output.

## Scores

| Condition | Task success | Discovery | Constraint compliance | Evidence handling | Usability | Efficiency | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| No-skill baseline | 2 | 1 | 2 | 2 | 2 | 2 | 11/12 |
| Candidate skill | 2 | 2 | 2 | 2 | 2 | 2 | 12/12 |

## Failure Notes

The baseline marked the incident report and executive recommendation cases as outside a general technical-writing procedure, even though it still produced reasonable draft structures. This routing error would reduce skill discovery and could send users to an undefined or less suitable workflow.

The candidate recognized all four technical-document cases, rejected the explanation-only case, preserved missing-data placeholders, and applied genre-specific evidence and verification rules.

Neither condition invented source findings, commands, costs, dates, or incident facts.

## Decision

**Keep.** The candidate improved trigger routing without reducing constraint compliance, evidence handling, usability, or efficiency. No revision was required from this paired run.

## Unmeasured Limits

- The exact routed model, token use, and elapsed generation time were not exposed.
- The cases used withheld inputs to test non-invention and structure. They did not test factual synthesis from a complete source packet.
- The evaluation did not render a designed document or test a procedure with a representative end user.
- This result supports the tested cases only. It is not a general efficacy claim.
