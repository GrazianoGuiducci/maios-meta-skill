# Maintain Repository Continuity

**Share AI project work across repositories and collaborators**

[Italiano](README_IT.md) · Public edition 0.3.1 · English operating method

## What it does

Understands the selected repository state and carries relevant changes forward while preserving concurrent work and shared revision identity.

## When to use it

When people and assistants share a project and useful work should not remain hidden in a local checkout.

Saved work can remain invisible to the person who needs to continue it. This competence connects a local result to the project's shared source while keeping the selected change identifiable.
Continuity includes the reasons for the change, concurrent contributions and the revision a collaborator can actually read. Commit, sharing and product deployment remain distinct effects.

## First use

1. Copy or attach [START_CHAT_EN.txt](START_CHAT_EN.txt). It includes the English method, operating knowledge, worked examples and any supplied executable sources.
2. Add your actual project, intent, relevant sources, existing work and available tools.
3. Entrust the useful contribution and identify actions the assistant may perform. Preserve its guide for later reentry.

You can begin with: “Use this competence for this work: […]. These are the sources and available means: […]. Carry out the entrusted work and retain what will let it continue. Involve me where […].” Adapt this to knowledge already present; it is not a compulsory questionnaire.

## Method

### Identify the selected repository and result

Reach the repository that owns the work and its current instructions. Understand what should become shared and why. A containing folder may hold several repositories. Continuity matters at meaningful results or handovers; it does not require Git closure after every edit or publication during a read-only request.

### Understand the current identities

Distinguish working files, local commits, tracking references, verified remote revision and generated or ignored artifacts. Use the project's Git tools and access policy to inspect branch, differences and remote relation. A local tracking reference can be stale; a successful fetch does not mean selected content is already shared.

### Preserve concurrent contributions

Understand changes before staging. Select only the files or portions belonging to authorized work. Older or uncommitted work is not disposable noise. Integrate independent local and remote contributions while preserving both lines. Resolve overlapping changes according to their meaning rather than deleting valid work for an apparently clean state.

### Complete the authorized effect

When the current mandate covers committing and sharing, review the selected payload, perform proportionate checks, create a coherent commit and share it on the intended branch using the recipient's authentication policy. If authority or access is missing, preserve the work and identify the exact open step without claiming shared source.

### Verify what the collaborator can receive

After sharing, verify the remote revision and its relation to local work and tracking. If reconciliation produces different identities, explain which commits or contents correspond. Provide an exact reference with relevant reasons and checks. Reachable source does not prove reading, installation or execution; deployment and release need their own evidence.

### Continue the knowledge of the change

Preserve the useful change, its reason, revision, checks and any remaining local-only work in the project guide. If a later case exposes loss or unnecessary procedure, improve the continuity method. Its purpose is shared, reconstructable work rather than a Git ritual or forced synchronization of every repository.

## Meta and autological relations

This is a technical source-continuity competence. The number of repositories or agents does not automatically give it a meta level.

Its method can become an object of learning when a handover shows that shared work was not reachable by the collaborator. Repairing that entry changes continuity practice. This differs from an autonomous process that pushes on a schedule and does not authorize one.

## Use in your environment

### In chat

Attach or paste START_CHAT_EN.txt, which contains the complete method, and add your context. The AI can work in the conversation's language. Retain the result and useful guidance if you want to resume in another chat.

### In an agent environment

Make the competence folder readable and have the agent read SKILL.md for the relevant work. Connect real sources and tools according to the environment's instructions. The kit does not install accounts, memory or recurring execution.

### With or without a kernel

With an existing kernel, connect the method to the competence or guide already responsible for the work. Without one, apply the instructions directly and preserve useful knowledge in the project or a reusable note.

## Application examples

- Share a change without including another author's files.
- Reconcile independent local and remote contributions.
- Give another assistant the exact revision to read.

[Read the examples](EXAMPLES.md). Cases illustrate possible use; they are not evidence of a recipient’s deployment.

## Learning and continuation

A later case shows whether work reaches shared source without loss or repeated reconstruction. A technical check remains attached to the revision it actually verified.

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

Read [INSTALL.md](INSTALL.md). Copy the complete `maintain-repository-continuity` folder into your project's `.agents/skills/` directory, then invoke `$maintain-repository-continuity` with your sources and intended work. Keep an existing copy for comparison instead of overwriting it.
