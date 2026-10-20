#!/usr/bin/env python3
"""Deterministic append-only reducer for material D-ND work continuity."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


STATE_SCHEMA = "dnd.material_work_continuity.state.v1"
EVENT_SCHEMA = "dnd.material_work_continuity.event.v1"
EVENT_KINDS = {
    "source_event",
    "assistant_projection",
    "verified_movement",
    "retraction_or_supersession",
    "authority_change",
    "unknown_change",
    "relation_checkpoint",
}
SOURCE_PROVENANCE = {
    "direct_operator",
    "owner_source",
    "operator_submitted_uncertain_authorship",
}
STATE_KEYS = {
    "schema",
    "version",
    "owner_surface",
    "owner_state_ref",
    "authority_initial",
    "authority_current",
    "events",
    "active_event_ids",
    "superseded_event_ids",
    "unknowns",
    "current_relation",
    "next_legal_action",
    "reopen_condition",
    "finite_state",
    "previous_digest",
    "state_digest",
}
EVENT_KEYS = {
    "schema",
    "event_id",
    "event_kind",
    "owner_surface",
    "previous_state_digest",
    "payload",
}
PAYLOAD_KEYS = {
    "source_event": {
        "provenance_class",
        "source_ref",
        "exact_text",
        "source_digest",
        "secret_classified",
        "source_gap_marker",
        "operative_status",
    },
    "assistant_projection": {
        "projection",
        "derives_from",
        "operative_status",
    },
    "verified_movement": {
        "action_requested",
        "action_performed",
        "evidence_refs",
        "effects_observed",
        "authority_before",
        "authority_after",
    },
    "retraction_or_supersession": {
        "retraction_authority_ref",
        "retracts",
        "scope",
        "effective_relation_change",
        "effects_not_reversed",
    },
    "authority_change": {
        "authority_before",
        "authority_after",
        "owner_receipt_ref",
    },
    "unknown_change": {"adds", "resolves", "evidence_refs"},
    "relation_checkpoint": {
        "source_event_refs",
        "projection_refs",
        "current_relation",
        "unknowns",
        "next_legal_action",
        "reopen_condition",
    },
}


class ContinuityError(ValueError):
    """Closed reducer failure with a stable reason."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _state_digest(state: dict[str, Any]) -> str:
    body = copy.deepcopy(state)
    body.pop("state_digest", None)
    return sha256_text(canonical_json(body))


def _seal(state: dict[str, Any]) -> dict[str, Any]:
    sealed = copy.deepcopy(state)
    sealed["state_digest"] = _state_digest(sealed)
    return sealed


def _require(condition: bool, reason: str) -> None:
    if not condition:
        raise ContinuityError(reason)


def _require_string(value: Any, reason: str, *, allow_blank: bool = False) -> str:
    _require(isinstance(value, str), reason)
    if not allow_blank:
        _require(bool(value.strip()), reason)
    return value


def _require_string_list(value: Any, reason: str) -> list[str]:
    _require(isinstance(value, list), reason)
    _require(all(isinstance(item, str) and item.strip() for item in value), reason)
    _require(len(value) == len(set(value)), reason)
    return list(value)


def initial_state(owner_surface: str, owner_state_ref: str, authority: str) -> dict[str, Any]:
    for value, label in (
        (owner_surface, "owner_surface required"),
        (owner_state_ref, "owner_state_ref required"),
        (authority, "authority required"),
    ):
        _require_string(value, label)
    return _seal(
        {
            "schema": STATE_SCHEMA,
            "version": 1,
            "owner_surface": owner_surface,
            "owner_state_ref": owner_state_ref,
            "authority_initial": authority,
            "authority_current": authority,
            "events": [],
            "active_event_ids": [],
            "superseded_event_ids": [],
            "unknowns": [],
            "current_relation": "",
            "next_legal_action": "",
            "reopen_condition": "",
            "finite_state": "EMPTY_CONTINUITY",
            "previous_digest": None,
            "state_digest": "",
        }
    )


def _basic_state_validation(state: dict[str, Any]) -> None:
    _require(isinstance(state, dict), "state must be an object")
    _require(set(state) == STATE_KEYS, "state fields are not closed")
    _require(state["schema"] == STATE_SCHEMA, "unsupported state schema")
    _require(state["version"] == 1, "unsupported state version")
    _require_string(state["owner_surface"], "owner_surface required")
    _require_string(state["owner_state_ref"], "owner_state_ref required")
    _require_string(state["authority_initial"], "authority_initial required")
    _require_string(state["authority_current"], "authority_current required")
    _require(isinstance(state["events"], list), "events must be a list")
    event_ids = [event.get("event_id") for event in state["events"] if isinstance(event, dict)]
    _require(len(event_ids) == len(state["events"]), "every event must be an object with event_id")
    _require(len(event_ids) == len(set(event_ids)), "duplicate event IDs in state")
    _require_string_list(state["active_event_ids"], "active_event_ids invalid")
    _require_string_list(state["superseded_event_ids"], "superseded_event_ids invalid")
    _require_string_list(state["unknowns"], "unknowns invalid")
    _require(set(state["active_event_ids"]).isdisjoint(state["superseded_event_ids"]), "event cannot be active and superseded")
    _require(set(state["active_event_ids"]) | set(state["superseded_event_ids"]) == set(event_ids), "event status coverage mismatch")
    _require_string(state["current_relation"], "current_relation invalid", allow_blank=True)
    _require_string(state["next_legal_action"], "next_legal_action invalid", allow_blank=True)
    _require_string(state["reopen_condition"], "reopen_condition invalid", allow_blank=True)
    _require(state["finite_state"] in {
        "EMPTY_CONTINUITY",
        "CONTINUITY_CAPTURED",
        "CURRENT_RELATION_RECONSTRUCTABLE",
        "INCOMPLETE_SOURCE_RECONSTRUCTION",
    }, "invalid reducer finite state")
    _require(state["previous_digest"] is None or isinstance(state["previous_digest"], str), "previous_digest invalid")
    _require(isinstance(state["state_digest"], str) and len(state["state_digest"]) == 64, "state_digest invalid")
    _require(_state_digest(state) == state["state_digest"], "state digest mismatch")


def _event_index(state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {event["event_id"]: event for event in state["events"]}


def _validate_event_shape(state: dict[str, Any], event: dict[str, Any]) -> None:
    _require(isinstance(event, dict), "event must be an object")
    _require(set(event) == EVENT_KEYS, "event fields are not closed")
    _require(event["schema"] == EVENT_SCHEMA, "unsupported event schema")
    _require_string(event["event_id"], "event_id required")
    _require(event["event_kind"] in EVENT_KINDS, "unsupported event kind")
    _require(event["owner_surface"] == state["owner_surface"], "event owner does not match state owner")
    _require_string(event["previous_state_digest"], "previous_state_digest required")
    _require(isinstance(event["payload"], dict), "event payload must be an object")
    _require(set(event["payload"]) == PAYLOAD_KEYS[event["event_kind"]], "event payload fields are not closed")


def _validate_source_event(payload: dict[str, Any]) -> None:
    _require(payload["provenance_class"] in SOURCE_PROVENANCE, "invalid source provenance")
    _require_string(payload["source_ref"], "source_ref required")
    _require(isinstance(payload["secret_classified"], bool), "secret_classified must be boolean")
    _require(payload["operative_status"] == "active", "new source event must be active")
    if payload["secret_classified"]:
        _require(payload["exact_text"] == "", "secret source exact text is forbidden")
        _require(payload["source_digest"] == "", "secret source digest is forbidden")
        _require_string(payload["source_gap_marker"], "secret source gap marker required")
    else:
        _require(payload["source_gap_marker"] == "", "non-secret source cannot carry a secret gap marker")
        _require_string(payload["source_digest"], "source digest required")
        if payload["exact_text"]:
            _require(sha256_text(payload["exact_text"]) == payload["source_digest"], "source exact text digest mismatch")
        else:
            _require(Path(payload["source_ref"]).is_absolute(), "external exact source_ref must be absolute")


def _source_text(payload: dict[str, Any]) -> str:
    if payload["exact_text"]:
        return payload["exact_text"]
    path = Path(payload["source_ref"])
    _require(path.is_file() and not path.is_symlink(), "owner receipt source unavailable")
    _require(path.stat().st_size <= 1024 * 1024, "owner receipt source too large")
    raw = path.read_bytes()
    _require(hashlib.sha256(raw).hexdigest() == payload["source_digest"], "owner receipt source digest mismatch")
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ContinuityError("owner receipt source is not UTF-8") from exc


def _validate_authority_grant(payload: dict[str, Any], before: str, after: str) -> None:
    try:
        grant = json.loads(_source_text(payload))
    except json.JSONDecodeError as exc:
        raise ContinuityError("owner receipt is not a structured authority grant") from exc
    _require(isinstance(grant, dict), "owner receipt is not a structured authority grant")
    _require(
        set(grant) == {"schema", "authority_before", "authority_after"},
        "owner receipt authority grant fields are not closed",
    )
    _require(
        grant["schema"] == "dnd.material_work_continuity.authority_grant.v1",
        "owner receipt authority grant schema invalid",
    )
    _require(grant["authority_before"] == before, "owner receipt authority_before mismatch")
    _require(grant["authority_after"] == after, "owner receipt authority_after mismatch")


def _validate_payload(state: dict[str, Any], event: dict[str, Any]) -> None:
    kind = event["event_kind"]
    payload = event["payload"]
    index = _event_index(state)
    if kind == "source_event":
        _validate_source_event(payload)
    elif kind == "assistant_projection":
        _require_string(payload["projection"], "projection required")
        refs = _require_string_list(payload["derives_from"], "derives_from invalid")
        _require(refs and all(ref in index for ref in refs), "projection derivation ref missing")
        _require(payload["operative_status"] == "active", "new projection must be active")
    elif kind == "verified_movement":
        _require_string(payload["action_requested"], "action_requested required")
        _require_string(payload["action_performed"], "action_performed required")
        _require_string_list(payload["evidence_refs"], "evidence_refs invalid")
        _require(bool(payload["evidence_refs"]), "verified movement requires evidence")
        _require_string_list(payload["effects_observed"], "effects_observed invalid")
        _require_string(payload["authority_before"], "authority_before required")
        _require_string(payload["authority_after"], "authority_after required")
        _require(payload["authority_before"] == state["authority_current"], "movement authority_before mismatch")
        _require(payload["authority_after"] == payload["authority_before"], "authority changes require authority_change event")
    elif kind == "retraction_or_supersession":
        authority_ref = _require_string(payload["retraction_authority_ref"], "retraction authority ref required")
        targets = _require_string_list(payload["retracts"], "retracts invalid")
        _require(bool(targets), "retraction target required")
        _require(authority_ref in index, "retraction authority event missing")
        authority_event = index[authority_ref]
        _require(authority_event["event_kind"] == "source_event", "retraction authority must be source event")
        _require(authority_event["payload"]["provenance_class"] in {"direct_operator", "owner_source"}, "retraction authority must be owner source")
        _require(authority_ref in state["active_event_ids"], "retraction authority source is not active")
        _require(authority_ref not in targets, "retraction cannot retract its own authority")
        _require(all(target in index for target in targets), "retraction target missing")
        _require(all(target not in state["superseded_event_ids"] for target in targets), "target already superseded")
        _require_string(payload["scope"], "retraction scope required")
        _require_string(payload["effective_relation_change"], "effective relation change required")
        effects_not_reversed = _require_string_list(payload["effects_not_reversed"], "effects_not_reversed invalid")
        required_effects = {
            effect
            for target in targets
            if index[target]["event_kind"] == "verified_movement"
            for effect in index[target]["payload"]["effects_observed"]
        }
        _require(required_effects <= set(effects_not_reversed), "retraction erased an observed effect")
    elif kind == "authority_change":
        _require_string(payload["authority_before"], "authority_before required")
        _require_string(payload["authority_after"], "authority_after required")
        owner_receipt_ref = _require_string(payload["owner_receipt_ref"], "owner receipt required")
        _require(payload["authority_before"] == state["authority_current"], "authority_before mismatch")
        _require(payload["authority_after"] != payload["authority_before"], "authority change must change authority")
        _require(owner_receipt_ref in index, "owner receipt event missing")
        owner_receipt = index[owner_receipt_ref]
        _require(owner_receipt["event_kind"] == "source_event", "owner receipt must be source event")
        _require(
            owner_receipt["payload"]["provenance_class"] in {"direct_operator", "owner_source"},
            "owner receipt must be operator or owner source",
        )
        _require(owner_receipt_ref in state["active_event_ids"], "owner receipt is not active")
        _validate_authority_grant(
            owner_receipt["payload"],
            payload["authority_before"],
            payload["authority_after"],
        )
    elif kind == "unknown_change":
        adds = _require_string_list(payload["adds"], "unknown adds invalid")
        resolves = _require_string_list(payload["resolves"], "unknown resolves invalid")
        evidence = _require_string_list(payload["evidence_refs"], "unknown evidence invalid")
        _require(set(adds).isdisjoint(resolves), "unknown cannot be added and resolved together")
        _require(set(resolves) <= set(state["unknowns"]), "resolved unknown not present")
        if resolves:
            _require(bool(evidence), "unknown resolution requires evidence")
    elif kind == "relation_checkpoint":
        source_refs = _require_string_list(payload["source_event_refs"], "source_event_refs invalid")
        projection_refs = _require_string_list(payload["projection_refs"], "projection_refs invalid")
        _require(bool(source_refs), "relation checkpoint requires source")
        for ref in source_refs:
            _require(ref in index and index[ref]["event_kind"] == "source_event", "checkpoint source ref invalid")
            _require(ref not in state["superseded_event_ids"], "checkpoint cannot use superseded source")
        for ref in projection_refs:
            _require(ref in index and index[ref]["event_kind"] == "assistant_projection", "checkpoint projection ref invalid")
            _require(ref not in state["superseded_event_ids"], "checkpoint cannot use superseded projection")
        _require_string(payload["current_relation"], "current relation required")
        _require_string_list(payload["unknowns"], "checkpoint unknowns invalid")
        _require(set(payload["unknowns"]) == set(state["unknowns"]), "checkpoint unknown coverage mismatch")
        _require_string(payload["next_legal_action"], "next legal action required")
        _require_string(payload["reopen_condition"], "reopen condition required")


def _active_source_gap(state: dict[str, Any]) -> bool:
    index = _event_index(state)
    return any(
        index[event_id]["event_kind"] == "source_event"
        and index[event_id]["payload"]["secret_classified"]
        for event_id in state["active_event_ids"]
    )


def apply_event(state: dict[str, Any], event: dict[str, Any], *, _replay: bool = False) -> dict[str, Any]:
    verify_state(state, full=not _replay)
    _validate_event_shape(state, event)
    index = _event_index(state)
    existing = index.get(event["event_id"])
    if existing is not None:
        if canonical_json(existing) == canonical_json(event):
            return copy.deepcopy(state)
        raise ContinuityError("event ID collision")
    _require(event["previous_state_digest"] == state["state_digest"], "state head mismatch")
    _validate_payload(state, event)

    updated = copy.deepcopy(state)
    old_digest = state["state_digest"]
    updated["events"].append(copy.deepcopy(event))
    updated["active_event_ids"].append(event["event_id"])
    kind = event["event_kind"]
    payload = event["payload"]

    if kind == "retraction_or_supersession":
        for target in payload["retracts"]:
            updated["active_event_ids"].remove(target)
            updated["superseded_event_ids"].append(target)
    elif kind == "authority_change":
        updated["authority_current"] = payload["authority_after"]
    elif kind == "unknown_change":
        updated["unknowns"] = sorted(
            (set(updated["unknowns"]) | set(payload["adds"])) - set(payload["resolves"])
        )
    elif kind == "relation_checkpoint":
        updated["current_relation"] = payload["current_relation"]
        updated["next_legal_action"] = payload["next_legal_action"]
        updated["reopen_condition"] = payload["reopen_condition"]

    if _active_source_gap(updated):
        updated["finite_state"] = "INCOMPLETE_SOURCE_RECONSTRUCTION"
    elif kind == "relation_checkpoint":
        updated["finite_state"] = "CURRENT_RELATION_RECONSTRUCTABLE"
    else:
        updated["finite_state"] = "CONTINUITY_CAPTURED"
    updated["previous_digest"] = old_digest
    updated["state_digest"] = ""
    return _seal(updated)


def verify_state(state: dict[str, Any], *, full: bool = True) -> None:
    _basic_state_validation(state)
    if not full:
        return
    rebuilt = initial_state(
        state["owner_surface"],
        state["owner_state_ref"],
        state["authority_initial"],
    )
    for event in state["events"]:
        rebuilt = apply_event(rebuilt, event, _replay=True)
    _require(canonical_json(rebuilt) == canonical_json(state), "state event chain mismatch")


def verify_source_locators(state: dict[str, Any]) -> list[str]:
    verify_state(state)
    failures: list[str] = []
    for event in state["events"]:
        if event["event_kind"] != "source_event":
            continue
        payload = event["payload"]
        if payload["secret_classified"] or payload["exact_text"]:
            continue
        path = Path(payload["source_ref"])
        if not path.is_file() or path.is_symlink():
            failures.append(f"{event['event_id']}:source_unavailable")
            continue
        if path.stat().st_size > 1024 * 1024:
            failures.append(f"{event['event_id']}:source_too_large")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != payload["source_digest"]:
            failures.append(f"{event['event_id']}:source_digest_mismatch")
    return failures


def reconstruct(state: dict[str, Any]) -> dict[str, Any]:
    verify_state(state)
    locator_failures = verify_source_locators(state)
    index = _event_index(state)
    effects = sorted(
        {
            effect
            for event in state["events"]
            if event["event_kind"] == "verified_movement"
            for effect in event["payload"]["effects_observed"]
        }
    )
    active_sources = [
        event_id
        for event_id in state["active_event_ids"]
        if index[event_id]["event_kind"] == "source_event"
    ]
    active_projections = [
        event_id
        for event_id in state["active_event_ids"]
        if index[event_id]["event_kind"] == "assistant_projection"
    ]
    movements = [
        event["event_id"]
        for event in state["events"]
        if event["event_kind"] == "verified_movement"
    ]
    retractions = [
        {
            "event_id": event["event_id"],
            "retraction_authority_ref": event["payload"]["retraction_authority_ref"],
            "retracts": list(event["payload"]["retracts"]),
            "scope": event["payload"]["scope"],
            "effective_relation_change": event["payload"]["effective_relation_change"],
            "effects_not_reversed": list(event["payload"]["effects_not_reversed"]),
        }
        for event in state["events"]
        if event["event_kind"] == "retraction_or_supersession"
    ]
    active_checkpoints = [
        event
        for event in state["events"]
        if event["event_kind"] == "relation_checkpoint"
        and event["event_id"] in state["active_event_ids"]
    ]
    latest_checkpoint = active_checkpoints[-1] if active_checkpoints else None
    finite_state = state["finite_state"]
    if locator_failures:
        finite_state = "INCOMPLETE_SOURCE_RECONSTRUCTION"
    return {
        "owner_surface": state["owner_surface"],
        "owner_state_ref": state["owner_state_ref"],
        "source_event_refs": active_sources,
        "active_source_event_refs": active_sources,
        "projection_refs": active_projections,
        "verified_movement_refs": movements,
        "retractions": retractions,
        "superseded_event_refs": list(state["superseded_event_ids"]),
        "effects_preserved": effects,
        "authority_before": state["authority_initial"],
        "authority_after": state["authority_current"],
        "authority_current": state["authority_current"],
        "unknowns": list(state["unknowns"]),
        "checkpoint_ref": latest_checkpoint["event_id"] if latest_checkpoint else None,
        "checkpoint": copy.deepcopy(latest_checkpoint["payload"]) if latest_checkpoint else None,
        "current_relation": state["current_relation"],
        "next_legal_action": state["next_legal_action"],
        "reopen_condition": state["reopen_condition"],
        "source_locator_failures": locator_failures,
        "coverage": {
            "event_count": len(state["events"]),
            "active_event_count": len(state["active_event_ids"]),
            "superseded_event_count": len(state["superseded_event_ids"]),
            "source_locator_failures": locator_failures,
        },
        "finite_state": finite_state,
        "state_digest": state["state_digest"],
    }


def _read_json(path: str) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    _require(isinstance(data, dict), "JSON root must be an object")
    return data


def _emit(value: dict[str, Any], output: str | None) -> None:
    rendered = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    if output:
        Path(output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--owner-surface", required=True)
    init.add_argument("--owner-state-ref", required=True)
    init.add_argument("--authority", required=True)
    init.add_argument("--output")
    reduce_cmd = sub.add_parser("reduce")
    reduce_cmd.add_argument("--state", required=True)
    reduce_cmd.add_argument("--event", required=True)
    reduce_cmd.add_argument("--output")
    verify = sub.add_parser("verify")
    verify.add_argument("--state", required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            value = initial_state(args.owner_surface, args.owner_state_ref, args.authority)
        elif args.command == "reduce":
            value = apply_event(_read_json(args.state), _read_json(args.event))
        else:
            value = reconstruct(_read_json(args.state))
    except (ContinuityError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    _emit(value, getattr(args, "output", None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
