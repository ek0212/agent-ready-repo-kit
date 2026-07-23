# Agent-Ready Repo Kit

Small rule and skill kit for coding agents in real repos.

Copy `AGENTS.md` and the `skills/` you need into the target repo.

## Writing Contract

All repo-authored prose follows [Full mode](AGENTS.md#full-mode), now and in future edits:

- Drop articles when meaning stays clear. Fragments OK. Use short precise words.
- No tool-call narration, decorative tables, emoji, or long raw error-log dumps unless asked.
- Standard acronyms OK. No invented abbreviations.
- Preserve exact technical terms, code, commands, paths, identifiers, and error text.

## What This Contains

- One self-contained [`AGENTS.md`](AGENTS.md): rules, procedures, path-scoped rules.
- Focused skills and eval cases in [`skills/`](skills/).

## Quick Start

1. Copy [`AGENTS.md`](AGENTS.md) into the target repo root.
2. Copy [`skills/`](skills/) into the target repo. Remove skills you do not need.
3. Keep project facts in the target repo, not this kit.

## Structure

```text
AGENTS.md                           # Rules, procedures, path rules
skills/
  skill-authoring/SKILL.md          # Create or split skills
  figma-to-ui/SKILL.md              # Figma-to-code implementation
  frontend-design/SKILL.md          # Distinctive web UI
  clear-explanation/SKILL.md        # Plain-language explanation
  no-ai-slop/SKILL.md               # Human-voice draft editing
  newsletter-growth/SKILL.md        # Newsletter strategy
  outreach-email/SKILL.md           # Concise one-to-one email
  mermaid-architecture-map/SKILL.md # GitHub-renderable diagrams
  excalidraw-system-sketch/SKILL.md # Freeform system sketches
  creative-writing/SKILL.md         # Narrative nonfiction
  dataset-triage/SKILL.md           # Tabular data sanity checks
  stanford-research/SKILL.md        # Literature synthesis
  */evals/cases.yaml                # Trigger and behavior cases
```

## AGENTS.md

[`AGENTS.md`](AGENTS.md) is the entrypoint. It contains:

- **Rules:** coding, safety, security, writing, static text, structure, model choice, agent communication.
- **Procedures:** coding, writing, static text hygiene, secrets/env review.
- **Path rules:** Python, Chrome Extension, VS Code Extension, Web App.

## Skills

| Skill | Use when |
|---|---|
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | Create, split, or route skills. |
| [`figma-to-ui`](skills/figma-to-ui/SKILL.md) | Implement an exact Figma selection and verify visual match. |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Build web UI where design quality matters. |
| [`clear-explanation`](skills/clear-explanation/SKILL.md) | Explain complex ideas clearly for a specific audience. |
| [`no-ai-slop`](skills/no-ai-slop/SKILL.md) | Edit drafts to sound sharper and more human, or detect AI-slop patterns. |
| [`newsletter-growth`](skills/newsletter-growth/SKILL.md) | Plan or audit newsletter growth strategy. |
| [`outreach-email`](skills/outreach-email/SKILL.md) | Draft concise one-to-one email and follow-up sequences. |
| [`mermaid-architecture-map`](skills/mermaid-architecture-map/SKILL.md) | Need GitHub-renderable diagrams or explicit boundaries. |
| [`excalidraw-system-sketch`](skills/excalidraw-system-sketch/SKILL.md) | Need grouping, swimlanes, or rough visual thinking. |
| [`creative-writing`](skills/creative-writing/SKILL.md) | Draft or edit nonfiction with narrative craft. |
| [`dataset-triage`](skills/dataset-triage/SKILL.md) | Check tabular data before analysis or modeling. |
| [`stanford-research`](skills/stanford-research/SKILL.md) | Synthesize research papers. |

### Skill Loading Rules

- Default to zero skills.
- Load at most one skill per pass unless the task spans domains.
- Prefer reading code and docs over loading more instructions.

### Skill Evaluation

Each skill includes five cases: three representative tasks, one should-not-trigger task, one boundary case. Cases define expected behavior. They do not prove skill improves outcomes.

Measure efficacy with paired runs: same task, model, harness, tools, attempts, and rubric; one run without skill, one with candidate skill. See [`skill-authoring`](skills/skill-authoring/SKILL.md#step-7-paired-evaluate).

## Extend

1. Add `skills/your-skill/SKILL.md`.
2. Add catalog rows in this file and `skills/README.md`.
3. Add path-scoped rules directly to `AGENTS.md`.
4. Keep `AGENTS.md` and every `SKILL.md` under 200 lines.
