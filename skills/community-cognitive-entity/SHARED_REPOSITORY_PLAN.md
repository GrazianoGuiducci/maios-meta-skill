# Proposed shared repository workflow
## Collecting experiments, improving the method and making the learning available to everyone

**Proposal only.** No GitHub issue form, automation, external forum monitor or shared repository service is installed by this document.

### A simple beginning: reuse the existing public repository

A separate repository may be useful later, but the experimental method and its revision history already have a public home. **During this draft review**, the skill resides on a pull-request branch rather than in a stable published release: direct links to it are not yet a permanent canonical distribution path. The public entry and contribution URL should be updated to a stable main/release location **when the review is actually accepted**, before inviting broad participation. Initially, use **issues and pull requests in the repository holding this skill**. This avoids a second source that participants would need to discover and reconcile.

The Community discussion remains the public conversation. GitHub holds the **versioned method** and an inspectable set of **learning notes**. Either place can receive a contribution; neither automatically changes the other.

Suggested flow:

```text
person + their AI explore a situation
    -> AI offers a short, human-reviewed public account
    -> person chooses Community reply and/or GitHub issue
    -> maintainer understands and links the contribution
    -> shared learning notes index the public return (including review-pending or disagreement)
    -> a qualified insight may be incorporated into the shared method
    -> if future AI behavior should change, a reviewed pull request updates the skill
    -> a versioned release makes the changed method available to other participants
    -> each person chooses if and how to use the new version locally
```

### A minimal issue template

If contributors begin returning work regularly, a GitHub Issue Form could prompt for:

- **What happened?** The task or situation, with private details omitted.
- **What did you and your AI learn?** Include an observation, difficulty or unexpected outcome.
- **What changed?** A question, decision, existing method, new reusable ability or the human–AI interaction.
- **What supports that account?** A public link, reproducible example or an explanation of what is still uncertain.
- **What could another participant investigate?**
- **Which version of the method did you use?** Optional but useful for comparing changes.

Do not require contributors to reveal identities, private code, proprietary files, system prompts or personal conversations. Unanswered sections should not block a relevant contribution.

### Review and integration

A maintainer first reads the actual contribution and its origin. The contributor's observation and the maintainer's interpretation remain distinct.

A contribution may be:
- added to the shared notes as an attributed observation;
- integrated into the skill because it changes a reusable way of working;
- retained as a context-specific alternative;
- flagged as an unresolved conflict or research question;
- left outside the shared resource if it is irrelevant, unverifiable in a consequential way, or cannot be shared with permission.

An accepted skill change should identify the earlier behavior, the causal difference, the new expected behavior and the conditions that justify it. If the experimental instructions themselves asked an AI to display the behavior under study, that is part of the observation conditions; it does not independently demonstrate spontaneous recognition. Do not require a separate baseline for each report, but allow an optional comparison that materially discriminates claims. Preserve previous versions. Use an ordinary pull request and review to avoid silently changing the method used by others.

### Automation worth considering after the first real returns

**Useful, limited automation:**
1. A GitHub Issue Form creates consistently readable submissions.
2. A GitHub Action checks a proposed update's file presence, metadata, links, version consistency and that example claims are clearly marked as illustrative where appropriate.
3. A pull request reports the changed method and the contributions supporting it.
4. Published releases and a visible changelog tell participants a newer version is available.

These tools can organize submissions and detect mechanical errors. They cannot determine whether an AI actually learned, whether a person's account is valid, or which contradictory interpretation should prevail.

**Optional later:** a forum watch using a platform-supported API or feed, if actually available and compliant with its terms, could notify maintainers of new replies. It should not silently download private content, generate pseudo-consensus, merge changes or publish responses. The live forum state and an accepted knowledge contribution are distinct.

### When a dedicated shared repository would help

Consider a separate public repository if the collaboration acquires independent maintainers, its own participant roles, issue volume or product identity. An openly accessible submissions index may be more useful initially than a new platform: people need to see **which returns were received, which changed the method and which remain disputed**, without counting duplicated versions of one report as independent. The same public source should have a clear canonical version and a path to its next release. Keep a single canonical skill location and clearly link or redirect older entries. A new repository by itself does not make the method more intelligent or the community synchronized.

### Proposed first public package

For the initial invitation, offer:
1. A plain-language [introduction](README.md).
2. The complete [AI instructions](START_CHAT_EN.txt), so anyone can paste them into their own AI.
3. The [shared learning notes](SHARED_LEARNINGS.md), initially empty but visibly ready for qualified returns.
4. A link to [how to contribute](CONTRIBUTING.md).

No participant needs to install special tooling. Before publishing the invitation, choose whether it belongs in the originating thread or a new linked topic according to the real conversation and forum guidance. Do not automatically repost the same invitation across both. If many participants later need repository-native installation, add it through the actual receiving environments rather than treating that need as established from the outset.
