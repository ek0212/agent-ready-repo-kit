"""Shared limits and labels for deck.py."""

NOTE_POINTS_MIN = 5
NOTE_POINTS_MAX = 8
MAX_NOTE_POINT_WORDS = 12
BOLD_MARKER = "**"

VISUALS_PER_DRAFT_SLIDE = 5
MAX_SENTENCES_PER_VISUAL = 2
MAX_HEADING_WORDS = 8

MD_SLIDE_PREFIX = "## Slide"
MD_VISUALS_HEADING = "### Visuals"
MD_NOTES_HEADING = "### Speaker notes"
TAKEAWAY_PREFIX = "In short:"

THEME_FONT_REFS = {"+mj-lt", "+mn-lt", "+mj-ea", "+mn-ea", "+mj-cs", "+mn-cs"}
SZ_UNITS_PER_PT = 100

MSG_VISUAL_COUNT = "slide {n}: expected {expected} candidate visuals, got {actual}"
MSG_VISUAL_SENTENCES = "slide {n} visual {v}: {count} sentences, max {limit}"
MSG_HEADING_WORDS = "slide {n}: heading has {count} words, max {limit}"
MSG_NOTES_EMPTY = "slide {n}: speaker notes are empty"
MSG_NOTES_NOT_BULLETS = "slide {n}: speaker notes must be bullet points"
MSG_NO_TAKEAWAY = "last slide: notes need a bullet starting 'In short:'"
MSG_POINT_COUNT = "slide {n}: {count} talking points, target {low}-{high} for ~1 minute"
MSG_POINT_TOO_LONG = "slide {n} point {p}: {count} words, max {limit}; write a point to cover, not a sentence"
MSG_POINT_SENTENCE = "slide {n} point {p}: ends with a period, likely a full sentence"
MSG_NO_BOLD = "slide {n}: no **bold** key term in notes"
MSG_NO_SELECTION = "slide {n}: no visual selected"
MSG_FONT = "slide {n}: font '{value}' not in template"
MSG_SIZE = "slide {n}: font size {value}pt not in template"
MSG_COLOR = "slide {n}: color #{value} not in template"
MSG_IMAGE = "slide {n}: image '{value}' not sourced from template"
MSG_SLIDE_COUNT = "deck has {actual} slides, selections have {expected}"
