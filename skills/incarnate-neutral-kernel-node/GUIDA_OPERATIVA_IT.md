# Incarnate Neutral Kernel Node

## Formare un ricevente conservandone la vita propria

Distingui pacchetto sorgente, fork o adattamento del nodo, proiezione configurata, file installati nell'host e conversazione presente. Una prima incarnazione forma un ricevente iniziale. Un aggiornamento incontra decisioni, conoscenza ed effetti locali già presenti: conservali comprendendo quali cambiamenti sorgente restano utili. Pari versioni non stabiliscono pari significato e versioni diverse non implicano un difetto.

Collega ogni funzione sorgente materiale all'owner ricevente che la porta. Adatta discovery, ingresso, persistenza, mezzi e apprendimento all'host effettivo; una cartella rinominata non trasporta quelle funzioni. Conserva ragioni delle relazioni respinte o differite quando un rientro le perderebbe. Un cambiamento valutato resta pendente fino all'implementazione ricevente e all'uso pertinente; file upstream invariati non completano quel lavoro.

## Ispezionare una coppia sorgente/ricevente selezionata

`scripts/inspect_kernel_pair.py` adatta in sola lettura l'ispettore sorgente. Usa Python 3.10+ e Git, senza chiamate di rete. Copia `references/port-map.example.json` nel progetto e imposta percorsi dei due repository, eventuale ambito sorgente, commit e tree valutati, percorsi degli owner e relazioni pendenti. Sostituisci i segnaposto con valori reali; l'esempio illustra un formato, senza affermare fatti sui tuoi repository.

Usa `git -C SOURCE rev-parse HEAD` per il commit valutato e `git -C SOURCE rev-parse HEAD:kernel` per un sottoalbero selezionato; `HEAD^{tree}` per l'intero repository. Per il destinatario usa il tree dell'intero repository. Esegui `python scripts/inspect_kernel_pair.py --workspace PATH --map PATH_TO_MAP`. I percorsi nel file possono essere relativi al workspace o assoluti. `python scripts/test_inspect_kernel_pair.py` esercita attualità dell'ambito e lavoro pendente con repository Git temporanei.

Il rapporto espone identità correnti, lavoro non committato, differenze pertinenti, percorsi mancanti e integrazione pendente. Un commit estraneo può lasciare invariato il sottoalbero valutato. Un commit valutato assente rende indisponibile il confronto: non inventare equivalenza. Il lavoro locale è mostrato separatamente perché il confronto dei tree committati non lo include. Leggi una differenza locale pertinente prima di agire. Il rapporto non installa, unisce, chiude relazioni o prova trasferimento semantico. Segui significato e sapere ricevente, registrando ciò che implementazione e uso dimostrano. Conserva uno stato recuperabile della superficie esatta senza azzerare lavoro di altri owner.
