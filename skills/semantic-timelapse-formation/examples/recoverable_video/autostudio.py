#!/usr/bin/env python3
"""MKCV AutoStudio 0.3 — bounded local video executor.

An AI's decision about story, direction and meaning belongs to the owner-native
competences; this script only performs exact selected, authorized local effects.
Standard library + Pillow, NumPy, OpenCV and local ffmpeg/ffprobe for supported profiles.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

VERSION = "0.3.2"
PROFILES = {
  "coded_scene": {"mode": "executable_with_trusted_time_renderer", "owners": ["Cinematic Direction", "Character Performance", "Film Montage", "Code Medium"], "scope": "deterministic frame-addressable authored scene, verified segments and interruption recovery; not autonomous story generation"},
  "animatic": {"mode": "executable", "owners": ["Editoriali", "Storyboard", "Film Montage", "Code Medium"], "scope": "timed stills and editorial camera motion; not character animation"},
  "edit_existing": {"mode": "executable", "owners": ["Film Montage", "Sound", "Code Medium"], "scope": "re-encoded normalized clip montage; optional external music; no default source-audio reuse"},
  "reference_3d": {"mode": "executable_with_trusted_renderer", "owners": ["Cinematic Direction", "Character Performance", "Code Medium"], "scope": "execute an already-authored trusted local renderer and compare its frame with a reference; no automatic 3D reconstruction"},
  "image_motion": {"mode": "needs_assets_or_adapter", "owners": ["Character Performance", "Code Medium"], "scope": "requires subject layers, masks and reconstructed background"},
  "procedural_3d_film": {"mode": "needs_scene_renderer", "owners": ["Cinematic Direction", "Character Performance", "Code Medium"], "scope": "requires an authored time-addressable 3D scene"},
  "motion_graphics": {"mode": "needs_graphics_adapter", "owners": ["Editoriali", "Perceptual Composition", "Code Medium"], "scope": "requires data semantics and a renderer"},
  "live_capture": {"mode": "needs_capture_receiver", "owners": ["Product Owner", "Direction", "Code Medium"], "scope": "requires true screen/software capture"},
  "generative_video": {"mode": "needs_provider", "owners": ["Storyboard", "Direction", "Provider"], "scope": "requires connected provider, explicit cost/rights and actual invocation"},
  "interactive_film": {"mode": "needs_interactive_runtime", "owners": ["UX-AI", "Design", "Code Medium"], "scope": "MP4 is not interactive software"},
}
EXECUTABLE = {"animatic","edit_existing","reference_3d","coded_scene"}
PROFILE_GAPS={
 "image_motion": "Clean background, subject mask or rig plus an image-motion adapter not supplied",
 "procedural_3d_film": "Authored time-addressable scene renderer must be installed in a compatible receiver",
 "motion_graphics": "Domain data and code motion-graphics renderer required",
 "live_capture": "Real application/screen capture controller is not connected to this process",
 "generative_video": "Video-generation provider not connected; rights, credits and authority unresolved",
 "interactive_film": "Requires real interactive runtime, not an MP4 renderer"
}
class MKCVError(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code=code


def hash_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def exec_process(cmd:list[str], timeout:int=120, *, cwd:Path|None=None, input_bytes:bytes|None=None) -> subprocess.CompletedProcess:
    try:
        p=subprocess.run(cmd, input=input_bytes, capture_output=True, cwd=cwd, timeout=timeout)
    except FileNotFoundError as exc:
        raise MKCVError("needs_capability_or_input", f"Executable missing: {cmd[0]}") from exc
    except subprocess.TimeoutExpired as exc:
        raise MKCVError("execution_timed_out", f"Process exceeded {timeout}s: {cmd[0]}") from exc
    if p.returncode:
        raise MKCVError("execution_failed", f"{cmd[0]} returned {p.returncode}: {p.stderr.decode('utf-8','replace')[-1500:]}")
    return p


def probe(path:Path) -> dict[str,Any]:
    data=json.loads(exec_process(["ffprobe","-v","error","-count_frames","-show_format","-show_streams","-of","json",str(path)],timeout=120).stdout)
    video=next((s for s in data.get("streams",[]) if s.get("codec_type")=="video"),None)
    if not video: raise MKCVError("bad_artifact", f"No video stream: {path.name}")
    frames=video.get("nb_read_frames") or video.get("nb_frames")
    fps=video.get("avg_frame_rate") or "0/1"
    return {"codec":video.get("codec_name"),"width":video.get("width"),"height":video.get("height"),
     "fps":fps,"frames":int(frames) if frames and frames!='N/A' else None,
     "duration":float(data.get("format",{}).get("duration") or 0),
     "audio":any(s.get("codec_type")=="audio" for s in data.get("streams",[])),
     "audio_codec":next((s.get("codec_name") for s in data.get("streams",[]) if s.get("codec_type")=="audio"),None)}


def decode_all(path:Path, timeout:int=140) -> None:
    exec_process(["ffmpeg","-hide_banner","-nostdin","-v","error","-xerror","-i",str(path),"-f","null","-"],timeout=timeout)


def is_inside(path:Path,root:Path)->bool:
    return path==root or root in path.parents


def work_path(root:Path, raw:str, *, existing:bool=True) -> Path:
    if not isinstance(raw,str) or not raw.strip(): raise MKCVError("invalid_job","Expected relative nonblank path")
    if Path(raw).is_absolute(): raise MKCVError("unsafe_path",f"Absolute path not allowed in job: {raw}")
    p=(root/raw).resolve()
    if not is_inside(p,root): raise MKCVError("unsafe_path", f"Path escapes job workspace: {raw}")
    if existing and (not p.is_file() or p.is_symlink()):
        raise MKCVError("needs_capability_or_input", f"Missing regular input file: {raw}")
    return p


def require_int(value:Any,lo:int,hi:int,name:str)->int:
    if type(value) is not int or not lo<=value<=hi:
        raise MKCVError("invalid_job",f"{name} must be integer in [{lo},{hi}]")
    return value


def select_profile(job:dict)->tuple[str|None,str|None]:
    requested=job.get("profile")
    if requested:
        if requested not in PROFILES: return None,"Unrecognized profile; cannot assume a video medium"
        return requested,None
    inputs=job.get("inputs",{})
    matches=[]
    if isinstance(inputs,dict):
        if inputs.get("images"):matches.append("animatic")
        if inputs.get("clips"):matches.append("edit_existing")
        if inputs.get("renderer") and inputs.get("reference"):matches.append("reference_3d")
    if len(matches)==1:return matches[0],None
    return None,"Material or intent is insufficient or ambiguous; select a medium from capabilities"


def load(job_path:Path,workspace:Path|None) -> tuple[dict,Path,Path]:
    job_path=job_path.resolve(strict=True)
    root=(workspace or (job_path.parent.parent if job_path.parent.name=='jobs' else job_path.parent)).resolve(strict=True)
    if not is_inside(job_path,root): raise MKCVError("unsafe_path", "Job file outside workspace")
    try: job=json.loads(job_path.read_text(encoding="utf-8"))
    except Exception as exc: raise MKCVError("invalid_job", f"Cannot parse job: {exc}") from exc
    if not isinstance(job,dict): raise MKCVError("invalid_job", "Job must be a JSON object")
    if job.get("id") and (not isinstance(job["id"],str) or not re.fullmatch(r"[\w-]{1,80}",job["id"], re.ASCII)):
        raise MKCVError("invalid_job","Job ID must use [A-Za-z0-9_-], max 80")
    if not isinstance(job.get("intent"),str) or not job["intent"].strip():
        raise MKCVError("invalid_job","intent is required as substantive text")
    return job,root,job_path


def plan_job(job:dict,root:Path)->dict:
    gaps=[]; warnings=[]
    profile,ambiguity=select_profile(job)
    if ambiguity: gaps.append(ambiguity)
    authority=job.get("authority",{})
    if not isinstance(authority,dict): raise MKCVError("invalid_job","authority must be object")
    for eff in ("publish","spend","send","deploy"):
        if authority.get(eff): gaps.append(f"{eff} is an external effect: not authorized by the local video executor")
    inputs=job.get("inputs",{})
    if not isinstance(inputs,dict):raise MKCVError("invalid_job","inputs must be object")
    out=job.get("output",{})
    if not isinstance(out,dict):raise MKCVError("invalid_job","output must be object")
    width=require_int(out.get("width",640),160,1920,"output.width")
    height=require_int(out.get("height",360),90,1080,"output.height")
    if width%2 or height%2:raise MKCVError("invalid_job","width and height must be even (H.264 yuv420p)")
    fps=require_int(out.get("fps",24),1,60,"output.fps")
    max_frames=require_int(job.get("limits",{}).get("max_frames",1800),1,12000,"limits.max_frames")
    dest=work_path(root,out.get("directory",f"runs/{job.get('id','job')}/"),existing=False)
    asset_map={}; expected=0
    def asset(label,path):
        p=work_path(root,path)
        if not p.exists(): gaps.append(f"Missing {label}: {path}")
        else:asset_map[label]={"path":str(p.relative_to(root)),"sha256":hash_file(p),"bytes":p.stat().st_size}
        return p
    if profile in PROFILE_GAPS:gaps.append(PROFILE_GAPS[profile])
    if profile in EXECUTABLE:
        import importlib.util
        for cmd in ("ffmpeg","ffprobe"):
            if not shutil.which(cmd):gaps.append(f"Executable missing on this receiver: {cmd}")
        for module in ("PIL","numpy","cv2"):
            if importlib.util.find_spec(module) is None:gaps.append(f"Python dependency missing: {module}")
    if profile=="coded_scene":
        expected=require_int(inputs.get("frames"),1,12000,"inputs.frames")
        chunk_frames=require_int(inputs.get("chunk_frames",48),1,500,"inputs.chunk_frames")
        if chunk_frames>max_frames: gaps.append("chunk_frames exceeds max_frames")
        if not inputs.get("renderer"):gaps.append("coded_scene needs a trusted time-addressed renderer")
        else:
            try:asset("renderer",inputs["renderer"])
            except MKCVError as e:gaps.append(str(e))
        if authority.get("execute_trusted_renderer") is not True:
            gaps.append("authority.execute_trusted_renderer=true required for authored Python scene")
        sha=inputs.get("renderer_sha256")
        if not isinstance(sha,str) or not re.fullmatch("[a-f0-9]{64}",sha):
            gaps.append("coded_scene requires pinned renderer_sha256")
        elif "renderer" in asset_map and asset_map["renderer"]["sha256"]!=sha:
            gaps.append("Pinned renderer SHA256 differs from local file")
        assets=inputs.get("assets",[])
        if not isinstance(assets,list):raise MKCVError("invalid_job","assets must be a list")
        for i,v in enumerate(assets):
            if not isinstance(v,str):raise MKCVError("invalid_job","assets entries must be paths")
            try:asset(f"asset_{i}",v)
            except MKCVError as e:gaps.append(str(e))
        if inputs.get("audio"):
            try:asset("music",inputs["audio"])
            except MKCVError as e:gaps.append(str(e))
    if profile=="reference_3d":
        for n in ("reference","renderer","regions","camera"):
            if not inputs.get(n):gaps.append(f"Missing {n} for reference_3d")
            else:
                try:asset(n,inputs[n])
                except MKCVError as e:gaps.append(str(e))
        if authority.get("execute_trusted_renderer") is not True:gaps.append("authority.execute_trusted_renderer=true required for Python execution")
        if not re.fullmatch(r"[\w-]+\.png", inputs.get("render_name","reconstruction_R2.png"),re.ASCII):
            raise MKCVError("invalid_job","render_name must be a flat PNG filename")
        if not inputs.get("renderer_sha256"):
            gaps.append("Explicit renderer_sha256 pin required to execute trusted code")
        elif "renderer" in asset_map and inputs["renderer_sha256"]!=asset_map["renderer"]["sha256"]:
            gaps.append("Trusted renderer hash changed — explicit authority update needed")
    elif profile=="animatic":
        ims=inputs.get("images",[])
        if not isinstance(ims,list) or not ims:gaps.append("animatic needs images[]")
        for i,im in enumerate(ims if isinstance(ims,list) else []):
            if not isinstance(im,dict):raise MKCVError("invalid_job",f"images[{i}] must be an object")
            frames=require_int(im.get("frames",48),1,1800,f"images[{i}].frames")
            expected+=frames
            try:asset(f"image_{i}",im["path"])
            except (KeyError,MKCVError) as e:gaps.append(f"images[{i}]: {e}")
        if inputs.get("audio"):
            try:asset("music",inputs["audio"])
            except MKCVError as e:gaps.append(str(e))
    elif profile=="edit_existing":
        clips=inputs.get("clips",[])
        if not isinstance(clips,list) or not clips:gaps.append("edit_existing needs clips[]")
        for i,clip in enumerate(clips if isinstance(clips,list) else []):
            if not isinstance(clip,dict):raise MKCVError("invalid_job",f"clips[{i}] must be an object")
            expected+=require_int(clip.get("frames",48),1,1800,f"clips[{i}].frames")
            require_int(clip.get("start_frame",0),0,10000000,f"clips[{i}].start_frame")
            try:
                path=asset(f"clip_{i}",clip["path"])
                if path.exists():
                    p=probe(path)
                    if p["frames"] and clip.get("start_frame",0)+clip.get("frames",48)>p["frames"]:
                        gaps.append(f"clips[{i}]: selection exceeds original video frames")
            except (KeyError,MKCVError) as e:gaps.append(f"clips[{i}]: {e}")
        if inputs.get("audio"):
            try:asset("music",inputs["audio"])
            except MKCVError as e:gaps.append(str(e))
        else:warnings.append("Source clip audio is not copied by this adapter; output is silent unless music input is supplied")
    if expected>max_frames:gaps.append(f"Expected {expected} frames exceeds max_frames={max_frames}")
    executor_files=[Path(__file__).resolve()]
    if profile=="coded_scene":executor_files.append(Path(__file__).resolve().with_name("mkcv_resumable.py"))
    executor_sources={x.name:hash_file(x) for x in executor_files}
    job_signature={"job":job,"inputs":asset_map,"executor":VERSION,"executor_sources":executor_sources,"profile":profile}
    fingerprint=hashlib.sha256(json.dumps(job_signature,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {"status":"executable" if profile in EXECUTABLE and not gaps else "needs_capability_or_input",
       "profile":profile,"intent":job["intent"],"owners":PROFILES.get(profile,{}).get("owners",[]),
       "profile_note":PROFILES.get(profile,{}).get("scope"),"gaps":gaps,"warnings":warnings,
       "fingerprint":fingerprint,"executor_sources":executor_sources,"inputs":asset_map,"expected_frames":expected or None,
       "output":{"directory":str(dest.relative_to(root)),"width":width,"height":height,"fps":fps}}


def crop_to_frame(img, width, height, progress:float, scale_from:float, scale_to:float, focus_x:float=.5, focus_y:float=.5):
    from PIL import Image
    import numpy as np
    s=scale_from+(scale_to-scale_from)*progress
    base=max(width/img.width,height/img.height)
    nw=max(width,int(round(img.width*base*s)));nh=max(height,int(round(img.height*base*s)))
    im=img.resize((nw,nh),Image.Resampling.LANCZOS)
    # Ease pan tied to progress, not to frame-count-dependent hidden state.
    ox=int((nw-width)*focus_x);oy=int((nh-height)*focus_y)
    ox=min(nw-width,max(0,ox));oy=min(nh-height,max(0,oy))
    return im.crop((ox,oy,ox+width,oy+height))


def write_rgb_frames(frames, output:Path,width:int,height:int,fps:int, count:int) -> None:
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-nostdin","-y","-f","rawvideo","-vcodec","rawvideo","-pix_fmt","rgb24",
          "-s",f"{width}x{height}","-r",str(fps),"-i","pipe:0","-an","-c:v","libx264","-preset","veryfast","-crf","21",
          "-pix_fmt","yuv420p","-threads","1","-movflags","+faststart",str(output)]
    import subprocess
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    seen=0
    try:
        for im in frames:
            if im.size!=(width,height):raise MKCVError("bad_frame",f"Expected {(width,height)}, got {im.size}")
            proc.stdin.write(im.convert("RGB").tobytes())
            seen+=1
        proc.stdin.close()
        err=proc.stderr.read()
        code=proc.wait(timeout=120)
        if code:raise MKCVError("execution_failed",f"ffmpeg exit {code}: {err.decode('utf-8','replace')[-1200:]}")
        if seen!=count:raise MKCVError("bad_artifact",f"Input frame count mismatch {seen} != {count}")
    except BaseException:
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        proc.kill();proc.wait()
        raise


def local_font(size:int):
    """Resolve a local font on this receiver; never require a private asset."""
    from PIL import ImageFont
    for name in ("DejaVuSans.ttf", "Arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def generate_animatic(job:dict, root:Path, work:Path, width:int,height:int,fps:int)->tuple[Path,int]:
    from PIL import Image, ImageDraw, ImageFont
    from itertools import accumulate
    images=[]; total=0
    for row in job["inputs"]["images"]:
        img=Image.open(work_path(root,row["path"])).convert("RGB")
        frames=row.get("frames",48)
        focus=row.get("focus",[.5,.5]); z=row.get("zoom",[1.0,1.04])
        if not (isinstance(focus,list) and len(focus)==2 and all(type(x) in (int,float) and 0<=x<=1 for x in focus)):
            raise MKCVError("invalid_job","focus must be [0..1,0..1]")
        if not (isinstance(z,list) and len(z)==2 and all(type(x) in (int,float) and 1<=x<=1.6 for x in z)):
            raise MKCVError("invalid_job","zoom must be [1..1.6,1..1.6]")
        images.append((img,frames,focus,z,row.get("caption","")))
        total+=frames
    # Editable accessibility companion for visible titles, never a transcript of spoken audio.
    def srt_time(frame:int)->str:
        ms=round(frame*1000/fps)
        h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);sec,ms=divmod(ms,1000)
        return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"
    cues=[];cursor=0
    for img,n,focus,z,caption in images:
        if caption:
            cues.append(f"{len(cues)+1}\n{srt_time(cursor)} --> {srt_time(cursor+n)}\n{caption}\n")
        cursor+=n
    if cues:
        (work/"visual_titles.srt").write_text("\n".join(cues)+"\n",encoding="utf-8")
    def frames():
        for img,n,focus,z,caption in images:
            for i in range(n):
                t=i/max(1,n-1); smooth=t*t*(3-2*t)
                a=crop_to_frame(img,width,height,smooth,z[0],z[1],focus[0],focus[1])
                if caption:
                    draw=ImageDraw.Draw(a)
                    from PIL import ImageFont
                    font=local_font(max(16,round(height*.05)))
                    limit=max(0,int(width*.84))
                    # Caption is editable overlay, not claimed to be in source image.
                    while draw.textbbox((0,0),caption,font=font)[2]>limit and font.size>12:
                        font=local_font(font.size-1)
                    bb=draw.textbbox((0,0),caption,font=font)
                    cx=(width-(bb[2]-bb[0]))//2; y=height-round(height*.11)
                    draw.rounded_rectangle((max(0,cx-13),y-8,min(width,cx+bb[2]-bb[0]+13),y+bb[3]-bb[1]+14),radius=10,fill=(12,16,31))
                    draw.text((cx,y),caption,font=font,fill=(246,248,252))
                yield a
    path=work/"video_only.mp4"
    write_rgb_frames(frames(),path,width,height,fps,total)
    return path,total


def generate_edit(job:dict, root:Path, work:Path,width:int,height:int,fps:int)->tuple[Path,int]:
    paths=[];total=0
    for i,clip in enumerate(job["inputs"]["clips"]):
        p=work_path(root,clip["path"])
        num=clip.get("frames",48); start=clip.get("start_frame",0)
        part=work/f"part_{i:02d}.mp4"
        # Explicit output-frame sampling, with trim enforced after output fps normalization.
        vf=(f"fps={fps},trim=start_frame={start}:end_frame={start+num},setpts=PTS-STARTPTS,"
            f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1")
        exec_process(["ffmpeg","-hide_banner","-nostdin","-v","error","-y","-i",str(p),"-vf",vf,
               "-an","-frames:v",str(num),"-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p", "-threads","1",str(part)],timeout=180)
        pr=probe(part)
        if pr["frames"]!=num:raise MKCVError("bad_artifact",f"Clip {i}: expected {num}, got {pr['frames']}")
        paths.append(part);total+=num
    # Reconstruct a strict CFR timeline instead of concatenating MP4 packets with
    # inherited container time bases (which can report an inaccurate avg FPS).
    video=work/"video_only.mp4"
    inputs=[]
    for item in paths: inputs.extend(["-i",str(item)])
    labels=''.join(f"[{i}:v]" for i in range(len(paths)))
    exec_process(["ffmpeg","-hide_banner","-nostdin","-v","error","-y",*inputs,
        "-filter_complex",f"{labels}concat=n={len(paths)}:v=1:a=0[v]",
        "-map","[v]","-r",str(fps),"-fps_mode","cfr","-frames:v",str(total),
        "-an","-c:v","libx264","-preset","veryfast","-crf","21",
        "-pix_fmt","yuv420p","-threads","1",str(video)],timeout=180)
    return video,total


def compare_reference(job:dict,root:Path, work:Path)->tuple[Path,None]:
    from PIL import Image,ImageDraw
    import numpy as np
    import cv2
    inputs=job["inputs"]
    trusted=work_path(root,inputs["renderer"])
    assert hash_file(trusted)==inputs["renderer_sha256"]
    shutil.copy2(trusted,work/"rebuild_reference.py")
    shutil.copy2(work_path(root,inputs["reference"]),work/"reference.png")
    shutil.copy2(work_path(root,inputs["camera"]),work/"scene_spec.json")
    shutil.copy2(work_path(root,inputs["regions"]),work/"regions.json")
    exec_process([sys.executable,str(work/"rebuild_reference.py")],cwd=work,timeout=150)
    output_name=inputs.get("render_name","reconstruction_R2.png")
    p=work/output_name
    if not p.is_file():raise MKCVError("bad_artifact",f"Renderer did not create {output_name}")
    ref=Image.open(work/"reference.png").convert("RGB")
    render=Image.open(p).convert("RGB")
    w,h=render.size; ref=ref.resize((w,h),Image.Resampling.LANCZOS)
    combo=Image.new("RGB",(w*2,h));combo.paste(ref);combo.paste(render,(w,0))
    combo.save(work/"comparison.png")
    Image.blend(ref,render,.5).save(work/"overlay.png")
    spec=json.loads((work/"regions.json").read_text(encoding="utf-8"));results=[]
    if not isinstance(spec.get("regions"),list):raise MKCVError("invalid_job","regions must be array")
    ref_array=np.asarray(ref,dtype=np.float32); ren_array=np.asarray(render,dtype=np.float32)
    for i,r in enumerate(spec["regions"]):
        name=re.sub(r"[^A-Za-z0-9_-]","_",r.get("id",f"ROI{i}"))
        v=r["roi"]
        if len(v)!=4 or not all(0<=x<=1 for x in v) or v[0]>=v[2] or v[1]>=v[3]:
            raise MKCVError("invalid_job",f"Invalid ROI: {name}")
        coords=[int(a*b) for a,b in zip(v,[w,h,w,h])]; x0,y0,x1,y1=coords
        if x0==x1 or y0==y1:continue
        im=Image.new("RGB",((x1-x0)*2,y1-y0));im.paste(ref.crop(coords));im.paste(render.crop(coords),(x1-x0,0));im.save(work/f"roi_{i:02}_{name}.png")
        results.append({"region":name,"mean_abs_pixel_difference_descriptive_not_fidelity":round(float(np.abs(ref_array[y0:y1,x0:x1]-ren_array[y0:y1,x0:x1]).mean()),2)})
    (work/"OBSERVATIONS.json").write_text(json.dumps({"status":"not_a_fidelity_certificate","camera_matched":"not_verified_automatically","regions":results},ensure_ascii=False,indent=2))
    return p,None


def mux_music(video:Path, audio:Path,out:Path, duration:float)->None:
    exec_process(["ffmpeg","-hide_banner","-nostdin","-v","error","-y","-i",str(video),"-i",str(audio),
       "-filter_complex",f"[1:a]apad,atrim=duration={duration:.7f}[a]",
       "-map","0:v:0","-map","[a]","-c:v","copy","-c:a","aac","-b:a","160k","-movflags","+faststart",str(out)],timeout=120)


def contact_sheet(path:Path,out:Path, positions:tuple[float,...]=(.05,.25,.5,.75,.95)) -> None:
    from PIL import Image,ImageDraw
    import cv2
    cap=cv2.VideoCapture(str(path))
    n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT));cells=[]
    for p in positions:
        cap.set(cv2.CAP_PROP_POS_FRAMES, min(n-1,int(round((n-1)*p))))
        ok,frame=cap.read()
        if ok:cells.append(Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)).resize((320,180)))
    cap.release()
    if cells:
        sheet=Image.new("RGB",(320*len(cells),180));
        for i,img in enumerate(cells):sheet.paste(img,(320*i,0))
        sheet.save(out,quality=90)


def execute(job:dict, root:Path, plan:dict, *, max_chunks:int|None=None) -> dict:
    if max_chunks is not None and plan["profile"]!="coded_scene":
        raise MKCVError("invalid_job","--max-chunks is supported only for coded_scene")
    if plan["profile"]=="coded_scene":
        from mkcv_resumable import execute as execute_resumable
        return execute_resumable(job,root,plan,sys.modules[__name__],max_chunks=max_chunks)
    if plan["status"]!="executable":return {"status":"needs_capability_or_input","plan":plan}
    folder=work_path(root,plan["output"]["directory"],existing=False)
    if folder.exists():
        receipt=folder/"EXECUTION.json"
        if receipt.exists():
            try:
                prev=json.loads(receipt.read_text())
                if prev.get("fingerprint")==plan["fingerprint"]:
                    assets=prev.get("artifacts",{})
                    if all((folder/k).is_file() and hash_file(folder/k)==v["sha256"] for k,v in assets.items()):
                        return {"status":"reused_verified","directory":plan["output"]["directory"],"receipt":prev}
            except (ValueError,KeyError):pass
        raise MKCVError("output_conflict","Destination exists but cannot prove matching job and intact files; select new output.directory")
    folder.parent.mkdir(parents=True,exist_ok=True)
    lock=folder.parent/("."+folder.name+".execution.lock")
    try: lock.mkdir()
    except FileExistsError as ex:
        raise MKCVError("execution_in_progress_or_stale_lock", "Another execution or an unresolved lock exists for this exact output; reconcile before retrying") from ex
    stage=folder.parent/("."+folder.name+".attempt-"+uuid.uuid4().hex[:8]);stage.mkdir()
    w=plan["output"]["width"];h=plan["output"]["height"];fps=plan["output"]["fps"]
    profile=plan["profile"]
    try:
        expected=plan["expected_frames"]
        if profile=="animatic": vid,expected=generate_animatic(job,root,stage,w,h,fps)
        elif profile=="edit_existing": vid,expected=generate_edit(job,root,stage,w,h,fps)
        elif profile=="reference_3d": vid,expected=compare_reference(job,root,stage)
        else:raise MKCVError("needs_capability_or_input",f"Profile not runnable: {profile}")
        if profile!="reference_3d":
            final=stage/"film.mp4"
            if job["inputs"].get("audio"):
                mux_music(vid,work_path(root,job["inputs"]["audio"]),final,expected/fps)
            else:shutil.copy2(vid,final)
            meta=probe(final)
            if meta["frames"]!=expected:
                raise MKCVError("bad_artifact",f"Decoded frame count {meta['frames']} != expected {expected}")
            if (meta["width"],meta["height"])!=(w,h):raise MKCVError("bad_artifact","Dimension mismatch")
            num,den=map(int,meta["fps"].split('/'))
            if den==0 or num!=fps*den:raise MKCVError("bad_artifact",f"Frame rate mismatch: {meta['fps']} != {fps}/1")
            decode_all(final)
            contact_sheet(final,stage/"contact_sheet.jpg")
            result={"video":meta,"expected_frames":expected,"decoded_without_errors":True,"claim":"technical_output_not_semantic_quality_certification"}
            # Normalized intermediate files are implementation detail: keep only deliverables.
            for file in stage.glob("part_*.mp4"):file.unlink()
            for name in ("video_only.mp4","concat.txt"):
                tmp=stage/name
                if tmp.exists():tmp.unlink()
        else:
            from PIL import Image
            x=Image.open(vid);x.verify()
            result={"still":{"width":x.width,"height":x.height},"decoded_without_errors":True,"claim":"model_rendered_not_reference_fidelity_certification"}
        artifacts={f.name:{"sha256":hash_file(f),"bytes":f.stat().st_size} for f in sorted(stage.iterdir()) if f.is_file() and f.name not in ("EXECUTION.json",)}
        receipt={"schema":"mkcv-execution-receipt/0.2","status":"completed","version":VERSION,"profile":profile,
            "job_id":job.get("id"),"fingerprint":plan["fingerprint"],"inputs":plan["inputs"],"result":result,
            "artifacts":artifacts,"limits":"local output only; no publication/spend/background execution"}
        (stage/"EXECUTION.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        stage.rename(folder)
        return {"status":"completed","directory":plan["output"]["directory"],"receipt":receipt}
    except BaseException as e:
        (stage/"ATTEMPT.json").write_text(json.dumps({"status":"failed_without_claimed_output","code":getattr(e,"code",type(e).__name__),"message":str(e),"job_fingerprint":plan["fingerprint"]},ensure_ascii=False,indent=2),encoding="utf-8")
        raise
    finally:
        # The incomplete attempt survives for analysis; only the active lock ends.
        lock.rmdir()


def main():
    ap=argparse.ArgumentParser(description="MKCV AutoStudio — local, bounded, receipts-first media executor")
    ap.add_argument("command",choices=["catalog","plan","run"])
    ap.add_argument("job",nargs="?",type=Path)
    ap.add_argument("--workspace",type=Path,default=None,help="Explicit workspace root; job and all assets must reside within it")
    ap.add_argument("--max-chunks",type=int,default=None,help="QA controlled suspension after this many newly rendered chunks (no background work)")
    args=ap.parse_args()
    try:
        if args.command=="catalog":
            print(json.dumps({"version":VERSION,"profiles":PROFILES,"implemented_profiles":sorted(EXECUTABLE)},ensure_ascii=False,indent=2));return
        if not args.job:raise MKCVError("invalid_job","Job path required")
        job,root,jobpath=load(args.job,args.workspace)
        plan=plan_job(job,root)
        obj=plan if args.command=="plan" else execute(job,root,plan,max_chunks=args.max_chunks)
        print(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True))
        if obj.get("status")=="partial":sys.exit(4)
        if obj.get("status") not in ("executable","completed","reused_verified"): sys.exit(3)
    except MKCVError as e:
        print(json.dumps({"status":e.code,"message":str(e)},ensure_ascii=False,indent=2),file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        # Do not claim success; preserve the failed attempt and a machine-readable error.
        print(json.dumps({"status":"execution_failed","type":type(e).__name__,"message":str(e)},ensure_ascii=False,indent=2),file=sys.stderr)
        sys.exit(2)

if __name__=="__main__": main()
