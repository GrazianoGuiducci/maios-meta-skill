"""An activity kit must work offline and retain its committed dependency identity."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_activities import render, package


class ActivityDeliveryTests(unittest.TestCase):
    def test_complete_bilingual_kit_is_reproducible_and_ignores_uncommitted_work(self):
        definition = json.loads((ROOT / 'activities/public-representation/activity.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / definition['folder']
            folder.mkdir(parents=True)
            (folder / 'activity.json').write_text(json.dumps(definition), encoding='utf-8')
            resources = []
            for name in definition['competences']:
                skill = root / 'skills' / name
                skill.mkdir(parents=True)
                (skill / 'SKILL.md').write_text('Committed method ' + name, encoding='utf-8')
                (skill / 'README.md').write_text('Committed guide ' + name, encoding='utf-8')
                resources.append({'native_entry': name, 'version': '1.0.0', 'skill': 'skills/' + name + '/SKILL.md'})
            (root / 'catalog.json').write_text(json.dumps({'resources': resources}), encoding='utf-8')
            for filename in ('LICENSE', 'NOTICE'):
                (root / filename).write_text(filename, encoding='utf-8')
            render(root)
            self.assertEqual(json.loads((root / 'catalog.json').read_text())['resources'], resources)
            def git(*args):
                subprocess.run(['git', '-C', str(root), *args], capture_output=True, check=True)
            git('init')
            git('add', '.')
            git('-c', 'user.name=Activity delivery test', '-c', 'user.email=test@example.invalid', 'commit', '-m', 'fixture')
            first = package('HEAD', root)[0]
            original = (root / first['package']).read_bytes()
            (root / resources[0]['skill']).write_text('Unrelated concurrent edit', encoding='utf-8')
            (folder / 'START_CHAT_EN.txt').write_text('Incomplete working draft', encoding='utf-8')
            second = package('HEAD', root)[0]
            self.assertEqual(first['sha256'], second['sha256'])
            self.assertEqual(original, (root / second['package']).read_bytes())
            with ZipFile(root / first['package']) as archive:
                prefix = definition['id'] + '-activity/'
                for locale, starter in [('en', 'START_CHAT_EN.txt'), ('it', 'AVVIO_CHAT_IT.txt')]:
                    text = archive.read(prefix + starter).decode('utf-8')
                    for item in definition[locale]['method'] + definition[locale]['guide'] + definition[locale]['examples']:
                        self.assertIn(item['body'], text)
                for resource in resources:
                    self.assertTrue(archive.read(prefix + resource['skill']).startswith(b'Committed method'))
                for filename in ('LICENSE', 'NOTICE', 'DEPENDENCIES.json', 'CONTEXT_EN.md', 'CONTESTO_IT.md'):
                    self.assertIn(prefix + filename, archive.namelist())


if __name__ == '__main__':
    unittest.main()
