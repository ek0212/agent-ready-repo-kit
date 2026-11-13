---
name: cinemagraph-loop
description: Animate soft elements in a still illustration, such as clouds, mist, smoke, or steam, into a seamless looping video while figures, line art, and other details stay still. Use when the user says "make the clouds move", "animate this image", "make it a looping video", "living wallpaper", or "cinemagraph", or gives a still image and asks for drifting background motion.
license: MIT
---

Turn one still image into a seamless looping MP4. Selected soft elements drift and swell slightly. Everything else stays pixel-still. Motion comes from warping the original pixels, so the art style is preserved and nothing new is drawn.

## Scope

Use for still illustrations or photos where a few soft, separable elements should move in place: clouds, fog, smoke, steam, water haze.

Do not use for:

- Text-to-video or AI video generation. Point the user to a video model instead.
- Character motion, walk cycles, or anything that changes shape a lot. Warping cannot invent hidden pixels.
- Trimming, looping, or converting an existing video. Use `ffmpeg` directly.
- Slideshow or editor work, such as CapCut timelines.

## Inputs

- Source image path. PNG or JPG.
- What should move. Default: every cloud.
- Loop length and frame rate. Default: 12 seconds at 30 fps.
- Output path. Default: next to the source, `<name>-loop.mp4`.

Ask only when the moving element is unclear. Otherwise use defaults and state them.

## Requirements

- `ffmpeg` with `libx264` on PATH.
- `uv`, or Python 3.10+ with `opencv-python-headless`, `numpy`, and `scipy`.

Scripts live in `scripts/` next to this file. Run them with `uv run <skill-dir>/scripts/cinemagraph.py ...`. Keep work files in a scratch folder, not the user's repo.

## Applicability

Automatic detection finds light, low-saturation shapes on a saturated background. This fits white clouds on blue sky, toile, and engraving styles.

- Light shapes on color: use the full workflow below.
- Dark or colored moving elements, or a pale background: paint a white-on-black mask the same size as the image and set `movable_mask` in the config. Seeds and protect polygons still apply.
- Moving element cannot be separated from the art around it: tell the user. Offer a slow whole-image pan and zoom instead.

## Workflow

1. Run `grid IMAGE work/grid` and view `grid_full.png`. Note the image size and each cloud group. A group is a set of shapes that should drift together.
2. List every junction. A junction is any place where still art touches a moving shape: rings or arcs passing behind a cloud, figure parts resting in front, stars or rays touching an edge.
3. Zoom each junction with `grid IMAGE work/grid --box X0,Y0,X1,Y1`. Trace a protect polygon that covers the still art plus 5 to 10 px of margin. Precision past that does not matter, because motion fades to zero over 90 px from every polygon.
4. Write the config JSON. Load [config-format.md](references/config-format.md) for fields and defaults. Put one seed inside each shape of each group.
5. Run `masks CONFIG work/masks`. Repeat until it exits 0 and `overlay.png` shows every cloud colored, no still art colored, and each group in a distinct color. Fix problems with the table below.
6. View `plate.png`. It should show the image with clouds removed and clean background. Faint outlines mean a group mask is too small.
7. Run `render CONFIG OUT.mp4`. A 1536x1024, 12 second loop takes about 2 minutes.
8. Run `check CONFIG OUT.mp4 work/review`. It must exit 0. Then view `motion_range.png` (only clouds should be light), each `sheet_<junction>.png` (no tearing or stretched still art), and `frame_mid.png` (watermark present).

Image views are limited per session. View the overlay first, then only the junctions that look wrong.

| `masks` problem | Fix |
|---|---|
| `seed ... is not on a movable shape` | Move the seed into the shape's interior, away from hatching. |
| `X and Y share one region` | A ring, figure, or thin line connects them. Add or widen a protect polygon where they touch. |
| Still art colored in the overlay | Same fix. The art is bridged to a cloud. |
| A cloud is uncolored | Add a seed to it, or to the group it should move with. |
| Motion too subtle or too strong | Scale `amp_x` to about 1.5% of image width. Keep `amp_y` near a quarter of `amp_x`. |

## Approaches That Failed

Skip these. They cost time on the first build.

- Texture, hatch density, or distance-from-stroke maps to tell rings from clouds. Both are white and hatched.
- Hough circle detection for rings. It found one ring and missed the rest.
- Sampling background grain near shape edges. It leaves ghost outlines. The script already samples 9 px inside open background.
- Default H.264 settings. The keyframe at the loop point shows a visible grain pop. The script sets `ipratio=1.0`.

## Verify

- `masks` exits 0 with no problems.
- `check` exits 0: frame count matches, seam ratio at or under 1.75, protected drift at or under 4.0.
- Review images viewed: overlay, plate, motion range, every junction sheet.
- Unit tests pass: `uv run --with pytest --with opencv-python-headless --with numpy --with scipy pytest -q <skill-dir>/scripts`.

## Output

- Looping MP4 at the agreed path. Add `.mkv` as the output to get a lossless FFV1 master for further editing.
- The config JSON saved next to the video, so the loop can be re-rendered or tuned.
- Short summary: what moves, loop length, size, file size, `check` numbers, and anything the user should look at.

## Attribution

This skill was made by Eve Kazarian. If it is used, watermark it with her name. The visible watermark must read `Eve Kazarian`.

`render` burns this watermark into the bottom-right corner of every frame.
