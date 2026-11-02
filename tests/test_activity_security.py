import copy
import json
from io import BytesIO
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_activities import package, render, target


class ActivitySecurityTests(unittest.TestCase):
    def test_package_resolves_reference_and_preserves_existing_edition(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            definition = json.loads((ROOT / 'activities/public-representation/activity.json').read_text(encoding='utf-8'))
            folder = root / definition['folder']
            folder.mkdir(parents=True)
            (folder / 'activity.json').write_text(json.dumps(definition), encoding='utf-8')
            catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
            (root / 'catalog.json').write_text(json.dumps(catalog), encoding='utf-8')
            for name in definition['competences']:
                support = root / 'skills' / name
                support.mkdir(parents=True)
                (support / 'SKILL.md').write_text('Synthetic fixture.', encoding='utf-8')
            for name in ('LICENSE', 'NOTICE'):
                (root / name).write_text('Synthetic fixture.', encoding='utf-8')
            render(root)
            def git(*args):
                return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.DEVNULL, text=True).strip()
            git('init')
            git('config', 'user.name', 'Isolated fixture')
            git('config', 'user.email', 'audit@example.invalid')
            git('config', 'core.hooksPath', str(root / 'no-hooks'))
            git('add', '.')
            git('commit', '-m', 'fixture')
            revision = git('rev-parse', 'HEAD')
            result = package('HEAD', root)[0]
            self.assertEqual(revision, result['source_revision'])
            archive_path = root / definition['package']
            original = archive_path.read_bytes()
            with ZipFile(BytesIO(original)) as archive:
                self.assertEqual(revision, json.loads(archive.read(definition['id'] + '-activity/DEPENDENCIES.json'))['source_revision'])
            manifest = (root / 'dist/activities-manifest.json').read_bytes()
            self.assertEqual(result, package(revision, root)[0])
            (root / 'NOTICE').write_text('Changed fixture.', encoding='utf-8')
            git('add', 'NOTICE')
            git('commit', '-m', 'changed fixture')
            with self.assertRaises(ValueError):
                package('HEAD', root)
            self.assertEqual(original, archive_path.read_bytes())
            self.assertEqual(manifest, (root / 'dist/activities-manifest.json').read_bytes())

    def test_malformed_metadata_is_rejected_before_any_generated_file(self):
        original = json.loads((ROOT / 'activities/public-representation/activity.json').read_text(encoding='utf-8'))
        changes = [('folder', '..'), ('folder', 'C:/outside'), ('package', '../outside.zip'),
                   ('package', 'dist/../../outside.zip'), ('id', '../unsafe'),
                   ('version', '<script>window.executed=true</script>'),
                   ('route', '/../outside/'), ('route', 'javascript:void(0)'),
                   ('route', '/resources/ai-activities/%2e%2e/')]
        for field, value in changes:
            with self.subTest(field=field, value=value), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.assertEqual(root.resolve().parent, Path(tempfile.gettempdir()).resolve())
                folder = root / original['folder']
                folder.mkdir(parents=True)
                (root / 'catalog.json').write_text('{"resources":[]}', encoding='utf-8')
                changed = copy.deepcopy(original)
                if field == 'route':
                    changed['en']['route'] = value
                else:
                    changed[field] = value
                (folder / 'activity.json').write_text(json.dumps(changed), encoding='utf-8')
                before = {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob('*') if path.is_file()}
                with self.assertRaises(ValueError):
                    render(root)
                self.assertEqual(before, {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob('*') if path.is_file()})

    def test_output_resolution_rejects_cross_platform_unsafe_names(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for path in ['../outside', '/absolute', 'C:/outside', 'C:relative', '\\server\\share',
                         'dist/../outside', 'dist/file.', 'dist/file ', 'dist/AUX.txt', 'dist/a:b.zip']:
                with self.subTest(path=path), self.assertRaises(ValueError):
                    target(root, path)

    def test_existing_symlink_cannot_redirect_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root, outside = base / 'root', base / 'outside'
            root.mkdir()
            outside.mkdir()
            try:
                (root / 'dist').symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest('Host does not permit symlink creation; native junction probe covers Windows separately')
            with self.assertRaises(ValueError):
                target(root, 'dist/package.zip')


if __name__ == '__main__':
    unittest.main()
