# Strumenti di lettura per il rilascio

Il kit include il riduttore deterministico e il validatore delle richieste del metodo sorgente. Leggono JSON fornito da te. Non ispezionano repository o account, non dimostrano la verità delle dichiarazioni, non approvano effetti, non pubblicano, non riavviano e non riparano un rilascio.

## Eseguire gli esempi fittizi forniti

Dalla cartella completa della competenza, con Python 3.10 o successivo:

```text
python scripts/reduce_release_state.py --self-test
python scripts/validate_effect_request.py --self-test
python scripts/reduce_release_state.py examples/release-context.sample.json
python scripts/validate_effect_request.py examples/effect-request.sample.json
```

L’esempio del riduttore rappresenta sorgente già promossa, runtime differente e autorità di attivazione assente. Restituisce await_runtime_gate anziché attivare. L’esempio della richiesta è sintetico, con revisioni ed evidenze segnaposto: il suo esito ready controlla la coerenza della fixture, non autorizza l’uso di quei dati su un sistema reale. Conservalo come dimostrazione e forma i tuoi dati dalle fonti effettive.

## Fornire le evidenze del proprio effetto

Leggi references/release-context.schema.json per i fatti osservati del ciclo e references/effect-request.schema.json per una richiesta esatta. Collega destinazione, revisione, servizi consentiti, località delle credenziali, versione precedente e verifiche compiute alle rispettive prove. Il validatore restituisce ready, needs_operator_decision o blocked. Una richiesta modificata produce una diversa impronta. L’identificatore dnd.effect-request.v1 conserva il protocollo sorgente dello strumento; non richiede il workspace che lo ha generato.

Gli strumenti usano la libreria standard Python. Se jsonschema è installato, il validatore esegue anche lo schema JSON incluso; i propri controlli strutturali e semantici funzionano senza quella dipendenza facoltativa. I self-test esercitano casi positivi e condizioni di arresto senza rete o controllo dei servizi. references/capability-manifest.json conserva lo stato candidato dell’automazione sorgente. Una fixture coerente non qualifica il tuo controller, host o recupero.
