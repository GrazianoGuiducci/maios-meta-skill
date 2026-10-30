#!/usr/bin/env python3
"""Reduce observed release facts to one next legal action without side effects."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED = {
    "source_owner_known": bool,
    "release_owner_known": bool,
    "production_consumer_known": bool,
    "remote_verified_authenticated": bool,
    "source_diff_reviewed": bool,
    "validation_passed": bool,
    "push_effect": str,
    "source_publication_authorized": bool,
    "runtime_activation_authorized": bool,
    "validator_executes_candidate_code_as_privileged": bool,
    "runtime_drift": bool,
    "rollback_proved": bool,
    "live_identity_verified": bool,
    "human_acceptance_verified": bool,
}

PUSH_EFFECTS = {"local_source", "source_remote_only", "production_bound_push"}


def validate_context(context: dict[str, Any]) -> None:
    missing = sorted(set(REQUIRED) - set(context))
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))
    for field, expected in REQUIRED.items():
        if not isinstance(context[field], expected):
            raise ValueError(f"{field} must be {expected.__name__}")
    if context["push_effect"] not in PUSH_EFFECTS:
        raise ValueError("push_effect must be one of: " + ", ".join(sorted(PUSH_EFFECTS)))
    for optional in ("production_source_matches_candidate", "runtime_matches_production_source"):
        if optional in context and context[optional] is not None and not isinstance(context[optional], bool):
            raise ValueError(f"{optional} must be boolean or null")


def decision(classification: str, next_action: str, gate: str | None, reason: str) -> dict[str, Any]:
    return {
        "classification": classification,
        "next_legal_action": next_action,
        "effect_gate": gate,
        "reason": reason,
        "side_effect_performed": False,
    }


def reduce_state(context: dict[str, Any]) -> dict[str, Any]:
    validate_context(context)

    if context["validator_executes_candidate_code_as_privileged"]:
        return decision(
            "stop_security",
            "separate unprivileged validation from the fixed privileged activator",
            None,
            "candidate-controlled code would execute with elevated privilege",
        )

    remote_identity_required = context["push_effect"] != "local_source"
    if (
        not context["source_owner_known"]
        or not context["release_owner_known"]
        or not context["production_consumer_known"]
        or (remote_identity_required and not context["remote_verified_authenticated"])
    ):
        return decision(
            "observe_only",
            "resolve owners, production consumer and any applicable authenticated remote identity",
            None,
            "the source-to-runtime graph is incomplete",
        )

    if context["runtime_drift"]:
        return decision(
            "stop_drift",
            "preserve drift evidence and reconcile the accepted change in source before runtime mutation",
            None,
            "runtime differs from its owning source",
        )

    if not context["source_diff_reviewed"] or not context["validation_passed"]:
        return decision(
            "prepare_source",
            "review the exact source boundary and complete least-privileged validation",
            None,
            "the candidate is not yet a validated source movement",
        )

    if context["push_effect"] != "local_source" and not context["source_publication_authorized"]:
        return decision(
            "await_source_gate",
            "request authorization for the exact source publication effect",
            context["push_effect"],
            "validated local source does not grant remote publication",
        )

    production_matches = context.get("production_source_matches_candidate")
    if context["push_effect"] != "local_source" and production_matches is not True:
        return decision(
            "publish_source",
            "perform only the authorized source movement and verify the resulting remote revision",
            context["push_effect"],
            "the production source does not yet identify the validated candidate",
        )

    runtime_matches = context.get("runtime_matches_production_source")
    if runtime_matches is not True:
        if not context["rollback_proved"]:
            return decision(
                "stop_recovery",
                "prove an independent previous-release restore path",
                None,
                "runtime activation lacks an independent rollback proof",
            )
        if not context["runtime_activation_authorized"]:
            return decision(
                "await_runtime_gate",
                "request authorization for the exact runtime activation",
                "runtime_activation",
                "source publication and runtime activation are distinct effects",
            )
        return decision(
            "activate_runtime",
            "activate the immutable validated release through the fixed activator and verify rollback readiness",
            "runtime_activation",
            "production source is selected but runtime identity has not advanced",
        )

    if not context["live_identity_verified"]:
        return decision(
            "verify_terminal",
            "verify service, ingress and destination behavior against the exact runtime identity",
            None,
            "matching source and runtime do not prove the live destination",
        )

    if not context["human_acceptance_verified"]:
        return decision(
            "await_acceptance",
            "obtain human acceptance tied to the verified live identity",
            None,
            "technical reconciliation is not operator acceptance",
        )

    return decision(
        "complete",
        "write terminal receipts and assess one bounded learning delta",
        None,
        "source, runtime, live behavior and acceptance are reconciled",
    )


def _base_case() -> dict[str, Any]:
    return {
        "source_owner_known": True,
        "release_owner_known": True,
        "production_consumer_known": True,
        "remote_verified_authenticated": True,
        "source_diff_reviewed": True,
        "validation_passed": True,
        "push_effect": "production_bound_push",
        "source_publication_authorized": False,
        "runtime_activation_authorized": False,
        "validator_executes_candidate_code_as_privileged": False,
        "runtime_drift": False,
        "rollback_proved": True,
        "production_source_matches_candidate": False,
        "runtime_matches_production_source": False,
        "live_identity_verified": False,
        "human_acceptance_verified": False,
    }


def self_test() -> None:
    cases: list[tuple[dict[str, Any], str]] = []
    case = _base_case()
    cases.append((case, "await_source_gate"))

    case = _base_case()
    case["validator_executes_candidate_code_as_privileged"] = True
    cases.append((case, "stop_security"))

    case = _base_case()
    case["runtime_drift"] = True
    cases.append((case, "stop_drift"))

    case = _base_case()
    case.update(
        source_publication_authorized=True,
        production_source_matches_candidate=True,
        runtime_matches_production_source=False,
    )
    cases.append((case, "await_runtime_gate"))

    case = _base_case()
    case.update(
        source_publication_authorized=True,
        runtime_activation_authorized=True,
        production_source_matches_candidate=True,
        runtime_matches_production_source=True,
        live_identity_verified=True,
        human_acceptance_verified=True,
    )
    cases.append((case, "complete"))

    case = _base_case()
    case.update(
        remote_verified_authenticated=False,
        push_effect="local_source",
        source_publication_authorized=False,
        runtime_activation_authorized=True,
        production_source_matches_candidate=None,
        runtime_matches_production_source=True,
        live_identity_verified=True,
        human_acceptance_verified=True,
    )
    cases.append((case, "complete"))

    for index, (candidate, expected) in enumerate(cases, start=1):
        actual = reduce_state(candidate)["classification"]
        if actual != expected:
            raise AssertionError(f"case {index}: expected {expected}, got {actual}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print(json.dumps({"self_test": "passed", "cases": 6}, sort_keys=True))
        return 0
    if args.context is None:
        parser.error("context is required unless --self-test is used")

    try:
        context = json.loads(args.context.read_text(encoding="utf-8"))
        if not isinstance(context, dict):
            raise ValueError("context root must be an object")
        print(json.dumps(reduce_state(context), indent=2, sort_keys=True))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
