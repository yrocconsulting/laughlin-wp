"""Building blocks for the full Laughlin site, on the Option C design system.

Every page is assembled from these sections so the site stays consistent and
new pages are quick to add.
"""
import json
from lx import *
from option_c import CSS as C_CSS, FONTQ, MARK, DIAGRAM

FAX = "1-775-883-4874"
TOLLFREE = "1-800-648-0966"
TOLLFREE_TEL = "tel:+18006480966"
ADDRESS = "680 W Nye Lane, Suite 202<br>Carson City, NV 89703"
HOURS = "Mon&ndash;Fri, 8:00 a.m.&ndash;5:00 p.m. Pacific"

# Main navigation, with dropdown children.
MENU = [
    ("Start a Business", "/start-a-business/", [
        ("Form an LLC", "/start-a-business/llc/"),
        ("Form a Corporation", "/start-a-business/corporation/"),
        ("Form a Nonprofit", "/start-a-business/nonprofit/"),
        ("Compare Structures", "/start-a-business/compare-structures/"),
        ("Why Nevada", "/start-a-business/nevada/"),
        ("International Clients", "/start-a-business/international/"),
        ("Filing Services", "/start-a-business/filing-services/"),
    ]),
    ("Protect My Business", "/protect-my-business/", [
        ("Corporate Veil Protection", "/protect-my-business/corporate-veil-protection/"),
        ("Registered Agent", "/protect-my-business/registered-agent/"),
        ("Minutes &amp; Records", "/protect-my-business/corporate-records/"),
        ("10 Common Mistakes", "/protect-my-business/common-mistakes/"),
        ("Free Business Review", "/business-review/"),
    ]),
    ("Grow My Business", "/grow-my-business/", [
        ("Business Credit", "/grow-my-business/business-credit/"),
        ("Living Trusts", "/grow-my-business/living-trusts/"),
        ("Strategy Consultation", "/business-review/"),
        ("Nevada Office Services", "/grow-my-business/#nevada-office"),
    ]),
    ("Resources &amp; Events", "/resources/", [
        ("Business Questions", "/resources/business-questions/"),
        ("Events &amp; Webinars", "/resources/events/"),
        ("Free Guides", "/resources/#guides"),
        ("Client Stories", "/case-studies/"),
    ]),
    ("About", "/about-us/", [
        ("About Laughlin", "/about-us/"),
        ("Client Stories", "/case-studies/"),
        ("Contact", "/contact/"),
    ]),
]

KIT_CSS = """
/* dropdown navigation */
.lx .nav .dd{position:relative;display:flex;align-items:center}
.lx .nav .dd>a:after{content:"";display:inline-block;width:6px;height:6px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-3px);margin-left:8px;opacity:.6}
.lx .nav .sub{display:none;position:absolute;top:100%;left:-18px;min-width:250px;background:var(--paper,#fff);border-top:3px solid var(--gold);box-shadow:0 24px 48px -24px rgba(10,45,100,.45);padding:10px 0;z-index:60}
.lx .nav .sub a{display:block;padding:9px 18px;border:0;font-size:15px;font-weight:500;white-space:nowrap}
.lx .nav .sub a:hover{background:var(--bg);color:var(--navy)}
.lx .nav .dd:hover .sub,.lx .nav .dd:focus-within .sub{display:block}
.lx .nav{gap:22px}
@media (max-width:1100px){
 .lx .nav .dd{flex-direction:column;align-items:stretch}
 .lx .nav .dd>a:after{display:none}
 .lx .nav .sub{display:block;position:static;box-shadow:none;border:0;padding:0 0 6px 16px;min-width:0;background:none}
 .lx .nav .sub a{padding:9px 0;font-size:15px;border-bottom:0}
}
/* footer contact block */
.lx .ftr .addr{font-style:normal;line-height:1.55;margin:0 0 12px}
.lx .ftr .addr b{color:#fff}
.lx .ftr .disc{border-top:1px solid rgba(255,255,255,.15);padding-top:18px;padding-bottom:4px;font-size:13px;color:#aab6cc;line-height:1.5}
.lx .ftr .base a{color:#dfe6f2}
.lx-c .sec.tight{padding-top:44px;padding-bottom:0}
/* breadcrumbs */
.lx-c .crumbs{font-family:var(--f-head);font-size:13px;font-weight:600;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px}
.lx-c .crumbs a{color:var(--muted);text-decoration:none}
.lx-c .crumbs a:hover{color:var(--navy)}
.lx-c .crumbs span{opacity:.5}
/* at a glance */
.lx-c .glance{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-top:8px}
.lx-c .glance div{padding:18px 18px 18px 0}
.lx-c .glance small{display:block;font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink);margin-bottom:4px}
.lx-c .glance b{font-family:var(--f-head);font-size:18px;color:var(--navy);line-height:1.25}
/* prose */
.lx-c .prose{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start}
.lx-c .prose .body{font-size:18px;color:var(--ink);max-width:680px}
.lx-c .prose .body p{margin:0 0 1em}
.lx-c .prose .body h3{font-family:var(--f-head);font-size:22px;color:var(--navy);margin:28px 0 8px}
.lx-c .prose .body ul{margin:0 0 1em;padding-left:0;list-style:none}
.lx-c .prose .body li{position:relative;padding-left:26px;margin:0 0 8px}
.lx-c .prose .body li:before{content:"";position:absolute;left:2px;top:.6em;width:8px;height:8px;background:var(--gold);transform:rotate(45deg)}
.lx-c .prose .body blockquote{margin:24px 0;padding-left:22px;border-left:4px solid var(--gold);font-style:italic;font-size:20px;line-height:1.45}
.lx-c .prose .body blockquote cite{display:block;font-style:normal;font-family:var(--f-head);font-size:14px;color:var(--muted);margin-top:8px}
/* link cards */
.lx-c .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:40px}
.lx-c .cards.two{grid-template-columns:repeat(2,1fr)}
.lx-c .cards.four{grid-template-columns:repeat(4,1fr)}
.lx-c .card{background:var(--paper);border:1px solid var(--line);padding:28px;text-decoration:none;display:flex;flex-direction:column;gap:8px;min-height:190px;transition:border-color .2s,transform .2s}
.lx-c .card:hover{border-color:var(--navy);transform:translateY(-3px)}
.lx-c .card small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .card strong{font-family:var(--f-head);font-size:23px;line-height:1.15;color:var(--navy);letter-spacing:-.01em}
.lx-c .card p{margin:0;font-size:16px;color:var(--muted)}
.lx-c .card:after{content:"\\2192";margin-top:auto;padding-top:8px;font-family:var(--f-head);font-weight:700;color:var(--gold-ink)}
.lx-c .card.hl{background:var(--navy);border-color:var(--navy)}
.lx-c .card.hl strong{color:#fff}
.lx-c .card.hl p{color:#C9D4E8}
.lx-c .card.hl small,.lx-c .card.hl:after{color:var(--gold)}
/* faq (light) */
.lx-c .faq{border-top:2px solid var(--navy)}
.lx-c .faq details{border-bottom:1px solid var(--line)}
.lx-c .faq summary{list-style:none;cursor:pointer;padding:22px 40px 22px 0;font-family:var(--f-head);font-size:20px;font-weight:600;color:var(--navy);position:relative;line-height:1.3}
.lx-c .faq summary::-webkit-details-marker{display:none}
.lx-c .faq summary:after{content:"";position:absolute;right:6px;top:28px;width:10px;height:10px;border-right:2px solid var(--gold-ink);border-bottom:2px solid var(--gold-ink);transform:rotate(45deg);transition:transform .2s}
.lx-c .faq details[open] summary:after{transform:rotate(-135deg)}
.lx-c .faq .a{padding:0 40px 22px 0;font-size:17px;color:var(--muted)}
.lx-c .faq .a p{margin:0 0 .8em}
.lx-c .faq-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start}
/* compare table */
.lx-c .tbl-wrap{overflow-x:auto;margin-top:36px;border:1px solid var(--line);background:var(--paper)}
.lx-c table.cmp{width:100%;border-collapse:collapse;min-width:720px;font-size:16px}
.lx-c table.cmp th,.lx-c table.cmp td{text-align:left;vertical-align:top;padding:16px 18px;border-bottom:1px solid var(--line)}
.lx-c table.cmp thead th{font-family:var(--f-head);font-size:18px;color:#fff;background:var(--navy);border:0}
.lx-c table.cmp tbody th{font-family:var(--f-head);font-size:14px;font-weight:700;color:var(--navy);width:20%;background:var(--bg)}
.lx-c table.cmp td{color:var(--ink)}
.lx-c .fine{font-size:14px;color:var(--muted);margin-top:16px}
/* numbered list (mistakes, steps) */
.lx-c .numbered{counter-reset:n;list-style:none;margin:0;padding:0}
.lx-c .numbered>li{counter-increment:n;display:grid;grid-template-columns:72px 1fr;gap:16px;padding:26px 0;border-top:1px solid var(--line)}
.lx-c .numbered>li:last-child{border-bottom:1px solid var(--line)}
.lx-c .numbered>li:before{content:counter(n,decimal-leading-zero);font-family:var(--f-head);font-weight:800;font-size:40px;line-height:1;color:transparent;-webkit-text-stroke:1.2px var(--navy);opacity:.5}
.lx-c .numbered h3{font-family:var(--f-head);font-size:22px;font-weight:700;color:var(--navy);margin:0 0 6px}
.lx-c .numbered p{margin:0;color:var(--muted);font-size:17px}
/* includes box */
.lx-c .inc{background:var(--navy);color:#DCE4F2;padding:36px;gap:12px}
.lx-c .inc h3{font-family:var(--f-head);color:#fff;font-size:24px;margin:0 0 6px}
.lx-c .inc ul{list-style:none;margin:0;padding:0}
.lx-c .inc li{position:relative;padding:10px 0 10px 24px;border-top:1px solid rgba(255,255,255,.14);font-size:17px}
.lx-c .inc li:before{content:"";position:absolute;left:2px;top:1.05em;width:8px;height:8px;background:var(--gold);transform:rotate(45deg)}
.lx-c .inc .go{display:inline-block;align-self:flex-start;font-family:var(--f-head);font-weight:700;text-decoration:none;padding:14px 22px;background:var(--gold);color:var(--navy);margin-top:12px}
.lx-c .split{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:start}
/* team */
.lx-c .team{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:36px}
.lx-c .person{background:var(--paper);border:1px solid var(--line);padding:26px}
.lx-c .person b{display:block;font-family:var(--f-head);font-size:20px;color:var(--navy)}
.lx-c .person small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .person p{margin:10px 0 0;font-style:italic;color:var(--muted)}
/* legal copy */
.lx-c .legal{max-width:760px;font-size:18px}
.lx-c .legal h2{font-family:var(--f-head);font-size:28px;color:var(--navy);margin:40px 0 12px;letter-spacing:-.01em}
.lx-c .legal h2:first-child{margin-top:0}
.lx-c .legal ul{padding-left:22px}
.lx-c .legal li{margin-bottom:8px}
.lx-c .updated{font-family:var(--f-head);font-size:14px;color:var(--muted)}
@media (max-width:1100px){
 .lx-c .prose,.lx-c .faq-grid,.lx-c .split{grid-template-columns:1fr;gap:36px}
 .lx-c .cards,.lx-c .cards.four{grid-template-columns:1fr 1fr}
 .lx-c .glance{grid-template-columns:1fr 1fr}
 .lx-c .team{grid-template-columns:1fr 1fr}
}
@media (max-width:640px){
 .lx-c .cards,.lx-c .cards.two,.lx-c .cards.four,.lx-c .glance,.lx-c .team{grid-template-columns:1fr}
 .lx-c .numbered>li{grid-template-columns:1fr;gap:4px}
 .lx-c .inc{padding:24px}
}
"""


def site_header():
    items = ""
    for label, url, kids in MENU:
        sub = "".join(f'<a href="{u}">{t}</a>' for t, u in kids)
        items += f'<div class="dd"><a href="{url}">{label}</a><div class="sub">{sub}</div></div>'
    return X(f"""<header class="hdr">
<div class="util"><div class="wrap in">
<nav class="acct" aria-label="Existing clients"><span class="lbl">Existing clients:</span><a href="/clients/">Renew services</a><a href="/clients/">Make a payment</a><a href="/clients/">Client support</a></nav>
<nav aria-label="Contact"><a class="talk" href="/contact/">Talk with an advisor</a><a class="tel" href="{TEL}">{PHONE}</a></nav>
</div></div>
<div class="wrap main">
<a class="logo" href="/" aria-label="Laughlin home"><img src="{LOGO}" alt="Laughlin"></a>
<input type="checkbox" id="lxnav"><label class="burger" for="lxnav" aria-label="Menu"><span></span><span></span><span></span></label>
<nav class="nav" aria-label="Main">{items}<a class="m-only" href="/clients/">Existing clients: renew &amp; pay</a><a class="cta" href="/start-a-business/">Start your business</a></nav>
</div>
</header>""", cls="hdr-w")


def site_footer():
    return X(f"""<footer class="ftr">
<div class="wrap in">
<div><span class="logo-w"><img src="{LOGO}" alt="Laughlin"></span>
<address class="addr"><b>Laughlin Associates, Inc.</b><br>{ADDRESS}</address>
<p class="addr"><a href="{TEL}"><strong>{PHONE}</strong></a><br>Toll-free <a href="{TOLLFREE_TEL}">{TOLLFREE}</a><br>Se habla espa&ntilde;ol<br>Fax {FAX}<br>{HOURS}</p></div>
<div><h4>Start</h4><ul><li><a href="/start-a-business/llc/">Form an LLC</a></li><li><a href="/start-a-business/corporation/">Form a Corporation</a></li><li><a href="/start-a-business/nonprofit/">Form a Nonprofit</a></li><li><a href="/start-a-business/compare-structures/">Compare Structures</a></li><li><a href="/start-a-business/nevada/">Why Nevada</a></li><li><a href="/start-a-business/filing-services/">Filing Services</a></li></ul></div>
<div><h4>Protect &amp; Grow</h4><ul><li><a href="/protect-my-business/corporate-veil-protection/">Corporate Veil Protection</a></li><li><a href="/protect-my-business/registered-agent/">Registered Agent</a></li><li><a href="/protect-my-business/corporate-records/">Minutes &amp; Records</a></li><li><a href="/grow-my-business/business-credit/">Business Credit</a></li><li><a href="/grow-my-business/living-trusts/">Living Trusts</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="/resources/business-questions/">Business Questions</a></li><li><a href="/resources/events/">Events &amp; Webinars</a></li><li><a href="/resources/#guides">Free Guides</a></li><li><a href="/protect-my-business/common-mistakes/">10 Common Mistakes</a></li><li><a href="/case-studies/">Client Stories</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="/about-us/">About Laughlin</a></li><li><a href="/clients/">Existing Clients</a></li><li><a href="/business-review/">Free Business Review</a></li><li><a href="/contact/">Contact</a></li><li><a href="/services/">All Services</a></li></ul></div>
</div>
<div class="wrap disc">Laughlin Associates provides business formation and compliance services. We are not a law or accounting firm and do not give legal, tax or accounting advice. When you need that advice, please consult a qualified professional.</div>
<div class="wrap base"><span>&copy; 2026 Laughlin Associates, Inc. Serving business owners nationwide since 1972.</span><span><a href="/privacy-policy/">Privacy Policy</a> &middot; Photography is temporary.</span></div>
</footer>""", cls="ftr-w")


def page(*sections, extra_css=""):
    from site_pages import PAGE_CSS
    return [C(
        style(FONTQ, C_CSS + PAGE_CSS + KIT_CSS + extra_css),
        site_header(),
        *[s for s in sections if s],
        site_footer(),
        cls="lx lx-c")]


def crumbs(trail):
    parts = ['<a href="/">Home</a>'] + [f'<a href="{u}">{t}</a>' for t, u in trail]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + "</nav>"


def hero(eyebrow, title, lede, trail=(), img=None, alt="", extra=None):
    bits = []
    if trail:
        bits.append(X(crumbs(trail)))
    bits += [T(f'<span class="eyebrow">{eyebrow}</span>'), H(title, "h1", "h1"), T(f"<p>{lede}</p>", "lede")]
    if extra:
        bits.append(X(extra) if isinstance(extra, str) else extra)
    copy = C(*bits, cls="ph-copy")
    kids = [copy] + ([I(img, "ph-media", alt)] if img else [])
    return C(C(*kids, cls="wrap ph-grid"), cls="phero", tag="section")


def btns(*pairs):
    """Row of buttons: (text, url, style) where style is '', 'gold', 'ghost' or 'link'."""
    out = []
    for t, u, s in pairs:
        out.append(f'<a class="xb {s}" href="{u}">{t}</a>')
    return '<div class="xbtns">' + "".join(out) + "</div>"


BTN_CSS = """
.lx-c .xbtns{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:6px}
.lx-c .xb{display:inline-flex;align-items:center;font-family:var(--f-head);font-weight:700;font-size:16px;text-decoration:none;padding:15px 24px;background:var(--navy);color:#fff;border:1.5px solid var(--navy)}
.lx-c .xb:hover{background:var(--navy-2);border-color:var(--navy-2)}
.lx-c .xb.gold{background:var(--gold);border-color:var(--gold);color:var(--navy)}
.lx-c .xb.ghost{background:transparent;color:var(--navy)}
.lx-c .xb.ghost:hover{background:var(--navy);color:#fff}
.lx-c .xb.link{background:none;border:0;border-bottom:1.5px solid var(--gold);padding:6px 0;color:var(--navy)}
.lx-c .xb.link:after{content:" \\2192";white-space:pre}
"""
KIT_CSS += BTN_CSS


def section(*kids, alt=False, eid=None, cls=""):
    c = "sec" + (" quiet" if alt else "") + (f" {cls}" if cls else "")
    return C(C(*kids, cls="wrap"), cls=c, tag="section", eid=eid)


def head(eyebrow, title, lede=None):
    kids = [T(f'<span class="eyebrow">{eyebrow}</span>'), H(title, "h2", "h2")]
    if lede:
        kids.append(T(f"<p>{lede}</p>", "lede"))
    return C(*kids, cls="cv-copy")


def prose(eyebrow, title, html, alt=False, eid=None, lede=None):
    return C(C(head(eyebrow, title, lede), X(f'<div class="body">{html}</div>'), cls="wrap prose"),
             cls="sec" + (" quiet" if alt else ""), tag="section", eid=eid)


def glance(items):
    return X('<div class="glance">' + "".join(f"<div><small>{a}</small><b>{b}</b></div>" for a, b in items) + "</div>")


def cards(items, cols=""):
    """items: (small, title, text, url[, 'hl'])"""
    out = ""
    for it in items:
        sm, t, p, u = it[:4]
        hl = " hl" if len(it) > 4 and it[4] else ""
        out += f'<a class="card{hl}" href="{u}"><small>{sm}</small><strong>{t}</strong><p>{p}</p></a>'
    return X(f'<div class="cards {cols}">{out}</div>')


def rows(items):
    return X('<div class="rows">' + "".join(
        f'<div class="rowi"><small>{a}</small><div><h3>{b}</h3><p>{c}</p></div></div>' for a, b, c in items) + "</div>")


def numbered(items):
    return X('<ol class="numbered">' + "".join(f"<li><div><h3>{a}</h3><p>{b}</p></div></li>" for a, b in items) + "</ol>")


def faq(items, schema=True):
    html = '<div class="faq">' + "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="a"><p>{a}</p></div></details>'
        for i, (q, a) in enumerate(items)) + "</div>"
    if schema:
        import re
        clean = lambda s: re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&rsquo;", "'").replace("&nbsp;", " ")
        data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in items]}
        html += '<script type="application/ld+json">' + json.dumps(data) + "</script>"
    return X(html)


def faq_section(eyebrow, title, items, lede=None, alt=False, eid=None):
    return C(C(head(eyebrow, title, lede), faq(items), cls="wrap faq-grid"),
             cls="sec" + (" quiet" if alt else ""), tag="section", eid=eid)


def includes(title, items, cta=None, url=None):
    li = "".join(f"<li>{x}</li>" for x in items)
    go = f'<a class="go" href="{url}">{cta} &rarr;</a>' if cta else ""
    return X(f'<div class="inc" style="display:flex;flex-direction:column"><h3>{title}</h3><ul>{li}</ul>{go}</div>')


def band(title, text, primary=("Talk with an advisor", "/contact/")):
    return X(f"""<section class="band"><div class="wrap band-in"><div><h2>{title}</h2><p>{text}</p></div>
<div class="acts"><a href="{primary[1]}">{primary[0]} &rarr;</a><a class="tel" href="{TEL}">Call {PHONE}</a></div></div></section>""")


def related(items, title="Keep reading"):
    return section(T(f'<span class="eyebrow">{title}</span>'), cards(items), alt=True)
