"""Render autonomous activity entries and reproducible kits with public competences."""
import argparse
import hashlib
from io import BytesIO
import json
import re
import subprocess
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
VERSION = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+(?:-[A-Za-z0-9.-]+)?(?:\+[A-Za-z0-9.-]+)?\Z')


def relative_path(value):
    if not isinstance(value, str) or not value or any(c in value for c in '\\:<>"|?*') or any(ord(c) < 32 for c in value):
        raise ValueError('Unsupported activity path')
    path = PurePosixPath(value)
    reserved = {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)), *(f'LPT{i}' for i in range(1, 10))}
    if path.is_absolute() or '/'.join(path.parts) != value or any(
            part in ('.', '..') or part.endswith((' ', '.')) or part.split('.')[0].upper() in reserved for part in path.parts):
        raise ValueError('Non-canonical activity path')
    return path


def target(root, value):
    relative_path(value)
    base = root.resolve()
    result = (base / value).resolve()
    if result == base or not result.is_relative_to(base):
        raise ValueError('Activity target leaves its selected root')
    return result


def validate_activity(value, root):
    if not isinstance(value.get('id'), str) or not IDENTIFIER.fullmatch(value['id']):
        raise ValueError('Unsupported activity identifier')
    if not isinstance(value.get('version'), str) or not VERSION.fullmatch(value['version']):
        raise ValueError('Unsupported activity version')
    if value.get('folder') != 'activities/' + value['id']:
        raise ValueError('Activity folder does not match its identity')
    target(root, value['folder'])
    package = relative_path(value['package'])
    if package.parent != PurePosixPath('dist') or package.suffix != '.zip':
        raise ValueError('Activity packages belong in dist/')
    target(root, value['package'])
    for locale in ('en', 'it'):
        text = value[locale]
        for key in ('route', 'category', 'title', 'description', 'intro', 'status', 'origin'):
            if not isinstance(text.get(key), str):
                raise ValueError('Missing activity text: ' + key)
        prefix = '/risorse/attivita-ai/' if locale == 'it' else '/resources/ai-activities/'
        route = text['route']
        if not route.startswith(prefix) or not route.endswith('/') or not IDENTIFIER.fullmatch(route[len(prefix):-1]):
            raise ValueError('Non-canonical activity route')
        for key, fields in [('method', ('title', 'body')), ('guide', ('title', 'body')),
                            ('examples', ('title', 'body')), ('context', ('label', 'hint'))]:
            if not isinstance(text.get(key), list) or not text[key] or any(
                    not isinstance(item, dict) or any(not isinstance(item.get(field), str) for field in fields) for item in text[key]):
                raise ValueError('Incomplete activity section: ' + key)
        for path in value.get('languages', {}).get(locale, {}).values():
            relative_path(path)
            if not path.startswith(value['folder'] + '/'):
                raise ValueError('Activity document leaves its source folder')
            target(root, path)


def validate_set(values, root):
    seen_ids, seen_packages = set(), set()
    for value in values:
        validate_activity(value, root)
        package = str(target(root, value['package'])).casefold()
        if value['id'] in seen_ids or package in seen_packages:
            raise ValueError('Activity identity or output collision')
        seen_ids.add(value['id'])
        seen_packages.add(package)


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def sections(items):
    return '\n\n'.join('## ' + x['title'] + '\n\n' + x['body'] for x in items)


def render(root=ROOT):
    catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    activities = []
    entries = [(path, json.loads(path.read_text(encoding='utf-8'))) for path in sorted((root / 'activities').glob('*/activity.json'))]
    validate_set([value for path, value in entries], root)
    for path, value in entries:
        if path.parent.resolve() != target(root, value['folder']):
            raise ValueError('Activity definition and declared folder differ')
        for filename in ('ACTIVITY.md', 'ATTIVITA.md', 'README.md', 'GUIDA_IT.md', 'EXAMPLES.md', 'ESEMPI_IT.md', 'CONTEXT_EN.md', 'CONTESTO_IT.md', 'START_CHAT_EN.txt', 'AVVIO_CHAT_IT.txt'):
            target(root, value['folder'] + '/' + filename)
    target(root, 'catalog.json')
    for path, value in entries:
        folder = target(root, value['folder'])
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
                target(root, value['folder'] + '/' + names[key]).write_text(body.rstrip() + '\n', encoding='utf-8', newline='\n')
            languages[locale] = {key: value['folder'] + '/' + name for key, name in names.items()}
        activities.append({key: value[key] for key in ('id', 'name', 'version', 'kind', 'folder', 'package', 'competences', 'license', 'en', 'it')} | {'definition': path.relative_to(root).as_posix(), 'languages': languages})
    catalog['activities'] = activities
    (root / 'catalog.json').write_bytes(encoded(catalog))
    return activities


def package(source_ref, root=ROOT):
    source_ref = subprocess.check_output(
        ['git', '-C', str(root), 'rev-parse', '--verify', '--end-of-options', source_ref + '^{commit}'],
        text=True).strip()
    def read(path):
        return subprocess.check_output(['git', '-C', str(root), 'show', source_ref + ':' + path])
    def tracked(folder):
        return subprocess.check_output(['git', '-C', str(root), 'ls-tree', '-r', '--name-only', source_ref, '--', folder], text=True).splitlines()
    catalog = json.loads(read('catalog.json'))
    validate_set(catalog.get('activities', []), root)
    target(root, 'dist/activities-manifest.json')
    skills = {row['native_entry']: row for row in catalog['resources']}
    packages, prepared = [], []
    for activity in catalog.get('activities', []):
        prefix = activity['id'] + '-activity/'
        members, folded = {}, set()
        def member(name, path):
            relative_path(name)
            if name.casefold() in folded:
                raise ValueError('Activity archive member collision')
            folded.add(name.casefold())
            members[name] = path
        for path in tracked(activity['folder']):
            member(prefix + Path(path).relative_to(activity['folder']).as_posix(), path)
        dependencies = []
        for name in activity['competences']:
            row = skills[name]
            folder = str(Path(row['skill']).parent).replace('\\', '/')
            relative_path(folder)
            if folder != 'skills/' + name or not IDENTIFIER.fullmatch(name):
                raise ValueError('Supporting competence folder does not match its identity')
            paths = tracked(folder)
            for path in paths:
                member(prefix + path, path)
            dependencies.append({'native_entry': name, 'version': row['version'], 'folder': folder,
                                 'files': {path: hashlib.sha256(read(path)).hexdigest() for path in paths}})
        for filename in ('LICENSE', 'NOTICE'):
            member(prefix + filename, filename)
        payloads = {name: read(source) for name, source in sorted(members.items())}
        for name in payloads:
            relative_path(name)
        payloads[prefix + 'DEPENDENCIES.json'] = encoded({'source_revision': source_ref, 'competences': dependencies})
        if (prefix + 'DEPENDENCIES.json').casefold() in folded:
            raise ValueError('Activity dependency record collision')
        buffer = BytesIO()
        with ZipFile(buffer, 'w', compression=ZIP_DEFLATED) as archive:
            for name, content in sorted(payloads.items()):
                entry = ZipInfo(name, date_time=(2026, 11, 2, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                archive.writestr(entry, content)
        content = buffer.getvalue()
        destination = target(root, activity['package'])
        if destination.exists() and destination.read_bytes() != content:
            raise ValueError('Activity package already exists with different bytes; select a new edition and package')
        prepared.append((activity, payloads, dependencies, content))
    for activity, payloads, dependencies, content in prepared:
        destination = target(root, activity['package'])
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        packages.append({'id': activity['id'], 'version': activity['version'], 'source_revision': source_ref,
                         'package': activity['package'], 'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
                         'competences': dependencies, 'files': {name: hashlib.sha256(content).hexdigest() for name, content in payloads.items()}})
    target(root, 'dist/activities-manifest.json').write_bytes(encoded({'schema_version': 1, 'packages': packages}))
    return packages


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-ref', help='Package this committed source; otherwise render editable activity sources')
    args = parser.parse_args()
    result = package(args.source_ref) if args.source_ref else render()
    print(json.dumps([{'id': row['id'], 'version': row['version']} for row in result]))
