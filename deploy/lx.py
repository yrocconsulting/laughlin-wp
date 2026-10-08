"""Shared helpers for building the homepage option pages as Elementor data.

Each option module builds a list of Elementor elements using these helpers.
Images are referenced as "lx:<name>" and resolved to media-library IDs/URLs
at deploy time (see deploy/resolve.py).
"""
import hashlib
import itertools

_counter = itertools.count()
_prefix = ["x"]


def reset_ids(prefix):
    global _counter
    _counter = itertools.count()
    _prefix[0] = prefix


def _id():
    return hashlib.md5(f"{_prefix[0]}-{next(_counter)}".encode()).hexdigest()[:7]


def C(*kids, cls="", tag=None, link=None):
    """Container (full width; layout is handled by our stylesheet)."""
    s = {"content_width": "full", "css_classes": cls}
    if tag:
        s["html_tag"] = tag
    if link:
        s["html_tag"] = "a"
        s["link"] = {"url": link, "is_external": "", "nofollow": ""}
    return {"id": _id(), "elType": "container", "isInner": False,
            "settings": s, "elements": [k for k in kids if k]}


def _w(kind, settings, cls):
    settings["_css_classes"] = cls
    return {"id": _id(), "elType": "widget", "widgetType": kind,
            "isInner": False, "settings": settings, "elements": []}


def H(text, tag="h2", cls=""):
    return _w("heading", {"title": text, "header_size": tag}, cls)


def T(html, cls=""):
    return _w("text-editor", {"editor": html}, cls)


def B(text, url="#", cls=""):
    return _w("button", {"text": text, "link": {"url": url, "is_external": "", "nofollow": ""}}, cls)


def I(name, cls="", alt=""):
    return _w("image", {"image": {"url": f"lx:{name}", "id": "", "alt": alt, "source": "library"},
                        "image_size": "full"}, cls)


def X(html, cls=""):
    return _w("html", {"html": html}, cls)


LOGO = "https://laughlin-staging.yroc.host/wp-content/uploads/2023/09/img-logo.png"
PHONE = "775-883-8484"
TEL = "tel:+17758838484"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?{q}&display=swap">'

# Base reset shared by every option. Scoped to .lx so the rest of the site is untouched.
BASE_CSS = """
/* Hide theme chrome on these preview pages */
div:has(> span > a[href*="portal.liquid-themes.com"]){display:none!important}
/* Let absolutely positioned decorations sit in their layout box, not the widget wrapper */
.lx .elementor-element.elementor-widget-html,.lx .elementor-widget-html>.elementor-widget-container{position:static}
html{scroll-behavior:smooth}
body.elementor-template-canvas{background:var(--bg)!important;margin:0}
.lx,.lx *{box-sizing:border-box}
.lx{background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
.lx .e-con{--padding-top:0;--padding-bottom:0;--padding-left:0;--padding-right:0;--gap:0;padding:0;margin:0;gap:0;display:flex;flex-direction:column;min-width:0;width:auto;max-width:none;flex:0 1 auto}
.lx .elementor-element.elementor-widget{margin:0;width:auto;max-width:100%}
.lx .elementor-widget-container{margin:0;padding:0}
.lx a{color:inherit}
.lx p{margin:0 0 1em}
.lx p:last-child{margin-bottom:0}
.lx .elementor-heading-title{font-family:var(--f-head);color:inherit;margin:0;padding:0;letter-spacing:normal;text-transform:none}
.lx .elementor-widget-image img{display:block;width:100%;height:100%;object-fit:cover;max-width:none}
.lx .elementor-widget-image .elementor-widget-container,.lx .elementor-widget-image{height:100%}
.lx .elementor-button{display:inline-flex;align-items:center;gap:.5em;font-family:var(--f-body);font-weight:600;font-size:16px;line-height:1.2;padding:15px 24px;border-radius:var(--radius,4px);background:var(--navy);color:#fff;border:1.5px solid var(--navy);text-decoration:none;transition:background .2s,color .2s,border-color .2s;fill:currentColor}
.lx .elementor-button:hover{background:var(--navy-2);border-color:var(--navy-2);color:#fff}
.lx .btn-gold .elementor-button{background:var(--gold);border-color:var(--gold);color:var(--navy)}
.lx .btn-gold .elementor-button:hover{background:#f6cd52;border-color:#f6cd52;color:var(--navy)}
.lx .btn-ghost .elementor-button{background:transparent;color:var(--navy);border-color:currentColor}
.lx .btn-ghost .elementor-button:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.lx .btn-link .elementor-button{background:none;border:0;padding:6px 0;color:var(--navy);border-bottom:1.5px solid var(--gold);border-radius:0}
.lx .btn-link .elementor-button:hover{background:none;color:var(--navy);border-color:var(--navy)}
.lx .btn-link .elementor-button-text:after{content:" \\2192"}
.lx .wrap{width:100%;max-width:1240px;margin-left:auto;margin-right:auto;padding-left:32px;padding-right:32px}
.lx .row{flex-direction:row}
.lx .btns{flex-direction:row;flex-wrap:wrap;gap:12px;align-items:center}
.lx ul.ticks{list-style:none;margin:0;padding:0}
.lx ul.ticks li{position:relative;padding-left:28px;margin:0 0 10px}
.lx ul.ticks li:before{content:"";position:absolute;left:0;top:.55em;width:14px;height:8px;border-left:2px solid var(--gold-ink);border-bottom:2px solid var(--gold-ink);transform:rotate(-45deg) translateY(-3px)}
.lx .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
/* Header */
.lx .hdr{position:relative;z-index:50;background:var(--hdr-bg,var(--bg))}
.lx .util{font-size:14px;border-bottom:1px solid var(--line)}
.lx .util .in{display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:42px}
.lx .util nav{display:flex;gap:22px;flex-wrap:wrap;align-items:center}
.lx .util a{text-decoration:none;opacity:.9}
.lx .util a:hover{opacity:1;text-decoration:underline}
.lx .util .lbl{font-weight:600}
.lx .util .tel{font-weight:700}
.lx .main{display:flex;align-items:center;justify-content:space-between;gap:24px;min-height:84px}
.lx .logo img{height:44px;width:auto;display:block}
.lx .nav{display:flex;align-items:center;gap:28px}
.lx .nav a{text-decoration:none;font-weight:600;font-size:16px;color:var(--ink);padding:8px 0;border-bottom:2px solid transparent}
.lx .nav a:hover{border-color:var(--gold)}
.lx .nav .cta{background:var(--navy);color:#fff;padding:12px 18px;border-radius:var(--radius,4px);border:0}
.lx .nav .cta:hover{background:var(--navy-2)}
.lx .burger,.lx #lxnav,.lx .nav .m-only{display:none}
/* Footer */
.lx .ftr{background:var(--ftr-bg,var(--navy));color:#dfe6f2;font-size:15px}
.lx .ftr .in{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr 1fr;gap:32px;padding-top:64px;padding-bottom:48px}
.lx .ftr h4{font-family:var(--f-body);font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:0 0 14px}
.lx .ftr ul{list-style:none;margin:0;padding:0}
.lx .ftr li{margin:0 0 8px}
.lx .ftr a{text-decoration:none;color:#fff}
.lx .ftr a:hover{text-decoration:underline}
.lx .ftr .logo-w{background:#fff;display:inline-block;padding:10px 14px;border-radius:6px;margin-bottom:16px}
.lx .ftr .logo-w img{height:34px;display:block}
.lx .ftr .base{border-top:1px solid rgba(255,255,255,.15);padding-top:20px;padding-bottom:28px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;font-size:13px;color:#aab6cc}
@media (max-width:1100px){
 .lx .nav{position:absolute;left:0;right:0;top:100%;background:var(--bg);flex-direction:column;align-items:stretch;gap:0;padding:8px 24px 24px;border-bottom:1px solid var(--line);display:none}
 .lx .nav a{padding:14px 0;border-bottom:1px solid var(--line)}
 .lx .nav .cta{margin-top:16px;text-align:center}
 .lx .nav .m-only{display:block}
 .lx #lxnav:checked ~ .nav{display:flex}
 .lx .burger{display:inline-flex;flex-direction:column;gap:5px;cursor:pointer;padding:10px}
 .lx .burger span{width:24px;height:2px;background:var(--ink);display:block}
 .lx .main{position:relative}
 .lx .util .acct{display:none}
 .lx .ftr .in{grid-template-columns:1fr 1fr}
}
@media (max-width:640px){
 .lx{font-size:16px}
 .lx .wrap{padding-left:18px;padding-right:18px}
 .lx .logo img{height:36px}
 .lx .main{min-height:70px}
 .lx .util .in{justify-content:center}
 .lx .util .talk{display:none}
 .lx .ftr .in{grid-template-columns:1fr}
}
"""

NAV = [("Start a Business", "#start"), ("Protect My Business", "#protect"),
       ("Grow My Business", "#grow"), ("Resources &amp; Events", "#learn"), ("About", "#story")]


def header(cta="Start your entity"):
    links = "".join(f'<a href="{u}">{t}</a>' for t, u in NAV)
    return X(f"""<header class="hdr">
<div class="util"><div class="wrap in">
<nav class="acct" aria-label="Existing clients"><span class="lbl">Existing clients:</span><a href="#clients">Renew services</a><a href="#clients">Make a payment</a><a href="#clients">Client support</a></nav>
<nav aria-label="Contact"><a class="talk" href="#advisors">Talk with an advisor</a><a class="tel" href="{TEL}">{PHONE}</a></nav>
</div></div>
<div class="wrap main">
<a class="logo" href="#top" aria-label="Laughlin home"><img src="{LOGO}" alt="Laughlin"></a>
<input type="checkbox" id="lxnav"><label class="burger" for="lxnav" aria-label="Menu"><span></span><span></span><span></span></label>
<nav class="nav" aria-label="Main">{links}<a class="m-only" href="#clients">Existing clients: renew &amp; pay</a><a class="cta" href="#formation">{cta}</a></nav>
</div>
</header>""", cls="hdr-w")


def footer():
    return X(f"""<footer class="ftr">
<div class="wrap in">
<div><span class="logo-w"><img src="{LOGO}" alt="Laughlin"></span>
<p>Helping business owners start, protect, grow and preserve what they build. Since 1971.</p>
<p><a href="{TEL}"><strong>{PHONE}</strong></a></p></div>
<div><h4>Start</h4><ul><li><a href="#formation">Form an LLC</a></li><li><a href="#formation">Form a Corporation</a></li><li><a href="#formation">Compare Entities</a></li><li><a href="#formation">Nonprofits</a></li></ul></div>
<div><h4>Protect</h4><ul><li><a href="#protect">Corporate Veil Protection</a></li><li><a href="#protect">Registered Agent</a></li><li><a href="#protect">Corporate Minutes</a></li><li><a href="#protect">Compliance</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="#learn">Webinars &amp; Events</a></li><li><a href="#learn">Guides &amp; E-books</a></li><li><a href="#learn">Live Q&amp;A</a></li><li><a href="#learn">Videos</a></li></ul></div>
<div><h4>Clients</h4><ul><li><a href="#clients">Renew Registered Agent</a></li><li><a href="#clients">Renew CVPS</a></li><li><a href="#clients">Make a Payment</a></li><li><a href="#clients">Client Support</a></li></ul></div>
</div>
<div class="wrap base"><span>&copy; 2026 Laughlin Associates, Inc. Serving business owners nationwide since 1971.</span><span>Design preview &mdash; photography is temporary.</span></div>
</footer>""", cls="ftr-w")


def style(fonts_q, css):
    return X(FONTS.format(q=fonts_q) + "<style>" + BASE_CSS + css + "</style>", cls="lx-style")


# Shared copy so all three options say the same things.
QUESTIONS = [
    ("What happens after I form an LLC?",
     "Forming the company is step one. To keep its protection, you'll need a registered agent, annual state filings, records of major decisions and finances kept separate from your own."),
    ("Is my LLC actually protecting me?",
     "Only if it's run like a separate business. Courts look at whether you kept records, held meetings where required and kept personal and business money apart."),
    ("What can weaken corporate protection?",
     "Missed filings, a lapsed registered agent, no minutes, mixing personal and business funds, and records that don't match what really happened."),
    ("Do I need corporate minutes?",
     "Corporations are generally required to keep them, and LLCs benefit from them. Minutes are your proof that the company made its own decisions."),
    ("What does a Registered Agent actually do?",
     "They accept legal and state notices for your company at a reliable address during business hours, so nothing important gets missed."),
    ("Does my business structure still make sense?",
     "As revenue, partners and goals change, the right structure can change too. An annual review helps you spot that before it costs you."),
]

STAGES = [
    ("Start", "Choose the right entity and form it correctly.", ["LLC &amp; corporation formation", "Entity comparison", "EIN &amp; business setup"]),
    ("Protect", "Keep the protection you formed the company for.", ["Corporate Veil Protection Service", "Registered agent", "Corporate records &amp; minutes"]),
    ("Grow", "Build credit, structure and strategy as you scale.", ["Business credit", "Strategy sessions", "Webinars &amp; live Q&amp;A"]),
    ("Preserve", "Plan for what comes next for you and your family.", ["Asset protection planning", "Living trusts", "Succession planning"]),
]
