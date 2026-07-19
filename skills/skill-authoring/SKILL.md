---
name: skill-authoring
description: Create, revise, split, route, validate, or evaluate agent skills using Agent Skills format. Use when user says "create a skill", "build a skill", "write a SKILL.md", "split this skill", "convert this to a skill", "test this skill", "benchmark a skill", or asks whether guidance belongs in AGENTS.md vs a skill.
license: MIT
---

Create focused skill from human-verified workflow. Test behavior against no-skill baseline.

## Scope

Use for reusable procedures with multiple steps and judgment. Put one stable rule in `AGENTS.md`. Keep volatile project state in source docs/config. Do not create skill for one-off task or declarative facts.

## Inputs

- Human-owned workflow, examples, constraints, and success criteria.
- Trigger phrases and negative triggers.
- Required inputs, outputs, tools, and target surfaces.
- Applicability boundary and lighter fallback.
- Existing skill inventory and repo placement rules.

Agent may scaffold, organize, compress, and test. Human owns domain truth. [SkillsBench](https://arxiv.org/abs/2602.12670) found self-generated packs below no-skill baselines in tested setups; discovery and creator/solver interference also contributed. Treat result as warning against unreviewed generated procedure, not ban on agent help.

## Workflow

### Step 1: Confirm Need

Create skill when workflow repeats, requires judgment, contains reusable traps, or should load only for relevant task. Reject when one rule, source link, or ordinary code/doc solves need.

### Step 2: Bound Skill

Write before body:

- Name: lowercase kebab-case job.
- Trigger: user language and file/domain cues.
- Negative trigger: nearest task that should not load it.
- Inputs: facts and artifacts required.
- Outputs: files or response produced.
- Scope: included and excluded work.
- Applicability: evidence that justifies full path.
- Fallback: cheaper or simpler path.

Default one focused skill. Split only when each module has separate trigger or load gate. [SkillsBench](https://arxiv.org/abs/2602.12670) found focused packs with at most three modules beat larger or exhaustive bundles. Benchmark evidence, not hard cap.

### Step 3: Write Frontmatter

Required:

```yaml
---
name: kebab-case-name
description: What skill does. Use when user says "trigger phrase" or asks for named job.
---
```

This repo validator also accepts `license`, `allowed-tools`, and `metadata`. Other runtimes may allow more. Check target validator.

Rules:

- Folder name matches `name`.
- Name uses lowercase letters, numbers, hyphens.
- Description under 1024 characters.
- Description says what and when, in third person.
- Include obvious and paraphrased triggers.
- No XML angle brackets.
- No `claude` or `anthropic` in name.

### Step 4: Write Body

Use concrete verbs and decision criteria. Include only context agent cannot safely infer.

Preferred shape:

1. Job statement.
2. Scope and inputs.
3. Ordered workflow.
4. Applicability and fallbacks.
5. Verification.
6. Output contract.

Match freedom to risk. Exact command for fragile path. Bounded heuristic when several approaches work. Heavy pipeline needs applicability boundary and lightweight fallback.

Write Full mode: short precise words, fragments allowed, no filler, tool narration, decorative tables, emoji, long raw logs, or invented abbreviations. Preserve exact terms, code, commands, paths, identifiers, and errors.

### Step 5: Use Progressive Disclosure

Loading order:

1. Frontmatter always.
2. `SKILL.md` when triggered.
3. Linked files on demand.

Keep `SKILL.md` under 200 lines in this repo. Move bulk material:

```text
skill-name/
  SKILL.md
  scripts/
  references/
  assets/
  evals/
```

Link support files with load criteria. No `README.md` inside skill folder. Avoid deep reference chains.

### Step 6: Static Validate

Check frontmatter, folder/name match, trigger precision, negative triggers, concrete steps, human review, stale facts, support links, applicability, fallback, and target surfaces.

Run repo validator:

```bash
uv run --with pyyaml python "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/<skill-name>
```

### Step 7: Paired Evaluate

Follow [Anthropic authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#evaluation-and-iteration):

1. Create at least three representative tasks, one should-not-trigger task, one boundary case.
2. Freeze inputs, model, harness, tools, attempt count, and scoring rubric.
3. Run no-skill baseline in clean context.
4. Run candidate skill under same conditions.
5. Score task success, discovery, constraint violations, tokens/tools, and time when available.
6. Inspect failures. Polished output is not task success.
7. Keep helpful instructions. Revise or remove neutral/harmful guidance.

For multi-skill tasks, test relevant subset. Do not load full library by default. [Generative Skill Composition](https://arxiv.org/abs/2606.32025) found selected sets beat full-library injection with lower prompt-token cost in tested setup.

Use deterministic verifier when practical. For containerized benchmark work, use [SkillsBench harness](https://github.com/benchflow-ai/skillsbench). Store cases, rubric, commands, and results under `evals/`. Use `evals/paired-run-template.md` when repo has no stronger harness.

### Step 8: Place And Register

This repo uses `skills/<skill-name>/SKILL.md`. Add skill to repo catalogs when new. Preserve unrelated edits.

## Output

- New or revised `SKILL.md`.
- Support files needed by workflow.
- Eval cases and result summary when run.
- Catalog updates for new skill.
- Static validation result and unmeasured limits.
- Paired-run report path before claiming efficacy.
