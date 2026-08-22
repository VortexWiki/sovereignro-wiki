"""
Data source for the "Important NPCs" page (Server Perks section).

Add a new NPC by appending a dict to NPCS below. Fields:

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

Order in this list is the order rows render in the table.

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

NPCS = [
]
