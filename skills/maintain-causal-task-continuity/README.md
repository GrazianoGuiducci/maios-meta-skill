# Maintain Causal Task Continuity

**Resume a project with AI after an interruption**

[Italiano](README_IT.md) · Public edition 0.3.1 · English operating method

## What it does

Organises working knowledge in an evolving guide and keeps a reentry point that lets the AI continue from relevant sources.

## When to use it

Use it when a project spans sessions, moves to another assistant or depends on decisions a short summary would lose.

This competence preserves what makes it possible to resume work: intent, reasons for decisions, acquired knowledge, completed operations and open questions. The current position connects to a guide detailed enough for the assistant to continue through the method already developed.
Use it when a project spans sessions, collaborators, interruptions or a reduction in context. The depth of preservation follows what would be costly or impossible to reconstruct.

## First use

1. Copy or attach [START_CHAT_EN.txt](START_CHAT_EN.txt). It includes the English method, operating knowledge, worked examples and any supplied executable sources.
2. Add your actual project, intent, relevant sources, existing work and available tools.
3. Entrust the useful contribution and identify actions the assistant may perform. Preserve its guide for later reentry.

You can begin with: “Use this competence for this work: […]. These are the sources and available means: […]. Carry out the entrusted work and retain what will let it continue. Involve me where […].” Adapt this to knowledge already present; it is not a compulsory questionnaire.

## Method

### Preserve reasons and capabilities alongside facts

Identify the selected work, who determines its direction and where its knowledge lives. Retrieve the existing guide before creating another container. Keep the reason for a decision alongside the choice: which source or condition supports it, what it makes possible and what could change it. Distinguish the operator's words, observed facts, inferences and proposals. An open possibility can remain accessible without becoming the next assignment. When several competences need to continue, preserve each contribution, why it remains relevant and the method from which it resumes; a list of names does not transfer that capability.

### A reentry point that reaches the working knowledge

Keep a short current position with the objective, object of the work, decisive sources, result reached, completed effects and next movement. Connect it to the guide that explains intentions, method, corrections and substantial steps. The current position and guide are functions: they can share one document. Use the place that actually holds responsibility for the project and is accessible to the receiving assistant. If a page is regenerated, keep the reasons in a source that regeneration will not erase. If you can work only in chat, return a complete text to save and bring into the next session.

### Accumulate knowledge during the work

Integrate a new reason, discovery or correction where it changes the method, while the relationship is still understandable. Preserve references to evidence instead of duplicating every log. When the direction changes, update what follows and keep the previous situation attributable to its time; do not make the new understanding appear to have been available in the past. Before expanding the sources further, preserve any decisive relationship at risk of being lost. A single routine operation does not require a diary: write what will change a decision or a later reentry.

### Resume from the present

At reentry, bring the current request together with the current position, guide and necessary sources. Make the starting point recognisable. Check facts that may have changed when verification is relevant and accessible. Treat an earlier summary as a pointer for recovery, not as authority over the present. Preserve decisions that remain valid; resolve differences through the source and the operator's new input. Do not repeat an effect already completed because the summary is incomplete. Keep authorisations, results and proposals distinguishable. Continue when the relationship is sufficiently understood, without reloading the entire history out of habit.

## Meta and autological relations

The direct work is to let a project continue. A meta relation becomes relevant when experience changes how a competence organises the knowledge needed for subsequent work.

The relation is autological when continuity considers its own way of preserving knowledge: if a summary retained the result but lost the reason for a decision, the method can learn to make that reason accessible. This does not amount to unlimited memory or autonomous execution.

## Use in your environment

### In a chat

Copy or attach START_CHAT_EN.txt and add your working context. It includes the complete method in English. Keep the useful return for the next session; the assistant may converse in your language.

### In an agentic environment

Make the resource folder readable to the assistant, point it to SKILL.md, and choose the project documents that will carry continuity. Tools and actions depend on the actual environment and mandate.

### With or without a kernel

With an existing kernel, connect the method to the relevant competence and guides. Without one, the complete starter supplies the operating method for the work described here.

## Application examples

- Resume app development with decisions and unresolved problems available.
- Continue research after changing chats.
- Hand a business proposal to another assistant with its objective and reasons.

[Read the examples](EXAMPLES.md). Cases illustrate possible use; they are not evidence of a recipient’s deployment.

## Learning and continuation

When reentry requires explaining an already acquired relationship again, identify whether the knowledge, the connection or the use of the guide was missing. Correct that point in the project and, when reusable, in the continuity method.
A written guide makes knowledge available. A different later piece of work can show whether it is actually taken up. Keep only what changes the continuation; learning concerns accessible documents and instructions, not the model's weights.

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

Read [INSTALL.md](INSTALL.md). Copy the complete `maintain-causal-task-continuity` folder into your project's `.agents/skills/` directory, then invoke `$maintain-causal-task-continuity` with your sources and intended work. Keep an existing copy for comparison instead of overwriting it.
