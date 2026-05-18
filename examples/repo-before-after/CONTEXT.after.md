# Example Project Context

## Language

**Capture**: A user-triggered extraction of visible page content.
_Avoid_: scrape

**Export**: A user-requested local file generated from captured data.
_Avoid_: sync

**Sync**: Optional cross-device backup, disabled by default.
_Avoid_: backup, upload

## Relationships

- A **Capture** can produce zero or one **Export**.
- **Sync** must never happen as a side effect of **Capture**.

## Flagged Ambiguities

- "Save" was used for both local export and remote sync. Use **Export** for local files and **Sync** for remote backup.

