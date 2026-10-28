# Project-file backup — 2026-10-28

This index inventories 40 project/conversation attachments. **Raw attachment backup status is partial, not complete.**

- `BACKUP_INDEX.json` preserves original filenames, original mounted-file byte counts, local Git blob SHA-1, SHA-256, canonical route, and destination path.
- `attachments/` currently contains exact blob copies for 13 attachments whose content was already present in the canonical repository. Those are byte-identical and safely reused.
- The other 27 attachment-specific snapshots differ from the existing GitHub files. Their hashes and current canonical source routes are recorded, but those distinct raw/text versions are not yet copied; do not treat a route-equivalent source as a snapshot backup.
- Do not overwrite current source owners with old or alternative bundles. The archive is provenance; current scoped author decisions and complete source owners remain authoritative.

The small old starter README from `kazekamimp3/kazekamimp3` is preserved under `backups/repository_snapshots_20261028/kazekamimp3/README.md`. The old repository now points to `kazekamimp3/kaze808`.
