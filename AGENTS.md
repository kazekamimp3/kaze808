# S7NS agent instructions — capability-routed retrieval

The only canonical project repository is `kazekamimp3/kaze808`. Begin every substantial S7NS WORK/PLAY from `AI_STUDIO_START_HERE.md`; do not treat this file as a replacement for its source routes.

## Required source-loading sequence
1. Read `KAZE_READ_FIRST.txt`.
2. Read the whole live `continuity/CURRENT.json` and `continuity/DELIVERY_LEDGER.json`.
3. Resolve the matching manuscript, checkpoint and any delivery reconciliation named by those live records.
4. Read the newest scoped author decisions relevant to the requested task.
5. Use `routing/CAPABILITY_ROUTER.yaml` then `routing/LOGICAL_PHYSICAL_SOURCE_MAP.json` to determine the required capabilities and physical owners.
6. Use `routing/MASTER_SOURCE_INDEX.json`, `complete_sources/ACCESS_INDEX.json`, and the applicable manifest to retrieve complete original owners. Read the whole relevant owner section, not just an index summary.

## Hard rules
- The logical owner is a concept; the physical source is the actual file/section/hash. Never assume the owner name is a standalone filename.
- Prefer current standalone owners where routed; otherwise locate the complete owner by the exact bundle/offset/length/hash mapping. If absent or truncated, report the missing source rather than inventing a substitute.
- Keep proposals, selections, preparation, delivery, author acceptance and live installation distinct.
- Never overwrite newer author decisions with old snapshots. Do not silently retcon originals, intentionally unresolved mechanics, or deliberate absurdities.
- WORK advances zero fictional time. PLAY only on explicit authorization. Do not replay a delivered scene simply because a newer package exists.
- Only load sources needed for the requested capability. Do not bulk-load all numbered root bundles by default; those files are preserved compatibility bundles and may be very large.
- For writing episodes, follow the sole `canon/presentation/Season3_Scene_Decision_Doctrine_20261010.md`; do not invent a second scene-construction procedure.
- For cross-workspace sync, reconcile live evidence once where connectors are accessible and verify each write by readback. Never claim unavailable Drive/Project UI changes.
- Do not delete source history or migration repositories as a shortcut to organization.
