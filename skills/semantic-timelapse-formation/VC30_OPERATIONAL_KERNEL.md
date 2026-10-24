# VC-30s — Operational competence field for code-made short videos

**State:** candidate 0.3.0, method available, not a standalone runtime or deployed generator. This is a **mini-kernel of cooperating capabilities** within Semantic Timelapse Formation, not a second axiomatic kernel, a mandatory multi-stage pipeline or a new publishing controller. The short film (about 30 seconds when selected) is the shared object that keeps visual direction, code, audio and learning connected.

## Form the film from the actual subject

The subject, its source, what is observed vs illustrated, the receiving viewer and the meaningful change determine which capabilities should participate. The mini-kernel can combine source understanding, generated visual references, storyboard/design, 2D/2.5D/3D scene implementation, timeline composition, optional narration/sound, encoding/inspection and return of reusable learning. Not every video needs characters, Three.js, voiceover or an independent image sequence.

**Image A** is a real output from an image generator, generated from source-bound instructions and **observed before writing the first visual frame in code**. The purpose is to avoid relying only on the model's visual recollection. **Image B** is the coded first frame of an editable scene, not a substitute for A. A bitmap does not provide hidden depth, character rigging or real events; the executable scene must acquire these if the film requires them.

An actor or object needs a recognisable identity across time: referent, role, visual features, observable state, actions, relations and, if necessary, pose, prop contacts and camera visibility. Isometric SVG/CSS or layered 2.5D can communicate depth; true 3D requires actual geometry, lighting and camera when they materially help understanding.

## Composing possible technical carriers

**HTML/video:** [HyperFrames](https://github.com/heygen-com/hyperframes) uses timed HTML clips and seekable timelines, with GSAP and custom `hf-seek` rendering for Canvas/Three.js. Its framework is Apache-2.0.

**React/video:** [Remotion](https://github.com/remotion-dev/remotion) uses `useCurrentFrame()`, compositions and sequences. Its Remotion License is **not** an unrestricted MIT or Apache license: consult current free/company terms for the user's organization.

**2D/interaction:** [PixiJS/GSAP example](https://github.com/AhmadDinkaa/pixijs-tic-tac-toe) separates scene objects, game state, feedback animations and sound. For a film, convert real-time event callbacks to frame-addressable states.

**Web/3D:** [GSAP/Three.js example](https://github.com/TheWebxite/phans-custom-tailor) provides shader-based fabric/photo effects and fallbacks, but a WebGL realtime loop cannot be assumed seekable. The source's license for code/asset reuse must be resolved separately.

**Narration/audio:** [Motion Video](https://github.com/bestagentkits/motion-video-skill) offers beat-aligned speech/captions/music and a measured export loop; its provider credentials and specific thresholds do not become universal requirements.

**Motion craft:** [iart motion-skills](https://github.com/iart-ai/motion-skills) links targeted skills for storytelling, character drawing, isometric projection, data infographics, WebGL, audio and frame inspection. Acquire only the relevant competence and treat each pack's examples separately from its general craft.

**Web motion language:** [modern-portfolio](https://github.com/sanidhyy/modern-portfolio) uses Framer Motion variants and layered page transitions; learn the coordination, not the website's styles or automatic video support.

These sources are **mechanisms and learning resources**, not installed providers. No code, images, fonts, music or shader assets are copied into this public skill. Resolve dependencies and permissions in the actual receiving environment.

## Learning from other people's methods, without copying their implementation

Two passes over the external sources refine **what the competence knows how to do**, not which repositories it installs.

**From labels to a perceptible medium.** A word like “cinematic” or “modern” cannot specify the scene. Let the actual subject make material, shape, framing, lighting and behaviour meaningful in image-generator reference A. Observe A as a **visual hypothesis**: do not repeat its arbitrary composition or false causal hints in coded scene B. Named looks, lists of default bans, numerical timing rules and branded styles from the source projects are not MAIOS invariants.

**From an illustrated character to a coherent action.** If a person or object matters to the film, recognise the visual features, pose, gaze, contact points and relations that must continue. A hand holding a tool, an eye directed at the object and a prop crossing a camera cut express a persistent relation, not just animated pixels. A flattened A cannot reveal the unseen back, a rig or hidden object geometry. Use a different viewpoint or an appropriate real asset rather than inventing those parts.

**From movement to a first-time reading.** A scene can be understood through what the eye can follow: action, consequence, hold, change of framing, words and silence. Time can illustrate sequence, comparison, uncertainty or cause; do not force every adjacent shot into a causal chain. If voice or music matters, use meaningful action/word cues rather than arbitrary timestamps, while allowing silent videos when appropriate.

**From render inspection to learning.** A still can expose geometry, a moving clip pacing, an encoded frame an export issue. These observations can refine the nearest method without creating an approval ritual. A model's assessment “as a first-time viewer” is not evidence of actual audience comprehension. Preserve that distinction.

The learned faculty is **situated perceptual translation**: understanding a source, forming an observable visual reference, and deriving a reproducible temporal expression that keeps the subject's meaning. Code and runtime decisions remain with the technical owner; no source project's code, assets or styles are bundled here.

## Recheck of previously unread sources: the generated image is not an animation rig

An audit of seven originally named repositories, all **18 iart package README entry points**, and the **seven top-level HyperFrames skills** found a missing distinction. This is **not** a claim to have read every iart skill (55 declared by the hub), every HyperFrames block or Remotion implementation.

The first genuinely generated and inspected **image A remains the visual reference**. It may establish art direction, the relation between characters/objects and the readable whole. But a single flattened illustration cannot independently animate a hand, held tool, background, eye movement or the reverse view of an object. When the actual motion needs them, form **additional source-bound visual elements, poses, masks or geometry**; when a single whole image suffices, keep it whole. Additional assets should remain coherent with the subject and A, while their provenance and roles stay identifiable. They are not retroactively relabelled as the first A.

This distinction was learned from [Generative Illustration](https://github.com/iart-ai/generative-illustration-skills), whose working methods separate illustrations into independently animable units. One of that project's source documents cautions that naïve SVG background removal can delete a foreground object. The lesson is to **preserve the subject when isolating parts**, not import a particular algorithm, template or vector file.

[HyperFrames media-use](https://github.com/heygen-com/hyperframes) also teaches that reused assets require source identity and separation across projects. An asset belongs to its context; a vaguely similar cached logo or illustration does not acquire the right identity. For a new video receiver, preserve the provenance/role needed to use media correctly, without assuming HyperFrames' own file manifest.

**What remains editable matters.** A scene translated into native editable elements, hosted time-seekable code or a finished rendered clip preserves different editing abilities. The rendered clip is not the same as a freely movable character. [Remotion ThreeCanvas](https://github.com/remotion-dev/remotion) is one example of 3D tied to absolute frame time, if that renderer is actually chosen.

**Format and language belong before the render.** A 16:9 master often must be **recomposed**, not merely cropped, for 9:16 while preserving people, objects and titles. Exact words should remain editable and, where appropriate, accessible through captions or transcripts, not be guessed from pixels in A. Current social platform overlay dimensions need case-specific confirmation.

No third-party source code or assets have been imported, and no new film is claimed.

## A video must be addressable in time

The export scene should support `frame(t, scene, assets)` or an equivalent absolute-frame method that can render frames **out of order**. GSAP tickers and Three.js `update(dt)` are live-web mechanisms, not an assurance of deterministic video. Seed randomness, wait for images/fonts/GPU to be ready, and preserve identities between shots. 30s × 24fps = 720 frames, but neither format nor frame rate is universal.

Separate **source time** (real recorded events and intervals) from **presentation time** (the timeline of the explanatory animation). When only the latter exists, the output is an explanatory short rather than documented time-lapse footage.

Audio and caption cues should share time data with the film if they contribute meaning. Silence can be the correct result. Check actual encoded duration, dimensions and track presence plus representative decoded frames when those claims matter; observing a clip is not proof of viewer understanding.

## Reusable recursive return

An image may introduce a false hierarchy; a character may lose its identity while turning; an HTML animation may fail to seek; a caption or soundtrack may create a misleading temporal implication. Correct the source interpretation, image instruction, visual design, code, sound or receiver method **at the owner that must act differently next time**. If a method already existed but was not reached, improve discovery, not the number of skill files. No claim that an exported film changes model weights or self-installs tools.

**Not yet exercised in this public edition:** the complete A generated → A observed → B coded with characters/objects → video chain, a new 3D render, external audio providers, publication. The kernel makes those capacities **discoverable**, not automatically active.

**Source coordinates and provenance:** this portable text distills methods from the linked projects as read on 24 October 2026. Source versions and licenses may change; re-open the actual repository where an integration/asset choice becomes material.
