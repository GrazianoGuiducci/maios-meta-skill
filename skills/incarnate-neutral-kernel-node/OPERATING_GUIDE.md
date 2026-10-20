# Incarnate Neutral Kernel Node

## Form a receiver and preserve its own life

Distinguish the upstream source package, a node-owned fork or adaptation, a configured projection, installed host files and the present conversation. A first incarnation forms an initial receiver. An update meets a receiver that already has local decisions, knowledge and observed effects. Preserve those contributions while understanding which source changes remain useful. Version equality cannot establish semantic equality, and different versions need not imply a defect.

Map each material source function to the receiving owner that must carry it. Adapt discovery, entry, persistence, tools and learning to the actual host; a renamed folder alone cannot transport those functions. Retain rejected or deferred relations with reasons where a later return could otherwise lose them. An assessed change remains pending until its receiving implementation and relevant use occur; unchanged upstream files do not finish that work.

## Inspect a selected source/receiver pair

The supplied `scripts/inspect_kernel_pair.py` is a read-only adaptation of the source inspector. It uses Python 3.10+ and Git, without network calls. Copy `references/port-map.example.json` into your project, set source and destination repository paths, source scope if any, assessed commit and tree identities, owner paths and pending relations. Placeholders must be replaced with actual values; the example is a format illustration, not a claim about your repositories.

Use `git -C SOURCE rev-parse HEAD` for the assessed commit and `git -C SOURCE rev-parse HEAD:kernel` for a selected subtree; use `HEAD^{tree}` when assessing the whole repository. Use the destination's whole tree identity. Run `python scripts/inspect_kernel_pair.py --workspace PATH --map PATH_TO_MAP`. Repository paths in the map can be relative to the selected workspace or absolute. Run `python scripts/test_inspect_kernel_pair.py` to exercise scoped freshness and pending work with temporary Git repositories.

The report exposes current identities, dirty work, relevant source/destination deltas, missing mapped paths and pending integration. An unrelated repository commit can leave the assessed subtree unchanged. A missing assessed commit makes comparison unavailable; do not manufacture equivalence. Dirty work is reported separately because committed tree comparisons do not include it. Inspect a relevant local delta before acting. The report never installs, merges, closes pending relations or proves semantic transfer. Follow the actual meaning and receiving knowledge, then record what implementation and use established. Preserve a recoverable earlier state for the exact changed surface rather than resetting another owner's work.
