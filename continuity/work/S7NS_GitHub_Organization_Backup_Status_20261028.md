# S7NS GitHub organization and backup status — 2026-10-28

## Canonical location
- Canonical repository: https://github.com/kazekamimp3/kaze808
- AI Studio start page: https://github.com/kazekamimp3/kaze808/blob/main/AI_STUDIO_START_HERE.md
- Paste-ready system prompt: https://github.com/kazekamimp3/kaze808/blob/main/AI_STUDIO_SYSTEM_PROMPT.txt
- Capability router: https://github.com/kazekamimp3/kaze808/blob/main/routing/CAPABILITY_ROUTER.yaml
- Logical/physical source map: https://github.com/kazekamimp3/kaze808/blob/main/routing/LOGICAL_PHYSICAL_SOURCE_MAP.json
- Retrieval contract: https://github.com/kazekamimp3/kaze808/blob/main/routing/AI_STUDIO_RETRIEVAL_CONTRACT.md

## Installed/read back
- PR #2 merged: https://github.com/kazekamimp3/kaze808/pull/2
- Canonical README and AGENTS entrypoints were replaced with shorter instructions; the previous copies are preserved under `backups/repository_snapshots_20261028/kaze808/`.
- The former `kazekamimp3/kazekamimp3` repository contained only the generic starter README. Its README now points to `kaze808`; the old README is preserved under `backups/repository_snapshots_20261028/kazekamimp3/README.md`. The old repo itself was not deleted.
- Readback verified the start page, prompt, capability router and valid JSON logical/physical map. Root README links to the router and prompt.
- The routing design uses Capability-Routed Functional Abstraction (CRFA) with Logical/Physical Source Separation as the companion principle.

## Backup status — NOT COMPLETE
Inventory: https://github.com/kazekamimp3/kaze808/blob/main/backups/project_uploads_20261028/BACKUP_INDEX.json

The index tracks 40 project/conversation attachment snapshots:
- 13 have exact content copies in the dated backup folder, reusing identical Git blobs already in the repository.
- 2 generated handoffs are archived as complete text-extracted copies; they are not claimed byte-identical to mounted raw files.
- 25 attachment-specific snapshots remain pending. Existing canonical owner routes are documented but are not treated as the same as the missing raw snapshot.

Tracking issue: https://github.com/kazekamimp3/kaze808/issues/4

## Existing integrity warning
The current `scripts/validate.py` GitHub Actions check fails on pre-existing manifest hash mismatches and invalid byte ranges. The same validator failed on main before PR #2. No source-owner or manifest rewrite was made as part of this routing job.

Tracking issue: https://github.com/kazekamimp3/kaze808/issues/3
Latest observed run at receipt preparation: https://github.com/kazekamimp3/kaze808/actions/runs/40785537896 (failed at the pre-existing validation step).

## Continuity safety
At this readback, `continuity/CURRENT.json` still reports E73 delivered provisionally / E74 next (`CURRENT` blob SHA: `46d557e00a0391f3fa6c2ddb3cadd0ad5a9ece1b`). `continuity/DELIVERY_LEDGER.json` remains untouched in this task (`8c7f9c737ab0351571d1a6bb11910c68bc592fda`). This GitHub organization job did not alter episode status, acceptance, PLAY authorization or fictional time.

## Final classification
- Retrieval architecture: INSTALLED_READBACK.
- Old repository pointer: INSTALLED_READBACK.
- Project attachment backup: PARTIAL, 15/40 paths archived.
- Existing integrity validator cleanup: OPEN.
- Canon continuity/cursor changes: NONE.
