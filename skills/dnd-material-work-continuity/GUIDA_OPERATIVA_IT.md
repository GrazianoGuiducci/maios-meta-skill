# D-ND Material Work Continuity

## Usare il registratore deterministico quando conta l'integrità esatta degli eventi

Il metodo testuale si usa anche da solo. Il kit fornisce inoltre reducer Python, schema JSON di eventi/stato, un registro d'esempio e test portabili della competenza sorgente. Il reducer verifica l'integrità del registro, senza diventare un'ammissione semantica o un'autorità indipendente. Gli hash rilevano registrazioni incoerenti; non provano la verità di una frase o di un riferimento di evidenza. Conserva registro originale e riferimenti alle fonti nel progetto proprietario.

I sette tipi di evento conservano fonte esatta, proiezione dell'assistente, movimento osservato, ritrattazione o superamento, cambio di autorità, cambiamento delle incognite e punto della relazione corrente. Le fonti mantengono l'attribuzione. Le proiezioni citano eventi precedenti. Una correzione supera un'interpretazione senza cancellare l'evento o gli effetti osservati. Il checkpoint espone fonti correnti, incognite residue e prossima azione permessa. Le fonti classificate segrete conservano un indicatore di lacuna, senza valori o hash del segreto. Non copiare credenziali nel registro.

## Eseguire l'esempio incluso

Usa Python 3.10 o successivo dalla cartella della competenza. Esegui `python scripts/demo_continuity.py --output-dir demo-ledger` scegliendo una cartella nuova. Scrive stato iniziale, sei eventi illustrativi con i rispettivi stati successivi e `reconstruction.json`. L'esempio corregge l'interpretazione di pubblicazione dell'assistente conservando una bozza realmente salvata. Non pubblica né contatta nessuno.

Esegui `python scripts/reduce_material_work_continuity.py verify --state demo-ledger/C1.state.json` per ricostruire quello stato. Per il tuo progetto, `init` accetta `--owner-surface`, `--owner-state-ref`, `--authority` e `--output` facoltativo. `reduce` accetta `--state`, `--event` e `--output` facoltativo; usa un file di uscita separato per conservare lo stato precedente. `previous_state_digest` dell'evento deve corrispondere allo stato che estende. L'esempio mostra la costruzione degli eventi attraverso l'interfaccia Python.

## Comprendere errori e limiti

La ripetizione esatta è idempotente; un evento alterato con la stessa identità viene respinto. Sono respinti predecessore superato, stato alterato, riferimento di autorità fabbricato o risoluzione di un'incognita priva di evidenza. Una fonte strutturata di concessione dell'autorità modella il cambiamento registrato; lo strumento non autentica la persona dietro un documento esterno. La fonte referenziata deve essere un file regolare assoluto con il digest registrato, al massimo 1 MiB; riferimenti mancanti, simbolici o cambiati rendono incompleta la ricostruzione. Le fonti esatte inline restano nel registro.

La CLI scrive soltanto l'uscita scelta e non usa la rete. Scrittori concorrenti richiedono serializzazione nel reale file o archivio; il reducer da solo non fornisce lock o transazioni. Lo stato valido per schema viene controllato anche ripercorrendo la catena degli eventi. Esegui i test portabili con `python -m pip install -r requirements-test.txt` e poi `python scripts/test_reduce_material_work_continuity.py`. Il reducer usa solo la libreria standard; `jsonschema` serve ai test dello schema. Lo schema mantiene i nomi del protocollo originale per compatibilità, con identificatore pubblico e percorsi Windows/POSIX.
