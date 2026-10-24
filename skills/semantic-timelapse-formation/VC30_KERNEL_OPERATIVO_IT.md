# VC-30s — mini-kernel operativo per video brevi in codice

**Stato:** candidata 0.4.0, sapere metodologico disponibile, non runtime autonomo né generatore installato. È un **mini-kernel di composizione competente** dentro Semantic Timelapse Formation, non un nuovo kernel assiomatico, una sequenza obbligatoria di fasi o un controllore di pubblicazione. Il film breve (circa 30 secondi quando selezionato) è l'oggetto che mantiene connessi progettazione visiva, codice, sonoro e apprendimento.

## Formare il filmato dall'oggetto reale

Soggetto, fonti, distinzione fra osservato e illustrato, destinatario e trasformazione significativa determinano quali capacità partecipano. Il mini-kernel può comporre comprensione della fonte, generatore d'immagini, storyboard/design, scena 2D/2.5D/3D, temporalità, narrazione/suono facoltativi, esportazione/osservazione e ritorno del sapere. Non tutti i film richiedono personaggi, Three.js, voce o sequenze multiple di immagini.

**Immagine A:** output reale di un generatore di immagini, formato da istruzioni source-bound e **osservato prima di scrivere in codice il primo frame visivo**. Serve a non ricostruire la scena solo «a memoria». **Immagine B:** primo frame di una scena codificata e modificabile, distinto da A. La bitmap A non possiede automaticamente profondità nascosta, rigging o eventi reali; la scena deve acquisirli quando il soggetto lo richiede.

Un attore/oggetto conserva identità riconoscibile nel tempo: referente, ruolo, segni visivi, stato osservabile, azione, rapporti con altri, eventuale posa/contatto con props e visibilità alla camera. SVG/CSS isometrico o 2.5D a livelli possono esprimere profondità; il vero 3D richiede geometria, luci e camera autentiche quando cambiano davvero la comprensione.

## Strumenti che possono partecipare, senza stack fisso

**HTML/video:** [HyperFrames](https://github.com/heygen-com/hyperframes) usa clip temporizzate e timeline con seek, con GSAP e `hf-seek` per Canvas/Three.js. Licenza del framework Apache-2.0.

**React/video:** [Remotion](https://github.com/remotion-dev/remotion) usa `useCurrentFrame()`, composizioni e sequenze. La Remotion License **non** è un permesso universale MIT/Apache: verificare condizioni gratuite/aziendali per il contesto attuale.

**2D/gioco:** [PixiJS con GSAP](https://github.com/AhmadDinkaa/pixijs-tic-tac-toe) separa oggetti di scena, stato, feedback e audio. La produzione video deve trasformare callback realtime in stati raggiungibili per frame.

**Web/3D:** [GSAP e Three.js](https://github.com/TheWebxite/phans-custom-tailor) mostrano shader per stoffa/immagini e fallback; il ciclo WebGL real-time non garantisce da sé seek. Chiarire licenze per codice e asset prima del riuso.

**Audio e voce:** [Motion Video](https://github.com/bestagentkits/motion-video-skill) mostra allineamento voce, caption e beat musicali con misure di export; credenziali dei provider e soglie specifiche restano condizioni di quell'implementazione.

**Saper fare del movimento:** [iart motion-skills](https://github.com/iart-ai/motion-skills) permette di raggiungere competenze più precise per personaggi, isometria, infografiche, WebGL, audio, storyboard e ispezione dei fotogrammi; non installare l'intera raccolta per ogni lavoro.

**Composizione web:** [modern-portfolio](https://github.com/sanidhyy/modern-portfolio) usa Framer Motion per varianti, entrate scaglionate e transizioni; apprendere la grammatica, senza assumere che il sito sia già un video esportabile.

Questi sono **metodi e sorgenti di sapere**, non dipendenze installate. Nessun asset, logo, foto, shader o codice di terzi è copiato in questa risorsa. Il ricevente reale sceglie i mezzi e risolve i relativi permessi/licenze.

## Apprendere dai metodi altrui, senza trasferire le implementazioni

Due giri sulle sorgenti esterne affinano **che cosa sa fare la competenza**, non quali repository deve installare.

**Dalle etichette a una materia visiva percepibile.** «Cinematografico» o «moderno» non specificano una scena. Lasciare che il soggetto determini materia, forma, inquadratura, luce e comportamento dell'immagine A. Osservare A come **ipotesi visiva**, senza importare nella scena B una composizione arbitraria o una causalità inventata. Le liste di stili vietati, i numeri di timing e i preset dei progetti sorgente non diventano invarianti MAIOS.

**Dal personaggio illustrato al gesto coerente.** Se un attore o oggetto è pertinente, riconoscere segni visivi, posa, sguardo, contatti e relazioni che devono continuare. Mano con attrezzo, sguardo verso l'oggetto e props che attraversano un cambio camera descrivono un rapporto persistente, non soltanto pixel animati. Un'immagine A appiattita non rivela retro, rig o volumi nascosti: cambiare prospettiva o acquisire gli asset reali necessari invece di inventarli.

**Dal movimento al primo incontro.** Una scena è comprensibile attraverso azione, conseguenza, pausa, cambio d'inquadratura, parole e silenzio. Il tempo può rappresentare sequenza, confronto, incertezza o causa: il montaggio non deve obbligare ogni inquadratura successiva a essere effetto della precedente. Voce e musica, se pertinenti, condividono gli eventi significativi, non timestamps arbitrari; il video muto resta possibile.

**Dall'osservazione al sapere.** Un fotogramma rende visibile la geometria, la visione in movimento il ritmo, un frame codificato un problema di export. Queste osservazioni possono correggere il metodo che le produce, senza tribunali di approvazione. La nostra valutazione «come primo spettatore» non è prova che un pubblico reale abbia compreso.

La capacità acquisita è la **trasduzione percettiva situata**: comprendere la fonte, formare un riferimento visivo osservabile e derivarne una rappresentazione temporale riproducibile conservando il significato del soggetto. Codice e runtime restano all'owner tecnico; qui non si importano codice, asset o stili di terzi.

## Rientro sulle fonti non ancora lette: l'immagine generata non è un rig

L'audit dei sette repository originali, dei **18 README di ingresso iart** e delle **sette skill principali HyperFrames** ha recuperato una distinzione mancante. **Non** significa che siano state lette tutte le 55 skill iart, tutti i blocchi HyperFrames o l'intera documentazione Remotion.

La prima **immagine A realmente generata e osservata** rimane il riferimento. Può definire direzione visiva, composizione e rapporti fra personaggi e oggetti. Ma una figura appiattita non permette automaticamente di animare braccio, oggetto impugnato, sfondo o retro. Quando il movimento realmente lo richiede, far formare **ulteriori elementi source-bound, pose, maschere, livelli o geometrie**; quando basta muovere l'immagine intera, non forzare la scomposizione. Gli asset successivi devono restare coerenti col soggetto e A, conservando ruolo, provenienza e identità: non sono retroattivamente «la prima immagine A».

La [competenza Generative Illustration](https://github.com/iart-ai/generative-illustration-skills) insegna a separare elementi animabili. Una sua guida riporta anche un falso positivo in un ritaglio SVG che ha cancellato una parte della figura. Il metodo acquisito è **separare senza perdere il referente**, non trasferire quel codice o una sua particolare euristica.

La competenza [HyperFrames media-use](https://github.com/heygen-com/hyperframes) mostra come non riusare asset di un altro progetto per semplice somiglianza di prompt: identità, fonte e condizioni di riuso partecipano alla formazione della scena. Non serve copiare il manifest della sua cache.

**Gradi diversi di modificabilità:** componenti nativi, codice che disegna un frame al tempo T e clip già renderizzata non conservano le stesse possibilità di intervento. Un MP4 terminato non contiene più un personaggio con arti modificabili. [Remotion ThreeCanvas](https://github.com/remotion-dev/remotion) è una possibilità di 3D controllato dal frame quando il ricevente reale la possiede.

**Destinazione e testo:** un 16:9 spesso richiede *ri-composizione* per un 9:16, non ritaglio; persone, elementi, testi e aree coperte dall'interfaccia partecipano già alla richiesta per A. Parole e caption che devono essere esatte restano modificabili e, dove pertinente, accessibili; non sono lettere immaginate dall'immagine generata. Le specifiche di una piattaforma vanno confermate nel caso effettivo.

Nessun codice/asset di terzi importato e nessun nuovo video dichiarato realizzato.

## Prima e oltre il video: concetto, relazione non lineare e trasferimento reale di A

Un altro rientro sulle sorgenti mette in luce capacità che **non richiedono un nuovo renderer**.

**Un concetto può precedere il filmato.** Quando esiste già un nucleo editoriale o di prodotto ancorato alle fonti, il video breve è una possibile espressione accanto a immagine, infografica, presentazione e guida interattiva. Recuperare oggetto, relazione, conseguenza e destinatario prima di formare il prompt di A; non ricavare la tesi soltanto dallo stile della clip precedente. I derivati conservano il significato, non lo stesso ritaglio. Nel percorso image-first selezionato la prima A rimane realmente generata e osservata.

**Un film lineare non rende lineare il soggetto.** La sequenza può mostrare co-presenza, confronto, alternative, ritorno ricorsivo che modifica ciò che segue, oppure capacità presente e orizzonte futuro in uno stesso campo. La vicinanza dei fotogrammi non autorizza un nesso causale, né un loop significa automaticamente tornare identici al punto iniziale. La grammatica temporale deriva dal **tipo di relazione** che si vuole mostrare.

**Presentazione e guida navigabile sono capacità distinte.** Una clip può introdurre un sistema attraverso spazi, azioni e conseguenze e condividere la rappresentazione con una guida interattiva. L'MP4 non riceve input, non conserva stato operativo e non esegue funzioni. La parentela visuale non prova identità funzionale.

**La descrizione di A non consegna la sua immagine.** Se un host genera A e un altro costruisce B, chi codifica deve poter **leggere davvero il file visivo o un asset effettivamente accessibile**, insieme a ciò che vi è stato osservato. Prompt, immagine vista soltanto in un'altra chat o link a una skill non completano il passaggio. Usare i mezzi già disponibili per il trasferimento reale quando serve; non presumere un servizio permanente o uno schema di metadati universale.

**Dimostrazione da screenshot ≠ esecuzione del prodotto.** Un cursore animato può illustrare un workflow, ma non attesta che il click o la risposta siano realmente avvenuti nel runtime. Distinguere schermata osservata, ricostruzione esplicativa ed esecuzione osservata quando il claim lo richiede.

Il trasferimento è di **conoscenze e metodi**, non di codice altrui o nuove tappe imposte.

## Immagine A prima del codice, non necessariamente al secondo zero

La prima immagine A è generata e osservata **prima di programmare l'animazione**, ma non deve necessariamente rappresentare il tempo `t=0` del film. Può essere un'immagine guida, l'identità di un personaggio, il gesto più significativo, una relazione spaziale o un momento rappresentativo. La scena codificata B possiede il **proprio** stato iniziale; la relazione utile con A può apparire anche più avanti. Non imporre una copia pixel per pixel come primo frame solo perché A è stata prodotta per prima nel lavoro.

**Una situazione rappresentata, più espressioni visibili.** Quando il soggetto contiene gesti o cambiamenti di stato, attori, oggetti tenuti in mano, camere, parole e suoni devono rendere aspetti coerenti **della stessa situazione ancorata alla fonte**. Un click, gesto o cambio di punto di vista non dimostra automaticamente che un evento sia accaduto. Alcuni video richiedono solo una relazione condivisa, altri un modello di stati/eventi più ricco: nessuna macchina a stati è universalmente obbligatoria.

**Una variante dei dati non è sempre un nuovo soggetto.** Una scena può produrre nuove varianti quando il tipo di relazione rimane pertinente. Un caso realmente diverso può richiedere un'altra prospettiva, grammatica percettiva, comprensione della fonte o prompt per A, non soltanto sostituire nomi e colori del vecchio template. La capacità riusabile riguarda *come formare* scene, non imporre la loro geometria ai casi futuri.

## Studio-Lab: il sapere partecipa nella postazione competente

L'ampliamento VC-30s selezionato dall'operatore ha formato [Studio-Lab](VC30_STUDIO_LAB_IT.md) con undici **postazioni specialistiche** anziché una filiera obbligatoria. Permettono a conoscenza di fonte, direzione visiva, immagine A e asset, storyboard, codice, voce/sonoro, rendering, consegna e apprendimento ricorsivo di partecipare quando cambiano il film effettivo. Entrare nella [guida portabile](VC30_STUDIO_LAB_IT.md) quando un progetto attraversa più discipline. Il metodo scritto non installa generatori, renderer o istanze autonome.

## Il film deve essere ricostruibile a qualsiasi tempo

Il renderer destinato all'export rende `frame(t, scena, asset)` o equivalente da un tempo/frame assoluto, **anche fuori ordine**. Ticker GSAP e `update(dt)` Three.js descrivono animazione realtime, non garantiscono filmati deterministici. Servono random ripetibile, disponibilità di font/asset/GPU e identità persistenti fra scene. 30 s × 24 fps = 720 frame, ma formato e fps non diventano regole generali.

Distinguere **tempo della fonte** (eventi realmente registrati) da **tempo del film** (narrazione animata). Senza misure temporali della fonte il risultato è una clip esplicativa, non un timelapse documentario.

Se audio e didascalie sono utili, cue e parole derivano dalla stessa timeline. Anche il silenzio può essere appropriato. Verificare durata, risoluzione, tracce e fotogrammi realmente codificati quando il claim li richiede; una clip leggibile non certifica comprensione del destinatario.

## Autoevoluzione della competenza

Un'immagine può introdurre una gerarchia inesistente; un personaggio può perdere identità cambiando orientamento; un'animazione HTML può non supportare seek; un suono può suggerire causalità non presente. La differenza torna alla competenza che dovrà comportarsi diversamente: comprensione della fonte, prompt, Design, codice, sonoro o ricevente. Sapere esistente non richiamato richiede migliore discovery, non un doppione. Un filmato esportato non cambia i pesi del modello né installa strumenti.

**Ancora non esercitato nel candidato pubblico:** percorso completo A generata→osservata→B con personaggi/oggetti→video, nuovo render 3D, provider audio, pubblicazione. Il mini-kernel rende queste capacità **raggiungibili**, non automaticamente attive.

**Provenienza:** conoscenza tratta dai repository linkati, letti il 24 ottobre 2026. Alla scelta concreta di un framework o asset recuperare licenze e versione correnti della fonte, perché possono cambiare.
