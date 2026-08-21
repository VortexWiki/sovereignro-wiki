# Contributing to the SovereignRO Wiki

This wiki is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
The site's styling comes from `docs/stylesheets/sovereignro.css` and is
applied automatically at build time on GitHub, you don't need to install
anything locally for that to work.

## How it actually works

1. You clone the repo and write/edit a `.md` file inside the `docs/` folder.
2. You push your branch or open a Pull Request against `main`.
3. A GitHub Action (`.github/workflows/deploy.yml`) automatically builds the
   site and deploys it to GitHub Pages.

The styling always comes from that automated build on GitHub, never from your
own machine.

## Writing a page: use the `{{ }}` macros

To make styled pages easy to write, this wiki has a small set of macros
(powered by `mkdocs-macros-plugin`). Instead of hand-writing HTML with CSS
classes, you call a macro with plain text and it produces the styled block
for you. This is the recommended way to write a page, and it avoids every
gotcha of writing raw HTML by hand.

**Easiest path: copy one of the templates in `docs/_templates/`, replace the
placeholder text, and you're done.**

### Available macros

**`{{ eyebrow("// Your label") }}`**
The small red uppercase label above a heading.

**`{{ heading("Page", accent="Title") }}`**
An accented heading. The `accent` part renders in red. Add `level=2` (or 3,
4...) for a `<h2>`/`<h3>` instead of the default `<h1>`.

```
{{ heading("How to", accent="Install", level=2) }}
```

**`{{ intro("Some intro text with a link if you want.") }}`**
A larger, lighter intro paragraph. HTML like `<a href="...">` works inside
the text; plain markdown `[link](url)` syntax does not (see limitations
below), use an `<a>` tag instead.

**`{{ hero("// Label", "Title", accent="Word", intro_text="...") }}`**
A centered hero block combining the three macros above, used at the very top
of a page.

**`{{ steps([...]) }}`**
A numbered step list with red numerals.

```
{{ steps([
  "<strong>Download</strong> the client.",
  "<strong>Extract</strong> the archive to a folder.",
  "<strong>Run</strong> the game."
]) }}
```

**`{{ tip_list([...]) }}`**
A bulleted tip list, styled to sit inside a troubleshooting callout.

**`{{ button("Text", "https://...") }}`**
A call-to-action button. Add `style="discord"` for the Discord-blue version
(default is gold), and `large=True` for a bigger button.

```
{{ button("Download Full Client", "https://dl.example.com/file.rar") }}
{{ button("Join Discord", "https://discord.gg/xxx", style="discord", large=True) }}
```

**`{{ download_card("Title", "Description", "Button text", "https://...") }}`**
The gold-bordered download card with an icon, title, description, and a
button. Add `mirror_text="..."` and `mirror_url="..."` for an optional
backup link underneath.

**`{{ alert_help(alert_title, alert_text, [tips], help_title, help_text, help_button_text, help_button_url) }}`**
The two-part troubleshooting section: a red alert card (icon + text + tip
list) followed by a centered help card with a button. See
`docs/_templates/page-with-alert-and-help.md` for a filled-in example.

### A note on text inside macros

Macro arguments are plain Python strings, not markdown. That means:

- **Bold/italic**: use `<strong>...</strong>` / `<em>...</em>` instead of
  `**...**` / `*...*`.
- **Links**: use `<a href="...">...</a>` instead of `[text](url)`.
- **Inline code**: use `<code>...</code>` instead of `` `text` ``.

This is a small tradeoff for not having to deal with HTML block structure or
the attr_list bug described below. If a page needs a lot of rich inline
formatting, consider writing the surrounding paragraphs as normal markdown
outside the macro calls, and only use macros for the structural blocks
(headings, steps, cards).

## Regular markdown works everywhere else

Outside of the macro calls, write normal markdown: headings with `##`,
**bold**, *italic*, `code`, [links](https://example.com), tables, images,
regular bullet/numbered lists, admonitions (`!!! note`), etc. All of that
works exactly like any other MkDocs page and needs no special handling.

## Advanced: writing raw HTML/CSS classes directly

Some existing pages (like `docs/download/index.md`) were written by hand
with the raw `sov-*` CSS classes before the macros existed, for maximum
layout control. You generally shouldn't need this for a new page, the
macros above cover the common cases, but if you do need something the
macros don't support, keep these rules in mind:

- **Never attach `{: .my-class }` after a markdown list** (`1. ...` or
  `- ...`). It binds to the last `<li>` instead of the whole list. Always
  wrap the list in a `<div class="my-class" markdown>` block instead.
- **Add the `markdown` attribute** on any `<div>`/`<section>`/`<p>` tag that
  contains markdown syntax (bold, links, lists), otherwise it won't be
  converted to HTML.
- **Leave a blank line** before and after markdown content inside a
  `<div markdown>` block.

Reach out before doing this if you're not sure, it's easy to end up with a
page that looks broken.

## Previewing locally (optional)

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open `http://localhost:8000`. The site reloads automatically on save.

To check that your build won't break anything before pushing (the same
check GitHub runs):

```bash
mkdocs build --strict
```

If this command shows an error, the Pull Request will fail on GitHub too.

## Adding a new page to the nav

1. Create your file at `docs/section-name/index.md` (or a subfolder).
2. Add it under `nav:` in `mkdocs.yml`, wherever it should appear.
3. Run `mkdocs build --strict` to confirm there are no warnings.
