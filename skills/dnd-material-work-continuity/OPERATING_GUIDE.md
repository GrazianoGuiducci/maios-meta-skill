# D-ND Material Work Continuity

## Use the deterministic recorder when exact event integrity matters

The textual method is usable on its own. This kit also supplies the source competence's Python reducer, event/state JSON schema, a worked ledger and portable tests. The reducer is a record-integrity tool, not a semantic admission gate or an independent authority. Hashes detect inconsistent records; they do not prove that a statement or evidence reference is true. Keep the original ledger and source locators in the project that owns them.

The seven event kinds preserve exact source, assistant projection, observed movement, retraction or supersession, authority change, unknown change and a current-relation checkpoint. Sources retain attribution. Projections cite preceding events. A correction supersedes an interpretation without deleting its event or erasing observed effects. A checkpoint exposes current sources, remaining unknowns and the next permitted action. Secret-classified sources retain a gap marker, without secret values or hashes. Never copy a credential into a record.

## Run the included example

Use Python 3.10 or later from the competence folder. Run `python scripts/demo_continuity.py --output-dir demo-ledger` with a new directory name. It writes an initial state, six illustrative events and their successor states, and `reconstruction.json`. The example corrects an assistant's publication interpretation while preserving a draft actually saved. It does not publish or contact anything.

Run `python scripts/reduce_material_work_continuity.py verify --state demo-ledger/C1.state.json` to reconstruct that state. For your project, `init` accepts `--owner-surface`, `--owner-state-ref`, `--authority` and optional `--output`. `reduce` accepts `--state`, `--event` and optional `--output`; use a separate output file to retain the preceding state. An event's `previous_state_digest` must match the state it extends. The demo shows how to construct each event through the Python interface.

## Understand failures and limits

An exact replay is idempotent; an altered event with the same identity is rejected. A stale predecessor, tampered state, fabricated authority reference or unsupported resolution of an unknown is rejected. A structured authority-grant source models a recorded change; the tool cannot authenticate the human behind an externally supplied document. A referenced source must be an absolute regular file with the recorded digest, at most 1 MiB; missing, symlinked or changed locators produce incomplete reconstruction. Inline exact sources remain available in the ledger.

The CLI writes only its chosen output and has no network calls. Concurrent writers need serialization at the actual file/store boundary; this reducer alone supplies no file lock or database transaction. A schema-valid state is also checked by replaying its event chain. Run the portable tests with `python -m pip install -r requirements-test.txt` followed by `python scripts/test_reduce_material_work_continuity.py`. The reducer itself uses only the standard library; `jsonschema` is needed by schema tests. The schema retains original protocol names for compatibility, with a public schema identifier and Windows/POSIX source paths.
