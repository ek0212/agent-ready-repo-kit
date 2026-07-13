---
name: dataset-triage
description: Run first-pass sanity checks on tabular data before analysis, joins, reports, or modeling. Works for CSV, TSV, Excel, SQL, Kusto/KQL, or pandas DataFrame. Covers shape, dtypes, missingness, duplicate rows, constant columns, candidate keys, categorical cardinality, numeric ranges, outliers, and format issues. Use when user asks "what's in this dataset", "is this data clean", "what should I check first", or points at an unfamiliar table/query result.
---

# Dataset Triage

Fast first look at tabular data. Catch wrong dtypes, missingness, duplicates, junk columns, broken keys, format issues before downstream work.

Triage only. Report flags. Do not change data.

## Use When

Unfamiliar row/column data appears: file, SQL table, Kusto/KQL table, pandas DataFrame.

Skip image, text, audio, non-tabular data.

## Step 1: Load DataFrame

Pick loader. After DataFrame exists, same checks.

File:

```python
import pandas as pd
df = pd.read_csv(path)            # or sep="\t" for .tsv
df = pd.read_excel(path, sheet_name=0)
```

SQL:

```python
import pandas as pd
df = pd.read_sql("SELECT * FROM schema.table", conn)
# Large tables: sample a recent window when a timestamp exists, e.g.
#   WHERE ts > DATEADD(hour, -2, GETDATE())   -- or LIMIT / TOP for a blind cap.
```

Kusto / KQL:

```python
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
client = KustoClient(KustoConnectionStringBuilder.with_az_cli_authentication(cluster))
resp = client.execute(database, "MyTable | where Timestamp > ago(2h) | take 100000")
df = dataframe_from_result_table(resp.primary_results[0])  # kusto helper
```

Prefer time window like `ago(2h)` over blind `take`. Recent contiguous slice shows current shape. Widen if too small.

pandas in memory: use directly.

Normalize columns:

```python
df.columns = [str(c).strip() for c in df.columns]
```

## Step 2: Structure

```python
print(df.shape)                    # rows, columns
print(df.dtypes)                   # wrong types: numbers as text, dates as strings
print(df.head()); print(df.tail()) # header-as-data, totals rows, shifted columns
```

## Step 3: Summary Stats

```python
print(df.describe(include="all").T)
```

Spot wrong ranges and unexpected values.

## Step 4: Missing Values

```python
miss = (df.isnull().sum() * 100 / len(df)).sort_values(ascending=False)
print(miss[miss > 0])
```

Flag high missingness, start at 20 percent, fully empty columns, fully populated join/aggregate fields.

## Step 5: Duplicates

```python
dups = int(df.duplicated().sum())
print(f"duplicate rows: {dups}")
```

Duplicates inflate counts and bias aggregates.

## Step 6: Constant Columns

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

Question/drop low-information columns.

## Step 7: Candidate Keys

```python
n = len(df)
for c in df.columns:
    if df[c].nunique(dropna=False) == n:
        print(f"candidate key: {c}")
```

Confirm assumed join keys unique. Names like id/key/uuid/code are clues, not proof.

## Step 8: Categorical Cardinality

```python
for c in df.select_dtypes(exclude="number").columns:
    u = df[c].nunique(dropna=False)
    flag = "  [high: free text or parse issue?]" if u > n * 0.5 else ""
    print(f"{c}: {u} unique{flag}")
```

High cardinality in expected category often means parse issue or free text.

## Step 9: Numeric Range And Outliers

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

Outliers are inspect candidates, not automatic errors.

## Step 10: Format Consistency

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

## Report

Severity:

- **Blockers:** broken keys, heavy missingness, count-affecting duplicates.
- **Cleanups:** whitespace, numeric-as-text, constant columns.
- **Notes:** outlier candidates, high cardinality.

State effect of each flag. Clean triage rules out mechanical issues, not domain errors.

## Access Notes

- SQL/Kusto: bounded sample first. With timestamp, prefer recent window, Kusto `where Timestamp > ago(2h)`, SQL `WHERE ts > DATEADD(hour, -2, GETDATE())`, over blind `take` / `TOP` / `LIMIT`. Confirm representativeness. Check row counts and key uniqueness on full table.
- Excel: check sheet name and header/totals rows.
- pandas in memory: dtypes reflect prior parsing until converted.
