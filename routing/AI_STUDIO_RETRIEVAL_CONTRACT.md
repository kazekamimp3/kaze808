# AI Studio retrieval contract

## Functional abstraction
Route by capability before selecting documents. A prompt describes a task; the router declares which knowledge functions are needed; the logical/physical map resolves each function's owner to an actual file, bundle section or state record. The model should not recursively read the entire repository for a narrow task.

## Logical owner vs physical source
A logical owner is stable semantic identity (for example, `state.live_episode_cursor` or `cast.character_fidelity`). A physical source is a concrete path/section/hash. One logical owner may require multiple physical owners; one physical bundle may contain many logical owners. Do not assume a logical owner is a standalone file. Use the master source index, complete-owner access index and manifest to resolve it.

## Retrieval sequence
1. Choose one or more routes from `routing/CAPABILITY_ROUTER.yaml`.
2. Resolve the logical owner in `routing/LOGICAL_PHYSICAL_SOURCE_MAP.json`.
3. Check `KAZE_READ_FIRST.txt` and live state records when current authority/continuity matters.
4. Fetch full relevant source owners. If bundled, use exact recorded location and integrity metadata.
5. Check scoped author updates, exclusions, current actor/resource state and source status.
6. Report unresolved source conflicts. Do not invent resolution.
7. On authorized writes, preserve prior contents/commits as evidence and verify the destination by readback.

## Keep context lean without losing authority
- Do not load all root numbered bundles automatically; many are large compatibility bundles.
- Do not use a summary to replace an owner where the complete owner is available.
- Do not assume every file in an index is current; respect scope and precedence.
- Do not treat research, setup receipts, future plans, selected concepts or prepared episodes as occurred story.
- Read the manuscript, checkpoint and delivery reconciliation needed for the actual cursor before PLAY.
- WORK advances zero fictional time. PLAY requires explicit authorization.
