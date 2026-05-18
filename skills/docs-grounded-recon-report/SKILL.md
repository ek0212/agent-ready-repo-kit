---
name: docs-grounded-recon-report
description: Produces a self-contained report with receipts from docs, code, and examples. Use for repo audits, research summaries, project handoffs, or agent-readable reports.
---

# Docs-Grounded Recon Report

## Inspiration

This follows the useful pattern from dataset-scout: produce a report that ties claims back to evidence, not a vibes-only summary.

## Use When

- A user wants a repo audit.
- A project needs a handoff report.
- A plan needs evidence from code and docs.
- A report should be readable by humans and reusable by agents.

## Workflow

1. Gather sources: README, docs, package files, tests, key modules, existing diagrams.
2. Extract claims only when they can be tied to evidence.
3. Group findings by strategy or theme.
4. Call out coverage gaps as first-class output.
5. Produce Markdown by default.
6. Offer HTML when comparison, inspection, or presentation benefits from layout.

## Report Shape

```markdown
# Recon Report

## Executive Summary

## Evidence Table

| Claim | Evidence | Confidence |
|---|---|---|

## Findings

## Coverage Gaps

## Recommended Next Actions

## Sources
```

## Rules

- Every non-obvious claim needs a source.
- Do not pretend missing evidence is evidence.
- Separate facts from inferences.
- Preserve uncertainty.

