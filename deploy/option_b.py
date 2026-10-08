"""Option B, "Real Answers, Real People": a bright, conversational page led by
the questions business owners ask. Uses a humanist sans, rounded shapes and people front and center."""
from lx import *

FONTQ = "family=Figtree:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500"

CSS = """
.lx-b{--bg:#FFFFFF;--ink:#0F1B33;--muted:#4F5B72;--navy:#0A2D64;--navy-2:#1A4590;--gold:#F0BE28;--gold-ink:#8C6A05;--line:#E3E8F0;--mist:#F1F4F9;--cream:#FFF8E6;--f-head:'Figtree',system-ui,sans-serif;--f-body:'Figtree',system-ui,sans-serif;--radius:999px;--r:22px}
.lx-b .hdr{border-bottom:1px solid var(--line)}
.lx-b .util{background:var(--navy);color:#fff;border:0}
.lx-b .util a{color:#fff}
.lx-b .util .tel{color:var(--gold)}
.lx-b .nav .cta{border-radius:999px}
.lx-b .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:700;color:var(--navy);background:var(--cream);padding:6px 14px;border-radius:99px}
.lx-b .eyebrow:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--gold)}
.lx-b .sec{padding-top:104px;padding-bottom:104px}
.lx-b .h2 .elementor-heading-title{font-size:clamp(32px,3.8vw,50px);line-height:1.08;font-weight:700;letter-spacing:-.025em;color:var(--ink)}
.lx-b .lede{font-size:19px;color:var(--muted);max-width:640px}
.lx-b .center{text-align:center;align-items:center}
.lx-b .center .lede{margin-left:auto;margin-right:auto}
/* hero */
.lx-b .hero{padding-top:72px;padding-bottom:40px;background:linear-gradient(180deg,var(--mist),#fff 85%)}
.lx-b .hero-top{gap:22px;max-width:900px;margin:0 auto}
.lx-b .h1 .elementor-heading-title{font-size:clamp(42px,5.6vw,76px);line-height:1;font-weight:800;letter-spacing:-.035em;color:var(--ink)}
.lx-b .h1 em{font-style:normal;color:var(--navy);background:linear-gradient(transparent 68%,rgba(240,190,40,.55) 68% 92%,transparent 92%)}
.lx-b .where{margin-top:48px}
.lx-b .where h2{font-size:15px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:center;margin:0 0 18px;font-family:var(--f-body)}
.lx-b .doors{display:grid;grid-template-columns:1.15fr 1.15fr .9fr;gap:18px}
.lx-b .door{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:330px;border-radius:var(--r);overflow:hidden;text-decoration:none;color:#fff;isolation:isolate;transition:transform .25s}
.lx-b .door:hover{transform:translateY(-4px)}
.lx-b .door img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform .5s}
.lx-b .door:hover img{transform:scale(1.04)}
.lx-b .door:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(10,25,55,0) 30%,rgba(10,25,55,.88))}
.lx-b .door .d-in{padding:26px}
.lx-b .door small{display:inline-block;font-size:13px;font-weight:700;background:rgba(255,255,255,.18);backdrop-filter:blur(6px);padding:5px 12px;border-radius:99px;margin-bottom:12px}
.lx-b .door strong{display:block;font-size:27px;line-height:1.12;font-weight:700;letter-spacing:-.01em}
.lx-b .door span{display:inline-flex;margin-top:14px;font-weight:700;background:var(--gold);color:var(--navy);padding:10px 16px;border-radius:99px;font-size:15px}
.lx-b .door.client{background:var(--navy)}
.lx-b .door.client:after{display:none}
.lx-b .door.client ul{list-style:none;margin:10px 0 0;padding:0}
.lx-b .door.client li{padding:7px 0;border-top:1px solid rgba(255,255,255,.18);font-weight:600;font-size:15px}
.lx-b .door.client li:after{content:" \\2192";color:var(--gold)}
.lx-b .trust{display:flex;justify-content:center;gap:12px 36px;flex-wrap:wrap;margin-top:34px;font-size:15px;color:var(--muted)}
.lx-b .trust b{color:var(--ink)}
/* conversation */
.lx-b .convo{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.lx-b .c-media{position:relative;height:540px}
.lx-b .c-media .m1{position:absolute;inset:0 90px 70px 0;border-radius:var(--r);overflow:hidden}
.lx-b .c-media .m2{position:absolute;right:0;bottom:0;width:46%;height:46%;border-radius:var(--r);overflow:hidden;border:6px solid #fff}
.lx-b .bubble{position:absolute;background:#fff;border-radius:18px;padding:14px 18px;font-weight:600;font-size:15px;box-shadow:0 18px 40px -18px rgba(15,27,51,.35);max-width:260px;line-height:1.35}
.lx-b .bubble.q{left:-18px;top:36px;border-bottom-left-radius:4px}
.lx-b .bubble.a{left:30%;bottom:16px;background:var(--navy);color:#fff;border-bottom-right-radius:4px}
.lx-b .bubble small{display:block;font-size:12px;font-weight:700;opacity:.65;margin-bottom:4px;text-transform:uppercase;letter-spacing:.06em}
.lx-b .c-copy{gap:22px}
/* questions */
.lx-b .ask{background:var(--mist)}
.lx-b .ask-head{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;margin-bottom:44px;flex-direction:row}
.lx-b .qs{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.lx-b .qcard{background:#fff;border-radius:var(--r);padding:28px;display:flex;flex-direction:column;gap:12px;text-decoration:none;border:1px solid transparent;transition:border-color .2s,transform .2s}
.lx-b .qcard:hover{border-color:var(--navy);transform:translateY(-3px)}
.lx-b .qcard .qm{width:38px;height:38px;border-radius:50%;background:var(--cream);color:var(--gold-ink);font-weight:800;display:flex;align-items:center;justify-content:center;font-size:18px}
.lx-b .qcard strong{font-size:21px;line-height:1.2;color:var(--ink);letter-spacing:-.01em}
.lx-b .qcard p{font-size:15px;color:var(--muted);margin:0}
.lx-b .qcard em{margin-top:auto;font-style:normal;font-weight:700;color:var(--navy);font-size:15px}
.lx-b .qcard.ask-us{background:var(--navy);color:#fff}
.lx-b .qcard.ask-us strong{color:#fff}
.lx-b .qcard.ask-us p{color:#C9D4E8}
.lx-b .qcard.ask-us em{color:var(--gold)}
/* CVPS */
.lx-b .cv{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.lx-b .cv-copy{gap:22px}
.lx-b .veil{background:var(--cream);border-radius:28px;padding:36px;display:grid;grid-template-columns:1fr 18px 1fr;gap:20px;align-items:stretch}
.lx-b .side{background:#fff;border-radius:18px;padding:22px}
.lx-b .side h4{margin:0 0 10px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.lx-b .side ul{list-style:none;margin:0;padding:0}
.lx-b .side li{padding:8px 0;border-top:1px solid var(--line);font-weight:600;font-size:15px}
.lx-b .wall{background:repeating-linear-gradient(180deg,var(--gold) 0 26px,#E2A90F 26px 30px);border-radius:6px;position:relative}
.lx-b .wall:after{content:"Corporate veil";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap;font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--navy)}
.lx-b .check{grid-column:1 / -1;background:#fff;border-radius:18px;padding:22px}
.lx-b .check h4{margin:0 0 6px;font-size:18px;color:var(--ink)}
.lx-b .check label{display:flex;gap:10px;align-items:flex-start;padding:8px 0;font-size:15px;cursor:pointer}
.lx-b .check input{accent-color:var(--navy);width:18px;height:18px;margin-top:2px;flex:0 0 18px}
.lx-b .check .res{margin-top:10px;font-size:14px;color:var(--muted)}
/* stairs */
.lx-b .stairs{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:end;margin-top:56px}
.lx-b .step{border-radius:var(--r);padding:26px;display:flex;flex-direction:column;gap:10px;background:var(--mist);text-decoration:none}
.lx-b .step:nth-child(1){min-height:250px}
.lx-b .step:nth-child(2){min-height:310px;background:#E6ECF6}
.lx-b .step:nth-child(3){min-height:370px;background:#D7E1F1}
.lx-b .step:nth-child(4){min-height:430px;background:var(--navy);color:#fff}
.lx-b .step b{font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink)}
.lx-b .step:nth-child(4) b{color:var(--gold)}
.lx-b .step h3{margin:0;font-size:30px;font-weight:800;letter-spacing:-.02em}
.lx-b .step p{font-size:15px;opacity:.85;margin:0}
.lx-b .step ul{list-style:none;padding:0;margin:auto 0 0}
.lx-b .step li{font-size:14px;font-weight:600;padding:6px 0;border-top:1px solid rgba(15,27,51,.12)}
.lx-b .step:nth-child(4) li{border-color:rgba(255,255,255,.2)}
/* formation strip */
.lx-b .form{background:var(--navy);color:#fff;border-radius:32px;padding:56px;display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
.lx-b .form h2{color:#fff;font-size:clamp(30px,3.4vw,44px);line-height:1.1;font-weight:800;margin:0 0 12px;letter-spacing:-.02em}
.lx-b .form p{color:#C9D4E8;font-size:17px}
.lx-b .chips{display:flex;flex-wrap:wrap;gap:10px}
.lx-b .chips a{background:rgba(255,255,255,.1);color:#fff;text-decoration:none;padding:12px 18px;border-radius:99px;font-weight:700;border:1px solid rgba(255,255,255,.2)}
.lx-b .chips a:hover{background:#fff;color:var(--navy)}
.lx-b .chips a.go{background:var(--gold);color:var(--navy);border-color:var(--gold)}
.lx-b .form .small{font-size:14px;margin-top:16px;color:#C9D4E8}
.lx-b .form .small a{color:#fff;font-weight:700}
/* story */
.lx-b .story{display:grid;grid-template-columns:.9fr 1.1fr;gap:72px;align-items:center}
.lx-b .s-media{height:560px;border-radius:var(--r);overflow:hidden}
.lx-b .s-copy{gap:22px}
.lx-b .tl{list-style:none;margin:8px 0 0;padding:0;border-left:2px solid var(--line)}
.lx-b .tl li{position:relative;padding:0 0 22px 26px}
.lx-b .tl li:before{content:"";position:absolute;left:-7px;top:6px;width:12px;height:12px;border-radius:50%;background:#fff;border:2px solid var(--navy)}
.lx-b .tl li:last-child:before{background:var(--gold);border-color:var(--gold)}
.lx-b .tl b{display:block;font-size:20px;color:var(--navy)}
.lx-b .tl span{color:var(--muted);font-size:15px}
.lx-b .tq{background:var(--mist);border-radius:18px;padding:24px;font-size:17px;font-weight:500}
.lx-b .tq cite{display:block;font-style:normal;font-weight:700;font-size:14px;color:var(--muted);margin-top:10px}
/* learn */
.lx-b .learn{background:var(--mist)}
.lx-b .ev{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:18px;margin-top:44px}
.lx-b .ecard{background:#fff;border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;text-decoration:none}
.lx-b .ecard img{width:100%;height:220px;object-fit:cover;display:block}
.lx-b .ecard .e-in{padding:24px;display:flex;flex-direction:column;gap:8px;flex:1}
.lx-b .ecard small{font-size:13px;font-weight:700;color:var(--gold-ink)}
.lx-b .ecard strong{font-size:22px;line-height:1.2;color:var(--ink)}
.lx-b .ecard p{font-size:15px;color:var(--muted);margin:0}
.lx-b .ecard em{font-style:normal;font-weight:700;color:var(--navy);margin-top:auto;padding-top:10px}
.lx-b .ecard.big img{height:300px}
/* clients + final */
.lx-b .final{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.lx-b .panel{border-radius:28px;padding:44px;display:flex;flex-direction:column;gap:14px}
.lx-b .panel h2{margin:0;font-size:34px;line-height:1.1;font-weight:800;letter-spacing:-.02em}
.lx-b .panel.talk{background:var(--cream)}
.lx-b .panel.cl{background:var(--mist)}
.lx-b .panel .links{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px}
.lx-b .panel .links a{background:#fff;border-radius:14px;padding:14px 16px;text-decoration:none;font-weight:700;color:var(--navy);font-size:15px}
.lx-b .panel .links a:hover{background:var(--navy);color:#fff}
.lx-b .panel .tel{font-size:36px;font-weight:800;color:var(--navy);text-decoration:none;letter-spacing:-.02em}
@media (max-width:1100px){
 .lx-b .doors{grid-template-columns:1fr 1fr}
 .lx-b .door.client{grid-column:1 / -1;min-height:auto}
 .lx-b .convo,.lx-b .cv,.lx-b .story,.lx-b .form,.lx-b .final{grid-template-columns:1fr;gap:44px}
 .lx-b .qs{grid-template-columns:1fr 1fr}
 .lx-b .stairs{grid-template-columns:1fr 1fr}
 .lx-b .step{min-height:0!important}
 .lx-b .ev{grid-template-columns:1fr 1fr}
 .lx-b .ask-head{flex-direction:column;align-items:flex-start}
}
@media (max-width:640px){
 .lx-b .sec{padding-top:68px;padding-bottom:68px}
 .lx-b .doors,.lx-b .qs,.lx-b .stairs,.lx-b .ev,.lx-b .panel .links{grid-template-columns:1fr}
 .lx-b .door{min-height:260px}
 .lx-b .c-media{height:420px}
 .lx-b .c-media .m1{inset:0 0 90px 0}
 .lx-b .bubble.q{left:10px}
 .lx-b .veil{grid-template-columns:1fr;padding:20px}
 .lx-b .wall{height:44px}
 .lx-b .wall:after{transform:translate(-50%,-50%)}
 .lx-b .form{padding:32px 24px;border-radius:24px}
 .lx-b .panel{padding:28px}
 .lx-b .s-media{height:360px}
}
"""


def build():
    reset_ids("b")
    qcards = "".join(f'<a class="qcard" href="#learn"><span class="qm">?</span><strong>{q}</strong><p>{a}</p><em>Read the answer &rarr;</em></a>'
                     for q, a in QUESTIONS[:5])
    qcards += f'<a class="qcard ask-us" href="{TEL}"><span class="qm">&hellip;</span><strong>Have a different question?</strong><p>Ask a Laughlin advisor. Real people, real answers, no ticket queue.</p><em>Call {PHONE} &rarr;</em></a>'
    steps = "".join(f'<a class="step" href="#{n.lower()}"><b>Stage {i+1}</b><h3>{n}</h3><p>{d}</p><ul>'
                    + "".join(f"<li>{x}</li>" for x in items) + "</ul></a>" for i, (n, d, items) in enumerate(STAGES))
    return [C(
        style(FONTQ, CSS),
        header("Start your entity"),
        # HERO
        C(C(
            C(T('<span class="eyebrow">Real advisors since 1971</span>'),
              H("Real answers for <em>every stage</em> of your business.", "h1", "h1"),
              T("<p>Start the right entity, keep it protected and plan what comes next, with people who've guided business owners for more than 55 years.</p>", "lede"),
              cls="hero-top center"),
            X(f"""<div class="where"><h2>Where are you today?</h2><div class="doors">
<a class="door" href="#formation"><img src="lx:owner-cafe" alt=""><div class="d-in"><small>I'm starting a business</small><strong>Form your LLC or corporation, the right way.</strong><span>Start your entity &rarr;</span></div></a>
<a class="door" href="#protect"><img src="lx:owner-workshop" alt=""><div class="d-in"><small>I already own a business</small><strong>Protect, maintain and strengthen it.</strong><span>Explore protection &rarr;</span></div></a>
<a class="door client" href="#clients"><div class="d-in"><small>I'm a Laughlin client</small><strong>Welcome back.</strong><ul><li>Renew services</li><li>Make a payment</li><li>Client support</li></ul></div></a>
</div>
<div class="trust"><span><b>55+ years</b> helping owners</span><span><b>Thousands</b> of businesses supported</span><span><b>2026</b> Inc. 5000 honoree</span><span><b>Nationwide</b> service</span></div></div>"""),
            cls="wrap"), cls="hero", tag="section"),
        # CONVERSATION
        C(C(
            C(I("laughlin-advisor", "m1", "A Laughlin advisor in conversation with a business owner"),
              I("laughlin-1on1", "m2", "One-on-one guidance"),
              X('<div class="bubble q"><small>Business owner</small>Is my LLC actually protecting me?</div><div class="bubble a"><small>Laughlin advisor</small>Let\'s look at your records together. Here\'s what to check.</div>'),
              cls="c-media"),
            C(T('<span class="eyebrow" id="advisors">You\'re not on your own</span>'),
              H("Formation is only the beginning. That's where most companies leave you.", "h2", "h2"),
              T("<p>Online filing services stop once your paperwork is accepted. But the questions start after that: what to file, what to keep, what could put your personal assets at risk.</p><p>At Laughlin you can call and talk to an advisor who knows business structure. We'll explain it in plain English and help you keep up.</p>", "lede"),
              C(B(f"Talk with an advisor", TEL), B("Attend a free live Q&amp;A", "#learn", "btn-ghost"), cls="btns"),
              cls="c-copy"),
            cls="wrap convo"), cls="sec", tag="section"),
        # QUESTIONS
        C(C(
            C(C(T('<span class="eyebrow" id="learn">Ask Laughlin</span>'),
                H("The questions owners ask us most.", "h2", "h2"), cls=""),
              B("Browse all answers", "#learn", "btn-link"), cls="ask-head"),
            X(f'<div class="qs">{qcards}</div>'),
            cls="wrap"), cls="sec ask", tag="section"),
        # CVPS
        C(C(
            C(T('<span class="eyebrow" id="protect">Corporate Veil Protection Service</span>'),
              H("Your company protects your personal assets, as long as it's maintained.", "h2", "h2"),
              T("<p>Forming an LLC or corporation puts a legal wall, the <strong>corporate veil</strong>, between your business and your personal life. If the company isn't kept up, a court can look past that wall and reach your home and savings.</p><p>Our Corporate Veil Protection Service keeps the wall standing: deadline reminders, help with minutes and resolutions, organized records and an annual check-in with a real advisor.</p>", "lede"),
              C(B("Explore Corporate Veil Protection", "#protect"), B("Get a free business review", "#review", "btn-ghost"), cls="btns"),
              cls="cv-copy"),
            X("""<div class="veil">
<div class="side"><h4>Your business</h4><ul><li>Contracts</li><li>Business debts</li><li>Lawsuits</li></ul></div>
<div class="wall" aria-hidden="true"></div>
<div class="side"><h4>Your personal life</h4><ul><li>Your home</li><li>Your savings</li><li>Your family</li></ul></div>
<div class="check" id="review"><h4>Quick self-check: is your wall solid?</h4>
<label><input type="checkbox"> We keep written minutes of major decisions</label>
<label><input type="checkbox"> Business and personal money are in separate accounts</label>
<label><input type="checkbox"> Our state filings and registered agent are current</label>
<label><input type="checkbox"> Contracts are signed in the company's name</label>
<p class="res">Missed any? That's common, and fixable. <a href="#review"><strong>Request a free business review &rarr;</strong></a></p></div>
</div>"""),
            cls="wrap cv"), cls="sec", tag="section"),
        # STAIRS
        C(C(
            C(T('<span class="eyebrow" id="grow">One relationship, every stage</span>'),
              H("Start. Protect. Grow. Preserve.", "h2", "h2"),
              T("<p>As your business climbs, your needs change. We're with you at every step.</p>", "lede"),
              cls="center"),
            X(f'<div class="stairs">{steps}</div>'),
            cls="wrap"), cls="sec", tag="section"),
        # FORMATION
        C(X(f"""<div class="wrap"><div class="form" id="formation"><div>
<h2 id="start">Ready to form your company? Start in minutes.</h2>
<p>File your LLC or corporation in any state, with real people checking the details and answering your questions along the way.</p></div>
<div><div class="chips"><a class="go" href="#formation">Start an LLC &rarr;</a><a href="#formation">Corporation</a><a href="#formation">S-Corp</a><a href="#formation">Nonprofit</a><a href="#formation">Compare entities</a></div>
<p class="small">Not sure which entity fits? <a href="{TEL}">Call {PHONE}</a> and we'll help you decide.</p></div></div></div>"""),
          cls="sec", tag="section"),
        # STORY
        C(C(
            I("laughlin-roundtable", "s-media", "Business owners at a Laughlin event"),
            C(T('<span class="eyebrow" id="story">Since 1971</span>'),
              H("Fifty-five years of helping owners avoid costly mistakes.", "h2", "h2"),
              X("""<ul class="tl">
<li><b>1971</b><span>Harley Laughlin, an independent truck driver, starts Laughlin to give entrepreneurs the same resources as big business.</span></li>
<li><b>Decades of education</b><span>Workshops, guides and live Q&amp;A for business owners all over the country.</span></li>
<li><b>Today</b><span>Thousands of businesses supported, a 2026 Inc. 5000 honoree, and still answering the phone.</span></li>
</ul>
<div class="tq">&ldquo;The care and concern that I have always received from Laughlin Associates is very much appreciated.&rdquo;<cite>Kristin Summers &middot; Summers Life Balance Coaching</cite></div>"""),
              cls="s-copy"),
            cls="wrap story"), cls="sec", tag="section"),
        # LEARN
        C(C(
            C(T('<span class="eyebrow">Learn with us</span>'),
              H("Live, free and full of real questions.", "h2", "h2"), cls=""),
            X("""<div class="ev">
<a class="ecard big" href="#learn"><img src="lx:laughlin-planning" alt=""><div class="e-in"><small>Every month &middot; Online</small><strong>LAI Business Edge: Live Q&amp;A</strong><p>Bring your questions about structure, compliance and protection. Our advisors answer them live.</p><em>Reserve a seat &rarr;</em></div></a>
<a class="ecard" href="#learn"><img src="lx:couple-docs" alt=""><div class="e-in"><small>Free guide</small><strong>LLC Quick Start Guide</strong><p>What to do in your first 90 days after forming.</p><em>Download &rarr;</em></div></a>
<a class="ecard" href="#learn"><img src="lx:laughlin-summit" alt=""><div class="e-in"><small>Nov 13&ndash;15, 2026 &middot; Dallas</small><strong>Magnify Your Wealth Summit</strong><p>Three days of strategy for business owners and investors.</p><em>Learn more &rarr;</em></div></a>
</div>"""),
            cls="wrap"), cls="sec learn", tag="section"),
        # FINAL
        C(X(f"""<div class="wrap final">
<div class="panel talk"><span class="eyebrow">Talk with a person</span><h2>You don't have to figure this out alone.</h2><p>Call and talk to an advisor about starting, protecting or restructuring your business.</p><a class="tel" href="{TEL}">{PHONE}</a></div>
<div class="panel cl" id="clients"><span class="eyebrow">Existing clients</span><h2>Welcome back.</h2><div class="links"><a href="#clients">Renew Registered Agent</a><a href="#clients">Renew CVPS</a><a href="#clients">Make a Payment</a><a href="#clients">Schedule Support</a><a href="#clients">Client Resources</a><a href="#clients">Update My Info</a></div></div>
</div>"""), cls="sec", tag="section"),
        footer(),
        cls="lx lx-b")]
