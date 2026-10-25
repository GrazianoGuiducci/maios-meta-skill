"""Render selected public kits from their authored bilingual presentation knowledge."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def render(entry):
    folder=ROOT/'skills'/entry
    resource=json.loads((folder/'catalog-entry.json').read_text(encoding='utf-8'))
    content=json.loads((folder/'presentation.json').read_text(encoding='utf-8'))
    for lang in ('en','it'):
        en=lang=='en';p=content[lang];f=resource['languages'][lang]
        def section(title, paragraphs):return '\n## '+title+'\n\n'+'\n\n'.join(paragraphs)+'\n'
        skill='---\nname: '+entry+'\ndescription: '+p['does']+' '+p['when']+'\n---\n\n# '+resource['name']+'\n\n'+p['does']+'\n\n'+'\n\n'.join(p['intro'])+'\n'
        context=p.get('reader_context')
        if context:
            skill+=section(context['title'],[context['situation'],context['point']])
        skill+='\n'.join(section(x['title'],[x['body']]) for x in p['method'])
        skill+=section('Continue through the actual project' if en else 'Continuare attraverso il progetto reale',p['learning'])
        skill+=section('Operating knowledge' if en else 'Sapere operativo',['Read OPERATING_GUIDE.md and EXAMPLES.md. With no file access, use the complete START_CHAT_EN.txt. The method composes with complementary project competences; actual tools, persistence and authorized effects belong to the receiving environment.' if en else 'Leggi GUIDA_OPERATIVA_IT.md ed ESEMPI_IT.md. Senza accesso ai file usa AVVIO_CHAT_IT.txt completo. Il metodo si compone con le competenze complementari del progetto; strumenti effettivi, persistenza ed effetti autorizzati appartengono al ricevente.'])
        guide='# '+resource['name']+(' — practical operating knowledge\n' if en else ' — sapere operativo pratico\n')
        guide+='\n'.join(section(x['title'],[x['body']]) for x in p['knowledge'])
        guide+=section(p['depth']['title'],p['depth']['paragraphs'])
        examples='# '+('Worked examples' if en else 'Esempi sviluppati')+'\n\n'+('Illustrative cases. Conditions, decisions and continuation are supplied to teach the method; these are not reports of customer results.' if en else 'Casi illustrativi. Condizioni, scelte e continuazione insegnano il metodo; non sono resoconti di risultati ottenuti presso clienti.')+'\n'
        examples+='\n'.join(section(x['title'],[x['body']]) for x in p['worked_examples'])
        readme='# '+resource['name']+'\n\n'+p['title']+'\n\n'+p['subtitle']+'\n\n'+p['does']+'\n\n'+p['when']+'\n'
        readme+=section('First use' if en else 'Primo uso',['Read '+Path(f['skill']).name+' and '+Path(f['operating_guide']).name+'. '+('Attach the whole START_CHAT_EN.txt in a chat and describe your actual assignment. The starter includes method, practical knowledge and the three worked examples.' if en else 'Allega in chat l’intero AVVIO_CHAT_IT.txt e descrivi il tuo incarico. L’avvio include metodo, sapere pratico e tre esempi sviluppati.')])
        readme+=section('Files and edition' if en else 'File ed edizione',[('Public edition ' if en else 'Edizione pubblica ')+resource['version']+'. '+('English is primary; Italian counterparts are included. Read INSTALL.md for project installation. The method is usable independently or with a kernel. The examples and the website exploration are illustrative.' if en else 'Inglese principale, con corrispondenti file italiani. Leggi INSTALL_IT.md per l’installazione nel progetto. Il metodo si usa autonomamente o con un kernel. Esempi ed esplorazione sul sito sono illustrativi.')])
        install='# '+('Install ' if en else 'Installare ')+resource['name']+'\n\n'+('Extract the complete ZIP and copy its ' if en else 'Estrai il pacchetto ZIP completo e copia la cartella ')+entry+(' folder into your project’s `.agents/skills/`. Preserve an existing copy and its learned knowledge instead of overwriting it. Open Codex in that project and invoke `$' if en else ' in `.agents/skills/` del progetto. Conserva una copia esistente e il suo apprendimento anziché sovrascriverla. Apri Codex nel progetto e richiama `$')+entry+('` with a real task. If discovery has not refreshed, start a new session. For another host use its native discovery or attach START_CHAT_EN.txt. Read the practical guide and examples alongside the skill.' if en else '` con un incarico reale. Se la discovery non è aggiornata, avvia una nuova sessione. In un altro host usa l’ingresso nativo o allega AVVIO_CHAT_IT.txt. Leggi guida pratica ed esempi insieme alla competenza.')+'\n'
        starter=skill.split('---\n',2)[2]+'\n\n'+guide+'\n\n'+examples+'\n\n'+('My assignment, sources, existing work, available means and requested result:\n' if en else 'Il mio incarico, le fonti, il lavoro esistente, i mezzi disponibili e il risultato richiesto:\n')
        for key,text in [('skill',skill),('operating_guide',guide),('examples',examples),('guide',readme),('installation',install),('starter',starter)]:
            (ROOT/f[key]).write_text(text,encoding='utf-8',newline='\n')
    (folder/'EDITION.json').write_text(json.dumps({'version':resource['version'],'state':'public_edition','source_competence':resource['source_title'],'languages':['en','it'],'independent_receiving_use':'unobserved'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('entries',nargs='+');args=parser.parse_args()
    for entry in args.entries:render(entry)
