# VC-30s Studio-Lab — produrre video in codice con competenze specializzate

**Stato:** metodo pubblico **candidato 0.4.1**. Si può usare come **guida di lavoro in una chat o in un harness** che possieda strumenti reali per immagini, file, codice e render. **Non** è uno studio software installato, un servizio autonomo o una garanzia che i provider citati siano disponibili. Il sapere proviene da [Semantic Timelapse Formation](SKILL_IT.md) e dal [mini-kernel operativo VC-30s](VC30_KERNEL_OPERATIVO_IT.md).

## MKCV — Mini Kernel Code Video, oltre il profilo di 30 secondi

**MKCV** è il nome del mini-kernel di competenze per produrre video in codice. **VC-30s** identifica un **profilo di durata** e i primi esercizi che hanno contribuito a formarlo, non il limite dei video che MKCV può affrontare. Questo Studio-Lab è **un solo laboratorio**: le sue undici postazioni restano facoltà riutilizzabili per altri durate, formati, personaggi, 2.5D/3D, audio e forme di rappresentazione quando il soggetto le richiede.

**Stato del metodo pubblico candidato:** struttura e sapere sono leggibili in queste istruzioni; non significa image generator, renderer o lavoro multi-agente installati nel ricevente. Il completamento produttivo si potrà osservare in un caso con A realmente generata/osservata, scena B programmata, film decodificato e lavoro recuperabile. Un secondo caso non identico permetterà di comprendere quale apprendimento è diventato effettivamente riusabile. Pubblicare una clip o una release rimane una decisione separata.

## Perché è uno studio-lab e non una lista di applicazioni

Un video breve richiede capacità diverse: capire l'oggetto, idearlo, formare un'immagine di riferimento, conservare identità di persone e oggetti, costruire il loro movimento, formare testo e suono, renderizzare, osservare, consegnare e imparare dal risultato. **Ogni postazione possiede uno specifico saper fare**, con un ingresso e un contributo. Possono operare nello stesso assistente o comporsi attraverso più riceventi: la presenza del documento non li avvia da sola.

Le postazioni sono **competenze attivabili quando pertinenti**, non undici passaggi obbligatori né una sequenza inviolabile. Un'immagine statica può concludere correttamente un lavoro; una voce può precedere la regia; il riferimento generato può far cambiare il soggetto.

## Le undici postazioni del laboratorio

| Postazione / competenza | Sapere che attiva nel lavoro | Contributo riusabile |
| --- | --- | --- |
| **Sorgente e concetto** — competenza del dominio/editoriale | Distingue fatto, interpretazione, ricostruzione e possibilità; individua soggetto, relazione, conseguenza e destinatario | Nucleo del film; ciò che può essere rappresentato senza inventare eventi |
| **Direzione visiva** — composizione percettiva | Forma la domanda visiva e la grammatica di materia, attori, geometria, luce e profondità; non impone look già usati | Condizioni per l'immagine generata e per la gerarchia |
| **Immagine A** — formazione generativa | Forma istruzioni source-bound, usa un vero generatore e osserva l'immagine; A è prima nel lavoro, non necessariamente `t=0` | Asset A accessibile, prompt/provenienza, comprensioni e ambiguità |
| **Attori e asset** — asset craft/continuità | Riconosce che cosa deve muoversi autonomamente, se servono pose, strati, sprite, rig o volumi reali; preserva identità e provenienza | Elementi realmente disponibili e relazione fra i loro gesti |
| **Regia e storyboard** — competenza temporale | Distingue causa, successione, simultaneità, confronto e ritorno; rende visibile la trasformazione e gli istanti da comprendere | Scene, attenzione, cue e continuità di mondo/camera |
| **Scena B e animazione** — programmazione del medium | Traduce il riferimento in scena editabile 2D/2.5D/3D, calcola stato/posa a un tempo T, gestisce asset e preview | Primo frame B codificato, scena e capacità di render |
| **Parole e voce** — scrittura/comunicazione | Mantiene frasi e dati esatti e editabili, forma narrazione e didascalie, sceglie spazi di lettura e tempi reali della voce | Copia, caption e battute legate ai gesti, o scelta del silenzio |
| **Suono** — sound design | Riconosce eventi sonori, atmosfera, musica, timing e diritti; non inserisce una colonna sonora perché “serve sempre” | Cue/tracce/mix pertinenti o nessun audio |
| **Render e osservazione** — produzione e percezione | Esporta con mezzi esistenti e osserva frame significativi e file reale; distingue export, estetica e verità rappresentata | Video/file misurato, fotogrammi osservati, correzioni locali |
| **Consegna e derivati** — produzione/canale | Rende adatte varianti, formati, sottotitoli e file editabili; riconosce quando 9:16 richiede nuova composizione | Uscita realmente accessibile nel canale selezionato |
| **Apprendimento e continuità** — meta-competenza | Distingue il risultato da una correzione riusabile; fa tornare il sapere al metodo che deve agire diversamente | Capacità migliorata, caso aggiornato e ingresso per il lavoro successivo |

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
