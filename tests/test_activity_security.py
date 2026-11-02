import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_activities import render, target


class ActivitySecurityTests(unittest.TestCase):
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
