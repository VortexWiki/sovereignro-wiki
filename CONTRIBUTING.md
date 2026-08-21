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

## Two ways to write a page: plain (default) vs styled (rare)

The wiki uses **plain markdown for almost every page**. Guides, FAQ, dungeon
info, server info, troubleshooting, anything meant to be read page after
page, all of that should read like a normal, clean documentation wiki: a
title, some headings, paragraphs, lists, tables, admonitions. Nothing fancy.

A small set of **styled "product" pages** (currently just Download) use the
official site's richer visual language (red eyebrow labels, accented
headings, gold buttons, gradient cards). That look is great for a one-off
landing-style page but gets busy and hard to scan if used on every guide
page, so it's reserved for pages that are more "marketing" than "reference".

**When in doubt, write plain markdown.** Only reach for the styled macros
below if you're building something like the Download page.

## Writing a plain content page (the default)

Copy `docs/_templates/page-simple.md` and fill it in. It's just:

```markdown
---
title: Page Title
---

# Page Title

One or two sentences summarizing the page's content.

## First subheading

Your content here. Regular markdown works: **bold**, *italic*,
[links](https://example.com), `code`, lists, tables, etc.
```

Useful plain-markdown patterns for this wiki:

**Numbered steps:** just a normal markdown list.

```markdown
1. Download the client.
2. Extract the archive.
3. Run the game.
```

**Tips / warnings:** use a normal admonition.

```markdown
!!! tip "Need help?"
    Join the community Discord to ask questions.

!!! warning "Antivirus false positives"
    Custom RO clients aren't code-signed, so antivirus software may flag them.
```

**Collapsible FAQ entries:**

```markdown
??? question "Is the server free to play?"
    Yes, the server is fully free to play.
```

**Tables**, images, and everything else work exactly like any other MkDocs
page, no special handling needed.

## Writing a styled "product" page (rare)

If you're building a standalone landing-style page (not a guide), this wiki
has a small set of `{{ }}` macros (powered by `mkdocs-macros-plugin`) that
produce the site's styled blocks without hand-writing HTML/CSS classes.
Copy one of `docs/_templates/page-styled-*.md` to start.

### Available macros

**`{{ eyebrow("// Your label") }}`**
The small red uppercase label above a heading.

**`{{ heading("Page", accent="Title") }}`**
An accented heading. The `accent` part renders in red. Add `level=2` (or 3,
4...) for a `<h2>`/`<h3>` instead of the default `<h1>`.

**`{{ intro("Some intro text with a link if you want.") }}`**
A larger, lighter intro paragraph. HTML like `<a href="...">` works inside
the text; plain markdown `[link](url)` syntax does not (see limitations
below).

**`{{ hero("// Label", "Title", accent="Word", intro_text="...") }}`**
A centered hero block combining the three macros above.

**`{{ steps([...]) }}`**
A numbered step list with red numerals (the styled version, for product
pages only, regular guide steps should just be a plain markdown list).

**`{{ tip_list([...]) }}`**
A bulleted tip list, styled to sit inside a troubleshooting callout.

**`{{ button("Text", "https://...") }}`**
A call-to-action button. Add `style="discord"` for the Discord-blue version
(default is gold), and `large=True` for a bigger button.

**`{{ download_card("Title", "Description", "Button text", "https://...") }}`**
The gold-bordered download card with an icon, title, description, and a
button. Add `mirror_text="..."` and `mirror_url="..."` for an optional
backup link underneath.

**`{{ alert_help(alert_title, alert_text, [tips], help_title, help_text, help_button_text, help_button_url) }}`**
The two-part troubleshooting section: a red alert card followed by a
centered help card with a button.

### A note on text inside macros

Macro arguments are plain Python strings, not markdown:

- **Bold/italic**: use `<strong>...</strong>` / `<em>...</em>` instead of
  `**...**` / `*...*`.
- **Links**: use `<a href="...">...</a>` instead of `[text](url)`.
- **Inline code**: use `<code>...</code>` instead of `` `text` ``.

## Advanced: writing raw HTML/CSS classes directly

The existing `docs/download/index.md` was written by hand with the raw
`sov-*` CSS classes before the macros existed, for maximum layout control.
You shouldn't need this, the macros above cover the product-page case, but
if you ever do, keep these rules in mind:

- **Never attach `{: .my-class }` after a markdown list** (`1. ...` or
  `- ...`). It binds to the last `<li>` instead of the whole list. Always
  wrap the list in a `<div class="my-class" markdown>` block instead.
- **Add the `markdown` attribute** on any `<div>`/`<section>`/`<p>` tag that
  contains markdown syntax, otherwise it won't be converted to HTML.
- **Leave a blank line** before and after markdown content inside a
  `<div markdown>` block.

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
