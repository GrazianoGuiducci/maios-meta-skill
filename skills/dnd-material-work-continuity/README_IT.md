# Ricostruire il lavoro e le decisioni di un progetto AI

Conserva richieste originali, azioni, correzioni e punto attuale senza riscrivere ciò che è avvenuto.

Versione **0.3.1** · Istruzioni e guida in italiano · Presentazione IT/EN.

Una decisione può cambiare senza cancellare ciò che è avvenuto prima. Questa competenza conserva il collegamento fra richiesta originale, interpretazione dell'AI, lavoro svolto e correzione successiva.

Il risultato è una ricostruzione utilizzabile da chi riprende il progetto. La storia dettagliata resta raggiungibile; il punto corrente contiene quanto serve per continuare.

## Cosa puoi affidarle

Mantiene una traccia degli eventi materiali e distingue la fonte dell’operatore dalle interpretazioni dell’assistente e dagli effetti osservati.

Quando cambiano requisiti e direzione o serve ricostruire perché un progetto si trova nello stato attuale.

- Ricostruisce una scelta poi modificata dal cliente.
- Conserva un’azione eseguita anche dopo una correzione di direzione.
- Passa un progetto a una nuova istanza con fonti, effetti e incognite riconoscibili.

## Primo uso

Apri [l'avvio completo](AVVIO_CHAT_IT.txt), incollalo o allegalo alla tua AI e compila il contesto finale. Contiene l'intero metodo, senza richiedere accesso a sorgenti private. Se il tuo ambiente legge file, può partire da [SKILL.md](SKILL_IT.md).

### In chat

Allega o incolla AVVIO_CHAT_IT.txt, che contiene l'intero metodo, e aggiungi il tuo contesto. L'AI può lavorare nella lingua della conversazione. Conserva il risultato e la guida utile se vuoi riprenderli in una nuova chat.

### In un ambiente agentico

Rendi leggibile la cartella della competenza e fai leggere SKILL.md prima del lavoro pertinente. Collega fonti e strumenti reali secondo le istruzioni dell'ambiente. Il kit non installa account, memoria o esecuzioni ricorrenti.

### Con o senza un kernel

Con un kernel esistente, collega il metodo alla competenza o guida che già possiede il lavoro. Senza kernel, applica direttamente le istruzioni e conserva la conoscenza utile nel progetto o in una nota riutilizzabile.

## Come proseguire

Un passaggio di consegne mostra quali collegamenti sono sufficienti e quali mancano. Conserva la correzione nel metodo di continuità, lasciando le scelte di progetto al loro responsabile.

La guida dell'attività o del progetto conserva il punto utile, le ragioni e le fonti. Riprendila quando cambi chat o ambiente. Se una correzione modifica il metodo di questa risorsa, mantieni riconoscibile la revisione usata e il caso che ha insegnato la differenza.

## Metodo e limiti della prima edizione

Questa competenza opera sulla continuità materiale: conserva che cosa è accaduto e da quali fonti deriva. Non decide da sola il significato di una scelta né lo stato complessivo del progetto.

La relazione diventa meta quando un errore di ricostruzione cambia il metodo con cui si conserva il lavoro. Per esempio, un riepilogo aveva mescolato proposta e approvazione: il seguito rende riconoscibili entrambe. Non è autonomia esecutiva, e un registro ben formato non dimostra memoria infallibile.

Questa edizione contiene sapere operativo ed esempi illustrativi. Formato, disponibilità e lettura dei file non certificano l'esercizio in un altro assistente. Usa i mezzi effettivi del tuo ambiente e l'autorizzazione pertinente alle azioni che vuoi affidargli.

[Leggi i tre esempi](ESEMPI_IT.md) · [Pagina della risorsa](https://maios.it/risorse/ricostruire-lavoro-decisioni/) · [Raccolta MAIOS Meta-Skill](https://github.com/GrazianoGuiducci/maios-meta-skill)


[English](README.md). Questa edizione offre il metodo completo in inglese come lingua principale; i file italiani ne conservano la traduzione.


## Sapere operativo pratico

[GUIDA_OPERATIVA_IT.md](GUIDA_OPERATIVA_IT.md) spiega decisioni, condizioni e mezzi che rendono utilizzabile il metodo. L'avvio include questo sapere; la cartella conserva anche le sorgenti leggibili direttamente.

## Licenza

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). Il kit scaricabile include LICENSE e NOTICE. Copyright 2026 Graziano Guiducci. Le guide comuni della repository sono riferimenti online facoltativi; metodo e sapere operativo pratico sono inclusi nel kit.


## Installare in Codex

Leggi [INSTALL_IT.md](INSTALL_IT.md). Copia l'intera cartella `dnd-material-work-continuity` nella directory `.agents/skills/` del progetto, poi richiama `$dnd-material-work-continuity` con fonti e lavoro da svolgere. Conserva un'eventuale copia esistente per confrontarla, senza sovrascriverla.
