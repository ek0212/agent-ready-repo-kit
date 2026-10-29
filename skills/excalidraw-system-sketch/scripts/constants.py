"""Shared limits, styles, and lookup paths for the excalidraw-system-sketch scripts."""

FONT_HELVETICA = 2
BODY_FONT_SIZE = 16
TITLE_FONT_SIZE = 20
BADGE_FONT_SIZE = 14
LINE_HEIGHT = 1.25

# Excalidraw insets text bound to a shape by this many pixels on each side.
BOUND_TEXT_PADDING = 5
# Excalidraw wraps arrow labels at max(0.7 * arrow width, 11 * font size).
ARROW_LABEL_WIDTH_FRACTION = 0.7
ARROW_LABEL_MIN_WIDTH_PER_FONT_PX = 11

BOX_TEXT_MARGIN = 40
BOX_VERTICAL_MARGIN = 36
ITEM_ICON_SIZE = 44
ITEM_ICON_GAP = 12
ZONE_ICON_SIZE = 30
ZONE_ICON_INSET = 14
BADGE_SIZE = 28
ARROW_GAP = 6

INK = "#1e1e1e"
MUTED = "#868e96"
WHITE = "#ffffff"
TRANSPARENT = "transparent"
NOTE_STROKE = "#f08c00"
NOTE_FILL = "#fff3bf"
OWNER_COLORS = {
    "blue": ("#1971c2", "#e7f5ff"),
    "green": ("#2f9e44", "#ebfbee"),
    "violet": ("#6741d9", "#f3f0ff"),
    "orange": ("#e8590c", "#fff4e6"),
}

LEFT = "left"
CENTER = "center"
TOP = "top"
MIDDLE = "middle"
TRUNCATION_MARKERS = ("...", "\u2026")

IMAGE_MIME_TYPES = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}
ICON_DIRS_ENV = "EXCALIDRAW_ICON_DIRS"
ICON_SEARCH_SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
ICON_SEARCH_LIMIT = 40
VSCODE_EXTENSION_DIRS = (".vscode/extensions", ".vscode-insiders/extensions")
DRAWIO_ICON_GLOBS = (
    "hediet.vscode-drawio-*/drawio/src/main/webapp/img/lib",
    "hediet.vscode-drawio-*/drawio/src/main/webapp/images",
)
EXCALIDRAW_WEBVIEW_GLOB = "pomdtr.excalidraw-editor-*/webview/dist"

BROWSER_CANDIDATES = (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)
BROWSER_COMMANDS = ("microsoft-edge", "google-chrome", "chromium", "chromium-browser")
RENDER_MAX_PIXELS = (3600, 2400)
RENDER_MARGIN = 120
RENDER_TIME_BUDGET_MS = 15000
RENDER_TIMEOUT_SECONDS = 60
RENDER_ATTEMPTS = 2
RENDER_PROFILE_DIR_NAME = "excalidraw-system-sketch-browser-profile"
