# S7NS Full-Corpus Ingestion for Google AI Studio

Status: ADDITIVE IMPLEMENTATION GUIDE
Purpose: Make the complete text-based S7NS repository corpus searchable from Gemini through a persistent File Search store.
This guide does not change canon, continuity, delivery status, author acceptance, or PLAY authorization.

## What this provides

A persistent Gemini File Search store containing the text files tracked in each selected Git branch. The ingestion script:

- Reads every UTF-8 text blob tracked by each selected branch, not just files returned by the current capability router.
- Indexes Markdown, TXT, JSON, YAML, source code, and other UTF-8 text files without filtering by lore topic.
- Keeps branch snapshots distinct. The same path on two branches is indexed twice with branch and commit provenance.
- Adds a small provenance header to each indexed copy containing branch, commit, path, and SHA-256. The original repository files are not changed.
- Waits for each import operation and writes a local JSON report listing imported files, skipped non-text/binary files, failures, branch commits, and the File Search store name.
- Marks the run INCOMPLETE if any text file fails to import or a non-text file is skipped. A successful script run means the eligible text corpus was indexed, not that Gemini has read every passage in every answer.

The File Search index is a retrieval system, not a promise that every source is inserted into every prompt. Ask questions against the whole corpus and require source citations. For a task requiring exhaustive review, instruct the model to enumerate and inspect all relevant source records, and report coverage limits.

## Important source-branch handling

The S7NS repository has divergent authority branches. Do not merge them merely to make ingestion easier.

Default branches included by the script:
- `main`
- `cutover/s7ns-authoritative-20261031`

They are indexed as separate snapshots. A file present on one branch but absent from the other remains branch-specific. Conflicting versions remain separately retrievable. The index does not decide which branch controls a disputed scope.

The current source-reconciliation checkpoint also records unresolved branch/dependency discrepancies. Preserve those as unresolved. Do not use this ingestion package to rewrite the CURRENT cursor, delivery ledger, manifests, hashes, or canon.

## Requirements

- Python 3.10+
- Git installed and the repository cloned locally
- Access to both selected branches
- A Google Gemini API key with Gemini API access
- Current Google Gen AI Python SDK

Install:

```bash
python -m pip install --upgrade google-genai
```

Set the API key in the shell:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

## Run the complete ingestion

From the repository root:

```bash
python tools/ai_studio_full_corpus_ingest.py \
  --repo-dir . \
  --branches main cutover/s7ns-authoritative-20261031 \
  --store-display-name "S7NS Full Source Library"
```

The script creates a new File Search store and indexes all eligible UTF-8 text blobs from both branches. It does not overwrite or delete an existing store. Save the printed store name and the generated `S7NS_FILE_SEARCH_INGESTION_REPORT.json`.

If the run reports INCOMPLETE, do not treat the store as complete. Resolve each reported failure or skipped item and rerun into a fresh store. The report is written locally and is not automatically committed to GitHub.

## Connect the store to Gemini

Use the store name printed by the script in a Gemini API / Interactions request with the File Search tool. The selected model must support File Search. Google's current documentation lists Gemini 3.8 Flash among supported models.

Example Python:

```python
from google import genai

client = genai.Client()
store_name = "fileSearchStores/REPLACE_WITH_YOUR_STORE_ID"

response = client.interactions.create(
    model="gemini-3.8-flash",
    input=(
        "You have access to the complete indexed S7NS source library. "
        "Search the full corpus before answering. Cite the source files used. "
        "Keep branch provenance visible and do not silently reconcile conflicts. "
        "If a requested fact is not supported by retrieved sources, say "
        "'Data not established: [Topic].' Distinguish source facts, proposals, "
        "prepared work, delivered work, and author-accepted work."
    ),
    tools=[{
        "type": "file_search",
        "file_search_store_names": [store_name],
    }],
)

for step in response.steps:
    if step.type == "model_output":
        for block in step.content:
            if block.type == "text":
                print(block.text)
                if block.annotations:
                    for annotation in block.annotations:
                        if annotation.type == "file_citation":
                            print("SOURCE:", annotation.file_name, annotation.source)
```

This is the persistent API-backed retrieval route. A plain AI Studio chat attachment is not automatically connected to a File Search store; use an AI Studio/API workflow that supports the File Search tool and pass the store name on requests.

## First verification prompt

After the store is built, ask Gemini:

```text
Audit the S7NS File Search library before doing creative work.

1. Report every indexed branch and commit represented in the ingestion report.
2. Identify the number of imported text files per branch.
3. Search for AI_STUDIO_START_HERE.md, KAZE_READ_FIRST.txt, AGENTS.md,
   CURRENT.json, DELIVERY_LEDGER.json, SEASON3_ACTIVE_OUTLINE.json,
   CAPABILITY_ROUTER.yaml, LOGICAL_PHYSICAL_SOURCE_MAP.json,
   MASTER_SOURCE_INDEX.json, ACCESS_INDEX.json, and MANIFEST.yaml.
4. Report which are present on each branch, citing the actual source files.
5. Identify duplicate paths with different contents and files present on only
   one branch. Do not resolve the differences.
6. State which source files could not be indexed, if any.
7. Do not claim that the corpus is complete unless the ingestion report and
   source coverage support that claim.
```

## Limits and integrity

- Gemini File Search has a per-document size limit of 100 MB. The script reports any source larger than this instead of silently truncating it.
- File Search store capacity depends on the Google AI project tier. A capacity or API failure is recorded as an ingestion failure.
- File Search uses chunking and retrieval. It does not guarantee that every chunk is returned for every query.
- Audio and video are not indexed by this text-only script. Binary files are listed in the report as skipped. They require a separate supported ingestion path.
- The script indexes Git-tracked files only. Untracked local files are not included.
- The script never writes to the source branches or modifies repository files.
- Google File Search citations identify retrieved source material; they do not establish author acceptance or resolve conflicting authority.

## Official Google documentation

- File Search: https://ai.google.dev/gemini-api/docs/file-search
- Files API: https://ai.google.dev/gemini-api/docs/files
- File input methods: https://ai.google.dev/gemini-api/docs/file-input-methods

## Authority note

This is an additive technical retrieval layer only. Existing S7NS source authority, latest direct author decisions, live state, delivery records, and complete source owners remain controlling. Historical sources remain historical evidence. Retrieval does not merge branches, advance fictional time, authorize PLAY, or convert any proposal or delivery into author acceptance.
