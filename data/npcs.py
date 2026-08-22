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
  sprite       Filename only, relative to
               docs/assets/sprites/npcs/<section's sprite_folder>/.
               Drop the actual .png/.gif into that folder with this exact
               name. If the file is missing, the table just shows a blank
               sprite slot instead of breaking the build.
  navi         The exact /navi command text, shown in a one-click-to-copy
               code block (Material's native copy-code button).
  description  HTML string (you can use <strong>, <a href="...">, etc).
               Not run through markdown, so no *bold* / [text](url) syntax
               here, only raw HTML tags.

Each section also needs:

  title           Heading shown above the section's table.
  sprite_folder   Folder name under docs/assets/sprites/npcs/ where this
                   section's sprite files live (e.g. "Eden_Main_Town").
                   Kept separate from `title` so an apostrophe or special
                   character in the title (like "Evenil's Casino") never
                   has to become part of a folder name.

To add a brand new section, add a new
{"title": "...", "sprite_folder": "...", "npcs": [...]} dict to SECTIONS,
in the position you want it to appear on the page.

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

# Shared placeholder shown for NPCs whose real /navi and description
# haven't been provided yet. Swap these two fields out per-NPC as the
# real data comes in; the sprite is already the real uploaded file.
_TBD_NAVI = "/navi (TBD)"
_TBD_DESC = "<em>(description TBD)</em>"

SECTIONS = [
    {
        "title": "Eden Main Town",
        "sprite_folder": "Eden_Main_Town",
        "npcs": [
            {
                "name": "Expert Helper Magnus",
                "sprite": "Expert_Helper_Magnus.gif",
                "navi": "/navi eden_night 80/112",
                "description": "<em>(description on hold)</em>",
            },
            {
                "name": "Donation Point Exchange",
                "sprite": "Donation_Point_Exchange.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
            {
                "name": "Kafra Hilda",
                "sprite": "Kafra_Hilda.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
            {
                "name": "Newbie Helper Luna",
                "sprite": "Newbie_Helper_Luna.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
            {
                "name": "Promo Code",
                "sprite": "Promo_Code.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
            {
                "name": "Tool Dealer",
                "sprite": "Tool_Dealer.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
            {
                "name": "Vote Rewards",
                "sprite": "Vote_Rewards.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
            {
                "name": "Warper",
                "sprite": "Warper.gif",
                "navi": _TBD_NAVI,
                "description": _TBD_DESC,
            },
        ],
    },
    {
        "title": "Quest Hub",
        "sprite_folder": "Quest_Hub",
        "npcs": [],
    },
    {
        "title": "Eden Grand Market",
        "sprite_folder": "Eden_Grand_Market",
        "npcs": [],
    },
    {
        "title": "Evenil's Casino",
        "sprite_folder": "Evenils_Casino",
        "npcs": [],
    },
]
