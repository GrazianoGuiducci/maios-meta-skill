# UX-AI Kernel Design

**Make an AI agent's work understandable**

[Italiano](README_IT.md) · Public edition 0.3.1 · English operating method

## What it does

Adapts explanation, depth and form to what a person needs to understand in order to guide, correct or continue the work.

## When to use it

When an AI system returns results but its user cannot understand what changed or how to participate.

An assistant can produce a useful result while leaving the person disoriented. This competence makes the relations that change the work understandable when they matter.
Explanation arises from the actual activity: what changes, why it matters, which sources support it and how the person can correct or continue. Its depth follows the need.

## First use

1. Copy or attach [START_CHAT_EN.txt](START_CHAT_EN.txt). It includes the English method, operating knowledge, worked examples and any supplied executable sources.
2. Add your actual project, intent, relevant sources, existing work and available tools.
3. Entrust the useful contribution and identify actions the assistant may perform. Preserve its guide for later reentry.

You can begin with: “Use this competence for this work: […]. These are the sources and available means: […]. Carry out the entrusted work and retain what will let it continue. Involve me where […].” Adapt this to knowledge already present; it is not a compulsory questionnaire.

## Method

### Explain at the point of use

Understand the current work and what the person needs to recognize in order to participate. Make a relation visible when it can change their next choice: a different source, a decision, a forming capability, a completed effect or an open question. Do not introduce a tutorial or component list merely because it exists.

### Connect event, meaning and intervention

Explain what happened, what it means here and what the person can do. Keep decision-changing uncertainty or conditions where the result is stated. Describe saved but inactive work accurately. Make correction, redirection or deeper explanation reachable through the available means.

### Adapt depth and representation

One sentence may suffice; a complex relation may need an example, comparison or wider view. Use the person's working vocabulary without assuming knowledge from role or silence. Choose text, images or interaction for their contribution to understanding and preserve access to depth. Brevity and comprehension are different measures.

### Let explanation correct the work

Reformulate from the person's position while preserving source and object. If an example or question exposes a lost premise, correct the work itself rather than only its tone. Repetition is not independent confirmation. Continue reformulation while it adds material understanding; the person's response can change question, method and form.

### Make work perceptible without taking over

In interfaces, connect proposals to real state and preserve the person's draft, selection, context and focus. New feedback should not erase ongoing work or simulate consent. Use design and implementation knowledge when building the surface. Explain operational reasons, sources and consequences without exposing or simulating private model reasoning.

### Learn from actual understanding

Do not measure success by how much explanation was emitted. Look for relevant consequences: the person finds the correction point, distinguishes proposal and effect, asks a more precise question or resumes with less reconstruction. Confusion, false control or excessive interruption teach what to change. Retain the lesson without imposing one universal response shape.

## Meta and autological relations

A meta relation can become visible when the system explains how a competence forms or changes and the person can guide that formation. Explanation does not become a second engine deciding domain truth.

This competence has an autological relation when it applies its method to the understandability of its own work: a confusing explanation becomes material for improving how it explains. This is distinct from agent autonomy and access to internal reasoning.

## Use in your environment

### In chat

Attach or paste START_CHAT_EN.txt, which contains the complete method, and add your context. The AI can work in the conversation's language. Retain the result and useful guidance if you want to resume in another chat.

### In an agent environment

Make the competence folder readable and have the agent read SKILL.md for the relevant work. Connect real sources and tools according to the environment's instructions. The kit does not install accounts, memory or recurring execution.

### With or without a kernel

With an existing kernel, connect the method to the competence or guide already responsible for the work. Without one, apply the instructions directly and preserve useful knowledge in the project or a reusable note.

## Application examples

- Explain a decision that needs the user's intervention.
- Show which sources support the state of an activity.
- Let everyday work progressively teach how to use the system's capabilities.

[Read the examples](EXAMPLES.md). Cases illustrate possible use; they are not evidence of a recipient’s deployment.

## Learning and continuation

Everyday work can gradually teach participation in the system. Useful evidence lies in how a person understands and intervenes in later situations, not in the presence of a panel or description.

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

Read [INSTALL.md](INSTALL.md). Copy the complete `ux-ai-kernel-design` folder into your project's `.agents/skills/` directory, then invoke `$ux-ai-kernel-design` with your sources and intended work. Keep an existing copy for comparison instead of overwriting it.
