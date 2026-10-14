# /// script
# requires-python = ">=3.10"
# dependencies = ["python-pptx>=1.0"]
# ///
"""Deck helpers for the presentation-builder skill.

Subcommands:
  draft SPEC.json OUT.pptx        Build black-and-white draft deck from approved script.
  selections DRAFT.pptx           Read user-edited draft into selections JSON.
  inspect TEMPLATE.pptx           Print template fonts, sizes, colors, layouts, and icons.
  check FINAL.pptx TEMPLATE.pptx  Verify final deck uses only template styling and assets.
"""

import argparse
import hashlib
import json
import re
import sys

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.util import Inches, Pt

import constants as C

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def count_words(text):
    return len(text.split())


def count_sentences(text):
    return len([s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s])


def validate_spec(spec):
    errors, warnings = [], []
    for n, slide in enumerate(spec["slides"], start=1):
        errors += validate_slide_text(n, slide)
        warnings += notes_length_warnings(n, slide.get("notes", ""))
    return errors, warnings


def validate_slide_text(n, slide):
    errors = []
    heading_words = count_words(slide.get("heading", ""))
    if heading_words > C.MAX_HEADING_WORDS:
        errors.append(C.MSG_HEADING_WORDS.format(n=n, count=heading_words, limit=C.MAX_HEADING_WORDS))
    visuals = slide.get("visuals", [])
    if len(visuals) != C.VISUALS_PER_DRAFT_SLIDE:
        errors.append(C.MSG_VISUAL_COUNT.format(n=n, expected=C.VISUALS_PER_DRAFT_SLIDE, actual=len(visuals)))
    for v, visual in enumerate(visuals, start=1):
        sentences = count_sentences(visual)
        if sentences > C.MAX_SENTENCES_PER_VISUAL:
            errors.append(C.MSG_VISUAL_SENTENCES.format(n=n, v=v, count=sentences, limit=C.MAX_SENTENCES_PER_VISUAL))
    if not slide.get("notes", "").strip():
        errors.append(C.MSG_NOTES_EMPTY.format(n=n))
    return errors


def notes_length_warnings(n, notes):
    words = count_words(notes)
    if words and not C.NOTES_WORDS_MIN <= words <= C.NOTES_WORDS_MAX:
        return [C.MSG_NOTES_LENGTH.format(n=n, count=words, low=C.NOTES_WORDS_MIN, high=C.NOTES_WORDS_MAX)]
    return []


def style_run(run, size_pt, bold=False):
    run.font.name = C.DRAFT_FONT
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(*C.DRAFT_TEXT_RGB)


def add_textbox(slide, name, top_in, height_in):
    width_in = C.SLIDE_WIDTH_IN - 2 * C.MARGIN_IN
    box = slide.shapes.add_textbox(Inches(C.MARGIN_IN), Inches(top_in), Inches(width_in), Inches(height_in))
    box.name = name
    box.text_frame.word_wrap = True
    return box.text_frame


def add_draft_slide(prs, slide_spec):
    slide = prs.slides.add_slide(prs.slide_layouts[C.BLANK_LAYOUT_INDEX])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(*C.DRAFT_BG_RGB)
    heading_run = add_textbox(slide, C.HEADING_SHAPE_NAME, C.MARGIN_IN, C.HEADING_HEIGHT_IN).paragraphs[0].add_run()
    heading_run.text = slide_spec["heading"]
    style_run(heading_run, C.DRAFT_HEADING_PT, bold=True)
    body_top = C.MARGIN_IN + C.HEADING_HEIGHT_IN
    body = add_textbox(slide, C.VISUALS_SHAPE_NAME, body_top, C.SLIDE_HEIGHT_IN - body_top - C.MARGIN_IN)
    for i, visual in enumerate(slide_spec["visuals"]):
        paragraph = body.paragraphs[0] if i == 0 else body.add_paragraph()
        run = paragraph.add_run()
        run.text = C.BULLET_PREFIX + visual
        style_run(run, C.DRAFT_BODY_PT)
    slide.notes_slide.notes_text_frame.text = slide_spec["notes"]


def build_draft(spec, out_path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(C.SLIDE_WIDTH_IN), Inches(C.SLIDE_HEIGHT_IN)
    for slide_spec in spec["slides"]:
        add_draft_slide(prs, slide_spec)
    prs.save(out_path)


def shape_text_by_name(slide, name):
    for shape in slide.shapes:
        if shape.name == name and shape.has_text_frame:
            return shape.text_frame
    return None


def read_selections(path):
    slides, issues = [], []
    for n, slide in enumerate(Presentation(path).slides, start=1):
        heading = shape_text_by_name(slide, C.HEADING_SHAPE_NAME)
        body = shape_text_by_name(slide, C.VISUALS_SHAPE_NAME)
        paragraphs = [p.text.strip() for p in body.paragraphs] if body else []
        visuals = [p.removeprefix(C.BULLET_PREFIX.strip()).strip() for p in paragraphs if p]
        notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
        if not visuals:
            issues.append(C.MSG_NO_SELECTION.format(n=n))
        slides.append({"heading": heading.text.strip() if heading else "", "selected_visuals": visuals, "notes": notes})
    return {"slides": slides, "issues": issues}


def theme_xml(prs):
    return etree.fromstring(prs.slide_masters[0].part.part_related_by(RT.THEME).blob)


def theme_colors(theme):
    colors = {}
    for slot in theme.find(".//a:clrScheme", NS):
        value = slot[0].get("lastClr") or slot[0].get("val")
        colors[etree.QName(slot).localname] = value.upper()
    return colors


def theme_fonts(theme):
    return {kind: theme.find(f".//a:fontScheme/a:{kind}/a:latin", NS).get("typeface") for kind in ("majorFont", "minorFont")}


def scan_styles(xml):
    fonts = {el.get("typeface") for el in xml.iterfind(".//a:latin", NS)} - C.THEME_FONT_REFS
    sizes = {int(el.get("sz")) / C.SZ_UNITS_PER_PT for el in xml.iter() if el.get("sz") and etree.QName(el).localname in ("rPr", "defRPr", "endParaRPr")}
    colors = {el.get("val").upper() for el in xml.iterfind(".//a:srgbClr", NS)}
    return fonts, sizes, colors


def image_hashes(part):
    return {hashlib.sha1(rel.target_part.blob).hexdigest(): rel.target_part.partname for rel in part.rels.values() if rel.reltype == RT.IMAGE}


def template_parts(prs):
    for master in prs.slide_masters:
        yield "master", master
        for layout in master.slide_layouts:
            yield f"layout '{layout.name}'", layout
    for n, slide in enumerate(prs.slides, start=1):
        yield f"slide {n}", slide


ICON_KINDS = {MSO_SHAPE_TYPE.PICTURE: "picture", MSO_SHAPE_TYPE.GROUP: "group", MSO_SHAPE_TYPE.FREEFORM: "freeform"}


def safe_shape_type(shape):
    try:
        return shape.shape_type
    except NotImplementedError:
        return None


def icon_entries(source, container):
    typed = [(s, safe_shape_type(s)) for s in container.shapes]
    return [{"source": source, "name": s.name, "kind": ICON_KINDS[t], "shape_id": s.shape_id} for s, t in typed if t in ICON_KINDS]


def layout_entries(prs):
    return [
        {"name": layout.name, "placeholders": [{"idx": ph.placeholder_format.idx, "type": str(ph.placeholder_format.type), "name": ph.name} for ph in layout.placeholders]}
        for layout in prs.slide_layouts
    ]


def inspect_template(path):
    prs = Presentation(path)
    theme = theme_xml(prs)
    fonts, sizes, colors, images, icons = set(theme_fonts(theme).values()), set(), set(theme_colors(theme).values()), {}, []
    for source, container in template_parts(prs):
        part_fonts, part_sizes, part_colors = scan_styles(container.part._element)
        fonts |= part_fonts
        sizes |= part_sizes
        colors |= part_colors
        images |= image_hashes(container.part)
        icons += icon_entries(source, container)
    return {
        "theme_fonts": theme_fonts(theme),
        "theme_colors": theme_colors(theme),
        "fonts": sorted(fonts),
        "sizes_pt": sorted(sizes),
        "colors": sorted(colors),
        "layouts": layout_entries(prs),
        "icons": icons,
        "images": {h: str(p) for h, p in images.items()},
    }


def check_slide(n, slide, allowed):
    fonts, sizes, colors = scan_styles(slide.part._element)
    issues = [C.MSG_FONT.format(n=n, value=f) for f in sorted(fonts - set(allowed["fonts"]))]
    issues += [C.MSG_SIZE.format(n=n, value=s) for s in sorted(sizes - set(allowed["sizes_pt"]))]
    issues += [C.MSG_COLOR.format(n=n, value=c) for c in sorted(colors - set(allowed["colors"]))]
    issues += [C.MSG_IMAGE.format(n=n, value=p) for h, p in image_hashes(slide.part).items() if h not in allowed["images"]]
    notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
    if not notes.strip():
        issues.append(C.MSG_NOTES_EMPTY.format(n=n))
    return issues


def check_final(final_path, template_path, selections_path=None):
    allowed = inspect_template(template_path)
    slides = list(Presentation(final_path).slides)
    issues = [issue for n, slide in enumerate(slides, start=1) for issue in check_slide(n, slide, allowed)]
    if selections_path:
        expected = len(json.load(open(selections_path))["slides"])
        if expected != len(slides):
            issues.append(C.MSG_SLIDE_COUNT.format(actual=len(slides), expected=expected))
    return issues


def report(issues, warnings=()):
    for line in warnings:
        print(f"WARN {line}", file=sys.stderr)
    for line in issues:
        print(f"FAIL {line}", file=sys.stderr)
    return 1 if issues else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    draft = sub.add_parser("draft")
    draft.add_argument("spec")
    draft.add_argument("out")
    sub.add_parser("selections").add_argument("draft")
    sub.add_parser("inspect").add_argument("template")
    check = sub.add_parser("check")
    check.add_argument("final")
    check.add_argument("template")
    check.add_argument("--selections")
    args = parser.parse_args(argv)

    if args.command == "draft":
        spec = json.load(open(args.spec))
        errors, warnings = validate_spec(spec)
        if not errors:
            build_draft(spec, args.out)
            print(f"wrote {args.out} ({len(spec['slides'])} slides)")
        return report(errors, warnings)
    if args.command == "selections":
        result = read_selections(args.draft)
        print(json.dumps(result, indent=2))
        return report([], result["issues"])
    if args.command == "inspect":
        print(json.dumps(inspect_template(args.template), indent=2))
        return 0
    issues = check_final(args.final, args.template, args.selections)
    if not issues:
        print("PASS final deck uses only template fonts, sizes, colors, and images; every slide has notes")
    return report(issues)


if __name__ == "__main__":
    sys.exit(main())
