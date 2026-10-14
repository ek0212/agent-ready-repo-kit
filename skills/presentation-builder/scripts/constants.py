"""Shared limits and labels for deck.py."""

NOTES_WORDS_MIN = 100
NOTES_WORDS_MAX = 160

VISUALS_PER_DRAFT_SLIDE = 5
MAX_SENTENCES_PER_VISUAL = 2
MAX_HEADING_WORDS = 8

DRAFT_FONT = "Arial"
DRAFT_HEADING_PT = 32
DRAFT_BODY_PT = 16
DRAFT_TEXT_RGB = (0x00, 0x00, 0x00)
DRAFT_BG_RGB = (0xFF, 0xFF, 0xFF)
SLIDE_WIDTH_IN = 13.333
SLIDE_HEIGHT_IN = 7.5
MARGIN_IN = 0.6
HEADING_HEIGHT_IN = 1.2
BLANK_LAYOUT_INDEX = 6

HEADING_SHAPE_NAME = "Heading"
VISUALS_SHAPE_NAME = "Candidate Visuals"
BULLET_PREFIX = "\u2022 "

THEME_FONT_REFS = {"+mj-lt", "+mn-lt", "+mj-ea", "+mn-ea", "+mj-cs", "+mn-cs"}
SZ_UNITS_PER_PT = 100

MSG_VISUAL_COUNT = "slide {n}: expected {expected} candidate visuals, got {actual}"
MSG_VISUAL_SENTENCES = "slide {n} visual {v}: {count} sentences, max {limit}"
MSG_HEADING_WORDS = "slide {n}: heading has {count} words, max {limit}"
MSG_NOTES_EMPTY = "slide {n}: speaker notes are empty"
MSG_NOTES_LENGTH = "slide {n}: notes have {count} words, target {low}-{high} for ~1 minute"
MSG_NO_SELECTION = "slide {n}: no visual selected"
MSG_FONT = "slide {n}: font '{value}' not in template"
MSG_SIZE = "slide {n}: font size {value}pt not in template"
MSG_COLOR = "slide {n}: color #{value} not in template"
MSG_IMAGE = "slide {n}: image '{value}' not sourced from template"
MSG_SLIDE_COUNT = "deck has {actual} slides, selections have {expected}"
