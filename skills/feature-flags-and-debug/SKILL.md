---
name: feature-flags-and-debug
description: Gate experimental, debug, or incomplete work behind feature flags and prevent debug behavior from leaking into production.
when_to_use: Invoke when adding debug UI, verbose logs, diagnostics, incomplete features, risky rollout behavior, or feature flag documentation.
---

# Feature Flags And Debug

## When To Invoke This Skill

- When adding experimental behavior.
- When adding debug UI, logs, or diagnostic paths.
- When a feature is incomplete but needs to be merged safely.
- Before release or PR review involving feature flags.

## Inputs

- Changed code.
- Existing feature flag or config system.
- Production build or deployment rules.

## Procedure

### Step 1: Decide Whether A Flag Is Needed

Use a feature flag for experimental, debug, incomplete, or risky behavior. Do not add flags for finished low-risk changes.

### Step 2: Use The Existing Flag System

Reuse the repo's existing flag/config pattern. Do not create a parallel flag mechanism.

### Step 3: Gate Debug Behavior

Wrap debug UI, verbose logs, diagnostics, and incomplete paths behind flags.

### Step 4: Set Safe Defaults

Disable debug or experimental behavior in production builds unless the release plan explicitly says otherwise.

### Step 5: Document Flags

Document active flags in a central config, README, or existing flag registry.

### Step 6: Verify Production Behavior

Check that production builds do not rely on debug flags being enabled.

## Outputs

- Flagged experimental or debug behavior.
- Updated flag documentation.
- Verification that production defaults are safe.
