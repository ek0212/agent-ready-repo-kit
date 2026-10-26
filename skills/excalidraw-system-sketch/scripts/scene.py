"""Build Excalidraw scenes where every piece of text is bound to a shape or arrow.

Import from a per-diagram build script:

    sys.path.insert(0, "<skill-dir>/scripts")
    from scene import Scene, item_size
"""

import base64
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import constants as C

Element = Dict[str, Any]
Point = Tuple[float, float]


class Scene:
    """Collects elements and embedded image files for one .excalidraw file."""

    def __init__(self) -> None:
        """Start an empty scene."""
        self.elements: List[Element] = []
        self.files: Dict[str, Dict[str, Any]] = {}
        self.by_id: Dict[str, Element] = {}

    def add(self, element_type: str, element_id: str, x: float, y: float, width: float, height: float,
            **fields: Any) -> Element:
        """Add an element with Excalidraw's common fields.

        Args:
            element_type: Excalidraw element type.
            element_id: Unique element ID.
            x: Left edge.
            y: Top edge.
            width: Width.
            height: Height.
            **fields: Type-specific fields and overrides.

        Returns:
            The added element.

        Raises:
            ValueError: If the ID is already used.
        """
        if element_id in self.by_id:
            raise ValueError(f"Duplicate element ID: {element_id}")
        element: Element = {
            "id": element_id, "type": element_type, "x": round(x, 2), "y": round(y, 2),
            "width": round(width, 2), "height": round(height, 2), "angle": 0, "strokeColor": C.INK,
            "backgroundColor": C.TRANSPARENT, "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
            "roughness": 1, "opacity": 100, "groupIds": [], "frameId": None, "roundness": None,
            "seed": stable_seed(element_id), "version": 1, "versionNonce": stable_seed(element_id + "/nonce"),
            "isDeleted": False, "boundElements": [], "updated": 1, "link": None, "locked": False,
        }
        element.update(fields)
        self.elements.append(element)
        self.by_id[element_id] = element
        return element

    def rectangle(self, element_id: str, x: float, y: float, width: float, height: float, stroke: str = C.INK,
                  fill: str = C.WHITE, dashed: bool = False, stroke_width: int = 2,
                  groups: Optional[List[str]] = None) -> Element:
        """Add a rounded rectangle.

        Args:
            element_id: Element ID.
            x: Left edge.
            y: Top edge.
            width: Width.
            height: Height.
            stroke: Outline color.
            fill: Background color.
            dashed: Whether the outline is dashed.
            stroke_width: Outline width.
            groups: Group IDs.

        Returns:
            The rectangle.
        """
        return self.add("rectangle", element_id, x, y, width, height, strokeColor=stroke, backgroundColor=fill,
                        strokeStyle="dashed" if dashed else "solid", strokeWidth=stroke_width,
                        roundness={"type": 3}, groupIds=groups or [])

    def bind_text(self, container: Element, text: str, font_size: int = C.BODY_FONT_SIZE,
                  font_family: int = C.FONT_HELVETICA, align: str = C.LEFT, vertical: str = C.MIDDLE,
                  color: str = C.INK) -> Element:
        """Bind text to a shape or arrow so it is part of that element.

        Args:
            container: Shape or arrow that owns the text.
            text: Newline-separated text.
            font_size: Font size in pixels.
            font_family: Excalidraw font family ID.
            align: Horizontal alignment.
            vertical: Vertical alignment inside a shape.
            color: Text color.

        Returns:
            The bound text element.
        """
        width, height = text_size(text, font_size, font_family)
        if container["type"] == "arrow":
            width = min(width, arrow_label_max_width(container, font_size))
            mid_x, mid_y = midpoint(container)
            x, y = mid_x - width / 2, mid_y - height / 2
        else:
            width = container["width"] - 2 * C.BOUND_TEXT_PADDING
            x = container["x"] + C.BOUND_TEXT_PADDING
            y = container["y"] + C.BOUND_TEXT_PADDING if vertical == C.TOP else \
                container["y"] + (container["height"] - height) / 2
        text_id = f"{container['id']}_text"
        container["boundElements"].append({"type": "text", "id": text_id})
        return self.add("text", text_id, x, y, width, height, text=text, originalText=text, fontSize=font_size,
                        fontFamily=font_family, textAlign=align, verticalAlign=vertical,
                        containerId=container["id"], lineHeight=C.LINE_HEIGHT, autoResize=True,
                        strokeColor=color, groupIds=list(container["groupIds"]))

    def image(self, element_id: str, path: Path, x: float, y: float, size: float,
              groups: Optional[List[str]] = None) -> Element:
        """Embed an icon file and place it.

        Args:
            element_id: Element ID.
            path: SVG or PNG file.
            x: Left edge.
            y: Top edge.
            size: Width and height.
            groups: Group IDs.

        Returns:
            The image element.

        Raises:
            ValueError: If the file type is not supported.
        """
        mime_type = C.IMAGE_MIME_TYPES.get(path.suffix.lower())
        if mime_type is None:
            raise ValueError(f"Unsupported icon type: {path}")
        file_id = hashlib.sha256(str(path.resolve()).encode()).hexdigest()[:40]
        if file_id not in self.files:
            data = base64.b64encode(path.read_bytes()).decode()
            self.files[file_id] = {"mimeType": mime_type, "id": file_id, "dataURL": f"data:{mime_type};base64,{data}",
                                   "created": 1, "lastRetrieved": 1}
        return self.add("image", element_id, x, y, size, size, status="saved", fileId=file_id, scale=[1, 1],
                        crop=None, strokeColor=C.TRANSPARENT, groupIds=groups or [])

    def zone(self, element_id: str, x: float, y: float, width: float, height: float, title: str,
             stroke: str, fill: str = C.TRANSPARENT, dashed: bool = False, icon: Optional[Path] = None) -> Element:
        """Add a boundary or grouping area with its title bound to the top-left corner.

        Args:
            element_id: Element ID.
            x: Left edge.
            y: Top edge.
            width: Width.
            height: Height.
            title: Title text.
            stroke: Outline color.
            fill: Background color.
            dashed: Whether the outline is dashed, used for trust boundaries.
            icon: Optional icon placed at the top-right corner.

        Returns:
            The zone rectangle.
        """
        groups = [f"{element_id}_group"]
        zone = self.rectangle(element_id, x, y, width, height, stroke, fill, dashed, 2 if dashed else 1, groups)
        self.bind_text(zone, title, C.TITLE_FONT_SIZE, C.FONT_EXCALIFONT, vertical=C.TOP)
        if icon:
            self.image(f"{element_id}_icon", icon, x + width - C.ZONE_ICON_INSET - C.ZONE_ICON_SIZE,
                       y + C.ZONE_ICON_INSET, C.ZONE_ICON_SIZE, groups)
        return zone

    def item(self, element_id: str, x: float, y: float, width: float, height: float, text: str,
             icon: Optional[Path] = None, stroke: str = C.INK, fill: str = C.WHITE) -> Element:
        """Add a box with bound text and an optional icon to its left.

        Args:
            element_id: Element ID.
            x: Left edge of the box. The icon sits in the column to its left.
            y: Top edge.
            width: Width.
            height: Height.
            text: Newline-separated sentences.
            icon: Optional icon file.
            stroke: Outline color.
            fill: Background color.

        Returns:
            The box.
        """
        groups = [f"{element_id}_group"]
        box = self.rectangle(element_id, x, y, width, height, stroke, fill, groups=groups)
        self.bind_text(box, text)
        if icon:
            self.image(f"{element_id}_icon", icon, x - C.ITEM_ICON_SIZE - C.ITEM_ICON_GAP,
                       y + (height - C.ITEM_ICON_SIZE) / 2, C.ITEM_ICON_SIZE, groups)
        return box

    def note(self, element_id: str, x: float, y: float, text: str) -> Element:
        """Add a sticky note sized to its bound text.

        Args:
            element_id: Element ID.
            x: Left edge.
            y: Top edge.
            text: Newline-separated sentences.

        Returns:
            The note box.
        """
        width, height = item_size(text)
        return self.item(element_id, x, y, width, height, text, stroke=C.NOTE_STROKE, fill=C.NOTE_FILL)

    def badge(self, element_id: str, center: Point, label: str, groups: Optional[List[str]] = None) -> Element:
        """Add a numbered circle with its number bound inside.

        Args:
            element_id: Element ID.
            center: Circle center.
            label: Short label, such as a step number.
            groups: Group IDs.

        Returns:
            The circle.
        """
        half = C.BADGE_SIZE / 2
        circle = self.add("ellipse", element_id, center[0] - half, center[1] - half, C.BADGE_SIZE, C.BADGE_SIZE,
                          backgroundColor=C.INK, groupIds=groups or [])
        self.bind_text(circle, label, C.BADGE_FONT_SIZE, align=C.CENTER, color=C.WHITE)
        return circle

    def arrow(self, element_id: str, start: Point, end: Point, dashed: bool = False, source: Optional[str] = None,
              target: Optional[str] = None, label: Optional[str] = None,
              groups: Optional[List[str]] = None) -> Element:
        """Add a straight arrow, bound to its endpoints and with its label bound to it.

        Args:
            element_id: Element ID.
            start: Start point.
            end: End point.
            dashed: Whether the line is dashed.
            source: Element the arrow starts from.
            target: Element the arrow points to.
            label: Optional label. Keep lines short; see arrow_label_max_width.
            groups: Group IDs.

        Returns:
            The arrow.
        """
        dx, dy = end[0] - start[0], end[1] - start[1]
        bindings: Dict[str, Optional[Dict[str, Any]]] = {}
        for key, bound_id in (("startBinding", source), ("endBinding", target)):
            bindings[key] = {"elementId": bound_id, "focus": 0, "gap": C.ARROW_GAP} if bound_id else None
            if bound_id:
                self.by_id[bound_id]["boundElements"].append({"type": "arrow", "id": element_id})
        arrow = self.add("arrow", element_id, start[0], start[1], abs(dx), abs(dy), points=[[0, 0], [dx, dy]],
                         lastCommittedPoint=None, startArrowhead=None, endArrowhead="arrow", elbowed=False,
                         strokeStyle="dashed" if dashed else "solid", roundness={"type": 2},
                         groupIds=groups or [], **bindings)
        if label:
            self.bind_text(arrow, label)
        return arrow

    def line(self, element_id: str, start: Point, end: Point, stroke: str = C.MUTED, dashed: bool = True) -> Element:
        """Add a plain line, such as a swimlane lifeline.

        Args:
            element_id: Element ID.
            start: Start point.
            end: End point.
            stroke: Line color.
            dashed: Whether the line is dashed.

        Returns:
            The line.
        """
        dx, dy = end[0] - start[0], end[1] - start[1]
        return self.add("line", element_id, start[0], start[1], abs(dx), abs(dy), points=[[0, 0], [dx, dy]],
                        lastCommittedPoint=None, startArrowhead=None, endArrowhead=None, strokeColor=stroke,
                        strokeWidth=1, strokeStyle="dashed" if dashed else "solid", startBinding=None, endBinding=None)

    def to_json(self) -> str:
        """Serialize the scene as .excalidraw file content.

        Returns:
            JSON text.
        """
        return json.dumps({"type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
                           "elements": self.elements, "appState": {"gridSize": None, "viewBackgroundColor": C.WHITE},
                           "files": self.files}, indent=2)

    def save(self, path: Path) -> None:
        """Write the scene to disk.

        Args:
            path: Output .excalidraw path.
        """
        path.write_text(self.to_json(), encoding="utf-8")


def text_width(line: str, font_size: int, font_family: int) -> float:
    """Estimate rendered line width so shapes start wide enough.

    Excalidraw re-measures after fonts load, so this only needs to be close.

    Args:
        line: One line of text.
        font_size: Font size in pixels.
        font_family: Excalidraw font family ID.

    Returns:
        Estimated width in pixels.
    """
    if font_family == C.FONT_EXCALIFONT:
        return len(line) * font_size * 0.62
    narrow, wide = set("iljtfrI.,:;'!|/()[]- "), set("mwMW@")
    units = sum(0.3 if ch in narrow else 0.86 if ch in wide else 0.56 for ch in line)
    return units * font_size * 1.05


def text_size(text: str, font_size: int = C.BODY_FONT_SIZE, font_family: int = C.FONT_HELVETICA) -> Tuple[float, float]:
    """Estimate the width and height of newline-separated text.

    Args:
        text: Text with one line per newline.
        font_size: Font size in pixels.
        font_family: Excalidraw font family ID.

    Returns:
        Width and height in pixels.
    """
    lines = text.split("\n")
    width = max(text_width(line, font_size, font_family) for line in lines)
    return width, len(lines) * font_size * C.LINE_HEIGHT


def item_size(text: str) -> Tuple[float, float]:
    """Size a box so its bound body text fits without wrapping.

    Args:
        text: Newline-separated sentences.

    Returns:
        Width and height in pixels.
    """
    width, height = text_size(text)
    return width + C.BOX_TEXT_MARGIN, height + C.BOX_VERTICAL_MARGIN


def arrow_label_max_width(arrow: Element, font_size: int) -> float:
    """Return the width at which Excalidraw wraps a label bound to an arrow.

    Args:
        arrow: Arrow element.
        font_size: Label font size in pixels.

    Returns:
        Maximum label width in pixels.
    """
    return max(C.ARROW_LABEL_WIDTH_FRACTION * arrow["width"], C.ARROW_LABEL_MIN_WIDTH_PER_FONT_PX * font_size)


def stable_seed(value: str) -> int:
    """Derive a stable seed so regenerated files diff cleanly.

    Args:
        value: Element ID or other stable key.

    Returns:
        Positive 31-bit integer.
    """
    return int(hashlib.sha256(value.encode()).hexdigest()[:8], 16) & 0x7FFFFFFF


def midpoint(arrow: Element) -> Point:
    """Return the midpoint of a straight arrow.

    Args:
        arrow: Arrow element.

    Returns:
        Midpoint coordinates.
    """
    (x0, y0), (x1, y1) = arrow["points"][0], arrow["points"][-1]
    return arrow["x"] + (x0 + x1) / 2, arrow["y"] + (y0 + y1) / 2


def check_scene(data: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    """Check bindings, embedded files, and text rules in a loaded .excalidraw file.

    Args:
        data: Parsed .excalidraw JSON.

    Returns:
        Errors that must be fixed, and warnings to review.
    """
    errors: List[str] = []
    warnings: List[str] = []
    elements = [e for e in data.get("elements", []) if not e.get("isDeleted")]
    by_id: Dict[str, Element] = {}
    for element in elements:
        if element["id"] in by_id:
            errors.append(f"Duplicate element ID {element['id']}.")
        by_id[element["id"]] = element
    for element in elements:
        if element["type"] == "text":
            check_text(element, by_id, errors, warnings)
        if element["type"] == "image" and element.get("fileId") not in data.get("files", {}):
            errors.append(f"Image {element['id']} has no embedded file.")
        check_back_references(element, by_id, errors)
    return errors, warnings


def check_text(text: Element, by_id: Dict[str, Element], errors: List[str], warnings: List[str]) -> None:
    """Check that one text element is bound and follows the writing rules.

    Args:
        text: Text element.
        by_id: All live elements keyed by ID.
        errors: Error list to extend.
        warnings: Warning list to extend.
    """
    container = by_id.get(text.get("containerId") or "")
    if container is None:
        errors.append(f"Text {text['id']} is a separate text box. Bind it to a shape or arrow.")
        return
    if {"type": "text", "id": text["id"]} not in (container.get("boundElements") or []):
        errors.append(f"Shape {container['id']} does not list its text {text['id']} in boundElements.")
    if any(marker in text["text"] for marker in C.TRUNCATION_MARKERS):
        warnings.append(f"Text {text['id']} looks truncated. Write values in full.")
    if container["type"] != "ellipse" and text.get("textAlign") != C.LEFT:
        warnings.append(f"Text {text['id']} is not left-aligned.")
    if container["type"] == "arrow":
        max_width = arrow_label_max_width(container, text["fontSize"])
        widest = max(text_width(line, text["fontSize"], text["fontFamily"]) for line in text["originalText"].split("\n"))
        if widest > max_width:
            warnings.append(f"Label {text['id']} will wrap at about {max_width:.0f}px. Shorten its lines.")


def check_back_references(element: Element, by_id: Dict[str, Element], errors: List[str]) -> None:
    """Check that bindings listed on an element point back to it.

    Args:
        element: Any element.
        by_id: All live elements keyed by ID.
        errors: Error list to extend.
    """
    for ref in element.get("boundElements") or []:
        other = by_id.get(ref["id"])
        if other is None:
            errors.append(f"{element['id']} lists missing element {ref['id']}.")
        elif ref["type"] == "text" and other.get("containerId") != element["id"]:
            errors.append(f"Text {ref['id']} does not point back to {element['id']}.")
        elif ref["type"] == "arrow" and element["id"] not in arrow_ends(other):
            errors.append(f"Arrow {ref['id']} is not bound to {element['id']}.")
    if element["type"] == "arrow":
        for bound_id in arrow_ends(element):
            if bound_id not in by_id:
                errors.append(f"Arrow {element['id']} is bound to missing element {bound_id}.")


def arrow_ends(arrow: Element) -> List[str]:
    """Return the IDs an arrow is bound to.

    Args:
        arrow: Arrow element.

    Returns:
        Bound element IDs.
    """
    return [binding["elementId"] for binding in (arrow.get("startBinding"), arrow.get("endBinding")) if binding]
