# Dashboard Email

Use only for newsletters whose main job is summarizing metrics, status, alerts, or recurring briefing data.

If user supplies a prior issue as target format, match that issue before adding
new dashboard elements. Do not force extra buttons, color blocks, or images when
reference issue is tighter and more text/table driven.

## Hierarchy

- Design for skimming. Put most important takeaway at top.
- Header: name, date, one-sentence summary. Keep header visually consistent; do not depend on CSS `position: sticky`.
- Lead with one primary metric or decision. Use clear size contrast; 36-48px metric type is starting range, not rule.
- Supporting labels 12-14px. Body copy 14-16px when template permits.
- One content idea per card. Headings and bold text should tell coherent story when read alone.
- Keep metric annotation near 10 words when meaning stays intact.

Do not assume every reader follows same scan path. F-pattern, inverted pyramid, and zig-zag layouts are options. Validate against actual content and audience.

## Layout

- Prefer 600-640px desktop container.
- Use one primary column.
- Two or three metric cards may share row on desktop only when each stays legible and stacks to one column on mobile.
- Never exceed three columns.
- Group related metrics with thin border or light neutral fill. Do not rely on shadow.
- Use generous padding and clear section gaps.
- Order mobile stack by importance, not desktop position.

## Color And Meaning

- Use neutral background, strong text, one brand accent.
- For consumer, creator, lifestyle, or personality-led newsletters, preserve the
  existing visual voice. Multiple controlled accent colors, emoji cues, and
  playful section labels are appropriate when they improve scanning and match
  the brand.
- Reserve red for real exception, decline, risk, or urgency. Reserve green for positive state only when meaning fits.
- Pair color with label, sign, arrow, or icon. Never encode trend by color alone.
- Keep text contrast at least 4.5:1; large text at least 3:1.
- Avoid decorative gradients or low-contrast color combinations that weaken reading.

Do not strip personality from a pre-existing template just because the issue has
dashboard structure.

## Metrics And Charts

- Prefer number, short label, direction, period, and comparison.
- Name denominator, unit, and time window when needed.
- Avoid dense scatterplots, multi-series charts, tiny legends, and interaction-dependent charts.
- Export simple charts as compressed PNG or JPG. Use SVG only after testing target clients.
- Add useful alt text plus nearby text summary. Email must still make sense with images blocked.
- Link detailed analysis to live dashboard or web version.

## Calls To Action

- One primary CTA per issue.
- Use high-contrast button with descriptive label.
- Add secondary CTA buttons or links when they help the reader reply, jump to a
  section, save, share, or open a useful source. Keep the primary CTA visually
  dominant.
- Aim for at least 44px button height and enough space from nearby links.
- Keep secondary links visually quiet and limited.

## Email HTML

- Prefer table-based layout for broad client compatibility.
- Use inline CSS and HTML attributes for critical width, padding, background, and image size.
- Avoid JavaScript, hover-dependent meaning, external stylesheets, and web-font dependency.
- Give images explicit width, responsive max width, and alt text.
- Keep critical text as live HTML, not baked into chart image.
- Provide browser or live-dashboard link when layout risk is material.

## Verify

- First scan reveals primary takeaway and exceptions.
- Test desktop and mobile stack.
- Test target clients, prioritizing audience client data. Include Gmail, Outlook, and Apple Mail when unknown.
- Test images on and off.
- Test links, CTA tap size, alt text, contrast, and reading order.
- Confirm numbers, units, periods, comparisons, and trend direction against source data.
- Check plain-text version.

## Sources

- [Campaign Monitor: structure for scanners](https://www.campaignmonitor.com/blog/email-marketing/structure-email-marketing-campaigns-scanners/)
- [EmailOctopus: layout, mobile, images, accessibility](https://emailoctopus.com/blog/designing-emails-everything-you-need-to-know)
- [Engage: HTML email compatibility and image fallbacks](https://engage.so/blog/a-complete-guide-to-creating-html-emails-best-practices-and-examples-for-saas-companies/)
- [beehiiv: mobile-friendly email templates](https://www.beehiiv.com/blog/mastering-mobile-friendly-email-templates)
- [W3C: WCAG contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
