"""A short web explanation must not replace the developed receiving method."""
import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('portable_renderer',ROOT/'tools/render_portable_editions.py')
renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(renderer)

class PortableRenderingTests(unittest.TestCase):
    def test_operative_depth_cases_and_attributed_metadata_survive_rendering(self):
        name='meta-skill-semantic-kernel'
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);folder=root/'skills'/name
            shutil.copytree(ROOT/'skills'/name,folder)
            source=json.loads((folder/'presentation.json').read_text(encoding='utf-8'))
            original=json.loads((folder/'EDITION.json').read_text(encoding='utf-8'))
            original['source_note']='Attributed local knowledge';(folder/'EDITION.json').write_text(json.dumps(original),encoding='utf-8')
            previous=renderer.ROOT
            try:renderer.ROOT=root;renderer.render(name)
            finally:renderer.ROOT=previous
            for lang,skill,starter,readme in [('en','SKILL.md','START_CHAT_EN.txt','README.md'),('it','SKILL_IT.md','AVVIO_CHAT_IT.txt','README_IT.md')]:
                body=(folder/skill).read_text(encoding='utf-8');complete=(folder/starter).read_text(encoding='utf-8')
                for section in source[lang]['operating_method']:self.assertIn(section['body'],body)
                for section in source[lang]['knowledge']+source[lang]['worked_examples']:self.assertIn(section['body'],complete)
                self.assertIn(str(len(source[lang]['worked_examples'])),(folder/readme).read_text(encoding='utf-8'))
            self.assertEqual(json.loads((folder/'EDITION.json').read_text(encoding='utf-8'))['source_note'],'Attributed local knowledge')

if __name__=='__main__':unittest.main()
