# Project-file backup — 2026-10-28

This index inventories the 40 project/conversation attachments visible in the session. **The full raw attachment backup is still incomplete.**

- `BACKUP_INDEX.json` preserves original filenames, original mounted-file byte counts, original Git blob SHA-1 and SHA-256, destination path, archive status and source route.
- 27 attachment snapshots are archived as content-exact copies, verified by matching each archived Git blob SHA-1 to the indexed original.
- 2 smaller generated handoff attachments have complete text-extracted snapshots stored, but Files-reader normalization changed their byte identity; they are not claimed as raw byte-identical backups.
- The remaining 11 attachment-specific snapshots are pending. Their original bytes, sizes and hashes were verified from the mounted attachments, but the connected Project Files reader is currently returning no readable content for those files, preventing safe transfer into GitHub. Their hashes/routes are not treated as backup copies. Track completion in [issue #4](https://github.com/kazekamimp3/kaze808/issues/4).
- Do not overwrite active source owners with old or alternative bundles. This backup is provenance; current scoped author decisions and complete-owner routes remain authoritative.

The old starter README from `kazekamimp3/kazekamimp3` is preserved under `backups/repository_snapshots_20261028/kazekamimp3/README.md`. The old repository now points to `kazekamimp3/kaze808`.
