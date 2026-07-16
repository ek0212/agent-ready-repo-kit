---
name: dataset-triage
description: Run read-only first-pass checks on tabular data before analysis, joins, reports, or modeling. Use when user asks "what is in this dataset", "is this data clean", "what should I check first", or provides an unfamiliar CSV, TSV, Excel sheet, SQL/KQL result, or pandas DataFrame.
license: MIT
---

Find mechanical data risks before downstream work. Report evidence. Do not mutate source data.

## Scope

Use for row-and-column data. Skip images, free text corpora, audio, and unstructured documents. Triage detects shape, parsing, missingness, duplicates, key, cardinality, range, and format risks. It does not prove domain correctness.

## Inputs

- Source path, query, table, or DataFrame.
- Expected grain and row meaning, when known.
- Expected keys, date range, units, and critical fields.
- Safe sample limits and access constraints.

Human owner confirms business rules, valid ranges, units, and key meaning.

## Workflow

### Step 1: Acquire Safely

Use existing loader and dependencies. Record source, sheet/query, row filter, sample method, and load errors.

- File: inspect extension, delimiter, encoding, sheet, header, and totals rows.
- SQL/KQL: start with bounded recent window when timestamp exists. Avoid full-table pull.
- In-memory frame: preserve original object; inspect copy when conversion needed.

If sample lacks enough rows or classes, widen deliberately. Never claim sample represents full table without evidence.

### Step 2: Pin Structure

Report row count, column count, column names, dtypes, first rows, last rows, and index shape. Flag:

- Empty dataset.
- Duplicate or blank column names.
- Header or totals row parsed as data.
- Numbers or dates stored as text.
- Shifted or malformed rows.

### Step 3: Run Core Checks

For pandas, adapt this compact baseline:

```python
n = len(df)
if n == 0:
    raise ValueError("dataset has no rows")

missing = df.isna().mean().sort_values(ascending=False)
duplicate_rows = int(df.duplicated().sum())
unique = df.nunique(dropna=False)
constant = unique[unique <= 1].index.tolist()
candidate_keys = [
    c for c in df.columns
    if df[c].notna().all() and df[c].nunique(dropna=False) == n
]
```

Then inspect:

- Missingness by column. Highlight fully empty and critical fields.
- Exact duplicates. Test domain-key duplicates separately when key known.
- Constant and near-constant columns. Treat 99% dominance as review threshold, not error.
- Candidate keys. Names such as `id`, `key`, or `uuid` are clues, not proof.
- Categorical cardinality and top values.
- Numeric min, max, quantiles, impossible signs, and unit mismatch.
- IQR outlier candidates. Do not label outliers as bad data without domain evidence.
- Whitespace, casing, sentinel strings, mixed formats, and numeric text.
- Date parse success, timezone consistency, gaps, and future dates when relevant.

### Step 4: Check Sample Limits

Run cheap full-table checks when access permits: row count, date span, missingness on critical fields, and key uniqueness. Keep heavy scans bounded. State checks omitted due cost or permissions.

### Step 5: Report

Group findings:

- **Blocker:** breaks grain, join, count, parse, or required field.
- **Cleanup:** formatting or low-information issue with known fix.
- **Review:** plausible anomaly needing domain owner.
- **Limit:** sample, access, parser, or untested assumption.

For each finding, give evidence, downstream effect, and next check. Do not clean data unless user asks in separate step.

## Fallbacks

- No pandas: use existing SQL/KQL/file tools and report equivalent checks.
- Large source: sample recent window plus cheap aggregate checks.
- Unknown grain: report candidate grains; do not assert key.
- Parse failure: stop, preserve error, propose loader change.

## Verify

- Source unchanged.
- Sample method explicit.
- Empty data handled.
- Findings separate evidence from domain judgment.
- Candidate keys tested, not guessed.
- Report states omitted checks and limits.

## Output

Return compact triage report plus commands or code used. Include blockers, cleanups, reviews, limits, and recommended next checks.
