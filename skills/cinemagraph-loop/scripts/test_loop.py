"""Tests for loop.py masks and seamless rendering."""

from pathlib import Path
from typing import Dict, List

import cv2
import numpy as np
import pytest

import loop

SKY_BGR = (192, 145, 88)
WHITE_BGR = (245, 248, 250)
BRIDGE: List[loop.Point] = [(140, 100), (180, 100), (180, 140), (140, 140)]
# Protect polygons need a few pixels of margin past the drawn shape.
BRIDGE_PROTECT: List[loop.Point] = [(135, 92), (185, 92), (185, 148), (135, 148)]


def synthetic_config(tmp_path: Path, protect: Dict[str, loop.Polygon]) -> loop.LoopConfig:
    """Write two clouds joined by a white bar, like a figure resting on both clouds.

    Args:
        tmp_path: Folder for the generated image.
        protect: Protect polygons for the config.

    Returns:
        Config with one seed per cloud.
    """
    image = np.full((200, 320, 3), SKY_BGR, np.uint8)
    cv2.ellipse(image, (90, 120), (60, 35), 0, 0, 360, WHITE_BGR, -1)
    cv2.ellipse(image, (230, 120), (60, 35), 0, 0, 360, WHITE_BGR, -1)
    cv2.rectangle(image, BRIDGE[0], BRIDGE[2], WHITE_BGR, -1)
    source = tmp_path / "scene.png"
    cv2.imwrite(str(source), image)
    motion = {name: loop.group_motion({}, index) for index, name in enumerate(["left", "right"])}
    return loop.LoopConfig(source=source, seeds={"left": [(90, 120)], "right": [(230, 120)]},
                           motion=motion, protect=protect, layer_order=[])


@pytest.fixture
def protected_scene(tmp_path: Path) -> loop.Scene:
    """Scene where the bar is protected, so each cloud is its own group.

    Args:
        tmp_path: Pytest temporary folder.

    Returns:
        Prepared scene.
    """
    config = synthetic_config(tmp_path, {"bar": BRIDGE_PROTECT})
    return loop.prepare_scene(loop.read_image(config.source), config)


def test_build_masks_bridged_groups_reports_shared_region(tmp_path: Path) -> None:
    """Two seeds joined by an unprotected bar report a shared region."""
    config = synthetic_config(tmp_path, {})

    masks = loop.build_masks(loop.read_image(config.source), config)

    assert any("share one region" in problem for problem in masks.problems)


def test_render_frame_loop_end_matches_start(protected_scene: loop.Scene) -> None:
    """Phase 1.0 renders the same frame as phase 0.0, so the loop has no seam."""
    first = loop.render_frame(protected_scene, 0.0).astype(int)
    wrapped = loop.render_frame(protected_scene, 1.0).astype(int)

    assert np.abs(first - wrapped).max() <= 1


def test_render_frame_protected_region_stays_still(protected_scene: loop.Scene) -> None:
    """Pixels inside a protect polygon match the watermarked source mid-loop."""
    protect = loop.polygon_mask(protected_scene.image.shape, [BRIDGE_PROTECT])
    reference = loop.apply_watermark(protected_scene.image, protected_scene.watermark)

    frame = loop.render_frame(protected_scene, 0.25).astype(np.float32)

    assert np.abs(frame[protect] - reference[protect]).mean() < 1.0
