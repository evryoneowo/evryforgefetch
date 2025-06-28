import json

import fetch
from renderer import renderer

with open('config.json') as f:
    parsed = json.loads(f.read())

ACCENT = parsed['accent_color']
RESET = parsed['reset_color']
SECONDARY = parsed['secondary_color']

fetchmain = fetch.Fetch(ACCENT, SECONDARY, RESET)

fetchmain.add('hi', 'hiii!')
fetchmain.add('desc', 'fully customizable fetch for you :3')

def run():
    fetchmain.print()