# Estrarre le idee dell’autore dalle conversazioni con l’AI

Ritrova concetti, correzioni e intuizioni in un corpus scelto, conservando la loro origine.

**Versione 0.3.1 · istruzioni in italiano · presentazione italiana e inglese.**

## Cosa affidarle

Distingue le parole dell’autore dalle risposte dell’assistente, elimina duplicazioni e rumore e organizza i concetti utili con il loro riferimento sorgente.

Quando il sapere è disperso in chat, appunti o trascrizioni e vuoi ricavarne idee o metodi utilizzabili.

## Iniziare in chat

Copia o allega [AVVIO_CHAT_IT.txt](AVVIO_CHAT_IT.txt), che include l’intero metodo, e completa il contesto finale con i tuoi materiali. Puoi conversare nella lingua che preferisci. Inizia da un caso reale: «In questi file cerca le idee che ho espresso su questo tema. Mantieni fonti e differenza tra mie parole, tue parafrasi e sviluppi possibili.»

Quando la chat non può salvare documenti, chiedi una restituzione completa da conservare e portare alla sessione successiva. La sola presenza del testo nella conversazione non garantisce memoria futura.

## Usarla in un ambiente agentico

Metti la cartella in una posizione che l’assistente può leggere e indicagli [SKILL.md](SKILL_IT.md). Collega i file del progetto e specifica dove conservare il sapere. Se l’ambiente ha un proprio meccanismo per le skill, usa il formato e l’ingresso che supporta; la semplice copia non dimostra scoperta o attivazione. Questo kit non installa integrazioni, account o scheduler.

## Con un kernel esistente o da sola

Con un kernel, fai partecipare il metodo attraverso le guide e le competenze già pertinenti; conserva conoscenza e autorità del progetto ricevente. Senza kernel, il corpo completo è utilizzabile direttamente. Quando serve sapere specialistico, raggiungi le fonti e le capacità effettive del tuo ambiente.

## Metodo, esempi e apprendimento

Il lavoro diretto è l’estrazione attribuita. La relazione meta appare quando una correzione ricavata dal corpus modifica il modo di scrivere, ricercare o formare altre competenze.

La relazione è autologica quando l’estrazione riconosce che il proprio metodo stava sostituendo la voce dell’autore: per esempio attribuendogli una generalizzazione prodotta dal modello. Corregge allora sia l’estratto sia il criterio di attribuzione. La ricostruzione rimane limitata alle fonti realmente disponibili.

Gli [esempi](ESEMPI_IT.md) sono illustrativi. Il metodo può essere adattato agli esiti e alle correzioni del tuo lavoro; conserva il motivo della modifica e ciò che rimane da osservare. L’apprendimento qui riguarda guide, istruzioni e conoscenza accessibile, non un aggiornamento dei pesi del modello. Gli effetti esterni dipendono dal mandato e dagli strumenti effettivi.

Origine della raccolta: Graziano Guiducci · MAIOS.


[English](README.md). Questa edizione offre il metodo completo in inglese come lingua principale; i file italiani ne conservano la traduzione.


## Sapere operativo pratico

[GUIDA_OPERATIVA_IT.md](GUIDA_OPERATIVA_IT.md) spiega decisioni, condizioni e mezzi che rendono utilizzabile il metodo. L'avvio include questo sapere; la cartella conserva anche le sorgenti leggibili direttamente.

## Licenza

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). Il kit scaricabile include LICENSE e NOTICE. Copyright 2026 Graziano Guiducci. Le guide comuni della repository sono riferimenti online facoltativi; metodo e sapere operativo pratico sono inclusi nel kit.


## Installare in Codex

Leggi [INSTALL_IT.md](INSTALL_IT.md). Copia l'intera cartella `operator-concept-preserver` nella directory `.agents/skills/` del progetto, poi richiama `$operator-concept-preserver` con fonti e lavoro da svolgere. Conserva un'eventuale copia esistente per confrontarla, senza sovrascriverla.
