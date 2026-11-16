"""Inner site pages (Services, About, Contact, Client Stories) built on the
Option C design system so they match the homepage."""
from lx import *
from option_c import CSS as C_CSS, FONTQ, MARK, DIAGRAM

# The generic MetForm contact form already on the site (name, email, phone, message).
CONTACT_FORM_ID = "116***1698940141153"

PAGE_CSS = """
/* page hero */
.lx-c .phero{padding-top:56px;padding-bottom:72px;border-bottom:1px solid var(--line)}
.lx-c .ph-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:end}
.lx-c .ph-copy{gap:22px}
.lx-c .ph-media{height:380px}
.lx-c .ph-media img{clip-path:polygon(0 6%,100% 0,100% 100%,0 96%)}
.lx-c .jump{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.lx-c .jump a{font-family:var(--f-head);font-weight:600;font-size:15px;text-decoration:none;padding:10px 16px;border:1px solid var(--navy);color:var(--navy)}
.lx-c .jump a:hover{background:var(--navy);color:#fff}
.lx-c .jump a span{color:var(--gold-ink);margin-right:6px}
/* service stages */
.lx-c .stage{padding-top:96px;padding-bottom:96px;border-bottom:1px solid var(--line);scroll-margin-top:20px}
.lx-c .stage.alt{background:var(--paper)}
.lx-c .st-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start}
.lx-c .st-head{gap:18px;position:sticky;top:24px}
.lx-c .st-head .n{font-family:var(--f-head);font-weight:800;font-size:88px;line-height:1;color:transparent;-webkit-text-stroke:1.5px var(--navy);opacity:.35}
.lx-c .st-head .when{font-family:var(--f-head);font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .st-media{height:260px;margin-top:8px}
.lx-c .svcs{display:flex;flex-direction:column}
.lx-c .svc{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:26px 0;border-top:1px solid var(--line)}
.lx-c .svc:last-child{border-bottom:1px solid var(--line)}
.lx-c .svc h3{font-family:var(--f-head);font-size:22px;font-weight:700;color:var(--navy);margin:0 0 6px;letter-spacing:-.01em}
.lx-c .svc p{margin:0;color:var(--muted);font-size:17px;max-width:560px}
.lx-c .svc .tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.lx-c .svc .tags span{font-family:var(--f-head);font-size:13px;font-weight:600;padding:5px 10px;background:var(--bg);border:1px solid var(--line);color:var(--ink)}
.lx-c .svc > a{font-family:var(--f-head);font-weight:700;font-size:15px;color:var(--navy);text-decoration:none;border-bottom:1.5px solid var(--gold);white-space:nowrap;margin-top:4px}
.lx-c .svc.feature{background:var(--navy);color:#DCE4F2;padding:32px;border:0;margin:8px 0;grid-template-columns:1fr}
.lx-c .svc.feature h3{color:#fff;font-size:26px}
.lx-c .svc.feature p{color:#C9D4E8}
.lx-c .svc.feature small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.lx-c .svc.feature .go{justify-self:start;display:inline-block;font-family:var(--f-head);font-weight:700;text-decoration:none;padding:14px 22px;background:var(--gold);color:var(--navy);margin-top:6px}
.lx-c .svc.feature ul{list-style:none;padding:0;margin:14px 0 4px;display:grid;grid-template-columns:1fr 1fr;gap:8px 24px}
.lx-c .svc.feature li{font-size:16px;padding-left:18px;position:relative}
.lx-c .svc.feature li:before{content:"";position:absolute;left:0;top:.55em;width:7px;height:7px;background:var(--gold);transform:rotate(45deg)}
/* veil explainer inside services */
.lx-c .veil-x{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center;margin-top:12px}
/* cta band */
.lx-c .band{background:var(--navy);color:#DCE4F2;padding-top:72px;padding-bottom:72px;border-bottom:1px solid rgba(255,255,255,.14)}
.lx-c .band-in{display:grid;grid-template-columns:1.2fr .8fr;gap:48px;align-items:center}
.lx-c .band h2{font-family:var(--f-head);font-size:clamp(28px,3.2vw,42px);line-height:1.08;font-weight:700;letter-spacing:-.02em;color:#fff;margin:0 0 10px}
.lx-c .band p{margin:0;font-size:18px;color:#C9D4E8}
.lx-c .band .acts{display:flex;flex-direction:column;gap:12px;align-items:flex-start}
.lx-c .band .acts a{font-family:var(--f-head);font-weight:700;text-decoration:none;padding:15px 24px;background:var(--gold);color:var(--navy)}
.lx-c .band .acts a.tel{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.5)}
/* about */
.lx-c .beliefs{display:grid;grid-template-columns:repeat(2,1fr);gap:0 56px}
.lx-c .eco{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.lx-c .eco a{background:var(--paper);border:1px solid var(--line);text-decoration:none;display:flex;flex-direction:column}
.lx-c .eco img{width:100%;height:200px;object-fit:cover;display:block}
.lx-c .eco .e-in{padding:24px;display:flex;flex-direction:column;gap:8px}
.lx-c .eco small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .eco strong{font-family:var(--f-head);font-size:22px;color:var(--navy);line-height:1.15}
.lx-c .eco p{margin:0;color:var(--muted);font-size:16px}
/* contact */
.lx-c .ct-side{gap:32px}
.lx-c .ct-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:72px;align-items:start}
.lx-c .ways{display:flex;flex-direction:column}
.lx-c .way{display:grid;grid-template-columns:120px 1fr;gap:20px;padding:22px 0;border-top:1px solid var(--line)}
.lx-c .way:last-child{border-bottom:1px solid var(--line)}
.lx-c .way small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink);padding-top:6px}
.lx-c .way a,.lx-c .way b{font-family:var(--f-head);font-size:24px;font-weight:700;color:var(--navy);text-decoration:none;letter-spacing:-.01em;display:block}
.lx-c .way p{margin:4px 0 0;color:var(--muted);font-size:16px}
.lx-c .form-card{background:var(--paper);border:1px solid var(--line);padding:40px;gap:18px;position:relative}
.lx-c .form-card:before{content:"";position:absolute;left:-1px;top:-1px;width:6px;height:72px;background:var(--gold)}
.lx-c .form-card h2{font-family:var(--f-head);font-size:28px;font-weight:700;color:var(--navy);margin:0;letter-spacing:-.01em}
.lx-c .form-card p.note{font-size:15px;color:var(--muted);margin:0}
.lx-c .form-card .elementor-widget-metform input:not([type=checkbox]):not([type=radio]),.lx-c .form-card .elementor-widget-metform textarea{width:100%;font-family:var(--f-body);font-size:17px;padding:14px 16px;border:1px solid var(--line);border-radius:0;background:#fff;color:var(--ink);box-shadow:none}
.lx-c .form-card .elementor-widget-metform input:focus,.lx-c .form-card .elementor-widget-metform textarea:focus{outline:2px solid var(--navy);outline-offset:-1px;border-color:var(--navy)}
.lx-c .form-card .elementor-widget-metform .e-con,.lx-c .form-card .elementor-widget-metform .elementor-element,.lx-c .form-card .elementor-widget-metform .elementor-column{width:100%!important;max-width:100%!important;flex:1 1 100%!important}
.lx-c .form-card .elementor-widget-metform label{font-family:var(--f-head);font-weight:600;font-size:14px;color:var(--ink)}
.lx-c .form-card .elementor-widget-metform button[type=submit],.lx-c .form-card .metform-btn{font-family:var(--f-head);font-weight:700;font-size:16px;background:var(--navy)!important;color:#fff!important;border:0!important;border-radius:0!important;padding:16px 28px!important}
.lx-c .form-card .elementor-widget-metform button[type=submit]:hover{background:var(--navy-2)!important}
.lx-c .expect{counter-reset:e;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:0 28px}
.lx-c .expect li{counter-increment:e;padding-top:16px;border-top:2px solid var(--navy);font-size:16px;color:var(--muted)}
.lx-c .expect li b{display:block;font-family:var(--f-head);font-size:18px;color:var(--navy);margin-bottom:4px}
.lx-c .expect li b:before{content:counter(e) ". ";color:var(--gold-ink)}
.lx-c .cl-big{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:36px}
.lx-c .cl-big a{background:var(--paper);border:1px solid var(--line);padding:24px;text-decoration:none;display:flex;flex-direction:column;gap:6px;min-height:150px}
.lx-c .cl-big a:hover{border-color:var(--navy)}
.lx-c .cl-big b{font-family:var(--f-head);font-size:19px;color:var(--navy);line-height:1.2}
.lx-c .cl-big span{font-size:15px;color:var(--muted)}
.lx-c .cl-big a:after{content:"\\2192";margin-top:auto;font-family:var(--f-head);color:var(--gold-ink);font-weight:700}
/* stories */
.lx-c .story{display:grid;grid-template-columns:.9fr 1.1fr;gap:64px;align-items:center;padding:56px 0;border-top:1px solid var(--line)}
.lx-c .story:last-child{border-bottom:1px solid var(--line)}
.lx-c .story .who small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .story .who h3{font-family:var(--f-head);font-size:28px;font-weight:700;color:var(--navy);margin:8px 0 4px;letter-spacing:-.01em}
.lx-c .story .who p{margin:0;color:var(--muted)}
.lx-c .story blockquote{margin:0;font-size:clamp(22px,2.2vw,28px);line-height:1.4;font-style:italic;color:var(--ink);border-left:4px solid var(--gold);padding-left:28px}
.lx-c .story .tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:14px}
.lx-c .story .tags span{font-family:var(--f-head);font-size:13px;font-weight:600;padding:5px 10px;background:var(--paper);border:1px solid var(--line)}
.lx-c .share{background:var(--paper);border:1px dashed var(--gold-ink);padding:40px;display:grid;grid-template-columns:1fr auto;gap:32px;align-items:center;margin-top:56px}
.lx-c .share h3{font-family:var(--f-head);font-size:26px;font-weight:700;color:var(--navy);margin:0 0 6px}
.lx-c .share p{margin:0;color:var(--muted)}
.lx-c .share a{font-family:var(--f-head);font-weight:700;text-decoration:none;padding:15px 24px;background:var(--navy);color:#fff;white-space:nowrap}
@media (max-width:1100px){
 .lx-c .ph-grid,.lx-c .st-grid,.lx-c .band-in,.lx-c .ct-grid,.lx-c .story,.lx-c .veil-x{grid-template-columns:1fr;gap:40px}
 .lx-c .st-head{position:static}
 .lx-c .eco{grid-template-columns:1fr 1fr}
 .lx-c .cl-big{grid-template-columns:1fr 1fr}
 .lx-c .ph-media{height:300px}
}
@media (max-width:640px){
 .lx-c .stage{padding-top:64px;padding-bottom:64px}
 .lx-c .svc{grid-template-columns:1fr}
 .lx-c .svc.feature{padding:24px}
 .lx-c .svc.feature ul,.lx-c .beliefs,.lx-c .eco,.lx-c .expect,.lx-c .cl-big{grid-template-columns:1fr}
 .lx-c .expect{gap:18px}
 .lx-c .way{grid-template-columns:1fr;gap:4px}
 .lx-c .form-card{padding:24px}
 .lx-c .share{grid-template-columns:1fr;padding:26px}
}
"""


def page(*sections):
    """Wrap page sections with the full-site header and footer."""
    import sitekit
    return sitekit.page(*sections)


def phero(eyebrow, title, lede, extra=None, img=None, alt=""):
    copy = C(T(f'<span class="eyebrow">{eyebrow}</span>'), H(title, "h1", "h1"), T(f"<p>{lede}</p>", "lede"),
             extra, cls="ph-copy")
    kids = [copy] + ([I(img, "ph-media", alt)] if img else [])
    return C(C(*kids, cls="wrap ph-grid"), cls="phero", tag="section")


def band(title, text):
    return X(f"""<section class="band"><div class="wrap band-in"><div><h2>{title}</h2><p>{text}</p></div>
<div class="acts"><a href="/contact/">Talk with an advisor &rarr;</a><a class="tel" href="{TEL}">Call {PHONE}</a></div></div></section>""")


def svc(title, text, tags=(), link=None, label="Learn more"):
    t = "".join(f"<span>{x}</span>" for x in tags)
    t = f'<div class="tags">{t}</div>' if t else ""
    a = f'<a href="{link}">{label} &rarr;</a>' if link else ""
    return f'<div class="svc"><div><h3>{title}</h3><p>{text}</p>{t}</div>{a}</div>'


def stage(anchor, n, name, when, line, img, alt, services, alt_bg=False):
    return C(C(
        C(X(f'<div class="n">0{n}</div>'), T(f'<span class="when">{when}</span>'), H(name, "h2", "h2"),
          T(f"<p>{line}</p>", "lede"), I(img, "st-media", alt), cls="st-head"),
        X(f'<div class="svcs">{services}</div>'),
        cls="wrap st-grid"), cls="stage alt" if alt_bg else "stage", tag="section", eid=anchor)


def services():
    reset_ids("svc")
    start = "".join([
        svc("Form an LLC or corporation", "We help you choose the right structure, then file it correctly in any state.",
            ["LLC", "S-Corporation", "C-Corporation", "Nonprofit", "Benefit corporation"], "/start-a-business/", "Start now"),
        svc("Compare structures", "Not sure which entity fits? See the differences side by side, or talk it through with an advisor.",
            link="/start-a-business/compare-structures/", label="Compare"),
        svc("EIN and business setup", "Employer ID, corporate record book and a clear checklist of what to do next.", link="/start-a-business/filing-services/"),
        svc("Name search and DBA", "Check your company name is available and register a trade name if you need one.", link="/start-a-business/filing-services/"),
        svc("Non-U.S. residents", "Form and run a U.S. company from outside the country.", link="/start-a-business/international/"),
    ])
    protect = (
        f"""<div class="svc feature" id="cvps"><small>Our signature service</small><h3>Corporate Veil Protection Service</h3>
<p>Your company keeps business debts and lawsuits away from your home and savings, as long as it's run like a separate business. CVPS keeps up the formalities so the protection holds.</p>
<ul><li>Deadline and renewal tracking</li><li>Annual minutes and resolutions</li><li>Corporate records kept in order</li><li>Yearly review with an advisor</li></ul>
<a class="go" href="/protect-my-business/corporate-veil-protection/">Explore CVPS &rarr;</a></div>"""
        + svc("Registered agent", "A reliable address that receives legal and state notices for your company, so nothing gets missed.",
              link="/protect-my-business/registered-agent/")
        + svc("Corporate minutes and record book", "Meetings and decisions documented properly. Your proof the company stands on its own.", link="/protect-my-business/corporate-records/")
        + svc("Compliance filings", "Annual reports and state filings, on time, every year.",
              ["Annual reports", "Certificate of good standing", "Foreign qualification"], "/start-a-business/filing-services/")
        + svc("Free business review", "Is your company still protecting you? We'll check your structure and records with you.",
              link="/business-review/", label="Request a review"))
    grow = "".join([
        svc("Business credit", "Build credit in the company's name, separate from your own.", link="/grow-my-business/business-credit/"),
        svc("Strategy sessions", "One-to-one time with an advisor on structure, taxes and next steps.", link="/business-review/"),
        svc("Live Q&amp;A and webinars", "LAI Business Edge: bring your questions, get straight answers. Free.", link="/resources/events/", label="See dates"),
        svc("Nevada mail forwarding", "A business address and mail handling for Nevada companies.", link="/grow-my-business/#nevada-office"),
    ])
    preserve = "".join([
        svc("Asset protection planning", "Structure your holdings so one claim can't reach everything you own."),
        svc("Living trusts", "Plan how your business and assets pass to the people you choose.", link="/grow-my-business/living-trusts/"),
        svc("Name changes and dissolution", "Change your company, or close it down cleanly when the time comes.", link="/start-a-business/filing-services/"),
    ])
    return page(
        phero("All services", "One partner for the life of your business.",
              "Start it right. Keep it protected. Grow it with a plan. Preserve what you've built.",
              X('<div class="jump"><a href="#start"><span>01</span>Start</a><a href="#protect"><span>02</span>Protect</a><a href="#grow"><span>03</span>Grow</a><a href="#preserve"><span>04</span>Preserve</a></div>'),
              "owner-workshop", "A business owner at work in his shop"),
        stage("start", 1, "Start", "Day one", "Pick the right structure. File it correctly.", "owner-cafe",
              "A new business owner at her shop door", start),
        stage("protect", 2, "Protect", "Every year", "Stay compliant. Keep your veil intact.", "laughlin-1on1",
              "A Laughlin advisor reviewing records with a client", protect, alt_bg=True),
        C(C(C(T('<span class="eyebrow">What is the corporate veil?</span>'),
              H("Your company protects you. Only if it's maintained.", "h2", "h2"),
              T("<p>An LLC or corporation draws a legal line between your business and your personal life. Run the company as its own business and the line holds. Let the upkeep slip and a court can step over it.</p>", "lede"),
              cls="cv-copy"),
            X(f'<div class="diagram">{DIAGRAM}</div>'), cls="wrap veil-x"), cls="sec cvps", tag="section"),
        stage("grow", 3, "Grow", "As you scale", "Build credit, strategy and structure.", "laughlin-planning",
              "A business owner mapping out a plan", grow),
        stage("preserve", 4, "Preserve", "What comes next", "Protect your assets. Plan the hand-off.", "advisor-seniors",
              "An advisor helping a couple plan ahead", preserve, alt_bg=True),
        band("Not sure where to start?", "Tell us where your business is today. We'll point you to the right next step."),
    )


def about():
    reset_ids("about")
    return page(
        phero("About Laughlin", "Built by a business owner. For business owners.",
              "Since 1972, we've helped entrepreneurs start the right company, keep it protected and plan what comes next.",
              None, "laughlin-roundtable", "Business owners at a Laughlin workshop"),
        C(C(
            C(X(f'<div class="big71">1972 {MARK}</div>'),
              H("It started with a truck driver.", "h2", "h2"),
              T("<p>Harley Laughlin was an independent truck driver. He believed small businesses deserved the same protections big companies take for granted, and started Laughlin in 1972 to provide them.</p><p>Five decades and thousands of businesses later, the job hasn't changed. We've seen which mistakes cost owners the most. Our services exist to prevent them.</p>", "lede"),
              X("""<div class="facts"><div><b>Thousands</b><span>of businesses supported</span></div><div><b>Nationwide</b><span>service in every state</span></div><div><b>Inc. 5000</b><span>2026 honoree</span></div></div>"""),
              cls="her-copy"),
            C(I("laughlin-1on1", "", "An advisor and client in conversation"),
              I("laughlin-notes", "", "Notes from a Laughlin session"),
              I("aaron-speaking", "", "Aaron Young speaking at a Laughlin event"),
              T('<p class="figcap">Archival photos from the early years would go here.</p>'),
              cls="her-media"),
            cls="wrap her"), cls="sec", tag="section"),
        C(C(
            C(T('<span class="eyebrow">What we believe</span>'),
              H("Formation is only the beginning.", "h2", "h2"),
              T("<p>Filing the paperwork takes a day. Running a protected business takes years. That's the part we're built for.</p>", "lede"),
              X('<ul class="pairs"><li>Teach first. Sell second.</li><li>People, not ticket queues.</li><li>Relationships measured in decades.</li></ul>'),
              cls="q-copy"),
            X("""<div class="rows">
<div class="rowi"><small>Education</small><div><h3>Workshops, guides and live Q&amp;A</h3><p>Teaching owners how to protect themselves has been part of Laughlin for decades.</p></div></div>
<div class="rowi"><small>People</small><div><h3>Advisors you can actually call</h3><p>Real specialists who know business structure, not a call center reading a script.</p></div></div>
<div class="rowi"><small>Protection</small><div><h3>Help after formation</h3><p>Corporate Veil Protection, registered agent and compliance, year after year.</p></div></div>
<div class="rowi"><small>Longevity</small><div><h3>Clients for life</h3><p>Many clients stay with us for years, through every stage of their business.</p></div></div>
</div>"""),
            cls="wrap q-grid"), cls="sec quiet", tag="section"),
        C(C(
            C(T('<span class="eyebrow">Learn with us</span>'),
              H("Part of a bigger community.", "h2", "h2"),
              T("<p>Laughlin's events and education bring business owners together to learn, ask questions and plan ahead.</p>", "lede"), cls=""),
            X("""<div class="eco">
<a href="/resources/events/"><img src="lx:laughlin-planning" alt=""><div class="e-in"><small>Every month &middot; Online</small><strong>LAI Business Edge: Live Q&amp;A</strong><p>Bring your questions about structure, compliance and protection.</p></div></a>
<a href="/resources/events/"><img src="lx:laughlin-summit" alt=""><div class="e-in"><small>Live event</small><strong>Magnify Your Wealth Summit</strong><p>Strategy for business owners and investors, in person.</p></div></a>
<a href="/resources/#guides"><img src="lx:couple-docs" alt=""><div class="e-in"><small>Free</small><strong>Guides and e-books</strong><p>LLC Quick Start Guide, compliance checklists and more.</p></div></a>
</div>"""),
            cls="wrap"), cls="sec", tag="section"),
        band("Talk to a real person.", "Questions about your business? Our advisors give straight answers in plain English."),
    )


def contact():
    reset_ids("contact")
    form = {"id": "c0f0rm1", "elType": "widget", "widgetType": "metform", "isInner": False,
            "settings": {"mf_form_id": CONTACT_FORM_ID, "_css_classes": "mf"}, "elements": []}
    return page(
        phero("Contact", "Talk to a real person.",
              "Questions about starting, protecting or changing your business? Call, or send a note and an advisor will get back to you."),
        C(C(
            C(X(f"""<div class="ways">
<div class="way"><small>Call</small><div><a href="{TEL}">{PHONE}</a><p>Talk with an advisor.</p></div></div>
<div class="way"><small>Toll-free</small><div><a href="tel:+18006480966">1-800-648-0966</a><p>Se habla espa&ntilde;ol.</p></div></div>
<div class="way"><small>Hours</small><div><b>Mon&ndash;Fri</b><p>8:00 a.m.&ndash;5:00 p.m. Pacific</p></div></div>
<div class="way"><small>Office</small><div><b>Laughlin Associates, Inc.</b><p>680 W Nye Lane, Suite 202<br>Carson City, NV 89703<br>Fax 1-775-883-4874</p></div></div>
<div class="way"><small>Clients</small><div><b>Existing clients</b><p><a href="/clients/" style="font-size:16px;border-bottom:1.5px solid var(--gold)">Renew, pay or schedule support &rarr;</a></p></div></div>
</div>"""),
              T('<span class="eyebrow">What to expect</span>'),
              X("""<ol class="expect"><li><b>We listen</b>Tell us where your business is today.</li><li><b>We explain</b>Your options, in plain English.</li><li><b>You decide</b>No pressure. Just a clear next step.</li></ol>"""),
              cls="ct-side"),
            C(H("Send us a note", "h2", ""), T('<p class="note">Tell us a little about your business and an advisor will get back to you.</p>'), form, cls="form-card"),
            cls="wrap ct-grid"), cls="sec", tag="section"),
        X('<iframe title="Map to Laughlin Associates" loading="lazy" style="display:block;width:100%;height:360px;border:0" src="https://maps.google.com/maps?q=680+W+Nye+Ln+Suite+202,+Carson+City,+NV+89703&amp;output=embed"></iframe>'),
    )


def stories():
    reset_ids("stories")
    return page(
        phero("Client stories", "Real owners. Real protection.",
              "Business owners who started with Laughlin, and stayed. In their own words.",
              None, "laughlin-advisor", "A Laughlin advisor in conversation with a client"),
        C(X("""<div class="wrap">
<div class="story"><div class="who"><small>Formation &amp; protection</small><h3>Dan Lincoln</h3><p>Bud the Spud Chip Trucks, Inc.</p><div class="tags"><span>Corporation</span><span>Ongoing compliance</span></div></div>
<blockquote>&ldquo;When I started my business, I knew I couldn't continue to run everything as a sole proprietor. But I really had no idea where to start. Thanks to your hand-holding, my business has been steered in the right direction and I have a proper understanding of my responsibilities to maintain my liability protection.&rdquo;</blockquote></div>
<div class="story"><div class="who"><small>Long-term client</small><h3>Kristin Summers</h3><p>Summers Life Balance Coaching</p><div class="tags"><span>Ongoing support</span></div></div>
<blockquote>&ldquo;The care and concern that I have always received from Laughlin Associates is very much appreciated. Your enthusiasm is very indicative of the attitude of your firm, helpful and willing to exert the maximum effort to ensure the success of your clients.&rdquo;</blockquote></div>
<div class="share"><div><h3>Have a Laughlin story?</h3><p>We'd love to feature how Laughlin helped your business. With your permission, of course.</p></div><a href="/contact/">Share your story &rarr;</a></div>
</div>"""), cls="sec", tag="section"),
        band("Start your own story.", "Form your company the right way, and keep it protected for years to come."),
    )
