# Config Format

Load when writing or debugging a cinemagraph-loop config. One JSON file per image. Relative paths resolve from the config file's folder. Coordinates are source-image pixels, `[x, y]`, origin top-left.

## Example

```json
{
  "source": "toile.png",
  "loop_seconds": 12,
  "groups": {
    "top_left": {"seeds": [[90, 120]]},
    "center": {"seeds": [[840, 600], [1100, 700]], "amp_x": 28, "billow": 0.014},
    "bottom": {"seeds": [[760, 920]], "amp_x": 30, "phase_x": 0.05}
  },
  "protect": {
    "ring_behind_center": [[740, 455], [870, 455], [870, 520], [828, 535], [740, 549]],
    "figure_legs": [[1180, 515], [1370, 515], [1350, 740], [1290, 778], [1188, 560]]
  },
  "layer_order": ["top_left", "center", "bottom"]
}
```

## Top-Level Fields

| Field | Required | Default | Meaning |
|---|---|---|---|
| `source` | yes | | Image to animate. |
| `groups` | yes | | Named cloud groups. Each group drifts as one unit. |
| `protect` | no | none | Named polygons that never move. Cover every junction between still art and a moving shape. |
| `layer_order` | no | top to bottom by group center | Back-to-front drawing order. Must list every group once. Put the frontmost group last. |
| `fps` | no | 30 | Frame rate. |
| `loop_seconds` | no | 12 | Loop length. Longer loops drift more slowly. |
| `light_saturation_max` | no | 80 | HSV saturation below this counts as a movable light shape. Raise it if pale-blue cloud shading is missed. |
| `background_saturation_min` | no | 110 | HSV saturation at or above this counts as open background for the clean plate. |
| `movable_mask` | no | detected | White-on-black PNG, same size as the source. Replaces light-shape detection. |

## Group Fields

| Field | Default | Meaning |
|---|---|---|
| `seeds` | required | Points inside each shape that belongs to the group. One seed per separate shape. |
| `amp_x` | 24 | Peak sideways drift in pixels. About 1.5% of image width reads as a gentle drift. |
| `amp_y` | 6 | Peak vertical bob in pixels. |
| `billow` | 0.012 | Peak swell as a fraction of distance from the group center. 0.012 moves each edge of a 400 px wide cloud about 2.4 px outward. |
| `phase_x` | spread by group index | Where in the loop the drift peaks, from 0 to 1. |
| `phase_y` | `phase_x` + 0.35 | Where in the loop the bob peaks. |

Every motion term completes exactly one cycle per loop, so the last frame flows into the first for any amplitude or phase.

## Protect Polygons

- Cover the still art at the junction plus 5 to 10 px of margin.
- Overlap into the cloud a little. The cut cloud edge sits still near the polygon and fades into full motion 90 px away.
- Use one polygon per junction and name it after what it protects. `masks` and `check` write one zoom per polygon with that name.
- A figure drawn in front of a cloud needs its whole overlapping part covered. A ring passing behind a cloud needs only the stub where it meets the cloud edge.
