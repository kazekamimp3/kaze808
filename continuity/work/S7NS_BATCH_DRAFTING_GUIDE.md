# S7NS batch episode drafting — plain-English guide

This adds a manual-start workflow that asks Google's Gemini model to draft 1–5 proposed S7NS episodes in one run and saves them on a separate GitHub branch. It does not run on every commit, publish episodes, change canon, or mark anything delivered.

It uses the approved E82–E100 cards in continuity/author/S7NS_SPACE_ARC_E82_E100_AI_STUDIO_HANDOFF_20261027.md. It refuses episode numbers outside that scoped handoff.

## One-time setup

### 1. Create a Gemini API key
1. Open [Google AI Studio API keys](https://aistudio.google.com/api-keys) on your phone.
2. Sign in and create a new API key.
3. Keep it private like a password. Never paste it into ChatGPT or a GitHub file.
4. Check [AI Studio usage](https://aistudio.google.com/usage) before large batches. API limits and possible charges depend on your Google project and usage.

### 2. Save it as a GitHub secret
1. Open https://github.com/kazekamimp3/kaze808
2. Open **Settings**.
3. Open **Secrets and variables** → **Actions**.
4. Tap **New repository secret**.
5. Name it exactly GEMINI_API_KEY.
6. Paste the key into the Secret field and save.

The key is not stored in repository files.

## How to run from your iPhone

After the setup pull request is reviewed and merged into main:

1. Open https://github.com/kazekamimp3/kaze808/actions
2. Select **S7NS batch episode drafting**.
3. Tap **Run workflow**.
4. Start with episode 82 and batch count 2 for the first test.
5. Leave the model as gemini-3.8-flash.
6. Tap **Run workflow** and wait.
7. Open the draft PR or branch link shown in the run summary.

Later you can choose up to 5 episodes per batch. Five complete episodes take more time and can use substantially more API quota than two.

## Safety rules

- Drafts are written under continuity/drafts/ai_studio_run_<run id>/.
- Existing manuscripts/checkpoints, CURRENT.json, and DELIVERY_LEDGER.json are not edited.
- Every batch report flags the unresolved E74–E80 continuity gap.
- The workflow checks repository branches for likely duplicate batch drafts before generating.
- Drafts are not official delivery, canon changes, or author acceptance.
- It never merges its draft pull request.

## Why the cursor is still held

The official records still report E73 / next E74. E80 and E81 have verified saved pairs, but E74–E80 have unresolved source, delivery, title, or locator discrepancies. This workflow does not pretend those gaps are resolved. It only drafts the explicitly selected future E82–E100 cards as proposals.

Before any official delivery, recover and reconcile E74–E80 and their matching manuscripts/checkpoints. Do not change the official cursor until the consecutive sequence is supported by evidence and author decisions.

## If something fails

- **Missing key:** complete the setup above.
- **API or quota error:** inspect the failed GitHub Actions run and AI Studio usage. Do not repeatedly rerun large batches until the cause is understood.
- **No automatic PR:** the branch is still saved. Open its link and create a draft pull request manually.
- **Short or truncated draft:** check the batch report and revise before delivery.
- **Duplicate warning:** inspect the named branch and reuse/revise that draft instead.
- **Missing source owner:** the report identifies missing mapped owner groups. Resolve those sources before treating a draft as ready.

## Not automated yet

This does not reconcile E74–E80, decide which conflicting E76/E77 version is authoritative, merge drafts into canon, deliver episodes in ChatGPT, or mark author acceptance. Those require evidence and/or explicit author decisions.
