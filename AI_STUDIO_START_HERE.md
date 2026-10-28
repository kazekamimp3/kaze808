# AI Studio — S7NS Start Here

## Purpose

This is the single front door for S7NS. The method is **Capability-Routed Functional Abstraction (CRFA)** with **logical/physical source separation**: first identify the function needed, then load only that function's required capabilities, then resolve each logical owner to its actual physical source. Do not begin by loading every file or by guessing filenames.

## Startup chain (mandatory for substantial work)

1. Read `KAZE_READ_FIRST.txt` for the newest scoped author directions. Historical headers inside it remain historical when superseded by newer sections.
2. Read the complete `continuity/CURRENT.json` and `continuity/DELIVERY_LEDGER.json`.
3. Follow their matching manuscript, checkpoint, state-owner and delivery-reconciliation paths. Do not infer status from a dated summary, handoff, or prepared file.
4. Read the newest scoped direct-author source relevant to this task.
5. Route the requested task through `routing/CAPABILITY_ROUTER.yaml`.
6. Resolve logical owners through `routing/LOGICAL_PHYSICAL_SOURCE_MAP.json`; then consult `routing/MASTER_SOURCE_INDEX.json`, `complete_sources/ACCESS_INDEX.json`, and `MANIFEST.yaml` for the actual file, bundle section, offset, length and hash.
7. Read all of each relevant complete owner before making consequential claims or writing scenes. A route/index/summary is not the owner itself.

## Source authority

Latest direct author instruction for its scope → active scoped author authority → actual delivered scene evidence → complete original owners → derived plans and archives. Preserve unresolved contradictions when sources do not settle them. Keep these states separate: `PROPOSED`, `AUTHOR_SELECTED`, `PREPARED`, `DELIVERED_PROVISIONAL`, `AUTHOR_ACCEPTED`, `INSTALLED_READBACK`. A delivered draft is not automatically accepted or installed.

## Task routing at a glance

| Task | Begin with | Then resolve |
|---|---|---|
| Current episode / what happens next | `continuity/CURRENT.json`, `continuity/DELIVERY_LEDGER.json` | Matching manuscript, checkpoint, delivery reconciliation and active outline |
| Episode generation / PLAY | This startup chain + the sole Scene Decision Doctrine | All relevant character, psychology, speech, relationship, mechanics, resource and scene owners |
| Character voice / fidelity | Capability route for that character | Current owner plus original voice/personality/relationship/mechanics owners |
| Power, kit, inventory or BELLY mechanics | Mechanics/kit capability | Exact current equipment and mechanic owner; verify actor, access, resources and state |
| Author decisions / exclusions | Scoped-authority capability | Latest matching decision and its scope; preserve older sources as evidence |
| Research | Research capability | Primary evidence, coverage, limits, citations and open gaps; research does not silently modify canon |
| Project setup / AI Studio prompt | Project configuration / retrieval capability | AGENTS.md, this file, KAZE_READ_FIRST, router, indexes, manifest |
| Backup / migration / install | Backup and integration capability | Backup index, commit/tree readback, connector-specific status and provenance receipts |

## Important behavior

- WORK advances **zero** fictional time. PLAY requires an explicit authorization.
- The normal PLAY format is two consecutive episodes as one seamless feature unless Kaze overrides it. Follow the sole existing scene-decision doctrine.
- Wade/Deadpool is the sole main-story narrator from the controlled point; Billy narrates campfire Specials. Narrator knowledge is bounded, and Brian cannot hear Wade.
- Do not restore removed actors, identities, forms, powers, relationships or equipment from historical bundles.
- Use character-specific humor and real agency; comedy may unfold inside the same action rather than replace it. Preserve consequential action, established power kits, visible cause/effect, and lasting consequences.
- Do not read every 1–3 MB numbered bundle by default. The root bundles are preserved compatibility sources; use the map and exact complete owner needed for the task.
- If a physical source is missing, inaccessible, or conflicting without a controlling resolution, say that plainly. Never claim that a cross-workspace write or project installation happened without readback evidence.

## Repository map

- `continuity/`: live state, delivery status, episodes, checkpoints, active outline, scoped author decisions.
- `canon/` and `character_sources/`: current character/voice/mechanics owners and complete originals.
- `routing/`: capability routes and logical-to-physical source resolution.
- `complete_sources/ACCESS_INDEX.json`: directory of original owner names; pair with the master source index.
- `research/` and `research_sources/`: grounded external research and coverage.
- `integrations/`, `project_install/`, `releases/`: reference projections and versioned installation/release artifacts, not automatic proof of current installation.
- `backups/`: project-file backups and repository migration history.

## Live cursor caution

At the time of this router change, GitHub `CURRENT.json` and `DELIVERY_LEDGER.json` are authoritative and report E73 as last delivered / E74 next, with later E74–80 chat-delivery reconciliation open. Verify live matching evidence before continuation. This note does not alter the cursor.
