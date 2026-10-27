# Keep the film continuous when rendering stops

When a render is long or interrupted, keep the intended timeline and render independently addressable frame intervals. Reuse a segment only after checking its inputs, code identity, frame count, dimensions, frame rate and decodability. A changed scene, asset or renderer calls for a new output identity. Segment boundaries are execution units; editing, gesture and narrative rhythm remain decisions about the film.

## Local use

The supplied job selects only the original trusted renderer, with an explicit SHA256. FFmpeg and ffprobe must already be installed and reachable on PATH; the script does not download them. From the competence folder:

```sh
cd examples/recoverable_video
python -m venv .venv
# Activate that environment with the command appropriate to your shell.
python -m pip install -r requirements.txt
python autostudio.py plan jobs/orbital_scene.json
python autostudio.py run jobs/orbital_scene.json --max-chunks 1
python autostudio.py run jobs/orbital_scene.json
python verify_recovery.py --output NEW_EMPTY_LOCATION
```

## Interpret the continuation

The first run returns `partial` and exit code 4: this is a controlled pause after one segment, not failure or a job left in the background. The second invocation of the same job verifies segments, completes the film and returns `completed`; another invocation returns `reused_verified`. `needs_capability_or_input` identifies missing means or inputs; `checkpoint_conflict` preserves earlier work when identity changed. Choose a new directory for changed work; do not delete checkpoints to bypass a mismatch. The four catalogue profiles need their own material; this package supplies a coded scene, not media for other examples. `reference_3d` executes an already-authored trusted local renderer with project-supplied inputs: it does not reconstruct an image automatically.

## Competences and evidence

A technical checkpoint preserves verified work. The project guide preserves subject, sources, reasons, open choices and what the next contributor must understand. Use both when needed: resuming an encoder does not restore an assistant’s understanding or start a background agent. Observing the resulting film may still change the scene, method or chosen medium.

The included coded-scene adapter was exercised in a Windows receiver with pause/resume, real process-tree interruption, damaged-segment repair and a continuous-render comparison. This does not establish narrative quality, image-to-3D fidelity, cross-host recovery or access to a media provider. The `examples/recoverable_video/VERIFICATION.json` report preserves the technical observation. The previous archive’s tests and media are not part of this kit. The supplied verification script exercises the local contract in a new directory.
