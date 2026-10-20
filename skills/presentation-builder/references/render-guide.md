# Render Guide

Load at Step 7. Recipes for `python-pptx>=1.0`. Run with `uv run --with python-pptx python render.py`.

## Start From Template

```python
from copy import deepcopy
from io import BytesIO
from pptx import Presentation
from pptx.opc.constants import RELATIONSHIP_TYPE as RT

prs = Presentation("template.pptx")
```

Open the template itself so masters, layouts, theme, fonts, and slide size carry over. Never start from a blank `Presentation()`.

## Harvest Icons Before Removing Sample Slides

Icons on sample slides disappear when those slides are dropped. Copy what you need first.

```python
icons = {}
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.name in wanted_icon_names:
            icons[shape.name] = shape
```

Keep references to the shapes (and their slide parts) until all new slides are built, then drop sample slides last.

## Place A Picture Icon

Reuse the exact image bytes so `deck.py check` can match the hash to the template.

```python
slide.shapes.add_picture(BytesIO(icon.image.blob), icon.left, icon.top, icon.width, icon.height)
```

Resize proportionally only. Keep the template's aspect ratio.

## Place A Vector Or Group Icon

```python
element = deepcopy(icon._element)
slide.shapes._spTree.insert_element_before(element, "p:extLst")
```

If the copied element contains `r:embed` or `r:link` attributes, relate each target image part to the new slide and rewrite the id:

```python
new_rid = slide.part.relate_to(source_slide.part.related_part(old_rid), RT.IMAGE)
```

Recolor vector icons only with template theme colors. Prefer theme color references (`MSO_THEME_COLOR`) over raw RGB.

## Build Content Slides

- Pick the template layout whose placeholder grid fits the selected visual. Use `inspect` output `layouts`.
- Put the approved heading in the title placeholder. Let size and font inherit from the layout.
- Remove unused placeholders: `ph._element.getparent().remove(ph._element)`.
- Position icons and native shapes on the layout's placeholder grid and margins.
- Native charts and shapes are allowed when styled only with template colors, fonts, and sizes.
- Set notes: `slide.notes_slide.notes_text_frame.text = approved_notes`.

## Drop Sample Slides

```python
sld_ids = prs.slides._sldIdLst
for sld_id in list(sld_ids)[:sample_count]:
    prs.part.drop_rel(sld_id.rId)
    sld_ids.remove(sld_id)
prs.save("final.pptx")
```

Add new slides before dropping, then drop the first `sample_count` entries.

## Render For Visual Review

Preferred when LibreOffice exists:

```bash
soffice --headless --convert-to pdf final.pptx
pdftoppm -png -r 60 final.pdf slide
```

Otherwise use a PowerPoint canvas `render_slide` action if the runtime has one, or ask the user to open the deck and confirm.

Inspect each image for overflow, overlap, unreadable icons, low contrast, leftover template text, and empty placeholders.
