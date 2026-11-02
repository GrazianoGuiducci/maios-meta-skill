# Form and distribute a public competence resource

[Italiano](DISTRIBUZIONE.md).

An internal method becomes a public resource when an outside recipient can understand its use, receive its knowledge and exercise it in their own context.

## Preserve the usable capability

Reach the source competence and the reasons its method evolved. Distinguish the general capability from the case that formed it. A concrete service may have as much value as a generative competence; meta level does not determine commercial priority.

Preserve meaning, conditions, reasons and revisability. Replace private dependencies with included knowledge or accessible entries. Removing paths and names alone does not teach what to observe or which difference should change a decision.

## Identity and explanation

Preserve the original competence name across languages. A functional title explains its recognizable work; a subtitle supplies context. Keep names, distribution identifiers and translated explanations distinguishable. Checking a page against a catalogue is insufficient if both repeat an assistant's invented name: reach the native source identity.

Cards expose what it does, when to use it and recognizable examples. Dedicated pages explain method, use and pertinent depth. Meta relations form or transform methods and capabilities; autological relations concern a capability's own operation. Composition, automation and autonomy retain different meanings.

## A complete receiving method

An operating body, guide, examples and starter support each other. A self-contained starter includes the necessary method; an inaccessible file reference does not. Explain chat, harness and existing-kernel differences where they affect use. Tools, accounts, persistence and schedulers require actual mechanisms.

English is this collection's primary language. Italian counterparts preserve the same operating relations. Translation must retain what is observed, why a distinction changes choice, how to act and what continues. Equal section counts or promises do not establish correspondence.

## Coherent source and delivery

The catalogue connects identity, version, state, language and file locations. Build distributed packages from the selected Git snapshot and compare archive members with its blobs. This also avoids silent inclusion of unrelated working changes or line-ending conversions. Preserve concurrent work.

Record the received revision when generating the website. Pair language routes, canonicals, alternates, guides, examples and starter content. An English heading does not establish an English experience if its selector or copied method remains in another language.

Articles and social adaptations derive from the selected resource. Shortening preserves thesis, state and conditions. A shared source, deployment, prepared text, publication and recipient use have separate identities and observations. When meaning changes, update dependent prepared texts and hashes without resetting publication history or repeating completed effects.

## Learning through use

Comprehension difficulty changes a card or explanation; missing operating knowledge changes method or guide; delivery divergence changes the build mechanism. Correct dependent projections while preserving unrelated work.

Feedback may change the product, explanation, distribution or formation method. Return reusable learning to the responsible competence. One completed case makes a method available; later non-identical use can reveal its assimilation and limits.
# Adaptable activities

The `activities` array in the catalogue identifies complete assignments that
compose existing competences. It is separate from the operating entries in
`resources` and from the skill installer. Each activity has its own edition,
localized method, guide, examples, context template and autonomous starter.

Run `python tools/build_activities.py` to render the activity documents from
their authored `activity.json` sources. Commit those sources, then run
`python tools/build_activities.py --source-ref COMMIT` to produce the kit from
that exact revision. `dist/activities-manifest.json` records the resulting
archive, source revision, supporting competence editions and file hashes.
Existing competence packages and their manifest are preserved.

The builder resolves a branch or tag to a full commit before reading source
files. An existing package with different bytes is rejected: select a new
edition and filename rather than replace a distributed archive.

The first `public-representation` 0.1.0 kit embedded the literal reference
`HEAD`. Its unchanged archive is now qualified by the external manifest with
source commit `46002f7c2ef809ec7f167036854d3037494c3d01` and
`embedded_source_reference: HEAD`. All 64 source members were compared with
that commit; the 65th member is the generated dependency record. This corrects
the external provenance record without claiming the old archive embedded a
full commit or changing its checksum.

The kit includes complete public supporting competences under `skills/`.
The activity guide explains adoption through the receiving environment; copying
the assignment does not create a recurring job or confer publication authority.

