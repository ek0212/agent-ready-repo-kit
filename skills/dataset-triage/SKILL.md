---
name: dataset-triage
description: Run a quick, standard first-pass set of sanity checks on any tabular dataset before relying on it for analysis, joins, reporting, or modeling. Works whether the data arrives as a file (CSV, TSV, Excel), a SQL table, a Kusto/KQL table, or an in-memory pandas DataFrame. Covers row and column counts, dtypes, missing-value rates, duplicate rows, constant and near-constant columns, candidate keys, categorical cardinality, numeric range and outlier flags, and basic format issues. Use when the user receives, loads, queries, or asks "what's in this dataset", "is this data clean", "what should I check first", or points at a table or query result before using it. Trigger even when the user does not say "triage" but is clearly about to start working with an unfamiliar dataset.
---

# Dataset Triage

A fast, standard first look at a tabular dataset, regardless of how it is accessed. The point is to catch the problems that quietly break downstream work, wrong dtypes, hidden missingness, duplicate rows, junk columns, broken keys, before any time goes into analysis, joins, dashboards, or models.

This is a triage pass, not a deep analysis. It answers "can I trust this data and what do I need to fix first". The pass reports only; it never changes the data.

## When to use

Use this whenever an unfamiliar dataset shows up and the user is about to work with it: a file on disk, a SQL table, a Kusto/KQL table, or a pandas DataFrame already in memory. It applies regardless of what comes next.

Do NOT use for image, text, or audio data, or for anything that is not row-and-column tabular.

## Step 1: Get the data into a DataFrame

Pick the loader for how the data is accessed. The remaining steps are identical once the data is a DataFrame.

File (CSV, TSV, Excel):
```python
import pandas as pd
df = pd.read_csv(path)            # or sep="\t" for .tsv
df = pd.read_excel(path, sheet_name=0)
```

SQL (any DB-API or SQLAlchemy connection):
```python
import pandas as pd
df = pd.read_sql("SELECT * FROM schema.table", conn)
# Large tables: sample a recent window when a timestamp exists, e.g.
#   WHERE ts > DATEADD(hour, -2, GETDATE())   -- or LIMIT / TOP for a blind cap.
```

Kusto / KQL (azure-kusto-data, or Azure Data Explorer):
```python
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
client = KustoClient(KustoConnectionStringBuilder.with_az_cli_authentication(cluster))
resp = client.execute(database, "MyTable | where Timestamp > ago(2h) | take 100000")
df = dataframe_from_result_table(resp.primary_results[0])  # kusto helper
```
Prefer a time-bounded window (e.g. `ago(2h)`) over a blind `take`: for telemetry
it gives a recent, contiguous slice that reflects current data shape, instead of
an arbitrary one. Widen the window if the recent slice is too small to be
representative.

pandas (already in memory): use the DataFrame directly.

Then strip whitespace from column names so the checks are reliable:
```python
df.columns = [str(c).strip() for c in df.columns]
```

## Step 2: Structural overview

```python
print(df.shape)                    # rows, columns
print(df.dtypes)                   # wrong types: numbers as text, dates as strings
print(df.head()); print(df.tail()) # header-as-data, totals rows, shifted columns
```

## Step 3: Summary statistics

```python
print(df.describe(include="all").T)
```
Numeric columns show count, mean, std, min, quartiles, max. Other columns show unique count, top value, frequency. This is the single most informative table for spotting wrong ranges and unexpected values.

## Step 4: Missing values

```python
miss = (df.isnull().sum() * 100 / len(df)).sort_values(ascending=False)
print(miss[miss > 0])
```
Flag columns above a threshold (start at 20 percent), fully empty columns, and note which columns are fully populated before any join or aggregate.

## Step 5: Duplicate rows

```python
dups = int(df.duplicated().sum())
print(f"duplicate rows: {dups}")
```
Duplicates inflate counts and bias aggregates. Catch them before any group-by or sum.

## Step 6: Constant and near-constant columns

```python
for c in df.columns:
    if df[c].isnull().all():
        continue
    top = df[c].value_counts(normalize=True, dropna=False).iloc[0]
    if df[c].nunique(dropna=False) <= 1:
        print(f"constant: {c}")
    elif top >= 0.99:
        print(f"near-constant: {c} ({top:.1%})")
```
These carry little or no information and are usually safe to drop or worth questioning.

## Step 7: Candidate keys and IDs

```python
n = len(df)
for c in df.columns:
    if df[c].nunique(dropna=False) == n:
        print(f"candidate key: {c}")
```
Confirm any column assumed to be a join key is actually unique before joining. A name hint (id, key, uuid, code) is a clue, not proof.

## Step 8: Categorical cardinality

```python
for c in df.select_dtypes(exclude="number").columns:
    u = df[c].nunique(dropna=False)
    flag = "  [high: free text or parse issue?]" if u > n * 0.5 else ""
    print(f"{c}: {u} unique{flag}")
```
Unexpectedly high cardinality on a column expected to be categorical often signals a parsing problem or free text where a category was expected.

## Step 9: Numeric range and outlier flags

```python
for c in df.select_dtypes(include="number").columns:
    s = df[c].dropna()
    if s.empty:
        continue
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    out = int(((s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)).sum())
    print(f"{c}: min={s.min():.4g} max={s.max():.4g} outlier_candidates={out}")
```
Outliers are candidates to inspect, not errors. A wide spread can be legitimate.

## Step 10: Format and consistency

```python
for c in df.select_dtypes(exclude="number").columns:
    v = df[c].dropna().astype(str)
    if v.empty:
        continue
    if (v != v.str.strip()).any():
        print(f"whitespace: {c}")
    if pd.to_numeric(v, errors="coerce").notna().mean() >= 0.9:
        print(f"numeric stored as text: {c}")
```

## Reporting

Summarize flags by severity, not as a raw dump:
- Blockers: broken keys, heavy missingness, duplicates that affect counts.
- Cleanups: whitespace, numeric-as-text, constant columns.
- Notes: outlier candidates, high cardinality.

State what each flag affects so the user can decide what to fix. A clean triage rules out mechanical problems, not domain errors.

## Notes per access method

- SQL and Kusto: triage a bounded sample first. When the table has a timestamp, prefer a recent time window (Kusto `where Timestamp > ago(2h)`, SQL `WHERE ts > DATEADD(hour, -2, GETDATE())`) over a blind `take` / `TOP` / `LIMIT`, so the sample reflects current data shape. Confirm the sample is representative before trusting rates; row counts and key uniqueness must be checked on the full table, not the sample.
- Excel: check the sheet name and whether a header or totals row was read as data.
- pandas in memory: dtypes already reflect prior parsing, so a numeric column read earlier as text stays text until converted.
