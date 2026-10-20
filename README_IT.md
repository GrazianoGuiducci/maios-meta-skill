# MAIOS Meta-Skill

**25 risorse per lavorare con l’AI, formare competenze e farne evolvere il metodo.**

[English](README.md) · [Risorse sul sito](https://maios.it/risorse/) · [Installare in Codex](docs/INSTALL_IT.md) · [Guida d’uso](docs/USO.md) · [Concetti](docs/CONCETTI.md)

La lingua principale della repository è l’inglese. Ogni risorsa comprende metodo operativo, guida, avvio completo ed esempi inglesi, con i corrispondenti file italiani collegati. I nomi tecnici delle skill restano uguali nelle due lingue; il catalogo conserva le intestazioni sorgenti originali.

L’edizione 0.3.0 recupera esempi articolati e sapere operativo dalle competenze native, inclusi gli strumenti portabili di continuità, orientamento e ispezione dei riceventi. Il [resoconto del trasferimento](docs/TRANSFER_REVIEW.md) spiega variazioni e portata delle prove. Le cartelle operative usano i nomi delle entry native; le rotte del sito conservano gli identificatori delle risorse.

## Primo uso

Scegli una risorsa e copia o allega tutto AVVIO_CHAT_IT.txt alla tua AI. Aggiungi intento, fonti, lavoro esistente e mezzi disponibili. Il file contiene il metodo completo. In un ambiente con file puoi rendere leggibile la cartella e usare SKILL_IT.md per la versione italiana.

## Installare in Codex

Scarica il kit e copia l'intera cartella canonica in `.agents/skills/` del progetto, oppure seleziona i kit con `python tools/install_skills.py`. La [guida d'installazione](docs/INSTALL_IT.md) spiega percorsi, cartelle esistenti, discovery, primo uso e aggiornamenti. L'installer richiede una destinazione esplicita e non sovrascrive skill esistenti.

La directory `skills/` contiene i 25 ingressi operativi. Gli [ID precedenti](docs/LEGACY_PATHS.md) restano utilizzabili nell'installer e nelle rotte del sito.

## Scegliere una risorsa

La raccolta comprende competenze, metacompetenze, funzioni e fondamenti, senza una gerarchia di qualità. KA, Kernel Assiomatico, è un kernel semantico: le metacompetenze ne sono facoltà operative. Meta_Skill forma ed evolve competenze nello stesso campo; FDLA rende operativa la correzione nel lavoro, senza aggiungere un controllore esterno.

| Risorsa | Cosa permette di fare | Tipo |
| --- | --- | --- |
| [Meta-Activity](skills/meta-activity/README_IT.md) | Crea attività programmate complesse, capaci di comprendere cosa fare e di evolvere. | Metacompetenza |
| [Maintain Causal Task Continuity](skills/maintain-causal-task-continuity/README_IT.md) | Organizza il sapere del lavoro in una guida aggiornabile e mantiene un punto di rientro che permette all’AI di continuare dalle fonti pertinenti. | Competenza |
| [Essential Condensate Preserver](skills/essential-condensate-preserver/README_IT.md) | Riconosce quale conoscenza merita di continuare, ne conserva significato e contesto d’uso e indica dove integrarla o quando superarla. | Competenza |
| [Operator Concept Preserver](skills/operator-concept-preserver/README_IT.md) | Distingue le parole dell’autore dalle risposte dell’assistente, elimina duplicazioni e rumore e organizza i concetti utili con il loro riferimento sorgente. | Competenza |
| [Meta_Metodo](skills/meta-metodo/README_IT.md) | Ricostruisce ciò da cui il lavoro prende senso, collega i piani che partecipano e lascia cambiare domanda e metodo quando emergono relazioni nuove. | Metacompetenza |
| [Signal Intelligence](skills/signal-intelligence/README_IT.md) | Rilegge i segnali attraverso provenienza, tempo, contraddizioni e relazioni con il progetto; porta il sapere utile nella competenza che deve operare diversamente. | Competenza |
| [D-ND Skill Evolution Guard](skills/dnd-skill-evolution-guard/README_IT.md) | Comprende quale relazione ha cambiato il risultato e aggiorna la competenza pertinente, il suo ingresso o le proiezioni che devono continuare da quella differenza. | Metacompetenza |
| [Classify Content With Taxonomic Titles And Descriptions](skills/classify-content-with-taxonomic-titles-and-descriptions/README_IT.md) | Dà al titolo l’identità del contenuto e al sottotitolo la relazione che manca: uso, situazione o contenuto concreto. | Facoltà editoriale |
| [Form Public Meta-Skill Resources](skills/form-public-metaskill-resources/README_IT.md) | Forma una risorsa utilizzabile fuori dal contesto d’origine, conservando il metodo e rendendo chiaro come iniziare nella propria AI. | Metacompetenza |
| [D-ND Material Work Continuity](skills/dnd-material-work-continuity/README_IT.md) | Mantiene una traccia degli eventi materiali e distingue la fonte dell’operatore dalle interpretazioni dell’assistente e dagli effetti osservati. | Competenza |
| [Public Learning Promotion](skills/public-learning-promotion/README_IT.md) | Distingue il contributo riutilizzabile dai dettagli privati e propone una forma coerente con ciò che è stato osservato o costruito. | Competenza |
| [Situated Activity Evolution](skills/situated-activity-evolution/README_IT.md) | Comprende perché un’attività produce conoscenza utile, ripete risultati inutilizzati o incontra nuove possibilità e ne forma il seguito pertinente. | Competenza |
| [Maintain Kernel Knowledge](skills/maintain-kernel-knowledge/README_IT.md) | Costruisce una conoscenza raggiungibile dalle fonti e distingue ciò che il sistema è, ciò che ha mostrato e ciò che intende diventare. | Competenza |
| [UX-AI Kernel Design](skills/ux-ai-kernel-design/README_IT.md) | Adatta spiegazione, profondità e forma a ciò che la persona deve comprendere per orientare, correggere o continuare il lavoro. | Competenza UX-AI |
| [Projectable Presence](skills/projectable-presence/README_IT.md) | Forma una presenza riconoscibile e collegata al prodotto reale: cosa rappresenta, cosa conosce, cosa può fare e come continua la relazione. | Metacompetenza |
| [Maintain Repository Continuity](skills/maintain-repository-continuity/README_IT.md) | Comprende lo stato del repository selezionato e porta avanti le modifiche pertinenti preservando lavoro concorrente e identità della revisione condivisa. | Competenza tecnica |
| [Compose Agreement Contract](skills/compose-agreement-contract/README_IT.md) | Forma l’architettura dell’accordo a partire da parti, risultato atteso, scambi e dipendenze; la scrittura dà forma precisa a queste relazioni. | Competenza di dominio |
| [Evolve Editoriali System](skills/evolve-editoriali-system/README_IT.md) | Comprende come organizzare il sapere editoriale, le sue relazioni con i domini e la continuità delle opere, lasciando che l’esperienza cambi il sistema. | Metacompetenza organizzativa |
| [Meta_Skill Semantic Kernel](skills/meta-skill-semantic-kernel/README_IT.md) | Riconosce le capacità pertinenti, riusa o compone quelle presenti e forma il sapere operativo necessario a una nuova competenza quando emerge quella relazione. | Kernel generativo di competenze |
| [Kernel Plugin Incarnation](skills/kernel-plugin-incarnation/README_IT.md) | Forma l’incarnazione del kernel nel plugin e ne mantiene riconoscibili confini, mezzi, installazione, uso e apprendimento. | Metacompetenza di prodotto |
| [Incarnate Neutral Kernel Node](skills/incarnate-neutral-kernel-node/README_IT.md) | Fa iniziare un nodo dal proprio scopo e dai propri mezzi, distinguendo il pacchetto ricevuto dalla sua installazione e dal lavoro che vi nascerà. | Metacompetenza di trasferimento |
| [Kernel Continuum Awareness](skills/kernel-continuum-awareness/README_IT.md) | Rende raggiungibile la comprensione operativa del kernel e gli permette di riconoscere come una differenza cambia il proprio metodo e le incarnazioni pertinenti. | Metacompetenza del kernel |
| [Proto Movimento](skills/proto-movimento/README_IT.md) | Fa diventare l’esperienza di costruzione e trasferimento sapere utile a formare un nuovo kernel e il metodo con cui lo si forma. | Competenza di formazione del kernel |
| [KA — Kernel Assiomatico](skills/operate-ka/README_IT.md) | Orienta l’assistente a comprendere fonte, intento, situazione e possibilità, mantenendo il contesto e il metodo disponibili come parti del campo. | Kernel semantico fondativo |
| [Operate FDLA](skills/operate-fdla/README_IT.md) | Recupera le relazioni ancora valide e usa ciò che le conseguenze rendono comprensibile per correggere il lavoro mentre si forma. | Funzione di correzione nel kernel |

## Comporre le capacità

Puoi insegnare un lavoro collegando formazione delle competenze, esempi e conservazione del sapere; sviluppare possibilità collegando metodo, ricerca e attività; continuare un progetto conservando ragioni ed eventi; coordinare contributi fra assistenti attraverso fonti e continuità. Sono possibilità da comporre nel contesto, non pipeline obbligatorie.

Con un kernel esistente integra il contributo nelle competenze e guide già utili. Senza kernel applica direttamente il metodo. Non occorre caricare tutte le 25 risorse per ogni incarico. Strumenti, persistenza, account e risvegli dipendono dall’ambiente reale; il testo non li configura.

## Edizioni e apprendimento

L’edizione pubblica corrente è **0.3.2**: inglese principale, con corrispondenti file italiani. [Catalogo](catalog.json) e [manifest](dist/manifest.json) collegano file, lingue, versioni e pacchetti. Gli avvii includono sapere operativo, casi articolati e sorgenti degli strumenti runtime forniti. Le vecchie edizioni conservano il proprio stato storico.

La coerenza dei file verifica l’identità della distribuzione. L’uso in un altro assistente e l’assimilazione di una correzione si osservano nel lavoro successivo. Un riscontro utile conserva caso, differenza e ragione, anche quando l’esito resta invariato.

[Formazione e distribuzione](docs/DISTRIBUZIONE.md) · [Contributi e riscontri](https://github.com/GrazianoGuiducci/maios-meta-skill/issues)

## Licenza

[Apache-2.0](LICENSE). I kit scaricabili includono licenza e nota di attribuzione.

Origine e direzione: **Graziano Guiducci · MAIOS** · [maios.it](https://maios.it/).
