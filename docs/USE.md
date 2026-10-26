# Use one MAIOS competence or compose a skill system in your project


## Start with the work you want to make possible

A competence gives an AI a method: what to understand in a situation, which sources matter, what should change a decision, and how useful learning can continue. You can use one competence, compose several in a project, or make a complete public collection available to your agentic environment.

The public MAIOS collection is at [maios-meta-skill](https://github.com/GrazianoGuiducci/maios-meta-skill). At the time of this edition it contains 42 bilingual resource kits with operating methods, guides, developed examples, and complete chat starters. You do not need all of them for every assignment. Installing every folder does not by itself make an agent able to select and exercise them.

## When one competence is enough

To make a complex system understandable, use [MAIOS Presentation Competence](https://maios.it/resources/presentare-sistemi-in-evoluzione/). Open its complete chat starter and copy or attach it to your conversation. Add your real task, actual system sources, relevant audience context, and available tools.

For example: “I need to explain a digital archive to visitors and curators. Here are the documents describing its contents and capabilities. Form a recognizable first explanation, connect it to how the archive actually works, and make its sources reachable for readers who want more depth.”

This is an illustrative assignment, not a claim about an existing customer archive. The method must adapt to the sources supplied rather than inventing capabilities. If the chat does not retain project files across sessions, preserve a short guide with source links, reasons for choices, corrections, and the next point of entry.

## When other competences can contribute

A presentation with a diagram may need knowledge about spatial relationships. A system change may require source reentry. Confusion observed at a first encounter can change the way the presentation competence operates next time.

Compose as needed with public resources such as:

- [Meta_Skill Semantic Kernel](https://maios.it/resources/creare-comporre-competenze/) to recognize, form, and compose competences.
- [UX-AI Kernel Design](https://maios.it/resources/comprendere-lavoro-agente/) for comprehensible AI behavior and orientation.
- [Concept-to-Media Formation](https://maios.it/resources/dal-concetto-ai-media/) to preserve meaning across explanatory media.
- [Maintain Causal Task Continuity](https://maios.it/resources/continuita-del-lavoro-ai/) for reasons and continuity across work sessions.
- [D-ND Skill Evolution Guard](https://maios.it/resources/evolvere-competenze/) to return reusable learning to the competence that should work differently.

These are potential contributions, **not a fixed pipeline**. A competence participates when its actual knowledge changes the work, not simply because its name is listed.

## When you want the full public collection in Codex

The collection ships an installer for Agent Skills folders. In your checkout, first inspect what is available:

```bash
python tools/install_skills.py --list
```

Choose the actual destination in your project. For one competence:

```bash
python tools/install_skills.py --skill maios-presentation-competence --dest /YOUR/PROJECT/.agents/skills --dry-run
python tools/install_skills.py --skill maios-presentation-competence --dest /YOUR/PROJECT/.agents/skills
```

For the entire public collection, only after checking the intended project and its existing skills:

```bash
python tools/install_skills.py --all --dest /YOUR/PROJECT/.agents/skills --dry-run
python tools/install_skills.py --all --dest /YOUR/PROJECT/.agents/skills
```

These paths are placeholders. The installer checks versions, package digests, and manifest membership; it does not overwrite an existing skill folder. It does not install an entire MAIOS runtime, provide credentials, configure services, or grant authority over accounts. Compare incoming versions with any knowledge your project has already acquired before integrating an update. See the [installation guide](https://github.com/GrazianoGuiducci/maios-meta-skill/blob/main/docs/INSTALL.md).

For another host, preserve the capability and its complete folder, but use that host's actual discovery and configuration mechanisms. Accessible instructions are not necessarily discovered or exercised.

## Give the receiving project its own working identity

The public kit supplies transferable know-how; your project supplies the object it works on. Its own entry should make its purpose, reliable sources, current work, actual tools and effects, relevant competences, and knowledge-continuation guide recoverable.

Do not copy the source repository's `AGENTS.md` automatically. It governs maintainers of the public collection, not your organization's work. A small receiving-project guide might identify:

```text
Project purpose: [the real work and intended result]
Project sources: [documents, code and data you own]
Current guide: [present status, decisive reasons, next entry]
Competences: use reachable skills when they change the task;
             do not load every skill on every turn.
Means and authority: [tools actually available and authorized effects]
Learning return: change the relevant competence/guide when work teaches it.
```

For a new recipient or migration, [Incarnate Neutral Kernel Node](https://maios.it/resources/avviare-nodo-ai/) and [Transfer Kernel Potential](https://maios.it/resources/trasferire-capacita-kernel/) distinguish recipient-owned identity and state from shared capability. [Kernel Continuum Awareness](https://maios.it/resources/coerenza-kernel-ai/) helps preserve still-causal knowledge as means and competences evolve.

## Observe first use and preserve the next movement

These are different observations:

**Installed:** the files were placed in the intended location.  
**Reachable:** the receiving environment can read them.  
**Discoverable:** the entry is found through the host's mechanism.  
**Exercised:** a concrete task shows that the competence actually changed understanding or action.  
**Assimilated into later work:** a different later case benefits from a correction without asking the person to reconstruct it.

Give the assistant a concrete assignment and observe what it does. It can explain which source and reason changed a decision; that report alone is not proof of later assimilation. Preserve meaningful decisions, results, and changed methods in the project guide. When experience teaches a reusable distinction, return it to the competence that should work differently, rather than accumulating summaries.

If your environment cannot preserve project files, use the complete chat starter and keep the continuation guide yourself. The method remains useful, while persistence and effects depend on actual host capabilities.

## What you have received

You have made one or more **public MAIOS competences** available to your project. They may be composed with KA, FDLA, Meta_Skill and continuity faculties insofar as the actual work and receiver make them relevant. They do not transfer developers' private configuration, credentials, outstanding tasks, or authority over your systems. Capability becomes observable through use and its consequences.

**Collection:** [maios-meta-skill](https://github.com/GrazianoGuiducci/maios-meta-skill) · **General use guide:** [public documentation](https://github.com/GrazianoGuiducci/maios-meta-skill/blob/main/docs/USE.md).

## With MAIOS Project Kernel 5.1.0, optionally

[MPK](https://github.com/GrazianoGuiducci/maios-project-kernel) is a separate product with a semantic system, competence formation, host adaptation and continuity. Its package uses its own installer, Python >=3.11 and preview/apply commands; follow [INSTALL](https://github.com/GrazianoGuiducci/maios-project-kernel/blob/main/package/INSTALL.md). This collection’s installer copies kits; it does not perform MPK installation or migration.

Before integrating, compare function, responsible owner, method and acquired local knowledge as well as names. For example, an MPK project already has competence formation: retain that owner and connect Onto-Skill for practical principle-to-ability discrimination where useful. Use cooperation when independent people or systems participate; copying folders alone is not cooperation.

| Collection function | Function already in MPK | Useful integration |
| --- | --- | --- |
| Meta_Skill, KA/FDLA and continuity | System and formation with local knowledge and reentry | Compare methods, preserve the local owner and connect only the useful delta |
| Onto-Skill | Formation of project-pertinent capabilities | Bring the condition and changed decision into the responsible guide |
| Cooperation | Participation of competences in work | Add independent-contributor knowledge when that relationship actually exists |
| MPC | Project knowledge and sources | Present the actual object without assigning all MAIOS properties to it |

Keep the contribution in the project’s own source and make it reachable through the host’s native entry. An incoming kit does not overwrite installed local learning. Documented compatibility, installation, discovery, exercise and later use retain their own observations; this guide does not establish integration in every host.

## When recurrence is useful


Use the environment's actual controller to create or update an entrusted activity. Recover an existing job when it has the same mandate. Read back identity, saved instructions, cadence or event, timezone and destination. A configured job and an observed future execution remain different facts.

When no controller is available, the assistant can prepare the activity and perform feasible work during the present session. Recurrence becomes actual when a real mechanism activates it. Local and web environments can differ in file access and availability; follow their current contracts for the selected setup.
