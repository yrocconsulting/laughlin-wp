"""Swap lx:<name> image references for media-library IDs/URLs and print slashed JSON.

Usage: python3 resolve.py pages/option-a.json media-map.json > out.json
The output is backslash-doubled because WordPress unslashes meta values on save.
"""
import json, re, sys
page, media = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))

def url(name): return media[name]["url"]

def walk(e):
    s = e.get("settings", {})
    if e.get("widgetType") == "image" and s["image"]["url"].startswith("lx:"):
        n = s["image"]["url"][3:]
        s["image"].update(url=url(n), id=media[n]["id"])
    for k, v in list(s.items()):
        if isinstance(v, str) and "lx:" in v:
            s[k] = re.sub(r"lx:([a-z0-9-]+)", lambda m: url(m.group(1)), v)
    for k in e.get("elements", []): walk(k)

for e in page["data"]: walk(e)
sys.stdout.write(json.dumps(page["data"]).replace("\\", "\\\\"))
