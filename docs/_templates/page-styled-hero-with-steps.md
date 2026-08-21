<!--
  STYLED TEMPLATE (use sparingly): a centered hero block + a numbered step
  list (red numerals), matching the official SovereignRO site's look.

  This is for standalone "product" pages only (Download-style pages), NOT
  for regular guide/reference content. Most wiki pages should use the
  plain page-simple.md template instead, this styled look gets busy for
  content meant to be read page after page.

  See CONTRIBUTING.md for the full list of available macros (eyebrow, heading, steps, etc.).
-->
---
title: Page Title
---

{{ hero(
  "// Your label",
  "How To Do", accent="This",
  intro_text="A short intro explaining what this guide covers."
) }}

{{ eyebrow("// Steps") }}

{{ heading("The", accent="Steps", level=2) }}

{{ steps([
  "<strong>First step</strong> with a short explanation.",
  "<strong>Second step</strong> with an explanation. You can include <code>inline code</code> or <a href=\"https://example.com\">links</a>.",
  "<strong>Third step</strong>, and so on."
]) }}
