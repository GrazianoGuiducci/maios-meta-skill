#!/usr/bin/env python3
"""Resumable, receipt-backed video-chunk adapter for MKCV AutoStudio.

The caller supplies a pinned, trusted, deterministic renderer that accepts:
--start-frame N --end-frame M --fps F --width W --height H --output PATH
Each invocation must make an H264/no-audio MP4 of exactly M-N frames.
This module never invents scenes or selects unauthorized external effects.
"""
from __future__ import annotations
import json
import os
import shutil
import socket
import sys
import time
import uuid
from pathlib import Path
from typing import Any


def _atomic_json(dest:Path, data:dict) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp=dest.with_name(dest.name+'.new-'+uuid.uuid4().hex[:8])
    try:
        with tmp.open('w',encoding='utf-8') as f:
            json.dump(data,f,sort_keys=True,indent=2,ensure_ascii=False)
            f.write('\n');f.flush();os.fsync(f.fileno())
        os.replace(tmp,dest)
    finally:
        if tmp.exists(): tmp.unlink()


def _load_json(p:Path, a)->dict:
    try:
        data=json.loads(p.read_text(encoding='utf-8'))
        if not isinstance(data,dict):raise ValueError('not an object')
        return data
    except (OSError, ValueError, UnicodeError) as exc:
        raise a.MKCVError('checkpoint_invalid',f'Cannot trust {p.name}; preserve and review partial work: {exc}') from exc


def _pid_alive(pid:int)->bool:
    if type(pid) is not int or pid<1:return False
    if os.name == "nt":
        # Windows signal 0 is CTRL_C_EVENT, not a process-existence query.
        # Wait on a query-only handle; never send a signal to inspect a lock.
        import ctypes
        from ctypes import wintypes
        api = ctypes.WinDLL("kernel32", use_last_error=True)
        api.OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
        api.OpenProcess.restype = wintypes.HANDLE
        api.WaitForSingleObject.argtypes = (wintypes.HANDLE, wintypes.DWORD)
        api.WaitForSingleObject.restype = wintypes.DWORD
        api.CloseHandle.argtypes = (wintypes.HANDLE,)
        api.CloseHandle.restype = wintypes.BOOL
        handle = api.OpenProcess(0x00100000, False, pid)  # SYNCHRONIZE only
        if not handle:
            return ctypes.get_last_error() != 87  # absent PID; otherwise unknown
        try:
            status = api.WaitForSingleObject(handle, 0)
            return status != 0  # WAIT_OBJECT_0 means terminated; unknown stays live
        finally:
            api.CloseHandle(handle)
    try:os.kill(pid,0);return True
    except ProcessLookupError:return False
    except PermissionError:return True


def _lock_dir(lock:Path,a)->list[dict[str,Any]]:
    events=[]
    try:lock.mkdir()
    except FileExistsError:
        if lock.is_symlink() or not lock.is_dir():raise a.MKCVError('unsafe_path','Lock path is not a directory')
        state=_load_json(lock/'holder.json',a)
        if state.get('hostname')!=socket.gethostname():
            raise a.MKCVError('execution_in_progress_or_unknown_lock','Cross-host or unidentified lock; do not steal')
        pid=state.get('pid')
        if _pid_alive(pid):
            raise a.MKCVError('execution_in_progress_or_stale_lock',f'Existing active renderer process {pid}')
        # This lock was held by a process that no longer exists on the same host.
        archived=lock.with_name(lock.name+'.stale-'+uuid.uuid4().hex[:8])
        lock.rename(archived)
        events.append({'event':'stale_lock_reclaimed','old_pid':pid,'archive':archived.name})
        try:lock.mkdir()
        except FileExistsError as exc:raise a.MKCVError('execution_in_progress_or_stale_lock','Concurrent restart') from exc
    _atomic_json(lock/'holder.json',{'pid':os.getpid(),'hostname':socket.gethostname(),'started':time.time()})
    return events


def _verify_chunk(path:Path,first:int,end:int,w:int,h:int,fps:int,a)->dict:
    if not path.is_file() or path.is_symlink():raise a.MKCVError('missing_chunk',f'Chunk missing/unsafe: {path.name}')
    info=a.probe(path)
    if info['codec']!='h264' or info['audio'] or (info['width'],info['height'])!=(w,h) or info['frames']!=end-first:
        raise a.MKCVError('invalid_chunk',f'{path.name}: wrong codec/dims/audio/frame count: {info}')
    num,den=map(int,info['fps'].split('/'))
    if den<=0 or num!=fps*den:
        raise a.MKCVError('invalid_chunk',f'{path.name}: FPS {info["fps"]} != {fps}')
    a.decode_all(path)
    return {'sha256':a.hash_file(path),'bytes':path.stat().st_size,'frames':end-first,'fps':info['fps'],'codec':'h264'}


def _verified_reuse(dest:Path, plan:dict, a)->dict:
    rec=_load_json(dest/'EXECUTION.json',a)
    if rec.get('fingerprint')!=plan['fingerprint'] or rec.get('status')!='completed':
        raise a.MKCVError('output_conflict','Completed output belongs to another input, job or executor')
    records=rec.get('artifacts',{})
    if not isinstance(records,dict) or not records or 'film.mp4' not in records:
        raise a.MKCVError('output_conflict','Completed receipt lacks verifiable media')
    for raw,datum in records.items():
        p=dest/raw
        if p.is_symlink() or not p.is_file() or a.hash_file(p)!=datum.get('sha256'):
            raise a.MKCVError('output_conflict',f'Published local artifact missing/modified: {raw}')
    meta=a.probe(dest/'film.mp4')
    if meta.get('frames')!=plan['expected_frames'] or meta.get('codec')!='h264':
        raise a.MKCVError('output_conflict','Final video could not be verified')
    a.decode_all(dest/'film.mp4')
    return {'status':'reused_verified','directory':plan['output']['directory'],'receipt':rec}


def execute(job:dict,root:Path,plan:dict,a,*,max_chunks:int|None=None)->dict:
    """Execute/resume chunks synchronously. max_chunks allows *controlled* suspend for QA."""
    if plan['status']!='executable':return {'status':'needs_capability_or_input','plan':plan}
    if max_chunks is not None and (type(max_chunks) is not int or max_chunks<=0):
        raise a.MKCVError('invalid_job','max_chunks must be positive integer')
    dest=a.work_path(root,plan['output']['directory'],existing=False)
    if dest.is_symlink():raise a.MKCVError('unsafe_path','Final output is a symlink')
    if dest.exists():
        return _verified_reuse(dest,plan,a)
    partial=dest.parent/('.'+dest.name+'.partial')
    lock=dest.parent/('.'+dest.name+'.execution.lock')
    if partial.is_symlink():raise a.MKCVError('unsafe_path','Partial output is a symlink')
    dest.parent.mkdir(parents=True,exist_ok=True)
    startup_events=_lock_dir(lock,a)
    try:
        inputs=job['inputs'];fps=plan['output']['fps'];w=plan['output']['width'];h=plan['output']['height']
        count=plan['expected_frames'];chunk=inputs['chunk_frames'];segments=[(s,min(s+chunk,count)) for s in range(0,count,chunk)]
        if partial.exists():
            state=_load_json(partial/'STATE.json',a)
            if state.get('fingerprint')!=plan['fingerprint'] or state.get('version')!=a.VERSION:
                raise a.MKCVError('checkpoint_conflict','Partial job has different inputs/owner/executor. Preserve old and select new output directory.')
            if state.get('segments_expected')!=[[s,e] for s,e in segments]:
                raise a.MKCVError('checkpoint_conflict','Partial segment schedule changed')
            for event in startup_events:state['events'].append(event)
        else:
            partial.mkdir()
            (partial/'segments').mkdir()
            (partial/'quarantine').mkdir()
            shutil.copy2(a.work_path(root,inputs['renderer']),partial/'scene_renderer.py')
            (partial/'assets').mkdir()
            for i,path in enumerate(inputs.get('assets',[])):
                shutil.copy2(a.work_path(root,path),partial/'assets'/f'{i:02d}_{Path(path).name}')
            state={'schema':'mkcv-chunk-checkpoint/0.3','version':a.VERSION,'fingerprint':plan['fingerprint'],
                  'profile':'coded_scene','expected_frames':count,'fps':fps,'width':w,'height':h,
                  'segments_expected':[[s,e] for s,e in segments], 'completed':{}, 'events':startup_events,
                  'source_renderer_sha256':plan['inputs']['renderer']['sha256'],
                  'source_assets':plan['inputs']}
            _atomic_json(partial/'STATE.json',state)
        # Pins are still valid at point of resume, including when the job includes external inputs.
        if a.hash_file(partial/'scene_renderer.py')!=plan['inputs']['renderer']['sha256']:
            raise a.MKCVError('checkpoint_conflict','Staged renderer changed from pinned source')
        for i,path in enumerate(inputs.get('assets',[])):
            if a.hash_file(partial/'assets'/f'{i:02d}_{Path(path).name}')!=plan['inputs'][f'asset_{i}']['sha256']:
                raise a.MKCVError('checkpoint_conflict','Staged asset changed')
        done_this_call=0; reused=0;created=0; repaired=0
        for start,end in segments:
            key=f'{start:08d}_{end:08d}'
            name=f'part_{key}.mp4'
            movie=partial/'segments'/name
            current=state['completed'].get(key)
            valid=None
            if movie.exists():
                try:
                    valid=_verify_chunk(movie,start,end,w,h,fps,a)
                    if current and (valid['sha256']!=current.get('sha256') or valid['bytes']!=current.get('bytes')):
                        raise a.MKCVError('invalid_chunk','Recorded chunk digest differs')
                except (a.MKCVError,ValueError,KeyError,RuntimeError) as exc:
                    reason=str(exc)[:250]
                    q=partial/'quarantine'/(name+'.damaged-'+uuid.uuid4().hex[:8])
                    movie.rename(q)
                    state['events'].append({'event':'invalid_chunk_quarantined','segment':key,'reason':reason,'quarantine':q.name})
                    repaired+=1;valid=None
                    state['completed'].pop(key,None)
                    current=None  # It was quarantined, not an independent missing chunk.
                    _atomic_json(partial/'STATE.json',state)
            if valid:
                if not current:
                    # Crash after encode, before checkpoint write. Adopt only after full decode.
                    state['events'].append({'event':'orphan_chunk_verified_and_adopted','segment':key})
                    state['completed'][key]=valid
                    _atomic_json(partial/'STATE.json',state)
                reused+=1
                continue
            if current and not movie.exists():
                state['events'].append({'event':'missing_chunk_regenerated','segment':key})
                repaired+=1
                state['completed'].pop(key,None)
                _atomic_json(partial/'STATE.json',state)
            # Trusted time-addressable renderer executes only the local selected effect.
            cmd=[sys.executable,str(partial/'scene_renderer.py'),'--start-frame',str(start),'--end-frame',str(end),
                 '--fps',str(fps),'--width',str(w),'--height',str(h),'--output',str(movie),
                 '--asset-root',str(partial/'assets')]
            try:
                executed=a.exec_process(cmd,timeout=180,cwd=partial)
                (partial/'segments'/f'{key}.log').write_bytes(executed.stdout[-10000:]+b'\nSTDERR:\n'+executed.stderr[-10000:])
                record=_verify_chunk(movie,start,end,w,h,fps,a)
            except BaseException as exc:
                state['events'].append({'event':'segment_failed','segment':key,'reason':str(exc)[:250]})
                _atomic_json(partial/'STATE.json',state)
                raise
            state['completed'][key]=record
            state['events'].append({'event':'rendered_and_decoded','segment':key,'sha256':record['sha256']})
            _atomic_json(partial/'STATE.json',state)
            created+=1;done_this_call+=1
            if max_chunks is not None and done_this_call>=max_chunks and len(state['completed'])<len(segments):
                return {'status':'partial','directory':plan['output']['directory'],
                        'checkpoint':partial.name,'verified_segments':len(state['completed']),
                        'total_segments':len(segments),'rendered_this_call':created,'reused_this_call':reused,
                        'next':'Run the SAME pinned job again to resume verified segments; no background job is running'}
        if len(state['completed'])!=len(segments):
            raise a.MKCVError('checkpoint_invalid','Not all expected segments verified')
        concat=partial/'concat.txt'
        concat.write_text(''.join(f"file 'segments/part_{s:08d}_{e:08d}.mp4'\n" for s,e in segments),encoding='utf-8')
        video=partial/'video_only.mp4'
        # Segment H264 encoders restart prediction at every boundary. Decode and
        # re-encode a single final timeline to reduce GOP seam artifacts.
        a.exec_process(['ffmpeg','-hide_banner','-nostdin','-v','error','-y','-f','concat','-safe','0',
                        '-i',str(concat),'-an','-c:v','libx264','-preset','veryfast','-crf','21',
                        '-r',str(fps),'-fps_mode','cfr','-frames:v',str(count),
                        '-threads','1','-pix_fmt','yuv420p','-movflags','+faststart',str(video)],timeout=160)
        final=partial/'film.mp4'
        if inputs.get('audio'):
            a.mux_music(video,a.work_path(root,inputs['audio']),final,count/fps)
        else:shutil.copy2(video,final)
        meta=a.probe(final)
        if meta['frames']!=count or (meta['width'],meta['height'])!=(w,h):
            raise a.MKCVError('bad_artifact',f'Concatenated video mismatch: {meta}')
        num,den=map(int,meta['fps'].split('/'))
        if den<1 or num!=fps*den:raise a.MKCVError('bad_artifact',f'Concatenated video FPS mismatch: {meta["fps"]}')
        a.decode_all(final,timeout=180)
        a.contact_sheet(final,partial/'contact_sheet.jpg')
        (partial/'segment_manifest.json').write_text(json.dumps({'fingerprint':plan['fingerprint'],
            'segments':[{'start':s,'end':e,'name':f'part_{s:08d}_{e:08d}.mp4',
                         **state['completed'][f'{s:08d}_{e:08d}']} for s,e in segments],
            'events':state['events']},ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
        video.unlink();concat.unlink()
        artifacts={str(p.relative_to(partial)):{'sha256':a.hash_file(p),'bytes':p.stat().st_size}
                   for p in sorted(partial.rglob('*')) if p.is_file() and not p.is_symlink()
                   and not p.name.startswith('STATE.json') and p.name!='EXECUTION.json'}
        receipt={'schema':'mkcv-execution-receipt/0.3','version':a.VERSION,'status':'completed',
                 'profile':'coded_scene','job_id':job.get('id'),'fingerprint':plan['fingerprint'],
                 'inputs':plan['inputs'],'executor_sources':plan.get('executor_sources'),'result':{'video':meta,'expected_frames':count,'decoded_without_errors':True,
                    'claim':'time_addressed_code_video_not_narrative_quality_or_semantic_fidelity_certification',
                    'final_encoding':'single_continuous_h264_reencode_from_decoded_verified_chunks',
                    'chunk_reused_this_call':reused,'chunks_rendered_this_call':created,
                    'chunks_repaired_this_call':repaired,'total_chunks':len(segments)},
                 'artifacts':artifacts,'limits':'No background processing, provider effects, publication or spending'}
        _atomic_json(partial/'EXECUTION.json',receipt)
        # Atomic public promotion occurs only after the entire output is verified.
        partial.rename(dest)
        return {'status':'completed','directory':plan['output']['directory'],'receipt':receipt}
    finally:
        if lock.is_dir() and not lock.is_symlink():shutil.rmtree(lock)
