"""Shared limits and labels for deck.py."""

NOTE_POINTS_MIN = 5
NOTE_POINTS_MAX = 8
MAX_SENTENCES_PER_NOTE_POINT = 2
MAX_SPOKEN_SENTENCE_WORDS = 20
PAUSE_MARKER = "[pause]"
NOTES_WORDS_MIN = 100
NOTES_WORDS_MAX = 160
BOLD_MARKER = "**"

SECTIONS = ("Opening Hook", "Core Arguments", "Supporting Data/Story", "Call to Action")
TALKING_DOWN_PHRASES = ("simply", "obviously", "basically", "of course", "as you know", "everyone knows", "needless to say")
AUDIENCE_WORDS = {"you", "your", "you're", "you'll", "you've", "yours"}

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
MSG_POINT_COUNT = "slide {n}: {count} bullets, target {low}-{high} for ~1 minute"
MSG_NOTES_LENGTH = "slide {n}: notes have {count} words, target {low}-{high} for ~1 minute"
MSG_POINT_SENTENCES = "slide {n} bullet {p}: {count} sentences, max {limit}; one idea per bullet"
MSG_LONG_SENTENCE = "slide {n} bullet {p}: sentence has {count} words, max {limit} for a spoken voice"
MSG_TALKING_DOWN = "slide {n}: '{value}' can sound condescending"
MSG_NO_AUDIENCE = "slide {n}: notes never address the audience as 'you'; state their benefit"
MSG_SECTION_UNKNOWN = "slide {n}: section '{value}' must be one of: {allowed}"
MSG_SECTION_ORDER = "slide {n}: section '{value}' out of order; flow is {allowed}"
MSG_SECTION_FIRST = "first slide must be section '{value}'"
MSG_SECTION_LAST = "last slide must be section '{value}'"
MSG_SECTION_MISSING = "no slides in section '{value}'"
MSG_NO_BOLD = "slide {n}: no **bold** key term in notes"
MSG_NO_SELECTION = "slide {n}: no visual selected"
MSG_FONT = "slide {n}: font '{value}' not in template"
MSG_SIZE = "slide {n}: font size {value}pt not in template"
MSG_COLOR = "slide {n}: color #{value} not in template"
MSG_IMAGE = "slide {n}: image '{value}' not sourced from template"
MSG_SLIDE_COUNT = "deck has {actual} slides, selections have {expected}"
