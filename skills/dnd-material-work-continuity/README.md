# D-ND Material Work Continuity

**Reconstruct an AI project's work and decisions**

[Italiano](README_IT.md) · Public edition 0.3.1 · English operating method

## What it does

Keeps a trace of material events and distinguishes the person's source, the assistant's interpretation and observed effects.

## When to use it

When requirements or direction change, or when the reasons behind a project's current state need to be reconstructed.

A decision can change without erasing what happened before it. This competence preserves the connection between an original request, the AI's interpretation, completed work and a later correction.
The result is a usable reconstruction for whoever resumes the project. Detailed history stays reachable; the current entry contains what is needed to continue.

## First use

1. Copy or attach [START_CHAT_EN.txt](START_CHAT_EN.txt). It includes the English method, operating knowledge, worked examples and any supplied executable sources.
2. Add your actual project, intent, relevant sources, existing work and available tools.
3. Entrust the useful contribution and identify actions the assistant may perform. Preserve its guide for later reentry.

You can begin with: “Use this competence for this work: […]. These are the sources and available means: […]. Carry out the entrusted work and retain what will let it continue. Involve me where […].” Adapt this to knowledge already present; it is not a compulsory questionnaire.

## Method

### Preserve the source before the account

When a request, decision or correction materially changes the work, retain the original wording or an exact reference accessible within the project. Keep uncertainty intact. Attribute the assistant's summary and inferences separately. If the source is missing, identify the reconstruction gap instead of recreating a quotation from memory.

### Follow events and effects

Record events that change reconstruction: a source, an AI proposal, an evidenced action, a correction, a change of authorization or a material unknown. Link effects to their evidence and observation time. A prepared file, a sent message and a received reply are different events. Preserve completed actions even when their original plan is abandoned.

### Correct without rewriting the past

A correction adds a new relation: identify the interpretation or instruction it supersedes and how continuation changes. Do not backdate a later understanding. Revoking permission changes what may happen now; it does not undo a completed effect. An AI summary cannot create authorization.

### Make the current position reconstructable

Keep a short entry linking still-valid sources, decisions, completed effects, unknowns and the relevant continuation. Detailed records and the current entry serve different purposes. Identified events and predecessor references help complex work; attributed, dated notes may suffice otherwise. At reentry, check relevant sources and disclose missing or changed coverage.

### Protect the work and improve reconstruction

Use the selected project's continuity surface and preserve concurrent contributions. If persistence is unavailable, return a note the person can retain. Avoid a universal diary and exclude secrets and unrelated private data. When reentry exposes a causal gap, improve the preservation method rather than merely adding more records.

## Meta and autological relations

This competence works on material continuity: what happened and which sources support it. It does not independently decide the meaning of a choice or the overall state of a project.

A meta relation appears when a reconstruction failure changes the preservation method. For example, a summary confused a proposal with approval; the revised method keeps both identifiable. This is distinct from autonomous execution, and a well-formed record does not prove infallible memory.

## Use in your environment

### In chat

Attach or paste START_CHAT_EN.txt, which contains the complete method, and add your context. The AI can work in the conversation's language. Retain the result and useful guidance if you want to resume in another chat.

### In an agent environment

Make the competence folder readable and have the agent read SKILL.md for the relevant work. Connect real sources and tools according to the environment's instructions. The kit does not install accounts, memory or recurring execution.

### With or without a kernel

With an existing kernel, connect the method to the competence or guide already responsible for the work. Without one, apply the instructions directly and preserve useful knowledge in the project or a reusable note.

## Application examples

- Reconstruct a decision later changed by a client.
- Preserve an action already performed after a change of direction.
- Hand over a project with identifiable sources, effects and unresolved questions.

[Read the examples](EXAMPLES.md). Cases illustrate possible use; they are not evidence of a recipient’s deployment.

## Learning and continuation

A handover reveals which links are sufficient and which are missing. Return the correction to the continuity method while leaving project decisions with their responsible owner.

## Resource files

- [SKILL.md](SKILL.md): English operating method.
- [START_CHAT_EN.txt](START_CHAT_EN.txt): complete English chat starter.
- [EXAMPLES.md](EXAMPLES.md): English application examples.
- [SKILL_IT.md](SKILL_IT.md), [AVVIO_CHAT_IT.txt](AVVIO_CHAT_IT.txt), [ESEMPI_IT.md](ESEMPI_IT.md): Italian method, starter and examples.
- [Common use guide](https://github.com/GrazianoGuiducci/maios-meta-skill/blob/bf2c9fcb63b7d1df638e85b7feea20da443e661e/docs/USE.md) and [conceptual guide](https://github.com/GrazianoGuiducci/maios-meta-skill/blob/bf2c9fcb63b7d1df638e85b7feea20da443e661e/docs/CONCEPTS.md).

With files, make this whole folder readable and use the host’s supported entry. Without persistent storage, retain a reentry note yourself. A method file does not establish configured tools, account access, scheduled execution or assimilation.


## Practical operating knowledge

[OPERATING_GUIDE.md](OPERATING_GUIDE.md) explains the decisions, conditions and means that make this method usable. The starter includes this knowledge; the folder also retains its directly readable sources.

## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). The downloaded kit includes LICENSE and NOTICE. Copyright 2026 Graziano Guiducci. Common repository guides are optional online references; the method and practical operating knowledge are included in this kit.


## Install in Codex

Read [INSTALL.md](INSTALL.md). Copy the complete `dnd-material-work-continuity` folder into your project's `.agents/skills/` directory, then invoke `$dnd-material-work-continuity` with your sources and intended work. Keep an existing copy for comparison instead of overwriting it.
