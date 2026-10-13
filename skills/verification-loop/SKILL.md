---
name: verification-loop
description: Build repeatable verification loops from recurring manual checks. Use when user says "make this a verification loop", "turn this check into a skill", "add verification to a skill", "chain skills", "wrap this workflow with verify", or asks for reusable pre-commit, post-change, or PR checks.
license: MIT
---

Build a loop that catches the same miss before humans repeat the same review.

## Scope

Use for recurring checks around code, docs, design, security, accessibility, logging, public APIs, screenshots, tests, or release gates.

Do not use for one-off test runs, generic QA, or implementing the product change itself unless user asks to encode reusable verification.

## Inputs

- Manual follow-up user repeats.
- Artifact to inspect: diff, file, route, screenshot, log, API, doc, or PR.
- Trigger conditions.
- Pass, fail, and warning criteria.
- Fix authority: report only, patch automatically, or ask.
- Existing skill or workflow to embed or wrap.
- Cost, latency, false-positive tolerance, and team visibility.

User owns standard. Mark judgment calls, missing evidence, and unstable gates.

## Workflow

### Step 1: Pick Check

Choose check only when it is repeatable and observable.

Good checks have:

- Clear trigger.
- Inspectable evidence.
- Small result surface.
- Known failure mode.
- Specific fix or escalation.

Reject vague checks such as `make quality better`. Convert them into checklist or rubric first.

### Step 2: Choose Run Mode

Pick one mode:

- **Standalone:** cross-cutting or occasional check invoked on demand. Use for security scans, accessibility audits, license headers, docs drift, or checks not tied to one producer.
- **Embedded:** check belongs to one producing skill you control. Add verification step to that `SKILL.md`.
- **Chained:** several handoffs always run together, or original skill cannot be edited. Create wrapper that invokes producer, then verifier.
- **PR gate:** stable loop runs on every PR. Use only after low false-positive rate, clear owner, team buy-in, and documented bypass path.

Promote from standalone to embedded or chained only after user repeatedly runs same follow-up. Promote to PR gate only after chain is stable.

### Step 3: Write Contract

Define:

1. Trigger: exact user language, file path, diff type, or workflow state.
2. Scope: what files, artifacts, or states are checked.
3. Evidence: commands, screenshots, source reads, static checks, or tests.
4. Pass criteria: required facts.
5. Fail criteria: violations and severity.
6. Fix policy: patch, stage comment, report, or ask.
7. Report shape: file:line, artifact, evidence, fix, and limits.
8. Stop rule: when to fail fast or escalate.

Prefer deterministic commands over model judgment. Use rubric only where deterministic verifier is not practical.

### Step 4: Implement

For standalone skill:

- Create focused `SKILL.md`.
- Add trigger-rich frontmatter.
- Keep tool permissions minimal when runtime supports `allowed-tools`.
- Add representative, negative, and boundary eval cases.

For embedded check:

- Edit producing skill you control.
- Add one clear verification step near end of workflow.
- Add check to producing skill verification list.
- Add or update eval case proving embedded check runs.

For chained loop:

- Create wrapper skill.
- State order, handoff artifact, failure stop rule, and final report shape.
- Keep each called skill independently useful unless chain is always required.

For PR gate:

- Reuse same rubric and commands from standalone or chain.
- Define owner, signal, bypass, false-positive handling, and rollout stage.
- Start as advisory before blocking.

### Step 5: Verify Loop

Run on fresh task or fixed fixture.

Confirm:

- Trigger loads correct skill.
- Check actually runs.
- Passing case stays quiet.
- Failing case is caught.
- Fix or report follows policy.
- Output names evidence and limits.

If loop does not run, tighten description or workflow. If loop overfires, narrow trigger or scope.

### Step 6: Control Cost

Each loop adds tokens, time, and possible noise. Keep expensive checks standalone until value is proven. Batch related checks only when they inspect same artifact and fail under same owner.

## Fallbacks

- Vague standard: produce checklist and ask for pass/fail criteria.
- Producer skill cannot be edited: create wrapper chain.
- No deterministic verifier: write evidence rubric and mark judgment.
- High false-positive risk: keep standalone and advisory.
- Team-wide gate requested too early: return staged rollout plan.

## Verify

- Check is repeatable, not one-off.
- Mode matches trigger frequency and ownership.
- Contract has trigger, evidence, criteria, fix policy, and stop rule.
- Eval cases include representative, negative, and boundary tasks.
- No PR-wide blocking before loop stabilizes.
- No efficacy claim without paired runs.

## Writing

Use direct simple sentences. Skip rhetorical flourishes. Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.

## Output

Return loop design or repo change. Include mode, trigger, contract, files changed, eval cases, verification result, promotion path, and limits.
