<!--
  STYLED TEMPLATE (use sparingly): a red alert block (icon + text + tip
  list) followed by a centered help card with a button (e.g. Discord),
  matching the official SovereignRO site's look.

  This is for standalone "product" pages only (Download-style pages), NOT
  for regular FAQ/Troubleshooting content. For actual FAQ/Troubleshooting
  guide pages, use the plain page-simple.md template with a normal
  markdown admonition (!!! warning) instead, it reads better for content
  meant to be scanned page after page. See the real Download page for a
  full example of this styled version in context (docs/download/index.md).

  See CONTRIBUTING.md for the full list of available macros (eyebrow, heading, steps, etc.).
-->
---
title: Page Title
---

{{ eyebrow("// Your label") }}

{{ heading("Section", accent="Title", level=2) }}

{{ alert_help(
  "Common issue title",
  "Explanation of the issue and its cause.",
  [
    "First thing to try.",
    "Second thing to try.",
    "Third thing to try."
  ],
  "Still stuck?",
  "Short text inviting the reader to ask for help.",
  "Join Discord",
  "https://discord.com/invite/eog"
) }}
