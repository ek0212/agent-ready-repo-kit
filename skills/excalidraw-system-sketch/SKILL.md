---
name: excalidraw-system-sketch
description: Plan, build, and render-check Excalidraw sketches for architecture, auth or data flows, trust boundaries, swimlanes, before-and-after designs, or system maps, with product icons for the services the project uses. Use when user asks for an Excalidraw diagram or .excalidraw file, rough system sketch, spatial grouping, swimlanes, icons on a sketch, or visual exploration that Mermaid cannot express well.
license: MIT
---

Create one readable spatial sketch plus durable Markdown summary. Every piece of text is part of a shape or arrow.

## Scope

Use when placement, grouping, swimlanes, icons, or exploration matters. Use Mermaid for exact sequence, state, dependency, or GitHub-rendered architecture unless user asks for Excalidraw. When user asks for an ordered flow in Excalidraw, draw swimlanes with numbered steps.

## Inputs

- Diagram purpose, audience, and where it will be viewed.
- Components, actors, systems, and flows.
- Trust boundaries, secrets, user data, and external services.
- Products the project uses, for icons.
- Existing `.excalidraw` file or visual conventions, if any.

User or repository owns system facts. Check prose docs against code and config, and cite `file:line` for facts the docs omit. Mark inferred nodes and unresolved flows.

## Workflow

Scripts live in `scripts/` next to this file. Run them with `uv run <skill-dir>/scripts/sketch.py ...`, or with `python` when `uv` is missing. They use only the standard library.

1. State one diagram question.
2. Gather facts from code and config as well as docs. Record each fact's source.
3. List boxes, groups, arrows, boundaries, icons, and annotations.
4. Choose a top-to-bottom flow by default. Use horizontal flow, swimlanes, nested zones, or before/after only when the content clearly reads better that way.
5. Separate internal, external, trusted, and untrusted areas.
6. Label secret and user-data entry points without including secret values.
7. Find icons with `sketch.py icons <keywords>`. Confirm each match is the right product.
8. Write a small build script that imports `scripts/scene.py`. Do not hand-write element JSON. Load [excalidraw-format.md](references/excalidraw-format.md) when writing the build script or debugging a file.
9. Run `sketch.py check <file>.excalidraw`. Fix every error.
10. Run `sketch.py render <file>.excalidraw <file>.png`. Read the PNG. Fix clipped, overlapping, or wrapped text, then rebuild and repeat.
11. Write companion `.md` summary with purpose, components, icon sources, boundaries, flows, assumptions, and open questions.

## Text Rules

- Text inside a shape is part of that shape. Bind it: the text sets `containerId` to the shape, and the shape lists `{ "type": "text", "id": "<text_id>" }` in `boundElements`. Never place a separate text element on top of a shape. `scene.py` does this for items, zones, badges, and arrow labels.
- Zone titles bind to their zone with `verticalAlign: "top"` and `textAlign: "left"`.
- Connector labels bind to their arrow. Excalidraw wraps them at the larger of 70% of the arrow's width or 11 times the font size (176px at 16px), and centers them on the arrow. Break lines short.
- Long step descriptions in swimlanes go in a message box above the arrow.
- Write full sentences. Write every value in full: IDs, URLs, names. Never truncate with `...`.
- Spell out each acronym on first use.
- Left-align text in boxes. Center only badge numbers.
- Use Helvetica (`fontFamily: 2`) for every text element, including titles, zone labels, badges, and arrow labels.

## Icons

- Use official Azure icons or official product icons wherever possible for the services and platforms the project actually uses.
- Use icons to clarify appropriate system and ownership boundaries. For example, place an Azure icon on an Azure tenant, subscription, resource group, virtual network, or service boundary when it improves recognition.
- Source order: icons in the repo, then local bundles that `sketch.py icons` finds, then official vendor icon packs the user downloads to a folder listed in `EXCALIDRAW_ICON_DIRS`.
- Never draw, trace, or approximate a vendor logo. If no official icon exists, leave it out and list it as open.
- Place item icons to the left of the box so bound text keeps the full box width. Zone icons go at the zone's top-right corner.
- Embed icons in the file. Record each icon's source path in the companion summary.

## Drawing Rules

- One concept per sketch.
- Prefer a vertical, top-to-bottom main flow. Keep the primary path visually centered and place branches beside the step where they diverge.
- Every box must represent a component, actor, data store, or boundary that participates in the flow.
- Never add boxed diagram titles, headers, footers, legends, summaries, keys, or decorative annotations. Put that information in the companion Markdown. Put essential relationship details on the relevant arrow.
- Color encodes one stable meaning, such as ownership, or stays decorative-free.
- Boundaries visible without color alone: dashed outlines for trust boundaries.
- State line meanings in the companion Markdown, for example dashed arrows for identity relationships and solid arrows for calls or grants.
- Avoid file-level detail unless diagram question requires it.
- Keep uncertain elements labeled `Assumption` or `Open`.

## Fallbacks

- No Excalidraw extension or Chromium browser: build and check the `.excalidraw` file, write companion Markdown, and state the render check was skipped.
- Flow already precise and user did not ask for Excalidraw: route to `mermaid-architecture-map`.
- Missing system facts: create partial sketch with open questions; do not invent architecture.
- Missing official icon: omit it and list it under open questions.
- Viewer cannot show `.excalidraw`, such as Azure DevOps or GitHub Markdown: export PNG or `.excalidraw.svg` from the editor.

## Verify

- `sketch.py check` reports zero errors: no separate text boxes, bindings point both ways, icons embedded.
- Render PNG reviewed: nothing clipped, overlapping, or crossing a boundary line.
- Diagram answers stated question.
- Main flow readable without zoom.
- Main flow runs top-to-bottom unless the content requires another direction.
- Every box participates in the flow; there are no header, footer, title, legend, summary, key, or decorative boxes.
- Every text element uses Helvetica (`fontFamily: 2`).
- Trust boundaries and external systems explicit.
- Appropriate Azure and product boundaries use official icons when available.
- No secrets or private data embedded.
- Companion summary matches visual.
- Open questions named.

## Writing

Use direct simple sentences. Skip rhetorical flourishes. Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.

## Output

- `.excalidraw` file and the build script that produced it.
- Render PNG used for review.
- Companion `.md` summary always.
- Assumptions and unresolved items.
