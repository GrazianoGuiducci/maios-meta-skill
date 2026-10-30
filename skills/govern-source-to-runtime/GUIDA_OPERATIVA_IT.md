# Govern Source to Runtime — sapere operativo pratico

## Le credenziali restano presso il nodo che ne possiede la policy

Usa l’adattatore autorizzato del tuo ambiente, con autenticazione non interattiva quando prevista. Non stampare, salvare nel codice o trasferire a un altro host il token locale, nemmeno codificato. Un bundle o un artefatto immutabile possono trasportare una revisione senza trasportarne la credenziale, quando quel trasferimento è compreso nell’incarico. Un errore di accesso non autorizza un altro account.


## La configurazione effettiva può differire dal file vicino

Un server può includere una copia indipendente anziché il template atteso. Leggi la configurazione realmente consumata, il tipo di file e i byte. Un percorso canonico, da solo, non prova un collegamento simbolico. Nelle prove isolate preserva la risoluzione corretta di moduli e dipendenze: un prefisso di test sbagliato può produrre un falso guasto del candidato.


## La salute ha tempi e forme propri

Dopo un riavvio attendi la convergenza entro un termine breve, conservando l’ultimo riscontro. Un rifiuto di connessione durante l’avvio non prova un guasto definitivo. Un servizio che esegue una singola operazione può tornare inattivo dopo un esito riuscito: conserva risultato, codice d’uscita e controllo terminale, anziché fingere attività continua. Una prova manuale conserva utente e gruppo effettivi.


## Una nuova identità non cancella tutte le prove precedenti

Riusa una prova soltanto per la relazione rimasta applicabile e con la sua identità originaria. Aggiorna revisioni, concorrenza, artefatto, controller e destinazione quando possono cambiare l’effetto. Un metodo o un controller cambiati riaprono le dipendenze pertinenti; non serve ricominciare tutto se la contraddizione è locale. Un’istruzione configurata non sostituisce l’ultima installazione realmente confermata.


## Supporto dichiarato e prova eseguita sono informazioni diverse

Minimo tecnico, piattaforme dichiarate e matrice effettivamente esercitata non coincidono. Verifica l’attribuzione di una dipendenza al suo tag e commit, compresi i tag annotati. Un archivio rigenerato cambia identità: rileggi il risultato corrente prima di un rilascio immutabile. La revisione dei file non decide da sola il significato di una modifica alla compatibilità.


## Il recupero riguarda tutti gli effetti cambiati

Tornare a un commit non ripristina necessariamente dati, notifiche o servizi esterni. Qualifica ripristino o compensazione presso i rispettivi responsabili. Mantieni indipendente la versione precedente e non usare riscritture forzate della storia condivisa come sostituto del recupero. La pulizia finale riguarda soltanto file del tentativo identificati e verificati.


## Gli strumenti inclusi leggono dati, non certificano il mondo

scripts/reduce_release_state.py riduce osservazioni a una prossima azione; scripts/validate_effect_request.py controlla coerenza, identità, servizi, recupero e selezione dell’effetto secondo gli schemi inclusi. Leggi TOOLS_IT.md per esempio e comandi. Un risultato ready è relativo alle evidenze fornite: nessuno dei due strumenti interroga account, pubblica, riavvia o concede permessi.


## L’automazione appartiene a una transizione qualificata

Una procedura riuscita non rende automaticamente governabili tutti i server. Per automatizzare servono contratto ristretto, idempotenza, separazione dei privilegi, osservazione terminale e recupero esercitati nel contesto pertinente. Anche rami, diff, log e artefatti di una pubblicazione possono esporre dati: trasferisci sapere riusabile, mantenendo privati dettagli e credenziali.

## La pubblicazione impara dal proprio percorso

Il metodo e i validatori deterministici sono disponibili; una distribuzione automatica universale non è fornita dal kit. Ogni ambiente possiede esecutori, accessi e politiche propri.

Un risultato osservato può insegnare una relazione riusabile. Il successivo uso non identico mostra dove quell’apprendimento continua e dove il metodo va affinato.
