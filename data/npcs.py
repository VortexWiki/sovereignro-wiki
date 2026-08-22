"""
Data source for the "Important NPCs" page (Server Perks section).

NPCs are grouped into sections by location (Eden Main Town, Quest Hub,
Eden Grand Market, Evenil's Casino, etc). Each section renders as its own
heading + table on the page, in the order SECTIONS is defined below.

Add a new NPC by appending a dict to the right section's "npcs" list.
Fields:

  name         Display name shown under the sprite and as the row's bold
               label inside the description (you still need to bold it
               yourself in `description`, this isn't automatic).
  sprite       Filename only, relative to docs/assets/sprites/npcs/.
               Drop the actual .png/.gif into that folder with this exact
               name. If the file is missing, the table just shows a blank
               sprite slot instead of breaking the build.
  navi         The exact /navi command text, shown in a one-click-to-copy
               code block (Material's native copy-code button).
  description  HTML string (you can use <strong>, <a href="...">, etc).
               Not run through markdown, so no *bold* / [text](url) syntax
               here, only raw HTML tags.

To add a brand new section, add a new {"title": "...", "npcs": [...]}
dict to SECTIONS, in the position you want it to appear on the page.

Example entry (commented out, not real data):

  {
      "name": "Banker",
      "sprite": "banker.png",
      "navi": "/navi prontera 133/216",
      "description": (
          "The <strong>Banker</strong> lets you access your zeny bank."
      ),
  },
"""

SECTIONS = [
    {
        "title": "Eden Main Town",
        "npcs": [
            {
                "name": "Expert Helper Magnus",
                "sprite": "Expert_Helper_Magnus.gif",
                "navi": "/navi eden_night 80/112",
                "description": "<em>(description on hold)</em>",
            },
        ],
    },
    {
        "title": "Quest Hub",
        "npcs": [],
    },
    {
        "title": "Eden Grand Market",
        "npcs": [],
    },
    {
        "title": "Evenil's Casino",
        "npcs": [],
    },
]
