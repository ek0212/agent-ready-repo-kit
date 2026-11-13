"""Defaults, thresholds, and encoder settings for the cinemagraph-loop scripts."""

import cv2

FPS = 30
LOOP_SECONDS = 12

# Movable elements: light shapes (clouds, mist, smoke) on a saturated background.
LIGHT_SATURATION_MAX = 80
LIGHT_BLUR_SIGMA = 1.5
LIGHT_BLUR_THRESHOLD = 0.35
CLOSE_KERNEL_PX = 7
MAX_FILLED_HOLE_AREA_PX = 2500
# Removes ring outlines and star rays that touch a cloud.
THIN_LINE_OPEN_KERNEL_PX = 13
THIN_LINE_REGROW_PX = 5
MASK_FILE_THRESHOLD = 127

# Motion field.
DEFAULT_AMP_X = 24.0
DEFAULT_AMP_Y = 6.0
DEFAULT_BILLOW = 0.012
DEFAULT_PHASE_Y_OFFSET = 0.35
GOLDEN_RATIO_FRACTION = 0.618034
# Swell peaks a quarter loop after the drift peak, so the motion reads as a slow roll.
BILLOW_PHASE_LEAD = 0.25
# Motion ramps from zero at a protect polygon to full strength this far away.
PIN_TAPER_PX = 90
FIELD_FALLOFF_PX = 40
FIELD_MARGIN_PX = 8
ALPHA_SOFTEN_SIGMA = 0.7

# Background plate painted behind moving elements.
BACKGROUND_SATURATION_MIN = 110
BACKGROUND_COLOR_SIGMA = 25
BACKGROUND_GRAIN_SIGMA = 3
# Grain samples stay this far inside open background so edges do not leave ghost outlines.
BACKGROUND_SAMPLE_INSET_PX = 9
BACKGROUND_OFFSET_TRIES = 40
BACKGROUND_OFFSET_RANGE_PX = (60, 400)
FILL_DILATE_PX = 2
RNG_SEED = 7

# Watermark required by the skill attribution rule.
WATERMARK_TEXT = "Eve Kazarian"
WATERMARK_FONT = cv2.FONT_HERSHEY_DUPLEX
WATERMARK_FONT_SCALE_PER_PX = 0.00075
WATERMARK_MARGIN_FRACTION = 0.018
WATERMARK_OPACITY = 0.85
WATERMARK_SHADOW_OPACITY = 0.45
WATERMARK_SHADOW_SIGMA = 1.5
WATERMARK_SHADOW_GROW_PX = 2

# Encoding. ipratio=1.0 keeps I-frame and P-frame grain similar so the loop point does not pop.
H264_CRF = 16
LOSSLESS_SUFFIX = ".mkv"
LOSSLESS_ARGS = ["-c:v", "ffv1", "-level", "3"]

# Review and checks.
GRID_FULL_STEP_PX = 100
GRID_ZOOM_SCALE = 3
GRID_ZOOM_STEP_PX = 10
GRID_ZOOM_LABEL_STEP_PX = 50
ZOOM_PAD_PX = 40
ZOOM_MAX_WIDTH_PX = 900
REVIEW_PHASES = 8
REVIEW_TILE_WIDTH_PX = 220
MOTION_RANGE_GAIN = 2.0
# Seam step may be this many times the median frame step. Lossless loops measure 1.0.
SEAM_RATIO_MAX = 1.75
# Mean absolute difference allowed in protect polygons, from codec noise only.
PROTECTED_DRIFT_MAX = 4.0

GROUP_COLORS_BGR = [(60, 60, 255), (60, 200, 60), (255, 120, 40), (0, 220, 255), (255, 0, 200),
                    (200, 255, 0), (120, 0, 255), (0, 140, 255), (255, 255, 0), (180, 120, 255)]
CONTOUR_BGR = (0, 0, 255)
PROTECT_BGR = (0, 200, 0)
LABEL_BGR = (255, 255, 255)
GRID_MAJOR_BGR = (0, 0, 255)
GRID_MINOR_BGR = (0, 230, 0)
