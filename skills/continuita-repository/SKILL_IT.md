---
name: continuita-repository
description: "Comprende lo stato del repository selezionato e porta avanti le modifiche pertinenti preservando lavoro concorrente e identità della revisione condivisa. Quando più assistenti o persone lavorano sullo stesso progetto e il risultato non deve restare nascosto in un checkout locale."
---

# Maintain Repository Continuity

**Condividere il lavoro AI tra repository e collaboratori**

Mantiene riconoscibile la relazione tra modifiche locali, commit e sorgente condivisa.

## Scopo e situazione

Comprende lo stato del repository selezionato e porta avanti le modifiche pertinenti preservando lavoro concorrente e identità della revisione condivisa.

Usa questa competenza: quando più assistenti o persone lavorano sullo stesso progetto e il risultato non deve restare nascosto in un checkout locale.

Un lavoro salvato può restare invisibile a chi deve continuarlo. Questa competenza collega il risultato locale alla sorgente condivisa del progetto, mantenendo chiaro che cosa appartiene alla modifica selezionata.

La continuità comprende le ragioni del cambiamento, i contributi concorrenti e la revisione che il collaboratore può davvero leggere. Commit, condivisione e pubblicazione del prodotto restano effetti distinti.

## Individuare repository e risultato selezionati

Raggiungi il repository che possiede il lavoro e le sue istruzioni attuali. Comprendi che cosa deve diventare condiviso e perché serve al seguito. Una cartella contenitore può ospitare più repository: non trattarli come un unico oggetto. La continuità diventa pertinente a un risultato significativo o a un passaggio di consegne, non richiede una chiusura Git dopo ogni modifica o una pubblicazione durante una richiesta di sola lettura.

## Comprendere le identità presenti

Distingui file di lavoro, commit locali, riferimento di tracciamento, revisione remota verificata e artefatti generati o ignorati. Usa gli strumenti Git e l'accesso previsti dal progetto per vedere ramo, differenze e rapporto con il remoto. Un riferimento locale può essere vecchio; un fetch riuscito non dimostra che il contenuto selezionato sia già condiviso. Evita di stampare o salvare credenziali mentre acquisisci queste informazioni.

## Preservare i contributi concorrenti

Leggi il significato delle modifiche prima di preparare il commit. Seleziona solo i file o le porzioni appartenenti al lavoro autorizzato. Un cambiamento vecchio o non ancora salvato in un commit non è per questo rumore eliminabile. Con contributi locali e remoti indipendenti, integra preservando entrambe le linee; se si sovrappongono sullo stesso oggetto, risolvi la relazione prima di scegliere il contenuto. Non ottenere ordine apparente cancellando lavoro valido.

## Completare l'effetto autorizzato

Quando il mandato corrente copre commit e condivisione, controlla il contenuto pertinente, esegui verifiche proporzionate, crea un commit coerente e condividi sul ramo previsto attraverso l'autenticazione del destinatario. Non trasferire la policy di credenziali o di push di un altro ambiente. Se l'effetto non è autorizzato o il mezzo manca, conserva il lavoro e indica il passaggio specifico ancora aperto senza dichiarare la sorgente condivisa.

## Verificare ciò che il collaboratore riceverà

Dopo la condivisione, verifica la revisione remota e la relazione con il risultato locale e il tracking. Se una riconciliazione produce identità diverse, spiega quali commit o contenuti corrispondono e quali restano distinti. Dai al collaboratore un riferimento esatto con ragioni e controlli rilevanti. Una sorgente raggiungibile non prova che sia stata letta, installata o eseguita. Deploy, release e attivazione richiedono il loro riscontro.

## Far continuare la conoscenza del cambiamento

Conserva nella guida del progetto il cambiamento utile, il perché, la revisione, le verifiche e l'eventuale lavoro rimasto locale. Se un nuovo caso espone una perdita o una procedura superflua, correggi il metodo di continuità. Il suo scopo è rendere il lavoro condivisibile e ricostruibile, non creare un rituale di Git o mantenere tutti i repository dell'ambiente sincronizzati per forza.

## Profondità del metodo

Questa è una competenza tecnica di continuità sorgente. Il numero di repository o di agenti non le attribuisce automaticamente un livello meta.

Il metodo può diventare oggetto di apprendimento quando un passaggio di consegne mostra che una modifica condivisa non era raggiungibile dal collaboratore. Correggere quell'ingresso cambia il modo di conservare la continuità. È diverso da un processo autonomo che esegue push a intervalli, e non autorizza tale processo.

## Continuità e apprendimento

Un caso successivo mostra se il lavoro arriva alla sorgente condivisa senza perdita e senza dover ricostruire la situazione. Un controllo tecnico resta legato alla revisione che ha effettivamente verificato.

Nel primo uso, parti dal contesto e dalle fonti effettivamente disponibili. Il metodo può essere esercitato in chat; persistenza, strumenti e azioni esterne dipendono dai mezzi e dal mandato del destinatario. Le istruzioni rendono la capacità utilizzabile, mentre il suo comportamento e il suo valore richiedono osservazione nel lavoro reale.
