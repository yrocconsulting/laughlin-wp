"""Generate Elementor page data for each homepage option into deploy/pages/."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import option_a, option_b, option_c, site_pages

PAGES = {
    "option-a": ("Homepage Option A: The Long Road", option_a),
    "option-b": ("Homepage Option B: Real Answers", option_b),
    "option-c": ("Homepage Option C: The Open Door", option_c),
    "services": ("Services", site_pages.services),
    "about-us": ("About Laughlin", site_pages.about),
    "contact": ("Contact", site_pages.contact),
    "case-studies": ("Client Stories", site_pages.stories),
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "pages")
    os.makedirs(out, exist_ok=True)
    for slug, (title, mod) in PAGES.items():
        with open(os.path.join(out, f"{slug}.json"), "w") as f:
            build = mod if callable(mod) else mod.build
            json.dump({"slug": slug, "title": title, "data": build()}, f, indent=1)
        print("built", slug)
