# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Command-line helpers for the excalidraw-system-sketch skill.

Subcommands:
  icons KEYWORD... [--root DIR]        Find product icons in the repo, local bundles, and EXCALIDRAW_ICON_DIRS.
  check FILE.excalidraw                Fail when text is not bound to a shape or arrow, or bindings are broken.
  render FILE.excalidraw OUT.png       Screenshot the file with the VS Code Excalidraw extension's renderer.
"""

import argparse
import base64
import functools
import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path
from typing import Any, List, Optional, Tuple

import constants as C
from scene import check_scene

HARNESS_STUB = (
    "<script>window.acquireVsCodeApi = () => ({postMessage(m) {(window.vscodeMessages ||= []).push(m);},"
    " getState() { return null; }, setState() {}});</script>"
)


class HarnessHandler(http.server.SimpleHTTPRequestHandler):
    """Serves the harness page at / and the extension's webview assets everywhere else."""

    page: bytes = b""

    def do_GET(self) -> None:
        """Return the harness page for the root path, else a static asset."""
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(self.page)))
            self.end_headers()
            self.wfile.write(self.page)
            return
        super().do_GET()

    def log_message(self, *args: Any) -> None:
        """Silence per-request logging."""


def extension_dirs() -> List[Path]:
    """Return VS Code extension folders that exist on this machine.

    Returns:
        Existing extension directories.
    """
    return [Path.home() / d for d in C.VSCODE_EXTENSION_DIRS if (Path.home() / d).is_dir()]


def latest_match(pattern: str) -> Optional[Path]:
    """Find the newest extension folder matching a glob.

    Args:
        pattern: Glob relative to an extension directory.

    Returns:
        Matching path, or None.
    """
    matches = sorted(path for base in extension_dirs() for path in base.glob(pattern) if path.is_dir())
    return matches[-1] if matches else None


def icon_roots(extra_roots: List[str]) -> List[Path]:
    """List folders to search for icons, most project-specific first.

    Args:
        extra_roots: Folders passed with --root.

    Returns:
        Existing folders.
    """
    roots = [Path(r) for r in extra_roots]
    roots += [Path(r) for r in os.environ.get(C.ICON_DIRS_ENV, "").split(os.pathsep) if r]
    roots.append(Path.cwd())
    for pattern in C.DRAWIO_ICON_GLOBS:
        bundle = latest_match(pattern)
        if bundle:
            roots.append(bundle)
    return [root for root in roots if root.is_dir()]


def find_icons(keywords: List[str], roots: List[Path]) -> List[Path]:
    """Find image files whose names contain every keyword.

    Args:
        keywords: Words that must all appear in the file name.
        roots: Folders to search.

    Returns:
        Matching icon paths, capped at ICON_SEARCH_LIMIT.
    """
    words = [word.lower() for word in keywords]
    matches: List[Path] = []
    for root in roots:
        for folder, subfolders, files in os.walk(root):
            subfolders[:] = [d for d in subfolders if d not in C.ICON_SEARCH_SKIP_DIRS]
            for name in files:
                path = Path(folder) / name
                if path.suffix.lower() in C.IMAGE_MIME_TYPES and all(w in path.stem.lower() for w in words):
                    matches.append(path)
                    if len(matches) >= C.ICON_SEARCH_LIMIT:
                        return matches
    return matches


def find_browser(explicit: Optional[str]) -> Path:
    """Locate a Chromium-based browser for headless screenshots.

    Args:
        explicit: Browser path passed with --browser.

    Returns:
        Browser executable.

    Raises:
        FileNotFoundError: If no supported browser is installed.
    """
    candidates = [explicit] if explicit else list(C.BROWSER_CANDIDATES)
    candidates += [shutil.which(command) for command in C.BROWSER_COMMANDS]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return Path(candidate)
    raise FileNotFoundError("No Edge or Chrome found. Pass --browser PATH.")


def render_viewport(scene_data: dict) -> Tuple[int, int, float]:
    """Size the browser window to the whole drawing.

    The extension centers the drawing at 100% zoom and ignores a saved zoom, so the window must hold
    the full drawing. A device scale below 1 keeps large drawings within RENDER_MAX_PIXELS.

    Args:
        scene_data: Parsed .excalidraw JSON.

    Returns:
        Window width and height in CSS pixels, and the device scale factor.
    """
    elements = [e for e in scene_data["elements"] if not e.get("isDeleted")]
    width = max(e["x"] + e["width"] for e in elements) - min(e["x"] for e in elements) + 2 * C.RENDER_MARGIN
    height = max(e["y"] + e["height"] for e in elements) - min(e["y"] for e in elements) + 2 * C.RENDER_MARGIN
    scale = min(1.0, C.RENDER_MAX_PIXELS[0] / width, C.RENDER_MAX_PIXELS[1] / height)
    return int(width), int(height), round(scale, 3)


def harness_page(scene_path: Path, webview: Path, port: int) -> bytes:
    """Build the extension's webview page with a stubbed VS Code API.

    Args:
        scene_path: .excalidraw file to show.
        webview: Extension webview dist folder.
        port: Local server port.

    Returns:
        HTML bytes.
    """
    scene_data = json.loads(scene_path.read_text(encoding="utf-8"))
    config = {"content": list(json.dumps(scene_data).encode()), "contentType": "application/json",
              "name": scene_path.stem, "viewModeEnabled": True, "theme": "light", "langCode": "en"}
    page = (webview / "index.html").read_text(encoding="utf-8")
    page = page.replace("{{data-excalidraw-config}}", base64.b64encode(json.dumps(config).encode()).decode())
    page = page.replace("{{excalidraw-asset-path}}", f"http://127.0.0.1:{port}/")
    return page.replace("<head>", "<head>" + HARNESS_STUB, 1).encode()


def render(scene_path: Path, out_png: Path, browser: Optional[str]) -> None:
    """Screenshot a .excalidraw file using the VS Code extension's Excalidraw build.

    Args:
        scene_path: .excalidraw file.
        out_png: Screenshot path.
        browser: Optional browser path.

    Raises:
        FileNotFoundError: If the extension or a browser is missing.
        RuntimeError: If the browser produced no screenshot.
    """
    webview = latest_match(C.EXCALIDRAW_WEBVIEW_GLOB)
    if webview is None:
        raise FileNotFoundError("Install the pomdtr.excalidraw-editor VS Code extension to render.")
    browser_path = find_browser(browser)
    handler = functools.partial(HarnessHandler, directory=str(webview))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    HarnessHandler.page = harness_page(scene_path, webview, server.server_address[1])
    width, height, scale = render_viewport(json.loads(scene_path.read_text(encoding="utf-8")))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    out_png.unlink(missing_ok=True)
    # A dedicated profile stops the browser from attaching to an open window. It is reused because a
    # brand-new profile can hang on first start; the retry then runs with the initialized profile.
    profile = Path(tempfile.gettempdir()) / C.RENDER_PROFILE_DIR_NAME
    command = [str(browser_path), "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
               "--hide-scrollbars", f"--virtual-time-budget={C.RENDER_TIME_BUDGET_MS}",
               f"--window-size={width},{height}", f"--force-device-scale-factor={scale}",
               f"--screenshot={out_png.resolve()}",
               f"http://127.0.0.1:{server.server_address[1]}/"]
    try:
        for _ in range(C.RENDER_ATTEMPTS):
            try:
                # Capturing output would hang: browser helper processes keep the pipes open after exit.
                subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                               timeout=C.RENDER_TIMEOUT_SECONDS, check=False)
            except subprocess.TimeoutExpired:
                continue
            if out_png.is_file():
                break
    finally:
        server.shutdown()
    if not out_png.is_file():
        raise RuntimeError(f"Browser did not write {out_png} after {C.RENDER_ATTEMPTS} attempts.")


def run_check(scene_path: Path) -> int:
    """Print check results for one file.

    Args:
        scene_path: .excalidraw file.

    Returns:
        Process exit code: 1 when errors exist.
    """
    errors, warnings = check_scene(json.loads(scene_path.read_text(encoding="utf-8")))
    for message in errors:
        print(f"ERROR {message}")
    for message in warnings:
        print(f"WARN  {message}")
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def main() -> int:
    """Parse arguments and run a subcommand.

    Returns:
        Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    icons = commands.add_parser("icons")
    icons.add_argument("keywords", nargs="+")
    icons.add_argument("--root", action="append", default=[])
    check = commands.add_parser("check")
    check.add_argument("file", type=Path)
    render_cmd = commands.add_parser("render")
    render_cmd.add_argument("file", type=Path)
    render_cmd.add_argument("out", type=Path)
    render_cmd.add_argument("--browser")
    args = parser.parse_args()

    if args.command == "icons":
        matches = find_icons(args.keywords, icon_roots(args.root))
        print("\n".join(str(path) for path in matches) or "No icons found. Leave the icon out and list it as open.")
        return 0
    if args.command == "check":
        return run_check(args.file)
    render(args.file, args.out, args.browser)
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
