#!/usr/bin/env python3
"""Validate an evidence-bound source/runtime effect request without side effects."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SCHEMA_ID = "dnd.effect-request.v1"
DECISION_SCHEMA_ID = "dnd.effect-request-decision.v1"
REVISION_LENGTH = 40
EFFECT_CONTRACTS = {
    "source_push": (True, False, False),
    "production_bound_push": (True, False, True),
    "runtime_activation": (False, True, True),
    "combined_release": (True, True, True),
}
REQUIRED_TERMINAL_CHECKS = {
    "checkout_revision",
    "service_health",
    "public_identity",
    "destination_behavior",
}
SCHEMA_PATH = Path(__file__).resolve().parents[1] / "references" / "effect-request.schema.json"


def _is_revision(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == REVISION_LENGTH
        and all(character in "0123456789abcdefABCDEF" for character in value)
    )


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _read_schema_validate(request: dict[str, Any]) -> None:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.validate(request, schema)


def _shape_validate(request: dict[str, Any]) -> None:
    if request.get("schema") != SCHEMA_ID:
        raise ValueError(f"schema must be {SCHEMA_ID}")
    required = {
        "request_id",
        "created_at",
        "effect",
        "operator_selection",
        "source",
        "validation",
        "runtime",
        "security",
        "receipt",
    }
    missing = sorted(required - set(request))
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))
    if not _nonempty_string(request["request_id"]):
        raise ValueError("request_id must be a non-empty string")
    try:
        datetime.fromisoformat(str(request["created_at"]).replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("created_at must be an ISO-8601 timestamp") from exc
    _read_schema_validate(request)


def _check(
    checks: list[dict[str, str]],
    blockers: list[str],
    check_id: str,
    condition: bool,
    success: str,
    failure: str,
) -> None:
    checks.append(
        {
            "id": check_id,
            "status": "pass" if condition else "fail",
            "detail": success if condition else failure,
        }
    )
    if not condition:
        blockers.append(f"{check_id}: {failure}")


def validate_effect_request(request: dict[str, Any]) -> dict[str, Any]:
    _shape_validate(request)
    checks: list[dict[str, str]] = []
    blockers: list[str] = []
    decisions_needed: list[str] = []
    declared_limits: list[str] = []

    effect = request["effect"]
    operator = request["operator_selection"]
    source = request["source"]
    validation = request["validation"]
    runtime = request["runtime"]
    security = request["security"]
    receipt = request["receipt"]

    kind = effect.get("kind")
    expected_contract = EFFECT_CONTRACTS.get(kind)
    actual_contract = (
        effect.get("source_publication"),
        effect.get("runtime_activation"),
        effect.get("production_bound"),
    )
    _check(
        checks,
        blockers,
        "effect.contract",
        expected_contract is not None and actual_contract == expected_contract,
        f"{kind} has a coherent effect boundary",
        "effect flags do not match the declared effect kind",
    )
    batch_policy = effect.get("batch_policy")
    policy_evidence = effect.get("policy_evidence")
    batch_policy_coherent = (
        kind == "combined_release" and batch_policy == "combined_adopted"
    ) or (
        kind != "combined_release" and batch_policy == "single_effect"
    )
    _check(
        checks,
        blockers,
        "effect.batch_policy",
        batch_policy_coherent and _nonempty_string(policy_evidence),
        "the effect batch matches an explicit owner policy",
        "a combined release requires an adopted combined policy; other requests must contain one effect",
    )

    local_revision = source.get("local_revision")
    _check(
        checks,
        blockers,
        "source.identity",
        _is_revision(local_revision) and _is_revision(source.get("local_tree")),
        "local commit and tree are immutable Git identities",
        "local_revision and local_tree must be exact 40-character Git identities",
    )
    _check(
        checks,
        blockers,
        "source.diff",
        bool(source.get("diff_reviewed"))
        and bool(source.get("scoped_paths"))
        and _nonempty_string(source.get("diff_review_evidence")),
        "the reviewed payload has an explicit path boundary and evidence",
        "the diff must be reviewed with scoped paths and evidence",
    )
    excluded_dirty = source.get("excluded_dirty_paths") or []
    _check(
        checks,
        blockers,
        "source.concurrent_work",
        not excluded_dirty or bool(source.get("excluded_paths_preserved")),
        "concurrent dirty paths are absent or explicitly preserved outside the payload",
        "excluded dirty paths are not proved preserved",
    )

    remote_targets = source.get("remote_targets") or []
    remote_targets_coherent = True
    production_target_selected = False
    for target in remote_targets:
        remote_targets_coherent = remote_targets_coherent and all(
            [
                _nonempty_string(target.get("branch")),
                target.get("role") in {"candidate", "production"},
                _is_revision(target.get("observed_revision")),
                _is_revision(target.get("expected_revision")),
                target.get("observed_revision") == target.get("expected_revision"),
                isinstance(target.get("will_update"), bool),
            ]
        )
        if target.get("role") == "production" and target.get("will_update"):
            production_target_selected = True
    if effect.get("source_publication"):
        remote_targets_coherent = bool(remote_targets) and remote_targets_coherent and any(
            target.get("will_update") for target in remote_targets
        )
    remote_auth_coherent = (
        bool(source.get("authenticated_remote_verified"))
        if remote_targets or effect.get("source_publication")
        else not bool(source.get("authenticated_remote_verified"))
    )
    _check(
        checks,
        blockers,
        "source.remote_refs",
        remote_targets_coherent
        and remote_auth_coherent
        and _nonempty_string(source.get("remote_verification_evidence")),
        "remote refs match their locked identities, or are explicitly not applicable to a local-only runtime effect",
        "remote refs are missing, stale, inconsistently authenticated or incompatible with the effect boundary",
    )
    _check(
        checks,
        blockers,
        "source.ancestry",
        bool(source.get("ancestry_verified"))
        and _nonempty_string(source.get("ancestry_evidence")),
        "the target revision is proven to extend the selected remote bases",
        "fast-forward ancestry is not evidenced",
    )
    if effect.get("production_bound") and effect.get("source_publication"):
        _check(
            checks,
            blockers,
            "source.production_target",
            production_target_selected,
            "a production source target is explicitly included",
            "the production-bound movement does not name a production source target",
        )
    _check(
        checks,
        blockers,
        "source.consumer",
        not effect.get("production_bound")
        or (
            bool(source.get("production_consumer_known"))
            and _nonempty_string(source.get("production_consumer_evidence"))
        ),
        "the production consumer is known or not applicable",
        "a production-bound effect lacks a verified consumer map",
    )

    failed_checks = validation.get("failed_checks") or []
    in_scope_failures = [
        item
        for item in failed_checks
        if item.get("classification") != "preexisting_out_of_scope"
    ]
    validation_coherent = (
        validation.get("status") == "pass"
        or (
            validation.get("status") == "partial"
            and bool(validation.get("passed_checks"))
            and not in_scope_failures
            and bool(failed_checks)
        )
    )
    _check(
        checks,
        blockers,
        "validation.scope",
        validation_coherent,
        "all in-scope checks pass; any declared failure is pre-existing and out of scope",
        "validation has an in-scope or unclassified failure",
    )
    declared_limits.extend(
        f"{item.get('id')}: {item.get('evidence')}" for item in failed_checks
    )

    security_conditions = [
        bool(security.get("credential_locality_preserved")),
        bool(security.get("noninteractive_auth")),
        bool(security.get("secrets_redacted")),
        not bool(security.get("candidate_code_runs_privileged")),
        not bool(security.get("force_push")),
        not bool(security.get("destructive_history")),
        _nonempty_string(security.get("credential_policy_source")),
        _nonempty_string(security.get("credential_evidence")),
    ]
    _check(
        checks,
        blockers,
        "security.boundary",
        all(security_conditions),
        "credential locality, least privilege and non-destructive history are preserved",
        "credential, privilege, secret or history safety is not proved",
    )

    if effect.get("runtime_activation"):
        runtime_present = isinstance(runtime, dict)
        _check(
            checks,
            blockers,
            "runtime.contract",
            runtime_present,
            "runtime activation has an explicit target contract",
            "runtime_activation requires a runtime object",
        )
        if runtime_present:
            current_revision = runtime.get("current_revision")
            target_revision = runtime.get("target_revision")
            rollback_revision = runtime.get("rollback_revision")
            _check(
                checks,
                blockers,
                "runtime.identity",
                _is_revision(current_revision)
                and _is_revision(target_revision)
                and target_revision == local_revision
                and _nonempty_string(runtime.get("identity_evidence")),
                "runtime current and target revisions are exact and target the reviewed source",
                "runtime identities are missing or the target differs from the reviewed source",
            )
            _check(
                checks,
                blockers,
                "runtime.source_first",
                bool(runtime.get("source_first_path"))
                and not bool(runtime.get("runtime_drift"))
                and not bool(runtime.get("direct_runtime_edit")),
                "activation preserves one source-first causal chain",
                "runtime drift or a direct-edit path would break source ownership",
            )
            allowlist = set(runtime.get("service_allowlist") or [])
            restart_set = set(runtime.get("services_to_restart") or [])
            active_set = set(runtime.get("services_currently_active") or [])
            successful_oneshot_set = set(
                runtime.get("services_currently_successful_oneshot") or []
            )
            _check(
                checks,
                blockers,
                "runtime.services",
                bool(allowlist)
                and restart_set.issubset(allowlist)
                and allowlist.issubset(active_set | successful_oneshot_set),
                "restart scope is bounded and every service is active or a successful oneshot",
                "service restart scope exceeds the allowlist or current service state is incomplete",
            )
            _check(
                checks,
                blockers,
                "runtime.rollback",
                _is_revision(rollback_revision)
                and rollback_revision != target_revision
                and bool(runtime.get("rollback_available"))
                and bool(runtime.get("rollback_independent"))
                and _nonempty_string(runtime.get("rollback_evidence")),
                "an independent previous revision and restore path are locked",
                "rollback identity is absent, identical to target or not independently proved",
            )
            terminal_checks = set(runtime.get("terminal_checks") or [])
            _check(
                checks,
                blockers,
                "runtime.terminal_proof",
                REQUIRED_TERMINAL_CHECKS.issubset(terminal_checks)
                and bool(runtime.get("unchanged_surfaces")),
                "terminal identity, health, public behavior and unchanged surfaces are planned",
                "terminal proof or unchanged-surface checks are incomplete",
            )
    else:
        _check(
            checks,
            blockers,
            "runtime.not_applicable",
            runtime is None,
            "no runtime mutation is included",
            "a runtime object is present although runtime activation is outside the effect",
        )

    _check(
        checks,
        blockers,
        "receipt.boundary",
        _nonempty_string(receipt.get("owner")) and _nonempty_string(receipt.get("path")),
        "the terminal receipt has an owner and durable path",
        "receipt owner or path is missing",
    )

    if effect.get("source_publication") and not operator.get("covers_source_publication"):
        decisions_needed.append("select the source publication outcome")
    if effect.get("runtime_activation") and not operator.get("covers_runtime_activation"):
        decisions_needed.append("select the runtime activation outcome")
    if not _nonempty_string(operator.get("outcome")) or not _nonempty_string(operator.get("source")):
        decisions_needed.append("identify the operator-selected outcome and its source")

    technical_status = "coherent" if not blockers else "incoherent"
    if blockers:
        status = "blocked"
        next_action = "resolve the listed technical contradictions with read-only evidence"
    elif decisions_needed:
        status = "needs_operator_decision"
        next_action = "ask one plain-language outcome question covering only the missing effect"
    else:
        status = "ready"
        next_action = "submit the locked effect request to the platform gate and execute only that batch"

    target_branches = [
        target["branch"] for target in remote_targets if target.get("will_update")
    ]
    runtime_summary = None
    if isinstance(runtime, dict):
        runtime_summary = {
            "host": runtime.get("host"),
            "path": runtime.get("path"),
            "current_revision": runtime.get("current_revision"),
            "target_revision": runtime.get("target_revision"),
            "services_to_restart": runtime.get("services_to_restart"),
            "rollback_revision": runtime.get("rollback_revision"),
            "unchanged_surfaces": runtime.get("unchanged_surfaces"),
        }
    canonical = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    request_digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    platform_message = (
        f"Effetto {kind} sul repository {source.get('repository')} alla revisione "
        f"{str(local_revision)[:12]}; branch {', '.join(target_branches) or 'nessuno'}"
    )
    if runtime_summary:
        platform_message += (
            f"; runtime {runtime_summary['host']}:{runtime_summary['path']} da "
            f"{str(runtime_summary['current_revision'])[:12]} a "
            f"{str(runtime_summary['target_revision'])[:12]}; restart "
            f"{', '.join(runtime_summary['services_to_restart'] or []) or 'nessuno'}; rollback "
            f"{str(runtime_summary['rollback_revision'])[:12]}"
        )
    platform_message += ". Le superfici non nominate restano invariate."

    return {
        "schema": DECISION_SCHEMA_ID,
        "request_id": request["request_id"],
        "request_digest": request_digest,
        "status": status,
        "technical_status": technical_status,
        "operator_decision_status": "covered" if not decisions_needed else "missing",
        "checks": checks,
        "blockers": blockers,
        "decisions_needed": decisions_needed,
        "declared_limits": declared_limits,
        "locked_effect": {
            "kind": kind,
            "repository": source.get("repository"),
            "revision": local_revision,
            "target_branches": target_branches,
            "runtime": runtime_summary,
        },
        "platform_gate": {
            "expected": bool(effect.get("production_bound")),
            "message": platform_message,
        },
        "next_legal_action": next_action,
        "side_effect_performed": False,
    }


def _base_case() -> dict[str, Any]:
    previous = "1" * 40
    target = "2" * 40
    return {
        "schema": SCHEMA_ID,
        "request_id": "maios-release-test",
        "created_at": "2026-08-11T09:00:00+02:00",
        "effect": {
            "kind": "combined_release",
            "source_publication": True,
            "runtime_activation": True,
            "production_bound": True,
            "batch_policy": "combined_adopted",
            "policy_evidence": "owner release contract explicitly adopts one combined source/runtime effect",
        },
        "operator_selection": {
            "outcome": "publish online and hand back the exact surface for testing",
            "source": "operator message",
            "covers_source_publication": True,
            "covers_runtime_activation": True,
        },
        "source": {
            "repository": "example/project",
            "branch": "candidate",
            "local_revision": target,
            "local_tree": "3" * 40,
            "diff_reviewed": True,
            "diff_review_evidence": "cached diff and path list",
            "scoped_paths": ["src/app.py", "tests/test_app.py"],
            "excluded_dirty_paths": ["notes/operator.html"],
            "excluded_paths_preserved": True,
            "remote_targets": [
                {
                    "branch": "candidate",
                    "role": "candidate",
                    "observed_revision": previous,
                    "expected_revision": previous,
                    "will_update": True,
                },
                {
                    "branch": "main",
                    "role": "production",
                    "observed_revision": previous,
                    "expected_revision": previous,
                    "will_update": True,
                },
            ],
            "authenticated_remote_verified": True,
            "remote_verification_evidence": "prompt-free authenticated fetch and ref readback",
            "ancestry_verified": True,
            "ancestry_evidence": "merge-base --is-ancestor for every updated ref",
            "production_consumer_known": True,
            "production_consumer_evidence": "mapped production checkout consumes main",
        },
        "validation": {
            "status": "partial",
            "passed_checks": ["focused tests", "syntax", "diff check"],
            "failed_checks": [
                {
                    "id": "workspace-topology",
                    "classification": "preexisting_out_of_scope",
                    "evidence": "known unrelated audit outside the selected owner",
                }
            ],
        },
        "runtime": {
            "host": "production.example",
            "path": "/opt/project",
            "current_revision": previous,
            "target_revision": target,
            "identity_evidence": "clean checkout and exact HEAD readback",
            "source_first_path": True,
            "runtime_drift": False,
            "direct_runtime_edit": False,
            "service_allowlist": ["project-api"],
            "services_to_restart": ["project-api"],
            "services_currently_active": ["project-api"],
            "services_currently_successful_oneshot": [],
            "rollback_revision": previous,
            "rollback_available": True,
            "rollback_independent": True,
            "rollback_evidence": "previous release remains reachable by the fixed restore path",
            "terminal_checks": sorted(REQUIRED_TERMINAL_CHECKS),
            "unchanged_surfaces": ["nginx", "database"],
        },
        "security": {
            "credential_policy_source": "workspace AGENTS.md",
            "credential_locality_preserved": True,
            "noninteractive_auth": True,
            "secrets_redacted": True,
            "candidate_code_runs_privileged": False,
            "force_push": False,
            "destructive_history": False,
            "credential_evidence": "token loaded in process memory under workspace policy",
        },
        "receipt": {
            "owner": "release owner",
            "path": "process/release-receipt.json",
        },
    }


def _local_runtime_case() -> dict[str, Any]:
    candidate = _base_case()
    candidate["request_id"] = "local-runtime-test"
    candidate["effect"] = {
        "kind": "runtime_activation",
        "source_publication": False,
        "runtime_activation": True,
        "production_bound": True,
        "batch_policy": "single_effect",
        "policy_evidence": "one local-source runtime activation with no remote publication",
    }
    candidate["operator_selection"]["covers_source_publication"] = False
    candidate["source"]["remote_targets"] = []
    candidate["source"]["authenticated_remote_verified"] = False
    candidate["source"]["remote_verification_evidence"] = (
        "not applicable: the selected immutable source repository has no remote target"
    )
    return candidate


def self_test() -> None:
    cases: list[tuple[str, dict[str, Any], str, str | None]] = []
    cases.append(("ready", _base_case(), "ready", None))
    cases.append(("local runtime ready", _local_runtime_case(), "ready", None))

    successful_oneshot = _local_runtime_case()
    successful_oneshot["runtime"]["services_currently_active"] = []
    successful_oneshot["runtime"]["services_currently_successful_oneshot"] = ["project-api"]
    cases.append(("successful oneshot runtime ready", successful_oneshot, "ready", None))

    missing_decision = _base_case()
    missing_decision["operator_selection"]["covers_runtime_activation"] = False
    cases.append(("operator decision", missing_decision, "needs_operator_decision", None))

    missing_combined_policy = _base_case()
    missing_combined_policy["effect"]["batch_policy"] = "single_effect"
    cases.append(
        (
            "combined release without adopted policy",
            missing_combined_policy,
            "blocked",
            "effect.batch_policy",
        )
    )

    stale_ref = _base_case()
    stale_ref["source"]["remote_targets"][0]["observed_revision"] = "4" * 40
    cases.append(("stale remote ref", stale_ref, "blocked", "source.remote_refs"))

    wrong_runtime = _base_case()
    wrong_runtime["runtime"]["target_revision"] = "5" * 40
    cases.append(("wrong runtime target", wrong_runtime, "blocked", "runtime.identity"))

    bad_rollback = _base_case()
    bad_rollback["runtime"]["rollback_revision"] = "2" * 40
    cases.append(("bad rollback", bad_rollback, "blocked", "runtime.rollback"))

    extra_service = _base_case()
    extra_service["runtime"]["services_to_restart"].append("nginx")
    cases.append(("service outside allowlist", extra_service, "blocked", "runtime.services"))

    in_scope_failure = _base_case()
    in_scope_failure["validation"]["failed_checks"][0]["classification"] = "in_scope"
    cases.append(("in-scope failure", in_scope_failure, "blocked", "validation.scope"))

    privileged = _base_case()
    privileged["security"]["candidate_code_runs_privileged"] = True
    cases.append(("privileged candidate", privileged, "blocked", "security.boundary"))

    for name, candidate, expected_status, expected_blocker in cases:
        result = validate_effect_request(candidate)
        if result["status"] != expected_status:
            raise AssertionError(
                f"{name}: expected {expected_status}, got {result['status']}"
            )
        if expected_blocker and not any(
            blocker.startswith(expected_blocker) for blocker in result["blockers"]
        ):
            raise AssertionError(f"{name}: missing blocker {expected_blocker}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print(json.dumps({"self_test": "passed", "cases": 11}, sort_keys=True))
        return 0
    if args.request is None:
        parser.error("request is required unless --self-test is used")
    try:
        request = json.loads(args.request.read_text(encoding="utf-8"))
        if not isinstance(request, dict):
            raise ValueError("request root must be an object")
        print(json.dumps(validate_effect_request(request), ensure_ascii=False, indent=2))
    except Exception as exc:  # CLI boundary: always emit a compact machine-readable error.
        print(json.dumps({"status": "invalid", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
