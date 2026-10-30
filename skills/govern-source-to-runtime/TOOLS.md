# Read-only release tools

The kit includes the source method's deterministic reducer and evidence-request validator. They read JSON supplied by you. They do not inspect repositories or accounts, prove that supplied statements are true, approve effects, publish, restart services or repair a release.

## Run the supplied fictional examples

From the complete skill folder, with Python 3.10 or newer:

```text
python scripts/reduce_release_state.py --self-test
python scripts/validate_effect_request.py --self-test
python scripts/reduce_release_state.py examples/release-context.sample.json
python scripts/validate_effect_request.py examples/effect-request.sample.json
```

The reducer's example represents source already promoted, a different active runtime and no runtime authority. It returns await_runtime_gate rather than performing activation. The request example is synthetic and uses placeholder revisions and evidence: its ready result checks coherence of that fixture, never permission to use those values on a real system. Preserve it as a demonstration and create your own data from actual sources.

## Supply evidence for your own effect

Read references/release-context.schema.json for observed lifecycle facts and references/effect-request.schema.json for an exact effect request. Keep target, source revision, service allowlist, credential locality, previous release and completed checks bound to their actual evidence. The request validator emits ready, needs_operator_decision or blocked. Any changed request produces a different digest. Its dnd.effect-request.v1 identifier preserves the tool's source protocol; it does not require the source workspace.

The tools use Python's standard library. If jsonschema is installed, the request tool additionally checks the included JSON schema; its own shape and semantic checks also run without that optional dependency. Both self-tests exercise positive and stop conditions without network or service control. Read references/capability-manifest.json for the source's candidate automation maturity. A coherent fixture is not qualification of your controller, host or recovery.
