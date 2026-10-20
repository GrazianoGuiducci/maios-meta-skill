"""Render the English primary README and its Italian counterpart."""


def render(root, resources):
    for lang in ('en','it'):
        en=lang=='en'
        label='Resource' if en else 'Risorsa'
        effect='What it enables' if en else 'Cosa permette di fare'
        kind='Type' if en else 'Tipo'
        rows=[f'| {label} | {effect} | {kind} |','| --- | --- | --- |']
        for resource in resources:
            r=resource[lang]
            guide=resource['languages'][lang]['guide']
            rows.append(f"| [{resource['name']}]({guide}) | {r.get('does',r.get('what_it_does'))} | {r.get('kind',r.get('type'))} |")
        if en:
            text='''# MAIOS Meta-Skill

**25 resources for working with AI, forming competences and evolving their methods.**

Turn knowledge developed through MAIOS work into methods you can use in your own chat or agentic environment. Each resource includes an operating method, a complete chat starter, a guide and application examples.

[Italiano](README_IT.md) · [Explore the resources](https://maios.it/resources/) · [Use guide](docs/USE.md) · [Concepts](docs/CONCEPTS.md)

## Start with your work

Choose a resource below, open its **START_CHAT_EN.txt**, then copy or attach the whole file to your AI conversation. Add your intent, sources, existing work and available means. The starter contains the complete method. With file access, make the whole competence folder readable and use SKILL.md as its entry.

English is the primary language of methods, guides, examples and starters. Italian versions are included and linked. Original competence names stay the same across languages.

Edition 0.3.0 restores developed examples and practical operating knowledge from the native competences, including the portable continuity, orientation and receiver-inspection tools. The [transfer record](docs/TRANSFER_REVIEW.md) explains what changed and the scope of the checks. Native entry names identify the operating folders; website routes retain their stable resource IDs.

## Choose a resource

The collection includes operating competences, metacompetences, functions and kernel foundations. These types describe different contributions rather than a quality hierarchy. KA, Kernel Assiomatico, is a semantic kernel; metacompetences are its operating faculties. Meta_Skill forms and evolves competences in that same field. FDLA makes causal correction operative within the work, without another external controller.

'''+ '\n'.join(rows)+'''

## Compose capabilities around a real task

- **Teach your AI a way of working:** combine competence formation, learning from examples and useful knowledge preservation. A correction can improve both the practical method and how it is learned.
- **Develop a project's possibilities:** combine situated method formation, signal intelligence and activity formation when their knowledge changes what becomes possible.
- **Continue a project:** connect causal continuity, material event history and essential knowledge. Preserve decision reasons, collaborators and completed effects across sessions.
- **Coordinate assistants:** combine situated method, recipient formation and continuity to preserve complementary contributions through shared sources and reasons.

These are possible compositions, not compulsory pipelines.

## Use in your environment

With an existing kernel, integrate the selected capability into the knowledge and guides already serving the project. Without a kernel, use the included method directly. You do not need to load all25 resources for one assignment.

Host tools, persistence, accounts and recurring activation depend on the actual environment. A method file does not configure them. The [use guide](docs/USE.md) explains how to connect the method to real means and preserve the knowledge needed for reentry.

## Editions and learning

The current public edition is **0.3.1**, with English public methods and Italian counterparts. The [catalogue](catalog.json) connects files, languages and versions; [dist/manifest.json](dist/manifest.json) records package identities and file hashes. Packages contain both languages, operating knowledge and worked examples. Starters include that knowledge and the sources of supplied runtime tools. Older downloadable editions retain their own meaning and history.

File consistency establishes delivery identity. Actual use in another assistant and assimilation of a correction are observed through later work, including unchanged outcomes and limitations. Preserve a case, the difference noticed and its reason when offering feedback.

[How resources are formed and distributed](docs/DISTRIBUTION.md) · [Report an issue or contribute](https://github.com/GrazianoGuiducci/maios-meta-skill/issues)

## License

[Apache-2.0](LICENSE). Downloadable kits include the license and attribution notice.

Origin and direction: **Graziano Guiducci · MAIOS** · [maios.it](https://maios.it/).
'''
        else:
            text='''# MAIOS Meta-Skill

**25 risorse per lavorare con l’AI, formare competenze e farne evolvere il metodo.**

[English](README.md) · [Risorse sul sito](https://maios.it/risorse/) · [Guida d’uso](docs/USO.md) · [Concetti](docs/CONCETTI.md)

La lingua principale della repository è l’inglese. Ogni risorsa comprende metodo operativo, guida, avvio completo ed esempi inglesi, con i corrispondenti file italiani collegati. I nomi originali delle competenze restano uguali nelle due lingue.

L’edizione 0.3.0 recupera esempi articolati e sapere operativo dalle competenze native, inclusi gli strumenti portabili di continuità, orientamento e ispezione dei riceventi. Il [resoconto del trasferimento](docs/TRANSFER_REVIEW.md) spiega variazioni e portata delle prove. Le cartelle operative usano i nomi delle entry native; le rotte del sito conservano gli identificatori delle risorse.

## Primo uso

Scegli una risorsa e copia o allega tutto AVVIO_CHAT_IT.txt alla tua AI. Aggiungi intento, fonti, lavoro esistente e mezzi disponibili. Il file contiene il metodo completo. In un ambiente con file puoi rendere leggibile la cartella e usare SKILL_IT.md per la versione italiana.

## Scegliere una risorsa

La raccolta comprende competenze, metacompetenze, funzioni e fondamenti, senza una gerarchia di qualità. KA, Kernel Assiomatico, è un kernel semantico: le metacompetenze ne sono facoltà operative. Meta_Skill forma ed evolve competenze nello stesso campo; FDLA rende operativa la correzione nel lavoro, senza aggiungere un controllore esterno.

'''+ '\n'.join(rows)+'''

## Comporre le capacità

Puoi insegnare un lavoro collegando formazione delle competenze, esempi e conservazione del sapere; sviluppare possibilità collegando metodo, ricerca e attività; continuare un progetto conservando ragioni ed eventi; coordinare contributi fra assistenti attraverso fonti e continuità. Sono possibilità da comporre nel contesto, non pipeline obbligatorie.

Con un kernel esistente integra il contributo nelle competenze e guide già utili. Senza kernel applica direttamente il metodo. Non occorre caricare tutte le25 risorse per ogni incarico. Strumenti, persistenza, account e risvegli dipendono dall’ambiente reale; il testo non li configura.

## Edizioni e apprendimento

L’edizione pubblica corrente è **0.3.1**: inglese principale, con corrispondenti file italiani. [Catalogo](catalog.json) e [manifest](dist/manifest.json) collegano file, lingue, versioni e pacchetti. Gli avvii includono sapere operativo, casi articolati e sorgenti degli strumenti runtime forniti. Le vecchie edizioni conservano il proprio stato storico.

La coerenza dei file verifica l’identità della distribuzione. L’uso in un altro assistente e l’assimilazione di una correzione si osservano nel lavoro successivo. Un riscontro utile conserva caso, differenza e ragione, anche quando l’esito resta invariato.

[Formazione e distribuzione](docs/DISTRIBUZIONE.md) · [Contributi e riscontri](https://github.com/GrazianoGuiducci/maios-meta-skill/issues)

## Licenza

[Apache-2.0](LICENSE). I kit scaricabili includono licenza e nota di attribuzione.

Origine e direzione: **Graziano Guiducci · MAIOS** · [maios.it](https://maios.it/).
'''
        version=resources[0]['version']
        text=text.replace('all25','all 25').replace('tutte le25','tutte le 25').replace('**0.3.1**',f'**{version}**')
        if en:
            text=text.replace('[Use guide](docs/USE.md)', '[Install in Codex](docs/INSTALL.md) · [Use guide](docs/USE.md)', 1)
            text=text.replace('## Choose a resource', '''## Install in Codex

Download a kit and copy its complete canonical folder into your project's `.agents/skills/` directory, or select kits with `python tools/install_skills.py`. The [installation guide](docs/INSTALL.md) covers exact paths, collision handling, discovery, first use and updates. The installer requires an explicit destination and never overwrites an existing skill.

The `skills/` directory contains the 25 operating entries. [Previous resource IDs](docs/LEGACY_PATHS.md) still work as installer selections and website routes.

## Choose a resource''', 1)
            text=text.replace('Original competence names stay the same across languages.', 'Canonical skill names stay the same across languages; original source titles remain recorded in the catalogue.')
        else:
            text=text.replace('[Guida d’uso](docs/USO.md)', '[Installare in Codex](docs/INSTALL_IT.md) · [Guida d’uso](docs/USO.md)', 1)
            text=text.replace('## Scegliere una risorsa', '''## Installare in Codex

Scarica il kit e copia l'intera cartella canonica in `.agents/skills/` del progetto, oppure seleziona i kit con `python tools/install_skills.py`. La [guida d'installazione](docs/INSTALL_IT.md) spiega percorsi, cartelle esistenti, discovery, primo uso e aggiornamenti. L'installer richiede una destinazione esplicita e non sovrascrive skill esistenti.

La directory `skills/` contiene i 25 ingressi operativi. Gli [ID precedenti](docs/LEGACY_PATHS.md) restano utilizzabili nell'installer e nelle rotte del sito.

## Scegliere una risorsa''', 1)
            text=text.replace('I nomi originali delle competenze restano uguali nelle due lingue.', 'I nomi tecnici delle skill restano uguali nelle due lingue; il catalogo conserva le intestazioni sorgenti originali.')
        (root/('README.md' if en else 'README_IT.md')).write_text(text,encoding='utf-8',newline='\n')
