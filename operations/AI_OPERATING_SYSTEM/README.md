# S7NS AI Operating System

A modular instruction set for using different AI assistants without giving them competing versions of S7NS.

**Current version: 1.1 (2026-10-30).** Shared execution, tool-access, sandbox, session-context, and delivery-format rules are defined in the Master Instruction.

## Install/use
1. Give the AI `MASTER_INSTRUCTION.md` as its persistent S7NS foundation.
2. For each task, attach only the relevant mode file from `MODES/`.
3. Keep the full current S7NS source package available separately. These instructions do not replace character manifests, complete source owners, episode manuscripts, checkpoints, or the active outline.
4. Use the activation command at the top of the selected mode file.
5. Preserve the handoff/status block when passing work to another AI.

## Seven modes
| Mode | Activation | Intended job |
|---|---|---|
| Brainstorming | `BRAINSTORM:` | Generate options without canonizing them |
| Outline development | `DEVELOP OUTLINE:` | Structure only author-selected material |
| Episode execution | `PLAY:` | Execute the exact authorized scope |
| Continuity audit | `AUDIT:` | Detect conflicts without repairing them silently |
| Character development | `CHARACTER WORK:` | Develop source-faithful character material |
| Research | `RESEARCH:` | Verify external facts separately from canon |
| Production management | `MANUAL UPDATE:` / `PRODUCTION:` | Retrieve, reconcile, track, and perform authorized operations |

## Raw-source bootstrap and platform adapters

Start external AI platforms at [PLATFORM_SOURCE_BOOTSTRAP.md](PLATFORM_SOURCE_BOOTSTRAP.md). It provides direct raw GitHub links and the required source retrieval order. Use the matching adapter from [ADAPTERS](ADAPTERS/): Grok Free (under 4,000 characters), Google AI Studio, or the generic raw-source adapter. Raw links do not guarantee platform fetch capability; if a model cannot retrieve them, attach the exact files instead.

## Active platform contract

GitHub is the authoritative source repository. Airtable provides structured tracking/projections. Notion provides encyclopedia, planning, handoffs and research documentation. Google Drive is retired from active S7NS operations unless Kaze explicitly reactivates it.

## Suggested AI assignment
- Google AI Studio: primary creative workshop and episode writer; use its raw-source adapter.
- Grok Free: optional wildcard brainstorming; use the ≤4,000-character adapter.
- Claude: independent editor and continuity reviewer.
- ChatGPT: source coordinator, research, and production management.
- Gemini app: alternative model and second opinion.

These are convenience assignments only. No model has canon authority.

## Existing S7NS procedures that remain controlling
- Active three-platform source/update contract: `operations/AI_OPERATING_SYSTEM/MASTER_INSTRUCTION.md` and `PLATFORM_SOURCE_BOOTSTRAP.md` (the dated four-connector contract is historical; its Google Drive requirement is superseded).
- Sole scene construction/revision procedure: `canon/presentation/Season3_Scene_Decision_Doctrine_20261010.md`
- Current state: `continuity/CURRENT.json`
- Delivery ledger: `continuity/DELIVERY_LEDGER.json`
- Source routing: `routing/MASTER_SOURCE_INDEX.json`
- Source manifest: `MANIFEST.yaml`
- Active outline/selected chronology: `continuity/SEASON3_ACTIVE_OUTLINE.json`

The two-episode seamless-feature default is conditional on the latest author direction and must never override a more specific current instruction.

## Setup audit snapshot: 2026-10-30
- GitHub CURRENT.json and DELIVERY_LEDGER.json report E73 / next E74.
- Airtable and Notion contain later provisional delivery evidence, including E74, E75, E80, E81, and E84–E85.
- E74–79 and official cursor reconciliation remain unresolved. E76–79 have exact-source gaps or title/version conflicts in the current inventory. Do not advance CURRENT/LEDGER or infer acceptance.
- The Oct 29 Space Saga remaster checkpoint is WORK-only: no episode draft, no PLAY, zero fictional time advanced. Older event inventory and E82–E100 development remain candidates unless specifically selected.
- Google Drive was unavailable in the checked ChatGPT environment on 2026-10-30 and was subsequently retired from active S7NS operations by Kaze. Do not recheck or use it unless explicitly reactivated.

This snapshot is a warning about reconciliation, not an amendment to story canon. Recheck live sources before every substantive task.

## File map
- [Master instruction](MASTER_INSTRUCTION.md)
- [Raw-source bootstrap](PLATFORM_SOURCE_BOOTSTRAP.md)
- [Grok Free adapter](ADAPTERS/GROK_FREE_4000.md)
- [Google AI Studio adapter](ADAPTERS/GOOGLE_AI_STUDIO.md)
- [Generic raw-source adapter](ADAPTERS/GENERIC_RAW_SOURCE.md)
- [01 Brainstorming](MODES/01_BRAINSTORMING.md)
- [02 Outline development](MODES/02_OUTLINE_DEVELOPMENT.md)
- [03 Episode execution](MODES/03_EPISODE_EXECUTION.md)
- [04 Continuity audit](MODES/04_CONTINUITY_AUDIT.md)
- [05 Character development](MODES/05_CHARACTER_DEVELOPMENT.md)
- [06 Research](MODES/06_RESEARCH.md)
- [07 Production management](MODES/07_PRODUCTION_MANAGEMENT.md)
