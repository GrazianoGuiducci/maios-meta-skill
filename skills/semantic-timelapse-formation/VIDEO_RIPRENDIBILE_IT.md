# Conservare il film quando il rendering si interrompe

Quando un rendering è lungo o si interrompe, conserva la timeline prevista e calcola intervalli di fotogrammi raggiungibili indipendentemente. Riusa un segmento solo dopo aver verificato input, identità del codice, numero di frame, dimensioni, frequenza e decodifica. Una scena, un asset o un renderer cambiato richiedono una nuova identità dell’output. I segmenti sono unità di esecuzione; montaggio, gesto e ritmo narrativo restano scelte sul film.

## Uso locale

Il job incluso seleziona soltanto un renderer originale fidato, con SHA256 esplicito. FFmpeg e ffprobe devono essere già installati e raggiungibili nel PATH; non vengono scaricati dallo script. Dalla cartella della competenza:

```sh
cd examples/recoverable_video
python -m venv .venv
# Attiva questo ambiente con il comando adatto alla tua shell.
python -m pip install -r requirements.txt
python autostudio.py plan jobs/orbital_scene.json
python autostudio.py run jobs/orbital_scene.json --max-chunks 1
python autostudio.py run jobs/orbital_scene.json
python verify_recovery.py --output NEW_EMPTY_LOCATION
```

## Interpretare la continuazione

Il primo run termina con stato `partial` e codice di uscita 4: è una sospensione controllata dopo un segmento, non un fallimento e non un job rimasto in background. La seconda invocazione dello stesso job verifica i segmenti, completa il film e restituisce `completed`; una nuova invocazione restituisce `reused_verified`. `needs_capability_or_input` indica mezzi o input mancanti; `checkpoint_conflict` conserva il lavoro precedente quando l’identità è cambiata. Scegli una nuova directory per un lavoro cambiato; non cancellare i checkpoint per far passare il controllo. I quattro profili del catalogo richiedono i propri materiali; questa confezione include una scena in codice, non i media di altri esempi. `reference_3d` esegue un renderer locale già scritto e fidato con gli input forniti dal progetto: non ricostruisce automaticamente un’immagine.

## Competenze e prove

Il checkpoint tecnico conserva lavoro verificato. La guida del progetto conserva soggetto, fonti, ragioni, scelte aperte e ciò che il prossimo contributore deve comprendere. Componili quando serve: riprendere un encoder non ricostruisce la comprensione di un assistente e non avvia un agente in background. L’osservazione del film risultante può ancora cambiare scena, metodo o mezzo scelto.

L’adattatore per scene in codice incluso è stato esercitato in un ricevente Windows con sospensione/ripresa, interruzione reale dell’albero di processo, riparazione di un segmento danneggiato e confronto con un render continuo. Questo non attesta qualità narrativa, fedeltà immagine→3D, recupero cross-host o accesso a un provider media. Il rapporto `examples/recoverable_video/VERIFICATION.json` conserva la prova tecnica. I test dell’archivio precedente e i suoi media non sono parte di questo pacchetto. Lo script di verifica incluso esercita il contratto locale su una cartella nuova.
