# Install a MAIOS skill in Codex

[Italiano](INSTALL_IT.md) · [Choose a resource](../README.md) · [Chat use](USE.md)

Each resource is a complete Agent Skills folder. Choose the capability you
need; its canonical folder contains `SKILL.md` and the supporting knowledge.
You can install one skill, several selected kits or the complete collection. Other skills are not prerequisites.

## Install from a downloaded kit

1. Download the resource ZIP from its MAIOS page and extract it. For FDLA,
   the extracted folder is `operate-fdla`.
2. Copy that whole folder into your project's `.agents/skills/` directory.
   The entry must be at `.agents/skills/operate-fdla/SKILL.md`, with its guide,
   examples and other files alongside it. Preserve an existing copy for review
   instead of overwriting it.
3. Open Codex in that project. Mention `$operate-fdla` and entrust a concrete
   task, supplying the source material it should use. Codex detects skill
   changes; restart the session if the new entry does not appear.

For example: “Use $operate-fdla to compare this summary with the author's
source below. Correct any change in meaning and explain the correction.”
Supply both texts after that request.

The installed entry remains English. For Italian work, ask for Italian output;
`SKILL_IT.md`, `README_IT.md` and the Italian examples remain available.

## Install from this repository

With Python 3.10 or later, open a terminal in a checked-out copy of this
repository. List the exact installable names:

```text
python tools/install_skills.py --list
```

Validate a selection without writing, then install it into the chosen project:

```text
python tools/install_skills.py --skill operate-fdla --dest "C:/Work/my-project/.agents/skills" --dry-run
python tools/install_skills.py --skill operate-fdla --dest "C:/Work/my-project/.agents/skills"
```

Use your project's actual path. POSIX paths work too. Repeat `--skill` to
select several resources. Stable resource IDs such as `fdla-correzione-ai`
resolve to the same canonical skill, `operate-fdla`. Use `--all` only when you
want the entire collection.

The installer reads release archives, checks their manifest and file digests,
and validates the complete selection before writing. It requires an explicit
destination and stops if any selected destination already exists. It never
changes Codex configuration, installs dependencies or executes kit scripts.
Each installed folder records its version and package digest in
`MAIOS_INSTALLATION.json`. An interrupted copy can leave a partial new folder;
`SKILL.md` becomes visible only after its supporting files are written.

## Check discovery and first use

Check the skill selector and the installed `SKILL.md` path. If the same name
is already available from another location, compare the entries and use the
one intended for this project; Codex does not merge duplicate skill names.

For a first task, observe whether Codex reaches the installed method and its
operating guide, uses the supplied sources, and produces a useful result.
An entry visible in a selector establishes discovery; the task establishes
only the behavior actually exercised. Keep useful knowledge in the project,
where the next session can recover it.

An update is a new package. Compare it with the existing competence and any
local learning before choosing how to integrate it. The installer deliberately
does not overwrite or automatically update an installed folder.

Other hosts have their own discovery and installation mechanisms. Preserve
the entire folder and follow that host's instructions. A ZIP here is a skill
kit; it is not a preconfigured plugin or an authenticated service.

Reference: [OpenAI's current skill documentation](https://learn.chatgpt.com/docs/build-skills).


[Compose the receiving project and optionally integrate MPK](USE.md): entry, sources, guides, functional comparison and preservation of local learning.
