import json

from pptx import Presentation

import constants as C
import deck

SPEC = {"slides": [{"heading": "Why trunk-based", "visuals": [f"Visual {i}. Signals change." for i in range(5)], "notes": "word " * 130}]}


def test_draft_selections_roundtrip(tmp_path):
    draft = tmp_path / "draft.pptx"
    deck.build_draft(SPEC, draft)
    prs = Presentation(draft)
    body = next(s for s in prs.slides[0].shapes if s.name == C.VISUALS_SHAPE_NAME)
    body.text_frame.paragraphs[0]._p.getparent().remove(body.text_frame.paragraphs[0]._p)
    prs.save(draft)
    result = deck.read_selections(draft)
    assert len(result["slides"][0]["selected_visuals"]) == 4
    assert result["slides"][0]["notes"].strip()


def test_validate_rejects_bad_visuals():
    bad = json.loads(json.dumps(SPEC))
    bad["slides"][0]["visuals"] = ["One. Two. Three."]
    errors, _ = deck.validate_spec(bad)
    assert len(errors) == 2


def test_check_flags_non_template_font(tmp_path):
    template, final = tmp_path / "t.pptx", tmp_path / "f.pptx"
    Presentation().save(template)
    deck.build_draft(SPEC, final)
    assert any("Arial" in issue for issue in deck.check_final(final, template))
