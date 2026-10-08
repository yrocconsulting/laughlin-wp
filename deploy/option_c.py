"""Option C, "The Open Door": a heritage-led page built from the Laughlin
logo mark, a gold door opening inside a navy frame. The door shape frames the photography, so the page
could only belong to Laughlin."""
from lx import *

FONTQ = "family=Archivo:wght@500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"

# The logo mark, redrawn: a navy frame with a gold door swinging open.
MARK = '<svg class="mark" viewBox="0 0 60 80" aria-hidden="true"><path d="M0 14 L0 80 L28 76 L28 70 L8 72 L8 20 L28 18 L28 12 Z" fill="#0A2D64"/><path d="M12 6 L34 0 L34 72 L12 70 Z" fill="#F0BE28"/></svg>'

CSS = """
.lx-c{--bg:#F7F3EA;--ink:#16203A;--muted:#535C70;--navy:#0A2D64;--navy-2:#163E80;--gold:#F0BE28;--gold-ink:#8A6604;--line:#E2D9C6;--paper:#FFFDF8;--f-head:'Archivo',system-ui,sans-serif;--f-body:'Source Serif 4',Georgia,serif;--radius:2px}
.lx-c .elementor-button{font-family:'Archivo',sans-serif;letter-spacing:.01em}
.lx-c .nav a{font-family:'Archivo',sans-serif;font-weight:600}
.lx-c .util{font-family:'Archivo',sans-serif}
.lx-c .eyebrow{display:inline-flex;align-items:center;gap:10px;font-family:var(--f-head);font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--navy)}
.lx-c .eyebrow:before{content:"";width:5px;height:22px;background:var(--gold);transform:skewY(-12deg)}
.lx-c .sec{padding-top:112px;padding-bottom:112px}
.lx-c .h2 .elementor-heading-title{font-size:clamp(32px,3.8vw,50px);line-height:1.05;font-weight:700;letter-spacing:-.02em;color:var(--navy)}
.lx-c .lede{font-size:19px;color:var(--muted);max-width:620px}
.lx-c .mark{width:34px;height:auto;display:block}
/* hero */
.lx-c .hero{padding-top:40px;padding-bottom:100px;overflow:hidden}
.lx-c .hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}
.lx-c .hero-copy{gap:26px}
.lx-c .h1 .elementor-heading-title{font-size:clamp(46px,6.2vw,88px);line-height:.96;font-weight:800;letter-spacing:-.035em;color:var(--navy)}
.lx-c .h1 em{font-style:normal;color:var(--ink);font-weight:500;display:block;font-size:.5em;letter-spacing:-.01em;line-height:1.1;margin-top:14px;font-family:'Source Serif 4',serif;font-style:italic}
.lx-c .creds{display:flex;flex-wrap:wrap;gap:10px 28px;font-family:var(--f-head);font-size:14px;font-weight:600;color:var(--muted);padding-top:22px;border-top:1px solid var(--line)}
.lx-c .creds span:before{content:"";display:inline-block;width:7px;height:7px;background:var(--gold);margin-right:9px;transform:rotate(45deg) translateY(-2px)}
.lx-c .doorway{position:relative;height:640px}
.lx-c .doorway .frame{position:absolute;left:4%;top:6%;bottom:0;width:20%;background:var(--navy);clip-path:polygon(0 4%,100% 0,100% 100%,0 96%)}
.lx-c .doorway .panel{position:absolute;left:14%;top:0;bottom:3%;right:0;background:var(--gold);clip-path:polygon(0 8%,100% 0,100% 100%,0 96%)}
.lx-c .doorway .photo{position:absolute;left:18%;top:5%;bottom:7%;right:4%;clip-path:polygon(0 8%,100% 0,100% 100%,0 95%)}
.lx-c .doorway .tag{position:absolute;left:0;bottom:12%;background:var(--paper);padding:18px 22px;max-width:260px;box-shadow:0 24px 50px -28px rgba(10,45,100,.55);font-size:15px;line-height:1.4}
.lx-c .doorway .tag b{display:block;font-family:var(--f-head);font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink);margin-bottom:6px}
/* two front doors */
.lx-c .fronts{display:grid;grid-template-columns:1fr 1fr}
.lx-c .front{padding:80px 64px;display:flex;flex-direction:column;gap:18px}
.lx-c .front.f1{background:var(--navy);color:#E6ECF7}
.lx-c .front.f2{background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.lx-c .front small{font-family:var(--f-head);font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.lx-c .front.f2 small{color:var(--gold-ink)}
.lx-c .front h2{font-family:var(--f-head);font-size:clamp(28px,3vw,40px);line-height:1.08;font-weight:700;letter-spacing:-.02em;margin:0;color:#fff}
.lx-c .front.f2 h2{color:var(--navy)}
.lx-c .front p{font-size:18px;margin:0;max-width:520px}
.lx-c .front ul{list-style:none;margin:6px 0 10px;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:0 24px}
.lx-c .front li a{display:block;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.18);text-decoration:none;font-family:var(--f-head);font-weight:600;font-size:16px}
.lx-c .front.f2 li a{border-color:var(--line);color:var(--navy)}
.lx-c .front li a:after{content:" \\2192";color:var(--gold)}
.lx-c .front.f2 li a:after{color:var(--gold-ink)}
.lx-c .front .go{align-self:flex-start;display:inline-block;font-family:var(--f-head);font-weight:700;text-decoration:none;padding:15px 24px;background:var(--gold);color:var(--navy)}
.lx-c .front.f2 .go{background:var(--navy);color:#fff}
.lx-c .front.f1{padding-left:max(32px,calc((100vw - 1240px) / 2 + 32px))}
.lx-c .front.f2{padding-right:max(32px,calc((100vw - 1240px) / 2 + 32px))}
/* lifetime */
.lx-c .life-head{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:end;margin-bottom:56px}
.lx-c .life{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--line)}
.lx-c .phase{padding:30px 28px 0 0;position:relative}
.lx-c .phase:before{content:"";position:absolute;left:0;top:-3px;height:5px;background:var(--navy);width:calc(var(--w) * 1%)}
.lx-c .phase .n{font-family:var(--f-head);font-weight:800;font-size:64px;line-height:1;color:transparent;-webkit-text-stroke:1.5px var(--navy);opacity:.35}
.lx-c .phase h3{font-family:var(--f-head);font-size:28px;font-weight:700;color:var(--navy);margin:10px 0 4px;letter-spacing:-.01em}
.lx-c .phase .when{font-family:var(--f-head);font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .phase p{color:var(--muted);font-size:16px;margin:12px 0}
.lx-c .phase a{display:block;font-family:var(--f-head);font-size:15px;font-weight:600;color:var(--ink);text-decoration:none;padding:7px 0}
.lx-c .phase a:hover{color:var(--navy);text-decoration:underline;text-decoration-color:var(--gold)}
/* CVPS */
.lx-c .cvps{background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.lx-c .cv-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.lx-c .cv-copy{gap:22px}
.lx-c .diagram{background:var(--bg);padding:36px;border:1px solid var(--line)}
.lx-c .diagram svg{width:100%;height:auto;display:block}
.lx-c .diagram .cap{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px;font-size:15px}
.lx-c .diagram h4{font-family:var(--f-head);margin:0 0 6px;font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:var(--navy)}
.lx-c .diagram .bad h4{color:#B4410F}
.lx-c .how{counter-reset:h;display:grid;grid-template-columns:1fr 1fr;gap:16px 28px;list-style:none;margin:8px 0;padding:0}
.lx-c .how li{counter-increment:h;font-size:16px;padding-top:12px;border-top:2px solid var(--navy)}
.lx-c .how li b{display:block;font-family:var(--f-head);color:var(--navy);font-size:16px;margin-bottom:2px}
.lx-c .how li b:before{content:counter(h) ". ";color:var(--gold-ink)}
/* heritage */
.lx-c .her{display:grid;grid-template-columns:1.1fr .9fr;gap:80px;align-items:center}
.lx-c .her-copy{gap:24px}
.lx-c .big71{font-family:var(--f-head);font-weight:800;font-size:clamp(90px,12vw,170px);line-height:.85;letter-spacing:-.05em;color:var(--navy);display:flex;align-items:flex-end;gap:18px}
.lx-c .big71 .mark{width:70px}
.lx-c .her-copy .quote{font-size:22px;font-style:italic;line-height:1.45;border-left:4px solid var(--gold);padding-left:22px;margin:6px 0}
.lx-c .her-copy .quote cite{display:block;font-style:normal;font-family:var(--f-head);font-size:14px;font-weight:600;color:var(--muted);margin-top:10px}
.lx-c .her-media{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:300px 220px;gap:14px}
.lx-c .her-media .elementor-widget-image:first-child{grid-column:1 / 3}
.lx-c .figcap{grid-column:1 / 3;font-size:14px;color:var(--muted);font-style:italic}
.lx-c .facts{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.lx-c .facts div{padding:18px 16px 18px 0}
.lx-c .facts b{display:block;font-family:var(--f-head);font-size:24px;font-weight:800;color:var(--navy)}
.lx-c .facts span{font-size:14px;color:var(--muted)}
/* answers */
.lx-c .ans{background:var(--navy);color:#DCE4F2}
.lx-c .ans .h2 .elementor-heading-title{color:#fff}
.lx-c .ans .eyebrow{color:#fff}
.lx-c .ans .lede{color:#B9C6DE}
.lx-c .ans-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px}
.lx-c .ans-side{gap:22px;position:sticky;top:24px}
.lx-c .ans-side .ph{height:300px}
.lx-c .qa details{border-top:1px solid rgba(255,255,255,.18)}
.lx-c .qa details:last-child{border-bottom:1px solid rgba(255,255,255,.18)}
.lx-c .qa summary{list-style:none;cursor:pointer;padding:24px 40px 24px 0;font-family:var(--f-head);font-size:22px;font-weight:600;color:#fff;position:relative;line-height:1.25}
.lx-c .qa summary::-webkit-details-marker{display:none}
.lx-c .qa summary:after{content:"";position:absolute;right:6px;top:32px;width:10px;height:10px;border-right:2px solid var(--gold);border-bottom:2px solid var(--gold);transform:rotate(45deg);transition:transform .2s}
.lx-c .qa details[open] summary:after{transform:rotate(-135deg)}
.lx-c .qa p{margin:0;padding:0 40px 24px 0;font-size:17px;color:#C9D4E8}
.lx-c .btn-ghost-w .elementor-button{background:transparent;border-color:#fff;color:#fff}
.lx-c .btn-ghost-w .elementor-button:hover{background:#fff;color:var(--navy)}
/* next steps */
.lx-c .steps{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:48px}
.lx-c .st{grid-column:span 2;background:var(--paper);border:1px solid var(--line);padding:28px;text-decoration:none;display:flex;flex-direction:column;gap:8px;transition:border-color .2s,transform .2s}
.lx-c .st:hover{border-color:var(--navy);transform:translateY(-3px)}
.lx-c .st.wide{grid-column:span 3}
.lx-c .st small{font-family:var(--f-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)}
.lx-c .st strong{font-family:var(--f-head);font-size:24px;line-height:1.15;color:var(--navy);letter-spacing:-.01em}
.lx-c .st span{font-size:16px;color:var(--muted)}
.lx-c .st.hl{background:var(--gold);border-color:var(--gold)}
.lx-c .st.hl small{color:var(--navy)}
.lx-c .st.hl span{color:var(--ink)}
/* clients */
.lx-c .clients{border-top:1px solid var(--line);background:var(--paper)}
.lx-c .cl{display:grid;grid-template-columns:auto 1fr;gap:48px;align-items:center;padding-top:44px;padding-bottom:44px}
.lx-c .cl h2{font-family:var(--f-head);font-size:26px;color:var(--navy);margin:0;display:flex;gap:14px;align-items:center}
.lx-c .cl nav{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end}
.lx-c .cl nav a{font-family:var(--f-head);font-weight:600;font-size:15px;text-decoration:none;padding:11px 16px;border:1px solid var(--navy);color:var(--navy)}
.lx-c .cl nav a:hover{background:var(--navy);color:#fff}
@media (max-width:1100px){
 .lx-c .hero-grid,.lx-c .cv-grid,.lx-c .her,.lx-c .ans-grid,.lx-c .life-head,.lx-c .cl{grid-template-columns:1fr;gap:44px}
 .lx-c .fronts{grid-template-columns:1fr}
 .lx-c .front.f1{padding-right:32px}
 .lx-c .front.f2{padding-left:max(32px,calc((100vw - 1240px) / 2 + 32px))}
 .lx-c .life{grid-template-columns:1fr 1fr;row-gap:36px}
 .lx-c .steps{grid-template-columns:1fr 1fr}
 .lx-c .st,.lx-c .st.wide{grid-column:span 1}
 .lx-c .doorway{height:520px}
 .lx-c .ans-side{position:static}
 .lx-c .cl nav{justify-content:flex-start}
}
@media (max-width:640px){
 .lx-c .sec{padding-top:72px;padding-bottom:72px}
 .lx-c .front,.lx-c .front.f1,.lx-c .front.f2{padding:48px 18px}
 .lx-c .front ul,.lx-c .life,.lx-c .steps,.lx-c .how,.lx-c .facts,.lx-c .diagram .cap{grid-template-columns:1fr}
 .lx-c .doorway{height:420px}
 .lx-c .doorway .tag{position:relative;left:auto;bottom:auto;margin-top:440px;max-width:none}
 .lx-c .her-media{grid-template-rows:220px 160px}
 .lx-c .diagram{padding:20px}
}
"""

DIAGRAM = """<svg viewBox="0 0 520 250" role="img" aria-label="The corporate veil separates business liabilities from personal assets">
<rect x="10" y="40" width="190" height="170" fill="#FFFDF8" stroke="#0A2D64" stroke-width="2"/>
<text x="105" y="30" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="13" fill="#0A2D64" letter-spacing="2">YOUR COMPANY</text>
<text x="105" y="95" text-anchor="middle" font-family="Archivo" font-size="15" fill="#16203A">Contracts</text>
<text x="105" y="130" text-anchor="middle" font-family="Archivo" font-size="15" fill="#16203A">Business debts</text>
<text x="105" y="165" text-anchor="middle" font-family="Archivo" font-size="15" fill="#16203A">Lawsuits</text>
<path d="M250 20 L272 14 L272 236 L250 230 Z" fill="#F0BE28"/>
<text x="261" y="125" text-anchor="middle" font-family="Archivo" font-weight="800" font-size="11" fill="#0A2D64" letter-spacing="2" transform="rotate(-90 261 125)">CORPORATE VEIL</text>
<rect x="320" y="40" width="190" height="170" fill="#0A2D64"/>
<text x="415" y="30" text-anchor="middle" font-family="Archivo" font-weight="700" font-size="13" fill="#0A2D64" letter-spacing="2">YOU &amp; YOUR FAMILY</text>
<text x="415" y="95" text-anchor="middle" font-family="Archivo" font-size="15" fill="#fff">Your home</text>
<text x="415" y="130" text-anchor="middle" font-family="Archivo" font-size="15" fill="#fff">Savings</text>
<text x="415" y="165" text-anchor="middle" font-family="Archivo" font-size="15" fill="#fff">Personal assets</text>
<path d="M205 125 L240 125" stroke="#B4410F" stroke-width="2" stroke-dasharray="4 4"/><path d="M234 119 L242 125 L234 131" fill="none" stroke="#B4410F" stroke-width="2"/>
</svg>
<div class="cap"><div><h4>When it's maintained</h4>Business claims stop at the company. Your personal assets stay out of reach.</div><div class="bad"><h4>When it's neglected</h4>Missed filings, no minutes or mixed finances can let a court &ldquo;pierce the veil.&rdquo;</div></div>"""


def build():
    reset_ids("c")
    whens = ["Day one", "Every year", "As you scale", "What comes next"]
    widths = [25, 50, 75, 100]
    life = "".join(
        f'<div class="phase" style="--w:{w}"><div class="n">0{i+1}</div><span class="when">{wh}</span><h3>{n}</h3><p>{d}</p>'
        + "".join(f'<a href="#{n.lower()}">{x}</a>' for x in items) + "</div>"
        for i, ((n, d, items), wh, w) in enumerate(zip(STAGES, whens, widths)))
    qa = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(QUESTIONS))
    return [C(
        style(FONTQ, CSS),
        header("Start your entity"),
        # HERO
        C(C(
            C(T(f'<span class="eyebrow">Laughlin &middot; Since 1971</span>'),
              H("Formation is only the beginning. <em>We open the door, then stay with you for everything that comes after.</em>", "h1", "h1"),
              T("<p>For more than 55 years, Laughlin has helped business owners start the right entity, protect what they've built, grow with confidence and plan for what's next.</p>", "lede"),
              C(B("Start your entity", "#formation", "btn-gold"), B("Protect a business I own", "#protect", "btn-ghost"), cls="btns"),
              X('<div class="creds"><span>Real advisors you can call</span><span>Nationwide</span><span>2026 Inc. 5000 Honoree</span></div>'),
              cls="hero-copy"),
            C(X('<div class="frame"></div><div class="panel"></div>'),
              I("owner-cafe", "photo", "A business owner standing in the doorway of her shop"),
              X(f'<div class="tag"><b>Talk to a real person</b>Questions about your business? <a href="{TEL}"><strong>{PHONE}</strong></a></div>'),
              cls="doorway"),
            cls="wrap hero-grid"), cls="hero", tag="section"),
        # TWO FRONT DOORS
        X(f"""<section class="fronts">
<div class="front f1" id="formation"><small id="start">Starting a business</small><h2>Form your LLC or corporation, with people who've done it since 1971.</h2>
<p>File in any state. We'll help you choose the right structure and set it up so it protects you from day one.</p>
<ul><li><a href="#formation">Form an LLC</a></li><li><a href="#formation">Form a corporation</a></li><li><a href="#formation">Nonprofits</a></li><li><a href="#formation">Compare entity types</a></li></ul>
<a class="go" href="#formation">Start your entity &rarr;</a></div>
<div class="front f2" id="protect"><small>Already own a business</small><h2>Keep your company protecting you, year after year.</h2>
<p>Our Corporate Veil Protection Service handles the upkeep formation-only companies leave to you.</p>
<ul><li><a href="#cvps">Corporate Veil Protection</a></li><li><a href="#protect">Registered agent</a></li><li><a href="#protect">Minutes &amp; records</a></li><li><a href="#review">Free business review</a></li></ul>
<a class="go" href="#cvps">Explore CVPS &rarr;</a></div>
</section>"""),
        # LIFETIME
        C(C(
            C(C(T('<span class="eyebrow" id="grow">The Laughlin way</span>'),
                H("Start. Protect. Grow. Preserve.", "h2", "h2"), cls=""),
              T("<p>A business isn't a single filing. It's decades of decisions. Laughlin is built to be there through all of them, not just the first day.</p>", "lede"),
              cls="life-head"),
            X(f'<div class="life">{life}</div>'),
            cls="wrap"), cls="sec", tag="section"),
        # CVPS
        C(C(
            C(T('<span class="eyebrow" id="cvps">Corporate Veil Protection Service</span>'),
              H("What is the corporate veil, and why should you care?", "h2", "h2"),
              T("<p>When you form an LLC or corporation, the law treats it as separate from you. That separation, the <em>corporate veil</em>, is what keeps business debts and lawsuits away from your personal assets.</p><p>But the veil only holds if the company is run like a separate business. That's where most owners fall behind, and where Laughlin helps.</p>", "lede"),
              X("""<ol class="how">
<li><b>We track your deadlines</b>Annual filings and renewals, so nothing lapses.</li>
<li><b>We help with minutes</b>Meetings and resolutions documented properly.</li>
<li><b>We keep records in order</b>The proof your company is truly separate.</li>
<li><b>We review with you yearly</b>A real advisor checks your structure still fits.</li>
</ol>"""),
              C(B("Explore Corporate Veil Protection", "#cvps"), B("Get a free business review", "#review", "btn-link"), cls="btns"),
              cls="cv-copy"),
            X(f'<div class="diagram">{DIAGRAM}</div>'),
            cls="wrap cv-grid"), cls="sec cvps", tag="section"),
        # HERITAGE
        C(C(
            C(X(f'<div class="big71" id="story">1971 {MARK}</div>'),
              H("Fifty-five years of business owners, not just filings.", "h2", "h2"),
              T("<p>Harley Laughlin was an independent truck driver who believed small businesses deserved the same protections big companies take for granted. He started Laughlin in 1971 to provide them.</p><p>Since then we've helped thousands of owners across the country. We've seen the mistakes that cost the most, and we've built our services around preventing them.</p>", "lede"),
              X("""<div class="facts"><div><b>Thousands</b><span>of businesses supported</span></div><div><b>Nationwide</b><span>service in every state</span></div><div><b>Inc. 5000</b><span>2026 honoree</span></div></div>
<p class="quote">&ldquo;My business has been steered in the right direction and I have a proper understanding of my responsibilities to maintain my liability protection.&rdquo;<cite>Dan Lincoln, Bud the Spud Chip Trucks, Inc.</cite></p>"""),
              cls="her-copy"),
            C(I("laughlin-roundtable", "", "Business owners at a Laughlin workshop"),
              I("laughlin-1on1", "", "Advisor and client in conversation"),
              I("aaron-speaking", "", "Aaron Young speaking at a Laughlin event"),
              T('<p class="figcap">Laughlin workshops and one-on-one guidance. Archival photos from the early years would go here.</p>'),
              cls="her-media"),
            cls="wrap her"), cls="sec", tag="section"),
        # ANSWERS
        C(C(
            C(T('<span class="eyebrow" id="learn">Straight answers</span>'),
              H("What business owners ask us every day.", "h2", "h2"),
              T("<p>Education has been part of Laughlin for decades. Here are plain-English answers. Want to go deeper? Join a live Q&amp;A.</p>", "lede"),
              I("laughlin-planning", "ph", "A business owner working through a plan at a Laughlin session"),
              C(B("Join a live Q&amp;A", "#learn", "btn-gold"), B("Free guides", "#learn", "btn-ghost-w"), cls="btns"),
              cls="ans-side"),
            X(f'<div class="qa">{qa}</div>'),
            cls="wrap ans-grid"), cls="sec ans", tag="section"),
        # NEXT STEPS
        C(C(
            C(T('<span class="eyebrow" id="advisors">Your next step</span>'),
              H("Ready to talk, or just getting started? Choose your next step.", "h2", "h2"), cls=""),
            X(f"""<div class="steps" id="review">
<a class="st wide hl" href="#formation"><small>Ready now</small><strong>Start your LLC or corporation</strong><span>Form in any state, set up right.</span></a>
<a class="st wide" href="{TEL}"><small>Talk it through</small><strong>Speak with an advisor &middot; {PHONE}</strong><span>No pressure, just answers.</span></a>
<a class="st" href="#cvps"><small>Protect</small><strong>Explore CVPS</strong><span>Keep your veil intact.</span></a>
<a class="st" href="#review"><small>Assess</small><strong>Free business review</strong><span>Is your structure still right?</span></a>
<a class="st" href="#learn"><small>Learn</small><strong>Attend a webinar</strong><span>Live and free, every month.</span></a>
</div>"""),
            cls="wrap"), cls="sec", tag="section"),
        # CLIENTS
        X(f"""<section class="clients" id="clients"><div class="wrap cl"><h2>{MARK} Existing clients</h2>
<nav><a href="#clients">Renew Registered Agent</a><a href="#clients">Renew CVPS</a><a href="#clients">Make a Payment</a><a href="#clients">Schedule Client Support</a><a href="#clients">Client Resources</a></nav></div></section>"""),
        footer(),
        cls="lx lx-c")]
