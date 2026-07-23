# Skills

Each folder has one standalone `SKILL.md` and `evals/cases.yaml`.

## Available Skills

| Skill | Use when |
|---|---|
| `skill-authoring` | Create, split, or route skills. |
| `figma-to-ui` | Implement an exact Figma selection and refine it through browser comparison. |
| `frontend-design` | Build web UI where design quality matters. |
| `clear-explanation` | Explain complex ideas clearly for a specific audience. |
| `no-ai-slop` | Edit drafts to sound sharper and more human, or detect AI-slop patterns. |
| `newsletter-growth` | Plan/audit newsletters for growth, engagement, monetization. |
| `outreach-email` | Draft concise one-to-one emails and value-adding follow-up sequences. |
| `mermaid-architecture-map` | Need GitHub diagrams or explicit boundaries. |
| `excalidraw-system-sketch` | Need grouping, swimlanes, rough visual thinking. |
| `creative-writing` | Draft/edit nonfiction with narrative craft. |
| `dataset-triage` | Check tabular data before analysis/modeling. |
| `stanford-research` | Synthesize research papers. |

## Loading Rules

- Default zero skills.
- Load at most one skill per pass unless task spans domains.
- Prefer code/docs over more instructions.
- Write skill prose in [Full mode](../AGENTS.md#full-mode).
- Each skill output must use direct simple sentences and avoid banned AI writing patterns from [Writing](../AGENTS.md#writing).

## Evaluation

- Three representative cases.
- One should-not-trigger case.
- One boundary case.
- Paired no-skill and candidate-skill runs required before efficacy claim.
