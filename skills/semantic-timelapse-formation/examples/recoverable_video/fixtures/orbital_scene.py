#!/usr/bin/env python3
"""MKCV — original *illustrative* orbital observatory code-made mini-film.

Deterministic, frame-index-addressable renderer for MKCV AutoStudio 0.3.
This is a stylized imaginary scene; it contains no spacecraft measurements,
photos, astronomical data, or real simulation of orbital mechanics.
"""
import argparse
import math
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SEED=20261026
rng=np.random.default_rng(SEED)
STARS=[(float(x),float(y),float(a),float(p)) for x,y,a,p in zip(rng.random(155),rng.random(155),rng.uniform(.3,1.,155),rng.uniform(0,6.28,155))]
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font_at(size:int,bold:bool=False):
    # System fonts are used where available. Font files are not redistributed.
    faces=[FONT_BOLD if bold else FONT,'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf',
           'C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf']
    for f in faces:
        try:return ImageFont.truetype(f,size)
        except OSError:pass
    return ImageFont.load_default()


def rgba_color(rgb):return tuple(map(int,np.clip(rgb,0,255)))
def render_frame(frame:int,fps:int,w:int,h:int)->Image.Image:
    """Entire image depends only on absolute frame index and fixed seed."""
    t=frame/fps
    y,x=np.mgrid[0:h,0:w].astype(np.float32)
    xx=x/w;yy=y/h
    soft=np.exp(-((xx-.72)**2/.24+(yy-.48)**2/.35))
    b=np.zeros((h,w,3),dtype=np.float32)
    b[:,:,0]=7+24*yy+15*soft; b[:,:,1]=12+15*yy+18*soft; b[:,:,2]=36+36*yy+29*soft
    # Gently moving atmospheric glow: procedural 2D space art, NOT a star chart.
    wave=np.exp(-((yy-(.72+.04*np.sin(xx*8-t*.25)))**2)/.018)
    b[:,:,0]+=7*wave; b[:,:,1]+=13*wave; b[:,:,2]+=29*wave
    im=Image.fromarray(np.uint8(np.clip(b,0,255)),mode='RGB').convert('RGBA')
    d=ImageDraw.Draw(im,'RGBA')
    for sx,sy,power,phase in STARS:
        starx=int(((sx + .008*t*(.3+sy))%1)*w);stary=int(sy*h)
        v=max(0.08,0.6+0.4*math.sin(phase+t*(1+sy*.8)))
        r=1.7 if power>.84 else 1
        d.ellipse((starx-r,stary-r,starx+r,stary+r),fill=(182,209,255,int(70+140*v*power)))
    # Planet is a code-constructed 2.5D sphere with a moving terminator.
    cx=w*.74;cy=h*.53;R=h*.325
    py,px=np.mgrid[0:h,0:w]
    dx=(px-cx)/R; dy=(py-cy)/R
    rad2=dx*dx+dy*dy; mask=rad2<=1
    nz=np.sqrt(np.clip(1-rad2,0,1))
    light=.31+.69*np.clip(-dx*.58-dy*.18+nz*.7,0,1)
    bands=(np.sin((dy+.3)*13.5+np.sin(dx*6+t*.025)*.6)+1)/2
    stripes=.22*np.sin(dy*31+dx*5+1.3)
    pc=np.zeros((h,w,4),dtype=np.uint8)
    pc[:,:,0]=np.uint8(np.clip((30+64*bands+44*stripes)*light,0,255))
    pc[:,:,1]=np.uint8(np.clip((84+70*bands)*light,0,255))
    pc[:,:,2]=np.uint8(np.clip((143+94*bands-22*stripes)*light+36*nz,0,255))
    pc[:,:,3]=np.where(mask,255,0)
    # Planetary atmosphere, low-key and stylized.
    gl=Image.new('RGBA',(w,h));g=ImageDraw.Draw(gl,'RGBA')
    for k in range(13,0,-1):
        gr=R+k*(h/330)
        g.ellipse((cx-gr,cy-gr,cx+gr,cy+gr),outline=(42,179,243,int(5+4*(14-k))),width=2)
    gl=gl.filter(ImageFilter.GaussianBlur(6))
    im=Image.alpha_composite(im,gl)
    # Back ring, planet, front ring; depth suggested through deliberate occlusion.
    ring=Image.new('RGBA',(w,h));dr=ImageDraw.Draw(ring,'RGBA')
    for j in range(15):
        rr=R*(1.15+j*.034)
        box=(cx-rr*1.38,cy-rr*.34,cx+rr*1.38,cy+rr*.34)
        dr.arc(box,181,359,fill=(106+j*4,164+j*2,211+j,int(47+4*j)),width=1)
    im=Image.alpha_composite(im,ring)
    im=Image.alpha_composite(im,Image.fromarray(pc,mode='RGBA'))
    front=Image.new('RGBA',(w,h));df=ImageDraw.Draw(front,'RGBA')
    for j in range(15):
        rr=R*(1.15+j*.034)
        box=(cx-rr*1.38,cy-rr*.34,cx+rr*1.38,cy+rr*.34)
        df.arc(box,1,179,fill=(119+j*4,176+j*2,205+j,int(43+5*j)),width=1)
    im=Image.alpha_composite(im,front)
    d=ImageDraw.Draw(im,'RGBA')
    # Small spacecraft scanning the atmosphere: fictional orbital motion.
    sx=w*(.31+.038*math.sin(t*.53));sy=h*(.46+.063*math.cos(t*.71));angle=.16*math.sin(t*.7)
    # a connecting beam grows near the middle of the film, tied to time and scene geometry
    progress=min(1,max(0,(t-1.9)/1.1));fade=max(0,min(1,(4.7-t)/.7))
    if progress>0:
        endpoint=(cx-R*.65,cy-R*.13)
        ex=sx+(endpoint[0]-sx)*progress;ey=sy+(endpoint[1]-sy)*progress
        beam=Image.new('RGBA',(w,h));bd=ImageDraw.Draw(beam,'RGBA')
        bd.line((sx,sy,ex,ey),fill=(28,192,243,int(70*fade)),width=9)
        beam=beam.filter(ImageFilter.GaussianBlur(9)); im=Image.alpha_composite(im,beam)
        d=ImageDraw.Draw(im,'RGBA');d.line((sx,sy,ex,ey),fill=(134,239,253,int(235*fade)),width=2)
        if progress>.99:
            glowR=12+3*math.sin((t-2.9)*5)
            d.ellipse((ex-glowR,ey-glowR,ex+glowR,ey+glowR),outline=(79,236,232,int(140*fade)),width=2)
    # Spacecraft facets, arranged around a rotated central body.
    def rot(qx,qy):return sx+qx*math.cos(angle)-qy*math.sin(angle),sy+qx*math.sin(angle)+qy*math.cos(angle)
    solar1=[rot(u,v) for u,v in [(-44,-13),(-17,-13),(-17,13),(-44,13)]]
    solar2=[rot(u,v) for u,v in [(17,-13),(44,-13),(44,13),(17,13)]]
    for panel in (solar1,solar2):
        d.polygon(panel,fill=(18,90,143,255),outline=(83,230,255,240))
        for k in range(1,4):
            xx1=panel[0][0]+(panel[1][0]-panel[0][0])*k/4
            xx2=panel[3][0]+(panel[2][0]-panel[3][0])*k/4
            d.line((xx1,panel[0][1],xx2,panel[3][1]),fill=(122,211,239,115),width=1)
    d.line((*rot(-18,0),*rot(18,0)),fill=(199,215,240,255),width=4)
    d.ellipse((*rot(-13,-11),*rot(13,11)),fill=(229,235,244,255),outline=(102,203,245,255),width=2)
    d.ellipse((sx-3,sy-3,sx+3,sy+3),fill=(33,241,233,255))
    d.line((*rot(0,-11),*rot(0,-24)),fill=(158,211,233,250),width=2)
    # Title holds the human meaning, not fake software UI or measured telemetry.
    f1=font_at(max(15,int(h*.062)),True)
    f2=font_at(max(11,int(h*.035)))
    f3=font_at(max(9,int(h*.026)))
    d.text((w*.06,h*.105),'MONDI IN CODICE',fill=(244,251,255,255),font=f1)
    d.text((w*.06,h*.105+h*.09),'Una scena prende movimento',fill=(157,228,245,250),font=f2)
    d.line((w*.06,h*.255,w*.18,h*.255),fill=(71,209,229,220),width=3)
    d.text((w*.06,h*.91),'MKCV  /  VISUALIZZAZIONE ORIGINALE',fill=(140,183,212,230),font=f3)
    return im.convert('RGB')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--start-frame',type=int,required=True)
    p.add_argument('--end-frame',type=int,required=True)
    p.add_argument('--fps',type=int,required=True)
    p.add_argument('--width',type=int,required=True)
    p.add_argument('--height',type=int,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--asset-root',type=Path,required=True)
    a=p.parse_args()
    if a.start_frame<0 or a.end_frame<=a.start_frame or a.end_frame-a.start_frame>1000:
        p.error('Invalid segment range')
    if a.width>1920 or a.height>1080 or a.width%2 or a.height%2 or a.fps>60:
        p.error('Invalid scene parameters')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    cmd=['ffmpeg','-hide_banner','-nostdin','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24',
         '-s',f'{a.width}x{a.height}','-r',str(a.fps),'-i','pipe:0','-an','-c:v','libx264',
         '-preset','veryfast','-crf','21','-threads','1','-pix_fmt','yuv420p','-movflags','+faststart',str(a.output)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    try:
        for i in range(a.start_frame,a.end_frame):
            frame=render_frame(i,a.fps,a.width,a.height)
            proc.stdin.write(frame.tobytes())
        proc.stdin.close()
        err=proc.stderr.read();code=proc.wait(timeout=100)
        if code:raise RuntimeError(err.decode('utf8','replace')[-1300:])
    except BaseException:
        if proc.stdin and not proc.stdin.closed:proc.stdin.close()
        proc.kill();proc.wait();raise
if __name__=='__main__':main()
