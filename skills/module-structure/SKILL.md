---
name: module-structure
description: Enforce predictable file organization and import grouping when creating or editing code modules.
when_to_use: Invoke when creating a source file, moving code between modules, changing imports, or cleaning up file order.
---

# Module Structure

## When To Invoke This Skill

- When creating a new source file.
- When editing imports or moving code between modules.
- When a file has become difficult to scan.

## Inputs

- Target source file.
- Existing file-order conventions in the repo.
- Language-specific formatter or linter rules.

## Procedure

### Step 1: Inspect Local Ordering

Check nearby files before changing structure. Match the repo's convention if it differs from this skill.

### Step 2: Order Top To Bottom

Use this order unless the repo has a stronger convention:

1. Copyright or license header, if present.
2. Imports.
3. Constants.
4. Classes.
5. Functions.
6. Executable entrypoint, such as `if __name__ == "__main__":`.

### Step 3: Group Imports

Group imports as:

1. Standard library.
2. Third-party packages.
3. Local or relative imports.

Keep imports at the top unless the repo deliberately uses lazy imports.

### Step 4: Verify

Run the repo formatter, linter, or import sorter if available.

## Outputs

- Predictably structured module.
- Verification result or note that no formatter/linter was available.
