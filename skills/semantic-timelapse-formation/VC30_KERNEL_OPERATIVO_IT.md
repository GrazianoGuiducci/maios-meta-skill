# VC-30s — mini-kernel operativo per video brevi in codice

**Stato:** candidata 0.3.0, sapere metodologico disponibile, non runtime autonomo né generatore installato. È un **mini-kernel di composizione competente** dentro Semantic Timelapse Formation, non un nuovo kernel assiomatico, una sequenza obbligatoria di fasi o un controllore di pubblicazione. Il film breve (circa 30 secondi quando selezionato) è l'oggetto che mantiene connessi progettazione visiva, codice, sonoro e apprendimento.

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

## Il film deve essere ricostruibile a qualsiasi tempo

Il renderer destinato all'export rende `frame(t, scena, asset)` o equivalente da un tempo/frame assoluto, **anche fuori ordine**. Ticker GSAP e `update(dt)` Three.js descrivono animazione realtime, non garantiscono filmati deterministici. Servono random ripetibile, disponibilità di font/asset/GPU e identità persistenti fra scene. 30 s × 24 fps = 720 frame, ma formato e fps non diventano regole generali.

Distinguere **tempo della fonte** (eventi realmente registrati) da **tempo del film** (narrazione animata). Senza misure temporali della fonte il risultato è una clip esplicativa, non un timelapse documentario.

Se audio e didascalie sono utili, cue e parole derivano dalla stessa timeline. Anche il silenzio può essere appropriato. Verificare durata, risoluzione, tracce e fotogrammi realmente codificati quando il claim li richiede; una clip leggibile non certifica comprensione del destinatario.

## Autoevoluzione della competenza

Un'immagine può introdurre una gerarchia inesistente; un personaggio può perdere identità cambiando orientamento; un'animazione HTML può non supportare seek; un suono può suggerire causalità non presente. La differenza torna alla competenza che dovrà comportarsi diversamente: comprensione della fonte, prompt, Design, codice, sonoro o ricevente. Sapere esistente non richiamato richiede migliore discovery, non un doppione. Un filmato esportato non cambia i pesi del modello né installa strumenti.

**Ancora non esercitato nel candidato pubblico:** percorso completo A generata→osservata→B con personaggi/oggetti→video, nuovo render 3D, provider audio, pubblicazione. Il mini-kernel rende queste capacità **raggiungibili**, non automaticamente attive.

**Provenienza:** conoscenza tratta dai repository linkati, letti il 24 ottobre 2026. Alla scelta concreta di un framework o asset recuperare licenze e versione correnti della fonte, perché possono cambiare.
