---
name: excalidraw-system-sketch
description: Plan, research, build, and render-check Excalidraw architecture sketches with deployed-resource discovery, trust boundaries, flows, regions, stable identifiers, and official product icons. Use when the user asks for an Excalidraw diagram or .excalidraw file, deployed integration map, rough system sketch, spatial grouping, swimlanes, icons, or visual exploration.
license: MIT
---

Create one readable spatial sketch plus an evidence-backed companion summary. Prioritize the end-to-end flow of data, its shape at each boundary, and clear inputs and outputs. Every piece of canvas text is part of a shape or arrow.

## Scope

Use when placement, grouping, boundaries, regions, swimlanes, icons, or exploration matters. Organize the sketch around data movement; include infrastructure to explain where data enters, changes, persists, and exits. For a deployed or current-state integration, inventory the relevant production deployment before drawing. For a conceptual sketch or a complete user-provided inventory, use the lighter path and do not perform unnecessary deployment discovery. When the user asks for an ordered flow, use numbered swimlanes.

## Inputs

- Diagram purpose, audience, and where it will be viewed.
- Components, actors, systems, and flows.
- Data sources, sinks, inputs, outputs, transformations, and persistence points.
- Data shape at each boundary: format, schema or contract, key fields, cardinality, and batch or streaming behavior when relevant.
- Trust boundaries, secret entry points, user data, and external services. Never collect secret values.
- Products the project uses, for icons.
- Environment scope. Default deployed/current-state requests to production only unless the user names another environment.
- Stable non-secret identifiers and paths when relevant: tenant ID, subscription ID, resource group, region, resource ID, input path, and output path.

## Deployment Evidence

- Use live cloud inventory as evidence of what is currently deployed when authenticated tools are available.
- Use Ev2, ARM, Bicep, Terraform, Kubernetes, Helm, pipeline manifests, deployment outputs, and other deployment-as-code artifacts to enumerate intended regions and resources.
- Use source code and runtime configuration to establish connections and data flow. Do not treat prose alone as proof that a resource is deployed.
- Use schemas, models, API contracts, event definitions, queries, sample metadata, and configuration to establish data shape. Do not inspect or reproduce sensitive payload values.
- Record where each fact came from in the companion summary. Cite repository evidence as `file:line`; record cloud query, subscription, resource group, and retrieval time for live inventory.
- Compare live inventory with deployment artifacts when both are available. Mark drift, stale declarations, and uncertain ownership explicitly.
- Never invent a region, resource, boundary, identifier, or connection. If access or evidence is incomplete, label coverage incomplete and list the missing source.

## Workflow

Scripts live in `scripts/` next to this file. Run them with `uv run <skill-dir>/scripts/sketch.py ...`, or with `python` when `uv` is missing. They use only the standard library.

1. State the diagram question, product boundary, environment, and production scope. Do not mix non-production resources into a production diagram.
2. Discover the relevant deployed resources. Search live inventory and deployment artifacts broadly enough to find every production region. Do not stop after finding one representative region.
3. Build an evidence matrix before drawing: product or owner, environment, tenant or subscription, region, resource, stable identifier, role in the flow, and evidence source.
4. Trace the data end to end before drawing. For each transition, identify the producer, input, transformation, output, consumer, transport or path, and data shape. Mark unknown contracts rather than guessing.
5. Reconcile sources. Use live inventory for current deployed state, deployment artifacts for intended coverage, code or configuration for connections, and schemas or contracts for data shape. Record drift and unresolved conflicts.
6. Confirm completeness. Represent every evidenced production region and every product-relevant deployed resource, including shared dependencies that participate in the flow. Explain omitted resources in the companion summary.
7. Choose a top-to-bottom flow by default. Use horizontal flow, swimlanes, nested zones, or before/after only when the content clearly reads better that way.
8. Find icons with `sketch.py icons <keywords>`. Confirm each match is the right product.
9. Write a small build script that imports `scripts/scene.py`. Do not hand-write element JSON. Load [excalidraw-format.md](references/excalidraw-format.md) when writing the build script or debugging a file.
10. Run `sketch.py check <file>.excalidraw`. Fix every error.
11. Run `sketch.py render <file>.excalidraw <file>.png`. Read the PNG. Fix clipped, overlapping, or wrapped text, then rebuild and repeat.
12. Write the companion `.md` summary with purpose, discovery method, evidence matrix, data contracts, components, icon sources, boundaries, flows, drift, assumptions, omissions, and open questions.

## Text Rules

- Text inside a shape is part of that shape. Bind it: the text sets `containerId` to the shape, and the shape lists `{ "type": "text", "id": "<text_id>" }` in `boundElements`. Never place a separate text element on top of a shape. `scene.py` does this for items, zones, badges, and arrow labels.
- Zone titles bind to their zone with `verticalAlign: "top"` and `textAlign: "left"`.
- Connector labels bind to their arrow. Excalidraw wraps them at the larger of 70% of the arrow's width or 11 times the font size (176px at 16px), and centers them on the arrow. Break lines short.
- Long step descriptions in swimlanes go in a message box above the arrow.
- Write full sentences. Write every value in full: IDs, URLs, names. Never truncate with `...`.
- Show stable non-secret identifiers and paths when they help the reader locate the real deployment.
- Label arrows with the data moving between components. Keep the canvas label short; put detailed schema or contract fields in the companion summary.
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
- Make data flow the dominant visual path. A reader should be able to follow data from each source through transformations and persistence to every output.
- Show each component's input and output explicitly. Name the data format or contract at boundaries when known.
- Distinguish transport from transformation. Arrows show movement; component boxes state what changes, validates, enriches, filters, aggregates, or persists the data.
- Do not draw an unexplained source, sink, or bidirectional arrow. Split different data movements into separate labeled arrows.
- Prefer a vertical, top-to-bottom main flow. Keep the primary path visually centered and place branches beside the step where they diverge.
- Show product and ownership boundaries clearly. Nest tenant, subscription, resource group, network, and region boundaries only when they explain deployment or flow.
- Represent regional differences directly. Repeat a regional branch when its deployed resources or connections differ; do not imply identical deployments.
- Every box must represent a component, actor, data store, or boundary that participates in the flow.
- Never add boxed diagram titles, headers, footers, legends, summaries, keys, or decorative annotations. Put that information in the companion Markdown. Put essential relationship details on the relevant arrow.
- Color encodes one stable meaning, such as ownership, or stays decorative-free.
- Boundaries visible without color alone: dashed outlines for trust boundaries.
- State line meanings in the companion Markdown, for example dashed arrows for identity relationships and solid arrows for calls or grants.

## Fallbacks

- No Excalidraw extension or Chromium browser: build and check the `.excalidraw` file, write companion Markdown, and state the render check was skipped.
- Flow already precise and user did not ask for Excalidraw: route to `mermaid-architecture-map`.
- No live cloud access: use deployment artifacts, mark the result as intended-state or partially verified, and name the unavailable inventory source.
- Missing system facts: create a partial sketch, mark coverage incomplete, and list open questions; do not invent architecture.
- Missing official icon: omit it and list it under open questions.
- Viewer cannot show `.excalidraw`, such as Azure DevOps or GitHub Markdown: export PNG or `.excalidraw.svg` from the editor.

## Verify

- `sketch.py check` reports zero errors: no separate text boxes, bindings point both ways, icons embedded.
- Render PNG reviewed: nothing clipped, overlapping, or crossing a boundary line.
- Diagram answers stated question.
- Every source, input, transformation, output, and sink can be traced end to end.
- Data shape is identified at each meaningful boundary, or marked unknown with the missing contract named.
- Inputs and outputs are unambiguous; arrows name what moves and components state what changes.
- Production diagrams contain production resources only unless the user requested a comparison.
- Every evidenced production region and product-relevant deployed resource is represented or explicitly listed as omitted.
- Companion evidence identifies how and where each deployed resource was found.
- Live inventory and deployment artifacts are reconciled; drift and incomplete coverage are visible.
- Main flow readable without zoom.
- Main flow runs top-to-bottom unless the content requires another direction.
- Every box participates in the flow; there are no header, footer, title, legend, summary, key, or decorative boxes.
- Every text element uses Helvetica (`fontFamily: 2`).
- Trust boundaries and external systems explicit.
- Appropriate Azure and product boundaries use official icons when available.
- No secret values, credentials, or personal data embedded. Stable infrastructure identifiers appear only when relevant and supported by authorized sources.
- Companion summary matches visual.
- Open questions named.

## Writing

Use direct simple sentences. Skip rhetorical flourishes. Avoid X-not-Y contrasts, self-answering rhetorical questions, em dashes, alliterative three-part phrases, vague inspirational pivots, unsourced claims, and unverified quotes.

## Output

- `.excalidraw` file and the build script that produced it.
- Render PNG used for review.
- Companion `.md` summary with the evidence matrix, data-contract matrix, discovery sources, icon sources, drift, assumptions, omissions, and unresolved items.
