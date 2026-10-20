# Usare una competenza MAIOS nella propria AI

[English](USE.md). L’inglese è la lingua principale della raccolta; questa guida è la versione italiana.

Una competenza contiene sapere operativo: aiuta l'AI a comprendere e svolgere un certo tipo di lavoro. Per usarla servono anche un intento reale, le fonti pertinenti e i mezzi che quell'ambiente può impiegare.

## In una chat

Per scegliere una risorsa, parti dal [catalogo del sito](https://maios.it/risorse/) o dalla tabella nel [README](../README.md). Ogni cartella contiene una guida e un file AVVIO_CHAT_IT.txt con il metodo da dare alla tua AI. Le modalità seguenti usano Meta-Activity come esempio e si adattano alla risorsa selezionata.

Per Meta-Activity, apri [AVVIO_CHAT_IT.txt](../skills/meta-activity/AVVIO_CHAT_IT.txt), copia tutto il testo oppure allega il file alla conversazione. Aggiungi il tuo contesto: cosa stai facendo, quali risultati servono, che cosa esiste già e quali strumenti l'AI può usare.

L'avvio include il metodo essenziale: funziona anche se la chat non può aprire il resto della repository. Per un lavoro più ampio, allega anche [SKILL_IT.md](../skills/meta-activity/SKILL_IT.md) e i riferimenti pertinenti. Se l'AI può leggere i file, puoi darle direttamente la cartella.

Una chat senza risvegli automatici può comunque formare e svolgere un'attività insieme a te. Per riprendere in una nuova sessione, salva la guida che contiene scopo, fonti, punto raggiunto, conoscenza utile e seguito, poi restituiscila all'AI.

## In un ambiente agentico

Un harness è l'applicazione che mette a disposizione dell'agente modello, strumenti, accessi e modalità di esecuzione. Rendi raggiungibile **l'intera cartella della competenza**, mantenendo i collegamenti relativi fra i file.

Per un'integrazione locale in Codex puoi copiare la cartella meta-activity nella directory delle skill del progetto:

    progetto/
      .agents/
        skills/
          meta-activity/
            SKILL.md
            README.md
            AVVIO_CHAT_IT.txt
            references/
            ...

Verifica nell'ambiente che la competenza sia disponibile e richiamala con un incarico reale. Se esiste già una competenza chiamata meta-activity, confrontala e scegli quale continuare: evitare due incarnazioni divergenti rende più chiaro il seguito.

La documentazione ufficiale descrive il [formato delle skill e la discovery in Codex](https://learn.chatgpt.com/docs/build-skills). Per altri ambienti usa i loro ingressi documentati oppure chiedi all'agente di leggere direttamente SKILL.md.

## Con un kernel

Per le altre risorse, il collegamento segue il loro contributo: una competenza applicativa svolge un lavoro, una metacompetenza può formare o trasformare metodi, KA e FDLA portano relazioni fondative e di correzione. Leggi la guida della risorsa prima di sovrapporla a istruzioni già presenti. La raccolta rende disponibili capacità; non richiede di caricarle tutte per ogni incarico.

Indica all'AI il kernel o la guida corrente del progetto. Meta-Activity usa intento, competenze, memoria e regole operative già presenti; la continuità resta nella sede che il progetto sa raggiungere. Una facoltà già disponibile può svolgere parte del lavoro: non occorre duplicarla.

Un kernel MAIOS può fornire una relazione più ampia fra contesto, competenze e apprendimento. La risorsa pubblica conserva comunque il sapere necessario al proprio uso e non richiede l'accesso ai repository privati del progetto MAIOS.

## Senza un kernel

Parti dal contesto che puoi fornire. Meta-Activity può organizzare un'attività, comporre il sapere disponibile e formare quello che manca attraverso fonti, strumenti ed esperienza.

Per continuare basta inizialmente una sede che il prossimo avvio possa leggere: un documento del progetto, un file o il prompt persistente dell'attività. Database, repository e altre applicazioni diventano utili quando servono al lavoro effettivo.

## Quando serve una ricorrenza

Chiedi di creare o aggiornare l'attività con il controller disponibile nell'ambiente. Il risultato deve identificare il job reale e la configurazione salvata: intento, istruzioni, cadenza o evento, fuso e destinazione.

La [documentazione delle attività programmate OpenAI](https://learn.chatgpt.com/docs/automations) distingue gli ambienti con file locali dalle attività web. Gli accessi dipendono dalla configurazione effettiva; il testo della competenza non li crea. Un'attività locale richiede che il computer e l'app restino disponibili.

Se manca il controller, l'AI può preparare l'incarico e svolgere il lavoro consentito nella sessione corrente. La ricorrenza sarà effettiva quando un mezzo reale la attiverà.

## Cosa osservare nel primo uso

Affida un'attività sufficientemente concreta da riconoscere un contributo utile. Controlla se l'AI ha usato le fonti pertinenti, ha svolto il lavoro affidato e ha conservato il sapere che permette di continuare. In un secondo avvio verifica che una correzione e la sua ragione cambino davvero il seguito.

Se condividi un riscontro nella repository, descrivi la situazione e il risultato rimuovendo dati riservati. Questa esperienza può migliorare sia il metodo della competenza sia la chiarezza della guida.

## Sapere operativo e strumenti

Ogni kit include GUIDA_OPERATIVA_IT.md e il corrispondente inglese. L'avvio porta metodo, sapere ed esempi articolati. Quando la funzione nativa fornisce un tool runtime, le sorgenti sono incluse nella cartella e nell'avvio. Una chat senza esecuzione può usare il metodo e preparare lavoro; l'esecuzione impiega Python, Git o altri mezzi reali dell'host. La guida selezionata spiega ingressi, comandi e test significativi. Non vengono fornite credenziali o stato privato dei nodi.

Le cartelle usano le entry native. Gli identificatori delle risorse continuano a individuare le rotte del sito; docs/IDENTITIES.json collega queste coordinate. Le precedenti cartelle rimandano ai kit correnti.


## Installare in Codex

Segui [INSTALL_IT.md](INSTALL_IT.md) per kit scaricato o installer della repository, discovery, primo uso e aggiornamenti. La [mappa dei percorsi precedenti](LEGACY_PATHS.md) raggiunge le cartelle operative.
