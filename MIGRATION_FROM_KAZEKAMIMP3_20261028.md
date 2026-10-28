# Migration from `kazekamimp3/kazekamimp3` to `kazekamimp3/kaze808`

Date: 2026-10-28
Status: MIGRATION POINTER + PROVENANCE COPY; old repository intentionally not deleted.

## Findings
A live GitHub tree inspection of `kazekamimp3/kazekamimp3` found exactly one tracked file: a 329-byte generic Google AI Studio starter `README.md`. It held no S7NS source files, manifests, episodes or project archive to merge.

## Action
- Preserve the exact source repository README in `backups/repository_snapshots_20261028/kazekamimp3/README.md`.
- Replace the old repository README with a short pointer to `kazekamimp3/kaze808`, avoiding future confusion over which repository is canonical.
- Preserve the previous target README and AGENTS instructions under `backups/repository_snapshots_20261028/kaze808/`.
- Organize retrieval using `AI_STUDIO_START_HERE.md`, `routing/CAPABILITY_ROUTER.yaml` and `routing/LOGICAL_PHYSICAL_SOURCE_MAP.json`.
- Preserve all available conversation/Project attachments under `backups/project_uploads_20261028/attachments/`, with a backup index for source-name/hash provenance.

## No silent destructive actions
The source repository is not deleted, no historical S7NS sources are removed, and no episode manuscript/checkpoint or active canon owner is overwritten by this migration. Its README serves as the forward pointer. This report does not equate package backup with author acceptance or project installation.
