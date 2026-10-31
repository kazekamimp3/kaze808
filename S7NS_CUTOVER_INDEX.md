# S7NS Clean-Cutover Source Snapshot
Built: 2026-10-31
Repository: kazekamimp3/kaze808
Branch: cutover/s7ns-authoritative-20261031
Parent: ac8138414d32f53ce75f479b69817a62ee60b18a
Purpose: self-contained replacement snapshot of the routed source bundles plus current live control, continuity and scoped author-decision owners. Existing main branch and historical repository are untouched.

## Authority and cursor
The live source router is continuity/CURRENT.json (E73 DELIVERED_PROVISIONAL; acceptance NOT_ASSERTED; next E74) and continuity/DELIVERY_LEDGER.json. E74–79 reconciliation is still open. Later backups do not advance the cursor. continuity/SEASON3_ACTIVE_OUTLINE.json is the current forward-plan owner. Selected future development is not occurred.

## Included source classes
- 28 physical source bundles declared as controlling_bundle by the repository's root MANIFEST.yaml generation. The old manifest itself is deliberately excluded because its endpoint is stale; the source bundles are retained as physical owners and routed by current index files.
- Live startup, current-state, delivery-ledger, active-outline, routing, access-index and doctrine files.
- Current cast-focus and condensed-weave author owners.
- E82–E100 future-development handoff and Kaze Spice/Vaas scoped author update.
- E73 manuscript, checkpoint and chat-delivery reconciliation.
- 2026-10-31 approved Space Saga future-development record.
- This index and PROJECT_INSTRUCTIONS.txt.

## Explicit exclusions
No old root MANIFEST.yaml, R21 attachment manifest, October 29 49-entry handoff ZIP, duplicate renamed upload copies, episode drafts beyond the verified live E73 pair, or unrelated historical backup snapshots are included as separate replacement sources. The included source bundles retain historical evidence where those bundles are the routed physical owner; they are not duplicate copies of newer standalone control files.

## Safety
This branch is a clean snapshot branch. It does not delete or replace files on main. Do not cut over an existing workspace until every included file is read back, all source routes resolve, and local extraction/hash QA passes. The unresolved E74–79 gate is disclosed, not silently adjudicated.

## Included files
See the branch tree. Every included file is a Git blob selected by path and SHA from the parent repository, except this index, PROJECT_INSTRUCTIONS.txt and the scoped 2026-10-31 author-decision record, which are new UTF-8 blobs.
