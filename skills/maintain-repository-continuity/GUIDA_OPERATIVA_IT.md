# Maintain Repository Continuity

## Riconciliare il lavoro selezionato con la sorgente condivisa

Identifica checkout proprietario, branch, percorsi selezionati, modifiche locali, upstream e identità remota reale. Il contenitore di lavoro può avere repository indipendenti. Non attribuire ogni file sporco alla task. Conserva corsie concorrenti e lavoro già staged; prepara soltanto il contributo selezionato. Il tracking è osservazione memorizzata finché non aggiornato con il meccanismo credenziali autorizzato.

Se locale e remoto sono cambiati indipendentemente, comprendi sovrapposizioni pertinenti e conserva entrambi i contributi validi. Usa l'integrazione minima che continua il lavoro; reset o sincronizzazione forzata possono cancellare sapere estraneo. Prima di condividere rivedi diff selezionato e controlli pertinenti. Commit e push seguono autorità e policy credenziali esistenti, senza stampare o conservare segreti.

Verifica ciò che contiene il remoto effettivo e distingui condivisione sorgente da installazione, deploy e comportamento pubblico. In alcuni progetti il push attiva un deploy separato: comprendi la relazione prima di invocarlo. Conserva identità condivisa e condizione di recupero se servono al seguito. Un checkout pulito non stabilisce correttezza del prodotto e i soli conteggi ahead/behind non decidono quale significato prevale.
