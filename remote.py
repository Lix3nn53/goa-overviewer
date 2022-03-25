# This is a sample config file, meant to give you an idea of how to format your
# config file and what's possible.
import sys
# Replace this with your path to manualmarkers.py,
sys.path.append("C:/Users/Lix3nn97/Desktop/MyOverviewer/")
# so python can find it
from markersMerchant import *
from markersNPC import *
from markersDungeon import *
from markersTown import *

def townFilter(poi):
    if poi['id'] == 'town':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '/n'


def dungeonFilter(poi):
    if poi['id'] == 'dungeon':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '/n'


def merchantFilter(poi):
    if poi['id'] == 'merchant':
        try:
            return (poi['name'], poi['description'], poi['icon'])
        except KeyError:
            return poi['name'] + '/n'


def npcFilter(poi):
    if poi['id'] == 'npc':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '/n'


# Define the path to your world here. 'My World' in this case will show up as
# the world name on the map interface. If you change it, be sure to also change
# the referenced world names in the render definitions below.
worlds['Adelia'] = "C:/Users/Lix3nn97/Desktop/LavaServer - Build/world"

# Define where to put the output here.
outputdir = "C:/Users/Lix3nn97/Desktop/MyOverviewer/remote"

# This is an item usually specified in a renders dictionary below, but if you
# set it here like this, it becomes the default for all renders that don't
# define it.
# Try "smooth_lighting" for even better looking maps!
rendermode = "smooth_lighting"

markers = markersTown + markersDungeon + markersMerchant + markersNPC

renders["adelia"] = {
    "showspawn": False,
    "center": [2065, 130, 1311],
    "defaultzoom": 5,
    'world': 'Adelia',
    'title': 'Guardians of Adelia',
    'crop': (-10, -10, 5000, 5000),
    "manualpois": markers,
    'markers': [dict(name="Towns", filterFunction=townFilter, icon="markers/marker_home.png", checked=True),
                dict(name="Dungeons", filterFunction=dungeonFilter,
                     icon="markers/marker_tower_red.png", checked=True),
                dict(name="Merchants", filterFunction=merchantFilter, checked=True),
                dict(name="NPCs", filterFunction=npcFilter,
                     icon="markers/marker_npc.png", checked=True),],
    # Note: The 'icon' parameter allows you to specify a custom icon, as per
    # standard markers. This icon must exist in the same folder as your
    # custom webassets or in the same folder as the generated index.html
    # in this case, we use the marker_town.png icon which comes with
    # the Overviewer by default, located in a subdirectory of web_assets.
    "imgformat": "webp",
    "imglossless": False,
    "imgquality": 80,
}

# This example is the same as above, but rotated
# renders["render2"] = {
#         'world': 'Adelia',
#         'northdirection': 'upper-right',
#         'title': 'Upper-right north direction',
# }

# Here's how to do a nighttime render. Also try "smooth_night" instead of "night"
# renders["render3"] = {
#         'world': 'My World',
#         'title': 'Nighttime',
#         # Notice how this overrides the rendermode default specified above
#         'rendermode': 'night',
# }

# .\overviewer.exe --config=C:\Users\Lix3nn97\Desktop\MyOverviewer\remote.py --no-tile-checks
# .\overviewer.exe --config=C:\Users\Lix3nn97\Desktop\MyOverviewer\remote.py --genpoi --skip-scan --skip-players
# .\overviewer.exe --config=C:\Users\Lix3nn97\Desktop\MyOverviewer\remote.py  --update-web-assets
