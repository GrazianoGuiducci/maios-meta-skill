# Installare una skill MAIOS in Codex

[English](INSTALL.md) · [Scegliere una risorsa](../README_IT.md) · [Uso in chat](USO.md)

Ogni risorsa è una cartella Agent Skills completa. Scegli la capacità utile:
la cartella con il nome tecnico contiene `SKILL.md` e il sapere di supporto.
Puoi installare una skill, più kit selezionati o l’intera raccolta. Le altre risorse non sono prerequisiti.

## Dal kit scaricato

1. Scarica lo ZIP dalla pagina MAIOS della risorsa ed estrailo. Per FDLA,
   la cartella risultante si chiama `operate-fdla`.
2. Copia l'intera cartella nella directory `.agents/skills/` del tuo progetto.
   L'ingresso deve essere `.agents/skills/operate-fdla/SKILL.md`, con guide,
   esempi e altri file accanto. Conserva un'eventuale copia esistente per
   confrontarla, senza sovrascriverla.
3. Apri Codex nel progetto. Richiama `$operate-fdla` e affida un lavoro concreto,
   fornendo le fonti pertinenti. Codex rileva le nuove skill; riavvia la sessione
   se l'ingresso non compare.

Per esempio: «Usa $operate-fdla per confrontare questo riassunto con la fonte
dell'autore qui sotto. Correggi eventuali cambiamenti di significato e spiega
la correzione». Aggiungi entrambi i testi dopo la richiesta.

L'ingresso installato rimane inglese. Per lavorare in italiano chiedi un
risultato italiano; `SKILL_IT.md`, `README_IT.md` e gli esempi italiani
restano disponibili.

## Dalla repository

Con Python 3.10 o successivo, apri un terminale nella copia della repository
e consulta i nomi realmente installabili:

```text
python tools/install_skills.py --list
```

Verifica la selezione senza scrivere, poi installala nel progetto scelto:

```text
python tools/install_skills.py --skill operate-fdla --dest "C:/Work/my-project/.agents/skills" --dry-run
python tools/install_skills.py --skill operate-fdla --dest "C:/Work/my-project/.agents/skills"
```

Usa il percorso reale del tuo progetto; sono supportati anche percorsi POSIX.
Ripeti `--skill` per più risorse. Gli ID stabili come `fdla-correzione-ai`
raggiungono la stessa skill tecnica, `operate-fdla`. Usa `--all` soltanto per
installare l'intera raccolta.

L'installer legge gli archivi di release e controlla manifest e impronte dei
file prima di scrivere. Richiede una destinazione esplicita e si ferma se una
cartella selezionata esiste già. Non cambia configurazioni Codex, installa
dipendenze o esegue gli script delle skill. Ogni cartella installata conserva
versione e impronta del pacchetto in `MAIOS_INSTALLATION.json`. Una copia
interrotta può lasciare una nuova cartella parziale; `SKILL.md` diventa visibile
solo dopo la scrittura dei file di supporto.

## Discovery e primo uso

Controlla il selettore delle skill e il percorso dello `SKILL.md` installato.
Se lo stesso nome è già disponibile altrove, confronta gli ingressi e scegli
quello pertinente al progetto: Codex non unisce skill omonime.

Nel primo lavoro osserva se Codex raggiunge metodo e guida operativa installati,
usa le fonti fornite e produce un risultato utile. La presenza nel selettore
mostra discovery; il lavoro mostra il comportamento effettivamente esercitato.
Conserva il sapere utile nel progetto, raggiungibile dalla sessione successiva.

Un aggiornamento è un nuovo pacchetto. Confrontalo con la competenza esistente
e con l'apprendimento locale prima di integrarlo. L'installer non sovrascrive
né aggiorna automaticamente una cartella installata.

Altri host hanno meccanismi propri. Conserva la cartella intera e segui le
loro istruzioni. Lo ZIP è un kit di skill: non configura un plugin o un
servizio autenticato.

Riferimento: [documentazione OpenAI sulle skill](https://learn.chatgpt.com/docs/build-skills).


[Comporre il sistema del progetto e integrare MPK facoltativamente](USO.md): ingresso, fonti, guide, confronto funzionale e conservazione del sapere locale.
