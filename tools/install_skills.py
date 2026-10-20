"""Install selected MAIOS release kits into an explicitly chosen skill folder."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def plan_install(root, destination, selected=(), all_skills=False):
    root, destination = Path(root).resolve(), Path(destination).absolute()
    catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    resources = catalog['resources']
    lookup = {key: item for item in resources for key in (item['id'], item['skill_name'])}
    if all_skills:
        chosen = resources
    else:
        unknown = sorted(set(selected) - lookup.keys())
        if unknown:
            raise ValueError('Unknown skill: ' + ', '.join(unknown) + '. Use --list.')
        chosen = list({lookup[key]['skill_name']: lookup[key] for key in selected}.values())
    if not chosen:
        raise ValueError('Choose --skill NAME or --all.')
    manifest = json.loads((root / 'dist/manifest.json').read_text(encoding='utf-8'))
    packages = {p['id']: p for p in manifest['packages']}
    planned = []
    for item in chosen:
        name = item['skill_name']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            raise ValueError('Invalid skill name: ' + name)
        target = destination / name
        if target.exists() or target.is_symlink():
            raise FileExistsError('Destination exists; nothing was overwritten: ' + str(target))
        package_path = (root / item['package']).resolve()
        if not package_path.is_relative_to(root / 'dist'):
            raise ValueError('Package is outside dist: ' + item['package'])
        data = package_path.read_bytes()
        record = packages[item['id']]
        digest = hashlib.sha256(data).hexdigest()
        if digest != record['sha256'] or record['version'] != item['version']:
            raise ValueError('Package identity mismatch: ' + name)
        files = {}
        with ZipFile(io.BytesIO(data)) as archive:
            for entry in archive.infolist():
                path = PurePosixPath(entry.filename)
                if (entry.is_dir() or path.is_absolute() or '..' in path.parts
                        or '\\' in entry.filename or len(path.parts) < 2
                        or path.parts[0] != name or any(':' in part for part in path.parts)
                        or (entry.external_attr >> 16) & 0o170000 == 0o120000):
                    raise ValueError('Unsafe package member: ' + entry.filename)
                relative = Path(*path.parts[1:])
                # Case-insensitive duplicates can overwrite on Windows.
                key = relative.as_posix().casefold()
                if key in files:
                    raise ValueError('Duplicate package member: ' + entry.filename)
                content = archive.read(entry)
                if hashlib.sha256(content).hexdigest() != record['files'].get(entry.filename):
                    raise ValueError('File identity mismatch: ' + entry.filename)
                files[key] = (relative, content)
        if len(files) != len(record['files']) or 'skill.md' not in files:
            raise ValueError('Incomplete package: ' + name)
        skill = files['skill.md'][1].decode('utf-8')
        front = skill.split('---', 2)
        if len(front) != 3 or front[0].strip():
            raise ValueError('Invalid SKILL.md entry: ' + name)
        metadata_name = re.search(r'^name:\s*(.*?)\s*$', front[1], re.M)
        if not metadata_name or metadata_name.group(1).strip('\"\'') != name:
            raise ValueError('SKILL.md name mismatch: ' + name)
        planned.append({'id': item['id'], 'name': name, 'version': item['version'],
                        'package_sha256': digest, 'target': target, 'files': files})
    return planned


def install(root, destination, selected=(), all_skills=False, dry_run=False):
    # Validate every selected archive and collision before creating anything.
    planned = plan_install(root, destination, selected, all_skills)
    output = []
    for item in planned:
        target = item['target']
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.mkdir()  # Exclusive creation: a concurrent install also fails safely.
            for key, (relative, content) in item['files'].items():
                if key == 'skill.md':
                    continue
                path = target / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open('xb') as stream:
                    stream.write(content)
            receipt = {k: item[k] for k in ('id', 'name', 'version', 'package_sha256')}
            receipt['repository'] = 'https://github.com/GrazianoGuiducci/maios-meta-skill'
            (target / 'MAIOS_INSTALLATION.json').write_text(
                json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
            # Discovery sees an entry only after all supporting files are present.
            pending = target / '.SKILL.installing'
            pending.write_bytes(item['files']['skill.md'][1])
            pending.rename(target / 'SKILL.md')
        output.append({k: item[k] for k in ('id', 'name', 'version', 'package_sha256')}
                      | {'target': str(target), 'files': len(item['files'])})
    return {'status': 'planned' if dry_run else 'installed', 'skills': output}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='List canonical names and stable resource IDs')
    parser.add_argument('--skill', action='append', default=[], help='Canonical skill name or stable resource ID; repeatable')
    parser.add_argument('--all', action='store_true', help='Install the complete resource collection')
    parser.add_argument('--dest', type=Path, help='Explicit destination, such as a project .agents/skills directory')
    parser.add_argument('--dry-run', action='store_true', help='Validate and show the plan without writing')
    args = parser.parse_args()
    if args.list:
        catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
        print(json.dumps([{'name': r['skill_name'], 'resource_id': r['id'], 'version': r['version']}
                          for r in catalog['resources']], indent=2))
        return
    if args.dest is None or (args.all and args.skill):
        parser.error('Choose --skill NAME (repeatable) or --all, and supply --dest PATH.')
    try:
        print(json.dumps(install(ROOT, args.dest, args.skill, args.all, args.dry_run), indent=2))
    except (ValueError, OSError, KeyError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
