from pptx import Presentation
from pptx.util import Inches

import constants as C
import deck

VISUALS = "\n".join(f"- Visual {i}. Signals change." for i in range(5))
NOTES = "\n".join("- You get a **branch**, your own private copy of the code, to work in safely." for _ in range(7))
NOTES += "\n- In short: you merge small changes daily, so your work ships sooner."


def make_draft(sections):
    blocks = [f"## Slide {n} ({s}): Heading {n}\n\n### Visuals\n{VISUALS}\n\n### Speaker notes\n{NOTES}\n" for n, s in enumerate(sections, start=1)]
    return "# Talk\n\n" + "\n".join(blocks)


DRAFT = make_draft(C.SECTIONS)


def test_parse_validate_and_select():
    slides = deck.parse_draft(DRAFT)
    assert slides[0]["heading"] == "Heading 1" and slides[0]["section"] == "Opening Hook"
    assert deck.validate_draft(slides) == ([], [])
    pruned = deck.parse_draft(DRAFT.replace("- Visual 0. Signals change.\n", "", 1))
    result = deck.read_selections(pruned)
    assert len(result["slides"][0]["selected_visuals"]) == 4
    assert result["slides"][0]["notes"]


def test_validate_rejects_bad_draft():
    bad = deck.parse_draft(DRAFT.replace(VISUALS, "- One. Two. Three.", 1).replace(NOTES, "Prose notes.", 1))
    assert len(deck.validate_draft(bad)[0]) == 3
    swapped = deck.parse_draft(make_draft(["Opening Hook", "Supporting Data/Story", "Core Arguments", "Call to Action"]))
    assert any("out of order" in e for e in deck.validate_draft(swapped)[0])
    preachy = deck.parse_draft(DRAFT.replace("to work in safely.", "to work in. It is simply safe. Done.", 1))
    errors, warnings = deck.validate_draft(preachy)
    assert any("3 sentences" in e for e in errors) and any("simply" in w for w in warnings)


def test_check_flags_non_template_font(tmp_path):
    template, final = tmp_path / "t.pptx", tmp_path / "f.pptx"
    Presentation().save(template)
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    run = slide.shapes.add_textbox(0, 0, Inches(1), Inches(1)).text_frame.paragraphs[0].add_run()
    run.text, run.font.name = "x", "Arial"
    prs.save(final)
    assert any("Arial" in issue for issue in deck.check_final(final, template))
