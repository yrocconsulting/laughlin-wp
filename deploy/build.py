"""Generate Elementor page data for every page into deploy/pages/.

PAGES is in publish order: parents come before their children. Each page's
`path` is its URL path; the last part is its slug and the rest is its parent.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import option_a, option_b, option_c, site_pages, pages_full as P

PAGES = [
    ("option-a", "Homepage Option A: The Long Road", option_a.build),
    ("option-b", "Homepage Option B: Real Answers", option_b.build),
    ("option-c", "Home", option_c.build),
    # Start
    ("start-a-business", "Start a Business", P.start_hub),
    ("start-a-business/llc", "Form an LLC", P.llc),
    ("start-a-business/corporation", "Form a Corporation", P.corporation),
    ("start-a-business/nonprofit", "Form a Nonprofit", P.nonprofit),
    ("start-a-business/compare-structures", "Compare Business Structures", P.compare),
    ("start-a-business/nevada", "Why Nevada", P.nevada),
    ("start-a-business/international", "International Clients", P.international),
    ("start-a-business/filing-services", "Filing Services", P.filing_services),
    # Protect
    ("protect-my-business", "Protect My Business", P.protect_hub),
    ("protect-my-business/corporate-veil-protection", "Corporate Veil Protection Service", P.cvps),
    ("protect-my-business/registered-agent", "Registered Agent", P.registered_agent),
    ("protect-my-business/corporate-records", "Corporate Minutes & Records", P.corporate_records),
    ("protect-my-business/common-mistakes", "10 Common Mistakes", P.common_mistakes),
    # Grow
    ("grow-my-business", "Grow My Business", P.grow_hub),
    ("grow-my-business/business-credit", "Business Credit", P.business_credit),
    ("grow-my-business/living-trusts", "Living Trusts", P.living_trusts),
    # Resources
    ("resources", "Resources & Events", P.resources_hub),
    ("resources/business-questions", "Business Questions", P.business_questions),
    ("resources/events", "Events & Webinars", P.events),
    # Company
    ("services", "All Services", site_pages.services),
    ("about-us", "About Laughlin", site_pages.about),
    ("case-studies", "Client Stories", site_pages.stories),
    ("contact", "Contact", site_pages.contact),
    ("clients", "Existing Clients", P.clients),
    ("business-review", "Free Business Review", P.business_review),
    ("privacy-policy", "Privacy Policy", P.privacy),
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "pages")
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    order = []
    for path, title, fn in PAGES:
        name = path.replace("/", "--")
        with open(os.path.join(out, f"{name}.json"), "w") as f:
            json.dump({"path": path, "title": title, "data": fn()}, f, indent=1)
        order.append(name)
    with open(os.path.join(out, "order.txt"), "w") as f:
        f.write("\n".join(order) + "\n")
    print(f"built {len(order)} pages")
