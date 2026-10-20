import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile, ZipInfo

SPEC=importlib.util.spec_from_file_location('installer',Path(__file__).resolve().parents[1]/'tools/install_skills.py')
installer=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'source';self.root.mkdir();(self.root/'dist').mkdir()
        self.dest=Path(self.temp.name)/'project'/'.agents'/'skills'
        self.resources=[];self.packages=[]
        self.add_skill('example-skill','old-name')

    def add_skill(self,name,resource_id=None,members=None):
        resource_id=resource_id or name
        members=members or {name+'/SKILL.md':b'---\nname: '+name.encode()+b'\ndescription: Example task.\n---\n\nRead GUIDE.md and apply it.\n',name+'/GUIDE.md':b'Use the supplied source before choosing.'}
        stream=io.BytesIO()
        with ZipFile(stream,'w') as z:
            for key,value in members.items():z.writestr(key,value)
        data=stream.getvalue();path='dist/'+name+'.zip';(self.root/path).write_bytes(data)
        self.resources.append({'id':resource_id,'skill_name':name,'version':'0.3.2','package':path})
        self.packages.append({'id':resource_id,'version':'0.3.2','sha256':hashlib.sha256(data).hexdigest(),'files':{key:hashlib.sha256(value).hexdigest() for key,value in members.items()}})
        self.save()

    def save(self):
        (self.root/'catalog.json').write_text(json.dumps({'resources':self.resources}))
        (self.root/'dist/manifest.json').write_text(json.dumps({'packages':self.packages}))

    def test_alias_and_canonical_install_same_complete_folder(self):
        result=installer.install(self.root,self.dest,['old-name','example-skill'])
        self.assertEqual(len(result['skills']),1)
        self.assertTrue((self.dest/'example-skill/SKILL.md').is_file())
        self.assertTrue((self.dest/'example-skill/GUIDE.md').is_file())
        self.assertEqual(json.loads((self.dest/'example-skill/MAIOS_INSTALLATION.json').read_text())['version'],'0.3.2')

    def test_dry_run_validates_without_creating_destination(self):
        self.assertEqual(installer.install(self.root,self.dest,['example-skill'],dry_run=True)['status'],'planned')
        self.assertFalse(self.dest.exists())

    def test_existing_skill_is_preserved_and_entire_batch_stops(self):
        self.add_skill('second-skill');existing=self.dest/'second-skill';existing.mkdir(parents=True)
        (existing/'notes.txt').write_text('local learning')
        with self.assertRaises(FileExistsError):installer.install(self.root,self.dest,all_skills=True)
        self.assertFalse((self.dest/'example-skill').exists())
        self.assertEqual((existing/'notes.txt').read_text(),'local learning')

    def test_corrupt_second_archive_prevents_any_install(self):
        self.add_skill('second-skill');(self.root/'dist/second-skill.zip').write_bytes(b'changed')
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,all_skills=True)
        self.assertFalse(self.dest.exists())

    def test_traversal_member_is_rejected_before_writing(self):
        self.add_skill('unsafe-skill',members={'unsafe-skill/../escape.txt':b'x'})
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['unsafe-skill'])
        self.assertFalse(self.dest.exists())

    def test_windows_path_member_is_rejected(self):
        self.add_skill('unsafe-skill',members={'unsafe-skill/C:/escape.txt':b'x'})
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['unsafe-skill'])

    def test_case_insensitive_member_collision_is_rejected(self):
        self.add_skill('unsafe-skill',members={'unsafe-skill/SKILL.md':b'x','unsafe-skill/skill.md':b'y'})
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['unsafe-skill'])

    def test_wrong_metadata_name_is_rejected(self):
        self.add_skill('wrong-name',members={'wrong-name/SKILL.md':b'---\nname: other\ndescription: Example.\n---\nWork'})
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['wrong-name'])

    def test_manifest_file_digest_is_checked(self):
        self.packages[0]['files']['example-skill/GUIDE.md']='0'*64;self.save()
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['example-skill'])

    def test_unknown_selection_creates_nothing(self):
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['missing'])
        self.assertFalse(self.dest.exists())

    def test_version_mismatch_is_rejected(self):
        self.resources[0]['version']='9.9.9';self.save()
        with self.assertRaises(ValueError):installer.install(self.root,self.dest,['example-skill'])


if __name__=='__main__':unittest.main()
