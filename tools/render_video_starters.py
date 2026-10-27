"""Assemble standalone video starters from the complete current operating files."""
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'skills/semantic-timelapse-formation'


def render():
    for lang in ('it','en'):
        names=(['SKILL_IT.md','GUIDA_OPERATIVA_IT.md','ESEMPI_IT.md','VC30_KERNEL_OPERATIVO_IT.md','VC30_STUDIO_LAB_IT.md','MKCV_CINEMA_IT.md'] if lang=='it' else
               ['SKILL.md','OPERATING_GUIDE.md','EXAMPLES.md','VC30_OPERATIONAL_KERNEL.md','VC30_STUDIO_LAB_EN.md','MKCV_CINEMA_EN.md'])
        body='\n\n'.join((FOLDER/name).read_text(encoding='utf-8') for name in names)
        body=re.sub(r'\A---\n.*?\n---\n','',body,count=1,flags=re.S)
        title=('Esempio tecnico facoltativo: renderer da immagine esistente' if lang=='it' else 'Optional technical example: renderer from an existing image')
        body+='\n\n## '+title+'\n\n```python\n'+(FOLDER/'examples/render_from_reference.py').read_text(encoding='utf-8')+'\n```\n\n'
        recovery=FOLDER/('VIDEO_RIPRENDIBILE_IT.md' if lang=='it' else 'RECOVERABLE_VIDEO_EN.md')
        if recovery.exists():
            body+='\n\n'+recovery.read_text(encoding='utf-8')+'\n'
            body+='\n## '+('Sorgenti facoltative incluse per un ambiente con strumenti locali' if lang=='it' else 'Optional included sources for an environment with local tools')+'\n\n'
            body+=('Salva i file indicati con terminazioni LF e un solo LF finale. Il job seleziona il renderer originale con il suo SHA256. In una chat senza strumenti usa il metodo e conserva la continuazione del progetto.\n' if lang=='it' else 'Save the named files with LF endings and exactly one final LF. The job selects the original renderer by SHA256. In a chat without tools, use the method and preserve the project continuation.\n')
            for name in ['autostudio.py','mkcv_resumable.py','fixtures/orbital_scene.py','jobs/orbital_scene.json','verify_recovery.py']:
                text=(FOLDER/'examples/recoverable_video'/name).read_text(encoding='utf-8')
                body+='\n### examples/recoverable_video/'+name+'\n\n```'+('json' if name.endswith('.json') else 'python')+'\n'+text.rstrip('\n')+'\n```\n'
        body+=('Il mio incarico, le fonti, i mezzi disponibili e il risultato richiesto:\n' if lang=='it' else 'My assignment, sources, available means and requested result:\n')
        (FOLDER/('AVVIO_CHAT_IT.txt' if lang=='it' else 'START_CHAT_EN.txt')).write_text(body,encoding='utf-8',newline='\n')


if __name__=='__main__':render()
