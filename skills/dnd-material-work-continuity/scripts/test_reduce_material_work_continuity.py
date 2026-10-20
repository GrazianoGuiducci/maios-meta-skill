from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "reduce_material_work_continuity.py"
SPEC = importlib.util.spec_from_file_location("continuity_reducer", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MaterialWorkContinuityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = MODULE.initial_state(
            "Example project",
            "project/CURRENT_STATE.md",
            "operator",
        )

    def event(self, event_id: str, kind: str, payload: dict) -> dict:
        return {
            "schema": MODULE.EVENT_SCHEMA,
            "event_id": event_id,
            "event_kind": kind,
            "owner_surface": "Example project",
            "previous_state_digest": self.state["state_digest"],
            "payload": payload,
        }

    def source_payload(self, text: str, source_ref: str = "inline:test") -> dict:
        return {
            "provenance_class": "direct_operator",
            "source_ref": source_ref,
            "exact_text": text,
            "source_digest": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "secret_classified": False,
            "source_gap_marker": "",
            "operative_status": "active",
        }

    def add_source(self, event_id: str, text: str) -> None:
        self.state = MODULE.apply_event(
            self.state,
            self.event(event_id, "source_event", self.source_payload(text)),
        )

    def test_exact_source_and_projection_remain_separate(self) -> None:
        self.add_source("S1", "exact source ?")
        projection = self.event(
            "P1",
            "assistant_projection",
            {
                "projection": "assistant interpretation",
                "derives_from": ["S1"],
                "operative_status": "active",
            },
        )
        self.state = MODULE.apply_event(self.state, projection)
        self.assertEqual(self.state["events"][0]["payload"]["exact_text"], "exact source ?")
        self.assertEqual(self.state["events"][1]["payload"]["projection"], "assistant interpretation")

    def test_exact_replay_is_idempotent_and_collision_is_rejected(self) -> None:
        event = self.event("S1", "source_event", self.source_payload("source"))
        self.state = MODULE.apply_event(self.state, event)
        replayed = MODULE.apply_event(self.state, event)
        self.assertEqual(replayed, self.state)
        collision = copy.deepcopy(event)
        collision["payload"]["exact_text"] = "changed"
        collision["payload"]["source_digest"] = hashlib.sha256(b"changed").hexdigest()
        with self.assertRaisesRegex(MODULE.ContinuityError, "collision"):
            MODULE.apply_event(self.state, collision)

    def test_stale_successor_and_tampered_state_are_rejected(self) -> None:
        stale = self.event("S1", "source_event", self.source_payload("source"))
        self.add_source("S0", "prior")
        with self.assertRaisesRegex(MODULE.ContinuityError, "head mismatch"):
            MODULE.apply_event(self.state, stale)
        tampered = copy.deepcopy(self.state)
        tampered["current_relation"] = "forged"
        with self.assertRaisesRegex(MODULE.ContinuityError, "digest mismatch"):
            MODULE.verify_state(tampered)

    def test_secret_source_value_and_digest_are_rejected(self) -> None:
        payload = {
            "provenance_class": "direct_operator",
            "source_ref": "operator-owned-secret",
            "exact_text": "secret-value",
            "source_digest": hashlib.sha256(b"secret-value").hexdigest(),
            "secret_classified": True,
            "source_gap_marker": "SECRET_NOT_PERSISTED",
            "operative_status": "active",
        }
        with self.assertRaisesRegex(MODULE.ContinuityError, "secret source exact text"):
            MODULE.apply_event(self.state, self.event("S1", "source_event", payload))

    def test_owner_retraction_preserves_source_and_observed_effects(self) -> None:
        self.add_source("S1", "do the work")
        movement = self.event(
            "M1",
            "verified_movement",
            {
                "action_requested": "create file",
                "action_performed": "created file",
                "evidence_refs": ["receipt:file-created"],
                "effects_observed": ["file-created"],
                "authority_before": "operator",
                "authority_after": "operator",
            },
        )
        self.state = MODULE.apply_event(self.state, movement)
        self.add_source("S2", "stop using that direction")
        retraction = self.event(
            "R1",
            "retraction_or_supersession",
            {
                "retraction_authority_ref": "S2",
                "retracts": ["S1", "M1"],
                "scope": "operative direction",
                "effective_relation_change": "stop prior direction",
                "effects_not_reversed": ["file-created"],
            },
        )
        self.state = MODULE.apply_event(self.state, retraction)
        rebuilt = MODULE.reconstruct(self.state)
        self.assertIn("S1", rebuilt["superseded_event_refs"])
        self.assertIn("file-created", rebuilt["effects_preserved"])
        self.assertEqual(len(self.state["events"]), 4)

    def test_retraction_cannot_erase_effect_or_lack_owner_source(self) -> None:
        self.add_source("S1", "source")
        projection = self.event(
            "P1",
            "assistant_projection",
            {"projection": "projection", "derives_from": ["S1"], "operative_status": "active"},
        )
        self.state = MODULE.apply_event(self.state, projection)
        bad = self.event(
            "R1",
            "retraction_or_supersession",
            {
                "retraction_authority_ref": "P1",
                "retracts": ["S1"],
                "scope": "source",
                "effective_relation_change": "erase",
                "effects_not_reversed": [],
            },
        )
        with self.assertRaisesRegex(MODULE.ContinuityError, "authority must be source"):
            MODULE.apply_event(self.state, bad)

    def test_authority_change_rejects_empty_or_fabricated_owner_receipt(self) -> None:
        empty = self.event(
            "A1",
            "authority_change",
            {
                "authority_before": "operator",
                "authority_after": "assistant",
                "owner_receipt_ref": "",
            },
        )
        with self.assertRaisesRegex(MODULE.ContinuityError, "owner receipt"):
            MODULE.apply_event(self.state, empty)
        fabricated = self.event(
            "A2",
            "authority_change",
            {
                "authority_before": "operator",
                "authority_after": "assistant",
                "owner_receipt_ref": "unverified:any-string",
            },
        )
        with self.assertRaisesRegex(MODULE.ContinuityError, "event missing"):
            MODULE.apply_event(self.state, fabricated)

    def test_authority_change_accepts_active_digest_bound_owner_source(self) -> None:
        grant = json.dumps(
            {
                "schema": "dnd.material_work_continuity.authority_grant.v1",
                "authority_before": "operator",
                "authority_after": "Example project owner",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        self.add_source("S1", grant)
        event = self.event(
            "A1",
            "authority_change",
            {
                "authority_before": "operator",
                "authority_after": "Example project owner",
                "owner_receipt_ref": "S1",
            },
        )
        self.state = MODULE.apply_event(self.state, event)
        self.assertEqual(self.state["authority_current"], "Example project owner")

    def test_authority_change_rejects_unrelated_active_source(self) -> None:
        self.add_source("S1", "ordinary source with no authority transfer")
        event = self.event(
            "A1",
            "authority_change",
            {
                "authority_before": "operator",
                "authority_after": "assistant",
                "owner_receipt_ref": "S1",
            },
        )
        with self.assertRaisesRegex(MODULE.ContinuityError, "structured authority grant"):
            MODULE.apply_event(self.state, event)

    def test_superseded_source_cannot_authorize_later_retraction(self) -> None:
        self.add_source("S1", "old source")
        self.add_source("S2", "new owner source")
        retire_source = self.event(
            "R1",
            "retraction_or_supersession",
            {
                "retraction_authority_ref": "S2",
                "retracts": ["S1"],
                "scope": "source authority",
                "effective_relation_change": "old source is no longer operative",
                "effects_not_reversed": [],
            },
        )
        self.state = MODULE.apply_event(self.state, retire_source)
        projection = self.event(
            "P1",
            "assistant_projection",
            {"projection": "projection", "derives_from": ["S2"], "operative_status": "active"},
        )
        self.state = MODULE.apply_event(self.state, projection)
        stale_retraction = self.event(
            "R2",
            "retraction_or_supersession",
            {
                "retraction_authority_ref": "S1",
                "retracts": ["P1"],
                "scope": "projection",
                "effective_relation_change": "stale source attempts relation change",
                "effects_not_reversed": [],
            },
        )
        with self.assertRaisesRegex(MODULE.ContinuityError, "not active"):
            MODULE.apply_event(self.state, stale_retraction)

    def test_unknown_resolution_requires_evidence(self) -> None:
        add = self.event(
            "U1",
            "unknown_change",
            {"adds": ["missing prior months"], "resolves": [], "evidence_refs": []},
        )
        self.state = MODULE.apply_event(self.state, add)
        resolve = self.event(
            "U2",
            "unknown_change",
            {"adds": [], "resolves": ["missing prior months"], "evidence_refs": []},
        )
        with self.assertRaisesRegex(MODULE.ContinuityError, "requires evidence"):
            MODULE.apply_event(self.state, resolve)

    def test_checkpoint_reconstructs_current_relation(self) -> None:
        self.add_source("S1", "preserve this")
        unknown = self.event(
            "U1",
            "unknown_change",
            {"adds": ["older unavailable source"], "resolves": [], "evidence_refs": []},
        )
        self.state = MODULE.apply_event(self.state, unknown)
        checkpoint = self.event(
            "C1",
            "relation_checkpoint",
            {
                "source_event_refs": ["S1"],
                "projection_refs": [],
                "current_relation": "material work continuity competence authorized",
                "unknowns": ["older unavailable source"],
                "next_legal_action": "create and validate owner-local competence",
                "reopen_condition": "new source or validation failure",
            },
        )
        self.state = MODULE.apply_event(self.state, checkpoint)
        receipt = MODULE.reconstruct(self.state)
        self.assertEqual(receipt["finite_state"], "CURRENT_RELATION_RECONSTRUCTABLE")
        self.assertEqual(receipt["current_relation"], "material work continuity competence authorized")
        self.assertEqual(receipt["checkpoint_ref"], "C1")
        self.assertEqual(receipt["checkpoint"]["source_event_refs"], ["S1"])
        self.assertEqual(receipt["checkpoint"]["next_legal_action"], "create and validate owner-local competence")

    def test_changed_owner_source_yields_incomplete_reconstruction(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.txt"
            path.write_text("original\n", encoding="utf-8")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            payload = {
                "provenance_class": "owner_source",
                "source_ref": str(path),
                "exact_text": "",
                "source_digest": digest,
                "secret_classified": False,
                "source_gap_marker": "",
                "operative_status": "active",
            }
            self.state = MODULE.apply_event(self.state, self.event("S1", "source_event", payload))
            path.write_text("changed\n", encoding="utf-8")
            receipt = MODULE.reconstruct(self.state)
            self.assertEqual(receipt["finite_state"], "INCOMPLETE_SOURCE_RECONSTRUCTION")
            self.assertEqual(receipt["source_locator_failures"], ["S1:source_digest_mismatch"])


class MaterialWorkContinuityPackageTests(unittest.TestCase):
    def test_schema_and_reducer_durable_states_match(self) -> None:
        schema = json.loads(
            (ROOT / "references/material-work-continuity.v0.schema.json").read_text(encoding="utf-8")
        )
        expected = {
            "EMPTY_CONTINUITY",
            "CONTINUITY_CAPTURED",
            "CURRENT_RELATION_RECONSTRUCTABLE",
            "INCOMPLETE_SOURCE_RECONSTRUCTION",
        }
        self.assertEqual(set(schema["properties"]["finite_state"]["enum"]), expected)

    def test_schema_rejects_open_payload_and_bad_digest_shape(self) -> None:
        from jsonschema import Draft202012Validator

        schema = json.loads(
            (ROOT / "references/material-work-continuity.v0.schema.json").read_text(encoding="utf-8")
        )
        bad = {
            "schema": MODULE.EVENT_SCHEMA,
            "event_id": "S1",
            "event_kind": "source_event",
            "owner_surface": "Example project",
            "previous_state_digest": "not-a-digest",
            "payload": {"arbitrary": "schema-must-reject-this"},
        }
        event_schema = {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": "#/$defs/event",
        }
        errors = list(Draft202012Validator(event_schema).iter_errors(bad))
        self.assertTrue(errors)

    def test_every_event_payload_class_has_a_schema_valid_representative(self) -> None:
        from jsonschema import Draft202012Validator

        schema = json.loads(
            (ROOT / "references/material-work-continuity.v0.schema.json").read_text(encoding="utf-8")
        )
        event_schema = {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": "#/$defs/event",
        }
        validator = Draft202012Validator(event_schema)
        state = MODULE.initial_state("Example project", "project/CURRENT_STATE.md", "operator")
        payloads = {
            "source_event": {
                "provenance_class": "direct_operator",
                "source_ref": "inline:test",
                "exact_text": "source",
                "source_digest": hashlib.sha256(b"source").hexdigest(),
                "secret_classified": False,
                "source_gap_marker": "",
                "operative_status": "active",
            },
            "assistant_projection": {
                "projection": "separate projection",
                "derives_from": ["S1"],
                "operative_status": "active",
            },
            "verified_movement": {
                "action_requested": "verify contract",
                "action_performed": "verified contract",
                "evidence_refs": ["test:representative"],
                "effects_observed": [],
                "authority_before": "operator",
                "authority_after": "operator",
            },
            "retraction_or_supersession": {
                "retraction_authority_ref": "S1",
                "retracts": ["P1"],
                "scope": "projection",
                "effective_relation_change": "projection no longer operative",
                "effects_not_reversed": [],
            },
            "authority_change": {
                "authority_before": "operator",
                "authority_after": "owner",
                "owner_receipt_ref": "S1",
            },
            "unknown_change": {
                "adds": ["unknown"],
                "resolves": [],
                "evidence_refs": [],
            },
            "relation_checkpoint": {
                "source_event_refs": ["S1"],
                "projection_refs": [],
                "current_relation": "bounded relation",
                "unknowns": ["unknown"],
                "next_legal_action": "verify",
                "reopen_condition": "new evidence",
            },
        }
        for index, (kind, payload) in enumerate(payloads.items(), start=1):
            event = {
                "schema": MODULE.EVENT_SCHEMA,
                "event_id": f"E{index}",
                "event_kind": kind,
                "owner_surface": "Example project",
                "previous_state_digest": state["state_digest"],
                "payload": payload,
            }
            self.assertEqual(list(validator.iter_errors(event)), [], kind)



if __name__ == "__main__":
    unittest.main()
