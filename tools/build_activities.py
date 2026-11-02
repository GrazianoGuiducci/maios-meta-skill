"""Render autonomous activity entries and reproducible kits with public competences."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def sections(items):
    return '\n\n'.join('## ' + x['title'] + '\n\n' + x['body'] for x in items)


def render(root=ROOT):
    catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    activities = []
    for path in sorted((root / 'activities').glob('*/activity.json')):
        value = json.loads(path.read_text(encoding='utf-8'))
        folder = root / value['folder']
        languages = {}
        for locale in ('en', 'it'):
            it = locale == 'it'
            text = value[locale]
            names = {'method': 'ATTIVITA.md' if it else 'ACTIVITY.md',
                     'guide': 'GUIDA_IT.md' if it else 'README.md',
                     'examples': 'ESEMPI_IT.md' if it else 'EXAMPLES.md',
                     'context': 'CONTESTO_IT.md' if it else 'CONTEXT_EN.md',
                     'starter': 'AVVIO_CHAT_IT.txt' if it else 'START_CHAT_EN.txt'}
            method = '# ' + text['title'] + '\n\n' + text['intro'] + '\n\n' + sections(text['method'])
            guide = '# ' + ('Usare e adattare l’attività' if it else 'Use and adapt the activity') + '\n\n' + sections(text['guide'])
            examples = '# ' + ('Esempi da adattare' if it else 'Examples to adapt') + '\n\n' + sections(text['examples'])
            context = '# ' + ('Il contesto del tuo progetto' if it else 'Your project context') + '\n\n' + '\n\n'.join(
                '## ' + row['label'] + '\n\n' + row['hint'] + '\n\n' + ('[Da completare]' if it else '[To complete]') for row in text['context'])
            prompt_intro = ('Usa il metodo seguente per il progetto che ti affido. Comprendi il contesto e le fonti correnti, poi svolgi il lavoro utile attraverso i mezzi e gli effetti affidati. Le sezioni qui incluse contengono il metodo completo: non presumere accessi o conoscenze private MAIOS. Se una relazione indispensabile manca, chiedi soltanto ciò che cambia il lavoro e prosegui con la parte indipendente. Se non ho selezionato una ricorrenza, inizia su richiesta.\n\n'
                            if it else 'Use the following method for the project I entrust to you. Understand the context and current sources, then perform useful work through the means and effects entrusted. The included sections contain the complete method: presume no access to private MAIOS knowledge. If an indispensable relation is missing, ask only for what changes the work and continue independent work. If I have not selected a recurrence, begin on request.\n\n')
            starter = prompt_intro + method + '\n\n' + guide + '\n\n' + examples + '\n\n' + context
            guide += '\n\n## ' + ('Provenienza e stato' if it else 'Origin and status') + '\n\n' + text['origin']
            guide += '\n\n' + ('[Metodo](ATTIVITA.md) · [Avvio completo](AVVIO_CHAT_IT.txt) · [Esempi](ESEMPI_IT.md) · [Contesto](CONTESTO_IT.md) · [English](README.md)' if it else '[Method](ACTIVITY.md) · [Complete starter](START_CHAT_EN.txt) · [Examples](EXAMPLES.md) · [Context](CONTEXT_EN.md) · [Italiano](GUIDA_IT.md)')
            for key, body in {'method': method, 'guide': guide, 'examples': examples, 'context': context, 'starter': starter}.items():
                (folder / names[key]).write_text(body.rstrip() + '\n', encoding='utf-8', newline='\n')
            languages[locale] = {key: value['folder'] + '/' + name for key, name in names.items()}
        activities.append({key: value[key] for key in ('id', 'name', 'version', 'kind', 'folder', 'package', 'competences', 'license', 'en', 'it')} | {'definition': path.relative_to(root).as_posix(), 'languages': languages})
    catalog['activities'] = activities
    (root / 'catalog.json').write_bytes(encoded(catalog))
    return activities


def package(source_ref, root=ROOT):
    def read(path):
        return subprocess.check_output(['git', '-C', str(root), 'show', source_ref + ':' + path])
    def tracked(folder):
        return subprocess.check_output(['git', '-C', str(root), 'ls-tree', '-r', '--name-only', source_ref, '--', folder], text=True).splitlines()
    catalog = json.loads(read('catalog.json'))
    skills = {row['native_entry']: row for row in catalog['resources']}
    packages = []
    for activity in catalog.get('activities', []):
        prefix = activity['id'] + '-activity/'
        members = {prefix + Path(path).relative_to(activity['folder']).as_posix(): path for path in tracked(activity['folder'])}
        dependencies = []
        for name in activity['competences']:
            row = skills[name]
            folder = str(Path(row['skill']).parent).replace('\\', '/')
            paths = tracked(folder)
            members.update({prefix + path: path for path in paths})
            dependencies.append({'native_entry': name, 'version': row['version'], 'folder': folder,
                                 'files': {path: hashlib.sha256(read(path)).hexdigest() for path in paths}})
        for filename in ('LICENSE', 'NOTICE'):
            members[prefix + filename] = filename
        payloads = {name: read(source) for name, source in sorted(members.items())}
        payloads[prefix + 'DEPENDENCIES.json'] = encoded({'source_revision': source_ref, 'competences': dependencies})
        destination = root / activity['package']
        destination.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(destination, 'w', compression=ZIP_DEFLATED) as archive:
            for name, content in sorted(payloads.items()):
                entry = ZipInfo(name, date_time=(2026, 11, 2, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                archive.writestr(entry, content)
        packages.append({'id': activity['id'], 'version': activity['version'], 'source_revision': source_ref,
                         'package': activity['package'], 'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
                         'competences': dependencies, 'files': {name: hashlib.sha256(content).hexdigest() for name, content in payloads.items()}})
    (root / 'dist/activities-manifest.json').write_bytes(encoded({'schema_version': 1, 'packages': packages}))
    return packages


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-ref', help='Package this committed source; otherwise render editable activity sources')
    args = parser.parse_args()
    result = package(args.source_ref) if args.source_ref else render()
    print(json.dumps([{'id': row['id'], 'version': row['version']} for row in result]))
