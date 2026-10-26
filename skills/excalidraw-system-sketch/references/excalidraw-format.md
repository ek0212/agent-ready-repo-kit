# Excalidraw format and render notes

Load when writing a build script, reading `sketch.py check` output, or debugging a render. Behavior below was checked against Excalidraw 0.18.1 as bundled in the `pomdtr.excalidraw-editor` 3.9.3 VS Code extension.

## Build script

Import the helpers and let them write bindings:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".agents/skills/excalidraw-system-sketch/scripts"))
import constants as C
from scene import Scene, item_size

scene = Scene()
stroke, fill = C.OWNER_COLORS["blue"]
scene.zone("tenant", 0, 0, 900, 400, "Tenant A, ID 11111111-2222-3333-4444-555555555555", stroke, fill, dashed=True)
text = "This is the API service.\nIt runs in region East US 2."
width, height = item_size(text)
api = scene.item("api", 100, 80, width, height, text, icon=Path("icons/app_service.svg"))
scene.item("db", 100, 260, width, height, "This is the orders database.\nIt stores no secrets.")
scene.arrow("api_to_db", (300, api["y"] + height + 6), (300, 254), source="api", target="db",
            label="The API reads\norders here.")
scene.save(Path("architecture.excalidraw"))
```

Size boxes with `item_size`. Compute positions from sizes so arrows line up with box centers.

## Bound text

Text belongs to a shape when both sides point at each other:

```json
{ "id": "api", "type": "rectangle", "boundElements": [{ "type": "text", "id": "api_text" }] }
{ "id": "api_text", "type": "text", "containerId": "api", "textAlign": "left", "verticalAlign": "middle" }
```

- Excalidraw insets shape text by 5px on each side. Shape text wraps at the shape width minus 10px.
- `verticalAlign` accepts `top`, `middle`, or `bottom`. Zone titles use `top`.
- Arrow labels use the same `containerId` link with the arrow. They wrap at `max(0.7 * arrow width, 11 * fontSize)` and sit centered on the arrow.
- `check` reports any text without a container as a separate text box.

## Arrows

- `startBinding` and `endBinding` hold `{ "elementId": ..., "focus": 0, "gap": 6 }`.
- Each bound shape lists `{ "type": "arrow", "id": ... }` in `boundElements`.
- Arrows can bind to images, so an arrow may end at an item's icon.

## Images

Images reference an entry in the top-level `files` map:

```json
{ "id": "api_icon", "type": "image", "fileId": "<sha>", "status": "saved", "scale": [1, 1] }
"files": { "<sha>": { "id": "<sha>", "mimeType": "image/svg+xml", "dataURL": "data:image/svg+xml;base64,..." } }
```

SVG and PNG both work. `check` fails when an image has no `files` entry.

## Fonts

| `fontFamily` | Font | Use |
| --- | --- | --- |
| 2 | Helvetica | Body text, IDs, URLs |
| 5 | Excalifont | Zone titles and headers |

The extension does not bundle Excalifont. Excalidraw fetches it at runtime, so offline renders may show a fallback font.

## Render harness

`sketch.py render` serves the extension's `webview/dist` on 127.0.0.1. It passes the file as base64 JSON in `data-excalidraw-config` and stubs `acquireVsCodeApi`.

- The extension centers the drawing at 100% zoom and ignores a saved zoom. The script sizes the browser window to the drawing and lowers the device scale factor for large drawings.
- The browser gets its own profile so it never attaches to an open window.
- A brand-new profile can hang on first start on managed Windows machines. The script reuses one profile in the temp folder and retries once.
- Browser output goes to `DEVNULL`. Capturing it hangs, because browser helper processes keep the pipes open.

## Viewing outside VS Code

Azure DevOps and GitHub Markdown cannot show `.excalidraw` files. Export a PNG or `.excalidraw.svg` from the editor and link that file.
