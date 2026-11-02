# Formare e distribuire una risorsa da una metacompetenza

[English](DISTRIBUTION.md). L’inglese è la lingua principale della raccolta; questa guida è la versione italiana.

La raccolta nasce dal lavoro MAIOS. Una competenza privata diventa una risorsa pubblica quando un destinatario esterno può comprenderne l'utilità, riceverne il sapere e usarlo nel proprio contesto.

## La capacità da rendere utilizzabile

Raggiungi la competenza sorgente e le ragioni per cui il suo metodo è cambiato. Distingui la capacità generale dall'applicazione che l'ha fatta emergere. Un servizio concreto può essere una risorsa altrettanto utile: il livello meta non determina una gerarchia di valore.

Forma l'incarnazione pubblica attraverso la capacità che deve continuare nel ricevente. Sostituisci riferimenti, percorsi e infrastrutture private con ingressi effettivamente utilizzabili; porta dentro il sapere necessario, comprese le relazioni che permettono di adattarlo o farlo crescere.

## Descrizione e primo uso

Il titolo identifica la risorsa. Il sottotitolo spiega quale lavoro permette di svolgere e in quale contesto. Il corpo rende comprensibili capacità, esempi, prerequisiti e modalità d'uso per una persona che incontra il progetto per la prima volta.

La scheda della raccolta rende subito visibili cosa fa e quando usarla, seguiti da esempi di lavoro riconoscibili. Nome, tipo e descrizioni del metodo accompagnano queste informazioni. Gli esempi esprimono le capacità della risorsa; la guida spiega quali strumenti e istruzioni occorrono per realizzarle nel proprio ambiente.

Corpo operativo, guida e avvio si sostengono. Un avvio autonomo include il metodo necessario a un primo uso; un semplice rinvio a file che il destinatario non può leggere non basta. Le indicazioni per chat, harness e kernel seguono ciò che serve alla risorsa effettiva.

## Un'identità e una versione

Il catalogo conserva nome, versione, stato, percorsi e descrizioni. La cartella della competenza resta la sorgente del metodo; i file di presentazione ne sono una proiezione. Il pacchetto scaricabile deve contenere gli stessi file della versione dichiarata.

La verifica dei file distribuiti raggiunge i byte della revisione Git, oltre al checkout locale: una conversione dei fine riga può rendere diversi i due ingressi. Questa raccolta conserva i testi in LF tramite .gitattributes; il pacchetto viene ricostruito dalla stessa forma.

Il sito MAIOS può generare schede e pagine da questi dati, registrando la revisione ricevuta. Substack e gli altri canali adattano la spiegazione per il proprio pubblico e collegano la risorsa completa. La preparazione dei testi e la loro pubblicazione conservano il proprio stato.

## Crescita attraverso l'uso

Quando una raccolta comprende più nature, la pubblicazione mantiene distinguibili competenze, composizioni, funzioni e fondamenti. La pagina spiega il lavoro sul suo oggetto, il livello meta che effettivamente trasferisce e l’eventuale relazione autologica con un esempio specifico. [La guida concettuale](CONCETTI.md) ne chiarisce il significato. La teoria descritta resta collegata al metodo consegnato.

Una serie editoriale può distribuire nel tempo risorse rese disponibili nello stesso rilascio. Il registro del canale conserva revisione, testo, destinazione, finestra e stato reale di ogni effetto; la disponibilità della risorsa non viene scambiata per un articolo già pubblicato.

Un riscontro può riguardare comprensione, metodo, strumenti disponibili o aspettative. Conserva la situazione e il nesso che spiega il cambiamento. Aggiorna la parte che deve operare diversamente e le proiezioni realmente dipendenti.

Meta-Activity è il primo caso. I file e le sezioni utili qui non costituiscono un template obbligatorio per tutte le prossime competenze. Il metodo si affina attraverso la loro formazione e l'uso.

Una traduzione conserva anche le relazioni operative: cosa osservare, quale differenza cambia la scelta, come agire e che cosa portare nel seguito. Titoli, conteggio delle sezioni e promessa di valore non sostituiscono questa corrispondenza.
# Attività da adattare

La sezione `activities` del catalogo identifica incarichi completi che
compongono competenze esistenti. È distinta dagli ingressi operativi in
`resources` e dall’installer delle skill. Ogni attività ha una propria edizione,
metodo localizzato, guida, esempi, modello di contesto e avvio autonomo.

`python tools/build_activities.py` genera i documenti dalle sorgenti autoriali
`activity.json`. Dopo il commit delle sorgenti,
`python tools/build_activities.py --source-ref COMMIT` produce il kit da quella
revisione esatta. `dist/activities-manifest.json` conserva archivio, revisione,
edizioni delle competenze di supporto e impronte dei file. Pacchetti e manifest
delle competenze già distribuite restano preservati.

Il generatore risolve ramo o tag in un commit completo prima di leggere le
sorgenti. Respinge un pacchetto esistente con byte diversi: occorrono una
nuova edizione e un nuovo nome, senza sostituire l’archivio distribuito.

Il primo kit `public-representation` 0.1.0 incorporava il riferimento letterale
`HEAD`. Il manifest esterno qualifica ora l’archivio invariato con il commit
`46002f7c2ef809ec7f167036854d3037494c3d01` e
`embedded_source_reference: HEAD`. Tutti i 64 membri sorgente sono stati
confrontati con quel commit; il 65° è il record di dipendenze generato.
La correzione riguarda la provenienza esterna: non attribuisce al vecchio
archivio un commit completo incorporato e non ne cambia l’impronta.

Il kit include le competenze pubbliche complete sotto `skills/`. La guida
spiega l’adozione attraverso il proprio ambiente: copiare l’incarico non crea
un job ricorrente e non attribuisce autorità di pubblicazione.

