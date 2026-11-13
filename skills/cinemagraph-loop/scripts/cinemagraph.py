# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless>=4.9", "numpy>=1.26", "scipy>=1.11"]
# ///
"""Command-line tools for the cinemagraph-loop skill.

Subcommands:
  grid IMAGE OUT_DIR [--box X0,Y0,X1,Y1 ...]  Write crops with a pixel grid for tracing coordinates.
  masks CONFIG OUT_DIR                         Write mask overlay, background plate, and junction zooms.
  render CONFIG OUT.mp4                        Render the loop. An .mkv output writes a lossless FFV1 master.
  check CONFIG VIDEO OUT_DIR                   Measure the loop seam and still regions; write review images.
"""

import argparse
import shutil
import statistics
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np

import constants as C
import loop

Box = Tuple[int, int, int, int]


def parse_box(text: str) -> Box:
    """Parse an X0,Y0,X1,Y1 box.

    Args:
        text: Comma-separated integers.

    Returns:
        Box tuple.

    Raises:
        argparse.ArgumentTypeError: When the text is not four integers.
    """
    try:
        x0, y0, x1, y1 = (int(value) for value in text.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("box must be X0,Y0,X1,Y1") from error
    return x0, y0, x1, y1


def clip_box(box: Box, shape: Tuple[int, ...]) -> Box:
    """Clip a box to the image bounds.

    Args:
        box: Box to clip.
        shape: Image shape.

    Returns:
        Clipped box.
    """
    height, width = shape[:2]
    x0, y0, x1, y1 = box
    return max(0, x0), max(0, y0), min(width, x1), min(height, y1)


def polygon_box(points: loop.Polygon, shape: Tuple[int, ...]) -> Box:
    """Return a padded, clipped bounding box around a polygon.

    Args:
        points: Polygon points.
        shape: Image shape.

    Returns:
        Box around the polygon.
    """
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    return clip_box((min(xs) - C.ZOOM_PAD_PX, min(ys) - C.ZOOM_PAD_PX,
                     max(xs) + C.ZOOM_PAD_PX, max(ys) + C.ZOOM_PAD_PX), shape)


def draw_grid(crop: np.ndarray, box: Box, scale: float, step: int, label_step: int) -> np.ndarray:
    """Draw source-pixel grid lines and coordinate labels on a scaled crop.

    Args:
        crop: Scaled crop.
        box: Source box the crop came from.
        scale: Crop scale factor.
        step: Grid spacing in source pixels.
        label_step: Label spacing in source pixels.

    Returns:
        Crop with grid.
    """
    x0, y0, x1, y1 = box
    for x in range((x0 // step + 1) * step, x1, step):
        major = x % label_step == 0
        position = int((x - x0) * scale)
        cv2.line(crop, (position, 0), (position, crop.shape[0]), C.GRID_MAJOR_BGR if major else C.GRID_MINOR_BGR, 1)
        if major:
            cv2.putText(crop, str(x), (position + 2, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, C.GRID_MAJOR_BGR, 1)
    for y in range((y0 // step + 1) * step, y1, step):
        major = y % label_step == 0
        position = int((y - y0) * scale)
        cv2.line(crop, (0, position), (crop.shape[1], position), C.GRID_MAJOR_BGR if major else C.GRID_MINOR_BGR, 1)
        if major:
            cv2.putText(crop, str(y), (2, position - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.45, C.GRID_MAJOR_BGR, 1)
    return crop


def zoom(image: np.ndarray, box: Box, max_scale: float) -> Tuple[np.ndarray, float]:
    """Crop and enlarge a box without exceeding the maximum review width.

    Args:
        image: Source image.
        box: Box to crop.
        max_scale: Largest scale factor.

    Returns:
        Scaled crop and the scale used.
    """
    x0, y0, x1, y1 = box
    scale = min(max_scale, C.ZOOM_MAX_WIDTH_PX / max(1, x1 - x0))
    crop = cv2.resize(image[y0:y1, x0:x1], None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    return crop, scale


def command_grid(args: argparse.Namespace) -> int:
    """Write a full-image grid, or zoomed grids for each --box.

    Args:
        args: Parsed arguments.

    Returns:
        Exit code.
    """
    image = loop.read_image(args.image)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"image size: {image.shape[1]}x{image.shape[0]}")
    if not args.box:
        full = draw_grid(image.copy(), (0, 0, image.shape[1], image.shape[0]), 1.0,
                         C.GRID_FULL_STEP_PX, C.GRID_FULL_STEP_PX)
        cv2.imwrite(str(out_dir / "grid_full.png"), full)
        print(f"wrote {out_dir / 'grid_full.png'}")
        return 0
    for box in args.box:
        box = clip_box(box, image.shape)
        crop, scale = zoom(image, box, C.GRID_ZOOM_SCALE)
        path = out_dir / f"grid_{box[0]}_{box[1]}_{box[2]}_{box[3]}.png"
        cv2.imwrite(str(path), draw_grid(crop, box, scale, C.GRID_ZOOM_STEP_PX, C.GRID_ZOOM_LABEL_STEP_PX))
        print(f"wrote {path}")
    return 0


def mask_overlay(image: np.ndarray, masks: loop.Masks, config: loop.LoopConfig) -> np.ndarray:
    """Color each group, outline protect polygons, and label groups.

    Args:
        image: Source image.
        masks: Segmentation result.
        config: Loop config.

    Returns:
        Overlay image.
    """
    overlay = (image * 0.55).astype(np.uint8)
    for index, (name, mask) in enumerate(masks.groups.items()):
        color = np.array(C.GROUP_COLORS_BGR[index % len(C.GROUP_COLORS_BGR)])
        overlay[mask] = (image[mask] * 0.35 + color * 0.65).astype(np.uint8)
        ys, xs = np.nonzero(mask)
        if len(xs):
            cv2.putText(overlay, name, (int(xs.mean()) - 30, int(ys.mean())), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        C.LABEL_BGR, 2)
    for points in config.protect.values():
        cv2.polylines(overlay, [np.array(points, np.int32)], True, C.LABEL_BGR, 1)
    return overlay


def junction_zoom(image: np.ndarray, masks: loop.Masks, points: loop.Polygon) -> np.ndarray:
    """Zoom on one protect polygon with group contours in red and the polygon in green.

    Args:
        image: Source image.
        masks: Segmentation result.
        points: Protect polygon.

    Returns:
        Zoomed review crop.
    """
    box = polygon_box(points, image.shape)
    crop, scale = zoom(image, box, C.GRID_ZOOM_SCALE)
    union = np.zeros(image.shape[:2], np.uint8)
    for mask in masks.groups.values():
        union |= mask.astype(np.uint8)
    contours, _ = cv2.findContours(union, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    origin = np.array(box[:2])
    for contour in contours:
        cv2.polylines(crop, [((contour.reshape(-1, 2) - origin) * scale).astype(np.int32)], True, C.CONTOUR_BGR, 1)
    cv2.polylines(crop, [((np.array(points) - origin) * scale).astype(np.int32)], True, C.PROTECT_BGR, 1)
    return draw_grid(crop, box, scale, C.GRID_ZOOM_STEP_PX, C.GRID_ZOOM_LABEL_STEP_PX)


def command_masks(args: argparse.Namespace) -> int:
    """Write segmentation review images and report mask problems.

    Args:
        args: Parsed arguments.

    Returns:
        Exit code 1 when masks have problems.
    """
    config = loop.load_config(args.config)
    image = loop.read_image(config.source)
    masks = loop.build_masks(image, config)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_dir / "overlay.png"), mask_overlay(image, masks, config))
    for name, points in config.protect.items():
        cv2.imwrite(str(out_dir / f"junction_{name}.png"), junction_zoom(image, masks, points))
    for name, mask in masks.groups.items():
        print(f"{name}: {int(mask.sum())} px")
    if masks.problems:
        print("problems:\n  " + "\n  ".join(masks.problems))
        return 1
    scene = loop.prepare_scene(image, config)
    cv2.imwrite(str(out_dir / "plate.png"), np.clip(scene.plate, 0, 255).astype(np.uint8))
    print(f"no mask problems; review {out_dir}")
    return 0


def encoder_args(output: Path, frame_count: int) -> List[str]:
    """Pick lossless FFV1 for .mkv and loop-friendly H.264 otherwise.

    Args:
        output: Output path.
        frame_count: Frames in one loop, used as the keyframe interval.

    Returns:
        ffmpeg output arguments.
    """
    if output.suffix == C.LOSSLESS_SUFFIX:
        return list(C.LOSSLESS_ARGS)
    return ["-c:v", "libx264", "-preset", "slow", "-crf", str(C.H264_CRF), "-tune", "grain",
            "-x264-params", f"ipratio=1.0:keyint={frame_count}",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart"]


def command_render(args: argparse.Namespace) -> int:
    """Render one seamless loop through ffmpeg.

    Args:
        args: Parsed arguments.

    Returns:
        Exit code.

    Raises:
        SystemExit: When ffmpeg is missing or fails.
    """
    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg not found on PATH")
    config = loop.load_config(args.config)
    image = loop.read_image(config.source)
    scene = loop.prepare_scene(image, config)
    height, width = image.shape[:2]
    output = Path(args.output)
    command = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
               "-s", f"{width}x{height}", "-r", str(config.fps), "-i", "-",
               *encoder_args(output, config.frame_count), str(output)]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    for index in range(config.frame_count):
        process.stdin.write(loop.render_frame(scene, index / config.frame_count).tobytes())
        if index % config.fps == 0:
            print(f"frame {index}/{config.frame_count}", file=sys.stderr, flush=True)
    process.stdin.close()
    if process.wait() != 0:
        raise SystemExit("ffmpeg failed")
    print(f"wrote {output}")
    return 0


def review_sheet(frames: List[np.ndarray], box: Box) -> np.ndarray:
    """Tile one region across sampled loop phases.

    Args:
        frames: Frames sampled across the loop.
        box: Region to tile.

    Returns:
        Horizontal strip of tiles.
    """
    x0, y0, x1, y1 = box
    tile_height = max(1, int(C.REVIEW_TILE_WIDTH_PX * (y1 - y0) / max(1, x1 - x0)))
    return np.hstack([cv2.resize(frame[y0:y1, x0:x1], (C.REVIEW_TILE_WIDTH_PX, tile_height)) for frame in frames])


def check_video(config: loop.LoopConfig, video: Path, out_dir: Path) -> List[str]:
    """Measure the loop seam and still regions, and write review images.

    Args:
        config: Loop config used for the render.
        video: Rendered video.
        out_dir: Folder for review images.

    Returns:
        Failed checks; empty when the loop passes.
    """
    image = loop.read_image(config.source)
    protect = loop.polygon_mask(image.shape, config.protect.values())
    reference = loop.apply_watermark(image, loop.watermark_layers(image.shape))
    sample_indices = {round(i * config.frame_count / C.REVIEW_PHASES) for i in range(C.REVIEW_PHASES)}
    capture = cv2.VideoCapture(str(video))
    first: Optional[np.ndarray] = None
    previous: Optional[np.ndarray] = None
    steps: List[float] = []
    drifts: List[float] = []
    samples: Dict[int, np.ndarray] = {}
    low = high = None
    index = 0
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        current = frame.astype(np.float32)
        gray = current.mean(axis=2)
        low = gray if low is None else np.minimum(low, gray)
        high = gray if high is None else np.maximum(high, gray)
        if previous is not None:
            steps.append(float(np.abs(current - previous).mean()))
        if first is None:
            first = current
        if protect.any() and index % config.fps == 0:
            drifts.append(float(np.abs(current[protect] - reference[protect]).mean()))
        if index in sample_indices:
            samples[index] = frame
        previous = current
        index += 1
    capture.release()
    if first is None or len(steps) < 2:
        return [f"could not decode frames from {video}"]

    out_dir.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_dir / "motion_range.png"), np.clip((high - low) * C.MOTION_RANGE_GAIN, 0, 255).astype(np.uint8))
    frames = [samples[i] for i in sorted(samples)]
    cv2.imwrite(str(out_dir / "frame_mid.png"), frames[len(frames) // 2])
    for name, points in config.protect.items():
        cv2.imwrite(str(out_dir / f"sheet_{name}.png"), review_sheet(frames, polygon_box(points, image.shape)))

    failures: List[str] = []
    seam_ratio = float(np.abs(first - previous).mean()) / statistics.median(steps)
    max_drift = max(drifts, default=0.0)
    print(f"frames: {index} (expected {config.frame_count})")
    print(f"seam ratio: {seam_ratio:.2f} (max {C.SEAM_RATIO_MAX})")
    print(f"protected drift: {max_drift:.2f} (max {C.PROTECTED_DRIFT_MAX})")
    if index != config.frame_count:
        failures.append(f"decoded {index} frames, expected {config.frame_count}")
    if seam_ratio > C.SEAM_RATIO_MAX:
        failures.append(f"loop seam jumps {seam_ratio:.2f}x a normal frame step")
    if max_drift > C.PROTECTED_DRIFT_MAX:
        failures.append(f"protected regions changed by {max_drift:.2f} on average")
    return failures


def command_check(args: argparse.Namespace) -> int:
    """Run loop checks and print failures.

    Args:
        args: Parsed arguments.

    Returns:
        Exit code 1 when any check fails.
    """
    failures = check_video(loop.load_config(args.config), Path(args.video), Path(args.out_dir))
    if failures:
        print("failed:\n  " + "\n  ".join(failures))
        return 1
    print(f"passed; review images in {args.out_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser.

    Returns:
        Parser with all subcommands.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    grid = commands.add_parser("grid", help="write crops with a pixel grid")
    grid.add_argument("image")
    grid.add_argument("out_dir")
    grid.add_argument("--box", type=parse_box, action="append", help="X0,Y0,X1,Y1; repeatable")
    grid.set_defaults(run=command_grid)
    masks = commands.add_parser("masks", help="review segmentation")
    masks.add_argument("config")
    masks.add_argument("out_dir")
    masks.set_defaults(run=command_masks)
    render = commands.add_parser("render", help="render the loop")
    render.add_argument("config")
    render.add_argument("output")
    render.set_defaults(run=command_render)
    check = commands.add_parser("check", help="check a rendered loop")
    check.add_argument("config")
    check.add_argument("video")
    check.add_argument("out_dir")
    check.set_defaults(run=command_check)
    return parser


def main() -> int:
    """Run the selected subcommand.

    Returns:
        Exit code.
    """
    args = build_parser().parse_args()
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
