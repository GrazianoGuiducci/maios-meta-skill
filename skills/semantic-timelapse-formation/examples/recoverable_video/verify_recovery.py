"""Exercise a local recovery contract in a new, explicitly selected directory."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys

sys.dont_write_bytecode=True

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True,help='New directory; existing work is never overwritten')
    args=parser.parse_args();root=args.output.resolve();root.mkdir(parents=True,exist_ok=False)
    source=Path(__file__).resolve().parent
    (root/'fixtures').mkdir();(root/'jobs').mkdir()
    for name in ['autostudio.py','mkcv_resumable.py','fixtures/orbital_scene.py']:
        shutil.copyfile(source/name,root/name)
    spec=importlib.util.spec_from_file_location('recovery_adapter',root/'mkcv_resumable.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    child=subprocess.Popen([sys.executable,'-c','import time;time.sleep(30)'])
    try:
        assert module._pid_alive(child.pid) and child.poll() is None
        child.kill();child.wait();assert not module._pid_alive(child.pid)
    finally:
        if child.poll() is None:child.kill();child.wait()
    original=json.loads((source/'jobs/orbital_scene.json').read_text(encoding='utf-8'))
    path=root/'jobs/orbital_scene.json'
    def run(job,label,partial=False,expected=0):
        path.write_text(json.dumps(job,ensure_ascii=False)+'\n',encoding='utf-8')
        command=[sys.executable,str(root/'autostudio.py'),'run',str(path),'--workspace',str(root)]
        if partial:command+=['--max-chunks','1']
        result=subprocess.run(command,capture_output=True,timeout=180)
        (root/(label+'.stdout.json')).write_bytes(result.stdout)
        (root/(label+'.stderr.txt')).write_bytes(result.stderr)
        if result.returncode!=expected:
            raise RuntimeError(label+': '+result.stderr.decode('utf-8','replace'))
        return json.loads(result.stdout or result.stderr)
    first=run(original,'pause',partial=True,expected=4);assert first['status']=='partial'
    changed=dict(original);changed['inputs']=dict(original['inputs'],frames=84)
    assert run(changed,'changed-job',expected=2)['status']=='checkpoint_conflict'
    final=run(original,'resume');assert final['receipt']['result']['chunk_reused_this_call']==1
    assert run(original,'reuse')['status']=='reused_verified'
    clean=dict(original);clean['id']='continuous';clean['output']=dict(original['output'],directory='runs/continuous')
    run(clean,'continuous')
    video=root/original['output']['directory']/'film.mp4'
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(video)==digest(root/'runs/continuous/film.mp4')
    proof={'state':'passed','scope':'local process liveness, controlled pause/resume, changed-job refusal, completed reuse and exact video comparison','platform':sys.platform,'video_sha256':digest(video),'video':str(video)}
    (root/'VERIFICATION.json').write_text(json.dumps(proof,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(proof))

if __name__=='__main__':main()
