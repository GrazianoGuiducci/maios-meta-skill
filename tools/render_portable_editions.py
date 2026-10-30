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
        if not content[lang].get('operating_method'):
            raise ValueError('Developed operating_method required; page summary cards cannot replace the receiving method: '+entry+'/'+lang)
    for lang in ('en','it'):
        en=lang=='en';p=content[lang];f=resource['languages'][lang]
        def section(title, paragraphs):return '\n## '+title+'\n\n'+'\n\n'.join(paragraphs)+'\n'
        description=p.get('entry_description',p['does']+' '+p['when'])
        skill='---\nname: '+entry+'\ndescription: '+json.dumps(description,ensure_ascii=False)+'\nmetadata:\n  version: '+resource['version']+'\n  language: '+lang+'\n---\n\n# '+resource['name']+'\n\n'+p['does']+'\n\n'+'\n\n'.join(p.get('operating_intro',p['intro']))+'\n'
        context=p.get('reader_context')
        if context:
            skill+=section(context['title'],[context['situation'],context['point']])
        adaptation=p.get('adaptation')
        if adaptation:
            skill+=section(adaptation['title'],adaptation['paragraphs'])
        skill+='\n'.join(section(x['title'],[x['body']]) for x in p.get('operating_method',p['method']))
        skill+=section('Continue through the actual project' if en else 'Continuare attraverso il progetto reale',p['learning'])
        skill+=section('Operating knowledge' if en else 'Sapere operativo',['Read OPERATING_GUIDE.md and EXAMPLES.md. With no file access, use the complete START_CHAT_EN.txt. The method composes with complementary project competences; actual tools, persistence and authorized effects belong to the receiving environment.' if en else 'Leggi GUIDA_OPERATIVA_IT.md ed ESEMPI_IT.md. Senza accesso ai file usa AVVIO_CHAT_IT.txt completo. Il metodo si compone con le competenze complementari del progetto; strumenti effettivi, persistenza ed effetti autorizzati appartengono al ricevente.'])
        guide='# '+resource['name']+(' — practical operating knowledge\n' if en else ' — sapere operativo pratico\n')
        guide+='\n'.join(section(x['title'],[x['body']]) for x in p['knowledge'])
        guide+=section(p['depth']['title'],p['depth']['paragraphs'])
        examples='# '+('Worked examples' if en else 'Esempi sviluppati')+'\n\n'+('Illustrative cases. Conditions, decisions and continuation are supplied to teach the method; these are not reports of customer results.' if en else 'Casi illustrativi. Condizioni, scelte e continuazione insegnano il metodo; non sono resoconti di risultati ottenuti presso clienti.')+'\n'
        examples+='\n'.join(section(x['title'],[x['body']]) for x in p['worked_examples'])
        readme='# '+resource['name']+'\n\n'+p['title']+'\n\n'+p['subtitle']+'\n\n'+p['does']+'\n\n'+p['when']+'\n'
        if adaptation:
            readme+=section(adaptation['title'],adaptation['paragraphs'])
        count=str(len(p['worked_examples']))
        readme+=section('First use' if en else 'Primo uso',[('Read ' if en else 'Leggi ')+Path(f['skill']).name+(' and ' if en else ' e ')+Path(f['operating_guide']).name+'. '+('Attach the whole START_CHAT_EN.txt in a chat and describe your actual assignment. The starter includes method, practical knowledge and '+count+' worked examples.' if en else 'Allega in chat l’intero AVVIO_CHAT_IT.txt e descrivi il tuo incarico. L’avvio include metodo, sapere pratico e '+count+' esempi sviluppati.')])
        readme+=section('Files and edition' if en else 'File ed edizione',[('Public edition ' if en else 'Edizione pubblica ')+resource['version']+'. '+('English is primary; Italian counterparts are included. Read INSTALL.md for project installation. The method is usable independently or with a kernel. The examples and the website exploration are illustrative.' if en else 'Inglese principale, con corrispondenti file italiani. Leggi INSTALL_IT.md per l’installazione nel progetto. Il metodo si usa autonomamente o con un kernel. Esempi ed esplorazione sul sito sono illustrativi.')])
        install='# '+('Adopt ' if en else 'Adottare ')+resource['name']+'\n\n'+('In a conversation, attach the complete START_CHAT_EN.txt and supply your work, sources and available means. With file access, keep the complete folder in a project-owned location and make SKILL.md reachable through the host’s native entry. Preserve an existing method, local learning and ongoing work; compare function, responsible owner and method before integrating a revision. Read the practical guide and examples. Instructions do not create missing tools or persistence.\n\n## Example: a Codex project\n\nExtract the complete ZIP and copy its ' if en else 'In una conversazione, allega l’intero AVVIO_CHAT_IT.txt e porta lavoro, fonti e mezzi disponibili. Con accesso ai file, conserva la cartella completa in una sede del progetto e rendi SKILL_IT.md raggiungibile dall’ingresso nativo dell’ambiente. Preserva il metodo esistente, l’apprendimento locale e il lavoro in corso; confronta funzione, responsabile e metodo prima di integrare una revisione. Leggi guida pratica ed esempi. Le istruzioni non creano strumenti o persistenza mancanti.\n\n## Esempio: un progetto Codex\n\nEstrai il pacchetto ZIP completo e copia la cartella ')+entry+(' folder into your project’s `.agents/skills/`. Keep an existing copy instead of overwriting it. Open Codex in that project and invoke `$' if en else ' in `.agents/skills/` del progetto. Conserva una copia esistente anziché sovrascriverla. Apri Codex nel progetto e richiama `$')+entry+('` with a real task. If discovery has not refreshed, start a new session. Other hosts use their own discovery and project conventions.\n' if en else '` con un incarico reale. Se la discovery non è aggiornata, avvia una nuova sessione. Gli altri ambienti usano la propria discovery e le proprie convenzioni di progetto.\n')
        starter=skill.split('---\n',2)[2]+'\n\n'+guide+'\n\n'+examples
        if f.get('tool_guide'):
            starter+='\n\n'+(ROOT/f['tool_guide']).read_text(encoding='utf-8')
        if f.get('runtime_sources'):
            starter+='\n\n## '+('Included tool sources' if en else 'Sorgenti degli strumenti inclusi')+'\n'
            for source in f['runtime_sources']:
                path=Path(source);syntax='python' if path.suffix=='.py' else 'json' if path.suffix=='.json' else 'text'
                starter+='\n### '+path.relative_to(folder.relative_to(ROOT)).as_posix()+'\n\n```'+syntax+'\n'+(ROOT/path).read_text(encoding='utf-8').rstrip()+'\n```\n'
        starter+='\n\n'+('My assignment, sources, existing work, available means and requested result:\n' if en else 'Il mio incarico, le fonti, il lavoro esistente, i mezzi disponibili e il risultato richiesto:\n')
        for key,text in [('skill',skill),('operating_guide',guide),('examples',examples),('guide',readme),('installation',install),('starter',starter)]:
            (ROOT/f[key]).write_text(text,encoding='utf-8',newline='\n')
    edition=json.loads((folder/'EDITION.json').read_text(encoding='utf-8')) if (folder/'EDITION.json').exists() else {}
    edition.update(version=resource['version'],state='public_edition',languages=['en','it'],independent_receiving_use='unobserved')
    if resource.get('source_title') is not None:edition['source_competence']=resource['source_title']
    (folder/'EDITION.json').write_text(json.dumps(edition,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('entries',nargs='+');args=parser.parse_args()
    for entry in args.entries:render(entry)
