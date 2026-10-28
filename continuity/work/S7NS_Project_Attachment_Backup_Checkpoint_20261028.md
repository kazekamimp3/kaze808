# S7NS Project Attachment Backup — Resume Checkpoint
Date: 2026-10-28
Repository: https://github.com/kazekamimp3/kaze808
Mode: WORK — no fictional time advanced.
Purpose: Resume the attachment backup from the newest unfinished step. Do not restart completed work.

## Verified repository state at checkpoint
- Main commit before checkpoint: `ba85412fbf10d2f86aa06320cc2cd628d6cf38b7`
- Main tree: `259c6a183d7b384cce226087cedc707e500d67cf`
- Backup index: `d5d68f006b64c17f85d3e1fadba305b0be20ffdf`
- Backup status from index: `PARTIAL_BACKUP_29_OF_40_SNAPSHOT_PATHS_ARCHIVED`
- Exact archived snapshots: 27
- Text-extracted snapshots without byte-identity claims: 2
- Attachment-specific copies still pending: 11
- Inventory total: 40
- Continuity cursor file SHA (read-only check): `46d557e00a0391f3fa6c2ddb3cadd0ad5a9ece1b`
- Delivery ledger file SHA (read-only check): `8c7f9c737ab0351571d1a6bb11910c68bc592fda`
- The continuity cursor and delivery ledger were not changed.

## Completed work to preserve
- Keep every existing archived snapshot and all prior commits.
- The index currently reports 27 snapshots whose archived Git blob SHA-1 matches the indexed original, plus 2 text-extracted snapshots that are explicitly not claimed byte-identical.
- The old repository migration, routing entry points, existing canonical source files, and backup receipts remain as previously committed. Do not recreate or overwrite them.

## Exact newest unfinished step
Recover and hash-verify the remaining originals, continuing with the multi-thousand-line source files that the Files reader truncates or normalizes.
The latest active test was reconstructing `18_WORLD_PRESENTATION(1).md` from the mounted attachment `file_00000000bcec820ea55409a0d61e1044`. Multi-range reads returned incomplete/normalized segments; candidate reconstructions did not match the indexed original Git blob SHA-1 `bf79c794715e4477444d44bae3abb90aa41af4c5`. No replacement was committed for that failed reconstruction. Do not label it exact without a hash match.
`19_RESEARCH(1).md` and `MANIFEST_SPACE_20261024.yaml` also exceed a single read range and need complete-source retrieval plus verification; do not assume their current partial reads are full.
Small-source checks confirmed exact matches for `17_BELLY_COMBAT.md`, `Dana_Character_Source_2.md`, `Mana_Character_Source_2.md`, and `dana_mana.md`; those checks do not themselves prove a snapshot is archived unless the destination path exists and index status is updated/read back.

## Remaining pending filenames
- `02_CURRENT_STATE_SPACE_20261024.md` — original SHA-1 `9f4d325da65515036cdd64ca8d458303120c8a72`, bytes 2058342
- `03_INDEX_ROUTING.md` — original SHA-1 `9c9339892b55188f1115fb4cbdab220782102003`, bytes 3015276
- `03_INDEX_ROUTING_SPACE_20261024.md` — original SHA-1 `c25ebf0a64ff23a7740f8211f836a33f324e3ba9`, bytes 3614995
- `13_SEASON3_CURRENT.md` — original SHA-1 `eab18eacc05216b3b186e55a7c6e170601da4ec7`, bytes 1089992
- `15_SEASON3_PLOTS.md` — original SHA-1 `82e770312fb12b734331f81d793ac57d9ec39e43`, bytes 1233572
- `15_SEASON3_PLOTS_SPACE_20261024.md` — original SHA-1 `6436749166edc07cc0229d55a02e42f3b445e24e`, bytes 2673388
- `16_ROSTER_DUELS_TRAVEL.md` — original SHA-1 `81991d7dc1c7b9e5290c69dacebe105744c73fb4`, bytes 1007570
- `18_WORLD_PRESENTATION(1)_R21_20261024.md` — original SHA-1 `f9861f69fc80310bdbaaf466382d5b922356432c`, bytes 687264
- `19_RESEARCH(1).md` — original SHA-1 `2fc02ec826edef0b08111082d94fdf5755ae76c5`, bytes 311336
- `19_RESEARCH(1)_R20_20261024.md` — original SHA-1 `e03781f3ccba8cb8a6a74199a24c7f2e20e4f4c1`, bytes 344823
- `MANIFEST_SPACE_20261024.yaml` — original SHA-1 `467e35ff2594724af054eed5429db24524a30b71`, bytes 231335

## Resume protocol
1. Read this checkpoint, then reread the live backup index and main tree before any write.
2. Use a source path that returns the complete original bytes/text. Do not reconstruct by guessing separators, trimming, or normalizing.
3. Create Git blobs and compare against each indexed original SHA-1. Only matching blobs may be marked exact.
4. For a text-only capture whose bytes cannot be reproduced, explicitly label it text-extracted; never call it raw or byte-identical.
5. Add only verified missing snapshot paths; preserve conflicting versions and all existing work.
6. Update the backup index and README in the same commit, then read them back from GitHub.
7. Update Issue #4 with verified progress. Do not close it until all 40 attachments are accounted for at the required fidelity.
8. Keep `continuity/CURRENT.json` and `continuity/DELIVERY_LEDGER.json` unchanged during backup work.

## Current pending list is authoritative only as of this checkpoint
Always re-read the live index first on resume; newer verified repository evidence supersedes this snapshot.
