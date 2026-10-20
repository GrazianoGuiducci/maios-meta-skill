# Rendere comprensibile il lavoro di un agente AI

Fa vedere alla persona il significato del movimento corrente e i punti in cui può intervenire.

Versione **0.3.1** · Istruzioni e guida in italiano · Presentazione IT/EN.

Un assistente può produrre un buon risultato lasciando la persona senza orientamento. Questa competenza rende comprensibili le relazioni che cambiano il lavoro nel momento in cui servono.

La spiegazione nasce dall'attività reale: ciò che cambia, perché conta, quali fonti lo sostengono e come la persona può correggere o continuare. La quantità di testo segue il bisogno.

## Cosa puoi affidarle

Adatta spiegazione, profondità e forma a ciò che la persona deve comprendere per orientare, correggere o continuare il lavoro.

Quando un sistema AI restituisce risultati ma chi lo usa non riesce a capire cosa cambia o come partecipare.

- Un assistente rende chiara una decisione che richiede l’intervento dell’utente.
- Un’interfaccia mostra da quali fonti dipende lo stato di un’attività.
- Il lavoro quotidiano insegna gradualmente come usare le capacità del sistema.

## Primo uso

Apri [l'avvio completo](AVVIO_CHAT_IT.txt), incollalo o allegalo alla tua AI e compila il contesto finale. Contiene l'intero metodo, senza richiedere accesso a sorgenti private. Se il tuo ambiente legge file, può partire da [SKILL.md](SKILL_IT.md).

### In chat

Allega o incolla AVVIO_CHAT_IT.txt, che contiene l'intero metodo, e aggiungi il tuo contesto. L'AI può lavorare nella lingua della conversazione. Conserva il risultato e la guida utile se vuoi riprenderli in una nuova chat.

### In un ambiente agentico

Rendi leggibile la cartella della competenza e fai leggere SKILL.md prima del lavoro pertinente. Collega fonti e strumenti reali secondo le istruzioni dell'ambiente. Il kit non installa account, memoria o esecuzioni ricorrenti.

### Con o senza un kernel

Con un kernel esistente, collega il metodo alla competenza o guida che già possiede il lavoro. Senza kernel, applica direttamente le istruzioni e conserva la conoscenza utile nel progetto o in una nota riutilizzabile.

## Come proseguire

Il lavoro quotidiano può insegnare gradualmente come partecipare al sistema. La prova utile è nel modo in cui una persona comprende e interviene in situazioni successive, non nella presenza di un pannello o di una descrizione.

La guida dell'attività o del progetto conserva il punto utile, le ragioni e le fonti. Riprendila quando cambi chat o ambiente. Se una correzione modifica il metodo di questa risorsa, mantieni riconoscibile la revisione usata e il caso che ha insegnato la differenza.

## Metodo e limiti della prima edizione

Il livello meta può diventare visibile quando il sistema spiega come una competenza si forma o cambia e la persona può orientare quella formazione. La spiegazione non diventa un secondo motore che decide la verità del dominio.

Questa competenza ha una relazione autologica quando applica il proprio metodo alla comprensibilità del proprio lavoro: una spiegazione che confonde diventa materiale per correggere il modo di spiegare. È distinto dall'autonomia dell'agente e dall'accesso al ragionamento interno.

Questa edizione contiene sapere operativo ed esempi illustrativi. Formato, disponibilità e lettura dei file non certificano l'esercizio in un altro assistente. Usa i mezzi effettivi del tuo ambiente e l'autorizzazione pertinente alle azioni che vuoi affidargli.

[Leggi i tre esempi](ESEMPI_IT.md) · [Pagina della risorsa](https://maios.it/risorse/comprendere-lavoro-agente/) · [Raccolta MAIOS Meta-Skill](https://github.com/GrazianoGuiducci/maios-meta-skill)


[English](README.md). Questa edizione offre il metodo completo in inglese come lingua principale; i file italiani ne conservano la traduzione.


## Sapere operativo pratico

[GUIDA_OPERATIVA_IT.md](GUIDA_OPERATIVA_IT.md) spiega decisioni, condizioni e mezzi che rendono utilizzabile il metodo. L'avvio include questo sapere; la cartella conserva anche le sorgenti leggibili direttamente.

## Licenza

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). Il kit scaricabile include LICENSE e NOTICE. Copyright 2026 Graziano Guiducci. Le guide comuni della repository sono riferimenti online facoltativi; metodo e sapere operativo pratico sono inclusi nel kit.


## Installare in Codex

Leggi [INSTALL_IT.md](INSTALL_IT.md). Copia l'intera cartella `ux-ai-kernel-design` nella directory `.agents/skills/` del progetto, poi richiama `$ux-ai-kernel-design` con fonti e lavoro da svolgere. Conserva un'eventuale copia esistente per confrontarla, senza sovrascriverla.
