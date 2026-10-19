"""Assemble resource entries without rewriting existing public methods."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    path = ROOT / 'catalog.json'
    catalog = json.loads(path.read_text(encoding='utf-8'))
    resources = {r['id']:r for r in catalog['resources']}
    for entry in sorted((ROOT/'skills').glob('*/catalog-entry.json')):
        item = json.loads(entry.read_text(encoding='utf-8'))
        assert item['id'] == entry.parent.name
        resources[item['id']] = item
    resources['meta-activity']['review_id'] = '00'
    ordered = sorted(resources.values(), key=lambda x:x.get('review_id',x['id']))
    assert {x['review_id'] for x in ordered} == {f'{x:02}' for x in range(25)}, 'The selected collection is incomplete'
    catalog['resources'] = ordered
    path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    rows = ['| Risorsa | Cosa permette di fare | Tipo |', '| --- | --- | --- |']
    for r in ordered:
        p=r['it']
        title = r['name'] if r['id']=='meta-activity' else p['title']
        rows.append(f"| [{title}]({r['guide']}) | {p.get('does',p.get('what_it_does'))} | {p.get('kind',p.get('type'))} |")
    readme='''# MAIOS Meta-Skill

**25 risorse per lavorare con l’AI, formare competenze e farne evolvere il metodo.**

La raccolta porta il sapere nato nel lavoro MAIOS in competenze utilizzabili nella propria chat o nel proprio ambiente agentico. Ogni risorsa include metodo completo, guida, avvio da copiare ed esempi. Le pagine MAIOS spiegano subito cosa fa e quando usarla, poi ne approfondiscono il funzionamento.

[Aprire la raccolta sul sito](https://maios.it/risorse/) · [English pages](https://maios.it/resources/) · [Guida comune](docs/USO.md) · [Concetti: competenza, meta e autologica](docs/CONCETTI.md)

## Scegliere una risorsa

La raccolta comprende competenze operative, metacompetenze, funzioni e fondamenti del kernel. I tipi esprimono contributi diversi. KA è il kernel fondativo; FDLA è la funzione di correzione nel movimento. Il numero di componenti o la parola “meta” non indicano un grado di qualità.

'''+ '\n'.join(rows)+'''

## Comporre le capacità intorno al lavoro

Un incarico può rendere pertinenti più risorse. Questi ingressi aiutano a riconoscerne il contributo senza imporre una sequenza fissa:

- **Insegnare un lavoro alla propria AI:** [formare competenze](skills/creare-comporre-competenze/README.md), [farle evolvere](skills/evolvere-competenze/README.md) e [conservare il sapere utile](skills/conservare-conoscenze-utili/README.md). Gli esempi e le correzioni possono cambiare anche il metodo con cui l’AI apprende quel lavoro.
- **Sviluppare possibilità per un progetto:** [formare il metodo](skills/organizzare-lavoro-complesso/README.md), [comprendere fonti e segnali](skills/fonti-segnali-conoscenza/README.md) e [formare attività](skills/meta-activity/README.md). Il contesto può far emergere un contributo diverso dalla prima rappresentazione del problema.
- **Continuare un progetto:** [continuità del lavoro](skills/continuita-del-lavoro-ai/README.md), [ricostruzione degli eventi](skills/ricostruire-lavoro-decisioni/README.md) e [condensato del sapere](skills/conservare-conoscenze-utili/README.md) conservano ragioni, fatti e seguito fra sessioni e collaboratori.
- **Coordinare assistenti AI:** [metodo situato](skills/organizzare-lavoro-complesso/README.md), [avvio di un nodo](skills/avviare-nodo-ai/README.md) e [continuità del progetto](skills/continuita-del-lavoro-ai/README.md) aiutano a formare contributi complementari e a integrarli attraverso fonti e ragioni condivise.

## Primo uso

Scegli la risorsa e apri il suo **AVVIO_CHAT_IT.txt**. Copia tutto il testo o allegalo alla chat, poi aggiungi intento, progetto, fonti e strumenti disponibili. L’avvio include il metodo completo del kit. In un ambiente agentico puoi invece rendere leggibile l’intera cartella e indicare SKILL.md come ingresso.

Con un kernel esistente, integra la capacità nel sapere e nelle guide del progetto. Senza kernel, parti direttamente dal metodo fornito. I file non creano accessi agli account, memoria del modello o ricorrenze: la guida spiega come collegare la capacità ai mezzi realmente presenti.

## Edizioni e apprendimento

Le risorse sono prime edizioni pubbliche0.1.0. Istruzioni e guide sono in italiano; le presentazioni sul sito sono in italiano e inglese. Un assistente può leggere il metodo italiano e lavorare con te nella lingua scelta.

Il [catalogo](catalog.json) collega file e versioni; [dist/manifest.json](dist/manifest.json) registra pacchetti e impronte. La verifica di questi file riguarda la coerenza del kit. I casi sono illustrativi; l’efficacia nel tuo ambiente e l’uso delle correzioni si osservano nel lavoro reale.

Un riscontro può migliorare il metodo, la guida o il modo di raggiungere la competenza. Conserva la situazione, la differenza osservata e la ragione della modifica. Il [metodo di distribuzione](docs/DISTRIBUZIONE.md) accompagna questo ritorno e le proiezioni editoriali.

Origine e direzione: **Graziano Guiducci · MAIOS**. [maios.it](https://maios.it/) · [Contributi e riscontri](https://github.com/GrazianoGuiducci/maios-meta-skill/issues).

---

**English:** MAIOS Meta-Skill provides25 public resources for AI work, competence formation, continuity and semantic kernels. Each includes an operating method, a complete chat starter, a guide and examples. The operating kits are in Italian; [the website presents the collection in English](https://maios.it/resources/). Types identify different contributions, including operating competences, meta-level methods, KA as a foundation and FDLA as in-flow correction.
'''
    readme=readme.replace('pubbliche0.1.0','pubbliche 0.1.0').replace('provides25','provides 25')
    (ROOT/'README.md').write_text(readme,encoding='utf-8',newline='\n')
    print(json.dumps({'resources':len(ordered),'ids':[r['id'] for r in ordered]}))


if __name__=='__main__':
    main()
