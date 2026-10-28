# Project-file backup — 2026-10-28

This index inventories the 40 project/conversation attachments available in the session. **The full raw attachment backup is still incomplete.**

- `BACKUP_INDEX.json` preserves original filenames, original mounted-file byte counts, original Git blob SHA-1 and SHA-256, destination path, archive status and source route.
- 13 attachments reuse content-exact blobs already present in the canonical repository.
- 2 smaller generated handoff attachments have a complete text-extracted snapshot stored, but Files-reader normalization changed their length; their raw byte identity is not claimed.
- The remaining 25 attachment-specific snapshots are pending. Their canonical/current source routes are listed, but route-equivalent content is not represented as a raw snapshot backup. Track completion in [issue #4](https://github.com/kazekamimp3/kaze808/issues/4).
- Do not overwrite active source owners with old or alternative bundles. This backup is provenance; current scoped author decisions and complete-owner routes remain authoritative.

The old starter README from `kazekamimp3/kazekamimp3` is preserved under `backups/repository_snapshots_20261028/kazekamimp3/README.md`. The old repository now points to `kazekamimp3/kaze808`.
