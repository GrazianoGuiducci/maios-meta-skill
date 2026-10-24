"""A technical render example, not a semantic time-lapse storyboard.

Make the reference image with an image generator first and save it as a local PNG.
The real project's semantic transformation must be designed from its sources.
"""
from __future__ import annotations
import argparse
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageOps


def frame_at(reference: Image.Image, t: float, duration: float, size: tuple[int, int]) -> Image.Image:
    """Render a code-built frame, using the generated image as a visible reference."""
    w, h = size
    u = max(0.0, min(1.0, t / duration))
    # Mild camera movement shows the rendering contract. Replace with a
    # source-grounded transformation; motion alone does not imply learning.
    zoom = 1.00 + 0.06 * (u * u * (3 - 2 * u))
    enlarged = ImageOps.fit(reference, (round(w * zoom), round(h * zoom)), method=Image.Resampling.LANCZOS)
    left = round((enlarged.width - w) * (0.45 + 0.1 * u))
    top = round((enlarged.height - h) / 2)
    return enlarged.crop((left, top, left+w, top+h)).convert('RGB')


def main() -> None:
    parser = argparse.ArgumentParser(description='Reference-image to coded-frame rendering example')
    parser.add_argument('reference', type=Path, help='Image generated first using an image generator')
    parser.add_argument('--preview', type=Path, default=Path('first_frame_in_code.png'))
    parser.add_argument('--video', type=Path, default=None)
    parser.add_argument('--duration', type=float, default=30.0)
    parser.add_argument('--fps', type=int, default=24)
    parser.add_argument('--width', type=int, default=960)
    parser.add_argument('--height', type=int, default=540)
    args = parser.parse_args()
    if not args.reference.is_file(): parser.error('Provide an existing image created with the image generator')
    if args.duration <= 0 or args.fps <= 0 or args.width <= 0 or args.height <= 0:
        parser.error('Duration, fps and dimensions must be positive')
    if args.video and not shutil.which('ffmpeg'):
        parser.error('FFmpeg is required for MP4 export')
    reference = ImageOps.exif_transpose(Image.open(args.reference)).convert('RGB')
    size = (args.width, args.height)
    first = frame_at(reference, 0.0, args.duration, size)
    first.save(args.preview)
    if not args.video:
        print(f'Wrote coded first frame: {args.preview}')
        return
    total_frames = round(args.duration * args.fps)
    cmd = ['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24',
           '-s',f'{args.width}x{args.height}','-r',str(args.fps),'-i','-','-an',
           '-c:v','libx264','-pix_fmt','yuv420p',str(args.video)]
    encoder = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        assert encoder.stdin is not None
        for i in range(total_frames):
            encoder.stdin.write(frame_at(reference, i/args.fps, args.duration, size).tobytes())
    except (BrokenPipeError, Exception):
        encoder.kill()
        encoder.communicate()
        raise
    else:
        assert encoder.stdin is not None
        encoder.stdin.close()
        assert encoder.stderr is not None
        err = encoder.stderr.read().decode('utf-8', errors='replace')
        code = encoder.wait()
        if code:
            raise RuntimeError(f'FFmpeg exit {code}: {err}')
    print(f'Wrote {total_frames} frames: {args.video}')


if __name__ == '__main__':
    main()
