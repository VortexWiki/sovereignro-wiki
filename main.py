"""
mkdocs-macros-plugin hooks for the SovereignRO wiki.

These macros let contributors write simple, readable calls in their markdown
(e.g. {{ steps([...]) }}) instead of hand-writing HTML with the site's custom
CSS classes (sov-eyebrow, sov-heading, sov-steps, etc.). Each macro returns
a ready-made HTML snippet with the right classes already applied, so a
contributor never has to memorize the class names or worry about the known
attr_list-on-lists bug (see CONTRIBUTING.md for background).

All macros are plain Python functions registered with the plugin below;
they return raw HTML strings that get inserted where the {{ ... }} call
appears in the markdown source, before the markdown/HTML is parsed.
"""

import os
import sys

from markupsafe import Markup

# mkdocs-macros-plugin imports this file as a module named "main" after
# adding the current working directory to sys.path, which normally makes
# sibling packages (like data/) importable. But that only works if mkdocs
# build is actually invoked from the repo root; if the CWD differs for any
# reason (a different working-directory in CI, a wrapper script, etc.) the
# import below fails, and the plugin swallows the exception and silently
# logs "No default module `main` found" instead of a real traceback. Force
# the repo root (this file's own directory) onto sys.path explicitly so the
# import is robust regardless of CWD.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.npcs import NPCS


def _esc(text):
    """Minimal HTML-escaping for text that isn't meant to carry markup."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


DOWNLOAD_ICON_SVG = (
    '<svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M12 3v12"/><polyline points="7 11 12 16 17 11"/>'
    '<path d="M5 21h14"/></svg>'
)

ALERT_ICON_SVG = (
    '<svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M12 9v4"/><path d="M12 17h.01"/>'
    '<path d="M10.3 3.8 2 18a2 2 0 0 0 1.7 3h16.6a2 2 0 0 0 1.7-3'
    'L13.7 3.8a2 2 0 0 0-3.4 0z"/></svg>'
)


def define_env(env):
    """Entry point called by mkdocs-macros-plugin. Registers every macro
    that becomes available inside markdown pages as {{ macro_name(...) }}.
    """

    @env.macro
    def eyebrow(text):
        """Small red uppercase label, e.g. {{ eyebrow("// Get in the game") }}"""
        return Markup(f'<span class="sov-eyebrow">{_esc(text)}</span>')

    @env.macro
    def heading(text, accent=None, level=1):
        """Accented page/section heading.

        {{ heading("Download the", accent="Client") }}          -> <h1>
        {{ heading("How to", accent="Install", level=2) }}      -> <h2>
        """
        tag = f"h{level}"
        accent_html = f' <span class="sov-accent">{_esc(accent)}</span>' if accent else ""
        return Markup(
            f'<{tag}><span class="sov-heading">{_esc(text)}{accent_html}</span></{tag}>'
        )

    @env.macro
    def intro(text):
        """Larger, lighter intro paragraph under a heading.
        Supports basic markdown-style links via plain HTML <a> tags if you
        need them; for anything more complex use raw HTML directly instead.
        """
        return Markup(f'<p class="sov-page-intro">{text}</p>')

    @env.macro
    def hero(eyebrow_text, title, accent=None, intro_text=None):
        """Centered hero block: eyebrow + heading + optional intro.

        {{ hero("// Get in the game", "Download the", accent="Client",
                 intro_text="Grab the client and you're ready to play.") }}
        """
        accent_html = f' <span class="sov-accent">{_esc(accent)}</span>' if accent else ""
        intro_html = f'<p class="sov-page-intro">{intro_text}</p>' if intro_text else ""
        return Markup(
            '<section class="sov-page-hero">'
            f'<span class="sov-eyebrow">{_esc(eyebrow_text)}</span>'
            f'<h1><span class="sov-heading">{_esc(title)}{accent_html}</span></h1>'
            f"{intro_html}"
            "</section>"
        )

    @env.macro
    def steps(items):
        """Numbered step list with red numerals.

        {{ steps(["Download the client.", "Extract the `.rar` archive.",
                   "Run the game."]) }}

        Each item can contain inline HTML (bold, links, code) since it is
        inserted as-is; write it as you would write a line of markdown-ish
        HTML, e.g. "**Download** the client using the button above."
        Plain markdown bold/italic syntax is NOT converted here (this
        bypasses the markdown parser), so use <strong>/<em> or write the
        HTML tags directly for emphasis.
        """
        lis = "".join(f"<li>{item}</li>" for item in items)
        return Markup(f'<div class="sov-steps"><ol>{lis}</ol></div>')

    @env.macro
    def tip_list(items):
        """Bulleted tip list, styled to sit inside a troubleshooting callout.

        {{ tip_list(["Add an exclusion in your antivirus.",
                      "Run as Administrator."]) }}
        """
        lis = "".join(f"<li>{item}</li>" for item in items)
        return Markup(f'<div class="sov-troubleshoot-list"><ul>{lis}</ul></div>')

    @env.macro
    def button(text, url, style="goldfill", large=False):
        """A styled call-to-action button.

        {{ button("Download Full Client", "https://dl.example.com/file.rar") }}
        {{ button("Join Discord", "https://discord.gg/xxx", style="discord") }}
        {{ button("Get Help", "https://discord.gg/xxx", style="discord", large=True) }}

        style: "goldfill" (default, primary gold action) or "discord".
        """
        classes = f"sov-btn-{style}"
        if large:
            classes += " sov-btn-lg"
        return Markup(f'<a class="{classes}" href="{_esc(url)}">{_esc(text)}</a>')

    @env.macro
    def download_card(title, description, button_text, button_url, mirror_text=None, mirror_url=None):
        """The gold-bordered download card with an icon, title, description,
        and primary action button, plus an optional mirror/backup link.

        {{ download_card(
             "SovereignRO — Full Client",
             "~8 GB .rar archive, a direct high-speed download from the official CDN.",
             "Download Full Client ↓", "https://dl.sovereignro.com/client.rar",
             mirror_text="download from Google Drive →",
             mirror_url="https://drive.google.com/..."
        ) }}
        """
        mirror_html = ""
        if mirror_text and mirror_url:
            mirror_html = (
                '<p class="sov-download-mirror-note">Main button not downloading? '
                f'<a href="{_esc(mirror_url)}">{_esc(mirror_text)}</a></p>'
            )
        return Markup(
            '<div class="sov-download-card">'
            '<div class="sov-download-card-body">'
            f'<span class="sov-download-icon">{DOWNLOAD_ICON_SVG}</span>'
            f"<div><h2>{_esc(title)}</h2><p>{description}</p></div>"
            "</div>"
            '<div class="sov-download-actions">'
            f'<a class="sov-btn-goldfill" href="{_esc(button_url)}">{_esc(button_text)}</a>'
            "</div>"
            f"{mirror_html}"
            "</div>"
        )

    @env.macro
    def alert_help(alert_title, alert_text, tips, help_title, help_text, help_button_text, help_button_url):
        """The two-part troubleshooting section: a red alert card (icon +
        text + tip list) followed by a centered help card with a button.

        {{ alert_help(
             "Antivirus & Firewall (read this first)",
             "This is the #1 reason a private-server client won't run.",
             ["Add an exclusion in your antivirus.", "Run as Administrator."],
             "Still stuck?",
             "Hop into our Discord and we'll help you out.",
             "Get Help on Discord", "https://discord.gg/xxx"
        ) }}
        """
        tips_html = "".join(f"<li>{t}</li>" for t in tips)
        return Markup(
            '<div class="sov-troubleshoot">'
            '<div class="sov-troubleshoot-alert">'
            f'<span class="sov-troubleshoot-alert-icon">{ALERT_ICON_SVG}</span>'
            f"<div><h3>{_esc(alert_title)}</h3><p>{alert_text}</p>"
            f'<div class="sov-troubleshoot-list"><ul>{tips_html}</ul></div>'
            "</div>"
            "</div>"
            '<div class="sov-troubleshoot-help">'
            f"<h3>{_esc(help_title)}</h3><p>{help_text}</p>"
            f'<a class="sov-btn-discord sov-btn-lg" href="{_esc(help_button_url)}">{_esc(help_button_text)}</a>'
            "</div>"
            "</div>"
        )

    @env.macro
    def spec_table(rows, callout=None):
        """Gold-bordered key/value spec table (server rates, episode, etc.),
        matching the download card's visual language. The last row is
        rendered as a highlighted "final word" row (e.g. Monetization);
        every other row is a plain label/value pair.

        {{ spec_table([
             ("Episode / Mode", "Renewal &mdash; 4th Job &amp; higher"),
             ("Base EXP rate", "7&times;"),
             ("Job EXP rate", "7&times;"),
             ("Item drop rate", "4&times;"),
             ("Card drop rate", "10&times;"),
             ("Monetization", "Cosmetics-only &mdash; no pay-to-win"),
             ("Anti-cheat", "BeamGuard (Gepard-style client protection)"),
           ], callout="Spend on looks, never on power...") }}
        """
        rows_html = "".join(
            f'<tr><th scope="row">{_esc(label)}</th><td>{value}</td></tr>'
            for label, value in rows
        )
        callout_html = (
            f'<p class="sov-spec-callout">{callout}</p>' if callout else ""
        )
        return Markup(
            '<div class="sov-spec-table-wrap">'
            '<table class="sov-spec-table">'
            f"<tbody>{rows_html}</tbody>"
            "</table>"
            f"{callout_html}"
            "</div>"
        )

    @env.macro
    def npc_table():
        """Important NPCs table: sprite + name, a one-click-to-copy /navi
        command, and a rich-text description. Reads its rows from
        data/npcs.py (NPCS list) so new NPCs can be added there without
        touching this macro or the page markdown.

        {{ npc_table() }}

        The /navi cell is built as a real Material "highlight" code block
        (the same markup pymdownx.superfences/highlight produce), so
        Material's native copy-code button (content.code.copy, already
        enabled in mkdocs.yml) picks it up automatically on hover, with
        zero custom JS.
        """
        if not NPCS:
            return Markup(
                '<p class="sov-npc-table-empty">'
                "<em>No NPCs added yet.</em></p>"
            )

        rows_html = ""
        for npc in NPCS:
            sprite_path = f"../../assets/sprites/npcs/{npc['sprite']}"
            rows_html += (
                '<tr class="sov-npc-row">'
                '<td class="sov-npc-cell-sprite">'
                '<div class="sov-npc-cell-sprite-inner">'
                f'<img src="{_esc(sprite_path)}" alt="{_esc(npc["name"])}" loading="lazy">'
                f'<span class="sov-npc-name">{_esc(npc["name"])}</span>'
                "</div>"
                "</td>"
                '<td class="sov-npc-cell-navi">'
                '<div class="highlight"><pre><span></span><code>'
                f"{_esc(npc['navi'])}"
                "</code></pre></div>"
                "</td>"
                f'<td class="sov-npc-cell-desc">{npc["description"]}</td>'
                "</tr>"
            )

        return Markup(
            '<div class="sov-npc-table-wrap">'
            '<table class="sov-npc-table">'
            "<thead><tr>"
            "<th>NPC</th><th>Location</th><th>Description</th>"
            "</tr></thead>"
            f"<tbody>{rows_html}</tbody>"
            "</table>"
            "</div>"
        )
