"""Render pages to static HTML that approximates Elementor's markup, for local review."""
import json, os, re, sys, html
here = os.path.dirname(os.path.abspath(__file__))

def img(name): return f"file://{here}/images/lx-{name}.jpg"

def res(s): return re.sub(r"lx:([a-z0-9-]+)", lambda m: img(m.group(1)), s)

def r(e):
    s = e["settings"]
    if e["elType"] == "container":
        tag = s.get("html_tag") or "div"
        kids = "".join(r(k) for k in e["elements"])
        return f'<{tag} class="elementor-element e-flex e-con-full e-con e-parent {s.get("css_classes","")}">{kids}</{tag}>'
    w, c = e["widgetType"], s.get("_css_classes", "")
    if w == "heading": inner = f'<{s["header_size"]} class="elementor-heading-title elementor-size-default">{s["title"]}</{s["header_size"]}>'
    elif w == "text-editor": inner = s["editor"]
    elif w == "button": inner = f'<div class="elementor-button-wrapper"><a class="elementor-button elementor-button-link elementor-size-sm" href="{s["link"]["url"]}"><span class="elementor-button-content-wrapper"><span class="elementor-button-text">{s["text"]}</span></span></a></div>'
    elif w == "image": inner = f'<img src="{res(s["image"]["url"])}" alt="{s["image"]["alt"]}">'
    elif w == "html": inner = res(s["html"])
    return f'<div class="elementor-element elementor-widget elementor-widget-{w} {c}"><div class="elementor-widget-container">{inner}</div></div>'

for f in sorted(os.listdir(os.path.join(here, "pages"))):
    p = json.load(open(os.path.join(here, "pages", f)))
    body = "".join(r(e) for e in p["data"])
    out = os.path.join(sys.argv[1], f.replace(".json", ".html"))
    open(out, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{p["title"]}</title></head><body class="elementor-template-canvas">{body}</body></html>')
    print(out)
