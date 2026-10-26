# Usare una competenza MAIOS o comporre un sistema di skill nel tuo progetto


## Parti dal lavoro che vuoi rendere possibile

Una competenza porta all'AI un metodo: quali aspetti di una situazione comprendere, quali sorgenti raggiungere, che cosa cambia una scelta e come conservare ciò che il lavoro insegna. Puoi usare una sola competenza, comporne alcune in un progetto oppure rendere disponibile un'intera raccolta al tuo sistema agentico.

Le risorse MAIOS sono indipendenti dal progetto che le ha generate. La raccolta pubblica è nel repository [maios-meta-skill](https://github.com/GrazianoGuiducci/maios-meta-skill). Contiene, alla data di questa edizione, 42 kit con metodo, guida, esempi, versioni italiane e inglesi e avvii per la chat. Non serve adottarle tutte per ottenere valore. E installarle tutte non significa, da solo, che un agente sappia selezionarle e utilizzarle.

## Quando ti basta una singola competenza

Se devi rendere comprensibile un sistema complesso, usa [MAIOS Presentation Competence](https://maios.it/risorse/presentare-sistemi-in-evoluzione/). Nella pagina trovi un avvio completo che puoi incollare o allegare a una conversazione. Aggiungi il tuo compito, le sorgenti reali del sistema, che cosa sai del destinatario e gli strumenti disponibili.

Per esempio: «Devo presentare un archivio digitale a visitatori e curatori. Questi sono i documenti che ne descrivono contenuti e funzioni. Forma una prima spiegazione riconoscibile, collegala al modo in cui l'archivio funziona e rendi raggiungibili le sorgenti per chi vuole approfondire».

È un incarico illustrativo: il metodo si deve adattare alle caratteristiche dell'archivio che fornisci, senza attribuirgli funzioni o risultati non documentati. Se la chat non conserva file o contesto fra sessioni, mantieni tu una guida breve con sorgenti, ragioni delle scelte, correzioni e punto da cui proseguire.

## Quando più competenze possono partecipare

Un compito può richiedere conoscenze diverse. Se la presentazione contiene un diagramma, serve comprendere quali oggetti e relazioni debbano essere visibili; se cambia il sistema presentato, serve recuperare la sorgente aggiornata; se un visitatore non comprende la pagina, l'esperienza può migliorare il metodo di presentazione.

Puoi comporre MPC con risorse già pubbliche, secondo ciò che il tuo progetto rende pertinente:

- [Meta_Skill Semantic Kernel](https://maios.it/risorse/creare-comporre-competenze/): riconoscere, formare e comporre capacità.
- [UX-AI Kernel Design](https://maios.it/risorse/comprendere-lavoro-agente/): rendere comprensibile l'attività di un agente e mantenerne il focus.
- [Concept-to-Media Formation](https://maios.it/risorse/dal-concetto-ai-media/): formare un concetto coerente prima dei suoi diversi media.
- [Maintain Causal Task Continuity](https://maios.it/risorse/continuita-del-lavoro-ai/): conservare ragioni e stato del lavoro per riprenderlo.
- [D-ND Skill Evolution Guard](https://maios.it/risorse/evolvere-competenze/): restituire una differenza utile alla competenza che dovrà comportarsi diversamente.

Questa è una composizione **possibile**, non una sequenza obbligatoria. Una competenza partecipa quando la sua conoscenza cambia il modo di comprendere o svolgere il lavoro, non perché il suo nome appare in un elenco.

## Quando vuoi rendere disponibile l'intera raccolta in Codex

La raccolta pubblica offre un installer per le cartelle Agent Skills. Nel checkout del repository esegui anzitutto:

```bash
python tools/install_skills.py --list
```

Scegli una **destinazione concreta** nel tuo progetto. Per installare una skill:

```bash
python tools/install_skills.py --skill maios-presentation-competence --dest /PERCORSO/DEL/PROGETTO/.agents/skills --dry-run
python tools/install_skills.py --skill maios-presentation-competence --dest /PERCORSO/DEL/PROGETTO/.agents/skills
```

Per l'intera raccolta, dopo aver controllato il progetto e le skill già presenti:

```bash
python tools/install_skills.py --all --dest /PERCORSO/DEL/PROGETTO/.agents/skills --dry-run
python tools/install_skills.py --all --dest /PERCORSO/DEL/PROGETTO/.agents/skills
```

I percorsi sono segnaposto, non percorsi da copiare letteralmente. L'installer controlla versioni, manifest e impronte; non sovrascrive cartelle già esistenti. Non installa un runtime MAIOS, non configura account o strumenti e non abilita autonomamente servizi. Se una skill esiste già, confrontane il sapere e l'eventuale apprendimento locale prima di integrare una nuova edizione. Consulta [la guida di installazione](https://github.com/GrazianoGuiducci/maios-meta-skill/blob/main/docs/INSTALL_IT.md).

Per un'altra piattaforma, conserva il metodo e la struttura delle cartelle, ma utilizza **il meccanismo di discovery realmente previsto da quell'ambiente**. Una cartella accessibile può non essere scoperta o esercitata dal modello.

## Come il progetto diventa il proprio ricevente

Le skill sono sapere trasferibile; il tuo progetto porta l'oggetto concreto su cui quel sapere deve lavorare. Un ingresso di progetto deve permettere all'AI di trovare il lavoro attuale, le sorgenti affidabili, gli strumenti disponibili, le competenze pertinenti e la guida in cui conservare motivi, decisioni e conseguenze.

Non è necessario copiare l'`AGENTS.md` della repository che distribuisce le skill: quel file governa il **manutentore della raccolta**, non la tua organizzazione. Forma invece le istruzioni del tuo progetto secondo il suo scopo. Un esempio minimo, da adattare, può indicare:

```text
Scopo del progetto: [lavoro reale e risultati desiderati]
Sorgenti del progetto: [documenti, codice e dati posseduti]
Stato/guida corrente: [punto da cui riprendere, ragioni e aperti]
Competenze: usa le skill raggiungibili che cambiano il lavoro,
             senza caricarle tutte a ogni incarico.
Mezzi e autorità: [strumenti realmente disponibili; effetti autorizzati]
Ritorno: ciò che si apprende cambia l'owner e la guida pertinenti.
```

Se stai formando un ricevente nuovo o migrando una capacità, usa [Incarnate Neutral Kernel Node](https://maios.it/risorse/avviare-nodo-ai/) e [Transfer Kernel Potential](https://maios.it/risorse/trasferire-capacita-kernel/) per distinguere l'identità del progetto dalle sorgenti condivise. [Kernel Continuum Awareness](https://maios.it/risorse/coerenza-kernel-ai/) permette di ritrovare relazioni ancora causali quando le competenze o gli strumenti cambiano.

## Come osservare il primo utilizzo e continuare

Dopo l'installazione, distingui:

**Installata:** il kit è materialmente nella destinazione prevista.
**Raggiungibile:** il ricevente può leggere i file necessari.
**Scopribile:** l'ingresso della competenza appare nel meccanismo previsto dall'ambiente.
**Esercitata:** un incarico reale mostra che la competenza ha cambiato comprensione o azione.
**Assimilata nel lavoro:** in una situazione successiva e diversa la correzione è usata senza doverla ricostruire da capo.

Per una prima osservazione, affida un incarico concreto. Chiedi all'AI di indicare quale fonte e quale relazione hanno cambiato la sua scelta, senza considerare questa dichiarazione una prova sufficiente da sola. Conserva il lavoro e la sua conseguenza nella guida del progetto. Quando un errore, una comprensione migliore o una possibilità nuova producono sapere riutilizzabile, falla tornare alla competenza che dovrà operare diversamente; non accumulare soltanto riassunti del passato.

Se non hai ancora un ambiente con file persistenti, usa una chat e conserva esplicitamente la guida di continuazione. Il metodo resta utilizzabile, ma la persistenza e le azioni dipendono dagli strumenti reali che hai a disposizione.

## Che cosa hai adottato

Hai reso disponibile al tuo progetto una o più **competenze pubbliche MAIOS**. Puoi comporle attraverso KA, FDLA, Meta_Skill e metodi di continuità nella misura in cui il tuo lavoro e il tuo ricevente le rendono pertinenti. Questo non trasferisce la configurazione privata degli sviluppatori, le credenziali, i loro compiti pendenti o un'autorità di azione sui tuoi sistemi. Il valore diventa osservabile nell'uso e nei modi in cui il lavoro continua a cambiare il saper fare.

**Raccolta completa:** [maios-meta-skill](https://github.com/GrazianoGuiducci/maios-meta-skill) · **Uso generale:** [guida pubblica](https://github.com/GrazianoGuiducci/maios-meta-skill/blob/main/docs/USO.md).

## Con MAIOS Project Kernel 5.1.0, facoltativamente

[MPK](https://github.com/GrazianoGuiducci/maios-project-kernel) è un prodotto distinto: porta già sistema semantico, formazione delle competenze, adattamento host e continuità. Il suo package usa il proprio installer, con Python >=3.11 e comandi preview/apply; segui [INSTALL](https://github.com/GrazianoGuiducci/maios-project-kernel/blob/main/package/INSTALL.md). L’installer di questa raccolta copia kit; non esegue l’installazione o le migrazioni MPK.

Prima di integrare, confronta funzione, responsabile, metodo e sapere già acquisito, oltre al nome. Per esempio, il progetto MPK possiede già la formazione delle competenze: conserva quella sede e collega Onto-Skill per la distinzione pratica principio→abilità quando utile. Usa la cooperazione se partecipano persone o sistemi indipendenti; la copia di cartelle da sola non è cooperazione.

| Funzione nella raccolta | Funzione già presente in MPK | Raccordo utile |
| --- | --- | --- |
| Meta_Skill, KA/FDLA e continuità | Sistema e formazione con conoscenza e rientro locali | Confrontare i metodi, preservare l’owner locale e collegare il solo delta utile |
| Onto-Skill | Formazione di capacità pertinenti al progetto | Portare condizioni e scelta che il principio cambia nella guida responsabile |
| Cooperazione | Partecipazione di competenze nel lavoro | Aggiungere sapere su contributori indipendenti solo quando quella relazione esiste |
| MPC | Conoscenza del progetto e sue sorgenti | Presentare l’oggetto effettivo, senza attribuirgli tutte le proprietà MAIOS |

Mantieni il contributo nella sede del progetto e rendilo raggiungibile dall’ingresso nativo dell’host. Un nuovo kit non sovrascrive l’apprendimento della copia installata. Compatibilità dichiarata, installazione, discovery, esercizio e uso successivo mantengono le proprie osservazioni; questa guida non attesta l’integrazione in ogni host.
