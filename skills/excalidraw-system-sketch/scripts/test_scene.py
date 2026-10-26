"""Tests for scene.py binding rules."""

import json

import constants as C
import scene


def test_item_text_bound_both_ways_passes_check() -> None:
    """Item text is bound to its box in both directions, so the scene has no errors."""
    sketch = scene.Scene()
    box = sketch.item("box", 0, 0, 300, 80, "This is one full sentence.")
    text = sketch.by_id["box_text"]

    assert text["containerId"] == "box"
    assert {"type": "text", "id": "box_text"} in box["boundElements"]
    assert scene.check_scene(json.loads(sketch.to_json()))[0] == []


def test_check_scene_separate_text_box_reports_error() -> None:
    """Text placed on a shape without binding is reported as a separate text box."""
    sketch = scene.Scene()
    sketch.rectangle("box", 0, 0, 300, 80)
    sketch.add("text", "loose", 10, 10, 100, 20, text="Loose.", originalText="Loose.", fontSize=16,
               fontFamily=C.FONT_HELVETICA, textAlign=C.LEFT, verticalAlign=C.TOP, containerId=None)

    errors, _ = scene.check_scene(json.loads(sketch.to_json()))

    assert any("loose" in message and "separate text box" in message for message in errors)


def test_zone_and_arrow_labels_bound_to_their_elements() -> None:
    """Zone titles bind to the top-left of the zone and arrow labels bind to the arrow."""
    sketch = scene.Scene()
    sketch.zone("zone", 0, 0, 600, 300, "Tenant", C.INK, dashed=True)
    sketch.item("a", 40, 60, 200, 60, "A.")
    sketch.item("b", 40, 200, 200, 60, "B.")
    sketch.arrow("a_to_b", (140, 126), (140, 194), source="a", target="b", label="A calls B.")

    title = sketch.by_id["zone_text"]
    label = sketch.by_id["a_to_b_text"]

    assert (title["containerId"], title["verticalAlign"], title["textAlign"]) == ("zone", C.TOP, C.LEFT)
    assert label["containerId"] == "a_to_b"
    assert scene.check_scene(json.loads(sketch.to_json()))[0] == []
