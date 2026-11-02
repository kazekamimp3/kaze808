#!/usr/bin/env python3
"""Index all UTF-8 text blobs from selected S7NS Git branches into Gemini File Search.

Original Git objects are read only. Each indexed document receives a provenance
header; no source file or branch is modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

from google import genai

DEFAULT_BRANCHES = ["main", "cutover/s7ns-authoritative-20261031"]
REPORT_NAME = "S7NS_FILE_SEARCH_INGESTION_REPORT.json"


def git(repo: Path, *args: str, check: bool = True) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        raise RuntimeError(
            f"git {' '.join(args)} failed: "
            + result.stderr.decode("utf-8", errors="replace").strip()
        )
    return result.stdout


def branch_commit(repo: Path, branch: str) -> str:
    return git(repo, "rev-parse", "--verify", f"{branch}^{{commit}}").decode().strip()


def tracked_paths(repo: Path, branch: str) -> list[str]:
    raw = git(repo, "ls-tree", "-r", "-z", "--name-only", branch)
    return [p.decode("utf-8", errors="strict") for p in raw.split(b"\0") if p]


def read_blob(repo: Path, branch: str, path: str) -> bytes:
    return git(repo, "show", f"{branch}:{path}")


def is_text_blob(data: bytes) -> bool:
    if b"\x00" in data:
        return False
    try:
        data.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def wait_for_operation(client: Any, operation: Any) -> Any:
    while not getattr(operation, "done", False):
        time.sleep(3)
        operation = client.operations.get(operation)
    error = getattr(operation, "error", None)
    if error:
        raise RuntimeError(str(error))
    return operation


def upload_text(
    client: Any,
    store_name: str,
    display_name: str,
    text: str,
) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".txt", delete=False
    ) as handle:
        handle.write(text)
        temp_path = handle.name
    try:
        operation = client.file_search_stores.upload_to_file_search_store(
            file=temp_path,
            file_search_store_name=store_name,
            config={"display_name": display_name[:512]},
        )
        wait_for_operation(client, operation)
    finally:
        Path(temp_path).unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Index complete text corpora from one or more Git branches."
    )
    parser.add_argument("--repo-dir", default=".", help="Local S7NS Git repository")
    parser.add_argument(
        "--branches", nargs="+", default=DEFAULT_BRANCHES,
        help="Git refs to index separately (default: main and Oct 31 cutover)",
    )
    parser.add_argument(
        "--store-display-name", default="S7NS Full Source Library",
        help="Display name for the new Gemini File Search store",
    )
    parser.add_argument(
        "--report", default=REPORT_NAME, help="Local JSON ingestion report path"
    )
    args = parser.parse_args()

    repo = Path(args.repo_dir).resolve()
    if not (repo / ".git").exists():
        print(f"ERROR: {repo} is not a Git working tree.", file=sys.stderr)
        return 2
    if not os.environ.get("GEMINI_API_KEY"):
        print("ERROR: GEMINI_API_KEY is not set.", file=sys.stderr)
        return 2

    client = genai.Client()
    store = client.file_search_stores.create(
        config={
            "display_name": args.store_display_name,
            "embedding_model": "models/gemini-embedding-2",
        }
    )
    store_name = store.name

    report: dict[str, Any] = {
        "status": "RUNNING",
        "store_name": store_name,
        "store_display_name": args.store_display_name,
        "embedding_model": "models/gemini-embedding-2",
        "branches": {},
        "imported": [],
        "skipped_non_text": [],
        "failures": [],
        "notes": [
            "Branch snapshots are indexed separately; no merge or authority resolution is performed.",
            "Indexed copies include provenance headers; Git source blobs remain unchanged.",
            "File Search retrieval does not guarantee every indexed chunk is returned for every query.",
        ],
    }

    for branch in args.branches:
        try:
            commit = branch_commit(repo, branch)
            paths = tracked_paths(repo, branch)
        except Exception as exc:
            report["failures"].append(
                {"branch": branch, "path": None, "error": str(exc)}
            )
            continue

        report["branches"][branch] = {
            "commit": commit,
            "tracked_path_count": len(paths),
        }

        for path in paths:
            try:
                data = read_blob(repo, branch, path)
                if not is_text_blob(data):
                    report["skipped_non_text"].append(
                        {"branch": branch, "commit": commit, "path": path,
                         "bytes": len(data), "reason": "Not valid UTF-8 text or contains NUL"}
                    )
                    continue

                source_text = data.decode("utf-8")
                source_sha256 = hashlib.sha256(data).hexdigest()
                provenance = (
                    "S7NS SOURCE PROVENANCE\n"
                    f"branch: {branch}\n"
                    f"commit: {commit}\n"
                    f"path: {path}\n"
                    f"source_sha256: {source_sha256}\n"
                    "The source content begins after this header. "
                    "Treat this branch snapshot as distinct from other branch snapshots.\n"
                    "----- BEGIN ORIGINAL SOURCE CONTENT -----\n"
                )
                indexed_text = provenance + source_text
                # Google File Search limit is 100 MB per document. Keep a safety margin.
                if len(indexed_text.encode("utf-8")) >= 90 * 1024 * 1024:
                    report["failures"].append(
                        {"branch": branch, "path": path,
                         "error": "Text blob exceeds the script's 90 MiB safety ceiling; split deliberately before ingesting."}
                    )
                    continue

                display_name = f"{branch}__{path}"
                upload_text(client, store_name, display_name, indexed_text)
                report["imported"].append(
                    {"branch": branch, "commit": commit, "path": path,
                     "source_sha256": source_sha256, "bytes": len(data),
                     "display_name": display_name[:512]}
                )
                print(f"INDEXED [{branch}] {path}")
            except Exception as exc:
                report["failures"].append(
                    {"branch": branch, "commit": commit, "path": path,
                     "error": str(exc)}
                )
                print(f"FAILED  [{branch}] {path}: {exc}", file=sys.stderr)

    report["status"] = (
        "COMPLETE"
        if not report["failures"] and not report["skipped_non_text"]
        else "INCOMPLETE"
    )
    report["summary"] = {
        "branch_count": len(report["branches"]),
        "imported_text_files": len(report["imported"]),
        "skipped_non_text_files": len(report["skipped_non_text"]),
        "failed_files": len(report["failures"]),
    }

    report_path = Path(args.report).resolve()
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print("\n" + json.dumps({
        "status": report["status"],
        "store_name": store_name,
        **report["summary"],
        "report": str(report_path),
    }, indent=2))
    return 0 if report["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
