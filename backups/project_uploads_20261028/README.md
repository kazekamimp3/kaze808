# Project-file backup — 2026-10-28

This directory preserves the 40 project/conversation attachments available to the current S7NS session at backup time, including the uploaded source bundles/manifests, the two current space/R20/R21 variants, Dana/Mana sources and two generated handoffs.

- `BACKUP_INDEX.json` records every original filename, original source hashes/sizes, the destination path and the copy method.
- `attachments/` contains the retrievable text copy for every attachment.
- Exact byte-identical files already present in the canonical repository reuse the existing identical Git blob in the archive path instead of needlessly creating a second content object.
- For other Project-backed attachments, the Files text reader normalizes line endings while exposing the full text; the original mounted-file SHA-256 and byte count remain recorded for provenance. Therefore those text copies are searchable/readable backups, but their Git blob SHA is not claimed to match the original raw bytes.
- This archive is provenance, not new canon. Active sources, author scope, current episode state and complete-owner routes still control.

The small previous starter README from `kazekamimp3/kazekamimp3` is preserved under `backups/repository_snapshots_20261028/kazekamimp3/README.md`, and the source repository is being left with a migration pointer rather than destructively deleted.
