"""Content for the full Laughlin site. Facts come from Laughlin's current site
(laughlinusa.com), rewritten in the new plain, short voice."""
from sitekit import *

START = ("Start a Business", "/start-a-business/")
PROTECT = ("Protect My Business", "/protect-my-business/")
GROW = ("Grow My Business", "/grow-my-business/")
RES = ("Resources &amp; Events", "/resources/")

CTA_START = ("Start your business", "/contact/")


# ---------------------------------------------------------------- START
def start_hub():
    reset_ids("start")
    return page(
        hero("Start a business", "Start your company the right way.",
             "Choose the right structure, file it correctly and set it up to protect you from day one. We've helped business owners do it since 1972.",
             img="owner-cafe", alt="A business owner opening her shop",
             extra=btns(("Talk with an advisor", "/contact/", "gold"), ("Compare structures", "/start-a-business/compare-structures/", "ghost"))),
        section(head("Choose your structure", "Which entity fits your business?",
                     "Each structure protects you differently and is taxed differently. Not sure? That's what our advisors are for."),
                cards([("Most popular", "Form an LLC", "Liability protection with flexible management and pass-through taxes.", "/start-a-business/llc/", True),
                       ("C-Corp &amp; S-Corp", "Form a Corporation", "The strongest structure for benefits, investors and transferring ownership.", "/start-a-business/corporation/"),
                       ("Mission-driven", "Form a Nonprofit", "For charitable, educational, religious or scientific purposes.", "/start-a-business/nonprofit/"),
                       ("Side by side", "Compare structures", "LLC, C-Corporation and S-Corporation compared in one table.", "/start-a-business/compare-structures/"),
                       ("Where to form", "Why Nevada", "Strong liability protection, privacy and no state income tax.", "/start-a-business/nevada/"),
                       ("Outside the U.S.?", "International clients", "Anyone can form a U.S. company. We'll help you do it right.", "/start-a-business/international/")])),
        section(C(C(head("How it works", "Three steps. Real people at each one."),
                    numbered([("Talk it through", "Tell us about your business and goals. We'll help you pick the structure and state that fit."),
                              ("We prepare and file", "Articles, registered agent and state filings, handled by people who've done this for decades."),
                              ("Start out protected", "EIN, corporate records and a clear checklist of what to keep up with next.")]), cls=""),
                  includes("After you file, we can also handle", ["Registered agent service in every state", "EIN (Employer Identification Number)",
                           "Corporate record book and minutes", "Business licenses", "Name search and DBA filings", "Foreign qualification in other states"],
                           "See all filing services", "/start-a-business/filing-services/"), cls="split"), alt=True),
        faq_section("Common questions", "Before you form.", [
            ("When should I form a business entity?", "If you run a business, even a part-time or home-based one, or you're about to start one, now is the time. A corporation or LLC separates your personal liability from your business liability."),
            ("Which state should I form in?", "Usually the state where your business has a physical presence. If you won't have an office or location, a state like Nevada can make sense. We'll help you weigh it."),
            ("How do I know if my company name is available?", f"Call us at {TOLLFREE} and we'll run a quick check. If the name is taken, we can often suggest small changes that will let it be filed."),
            ("Can one person form a corporation?", "Yes. You can be the only shareholder, director, officer and employee. Structured correctly, a one-person company can use many of the same tools as large companies."),
        ]),
        band("Ready to start?", "Talk with an advisor about your business. We'll help you choose the right structure and file it correctly."),
    )


def llc():
    reset_ids("llc")
    return page(
        hero("Form an LLC", "The LLC: protection with flexibility.",
             "A Limited Liability Company gives you the liability protection of a corporation with the simpler tax treatment of a partnership. It's one of the most popular structures for small businesses.",
             trail=[START, ("Form an LLC", "/start-a-business/llc/")], img="owner-workshop", alt="A small business owner in his workshop",
             extra=btns(("Form your LLC", "/contact/", "gold"), ("Compare to a corporation", "/start-a-business/compare-structures/", "link"))),
        section(glance([("Owned by", "Members"), ("Managed by", "Members or a manager"), ("Taxed as", "Pass-through or as a corporation"), ("Protects", "Members&rsquo; personal assets")]), cls="tight"),
        prose("What is an LLC?", "Corporation protection. Partnership simplicity.", """
<p>An LLC is a hybrid. Its owners, called <strong>members</strong>, get the same personal liability protection as shareholders of a corporation. Profits and losses can pass through to the members' own tax returns, like a partnership.</p>
<p>Members can be individuals or other companies, including corporations. You choose whether the LLC is <strong>member-managed</strong> or <strong>manager-managed</strong> when you form it.</p>
<h3>Why owners choose an LLC</h3>
<ul><li>Personal asset protection</li><li>Flexible management and ownership</li><li>Tax flexibility: pass-through, or taxed as a corporation</li><li>Less paperwork than a corporation</li></ul>
<h3>Common uses</h3>
<ul><li>Operating a small business</li><li>Holding real estate</li><li>Holding trading or investment accounts</li></ul>
<h3>Worth knowing</h3>
<p>LLC laws differ from state to state, and an LLC still has to be run as a separate business to keep its protection. That means records, separate finances and staying in good standing.</p>"""),
        faq_section("LLC questions", "What owners ask about LLCs.", [
            ("Is an LLC better than a corporation?", "It depends on your goals. LLCs are simpler and more flexible. Corporations can offer more fringe benefits and make it easier to bring in investors or transfer ownership. An advisor can walk you through it."),
            ("Does an LLC need minutes and records?", "Courts look at whether an LLC is run as a separate business. Keeping minutes of major decisions, an operating agreement and separate finances is your proof."),
            ("Can my LLC be taxed as an S-Corporation?", "Yes. An LLC can elect to be taxed as a corporation, including an S-Corporation, if it qualifies. Talk to your tax professional about whether it makes sense."),
            ("Who can be a member?", "Individuals, other LLCs, corporations and trusts can all be members. LLCs have far fewer ownership restrictions than S-Corporations."),
        ], alt=True),
        band("Form your LLC with Laughlin.", "We'll file it correctly in any state and help you keep it protected, year after year."),
    )


def corporation():
    reset_ids("corp")
    return page(
        hero("Form a Corporation", "Corporations: built for protection and growth.",
             "A corporation is its own legal person. Structured and maintained correctly, it offers strong liability protection, tax planning options and an easy way to transfer ownership.",
             trail=[START, ("Form a Corporation", "/start-a-business/corporation/")], img="advisor-desk", alt="An advisor reviewing documents with a client",
             extra=btns(("Form your corporation", "/contact/", "gold"), ("Compare structures", "/start-a-business/compare-structures/", "link"))),
        C(C(C(head("C-Corporation", "The standard corporation.",
                   "When you file a corporation with the state, you're forming a C-Corporation."),
              X("""<div class="body"><ul><li>Files its own tax return</li><li>No limit on the number or type of shareholders</li><li>Can issue different classes of stock</li><li>Shares transfer freely</li><li>Can offer fringe benefits</li></ul>
<p><strong>Common uses:</strong> operating a business, raising capital.</p></div>"""), cls="cv-copy prose-col"),
            C(head("S-Corporation", "A corporation with pass-through taxes.",
                   "An S-Corporation starts as a regular corporation, then elects S status with the IRS by filing Form 2553."),
              X("""<div class="body"><ul><li>Profits and losses pass through to shareholders</li><li>Same liability protection as a C-Corporation</li><li>100 or fewer shareholders</li><li>One class of stock</li><li>Shareholders must be U.S. citizens or residents (with limited exceptions)</li></ul>
<p><strong>Timing:</strong> file Form 2553 within 75 days of forming, or of the start of your tax year.</p></div>"""), cls="cv-copy prose-col"),
            cls="wrap split"), cls="sec", tag="section"),
        section(C(C(head("The catch", "Corporations have to act like corporations.",
                         "Courts expect corporate formalities: meetings, minutes, approvals and records. It doesn't matter if you're the only shareholder. Skip them and you risk losing the protection you formed the company for."),
                    X(btns(("How Corporate Veil Protection helps", "/protect-my-business/corporate-veil-protection/", "link"))), cls=""),
                  includes("Your first steps after forming", ["Read and understand your Articles of Incorporation", "Create and sign your bylaws", "Get your EIN from the IRS",
                           "File Form 2553 if you're electing S status", "Open a separate business bank account", "Hold your first board of directors meeting", "Get the business licenses you need"]),
                  cls="split"), alt=True),
        faq_section("Corporation questions", "What owners ask about corporations.", [
            ("Who can form a corporation?", "Anyone. You can be the sole shareholder, director, officer and employee."),
            ("C-Corp or S-Corp?", "It's mostly a tax decision. S-Corporations pass income through to shareholders; C-Corporations pay their own tax and have no ownership restrictions. Ask your tax professional which fits, and we'll handle the filings."),
            ("Do I really need to hold meetings if I'm the only owner?", "Yes. State law generally requires annual shareholder minutes, and board decisions should be documented. It's your proof the company is separate from you."),
        ]),
        band("Form your corporation with Laughlin.", "We'll file it, set it up and help you keep the formalities that protect you."),
    )


def nonprofit():
    reset_ids("np")
    return page(
        hero("Form a Nonprofit", "Turn a mission into an organization.",
             "A nonprofit corporation is formed for a charitable, educational, religious, literary or scientific purpose. We'll form it at the state level and help you pursue tax-exempt status.",
             trail=[START, ("Form a Nonprofit", "/start-a-business/nonprofit/")], img="laughlin-roundtable", alt="People gathered around a table",
             extra=btns(("Talk with an advisor", "/contact/", "gold"))),
        prose("How it works", "Two steps: form it, then apply for exemption.", """
<p>Forming a nonprofit is a lot like forming a regular corporation. The extra step is applying for tax-exempt status with the IRS, usually <strong>501(c)(3)</strong>, and with your state.</p>
<h3>Advantages</h3>
<ul><li>Exempt from corporate income tax, once approved</li><li>Can receive grants and donations</li><li>Donors may be able to deduct contributions</li><li>Directors, officers and members are protected from personal liability</li><li>Can pay reasonable salaries</li></ul>"""),
        faq_section("Nonprofit questions", "What founders ask us.", [
            ("Am I automatically tax-exempt when I form a nonprofit?", "No. You need to apply to the IRS for 501(c)(3) status. Until you're approved, you can't present donations as tax-deductible."),
            ("Which state should I form in?", "Usually the state where you'll operate. If you'll work in other states, you may need to qualify to do business there too."),
            ("What do I have to keep up with?", "Annual meetings, board minutes and the rules that come with your exempt status. Most states also require an annual renewal and a registered agent."),
        ], alt=True),
        band("Start your nonprofit.", "We'll form it at the state level and help you prepare for tax-exempt status."),
    )


def compare():
    reset_ids("cmp")
    rowsd = [
        ("Ownership", "Stock. Can have different classes.", "Membership interests. Can have different classes.", "One class of stock (voting or non-voting)."),
        ("Eligible owners", "No restrictions.", "No restrictions.", "Up to 100 shareholders. No corporate or non-resident alien shareholders."),
        ("Management", "Directors and officers.", "Members, or a manager.", "Directors and officers."),
        ("Taxes", "Files its own return.", "Pass-through by default, or can elect corporate tax.", "Pass-through to shareholders by ownership percentage."),
        ("Liability protection", "Shareholders, officers and directors.", "Members and managers.", "Shareholders, officers and directors."),
        ("Duration", "Perpetual.", "Set by the operating agreement.", "Perpetual."),
        ("Transferring ownership", "Shares transfer freely.", "May be restricted by state law or the operating agreement.", "Only to eligible S-Corporation shareholders."),
        ("Formalities", "Meetings, minutes and approvals required.", "Fewer required. Records still matter.", "Meetings, minutes and approvals required."),
    ]
    body = "".join(f"<tr><th>{r[0]}</th><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>" for r in rowsd)
    table = f"""<div class="tbl-wrap"><table class="cmp"><thead><tr><th></th><th>C-Corporation</th><th>LLC</th><th>S-Corporation</th></tr></thead><tbody>{body}</tbody></table></div>
<p class="fine">A general comparison, not legal or tax advice. Rules vary by state; talk to your tax professional about your situation.</p>"""
    return page(
        hero("Compare structures", "LLC, C-Corp or S-Corp? See them side by side.",
             "Every structure protects you. They differ in how they're owned, managed and taxed.",
             trail=[START, ("Compare Structures", "/start-a-business/compare-structures/")]),
        section(X(table)),
        section(head("Still deciding?", "Pick the one that fits where you're going."),
                cards([("Flexible", "LLC", "Simple to run, flexible taxes. Great for small businesses and real estate.", "/start-a-business/llc/"),
                       ("Growth", "C-Corporation", "No ownership limits, fringe benefits, easy to bring in investors.", "/start-a-business/corporation/"),
                       ("Pass-through", "S-Corporation", "Corporate protection with pass-through taxes, within IRS limits.", "/start-a-business/corporation/")]), alt=True),
        band("Not sure which fits?", "Ten minutes with an advisor can save years of restructuring. Tell us about your business."),
    )


def nevada():
    reset_ids("nv")
    return page(
        hero("Why Nevada", "Nevada: a business-friendly place to form.",
             "Laughlin is based in Carson City, Nevada's capital. Nevada is known for strong liability protection, privacy and low taxes, and you don't need to live here to form a company here.",
             trail=[START, ("Why Nevada", "/start-a-business/nevada/")], img="laughlin-summit", alt="A Laughlin event",
             extra=btns(("Form in Nevada", "/contact/", "gold"))),
        section(head("The Nevada advantage", "What Nevada offers business owners."),
                rows([("Taxes", "No state corporate or personal income tax", "Nevada doesn't tax corporate or personal income. (Very large businesses may owe the state's Commerce Tax on gross revenue.)"),
                      ("Liability", "Strong protection for officers and directors", "Nevada law limits personal liability for officers and directors, except in cases like fraud."),
                      ("Privacy", "Shareholders aren't filed with the state", "Nevada doesn't require you to file the names of a corporation's stockholders."),
                      ("Flexibility", "Simple requirements", "One person can hold every position. Officers, directors and owners can live anywhere and meet anywhere.")])),
        section(C(C(head("Do you need to be in Nevada?", "No relocation required.",
                         "You can form a Nevada company by phone or online and never visit the state. If you do business in another state, you'll usually need to qualify there too. We'll tell you if that applies."), cls=""),
                  includes("Laughlin's Nevada office services", ["Registered agent in Carson City", "Mail forwarding for Nevada companies", "Telephone answering in your company's name", "Corporate records and compliance"],
                           "Ask about Nevada services", "/contact/"), cls="split"), alt=True),
        band("Is Nevada right for your business?", "It depends on where you operate and what you're protecting. We'll help you decide."),
    )


def international():
    reset_ids("intl")
    return page(
        hero("International clients", "Form a U.S. company from anywhere.",
             "Anyone can form a business in the United States, from any country. For most people, the process is the same as it is for U.S. citizens.",
             trail=[START, ("International Clients", "/start-a-business/international/")], img="advisor-table", alt="An advisor meeting with clients",
             extra=btns(("Talk with an advisor", "/contact/", "gold"))),
        section(C(C(head("What you'll need", "Three decisions to get started."),
                    numbered([("Your company name", "We'll check availability in the state you choose."),
                              ("The state", "Usually where your business will have a physical presence. With no U.S. location, a state like Nevada can work well."),
                              ("The type of entity", "Corporation, LLC or nonprofit. We'll help you choose.")]), cls=""),
                  includes("If you form in Nevada, we can provide", ["A U.S. business address", "Mail forwarding", "Telephone answering in your company name", "Registered agent service"],
                           "Ask about international formation", "/contact/"), cls="split")),
        band("Questions before you start?", f"Call {PHONE} from outside the U.S., or send us a note and an advisor will get back to you."),
    )


def filing_services():
    reset_ids("filing")
    return page(
        hero("Filing services", "The paperwork, handled.",
             "Beyond formation, businesses need filings at every stage. We'll prepare and file them for you, in any state.",
             trail=[START, ("Filing Services", "/start-a-business/filing-services/")]),
        section(rows([("Setup", "EIN (Employer Identification Number)", "Your company's federal tax ID. You'll need it to open a bank account and hire."),
                      ("Setup", "Name search", "Make sure your company name is available before you file."),
                      ("Setup", "DBA (Doing Business As)", "Operate under a trade name that's different from your legal company name."),
                      ("Setup", "Business licenses", "Find and file the city, county and state licenses your business needs."),
                      ("Expand", "Foreign qualification", "Register your company to do business in another state, so you avoid penalties."),
                      ("Expand", "Certificate of Good Standing", "Official proof your company is current with the state. Lenders and other states often ask for one."),
                      ("Change", "Name change", "Change your company's legal name with the state."),
                      ("Close", "Dissolving your company", "Close a company properly so it doesn't keep owing fees and filings.")])),
        band("Need a filing?", f"Call {TOLLFREE} or send us a note. We'll tell you what's required and take care of it."),
    )


# ---------------------------------------------------------------- PROTECT
def protect_hub():
    reset_ids("protect")
    return page(
        hero("Protect my business", "Keep your company protecting you.",
             "Forming the company was step one. Keeping it in good standing, with the records to prove it's separate from you, is what keeps your personal assets safe.",
             img="laughlin-1on1", alt="An advisor reviewing records with a client",
             extra=btns(("Explore Corporate Veil Protection", "/protect-my-business/corporate-veil-protection/", "gold"), ("Free business review", "/business-review/", "ghost"))),
        C(C(C(head("Why it matters", "Your company protects you. Only if it's maintained.",
                   "An LLC or corporation draws a legal line between your business and your personal life. Run the company as its own business and the line holds. Let the upkeep slip and a court can step over it."),
              cls=""), X(f'<div class="diagram">{DIAGRAM}</div>'), cls="wrap veil-x"), cls="sec cvps", tag="section"),
        section(head("Protection services", "Everything that keeps your company in good standing."),
                cards([("Signature service", "Corporate Veil Protection", "Minutes, records, deadlines and a yearly review, handled with you.", "/protect-my-business/corporate-veil-protection/", True),
                       ("Required by law", "Registered Agent", "A reliable address for legal notices, in every state you operate.", "/protect-my-business/registered-agent/"),
                       ("Your proof", "Minutes &amp; Records", "Corporate minutes and a record book that show the company stands on its own.", "/protect-my-business/corporate-records/"),
                       ("Learn", "10 Common Mistakes", "The mistakes that most often cost owners their protection.", "/protect-my-business/common-mistakes/"),
                       ("Check-up", "Free Business Review", "Is your company still protecting you? We'll look at it with you.", "/business-review/"),
                       ("Every year", "Compliance filings", "Annual reports and state filings, on time.", "/start-a-business/filing-services/")])),
        band("Is your company still protecting you?", "Most owners don't know until it's tested. Let's check it together."),
    )


def cvps():
    reset_ids("cvps")
    return page(
        hero("Corporate Veil Protection Service", "The upkeep that keeps your protection intact.",
             "Your corporation or LLC protects your personal assets only if you can prove it's separate from you. CVPS keeps the records, meetings and deadlines that prove it.",
             trail=[PROTECT, ("Corporate Veil Protection", "/protect-my-business/corporate-veil-protection/")], img="laughlin-1on1", alt="An advisor and client reviewing records",
             extra=btns(("Talk to us about CVPS", "/contact/", "gold"), ("Already a client? Renew", "/clients/", "link"))),
        prose("What is the corporate veil?", "The line between you and your company.", """
<p>The corporate veil is the protection between your personal assets and your business. If you have a corporation or LLC, you're expected to keep records that prove there's real separation between you and the company.</p>
<p>If you don't, a court can treat you like a sole proprietor, and you can be held personally responsible for the company's debts, lawsuits and even tax penalties.</p>
<blockquote>&ldquo;I am not the company, and the company is not me.&rdquo;<cite>The rule every owner should run by</cite></blockquote>
<p>Small, closely held companies are held to the same standards as big ones. If you're the only shareholder, director and officer, keeping that separation clear matters even more.</p>"""),
        section(C(C(head("How CVPS helps", "We help you manage your entity, every year."),
                    numbered([("Maintain corporate formalities", "Annual meetings and minutes, plus resolutions for major decisions, prepared with you."),
                              ("Consolidate your records", "Your company's documents, organized in one place and kept current."),
                              ("Track your company's history", "A record of what your company decided and when. Your proof it acts on its own."),
                              ("Stay ahead of deadlines", "Reminders for filings and renewals, so nothing lapses."),
                              ("Talk to a real person", "Questions about what to document? Call your advisor.")]), cls=""),
                  C(X(f'<div class="diagram">{DIAGRAM}</div>'), cls=""), cls="split"), alt=True),
        faq_section("CVPS questions", "What clients ask about CVPS.", [
            ("Do I need CVPS if I'm a one-person company?", "Especially then. When one person owns and runs everything, it's easiest for someone to argue the company and the owner are the same. Good records are your defense."),
            ("Is CVPS only for corporations?", "No. LLCs benefit from documented decisions and organized records too."),
            ("What records matter most?", "Annual meeting minutes, resolutions for major decisions (loans, real estate, big purchases), stock or membership ledgers, and proof that business and personal finances are separate."),
            ("Can I add CVPS if Laughlin didn't form my company?", "Yes. We help companies no matter who formed them."),
        ]),
        band("Protect what you've built.", "Talk with an advisor about Corporate Veil Protection for your company."),
    )


def registered_agent():
    reset_ids("ra")
    return page(
        hero("Registered agent", "Never miss a legal notice.",
             "Every state requires your company to keep a registered agent in the state where it's formed, and in each state where it's qualified to do business.",
             trail=[PROTECT, ("Registered Agent", "/protect-my-business/registered-agent/")], img="advisor-desk", alt="An advisor handling documents",
             extra=btns(("Order registered agent service", "/contact/", "gold"), ("Renew", "/clients/", "ghost"))),
        section(C(C(head("What a registered agent does", "A reliable address for the notices that matter.",
                         "Your registered agent receives legal papers and state notices for your company and makes sure they reach you quickly."), cls=""),
                  includes("Laughlin's registered agent service includes", ["Forwarding your legal documents quickly", "Notices about changing rules and regulations", "Reminders when your annual list is due", "Documents to keep your company in good standing"]),
                  cls="split")),
        section(head("Why Laughlin", "More than an address."),
                rows([("Experience", "Five decades of doing this", "Acting as your own agent is risky. Miss a lawsuit notice and you could lose by default."),
                      ("Deadlines", "Avoid late fees and revocation", "Miss a state filing and you face fines, or your company can be revoked."),
                      ("Information", "We keep you informed", "We follow changes in regulations and the law, and let you know what affects you."),
                      ("Support", "People who answer", "A trained, experienced team that's here when you need us.")]), alt=True),
        band("Need a registered agent?", "Order new service or renew an existing one. We cover every state."),
    )


def corporate_records():
    reset_ids("records")
    return page(
        hero("Minutes &amp; records", "Your company's proof that it stands on its own.",
             "Corporate minutes and a complete record book document the decisions your company makes. When your protection is challenged, they're the evidence.",
             trail=[PROTECT, ("Minutes &amp; Records", "/protect-my-business/corporate-records/")], img="laughlin-notes", alt="Taking notes at a meeting"),
        prose("Corporate minutes", "Why minutes matter.", """
<p>Corporate minutes are legal records of the decisions your company makes during the year. State law requires corporations to prepare annual shareholder minutes, and board decisions should be documented too.</p>
<blockquote>&ldquo;The sole stockholder did not keep corporate minutes: the court held that such a circumstance justified a disregard of the corporate entity.&rdquo;<cite>Cohen v. Williams, 294 Ala. 417, 318 So. 2d 279</cite></blockquote>
<h3>Who asks to see your minutes</h3>
<ul><li>Courts and creditors</li><li>The IRS, in an audit</li><li>Banks, when you apply for a loan</li><li>State agencies</li><li>Shareholders, investors and buyers</li></ul>"""),
        section(C(C(head("Corporate record book", "Everything in one place.",
                         "A customized corporate or LLC kit keeps your company's key documents organized and ready."), cls=""),
                  includes("A Laughlin record book includes", ["Custom binder and matching slipcase", "Customized stock or membership certificates", "Stock transfer or membership ledger", "Corporate embossing seal", "Minutes and bylaws, or operating agreement", "Tabbed sections for every record"],
                           "Order a record book", "/contact/"), cls="split"), alt=True),
        band("Behind on your minutes?", "It's common, and fixable. Corporate Veil Protection can help you catch up and stay current.",
             ("Explore Corporate Veil Protection", "/protect-my-business/corporate-veil-protection/")),
    )


def common_mistakes():
    reset_ids("mistakes")
    items = [
        ("One owner dominating the company", "Common in small businesses. On its own it won't cost you your protection, but combined with other mistakes it can."),
        ("No corporate records", "Many companies that lose in court never held a single meeting. Record books without minutes put owners at risk."),
        ("No separate financial records", "If you can't show business and personal money are separate, you risk being accused of commingling funds."),
        ("Using company assets personally", "A sole proprietor can take cash from the till. A corporation's owner can't. The same goes for company property."),
        ("Under-capitalizing the company", "A company needs enough capital to have a fair chance of success, or it may not look like a real business."),
        ("Falling out of good standing", "If your state has revoked your company for missed fees or filings, it's hard to argue it's a real, separate business."),
        ("Signing as yourself, not the company", "Sign as an officer of the company (&ldquo;Company name, By: ___, President&rdquo;), never just your own name."),
        ("Not identifying the business as a company", "Customers and creditors should know they're dealing with a corporation or LLC, not you personally."),
        ("Running related companies together", "Each company needs its own meetings, records and bank accounts."),
        ("Ignoring formalities between related entities", "Deals between your own companies should be documented and at arm's length."),
    ]
    return page(
        hero("10 common mistakes", "The quiet mistakes that cost owners their protection.",
             "Courts can &ldquo;pierce the veil&rdquo; and reach your personal assets when a company isn't run as a separate business. These are the mistakes we see most.",
             trail=[PROTECT, ("10 Common Mistakes", "/protect-my-business/common-mistakes/")]),
        section(numbered(items)),
        band("Recognize any of these?", "Most are easy to fix. A free business review shows you where you stand.",
             ("Get a free business review", "/business-review/")),
    )


# ---------------------------------------------------------------- GROW
def grow_hub():
    reset_ids("grow")
    return page(
        hero("Grow my business", "Build what's next, on a solid foundation.",
             "As your business grows, so do your needs: credit in the company's name, a clear strategy and a plan for the assets you've built.",
             img="laughlin-planning", alt="A business owner planning",
             extra=btns(("Book a strategy consultation", "/business-review/", "gold"))),
        section(head("Grow", "Strengthen the business."),
                cards([("Funding", "Business credit", "Build credit in your company's name, separate from your personal credit.", "/grow-my-business/business-credit/", True),
                       ("Strategy", "Strategy consultation", "Time with an advisor on structure, goals and your next steps.", "/business-review/"),
                       ("Learn", "Live Q&amp;A and events", "Bring your questions. Hear from other owners.", "/resources/events/")])),
        section(head("Preserve", "Protect what you've built."),
                cards([("Planning", "Living trusts", "Organize your assets and spare your family probate delays.", "/grow-my-business/living-trusts/"),
                       ("Protection", "Asset protection", "Structure your holdings so one claim can't reach everything you own.", "/contact/"),
                       ("Closing", "Dissolving a company", "When it's time, close a company cleanly.", "/start-a-business/filing-services/")]), alt=True),
        section(C(C(head("Nevada office services", "A presence in Nevada, without moving.",
                         "For Nevada corporations and LLCs, Laughlin can provide a business address, mail forwarding and telephone answering in your company's name."), cls=""),
                  includes("Available for Nevada companies", ["Mail forwarding", "Live telephone answering in your company name", "Registered agent in Carson City"], "Ask about Nevada services", "/contact/"),
                  cls="split"), eid="nevada-office"),
        band("What's next for your business?", "Talk with an advisor about growing, funding or protecting what you've built."),
    )


def business_credit():
    reset_ids("credit")
    return page(
        hero("Business credit", "Fund your business without risking your personal credit.",
             "Business credit is tied to your company's identity, not yours. But it isn't automatic: it has to be built on purpose.",
             trail=[GROW, ("Business Credit", "/grow-my-business/business-credit/")], img="owner-desk", alt="A business owner reviewing paperwork",
             extra=btns(("Talk to us about business credit", "/contact/", "gold"))),
        prose("Why it matters", "Keep business and personal credit apart.", """
<p>Most small business owners fund their companies with personal credit. That ties your personal finances to the business's risks, and limits how far you can grow.</p>
<p>Business credit works like personal credit, but it's linked to your company's tax ID. Reporting agencies don't assign it automatically, so many owners never build a score at all.</p>
<h3>How Laughlin helps</h3>
<ul><li>Prepare your business to be lender-ready</li><li>Establish and build your company's credit profile</li><li>Connect you with lenders for credit lines, growth financing and equipment financing</li></ul>"""),
        section(head("Funding options", "What strong business credit can open up."),
                rows([("Credit lines", "Business credit lines", "Access to lenders offering credit in your company's name."),
                      ("Growth", "Growth financing", "Fund your next expansion with business loans."),
                      ("Equipment", "Equipment financing", "Finance the equipment you need through the business.")]), alt=True),
        band("Ready to build business credit?", "We'll help you prepare your company and build its profile, step by step."),
    )


def living_trusts():
    reset_ids("trusts")
    return page(
        hero("Living trusts", "Protect what you've built. Simplify what happens next.",
             "A living trust organizes your assets, helps your family avoid probate delays and sets out a clear plan for the people you care about.",
             trail=[GROW, ("Living Trusts", "/grow-my-business/living-trusts/")], img="advisor-seniors", alt="An advisor helping a couple plan",
             extra=btns(("Start your living trust", "/contact/", "gold"), ("Schedule a consultation", "/business-review/", "ghost"))),
        section(C(C(head("What is a living trust?", "Your plan, in your control.",
                         "A living trust holds your assets during your lifetime and passes them to your beneficiaries without going through probate. You stay in control while you're alive and well."),
                    X("""<div class="body"><h3>Why it matters</h3><p>Without a plan, your family can face probate delays, frozen accounts, confusion over business ownership and hard decisions at an already emotional time.</p></div>"""), cls=""),
                  includes("The living trust package includes", ["Revocable living trust", "Pour-over will", "Healthcare directive", "Financial power of attorney", "HIPAA authorization"],
                           "Get started", "/contact/"), cls="split")),
        section(rows([("Control", "Keep control of your assets", "You manage everything in the trust while you're alive and well."),
                      ("Probate", "Help your family avoid probate", "Fewer court delays and expenses for the people you leave behind."),
                      ("Privacy", "Keep it private", "Unlike a will, a trust generally doesn't become public record."),
                      ("Business", "Plan for your business", "Make clear who owns and runs your company next.")]), alt=True),
        band("Plan what comes next.", "Start your living trust, or talk it through with an advisor first."),
    )


# ---------------------------------------------------------------- RESOURCES
FAQ_ALL = [
    ("What happens after I form an LLC?", "You keep it in good standing. That means a registered agent, annual state filings, records of big decisions and business money kept separate from yours."),
    ("Is my LLC actually protecting me?", "Only if it's run like a separate business. Courts look at your records, your filings and whether business and personal money stay apart."),
    ("What can weaken corporate protection?", "Missed filings, a lapsed registered agent, no minutes, mixed bank accounts and contracts signed in your own name. See our list of the 10 most common mistakes."),
    ("Do I need corporate minutes?", "Corporations are generally required to keep them. LLCs benefit from them. Minutes are your proof the company makes its own decisions."),
    ("What does a registered agent do?", "Receives legal and state notices for your company at a reliable address and forwards them to you quickly, so nothing important gets missed."),
    ("Does my business structure still make sense?", "Revenue, partners and goals change, and your structure may need to change too. A yearly review catches it early."),
    ("When should I form a business entity?", "If you run a business, even part-time or from home, or you're about to start one, now is the time. An entity separates your personal liability from the business."),
    ("LLC or corporation: which is better?", "Neither is better for everyone. LLCs are simpler and more flexible; corporations offer more fringe benefits and make it easier to bring in investors. See our side-by-side comparison."),
    ("What is an S-Corporation?", "A regular corporation that has elected S status with the IRS (Form 2553), so profits and losses pass through to the shareholders. It has ownership limits, including 100 or fewer shareholders."),
    ("Do I need to live in Nevada to form a Nevada company?", "No. Owners, officers and directors can live anywhere. If you do business in another state, you'll usually need to qualify there too."),
    ("Can a non-U.S. resident form a U.S. company?", "Yes. Anyone can form a U.S. company, from any country. The process is largely the same as it is for U.S. citizens."),
    ("What is foreign qualification?", "Registering your company to do business in a state other than the one where it was formed. Skipping it can lead to penalties and fines."),
    ("Is business credit separate from my personal credit?", "It can be. Business credit is tied to your company's tax ID, but it has to be built on purpose; it isn't assigned automatically."),
    ("What is a living trust?", "A legal document that holds your assets during your lifetime and passes them to your beneficiaries without probate, while you stay in control."),
]


def resources_hub():
    reset_ids("res")
    return page(
        hero("Resources &amp; events", "Learn before you file.",
             "Plain-English answers, free guides and live events. Education has been part of Laughlin for decades.",
             img="laughlin-notes", alt="Taking notes at a Laughlin session"),
        section(cards([("Straight answers", "Business questions", "The questions owners ask us most, answered in plain English.", "/resources/business-questions/", True),
                       ("Live", "Events &amp; webinars", "Live Q&amp;A, workshops and the Magnify Your Wealth Summit.", "/resources/events/"),
                       ("Protect", "10 common mistakes", "The mistakes that most often cost owners their protection.", "/protect-my-business/common-mistakes/")])),
        section(head("Free guides", "Download, read, then call us with questions."),
                rows([("Starting", "LLC Quick Start Guide", "The what, when and why of the LLC, and how it compares to a corporation."),
                      ("Starting", "Making the Right Business Choice", "Sole proprietorships, partnerships, corporations, LLCs and nonprofits, explained."),
                      ("Strategy", "Incorporate: The Road to Riches", "How business owners can use the same strategies as big companies, by following the rules."),
                      ("Protecting", "The Importance of Corporate Record Keeping", "Why records are what keep your protection and tax benefits intact."),
                      ("Growing", "Survive &amp; Thrive", "Ten things every business owner should have in place, whatever the economy is doing."),
                      ("Nevada", "Why Nevada?", "Whether forming in Nevada can benefit your business.")]),
                X(btns(("Request a guide", "/contact/", ""))), alt=True, eid="guides"),
        band("Have a question we didn't answer?", "Call and ask. Real advisors, plain English, no pressure."),
    )


def business_questions():
    reset_ids("faq")
    return page(
        hero("Business questions", "Straight answers. Plain English.",
             "The questions business owners ask us every day, about starting, protecting and growing a company.",
             trail=[RES, ("Business Questions", "/resources/business-questions/")]),
        C(C(C(head("Ask Laughlin", "Common questions.", "Don't see yours? Call us. That's what we're here for."),
              X(btns(("Ask an advisor", "/contact/", "gold"))), cls="cv-copy"),
            faq(FAQ_ALL), cls="wrap faq-grid"), cls="sec", tag="section"),
        band("Still have questions?", "Talk with an advisor. No pressure, just answers."),
    )


def events():
    reset_ids("events")
    return page(
        hero("Events &amp; webinars", "Learn live. Ask questions. Meet other owners.",
             "Laughlin's events bring business owners together to learn how to start, protect and grow their companies.",
             trail=[RES, ("Events &amp; Webinars", "/resources/events/")], img="laughlin-roundtable", alt="Business owners at a Laughlin workshop"),
        section(cards([("Online &middot; Free", "LAI Business Edge: Live Q&amp;A", "Bring your questions about structure, compliance and protection. Our advisors answer them live.", "/contact/", True),
                       ("Nov 13&ndash;15, 2026 &middot; Dallas", "Magnify Your Wealth Summit", "Three days of strategy for business owners and investors.", "/contact/"),
                       ("Ongoing", "Workshops &amp; webinars", "Sessions on entity structure, compliance, business credit and more.", "/contact/")])),
        section(C(C(head("Upcoming dates", "Event calendar.",
                         "Dates for upcoming webinars and workshops will be listed here. Call us or send a note to reserve a seat."), cls=""),
                  includes("What to expect", ["Plain-English education, no sales pitch", "Real questions from real owners", "Time with Laughlin advisors"], "Reserve a seat", "/contact/"),
                  cls="split"), alt=True),
        band("Want to be notified about events?", "Send us a note and we'll let you know when the next session is scheduled."),
    )


# ---------------------------------------------------------------- COMPANY
def clients():
    reset_ids("clients")
    return page(
        hero("Existing clients", "Welcome back.",
             "Renew services, make a payment or get help from your advisor. Everything you need, in one place.",
             img="laughlin-advisor", alt="A Laughlin advisor"),
        section(cards([("Renew", "Renew Registered Agent", "Keep your registered agent service current.", "/contact/", True),
                       ("Renew", "Renew Corporate Veil Protection", "Another year of minutes, records and reviews.", "/contact/"),
                       ("Renew", "Renew Nevada mail forwarding", "Keep your Nevada mail forwarding active.", "/contact/"),
                       ("Pay", "Make a payment", "Pay an invoice or renewal.", "/contact/"),
                       ("Support", "Schedule client support", "Book time with your advisor.", "/contact/"),
                       ("Resources", "Client resources", "Guides, checklists and answers.", "/resources/")])),
        section(C(C(head("Need help now?", "Call your advisor.", f"Our office is open {HOURS}."), cls=""),
                  X(f"""<div class="ways"><div class="way"><small>Call</small><div><a href="{TEL}">{PHONE}</a></div></div>
<div class="way"><small>Toll-free</small><div><a href="{TOLLFREE_TEL}">{TOLLFREE}</a><p>Se habla espa&ntilde;ol</p></div></div></div>"""),
                  cls="split"), alt=True),
    )


def business_review():
    reset_ids("review")
    return page(
        hero("Free business review", "Is your company still protecting you?",
             "Whether you're about to start or you've been in business for years, a complimentary consultation gets you answers for your specific situation.",
             img="advisor-table", alt="An advisor meeting with business owners",
             extra=btns(("Schedule your review", "/contact/", "gold"), (f"Call {TOLLFREE}", TOLLFREE_TEL, "ghost"))),
        section(C(C(head("What we'll cover", "One conversation. A clear next step."),
                    numbered([("Your goals", "Where your business is today, and where you want it to go."),
                              ("Your options", "The structure, protection and filings that fit, explained plainly."),
                              ("Your next steps", "What to do now, what can wait, and how we can help.")]), cls=""),
                  includes("Good to have handy", ["Your company name and state", "Your entity type (LLC, corporation, etc.)", "Your last annual filing date", "Any questions on your mind"]),
                  cls="split")),
        band("Save hours of research.", "Get answers that apply to your situation. No pressure, no obligation.", ("Schedule your review", "/contact/")),
    )


def privacy():
    reset_ids("privacy")
    return page(
        hero("Privacy policy", "Your privacy matters to us.",
             "How Laughlin Associates collects, uses and protects your information."),
        section(X(f"""<div class="legal">
<h2>Laughlin Associates Privacy Policy</h2>
<p>Laughlin Associates has nothing but the highest respect for your privacy. We collect client information to help you:</p>
<ul><li>Find the information, products and services you came to our website to learn about</li>
<li>Stay on top of important deadlines (taxes, renewals, seminar information and more)</li>
<li>Learn about special offers relevant to you</li></ul>
<p>We recognize the importance of privacy to our clients, so we maintain and use client information responsibly. <strong>We never rent or sell the information you provide to us online to third parties.</strong></p>
<p>If you have any questions about our privacy policy, please contact us. We'll be happy to address any questions or concerns.</p>
<h2>Our security safeguards</h2>
<p>We do our utmost to provide a safe and convenient online experience. That includes safeguarding the integrity of our customers' payment information.</p>
<p>We use SSL (secure sockets layer) encryption to protect your payment information as it's transmitted to us. SSL scrambles data as it travels from your computer to our servers.</p>
<p>If you'd rather not register for a seminar, form a company or buy our publications online, call us at <a href="{TOLLFREE_TEL}">{TOLLFREE}</a> and a consultant will be happy to help.</p>
<h2>Contact us</h2>
<p>Laughlin Associates, Inc.<br>{ADDRESS}<br>Phone: <a href="{TEL}">{PHONE}</a> &middot; Toll-free: <a href="{TOLLFREE_TEL}">{TOLLFREE}</a></p>
</div>""")),
    )
