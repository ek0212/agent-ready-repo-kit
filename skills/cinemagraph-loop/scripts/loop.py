"""Build cloud masks, a clean background plate, and seamless looping frames.

Import from cinemagraph.py or a test:

    sys.path.insert(0, "<skill-dir>/scripts")
    import loop
"""

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import cv2
import numpy as np
from scipy import ndimage as ndi

import constants as C

Point = Tuple[int, int]
Polygon = List[Point]
WatermarkLayers = Tuple[np.ndarray, np.ndarray]

TAU = 2 * math.pi


@dataclass
class GroupMotion:
    """Drift for one group. Amplitudes are pixels; phases are fractions of the loop."""

    amp_x: float
    amp_y: float
    billow: float
    phase_x: float
    phase_y: float


@dataclass
class LoopConfig:
    """Everything needed to render one image as a loop."""

    source: Path
    seeds: Dict[str, List[Point]]
    motion: Dict[str, GroupMotion]
    protect: Dict[str, Polygon]
    layer_order: List[str]
    fps: int = C.FPS
    loop_seconds: float = C.LOOP_SECONDS
    light_saturation_max: int = C.LIGHT_SATURATION_MAX
    background_saturation_min: int = C.BACKGROUND_SATURATION_MIN
    movable_mask: Optional[Path] = None

    @property
    def frame_count(self) -> int:
        """Number of frames in one loop."""
        return int(round(self.fps * self.loop_seconds))


@dataclass
class Masks:
    """Segmentation result for one image."""

    silhouette: np.ndarray
    protect: np.ndarray
    groups: Dict[str, np.ndarray]
    problems: List[str]


@dataclass
class GroupField:
    """Per-pixel motion weight, compositing alpha, and drift settings for one group."""

    weight: np.ndarray
    alpha: np.ndarray
    center: Tuple[float, float]
    motion: GroupMotion


@dataclass
class Scene:
    """Precomputed inputs for rendering any frame of the loop."""

    image: np.ndarray
    plate: np.ndarray
    fields: Dict[str, GroupField]
    order: List[str]
    grid_x: np.ndarray
    grid_y: np.ndarray
    watermark: WatermarkLayers


def load_config(path: Path) -> LoopConfig:
    """Read a loop config JSON file. Relative paths resolve from the config folder.

    Args:
        path: Config file path.

    Returns:
        Parsed config with default motion filled in.

    Raises:
        ValueError: When groups, seeds, or layer_order are missing or inconsistent.
    """
    path = Path(path)
    raw = json.loads(path.read_text())
    base = path.resolve().parent
    groups = raw.get("groups") or {}
    if not groups:
        raise ValueError("config needs at least one entry in 'groups'")
    seeds: Dict[str, List[Point]] = {}
    motion: Dict[str, GroupMotion] = {}
    for index, (name, spec) in enumerate(groups.items()):
        if not spec.get("seeds"):
            raise ValueError(f"group '{name}' needs at least one seed")
        seeds[name] = [(int(x), int(y)) for x, y in spec["seeds"]]
        motion[name] = group_motion(spec, index)
    layer_order = list(raw.get("layer_order", []))
    if layer_order and sorted(layer_order) != sorted(groups):
        raise ValueError("layer_order must list every group exactly once")
    mask = raw.get("movable_mask")
    return LoopConfig(
        source=base / raw["source"],
        seeds=seeds,
        motion=motion,
        protect={name: [(int(x), int(y)) for x, y in pts] for name, pts in raw.get("protect", {}).items()},
        layer_order=layer_order,
        fps=int(raw.get("fps", C.FPS)),
        loop_seconds=float(raw.get("loop_seconds", C.LOOP_SECONDS)),
        light_saturation_max=int(raw.get("light_saturation_max", C.LIGHT_SATURATION_MAX)),
        background_saturation_min=int(raw.get("background_saturation_min", C.BACKGROUND_SATURATION_MIN)),
        movable_mask=base / mask if mask else None,
    )


def group_motion(spec: Dict[str, float], index: int) -> GroupMotion:
    """Fill drift settings, spreading default phases so groups do not move in step.

    Args:
        spec: Group entry from the config.
        index: Group position, used for the default phase.

    Returns:
        Drift settings for the group.
    """
    phase = (index * C.GOLDEN_RATIO_FRACTION) % 1.0
    return GroupMotion(
        amp_x=float(spec.get("amp_x", C.DEFAULT_AMP_X)),
        amp_y=float(spec.get("amp_y", C.DEFAULT_AMP_Y)),
        billow=float(spec.get("billow", C.DEFAULT_BILLOW)),
        phase_x=float(spec.get("phase_x", phase)),
        phase_y=float(spec.get("phase_y", (phase + C.DEFAULT_PHASE_Y_OFFSET) % 1.0)),
    )


def read_image(path: Path) -> np.ndarray:
    """Read a BGR image.

    Args:
        path: Image file path.

    Returns:
        BGR uint8 array.

    Raises:
        FileNotFoundError: When the file cannot be read as an image.
    """
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"could not read image {path}")
    return image


def smoothstep(values: np.ndarray) -> np.ndarray:
    """Ease values from 0 to 1 with zero slope at both ends.

    Args:
        values: Input array; values outside 0..1 are clipped.

    Returns:
        Eased array.
    """
    clipped = np.clip(values, 0.0, 1.0)
    return clipped * clipped * (3 - 2 * clipped)


def disk(radius: int) -> np.ndarray:
    """Return an elliptical structuring element with the given radius.

    Args:
        radius: Radius in pixels.

    Returns:
        Kernel for OpenCV morphology.
    """
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * radius + 1, 2 * radius + 1))


def light_silhouette(image: np.ndarray, saturation_max: int) -> np.ndarray:
    """Find light shapes, closing hatch lines and small holes inside them.

    Args:
        image: BGR image.
        saturation_max: Highest HSV saturation counted as light.

    Returns:
        Boolean mask of light shapes.
    """
    saturation = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[..., 1]
    light = cv2.GaussianBlur((saturation < saturation_max).astype(np.float32), (0, 0), C.LIGHT_BLUR_SIGMA)
    closed = cv2.morphologyEx((light > C.LIGHT_BLUR_THRESHOLD).astype(np.uint8), cv2.MORPH_CLOSE,
                              disk(C.CLOSE_KERNEL_PX // 2)).astype(bool)
    holes = ndi.binary_fill_holes(closed) & ~closed
    hole_labels, count = ndi.label(holes)
    sizes = ndi.sum(holes, hole_labels, range(1, count + 1))
    small_holes = np.isin(hole_labels, np.nonzero(sizes < C.MAX_FILLED_HOLE_AREA_PX)[0] + 1)
    return closed | small_holes


def movable_silhouette(image: np.ndarray, config: LoopConfig) -> np.ndarray:
    """Return the user mask when given, otherwise the detected light shapes.

    Args:
        image: BGR image.
        config: Loop config.

    Returns:
        Boolean mask of pixels that may move.

    Raises:
        ValueError: When the mask size does not match the image.
    """
    if config.movable_mask is None:
        return light_silhouette(image, config.light_saturation_max)
    mask = cv2.imread(str(config.movable_mask), cv2.IMREAD_GRAYSCALE)
    if mask is None or mask.shape != image.shape[:2]:
        raise ValueError(f"movable_mask must be a grayscale image the same size as {config.source.name}")
    return mask > C.MASK_FILE_THRESHOLD


def polygon_mask(shape: Tuple[int, ...], polygons: Iterable[Polygon]) -> np.ndarray:
    """Rasterize filled polygons.

    Args:
        shape: Image shape; only height and width are used.
        polygons: Polygons as lists of (x, y) points.

    Returns:
        Boolean mask covering every polygon.
    """
    mask = np.zeros(shape[:2], np.uint8)
    for points in polygons:
        cv2.fillPoly(mask, [np.array(points, np.int32)], 1)
    return mask.astype(bool)


def drop_thin_lines(mask: np.ndarray) -> np.ndarray:
    """Remove thin strokes, such as ring outlines, that merged into a group.

    Args:
        mask: Boolean group mask.

    Returns:
        Mask without strokes thinner than the opening kernel.
    """
    raw = mask.astype(np.uint8)
    body = cv2.morphologyEx(raw, cv2.MORPH_OPEN, disk(C.THIN_LINE_OPEN_KERNEL_PX // 2))
    return (raw & cv2.dilate(body, disk(C.THIN_LINE_REGROW_PX))).astype(bool)


def build_masks(image: np.ndarray, config: LoopConfig) -> Masks:
    """Split movable shapes into named groups using seeds and protect polygons.

    Args:
        image: BGR image.
        config: Loop config.

    Returns:
        Masks plus problems such as off-shape seeds or groups that share a region.
    """
    height, width = image.shape[:2]
    silhouette = movable_silhouette(image, config)
    protect = polygon_mask(image.shape, config.protect.values())
    labels, _ = ndi.label(silhouette & ~protect)
    owners: Dict[int, str] = {}
    problems: List[str] = []
    groups: Dict[str, np.ndarray] = {}
    for name, seeds in config.seeds.items():
        ids = set()
        for x, y in seeds:
            if not (0 <= x < width and 0 <= y < height):
                problems.append(f"{name}: seed ({x}, {y}) is outside the image")
                continue
            label = int(labels[y, x])
            if label == 0:
                problems.append(f"{name}: seed ({x}, {y}) is not on a movable shape")
                continue
            if owners.get(label, name) != name:
                problems.append(f"{name} and {owners[label]} share one region; add a protect polygon where they touch")
            owners[label] = name
            ids.add(label)
        groups[name] = drop_thin_lines(np.isin(labels, list(ids)))
        if not groups[name].any():
            problems.append(f"{name}: group is empty")
    return Masks(silhouette, protect, groups, list(dict.fromkeys(problems)))


def build_background_plate(image: np.ndarray, movable: np.ndarray, saturation_min: int) -> np.ndarray:
    """Paint background color plus real background grain over movable pixels.

    Args:
        image: BGR image.
        movable: Pixels to replace.
        saturation_min: Lowest HSV saturation counted as open background.

    Returns:
        Float32 BGR plate.
    """
    saturation = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[..., 1]
    background = (saturation >= saturation_min).astype(np.float32)
    image_f = image.astype(np.float32)
    weight = cv2.GaussianBlur(background, (0, 0), C.BACKGROUND_COLOR_SIGMA) + 1e-4
    color = cv2.GaussianBlur(image_f * background[..., None], (0, 0), C.BACKGROUND_COLOR_SIGMA) / weight[..., None]
    grain = image_f - cv2.GaussianBlur(image_f, (0, 0), C.BACKGROUND_GRAIN_SIGMA)
    deep_background = cv2.erode(background.astype(np.uint8), disk(C.BACKGROUND_SAMPLE_INSET_PX)) > 0

    height, width = background.shape
    ys, xs = np.nonzero(movable)
    filled = np.zeros(len(xs), bool)
    fill_grain = np.zeros((len(xs), 3), np.float32)
    rng = np.random.default_rng(C.RNG_SEED)
    for _ in range(C.BACKGROUND_OFFSET_TRIES):
        radius = rng.uniform(*C.BACKGROUND_OFFSET_RANGE_PX)
        angle = rng.uniform(0, TAU)
        sample_x = np.clip(xs + int(radius * math.cos(angle)), 0, width - 1)
        sample_y = np.clip(ys + int(radius * math.sin(angle)), 0, height - 1)
        usable = ~filled & deep_background[sample_y, sample_x]
        fill_grain[usable] = grain[sample_y[usable], sample_x[usable]]
        filled |= usable

    plate = image_f.copy()
    plate[ys, xs] = color[ys, xs] + fill_grain
    return plate


def build_fields(masks: Masks, motion: Dict[str, GroupMotion]) -> Dict[str, GroupField]:
    """Build per-group motion weights that fade to zero at protect polygons.

    Args:
        masks: Segmentation result.
        motion: Drift settings per group.

    Returns:
        Field per non-empty group.
    """
    reach = max(math.hypot(m.amp_x, m.amp_y) for m in motion.values()) + C.FIELD_MARGIN_PX
    dist_to_pin = cv2.distanceTransform((~masks.protect).astype(np.uint8), cv2.DIST_L2, 5)
    pin_taper = smoothstep(dist_to_pin / C.PIN_TAPER_PX)
    fields: Dict[str, GroupField] = {}
    for name, mask in masks.groups.items():
        if not mask.any():
            continue
        dist_out = cv2.distanceTransform((~mask).astype(np.uint8), cv2.DIST_L2, 5)
        support = smoothstep(1.0 - (dist_out - reach) / C.FIELD_FALLOFF_PX)
        ys, xs = np.nonzero(mask)
        fields[name] = GroupField(
            weight=(support * pin_taper).astype(np.float32),
            alpha=cv2.GaussianBlur(mask.astype(np.float32), (0, 0), C.ALPHA_SOFTEN_SIGMA),
            center=(float(xs.mean()), float(ys.mean())),
            motion=motion[name],
        )
    return fields


def watermark_layers(shape: Tuple[int, ...]) -> WatermarkLayers:
    """Rasterize the attribution watermark for the bottom-right corner.

    Args:
        shape: Frame shape; only height and width are used.

    Returns:
        Text coverage and soft shadow coverage, each 0..1 float32.
    """
    height, width = shape[:2]
    scale = C.WATERMARK_FONT_SCALE_PER_PX * height
    (text_width, _), _ = cv2.getTextSize(C.WATERMARK_TEXT, C.WATERMARK_FONT, scale, 1)
    margin = round(C.WATERMARK_MARGIN_FRACTION * height)
    origin = (width - text_width - margin, height - margin)
    ink = np.zeros((height, width), np.uint8)
    shadow = np.zeros((height, width), np.uint8)
    cv2.putText(ink, C.WATERMARK_TEXT, origin, C.WATERMARK_FONT, scale, 255, 1, cv2.LINE_AA)
    cv2.putText(shadow, C.WATERMARK_TEXT, origin, C.WATERMARK_FONT, scale, 255,
                1 + C.WATERMARK_SHADOW_GROW_PX, cv2.LINE_AA)
    soft_shadow = cv2.GaussianBlur(shadow.astype(np.float32) / 255.0, (0, 0), C.WATERMARK_SHADOW_SIGMA)
    return ink.astype(np.float32) / 255.0, soft_shadow


def apply_watermark(frame: np.ndarray, layers: WatermarkLayers) -> np.ndarray:
    """Draw light text over a soft dark shadow so it reads on sky and cloud.

    Args:
        frame: BGR uint8 or float frame.
        layers: Output of watermark_layers for this frame size.

    Returns:
        Watermarked float32 frame.
    """
    ink, shadow = (layer[..., None] for layer in layers)
    out = frame.astype(np.float32) * (1 - C.WATERMARK_SHADOW_OPACITY * shadow)
    return out * (1 - C.WATERMARK_OPACITY * ink) + 255.0 * C.WATERMARK_OPACITY * ink


def prepare_scene(image: np.ndarray, config: LoopConfig) -> Scene:
    """Precompute masks, plate, and motion fields for rendering.

    Args:
        image: BGR image.
        config: Loop config.

    Returns:
        Scene ready for render_frame.

    Raises:
        ValueError: When the masks have problems that would make the loop tear.
    """
    masks = build_masks(image, config)
    if masks.problems:
        raise ValueError("fix mask problems first:\n" + "\n".join(masks.problems))
    movable = np.zeros(image.shape[:2], np.uint8)
    for mask in masks.groups.values():
        movable |= mask.astype(np.uint8)
    movable = cv2.dilate(movable, disk(C.FILL_DILATE_PX)).astype(bool) & ~masks.protect
    fields = build_fields(masks, config.motion)
    order = config.layer_order or sorted(fields, key=lambda name: fields[name].center[1])
    grid_y, grid_x = np.mgrid[0:image.shape[0], 0:image.shape[1]].astype(np.float32)
    plate = build_background_plate(image, movable, config.background_saturation_min)
    return Scene(image, plate, fields, order, grid_x, grid_y, watermark_layers(image.shape))


def displacement(field: GroupField, phase: float, grid_x: np.ndarray, grid_y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Return per-pixel x and y offsets for one group at a loop phase.

    Every term is a whole-cycle sine of phase, so phase 0 and phase 1 match exactly.

    Args:
        field: Group field.
        phase: Loop position from 0 to 1.
        grid_x: Pixel x coordinates.
        grid_y: Pixel y coordinates.

    Returns:
        Offsets in pixels along x and y.
    """
    motion = field.motion
    drift_x = motion.amp_x * math.sin(TAU * (phase + motion.phase_x))
    drift_y = motion.amp_y * math.sin(TAU * (phase + motion.phase_y))
    swell = motion.billow * math.sin(TAU * (phase + motion.phase_x + C.BILLOW_PHASE_LEAD))
    center_x, center_y = field.center
    offset_x = field.weight * (drift_x + swell * (grid_x - center_x))
    offset_y = field.weight * (drift_y + swell * (grid_y - center_y))
    return offset_x, offset_y


def render_frame(scene: Scene, phase: float) -> np.ndarray:
    """Composite every group over the background plate at one loop phase.

    Args:
        scene: Prepared scene.
        phase: Loop position from 0 to 1.

    Returns:
        Watermarked BGR uint8 frame.
    """
    out = scene.plate.copy()
    for name in scene.order:
        field = scene.fields[name]
        offset_x, offset_y = displacement(field, phase, scene.grid_x, scene.grid_y)
        map_x = scene.grid_x - offset_x
        map_y = scene.grid_y - offset_y
        color = cv2.remap(scene.image, map_x, map_y, cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT_101)
        alpha = cv2.remap(field.alpha, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)[..., None]
        out = alpha * color.astype(np.float32) + (1 - alpha) * out
    return np.clip(apply_watermark(out, scene.watermark), 0, 255).astype(np.uint8)
