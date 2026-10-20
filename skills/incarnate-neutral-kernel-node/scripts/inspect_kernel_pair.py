#!/usr/bin/env python3
"""Read-only source, receiving-node and pending port-state inspection."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout.strip()


def revision_exists(repo: Path, revision: str | None) -> bool:
    if not revision:
        return False
    result = subprocess.run(
        ["git", "-C", str(repo), "cat-file", "-e", f"{revision}^{{commit}}"],
        check=False,
        capture_output=True,
    )
    return result.returncode == 0


def tree_identity(repo: Path, scoped_root: str | None) -> str:
    revision = f"HEAD:{scoped_root}" if scoped_root else "HEAD^{tree}"
    return git(repo, "rev-parse", revision)


def repository_state(
    repo: Path, identity: dict[str, Any], scoped_root: str | None
) -> dict[str, Any]:
    head = git(repo, "rev-parse", "HEAD")
    tree = tree_identity(repo, scoped_root)
    branch = git(repo, "branch", "--show-current")
    status = git(repo, "status", "--short")
    assessed_head = identity["assessed_repository_head"]
    assessed_tree = identity["assessed_tree"]
    state: dict[str, Any] = {
        "path": str(repo),
        "scope": scoped_root or ".",
        "head": head,
        "tree": tree,
        "branch": branch,
        "clean": not bool(status),
        "status": status.splitlines() if status else [],
        "assessed_repository_head": assessed_head,
        "assessed_tree": assessed_tree,
        "repository_changed_since_assessment": head != assessed_head,
        "tree_changed_since_assessment": tree != assessed_tree,
        "changed_paths_since_assessment": [],
        "commits_since_assessment": [],
    }
    if head != assessed_head and revision_exists(repo, assessed_head):
        path_args = ["--", scoped_root] if scoped_root else []
        changed = git(repo, "diff", "--name-only", f"{assessed_head}..{head}", *path_args)
        log = git(
            repo,
            "log",
            "--format=%H%x09%s",
            f"{assessed_head}..{head}",
            *path_args,
        )
        state["changed_paths_since_assessment"] = changed.splitlines() if changed else []
        state["commits_since_assessment"] = log.splitlines() if log else []
    elif head != assessed_head:
        state["comparison_unavailable"] = "assessed repository head is not present locally"

    if head != assessed_head and tree == assessed_tree:
        state["repository_only_drift"] = (
            "repository head changed but the relevant tree did not; do not reopen "
            "this source relation from unrelated repository noise"
        )
    return state


def mapped_path_coverage(
    workspace: Path, port_map: dict[str, Any]
) -> dict[str, list[str]]:
    source_repo = workspace / port_map["source"]["local_repo"]
    destination_repo = workspace / port_map["destination"]["local_repo"]
    missing_source: list[str] = []
    missing_destination: list[str] = []
    for owner in port_map["owner_map"]:
        for relative in owner.get("source_paths", []):
            local_relative = Path(relative)
            if port_map["source"].get("root") and local_relative.parts[0] == port_map["source"]["root"]:
                local_relative = Path(*local_relative.parts[1:])
                candidate = source_repo / port_map["source"]["root"] / local_relative
            else:
                candidate = source_repo / local_relative
            if not candidate.exists():
                missing_source.append(relative)
        for relative in owner.get("current_destination_paths", []):
            if not (destination_repo / relative).exists():
                missing_destination.append(relative)
    return {
        "missing_source_paths": sorted(set(missing_source)),
        "missing_current_destination_paths": sorted(set(missing_destination)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Inspect source and receiving-node identities, relevant trees, "
            "mapped owners and pending port states without mutation."
        )
    )
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--map", type=Path, required=True)
    args = parser.parse_args()
    map_path = args.map.resolve()
    port_map = json.loads(map_path.read_text(encoding="utf-8-sig"))
    if port_map.get("schema") != "maios.neutral-kernel-port-map.v1":
        raise SystemExit("unsupported port-map schema")
    workspace = args.workspace.resolve()

    source = port_map["source"]
    destination = port_map["destination"]
    source_repo = workspace / source["local_repo"]
    destination_repo = workspace / destination["local_repo"]
    for repo in (source_repo, destination_repo):
        if not (repo / ".git").exists():
            raise SystemExit(f"repository not found: {repo}")

    source_state = repository_state(source_repo, source, source.get("root"))
    destination_state = repository_state(destination_repo, destination, None)
    pending_relations = [
        {
            "id": relation["id"],
            "disposition": relation["disposition"],
            "lifecycle": relation["lifecycle"],
            "target_owner": relation["target_owner"],
        }
        for relation in port_map["relation_states"]
        if relation["lifecycle"] == "assessed_not_integrated"
    ]
    version_path = destination_repo / "VERSION"
    port_state = port_map["port_state"]
    if source_state["tree_changed_since_assessment"]:
        next_action = (
            "assess the changed source owners, reconcile any superseding delta "
            "with the preserved pending destination relations, then continue "
            "destination implementation"
        )
    elif destination_state["tree_changed_since_assessment"]:
        next_action = (
            "reread the changed destination owners, reconcile them with the "
            "preserved pending relations, then continue destination implementation"
        )
    elif pending_relations:
        next_action = (
            "continue pending destination implementation even if the source tree "
            "is unchanged; reopen source assessment only if a relevant source "
            "tree delta or superseding relation appears"
        )
    else:
        next_action = "no pending integration and no relevant source-tree delta"

    report = {
        "schema": "maios.neutral-kernel-pair-inspection.v1",
        "map": str(map_path),
        "source": source_state,
        "destination": destination_state,
        "destination_version": (
            version_path.read_text(encoding="utf-8").strip()
            if version_path.exists()
            else None
        ),
        "port_state": port_state,
        "pending_relations": pending_relations,
        "mapped_path_coverage": mapped_path_coverage(workspace, port_map),
        "next_action": next_action,
        "semantic_boundary": (
            "identity and path deltas are freshness evidence only; assessed, "
            "implemented, structurally verified, host exercised and assimilated "
            "remain distinct states"
        ),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
