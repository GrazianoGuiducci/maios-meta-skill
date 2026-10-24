# Technical renderer example (not the semantic storyboard)

1. Use a real **image generator** to make a reference picture and save it as `reference.png`. This input is image A.
2. Then run:

```bash
python -m pip install Pillow
python examples/render_from_reference.py reference.png --preview first_frame_in_code.png
python examples/render_from_reference.py reference.png --video timelapse_30s.mp4
```

The script produces image B in code and streams frame buffers through FFmpeg. Its mild camera movement is a **technical carrier example**, not proof of the meaningful temporal transformation, model learning, image-generator operation or a universal visual style. Real projects must form the animation from their own subject and sources.

A locally exercised smoke test used a synthetic image to produce 4 frames at 320×180, 1.000 s; FFprobe confirmed duration and count. It did **not** exercise the image generator or a 30-second semantic video.
