"""Generate Elementor page data for each homepage option into deploy/pages/."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import option_a, option_b, option_c

PAGES = {
    "option-a": ("Homepage Option A: The Long Road", option_a),
    "option-b": ("Homepage Option B: Real Answers", option_b),
    "option-c": ("Homepage Option C: The Open Door", option_c),
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "pages")
    os.makedirs(out, exist_ok=True)
    for slug, (title, mod) in PAGES.items():
        with open(os.path.join(out, f"{slug}.json"), "w") as f:
            json.dump({"slug": slug, "title": title, "data": mod.build()}, f, indent=1)
        print("built", slug)
