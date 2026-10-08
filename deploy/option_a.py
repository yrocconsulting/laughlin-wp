"""Option A, "The Long Road": a warm, editorial page built around the
Start, Protect, Grow, Preserve journey. Uses serif headlines, paper tones and plenty of white space."""
from lx import *

FONTQ = "family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Public+Sans:wght@400;500;600;700"

CSS = """
.lx-a{--bg:#FBF8F2;--ink:#1B2335;--muted:#5A6275;--navy:#0A2D64;--navy-2:#163E80;--gold:#F0BE28;--gold-ink:#94700A;--line:#E6DECD;--soft:#F3EDE1;--f-head:'Newsreader',Georgia,serif;--f-body:'Public Sans',system-ui,sans-serif;--radius:3px}
.lx-a .eyebrow{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)}
.lx-a .sec{padding-top:112px;padding-bottom:112px}
.lx-a .h2 .elementor-heading-title{font-size:clamp(34px,4vw,52px);line-height:1.08;font-weight:400;letter-spacing:-.01em;color:var(--navy)}
.lx-a .h2 em,.lx-a .h1 em{font-style:italic;color:var(--ink)}
.lx-a .lede{font-size:19px;color:var(--muted);max-width:620px}
/* hero */
.lx-a .hero{padding-top:56px;padding-bottom:96px}
.lx-a .hero-grid{display:grid;grid-template-columns:1.08fr .92fr;gap:64px;align-items:center}
.lx-a .hero-copy{gap:26px}
.lx-a .h1 .elementor-heading-title{font-size:clamp(42px,5.4vw,74px);line-height:1.02;font-weight:400;letter-spacing:-.02em;color:var(--navy)}
.lx-a .paths{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
.lx-a .path{display:flex;flex-direction:column;gap:6px;padding:22px 22px 20px;background:#fff;border:1px solid var(--line);border-top:3px solid var(--navy);text-decoration:none;transition:transform .2s,box-shadow .2s}
.lx-a .path:hover{transform:translateY(-2px);box-shadow:0 14px 30px -18px rgba(10,45,100,.45)}
.lx-a .path small{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink)}
.lx-a .path strong{font-family:var(--f-head);font-weight:500;font-size:24px;line-height:1.15;color:var(--navy)}
.lx-a .path span{font-size:15px;color:var(--muted)}
.lx-a .path span:after{content:" \\2192";color:var(--navy);font-weight:700}
.lx-a .path.p2{border-top-color:var(--gold)}
.lx-a .human{display:flex;align-items:center;gap:14px;font-size:15px;color:var(--muted)}
.lx-a .human img{width:48px;height:48px;border-radius:50%;object-fit:cover}
.lx-a .human a{color:var(--navy);font-weight:700;text-decoration:none}
.lx-a .hero-media{position:relative;height:620px}
.lx-a .hero-media .ph{position:absolute;inset:0 0 0 48px}
.lx-a .hero-media .ph2{position:absolute;left:0;bottom:-36px;width:44%;height:200px;border:8px solid var(--bg)}
.lx-a .note{position:absolute;right:-12px;top:36px;background:#fff;padding:18px 20px;max-width:250px;font-size:14px;line-height:1.45;box-shadow:0 20px 40px -24px rgba(0,0,0,.35);border-left:3px solid var(--gold)}
.lx-a .note b{display:block;font-family:var(--f-head);font-size:30px;font-weight:500;color:var(--navy);line-height:1}
/* journey */
.lx-a .journey{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.lx-a .j-head{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:end;margin-bottom:64px}
.lx-a .road{position:relative;display:grid;grid-template-columns:repeat(4,1fr);gap:0}
.lx-a .road:before{content:"";position:absolute;left:0;right:0;top:27px;height:2px;background:linear-gradient(90deg,var(--navy) 0 25%,var(--gold) 25% 100%)}
.lx-a .stop{position:relative;padding-right:36px}
.lx-a .stop .dot{width:56px;height:56px;border-radius:50%;background:#fff;border:2px solid var(--navy);display:flex;align-items:center;justify-content:center;font-family:var(--f-head);font-size:22px;color:var(--navy);position:relative;margin-bottom:26px}
.lx-a .stop:first-child .dot{background:var(--navy);color:#fff}
.lx-a .stop h3{font-family:var(--f-head);font-weight:500;font-size:32px;color:var(--navy);margin:0 0 8px}
.lx-a .stop p{color:var(--muted);font-size:16px}
.lx-a .stop ul{list-style:none;padding:0;margin:16px 0 0;border-top:1px solid var(--line)}
.lx-a .stop li{border-bottom:1px solid var(--line)}
.lx-a .stop li a{display:block;padding:10px 0;font-size:15px;font-weight:600;color:var(--ink);text-decoration:none}
.lx-a .stop li a:hover{color:var(--navy)}
.lx-a .stop.not:after{content:"Where most formation companies stop";position:absolute;left:72px;top:-6px;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--gold-ink);background:#fff;padding:0 8px}
/* formation */
.lx-a .form-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:80px;align-items:center}
.lx-a .form-media{height:560px}
.lx-a .form-copy{gap:24px}
.lx-a .steps{counter-reset:s;list-style:none;margin:8px 0 8px;padding:0;border-top:1px solid var(--line)}
.lx-a .steps li{counter-increment:s;display:grid;grid-template-columns:56px 1fr;gap:8px;padding:18px 0;border-bottom:1px solid var(--line)}
.lx-a .steps li:before{content:counter(s,decimal-leading-zero);font-family:var(--f-head);font-size:26px;color:var(--gold-ink)}
.lx-a .steps b{display:block;color:var(--navy);font-size:17px}
.lx-a .steps span{color:var(--muted);font-size:15px}
.lx-a .entities{display:flex;flex-wrap:wrap;gap:8px;font-size:14px}
.lx-a .entities a{padding:7px 14px;border:1px solid var(--line);border-radius:99px;text-decoration:none;background:#fff;font-weight:600;color:var(--navy)}
.lx-a .entities a:hover{border-color:var(--navy)}
/* CVPS */
.lx-a .cvps{background:var(--soft)}
.lx-a .cv-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:80px;align-items:start}
.lx-a .cv-copy{gap:24px}
.lx-a .cv-def{font-family:var(--f-head);font-size:22px;line-height:1.45;color:var(--ink);border-left:3px solid var(--gold);padding-left:22px}
.lx-a .cv-def b{font-weight:500;color:var(--navy)}
.lx-a .cv-card{background:#fff;padding:40px;gap:20px;box-shadow:0 30px 60px -40px rgba(10,45,100,.4)}
.lx-a .cv-card h3{font-family:var(--f-head);font-weight:500;font-size:26px;color:var(--navy);margin:0 0 6px}
.lx-a .cracks{list-style:none;margin:0;padding:0}
.lx-a .cracks li{display:flex;gap:14px;padding:14px 0;border-bottom:1px dashed var(--line);font-size:16px}
.lx-a .cracks li:before{content:"";flex:0 0 10px;height:10px;margin-top:8px;border:2px solid #C2410C;border-radius:50%}
.lx-a .cv-help{background:var(--navy);color:#E8EEF8;padding:24px;font-size:15px;margin-top:8px}
.lx-a .cv-help b{color:var(--gold)}
/* story */
.lx-a .story-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:80px;align-items:center}
.lx-a .year{font-family:var(--f-head);font-size:clamp(110px,16vw,220px);line-height:.8;color:var(--navy);letter-spacing:-.04em}
.lx-a .year small{display:block;font-family:var(--f-body);font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink);margin-top:22px;font-weight:700}
.lx-a .story-copy{gap:22px}
.lx-a .proof{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line);margin-top:12px}
.lx-a .proof div{padding:18px 18px 0 0}
.lx-a .proof b{display:block;font-family:var(--f-head);font-weight:500;font-size:28px;color:var(--navy);line-height:1.1}
.lx-a .proof span{font-size:14px;color:var(--muted)}
.lx-a .quote{font-family:var(--f-head);font-style:italic;font-size:22px;line-height:1.45;color:var(--ink);margin-top:12px}
.lx-a .quote cite{display:block;font-family:var(--f-body);font-style:normal;font-size:14px;font-weight:700;color:var(--muted);margin-top:12px;letter-spacing:.04em}
.lx-a .story-media{height:420px;margin-top:64px}
.lx-a .story-media img{object-position:50% 35%}
.lx-a .clients{border-bottom:1px solid rgba(255,255,255,.12)}
/* learn */
.lx-a .learn{background:#fff;border-top:1px solid var(--line)}
.lx-a .learn-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:72px}
.lx-a .qa{border-top:2px solid var(--navy);margin-top:36px}
.lx-a .qa details{border-bottom:1px solid var(--line)}
.lx-a .qa summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:24px;padding:22px 0;font-family:var(--f-head);font-size:24px;line-height:1.25;color:var(--navy)}
.lx-a .qa summary::-webkit-details-marker{display:none}
.lx-a .qa summary:after{content:"+";font-family:var(--f-body);font-size:24px;color:var(--gold-ink);transition:transform .2s}
.lx-a .qa details[open] summary:after{transform:rotate(45deg)}
.lx-a .qa p{color:var(--muted);padding:0 48px 22px 0;margin:0}
.lx-a .qa .more{display:inline-block;margin:0 0 22px;font-weight:700;color:var(--navy);text-decoration:none;border-bottom:1.5px solid var(--gold)}
.lx-a .side{gap:20px;position:sticky;top:24px}
.lx-a .side-media{height:260px}
.lx-a .event{border:1px solid var(--line);padding:28px;gap:12px;background:var(--bg)}
.lx-a .event small{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-ink)}
.lx-a .event h3{font-family:var(--f-head);font-weight:500;font-size:26px;color:var(--navy);margin:4px 0 8px;line-height:1.15}
/* people / next steps */
.lx-a .people-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.lx-a .people-media{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:240px 240px;gap:12px}
.lx-a .people-media .elementor-widget-image:first-child{grid-row:1 / 3}
.lx-a .people-copy{gap:24px}
.lx-a .next{display:grid;grid-template-columns:1fr 1fr;gap:0;border-top:1px solid var(--line)}
.lx-a .next a{display:block;padding:18px 16px 18px 0;border-bottom:1px solid var(--line);text-decoration:none}
.lx-a .next a b{display:block;color:var(--navy);font-size:17px}
.lx-a .next a span{font-size:14px;color:var(--muted)}
.lx-a .next a:hover b{text-decoration:underline;text-decoration-color:var(--gold);text-underline-offset:4px}
/* clients */
.lx-a .clients{background:var(--navy);color:#fff;padding-top:44px;padding-bottom:44px}
.lx-a .cl-in{display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap}
.lx-a .cl-in h2{font-family:var(--f-head);font-weight:400;font-size:30px;margin:0;color:#fff}
.lx-a .cl-in h2 span{display:block;font-family:var(--f-body);font-size:15px;color:#B9C6DE;margin-top:4px}
.lx-a .cl-links{display:flex;gap:10px;flex-wrap:wrap}
.lx-a .cl-links a{padding:11px 16px;border:1px solid rgba(255,255,255,.3);color:#fff;text-decoration:none;font-weight:600;font-size:15px}
.lx-a .cl-links a:hover{background:var(--gold);color:var(--navy);border-color:var(--gold)}
@media (max-width:1100px){
 .lx-a .hero-grid,.lx-a .form-grid,.lx-a .cv-grid,.lx-a .story-grid,.lx-a .learn-grid,.lx-a .people-grid,.lx-a .j-head{grid-template-columns:1fr;gap:48px}
 .lx-a .road{grid-template-columns:1fr 1fr;row-gap:48px}
 .lx-a .road:before{display:none}
 .lx-a .stop.not:after{display:none}
 .lx-a .hero-media{height:460px}
 .lx-a .side{position:static}
}
@media (max-width:640px){
 .lx-a .sec{padding-top:72px;padding-bottom:72px}
 .lx-a .paths,.lx-a .road,.lx-a .next,.lx-a .proof{grid-template-columns:1fr}
 .lx-a .hero-media{height:380px}
 .lx-a .hero-media .ph{left:0}
 .lx-a .hero-media .ph2{display:none}
 .lx-a .note{right:12px;top:auto;bottom:12px}
 .lx-a .form-media{height:320px}
 .lx-a .cv-card{padding:26px}
 .lx-a .people-media{grid-template-rows:180px 180px}
}
"""


def build():
    reset_ids("a")
    stages = "".join(
        f'<div class="stop{" not" if i == 0 else ""}"><div class="dot">{i+1}</div><h3>{n}</h3><p>{d}</p><ul>'
        + "".join(f'<li><a href="#{n.lower()}">{x}</a></li>' for x in items) + "</ul></div>"
        for i, (n, d, items) in enumerate(STAGES))
    qa = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p><a class="more" href="#learn">Read the full answer</a></details>'
                 for i, (q, a) in enumerate(QUESTIONS))
    return [C(
        style(FONTQ, CSS),
        header(),
        # HERO
        C(C(
            C(T('<span class="eyebrow">Helping business owners since 1971</span>'),
              H("Forming your company is the beginning. <em>We're here for everything after.</em>", "h1", "h1"),
              T("<p>Laughlin helps entrepreneurs start the right entity, keep it protected, grow with confidence and plan what comes next, with experienced advisors you can actually reach.</p>", "lede"),
              X("""<div class="paths">
<a class="path" href="#formation"><small>I'm starting a business</small><strong>Form an LLC or corporation</strong><span>Start your entity</span></a>
<a class="path p2" href="#protect"><small>I already own a business</small><strong>Protect &amp; maintain what you built</strong><span>Explore protection</span></a>
</div>"""),
              X(f'<div class="human"><img src="lx:laughlin-advisor" alt=""><div>Not sure which applies to you? <a href="{TEL}">Talk with an advisor &middot; {PHONE}</a></div></div>'),
              cls="hero-copy"),
            C(I("laughlin-1on1", "ph", "A Laughlin advisor working through questions with a business owner"),
              I("laughlin-planning", "ph2", "Business planning session"),
              X('<div class="note"><b>55+ years</b>of helping owners avoid the mistakes that cost the most, long after the paperwork is filed.</div>'),
              cls="hero-media"),
            cls="wrap hero-grid"), cls="hero", tag="section"),
        # JOURNEY
        C(C(
            C(C(T('<span class="eyebrow">One relationship, every stage</span>'),
                H("Most formation companies stop at step one. <em>Laughlin was built for the whole road.</em>", "h2", "h2"), cls=""),
              T("<p>Your business changes. Your protection, structure and plans should keep up. We stay with you from the day you file to the day you hand it on.</p>", "lede"),
              cls="j-head"),
            X(f'<div class="road">{stages}</div>'),
            cls="wrap"), cls="sec journey", tag="section"),
        # FORMATION
        C(C(
            I("owner-cafe", "form-media", "A business owner opening the door of her shop"),
            C(T('<span class="eyebrow" id="formation">Start a business</span>'),
              H("Ready to form your company? Let's set it up right the first time.", "h2", "h2"),
              T("<p>Choose your entity, and we'll handle the filing in any state, with guidance so you're not guessing.</p>", "lede"),
              X("""<ol class="steps">
<li><div><b>Choose your structure</b><span>LLC, S-Corp, C-Corp or nonprofit. Not sure? Compare them side by side or ask us.</span></div></li>
<li><div><b>We prepare and file</b><span>Articles, registered agent and state filings handled by people who've done this for decades.</span></div></li>
<li><div><b>Start out protected</b><span>EIN, corporate records and a clear checklist of what to keep up with next.</span></div></li>
</ol>"""),
              C(B("Start your LLC or corporation", "#formation", "btn-gold"), B("Compare entity types", "#formation", "btn-link"), cls="btns"),
              X('<div class="entities"><a href="#formation">LLC</a><a href="#formation">S-Corporation</a><a href="#formation">C-Corporation</a><a href="#formation">Nonprofit</a><a href="#formation">Non-U.S. residents</a></div>'),
              cls="form-copy"),
            cls="wrap form-grid"), cls="sec", tag="section"),
        # CVPS
        C(C(
            C(T('<span class="eyebrow" id="protect">Corporate Veil Protection Service</span>'),
              H("Your company is a wall between your business and your home. <em>It only holds if it's maintained.</em>", "h2", "h2"),
              T('<p class="cv-def">That wall is called the <b>corporate veil</b>. It keeps business debts and lawsuits away from your house, savings and family. But courts can &ldquo;pierce the veil&rdquo; when a company isn&rsquo;t run as a truly separate business.</p>'),
              T("<p>Formation-only companies file your paperwork and move on. Laughlin's Corporate Veil Protection Service keeps you on track every year with reminders, minutes, records and a real person to call when you're unsure.</p>"),
              C(B("Explore Corporate Veil Protection", "#protect"), B("Is my company protected? Free review", "#review", "btn-link"), cls="btns"),
              cls="cv-copy"),
            C(X("""<h3>What quietly weakens your protection</h3>
<ul class="cracks">
<li>No annual meetings or written minutes</li>
<li>Personal and business money in the same account</li>
<li>Late state filings or a lapsed registered agent</li>
<li>Records that don't match the decisions you made</li>
<li>Signing contracts in your own name, not the company's</li>
</ul>
<div class="cv-help"><b>How Laughlin helps:</b> we track your deadlines, help prepare minutes and resolutions, keep your corporate records in order and review your compliance with you every year.</div>"""),
              cls="cv-card"),
            cls="wrap cv-grid"), cls="sec cvps", tag="section"),
        # STORY
        C(C(
            X('<div class="year" id="story">1971<small>Where Laughlin began</small></div>'),
            C(H("Started by an independent truck driver who believed small businesses deserved the same protection as big ones.", "h2", "h2"),
              T("<p>Harley Laughlin founded the company to give everyday entrepreneurs the resources and safeguards large corporations take for granted. More than 55 years later, that is still the job. We've seen what goes wrong when a company isn't maintained, and we help owners avoid it.</p>", "lede"),
              X("""<div class="proof"><div><b>Thousands</b><span>of businesses supported</span></div><div><b>Nationwide</b><span>formation in every state</span></div><div><b>Inc. 5000</b><span>2026 honoree</span></div></div>
<p class="quote">&ldquo;I really had no idea where to start. Thanks to your hand-holding, I have a proper understanding of my responsibilities to maintain my liability protection.&rdquo;<cite>DAN LINCOLN &middot; BUD THE SPUD CHIP TRUCKS, INC.</cite></p>"""),
              cls="story-copy"),
            cls="wrap story-grid"),
          C(I("laughlin-roundtable", "story-media", "Business owners at a Laughlin workshop"), cls="wrap"),
          cls="sec", tag="section"),
        # LEARN
        C(C(
            C(T('<span class="eyebrow" id="learn">Straight answers</span>'),
              H("The questions business owners ask us every week.", "h2", "h2"),
              X(f'<div class="qa">{qa}</div>'),
              cls=""),
            C(I("laughlin-notes", "side-media", "Taking notes during a Laughlin session"),
              X("""<div class="event"><small>Live &amp; free</small><h3>LAI Business Edge: live Q&amp;A with our advisors</h3><p>Bring your questions about structure, compliance and protection. Get plain-English answers.</p></div>"""),
              C(B("See upcoming webinars", "#learn"), B("Download a free guide", "#learn", "btn-link"), cls="btns"),
              cls="side"),
            cls="wrap learn-grid"), cls="sec learn", tag="section"),
        # PEOPLE / NEXT STEPS
        C(C(
            C(I("advisor-table", "", "An advisor reviewing plans with business owners"),
              I("laughlin-advisor", "", "A Laughlin advisor in conversation"),
              I("advisor-seniors", "", "An advisor helping a couple plan ahead"), cls="people-media"),
            C(T('<span class="eyebrow" id="advisors">Real people</span>'),
              H("You don't have to figure all of this out alone.", "h2", "h2"),
              T("<p>Call and you'll reach someone who knows business structure, not a ticket queue. Pick the next step that fits where you are.</p>", "lede"),
              X(f"""<div class="next" id="review">
<a href="#formation"><b>Start an entity</b><span>Form an LLC or corporation</span></a>
<a href="#protect"><b>Explore CVPS</b><span>Keep your protection intact</span></a>
<a href="{TEL}"><b>Talk with an advisor</b><span>{PHONE}</span></a>
<a href="#learn"><b>Attend a webinar</b><span>Live, free, bring questions</span></a>
<a href="#review"><b>Free business review</b><span>Is your structure still right?</span></a>
<a href="#learn"><b>Free guides</b><span>LLC Quick Start and more</span></a>
</div>"""),
              cls="people-copy"),
            cls="wrap people-grid"), cls="sec", tag="section"),
        # EXISTING CLIENTS
        X("""<section class="clients" id="clients"><div class="wrap cl-in"><h2>Already a Laughlin client?<span>Everything you need, one click away.</span></h2>
<div class="cl-links"><a href="#clients">Renew Registered Agent</a><a href="#clients">Renew CVPS</a><a href="#clients">Make a Payment</a><a href="#clients">Schedule Client Support</a><a href="#clients">Client Resources</a></div></div></section>"""),
        footer(),
        cls="lx lx-a")]
