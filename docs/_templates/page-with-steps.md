<!--
  TEMPLATE: page with a centered hero block + a numbered step list (red
  numerals). Useful for "how to do X in N steps" guides (e.g. Installation,
  a quest guide, a setup walkthrough).
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
