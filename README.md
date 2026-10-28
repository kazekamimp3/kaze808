# S7NS — Canonical Source Repository

**Canonical home: `kazekamimp3/kaze808`.** This repository is organized for capability-routed retrieval by AI Studio and other agents. Start with [AI_STUDIO_START_HERE.md](AI_STUDIO_START_HERE.md), or paste [AI_STUDIO_SYSTEM_PROMPT.txt](AI_STUDIO_SYSTEM_PROMPT.txt) into an AI Studio system/instructions field.

## One entry point, task-routed source retrieval

1. Read [AI Studio start instructions](AI_STUDIO_START_HERE.md).
2. Read `KAZE_READ_FIRST.txt`, then live `continuity/CURRENT.json` and `continuity/DELIVERY_LEDGER.json`.
3. Use [`routing/CAPABILITY_ROUTER.yaml`](routing/CAPABILITY_ROUTER.yaml) to choose the capability route.
4. Resolve the logical owner to its physical source using [`routing/LOGICAL_PHYSICAL_SOURCE_MAP.json`](routing/LOGICAL_PHYSICAL_SOURCE_MAP.json), [`routing/MASTER_SOURCE_INDEX.json`](routing/MASTER_SOURCE_INDEX.json), and [`complete_sources/ACCESS_INDEX.json`](complete_sources/ACCESS_INDEX.json).
5. Read the full relevant owner and its current scope. An index or summary is not a substitute for the complete source.

## Current organization receipt

Read [the GitHub organization and backup status receipt](continuity/work/S7NS_GitHub_Organization_Backup_Status_20261028.md) for verified readbacks, the partial backup inventory, open integrity issue, and continuity-safety record.

## Repository layout

- `continuity/` — live episode state, delivery ledger, episode manuscripts/checkpoints, active chronology, scoped author decisions, and historical reconciliation.
- `canon/`, `character_sources/`, `complete_sources/` — character, voice, mechanics, relationship, presentation and original-source owners.
- `routing/` — capability routing, logical-owner to physical-source mapping, exact source locators and retrieval rules.
- `research/`, `research_sources/` — source-grounded research, coverage and identified open questions.
- `authority/`, `state/` — removals, resolution records, scoped state and evidence boundaries.
- `integrations/`, `project_install/`, `releases/` — connection/reference snapshots, project-install artifacts and versioned packages; these are not automatically live installations.
- `backups/` — date-stamped original project attachments and repository-migration provenance.

## Source and status discipline

Latest direct Kaze instruction controls its scope, followed by scoped active author authority, actual delivered-scene evidence, complete original owners, then derived plans and archives. Preserve deliberate contradictions and historical evidence; do not silently merge competing snapshots.

Keep `PROPOSED`, `AUTHOR_SELECTED`, `PREPARED`, `DELIVERED_PROVISIONAL`, `AUTHOR_ACCEPTED`, and `INSTALLED_READBACK` distinct. Delivery does not imply acceptance. WORK advances zero fictional time; PLAY requires explicit authorization. Never change the episode cursor based on a handoff or an unverified chat claim alone.

The root numbered Markdown bundles and old versioned snapshots are preserved for provenance and exact manifest routes. They are not an instruction to load every large bundle for every task. Route to the smallest sufficient capability set, then open each required complete owner.

## Known validation issue

The existing GitHub Actions integrity check is failing on source-hash and byte-range validation, including on main before the AI Studio router merge. Track it in [issue #3](https://github.com/kazekamimp3/kaze808/issues/3). Do not blindly rewrite manifest hashes to make the check green; reconcile exact source bytes and owner routes first.

## Backup and migration status

- [Project attachment backup](backups/project_uploads_20261028/README.md) documents the 2026-10-28 project-file archive. Its exact raw-snapshot backup remains partial (15/40 paths archived); [issue #4](https://github.com/kazekamimp3/kaze808/issues/4) tracks the 25 remaining attachment-specific snapshots.
- [Source-repository migration note](MIGRATION_FROM_KAZEKAMIMP3_20261028.md) records the contents of `kazekamimp3/kazekamimp3`. The former repository is kept as a redirect/provenance source, not deleted.
- Backup inventories preserve source filenames, hashes, and byte/text-normalization caveats. A content hash verifies stored bytes only; it does not mean the content is current canon or author-accepted.
