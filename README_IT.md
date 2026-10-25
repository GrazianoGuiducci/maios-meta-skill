# MAIOS Meta-Skill

**42 risorse per lavorare con l’AI, formare competenze e farne evolvere il metodo.**

[English](README.md) · [Risorse sul sito](https://maios.it/risorse/) · [Installare in Codex](docs/INSTALL_IT.md) · [Guida d’uso](docs/USO.md) · [Concetti](docs/CONCETTI.md)

La lingua principale della repository è l’inglese. Ogni risorsa comprende metodo operativo, guida, avvio completo ed esempi inglesi, con i corrispondenti file italiani collegati. I nomi tecnici delle skill restano uguali nelle due lingue; il catalogo conserva le intestazioni sorgenti originali.

L’edizione 0.3.0 recupera esempi articolati e sapere operativo dalle competenze native, inclusi gli strumenti portabili di continuità, orientamento e ispezione dei riceventi. Il [resoconto del trasferimento](docs/TRANSFER_REVIEW.md) spiega variazioni e portata delle prove. Le cartelle operative usano i nomi delle entry native; le rotte del sito conservano gli identificatori delle risorse.

## Primo uso

Scegli una risorsa e copia o allega tutto AVVIO_CHAT_IT.txt alla tua AI. Aggiungi intento, fonti, lavoro esistente e mezzi disponibili. Il file contiene il metodo completo. In un ambiente con file puoi rendere leggibile la cartella e usare SKILL_IT.md per la versione italiana.

## Installare in Codex

Scarica il kit e copia l'intera cartella canonica in `.agents/skills/` del progetto, oppure seleziona i kit con `python tools/install_skills.py`. La [guida d'installazione](docs/INSTALL_IT.md) spiega percorsi, cartelle esistenti, discovery, primo uso e aggiornamenti. L'installer richiede una destinazione esplicita e non sovrascrive skill esistenti.

La directory `skills/` contiene i 42 ingressi operativi. Gli [ID precedenti](docs/LEGACY_PATHS.md) restano utilizzabili nell'installer e nelle rotte del sito.

Un [caso illustrativo mostra come le competenze partecipano a un progetto MAIOS](docs/COMPETENZE_NEL_LAVORO.md).

Scopri [come adattare i metodi a formazione, cultura, servizi e ricerca](docs/ADATTARE.md). MKCV, il metodo di produzione video, è **beta e in apprendimento**.

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
| [KA — Kernel Assiomatico](skills/operate-ka/README_IT.md) | Contrasta bias cognitivi, filtri, presupposti e giudizi con cui i modelli linguistici (LLM) restringono il lavoro. Mantiene aperte le possibilità: intento, fonti, fatti e situazione reale formano il metodo, senza ridurre il progetto a ciò che l’AI conosce o presume. | Kernel semantico fondativo |
| [Operate FDLA](skills/operate-fdla/README_IT.md) | Riconosce e corregge presupposti, giudizi e interpretazioni con cui l’AI altera il lavoro. Contrasta il drift, cioè lo scostamento progressivo da intento, fonti e significato. Usa ciò che resta valido e ciò che emerge dalle conseguenze per correggere il lavoro mentre prende forma. | Funzione di correzione nel kernel |
| [D-ND Learn From Demonstration](skills/dnd-learn-from-demonstration/README_IT.md) | Comprende le decisioni dietro un esempio e porta l’apprendimento sostenuto dalle fonti nella competenza o implementazione che deve operare diversamente. | Competenza di apprendimento |
| [Situated Possibility Formation](skills/situated-possibility-formation/README_IT.md) | Rende comprensibili possibilità utili e sviluppa domande, relazioni o mezzi che possono trasformarle in lavoro. | Competenza generativa |
| [Semantic Relational Comprehension](skills/semantic-relational-comprehension/README_IT.md) | Comprende l’oggetto reale dietro le rappresentazioni e ne usa le ragioni per riformare domande, confronti e metodi. | Competenza di comprensione |
| [Cognitive Delegation Manager](skills/cognitive-delegation-manager/README_IT.md) | Collega contributi complementari attraverso intento, fonti accessibili, responsabilità concorrenti e ritorno significativo nel progetto. | Competenza di coordinamento |
| [Transfer Kernel Potential](skills/transfer-kernel-potential/README_IT.md) | Comprende ciò che deve continuare da una capacità sorgente e ne forma un’incarnazione utilizzabile autonomamente attraverso i mezzi del ricevente. | Metacompetenza di trasferimento |
| [Resource Need Formation](skills/resource-need-formation/README_IT.md) | Forma il bisogno di risorse da ciò che deve diventare possibile, prima di scegliere fornitore, strumento finanziario o altro portatore. | Competenza business |
| [Authorial Source Discrimination](skills/authorial-source-discrimination/README_IT.md) | Riconosce ciò che porta il significato dell’autore e lo conserva adattando quanto richiedono l’artefatto e la situazione ricevente selezionati. | Competenza editoriale |
| [Concept-to-Media Formation](skills/concept-to-media-formation/README_IT.md) | Forma il concetto e la relazione editoriale comuni da cui produrre media diversi conservando il significato sorgente. | Metacompetenza editoriale |
| [Semantic Timelapse Formation](skills/semantic-timelapse-formation/README_IT.md) | Forma istruzioni per immagini e film in codice fedeli alle sorgenti, componendo competenze visive, narrative e tecniche attraverso MKCV, beta e in apprendimento. | Competenza visiva generativa |
| [Onto-Skill](skills/onto-skill/README_IT.md) | Riconosce un principio trasferibile nel contributo dell’autore e lo rende operante nella competenza e nell’abilità pertinenti. | Metacompetenza generativa |
| [Form Cooperative Capability from Sources](skills/form-cooperative-capability-from-sources/README_IT.md) | Forma ed evolve la competenza di progetto che genera cooperazione da conoscenza sorgente, intento e partecipanti reali. | Metacompetenza generativa |
| [Funded Request Project Formation](skills/funded-request-project-formation/README_IT.md) | Forma soluzioni e progetti da bandi, challenge, RFP e collaborazioni finanziate, componendo il sapere esistente e sviluppando le competenze necessarie. | Metacompetenza generativa |
| [MAIOS Presentation Competence](skills/maios-presentation-competence/README_IT.md) | Forma presentazioni, spiegazioni e mappe navigabili che collegano identità reale, capacità generative del sistema e situazione del destinatario. | Competenza comunicativa situata |
| [Cinematic Screenwriting](skills/cinematic-screenwriting/README_IT.md) | Forma situazioni cinematografiche originali, treatment, scene e dialoghi, conservando autorialità e continuità causale con regia, interpretazione e montaggio. | Competenza di scrittura cinematografica |
| [Cinematic Direction](skills/cinematic-direction/README_IT.md) | Forma l’esperienza cinematografica di una scena attraverso messa in scena, punto di vista, camera, luce e relazione con interpretazione e montaggio. | Competenza di Design cinematografico |
| [Character & Object Performance](skills/character-performance/README_IT.md) | Forma l’interpretazione osservabile di personaggi e oggetti animati, collegando identità, intenzione autoriale, azione, reazione e scena. | Competenza di interpretazione animata |
| [Film Montage](skills/film-montage/README_IT.md) | Forma significato cinematografico attraverso relazioni fra inquadrature, durate, suono e transizioni, conservando fonte e conseguenze della scena. | Competenza di composizione temporale |

## Comporre le capacità

Puoi insegnare un lavoro collegando formazione delle competenze, esempi e conservazione del sapere; sviluppare possibilità collegando metodo, ricerca e attività; continuare un progetto conservando ragioni ed eventi; coordinare contributi fra assistenti attraverso fonti e continuità. Sono possibilità da comporre nel contesto, non pipeline obbligatorie.

Con un kernel esistente integra il contributo nelle competenze e guide già utili. Senza kernel applica direttamente il metodo. Non occorre caricare tutte le 42 risorse per ogni incarico. Strumenti, persistenza, account e risvegli dipendono dall’ambiente reale; il testo non li configura.

## Edizioni e apprendimento

Ogni risorsa dichiara nel catalogo la propria edizione: inglese principale, con sapere operativo italiano corrispondente. [Catalogo](catalog.json) e [manifest](dist/manifest.json) collegano file, lingue, versioni e pacchetti. Gli avvii includono sapere operativo, casi articolati e sorgenti degli strumenti runtime forniti. Le vecchie edizioni conservano il proprio stato storico.

La coerenza dei file verifica l’identità della distribuzione. L’uso in un altro assistente e l’assimilazione di una correzione si osservano nel lavoro successivo. Un riscontro utile conserva caso, differenza e ragione, anche quando l’esito resta invariato.

[Formazione e distribuzione](docs/DISTRIBUZIONE.md) · [Contributi e riscontri](https://github.com/GrazianoGuiducci/maios-meta-skill/issues)

## Licenza

[Apache-2.0](LICENSE). I kit scaricabili includono licenza e nota di attribuzione.

Origine e direzione: **Graziano Guiducci · MAIOS** · [maios.it](https://maios.it/).
