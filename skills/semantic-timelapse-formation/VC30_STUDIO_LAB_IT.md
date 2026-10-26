# VC-30s Studio-Lab — produrre video in codice con competenze specializzate

MKCV comprende più percorsi di produzione. Questo testo approfondisce il profilo riferimento→scena: nei lavori con immagini o clip già disponibili il mezzo parte da quei materiali, come descritto nella guida operativa.

MKCV è beta, in apprendimento. Il lavoro sul film e le osservazioni risultanti fanno evolvere il metodo.

**Stato:** metodo pubblico **edizione 0.1.3**. Si può usare come **guida di lavoro in una chat o in un harness** che possieda strumenti reali per immagini, file, codice e render. **Non** è uno studio software installato, un servizio autonomo o una garanzia che i provider citati siano disponibili. Il sapere proviene da [Semantic Timelapse Formation](SKILL_IT.md) e dal [mini-kernel operativo VC-30s](VC30_KERNEL_OPERATIVO_IT.md).

## MKCV — Mini Kernel Code Video, oltre il profilo di 30 secondi

**MKCV** è il nome della composizione di competenze per produrre video in codice. **VC-30s** identifica un profilo di durata breve. Le postazioni di questa guida possono contribuire a film di diversa durata, formato e linguaggio visivo quando il soggetto le richiede.

**Metodo operativo pubblico:** usa queste istruzioni con gli strumenti effettivi del tuo ambiente. Conserva immagine A generata e osservata, scena B modificabile e film esportato per poter riprendere e migliorare il lavoro.

## Perché è uno studio-lab e non una lista di applicazioni

Un video breve richiede capacità diverse: capire l'oggetto, idearlo, formare un'immagine di riferimento, conservare identità di persone e oggetti, costruire il loro movimento, formare testo e suono, renderizzare, osservare, consegnare e imparare dal risultato. **Ogni postazione possiede uno specifico saper fare**, con un ingresso e un contributo. Possono operare nello stesso assistente o comporsi attraverso più riceventi: la presenza del documento non li avvia da sola.

Le postazioni sono **competenze attivabili quando pertinenti**, non undici passaggi obbligatori né una sequenza inviolabile. Un'immagine statica può concludere correttamente un lavoro; una voce può precedere la regia; il riferimento generato può far cambiare il soggetto.

## Le undici postazioni del laboratorio

| Postazione / competenza | Sapere che attiva nel lavoro | Contributo riusabile |
| --- | --- | --- |
| **Sorgente e concetto** — competenza del dominio/editoriale | Distingue fatto, interpretazione, ricostruzione e possibilità; individua soggetto, relazione, conseguenza e destinatario | Nucleo del film; ciò che può essere rappresentato senza inventare eventi |
| **Direzione visiva** — composizione percettiva | Forma la domanda visiva e la grammatica di materia, attori, geometria, luce e profondità; non impone look già usati | Condizioni per l'immagine generata e per la gerarchia |
| **Immagine A** — formazione generativa | Forma istruzioni ancorato alle fonti, usa un vero generatore e osserva l'immagine; A è prima nel lavoro, non necessariamente `t=0` | Asset A accessibile, prompt/provenienza, comprensioni e ambiguità |
| **Attori e asset** — asset craft/continuità | Riconosce che cosa deve muoversi autonomamente, se servono pose, strati, sprite, rig o volumi reali; preserva identità e provenienza | Elementi realmente disponibili e relazione fra i loro gesti |
| **Regia e storyboard** — competenza temporale | Distingue causa, successione, simultaneità, confronto e ritorno; rende visibile la trasformazione e gli istanti da comprendere | Scene, attenzione, cue e continuità di mondo/camera |
| **Scena B e animazione** — programmazione del medium | Traduce il riferimento in scena editabile 2D/2.5D/3D, calcola stato/posa a un tempo T, gestisce asset e preview | Primo frame B codificato, scena e capacità di render |
| **Parole e voce** — scrittura/comunicazione | Mantiene frasi e dati esatti e editabili, forma narrazione e didascalie, sceglie spazi di lettura e tempi reali della voce | Copia, caption e battute legate ai gesti, o scelta del silenzio |
| **Suono** — sound design | Riconosce eventi sonori, atmosfera, musica, timing e diritti; non inserisce una colonna sonora perché “serve sempre” | Cue/tracce/mix pertinenti o nessun audio |
| **Render e osservazione** — produzione e percezione | Esporta con mezzi esistenti e osserva frame significativi e file reale; distingue export, estetica e verità rappresentata | Video/file misurato, fotogrammi osservati, correzioni locali |
| **Consegna e derivati** — produzione/canale | Rende adatte varianti, formati, sottotitoli e file editabili; riconosce quando 9:16 richiede nuova composizione | Uscita realmente accessibile nel canale selezionato |
| **Apprendimento e continuità** — meta-competenza | Distingue il risultato da una correzione riusabile; fa tornare il sapere al metodo che deve agire diversamente | Capacità migliorata, caso aggiornato e ingresso per il lavoro successivo |

## Animare il soggetto della reference

Chiarisci quale movimento è affidato: animare il personaggio e gli oggetti raffigurati nella reference, costruire un modello da quella figura oppure creare una scena nuova dal medesimo concetto. Le tre richieste possono richiedere asset e metodi differenti.

Quando la richiesta è image-to-motion, la postazione di A deve formare/riconoscere un gesto **dentro l'immagine**. la produzione tecnica può usare maschere, strati 2.5D, asset aggiuntivi coerenti, ricostruzione delle zone occluse, modello 3D reale se pertinente o un provider image-to-video quando effettivamente disponibile. Non inferire rig, retro o movimenti nascosti da un'immagine piatta. I diagrammi sovrapposti sono ammessi quando aiutano davvero, non sono un surrogato del movimento del soggetto.

**Possibilità tecnologica, non dipendenza:** [Motion.so MCP](https://docs.motion.so/guides/mcp) permette a un agente connesso di creare/rivedere video, allegare media tramite upload e ricevere un filmato. Questo non dimostra la fedeltà dell'animazione dell'immagine di partenza. Il servizio richiede accesso account/OAuth e può consumare crediti; un file locale va caricato realmente. Il prodotto Motion presenta integrazioni social, ma gli strumenti MCP video documentati **non confermano una pubblicazione social diretta**. L'responsabile del canale e l'autorizzazione restano distinti.

## Conservare identità e geometria nell’animazione 2.5D

Per movimenti limitati puoi estrarre testa, braccio o altre parti pertinenti dalla reference, definirne maschere e pivot e ricostruire le zone che il moto rende visibili. Conserva la distinzione tra pixel originali e sfondo ricostruito. Luce e camera devono continuare a descrivere lo stesso ambiente.

Distingui tre modalità produttive: animare la stessa immagine con livelli 2.5D; costruire una geometria 3D dalla reference; creare una scena nuova interamente in codice. Il primo metodo serve movimenti e viste limitati. Per rotazioni libere, nuove superfici e occlusioni serve la geometria pertinente. Scegli attraverso il soggetto e l’effetto richiesto.

Le competenze [cinetic](https://github.com/Leonxlnx/cinetic) e [img2threejs](https://github.com/img2threejs/img2threejs) forniscono sapere sul film diretto da un soggetto e sulla analisi di componenti/giunti/materiali rispetto ad una reference. [Remotion skills](https://github.com/remotion-dev/skills) rende esplicite le capacità di composizione, preview e render. Prendiamo **metodi**, non il codice, le palette o le norme stilistiche interne di questi progetti.

Una ricostruzione delle palpebre o del volto può alterare l’identità del personaggio. Osserva la resa e scegli un gesto più piccolo quando conserva meglio il soggetto. I cartelli già presenti nella reference appartengono alla scena originale; nuovi pannelli o diagrammi aggiungono invece un altro livello di rappresentazione. Se serve un diverso linguaggio cinematografico, forma una nuova reference o un modello coerente.

## Come entrare operativamente

Quando c'è un soggetto concreto, iniziare dalle **fonti reali del caso**. Identificare che cosa deve cambiare nella percezione e raggiungere la competenza adatta; non compilare tutte le postazioni per rito.

Nel percorso di questa competenza, formare le istruzioni e **generare con un image generator una vera immagine A**, poi osservarla. L'immagine può essere un personaggio, una vista centrale, una scena madre, un momento di azione non iniziale: *prima nella produzione non equivale a primo frame del film*. Se servono parti animate indipendentemente, creare soltanto le risorse pertinenti coerenti con A, senza attribuirle una mesh o un rig invisibile.

Progettare il cambiamento temporale dal **tipo di relazione del soggetto**. Costruire la scena in codice B e il suo primo frame `t=0`, con le effettive capacità del ricevente. Un renderer video dovrebbe poter ricostruire il frame a un tempo richiesto senza dipendere da un timer libero del browser. Video da screenshot con cursore simulato sono **ricostruzioni**, non registrazioni di un prodotto operativo.

Se immagini, asset e codice vivono in riceventi diversi, il receiver che costruisce B deve poter **aprire davvero il file A**. Una descrizione testuale o una skill letta non trasferisce i byte dell'immagine. Tracce audio, licenze e credenziali dei provider rimangono condizioni reali da risolvere.

Osservare l'artefatto prima di dichiararlo consegnato: durata, formato e codec richiedono evidenza del file, mentre leggibilità e continuità richiedono vedere fotogrammi/movimento. Nessuna osservazione interna certifica da sola che il pubblico reale abbia compreso il contenuto.

## Fascicolo minimo per una produzione

Creare un fascicolo **solo quando un caso è selezionato**, con la profondità necessaria:

- **Oggetto:** fonte/versione, soggetto, situazione di ricezione e statuto (fatto, ricostruzione, allegoria, possibilità).
- **Competenze effettivamente partecipanti:** perché sono entrate e quale contributo hanno prodotto.
- **A:** prompt, asset davvero generato, percorso realmente accessibile, osservazioni e limite; non confonderlo con B.
- **B:** scena/asset codificati, primo frame, tempo e capacità del renderer; A può rappresentare un altro momento.
- **Output:** MP4/altri file realmente esistenti, durata/fps/risoluzione o audio quando misurati, canale/destinazione.
- **Ritorno:** differenza causalmente riusabile, competenza che deve cambiare, dove il sapere è stato conservato e condizione per il seguito.

Il fascicolo è un mezzo di continuità, non un modulo da riempire sempre. File generati e diritti rimangono nel proprio spazio; non pubblicare asset personali/riservati per facilitare il passaggio fra AI.

## Conoscenza acquisita, senza incorporare codice di terzi

I metodi sono stati approfonditi a partire da [HyperFrames](https://github.com/heygen-com/hyperframes), [Remotion](https://github.com/remotion-dev/remotion), [PixiJS + GSAP](https://github.com/AhmadDinkaa/pixijs-tic-tac-toe), [GSAP + Three.js](https://github.com/TheWebxite/phans-custom-tailor), [Motion Video](https://github.com/bestagentkits/motion-video-skill), [iart motion skills](https://github.com/iart-ai/motion-skills) e [modern-portfolio](https://github.com/sanidhyy/modern-portfolio). L'apprendimento riguarda scene, tempo, asset e movimento **situati**. Non abbiamo importato codice, effetti, font o immagini dai repository indicati e non dichiariamo studiati tutti i loro file. Dipendenze e licenze si risolvono soltanto quando un lavoro realmente le usa.

**Arresto:** la competenza può concludere con un film, con un metodo migliorato o con una diversa rappresentazione più adeguata. Un laboratorio operativo non prescrive una durata o un formato indipendenti dal caso.
