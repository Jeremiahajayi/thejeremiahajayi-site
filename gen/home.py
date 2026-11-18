#!/usr/bin/env python3
"""Homepage: creative confidence with editorial discipline.

Writes the homepage body (hero through contact) and its stylesheet into
project/Home-B2.dc.html. Header, guide and shared CSS come from sync_home.py.
Core palette: ink, paper, cream, orange. Accents (sun, mint, blush, night) are
used section by section; lavender belongs to EmpowerQ.
"""
import json, pathlib, re

HOME = pathlib.Path(__file__).parent.parent / 'project' / 'Home-B2.dc.html'
B = lambda i: '/_blob/' + i
CAL = 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi'
ARR = '<span class="arr" aria-hidden="true">→</span>'

IMG = dict(
    head='ab01351679f0c21d14aae4bf06f3affa', serp='97c7a07c9e01d68334e57d95e5d31f53', results='fc39c3db9800ffc1933e240a5186b657',
    certn_team='059d23d54fba852a7e2e28c2b4ef3db4', certn_sec='36e76e09b9ca821b9929e0aefe6a563a', certn_chk='bf5746c3149793e151b4bc8233744e8b',
    askai='b231344f1e5c3214a838fe77d08c503f', xofu='0dfa31b585c479139da9600a8bdd8b9d', xofu_price='a4cbf106e17930bec111332800b706fd',
    xofu_news='690c37a910717b44a095316769f59bf8', mena='04684a9d91b293a1856c9baf69694f0d', guides='805be6f1e5453616f33a1d34c9c1f227',
    ksa='11081f461253fb84fb4a4bb9bf11f88b', cover='33c1f064948e333f4df17633271445aa', contents='7eb8244cdcb54835b411e77a562f76ac',
    award='1ada8c43b66919c70ad6d23904db5df0', tags='2887802b6b670e13694193452b911747',
)

# Hero rows: verb, number, discipline, hover hint, service page, project shown beside the portrait
LINES = [
    ('clear', '01', 'Positioning & messaging', 'A story buyers can repeat', 'Site-Service-Positioning.dc.html',
     IMG['xofu'], 'Xofu · the homepage I rewrote'),
    ('land', '02', 'Launches & go-to-market', 'Launches built for pipeline', 'Site-Service-Launch.dc.html',
     IMG['askai'], 'RemotePass · the Ask AI launch'),
    ('travel', '03', 'Content & storytelling', 'Content that keeps working', 'Site-Service-Content.dc.html',
     IMG['serp'], 'Stears · #1 on Google, above the BBC'),
]

FACTS = [
    'Ẹ káàbọ̀! That’s “welcome” in Yoruba.',
    'I almost became a lawyer. The story’s further down.',
    'I work from Lagos with teams in Europe, North America, the Middle East and Africa.',
    'In 2025 I co-founded EmpowerQ, a career nonprofit for queer Nigerians.',
    'One of my Buffer guest posts ranked #1 on Google for its main search phrase.',
]

QUOTES = [
    ('He doesn’t just blur the lines between Sales and Marketing—he obliterates them.', 'Wesley Hattingh', 'RemotePass', 'q-sun'),
    ('I got a front-row seat to how brilliant, resourceful, and proactive Jeremiah was.', 'Adetoro Adeniran', 'Stears', 'q-mint'),
    ('I think expectations from you are always so much but you deliver without fail.', 'Shivani Saxena', 'RemotePass', 'q-blush'),
    ('You did a great job with the marketing plan for the FX Monitor.', 'Yvette Dimiri', 'Stears', 'q-paper'),
]

DISCIPLINES = [
    ('Clear', '🔍', 'd-clear', 'shp-flower', 'Positioning & messaging', 'Finding what makes a product worth choosing, then turning it into a story the whole company can tell the same way.', 'Xofu', 'Site-Service-Positioning.dc.html'),
    ('Land', '🚀', 'd-land', 'shp-star', 'Launches & go-to-market', 'Launches planned end to end, from narrative and timing to press, partners and the material sales needs on day one.', 'RemotePass × Certn, the Ask AI launch, and 20+ launches I’ve led', 'Site-Service-Launch.dc.html'),
    ('Travel', '✈️', 'd-travel', 'shp-clover', 'Content & storytelling', 'Content people seek out and share, built to keep working long after it’s published.', 'Stears Elections and the RemotePass content engine', 'Site-Service-Content.dc.html'),
]


def hero():
    rows = ''.join(
        f'<a class="h-row" href="{href}" data-peek="{i}" style="--i:{i}"><span class="h-tag"><span class="h-num">{num}</span>{name}<span class="h-tag-s">{sub} →</span></span>'
        f'<span class="h-line"><span class="h-mk">Make it</span> <span class="h-verb v{i + 1}"><span class="h-ink" aria-hidden="true"></span><span class="h-vt">{verb}.</span></span></span></a>'
        for i, (verb, num, name, sub, href, img, cap) in enumerate(LINES)
    )
    peeks = ''.join(
        f'<figure class="h-peek{" is-on" if i == 0 else ""}" data-peek-card="{i}"><figcaption>{cap}</figcaption><img src="{B(img)}" alt="" loading="{"eager" if i == 0 else "lazy"}"></figure>'
        for i, (verb, num, name, sub, href, img, cap) in enumerate(LINES)
    )
    facts = json.dumps(FACTS, ensure_ascii=False).replace('"', '&quot;')
    return f'''<section id="top" class="h-hero" data-hero data-sky="day">
<div class="h-sky" aria-hidden="true"><span class="h-stars"></span><span class="h-sun"></span></div>
<div class="h-rays" aria-hidden="true"></div>
<div class="wrap h-grid">
<div class="h-copy">
<p class="h-hello"><span lang="yo">Ẹ káàbọ̀</span><span aria-hidden="true">·</span><span>Lagos, {{{{time}}}}</span><span class="h-skyl" data-sky-label></span></p>
<h1 class="h-id"><b>Jeremiah Ajayi</b> is a marketing consultant for B2B SaaS and technology companies.</h1>
<p class="h-display sg">{rows}</p>
</div>
<div class="h-stage">
<div class="h-peeks" aria-hidden="true">{peeks}</div>
<span class="shp shp-flower h-flower" aria-hidden="true"></span>
<div class="shp shp-scallop h-photo"><img src="{B(IMG['head'])}" alt="Portrait of Jeremiah Ajayi" width="800" height="800"></div>
<div class="h-ring" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="h-ring-p" d="M60,60 m-47,0 a47,47 0 1,1 94,0 a47,47 0 1,1 -94,0"/></defs><text><textPath href="#h-ring-p" textLength="290" lengthAdjust="spacingAndGlyphs">CONTENT MARKETING SPECIALIST OF THE YEAR · 2025 ·</textPath></text></svg><span class="sg">Martech<br>Africa</span></div>
<button type="button" class="h-bub" data-facts="{facts}" aria-live="polite" onClick="{{{{nextFact}}}}"><span class="h-bub-t">{{{{fact}}}}</span><span class="h-bub-more">Tell me something else <span aria-hidden="true">↻</span></span></button>
</div>
<div class="h-foot">
<p class="h-lede">I help ambitious teams get understood, launched and chosen. Eight years of positioning, launches and content for companies in Europe, North America, the Middle East and Africa.</p>
<div class="h-cta"><a class="btn-o h-btn" href="#work">See the work <span class="arr arr-d" aria-hidden="true">↓</span></a><a class="h-btn h-btn-ink" href="{CAL}">Book a call <span class="arr" aria-hidden="true">↗</span></a><a class="h-hire" href="Site-Contact.dc.html#hiring">Hiring? I’m open to senior marketing roles {ARR}</a></div>
</div>
</div>
</section>'''


def logos():
    return '''<div class="lg-band" aria-label="Clients and collaborators">
<div class="wrap lg-head"><p class="eyebrow">Teams I’ve worked with</p></div>
<div class="lt-wrap">
<ul class="logo-track">
<sc-for list="{{clientsLoop}}" as="n" hint-placeholder-count="18"><li aria-hidden="{{n.dup}}"><img class="logo-i" src="{{n.src}}" alt="{{n.a}}" style="height: {{n.h}}; width: auto; display: block"></li></sc-for>
</ul>
</div>
</div>'''


def meta(n, client, year, disc):
    return f'<p class="pc-meta"><span class="pc-n sg">{n}</span><span class="pc-client">{client} · {year}</span><span class="pc-disc">{disc}</span></p>'


def facts_dl(role, made, result):
    return (f'<dl class="pc-dl"><div><dt>My role</dt><dd>{role}</dd></div><div><dt>What we made</dt><dd>{made}</dd></div>'
            f'<div class="pc-res"><dt>Result</dt><dd>{result}</dd></div></dl>')


def stears():
    return f'''<article class="pc pc-stears" id="stears" aria-labelledby="st-title">
<div class="st-head">
{meta('01', 'Stears', '2023', 'Content & storytelling')}
<h3 id="st-title" class="sg pc-title st-title">How a new election tracker beat the BBC on Google</h3>
</div>
<div class="st-body">
<div class="st-copy">
<div class="st-tabs" role="tablist" aria-label="The Stears case">
<button type="button" role="tab" id="st-t0" aria-controls="st-p0" aria-selected="true" data-st="0">The challenge</button>
<button type="button" role="tab" id="st-t1" aria-controls="st-p1" aria-selected="false" tabindex="-1" data-st="1">What I did</button>
<button type="button" role="tab" id="st-t2" aria-controls="st-p2" aria-selected="false" tabindex="-1" data-st="2">The result</button>
</div>
<div class="st-panel" role="tabpanel" id="st-p0" aria-labelledby="st-t0"><p>Stears rebuilt Nigeria’s first real-time election tracker for the 2023 general election. As the content and SEO lead, my job was to make sure millions of Nigerians could find it, and trust it, the moment results started coming in.</p><p class="st-role">I worked across editorial, engineering, data and design.</p></div>
<div class="st-panel" role="tabpanel" id="st-p1" aria-labelledby="st-t1" hidden><ol class="st-steps"><li>Built the search strategy from scratch for questions like “2023 election results” and “presidential candidates Nigeria”.</li><li>Designed programmatic candidate profiles: 10,000+ pages covering every candidate for governor, senate and president.</li><li>Trained the analyst team, mostly economists, to publish for search, and kept pages accurate and fast at peak traffic.</li></ol></div>
<div class="st-panel" role="tabpanel" id="st-p2" aria-labelledby="st-t2" hidden><div class="st-results"><p><span class="sg st-big st-hot">#1</span><span>on Google for “2023 election results”, above the BBC, CNN and INEC</span></p><p><span class="sg st-big">1.9M+</span><span>users, 52% of them from search</span></p></div></div>
<p class="st-next"><a class="h-link" href="Site-Work.dc.html#stears">Read the full case study {ARR}</a></p>
</div>
<div class="st-stage" aria-hidden="true">
<div class="st-v is-on" data-v="0"><img src="{B(IMG['results'])}" alt="" loading="lazy"><span class="st-chip">The Stears Elections results page</span></div>
<div class="st-v" data-v="1"><div class="st-dots"><span class="st-dots-on"></span></div><p class="st-dots-n"><b class="sg">10,000+</b> candidate pages, covering every candidate for governor, senate and president</p></div>
<div class="st-v" data-v="2"><img class="st-serp" src="{B(IMG['serp'])}" alt="" loading="lazy"><ol class="st-rank"><li class="st-me"><b>#1</b> Stears Elections</li><li>BBC</li><li>CNN</li><li>INEC</li></ol><span class="st-chip">Google, “2023 election results”</span></div>
</div>
</div>
</article>'''


def certn():
    return f'''<article class="pc pc-certn" id="certn-home">
<div class="pc-media cn-media">
<img class="cn-a" src="{B(IMG['certn_sec'])}" alt="Launch visual: candidate data secured by Certn" loading="lazy">
<img class="cn-b" src="{B(IMG['certn_chk'])}" alt="Launch visual: a completed background check, powered by Certn" loading="lazy">
<img class="cn-c" src="{B(IMG['certn_team'])}" alt="RemotePass × Certn launch visual" loading="lazy">
<ul class="cn-press" aria-label="Where the launch was covered"><li>Yahoo Finance</li><li>Fox</li><li>NBC</li></ul>
</div>
<div class="pc-copy">
{meta('02', 'RemotePass × Certn', '2024', 'Launches & go-to-market')}
<h3 class="sg pc-title"><a class="pc-go" href="Site-Work.dc.html#certn">The partnership launch that went global</a></h3>
<p class="pc-big"><span class="sg">270+</span> media pickups in the weeks after a $5.5M raise</p>
{facts_dl('Ran go-to-market end to end, positioning the integration as proof RemotePass was ready for enterprise buyers.', 'The launch narrative and timing with Certn’s global team, the press push, and sales enablement.', 'Coverage including Yahoo Finance, Fox and NBC, and enterprise conversations in fintech and healthtech.')}
</div>
</article>'''


def askai():
    return f'''<article class="pc pc-askai" id="askai-home">
<div class="pc-copy">
{meta('03', 'RemotePass Ask AI', '2025', 'Launches & go-to-market')}
<h3 class="sg pc-title"><a class="pc-go" href="Site-Work.dc.html#askai">Everyone was selling AI. We sold the answer.</a></h3>
{facts_dl('Led the launch campaign for Ask AI, RemotePass’s newest feature, at the peak of the AI craze.', 'One idea, carried from the landing page to the announcement video to sales enablement: HR leaders can simply ask their workforce data a question.', 'Record MQL performance, and a sales team flooded with enquiries about the product.')}
<p class="pc-links"><a class="pc-ext" href="https://lnkd.in/p/gMXYb4hH">Watch the announcement <span aria-hidden="true">↗</span></a><a class="pc-ext" href="https://www.remotepass.com/ai">See the landing page <span aria-hidden="true">↗</span></a></p>
</div>
<div class="pc-media ai-media">
<img src="{B(IMG['askai'])}" alt="The Ask AI launch page on remotepass.com: Get answers from your workforce data and let Ask AI do the rest" loading="lazy">
<span class="ai-q" aria-hidden="true">Ask your workforce data a question</span>
</div>
</article>'''


def xofu():
    return f'''<article class="pc pc-xofu" id="xofu-home">
<div class="xf-top">
{meta('04', 'Xofu', '2026', 'Positioning & messaging')}
<p class="sg xf-quote" aria-hidden="true">“Does AI <span>recommend</span> us?”</p>
<p class="xf-sub">The one buyer question I rebuilt an AI visibility platform’s story around.</p>
</div>
<div class="xf-grid">
<div class="pc-media xf-media">
<img class="xf-a" src="{B(IMG['xofu'])}" alt="Xofu homepage hero from the rewrite: Grow your brand’s visibility in AI search" loading="lazy">
<img class="xf-b" src="{B(IMG['xofu_price'])}" alt="Xofu pricing draft with four tiers" loading="lazy">
<img class="xf-c" src="{B(IMG['xofu_news'])}" alt="Xofu newsletter layout" loading="lazy">
</div>
<div class="pc-copy">
<h3 class="sg pc-title"><a class="pc-go" href="Site-Work.dc.html#xofu">Giving a new AI product one clear question to answer</a></h3>
{facts_dl('Head of Product Marketing for a platform in a brand-new category, with no story buyers could repeat.', 'New positioning, the website, pricing, onboarding emails and the Citation Audit launch.', 'The launch email reached a <b>3.7% click-through rate</b>, double the previous best.')}
</div>
</div>
</article>'''


def engine():
    return f'''<article class="pc pc-engine" id="engine-home">
<div class="pc-copy">
{meta('05', 'RemotePass', '2024–25', 'Content & storytelling')}
<h3 class="sg pc-title"><a class="pc-go" href="Site-Work.dc.html#engine">A content engine for global hiring, with an English–Arabic hub</a></h3>
<div class="en-stats"><p><span class="sg">174%</span>organic user acquisition, year on year</p><p><span class="sg">$500K+</span>pipeline influenced in under a year</p></div>
{facts_dl('Joined after a $5.5M raise and built RemotePass’s first content strategy across the whole customer journey, with a freelance team I hired and briefed.', 'SEO content that ranks on page one, thought leadership featured on Wamda, a help centre and product videos, and sales decks, one-pagers and case studies.', '$192K in revenue in Q1 2025 alone from people who found us through content, with no ad spend.')}
</div>
<div class="pc-media en-media">
<img class="en-a" src="{B(IMG['mena'])}" alt="The RemotePass MENA hub for payroll and HR, in English and Arabic" loading="lazy">
<img class="en-b" src="{B(IMG['guides'])}" alt="The RemotePass country guides hub, with guides filtered by region" loading="lazy">
<img class="en-c" src="{B(IMG['ksa'])}" alt="KSA payroll campaign carousel cover" loading="lazy">
</div>
</article>'''


def work():
    return f'''<div class="sheet" data-sheet>
{logos()}
<section id="work" class="sw" aria-labelledby="sw-title">
<div class="wrap">
<div class="sw-head">
<p class="eyebrow">Selected work</p>
<h2 id="sw-title" class="sg sw-title">Work where the story <em>changed</em> the outcome.</h2>
<p class="sw-sum">Five projects, each with what I was responsible for, what we made and what happened. Across my work: <b>$3M+</b> in pipeline influenced and <b>20+</b> launches led.</p>
</div>
{stears()}
<div class="pc-pair">
{certn()}
{askai()}
</div>
{xofu()}
{engine()}
<p class="sw-all"><a class="btn-o h-btn" href="Site-Work.dc.html">All case studies {ARR}</a></p>
</div>
</section>
</div>'''


def quotes():
    cards = ''.join(
        f'<figure class="qt {cls}"><blockquote class="sg">“{q}”</blockquote><figcaption><b>{who}</b> · {org}</figcaption></figure>'
        for q, who, org, cls in QUOTES
    )
    return f'''<section class="qs" aria-labelledby="qs-title">
<div class="wrap">
<p class="eyebrow">In their words</p>
<h2 id="qs-title" class="sg qs-title">What it’s like to work with me, from the people who did.</h2>
<div class="qt-row">{cards}</div>
</div>
</section>'''


def expertise():
    cards = ''.join(
        f'<a class="xd {cls}" href="{href}"><span class="xd-badge"><span class="shp {shp} xd-shp" aria-hidden="true"></span><span class="xd-emo" aria-hidden="true">{emo}</span></span>'
        f'<span class="xd-verb sg">{verb}<i>.</i></span><span class="xd-name sg">{name}</span><span class="xd-long">{long}</span>'
        f'<span class="xd-proof"><b>See it in</b> {proof}</span><span class="xd-go">See the service {ARR}</span></a>'
        for verb, emo, cls, shp, name, long, proof, href in DISCIPLINES
    )
    return f'''<section id="expertise" class="xs" aria-labelledby="xs-title">
<div class="wrap">
<div class="xs-head"><h2 id="xs-title" class="sg xs-title">Three disciplines. One job: helping good products get chosen.</h2>
<p class="xs-sub">Research, SEO, AI search and sales enablement are how I do the work. These three are what the work is for.</p></div>
<div class="xd-grid">{cards}</div>
</div>
</section>'''


def research():
    return f'''<section id="research" class="rs" aria-labelledby="rs-title">
<div class="wrap rs-grid">
<figure class="rs-fan" data-inview>
<a href="https://stateofaisearchinnigeria.eo.page/download" aria-label="Read The State of AI Search in Nigeria">
<img class="rs-back" src="{B(IMG['contents'])}" alt="" loading="lazy">
<img class="rs-front" src="{B(IMG['cover'])}" alt="Cover of The State of AI Search in Nigeria, by Jeremiah Ajayi and Felix Akinnibi" loading="lazy" width="1000" height="1414">
<span class="rs-sticker sg" aria-hidden="true">A first<br>for Nigeria</span>
</a>
<figcaption><b>The State of AI Search in Nigeria</b><span>2026 · 71 pages · co-authored with Felix Akinnibi</span></figcaption>
</figure>
<div class="rs-copy">
<p class="eyebrow">Writing & research</p>
<h2 id="rs-title" class="sg rs-title">I write about how buyers find, judge and <span>choose.</span></h2>
<ul class="rs-list">
<sc-for list="{{{{writing}}}}" as="w" hint-placeholder-count="6"><li><a class="rs-row" href="{{{{w.href}}}}"><span class="rs-outlet">{{{{w.outlet}}}}</span><span class="rs-t">{{{{w.title}}}}</span><span class="rs-note">{{{{w.note}}}}</span></a></li></sc-for>
</ul>
<p><a class="h-link" href="Site-Writing.dc.html">All writing and research {ARR}</a></p>
</div>
</div>
</section>'''


def about():
    return f'''<section id="about" class="ab" aria-labelledby="ab-title">
<div class="wrap ab-grid">
<div class="ab-copy">
<p class="eyebrow">The short version</p>
<h2 id="ab-title" class="sg ab-title" data-inview>I was meant to be a <span class="ab-strike">lawyer<i aria-hidden="true"></i></span><span class="ab-ins" aria-hidden="true">marketer</span>.</h2>
<p>In 2018, in a law lecture I barely remember, a friend told me about freelance writing. I wrote my way into strategy, then into marketing for some of Africa’s most watched startups, then for teams around the world.</p>
<p>Along the way I kept opening doors for others: Digivention, a career conference for 1,000+ young Nigerians; Write to Win, for freelance writers; and Wednesday Goodness, a career newsletter read by 900+ people. EmpowerQ is where that became a mission.</p>
<p><a class="h-link" href="Site-About.dc.html">Read the longer story {ARR}</a></p>
</div>
<figure class="ab-photo"><img class="img-rv" src="{B(IMG['award'])}" alt="Jeremiah receiving the Martech Africa award for Content Marketing Specialist of the Year" loading="lazy"><span class="ab-stk" aria-hidden="true">🏆</span><figcaption>Receiving Martech Africa’s Content Marketing Specialist of the Year, 2025</figcaption></figure>
</div>
<div class="wrap">
<div class="tl" data-tl>
<p class="eyebrow">The route so far</p>
<div class="tl-track"><span class="tl-fill"></span><span class="tl-plane" aria-hidden="true">✈️</span></div>
<ol class="tl-list">
<sc-for list="{{{{route}}}}" as="r" hint-placeholder-count="8"><li class="tl-i" style="--dot: {{{{r.dot}}}}"><span class="tl-y sg">{{{{r.year}}}}</span><span class="tl-w">{{{{r.what}}}}</span></li></sc-for>
</ol>
</div>
</div>
</section>'''


def empowerq():
    return f'''<section id="empowerq" class="eq" aria-labelledby="eq-title">
<span class="shp shp-flower eq-s1" aria-hidden="true"></span><span class="shp shp-clover eq-s2" aria-hidden="true"></span>
<div class="wrap eq-grid">
<div class="eq-copy">
<p class="eq-top"><span class="eyebrow eq-eyebrow">The work I care about most</span><span class="eq-pill">Finalist · Social Shifters Global Innovation Challenge 2026</span></p>
<h2 id="eq-title" class="sg eq-title">EmpowerQ</h2>
<p class="eq-lede sg">Every queer Nigerian professional deserves a fair shot at a good career.</p>
<p>Many LGBTQ+ Nigerians are shut out of the networks, mentorship and fair hiring that careers depend on. I co-founded EmpowerQ in 2025 to change that, with practical support, honest research and a community that makes work safer.</p>
<ul class="eq-list">
<sc-for list="{{{{programs}}}}" as="p" hint-placeholder-count="5"><li><b>{{{{p.name}}}}</b><span>{{{{p.line}}}}</span></li></sc-for>
</ul>
<div class="eq-cta"><a class="eq-btn" href="https://www.empowerqueer.org">Visit EmpowerQ <span class="arr" aria-hidden="true">↗</span></a><a class="eq-link" href="mailto:jeremiah@thejeremiahajayi.com?subject=Partnering%20with%20EmpowerQ">Partner or fund our work {ARR}</a></div>
</div>
<figure class="eq-photo"><img class="img-rv" src="{B(IMG['tags'])}" alt="Name tags and lanyards for Out of Office, EmpowerQ’s queer career conference" loading="lazy"><span class="eq-badge sg"><b>100+</b>at our first Out of Office</span><figcaption>We keep attendees’ faces off the web.</figcaption></figure>
</div>
</section>'''


def contact():
    return f'''<section id="contact" class="ct" aria-labelledby="ct-title">
<div class="wrap">
<h2 id="ct-title" class="sg ct-title">What are you working on?</h2>
<div class="ct-grid">
<div class="ct-doors" role="radiogroup" aria-label="What you need">
<sc-for list="{{{{doors}}}}" as="d" hint-placeholder-count="5">
<button class="door ct-door" data-css data-door="{{{{$index}}}}" role="radio" aria-checked="{{{{d.selected}}}}" onClick="{{{{d.pick}}}}"><span class="ct-ic" aria-hidden="true">{{{{d.e}}}}</span><span class="ct-label sg">{{{{d.label}}}}</span><span class="ct-who">{{{{d.who}}}}</span></button>
</sc-for>
</div>
<div class="ct-panel" aria-live="polite">
<p class="ct-p-who" data-slot="who">{{{{door.who}}}}</p>
<p class="sg ct-p-title" data-slot="title">{{{{door.title}}}}</p>
<p class="ct-p-body" data-slot="body">{{{{door.body}}}}</p>
<a class="btn-o ct-p-cta" data-slot="cta" href="{{{{door.href}}}}">{{{{door.cta}}}}</a>
<p class="ct-p-mail">Or write to me directly: <a href="mailto:jeremiah@thejeremiahajayi.com">jeremiah@thejeremiahajayi.com</a></p>
</div>
</div>
<footer class="ct-foot">
<span class="sg ct-brand"><span aria-hidden="true" class="ct-mark">JA</span>Jeremiah Ajayi</span>
<span class="ct-nav"><a href="https://www.linkedin.com/in/jeremiah-ajayi/">LinkedIn</a><a href="Site-Work.dc.html">Work</a><a href="Site-Writing.dc.html">Writing</a><a href="Site-About.dc.html">About</a><a href="Site-Contact.dc.html">Contact</a><span>Lagos 🇳🇬 · {{{{time}}}} · © 2026</span></span>
</footer>
</div>
</section>'''


CSS = r'''
/*home:start*/
.wrap{max-width:1280px;margin:0 auto;padding-left:clamp(20px,5vw,48px);padding-right:clamp(20px,5vw,48px);box-sizing:border-box}
.eyebrow{margin:0 0 18px;font:700 12.5px/1.4 'DM Sans',system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;color:#6B675F}
.h-link{display:inline-flex;align-items:center;gap:8px;color:inherit;font-weight:700;font-size:16px;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px;text-decoration-color:#FF5A2A;transition:color .25s}
.h-link:hover{color:inherit}
.h-link:hover .arr{transform:translateX(5px)}
/* ---------- hero ---------- */
.h-hero{position:relative;background:#FFF5D9;color:#111;overflow:hidden;isolation:isolate}
.h-rays{position:absolute;left:calc(var(--sx,72%) - 45vw);top:calc(var(--sy,18%) - 45vw);width:90vw;height:90vw;color:var(--ray,#FFC83D);opacity:var(--rop,.55);z-index:-1;transition:color 1.5s,opacity 1.5s;background:repeating-conic-gradient(from 0deg at 50% 50%,currentColor 0 4deg,transparent 4deg 11deg);-webkit-mask:radial-gradient(closest-side,#000 40%,transparent 100%);mask:radial-gradient(closest-side,#000 40%,transparent 100%);animation:spin 160s linear infinite}
.h-grid{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);grid-template-areas:"copy stage" "foot stage";column-gap:clamp(24px,4vw,64px);padding-top:clamp(28px,3.4vw,52px);padding-bottom:clamp(44px,5vw,72px)}
.h-copy{grid-area:copy}.h-stage{grid-area:stage}.h-foot{grid-area:foot}
.h-hello{margin:0 0 10px;display:flex;gap:10px;font-size:14px;font-weight:600;color:#6B675F}
.h-hello span:first-child{color:#111}
.h-id{margin:0 0 clamp(18px,2.2vw,28px);max-width:36ch;font:500 18px/1.5 'DM Sans',system-ui,sans-serif;color:#45423C}
.h-id b{color:#111}
.h-display{margin:0;display:flex;flex-direction:column;gap:clamp(4px,.6vw,10px);font-weight:700;font-size:clamp(50px,6.6vw,104px);line-height:.96;letter-spacing:-.055em}
.h-row{display:flex;flex-direction:column;align-items:flex-start;color:#111;text-decoration:none;will-change:transform}
.h-row:nth-child(2){padding-left:clamp(0px,4vw,64px)}
.h-row:nth-child(3){padding-left:clamp(0px,8vw,128px)}
.h-tag{order:2;margin-top:8px;display:inline-flex;align-items:center;gap:10px;padding:5px 12px 5px 6px;border:1.5px solid #111;border-radius:999px;background:#FFFDF6;font:600 13px/1.2 'DM Sans',system-ui,sans-serif;letter-spacing:0;transition:background .3s,color .3s}
.h-num{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:#111;color:#FFF5D9;font:700 10.5px 'Space Grotesk',system-ui,sans-serif}
.h-tag-s{max-width:0;overflow:hidden;white-space:nowrap;opacity:0;transition:max-width .45s cubic-bezier(.2,.8,.2,1),opacity .3s}
.h-line{white-space:nowrap}
.h-mk{color:#111}
.h-verb{position:relative;display:inline-block;padding:0 .12em .04em;transition:transform .45s cubic-bezier(.2,.8,.2,1)}
.h-ink{position:absolute;inset:.06em 0 0;border-radius:.14em;transform-origin:left center;animation:ink .7s cubic-bezier(.7,0,.2,1) both;animation-delay:calc(.35s + var(--i) * .22s)}
.h-row[style*="--i:0"] .h-ink,.v1 .h-ink{background:#FFC83D}
.v2 .h-ink{background:#FF5A2A}
.v3 .h-ink{background:#8FE3B0}
.h-vt{position:relative}
.h-row.is-on .h-verb,.h-row:hover .h-verb,.h-row:focus-visible .h-verb{transform:rotate(-2.5deg) translateY(-2px)}
.h-row.is-on .h-tag,.h-row:hover .h-tag,.h-row:focus-visible .h-tag{background:#111;color:#FFF5D9}
.h-row.is-on .h-num,.h-row:hover .h-num{background:#FF5A2A;color:#111}
.h-row:hover .h-tag-s,.h-row:focus-visible .h-tag-s{max-width:260px;opacity:1}
@keyframes ink{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes spin{to{transform:rotate(360deg)}}
.h-foot{align-self:end;padding-top:clamp(22px,2.6vw,34px)}
.h-lede{margin:0;max-width:50ch;font-size:18px;line-height:1.6;color:#2D2B27}
.h-cta{margin-top:22px;display:flex;flex-wrap:wrap;align-items:center;gap:12px 14px}
.h-btn{display:inline-flex;align-items:center;gap:10px;min-height:56px;padding:0 26px;border-radius:999px;font-size:16px;font-weight:700;text-decoration:none}
.h-btn-ink{background:#111;color:#FFF5D9;box-shadow:3px 3px 0 #FF5A2A;transition:transform .2s,box-shadow .2s}
.h-btn-ink:hover{color:#FFF5D9;transform:translate(-2px,-2px);box-shadow:5px 5px 0 #FF5A2A}
.h-btn:hover .arr{transform:translateX(4px)}
.h-hire{flex-basis:100%;margin-top:4px;font-size:14.5px;font-weight:600;color:#45423C;text-decoration:underline;text-underline-offset:4px;text-decoration-color:rgba(17,17,17,.3)}
.h-hire:hover{color:#111;text-decoration-color:#FF5A2A}

/* the sky follows the time of day in Lagos */
.h-hero{background:var(--sky,#FFF5D9);transition:background 1.5s}
.h-sky{position:absolute;inset:0;z-index:-2;pointer-events:none}
.h-sun{position:absolute;left:var(--sx,72%);top:var(--sy,18%);width:clamp(90px,9vw,140px);aspect-ratio:1;border-radius:50%;background:var(--sun,#FFC83D);transform:translate(-50%,-50%);box-shadow:0 0 0 18px color-mix(in srgb,var(--sun,#FFC83D) 22%,transparent),0 0 90px 30px color-mix(in srgb,var(--sun,#FFC83D) 45%,transparent);transition:left 1.5s,top 1.5s,background 1.5s,box-shadow 1.5s}
.h-stars{position:absolute;inset:0;opacity:0;transition:opacity 1.5s;background-image:radial-gradient(circle,#F2EFE8 1.2px,transparent 1.6px),radial-gradient(circle,#F2EFE8 .9px,transparent 1.3px);background-size:140px 120px,90px 70px;background-position:20px 30px,60px 10px}
.h-skyl{display:inline-flex;align-items:center;gap:6px;padding:2px 10px;border-radius:999px;background:rgba(17,17,17,.06);color:inherit;font-weight:600}
.h-skyl:empty{display:none}
.h-hero[data-sky="dawn"]{--sky:linear-gradient(180deg,#FFD9C7 0%,#FFF5D9 70%);--sun:#FF8FB6;--ray:#FF8FB6;--rop:.4}
.h-hero[data-sky="morning"]{--sky:#FFF5D9;--sun:#FFC83D;--ray:#FFC83D;--rop:.5}
.h-hero[data-sky="noon"]{--sky:#FFF8E3;--sun:#FFD54F;--ray:#FFC83D;--rop:.7}
.h-hero[data-sky="golden"]{--sky:linear-gradient(180deg,#FFD7A6 0%,#FFF1D6 75%);--sun:#FF5A2A;--ray:#FF8A3D;--rop:.5}
.h-hero[data-sky="dusk"]{--sky:linear-gradient(180deg,#2E2350 0%,#6B4FA8 60%,#FF8FB6 130%);--sun:#FF8FB6;--ray:#FF8FB6;--rop:.18}
.h-hero[data-sky="night"]{--sky:linear-gradient(180deg,#0B1F22 0%,#0E2A2E 100%);--sun:#F2EFE8;--ray:#8FE3B0;--rop:.1}
.h-hero[data-sky="night"] .h-sun{box-shadow:inset -22px -10px 0 0 #C9C4BA,0 0 60px 10px rgba(242,239,232,.18)}
.h-hero[data-sky="night"] .h-stars,.h-hero[data-sky="dusk"] .h-stars{opacity:.8}
.h-hero[data-sky="dusk"] .h-stars{opacity:.35}
.h-hero[data-sky="dusk"],.h-hero[data-sky="night"]{color:#F2EFE8}
.h-hero[data-sky="dusk"] .h-hello,.h-hero[data-sky="night"] .h-hello,.h-hero[data-sky="dusk"] .h-id,.h-hero[data-sky="night"] .h-id,.h-hero[data-sky="dusk"] .h-lede,.h-hero[data-sky="night"] .h-lede,.h-hero[data-sky="dusk"] .h-hire,.h-hero[data-sky="night"] .h-hire{color:#D9D4CA}
.h-hero[data-sky="dusk"] .h-hello span:first-child,.h-hero[data-sky="night"] .h-hello span:first-child,.h-hero[data-sky="dusk"] .h-id b,.h-hero[data-sky="night"] .h-id b,.h-hero[data-sky="dusk"] .h-mk,.h-hero[data-sky="night"] .h-mk,.h-hero[data-sky="dusk"] .h-row,.h-hero[data-sky="night"] .h-row{color:#F2EFE8}
.h-hero .h-vt,.h-hero .h-tag{color:#111}
.h-hero .h-row.is-on .h-tag,.h-hero .h-row:hover .h-tag{color:#FFF5D9}
.h-hero[data-sky="dusk"] .h-skyl,.h-hero[data-sky="night"] .h-skyl{background:rgba(242,239,232,.12)}
.h-hero[data-sky="dusk"] .h-btn-ink,.h-hero[data-sky="night"] .h-btn-ink{background:#F2EFE8;color:#111}
.h-hero[data-sky="dusk"] .h-ring text,.h-hero[data-sky="night"] .h-ring text{fill:#F2EFE8}
.h-hero[data-sky="dusk"] .h-hire,.h-hero[data-sky="night"] .h-hire{text-decoration-color:rgba(242,239,232,.4)}
@media (prefers-reduced-motion: reduce){.h-sun,.h-hero,.h-rays,.h-stars{transition:none}}
/* portrait stage */
.h-stage{position:relative;align-self:center;aspect-ratio:1/1.08;min-height:420px}
.h-flower{position:absolute;left:8%;top:6%;width:84%;aspect-ratio:1;background:#FF5A2A;animation:spin 60s linear infinite}
.h-photo{position:absolute;left:17%;top:15%;width:66%;aspect-ratio:1;background:#FFFDF6;transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.h-photo img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 22%;transform:scale(1.06)}
.h-stage:hover .h-photo{transform:rotate(-3deg) scale(1.02)}
.h-peeks{position:absolute;left:-24%;top:-3%;width:58%;aspect-ratio:4/3}
.h-peek{position:absolute;inset:0;margin:0;border-radius:12px;background:#fff;box-shadow:0 22px 50px rgba(17,17,17,.22);border:1.5px solid #111;overflow:hidden;opacity:0;transform:translate(30%,18%) rotate(4deg) scale(.86);transition:opacity .45s,transform .7s cubic-bezier(.2,.8,.2,1)}
.h-peek img{display:block;width:100%;height:calc(100% - 30px);object-fit:cover;object-position:center top}
.h-peek figcaption{border-bottom:1.5px solid #111}
.h-peek figcaption{height:30px;display:flex;align-items:center;padding:0 10px;font:600 11.5px/1 'DM Sans',system-ui,sans-serif;background:#111;color:#FFF5D9;white-space:nowrap;overflow:hidden}
.h-peek.is-on{opacity:1;transform:rotate(-7deg)}
.h-ring{position:absolute;right:2%;bottom:15%;width:30%;max-width:132px;aspect-ratio:1;display:grid;place-items:center}
.h-ring svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible;animation:spin 24s linear infinite}
.h-ring text{font:700 8.6px 'Space Grotesk',system-ui,sans-serif;fill:#111;letter-spacing:.06em}
.h-ring span{display:grid;place-items:center;width:64%;aspect-ratio:1;border-radius:50%;background:#111;color:#FFC83D;font-size:13px;font-weight:700;line-height:1.05;text-align:center;letter-spacing:-.01em}
.h-bub{position:absolute;left:-2%;bottom:0;max-width:300px;display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:14px 16px;border:1.5px solid #111;border-radius:18px 18px 18px 4px;background:#FFFDF6;box-shadow:4px 4px 0 #111;color:#111;font:500 15px/1.4 'DM Sans',system-ui,sans-serif;text-align:left;cursor:pointer;transition:transform .2s,box-shadow .2s}
.h-bub:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 #111}
.h-bub-more{font-size:12.5px;font-weight:700;color:#C23A0E}
.h-bub.pop .h-bub-t{animation:pop .4s cubic-bezier(.2,.8,.2,1)}
@keyframes pop{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.js-rv .h-stage>*{animation-fill-mode:both}
.h-photo{animation:grow .9s .1s cubic-bezier(.2,.8,.2,1) both}
@keyframes grow{from{opacity:0;transform:scale(.8) rotate(-8deg)}to{opacity:1;transform:none}}
/* ---------- the sheet (logos + work) rises over the hero ---------- */
.h-stick{position:sticky;top:0;z-index:0;min-height:100vh;box-sizing:border-box}
.h-stick::after{content:"";position:absolute;inset:0;z-index:5;background:#111;opacity:calc(var(--hp,0) * .55);pointer-events:none}
.sheet{position:relative;z-index:2;background:#111;color:#F2EFE8;border-radius:clamp(24px,3.4vw,48px) clamp(24px,3.4vw,48px) 0 0;margin-top:-34px;transform-origin:50% 0}
.lg-band{padding:clamp(40px,5vw,64px) 0 8px}
.lg-band .eyebrow{color:#8A867E;margin-bottom:12px}
.lt-wrap{overflow:hidden}
.logo-track{margin:0;padding:0;list-style:none;display:flex;align-items:center;gap:14px;width:max-content;animation:logos 50s linear infinite}
.lt-wrap:hover .logo-track{animation-play-state:paused}
.logo-track li{flex:none;display:flex;align-items:center;justify-content:center;height:84px;padding:0 30px;border-radius:18px;background:#F2EFE8}
.logo-track li:nth-child(3n+2){background:#FFF5D9}.logo-track li:nth-child(3n){background:#FFFFFF}
.logo-i{max-height:40px}
@keyframes logos{to{transform:translateX(calc(-50% - 7px))}}
.sw{padding:clamp(64px,8vw,112px) 0 clamp(80px,10vw,140px)}
.sw .eyebrow{color:#8A867E}
.sw-head{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:12px 48px;align-items:end;margin-bottom:clamp(40px,5vw,64px)}
.sw-head .eyebrow{grid-column:1/-1}
.sw-title{margin:0;font-weight:700;font-size:clamp(44px,6vw,96px);line-height:.94;letter-spacing:-.055em;max-width:13ch}
.sw-title em{font-style:normal;color:#111;background:#FF5A2A;padding:0 .1em;border-radius:.12em;display:inline-block;transform:rotate(-2deg)}
.sw-sum{margin:0;font-size:17px;line-height:1.6;color:#B5B0A6;max-width:40ch}
.sw-sum b{color:#F2EFE8}
.sw-all{margin:clamp(40px,5vw,64px) 0 0;text-align:center}
/* project cards */
.pc{position:relative;border-radius:clamp(20px,2.4vw,32px);padding:clamp(24px,3.4vw,52px);margin-top:clamp(18px,2vw,28px);overflow:hidden}
.pc-meta{margin:0 0 16px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;font-size:13.5px;font-weight:600}
.pc-n{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:currentColor;font-size:13px}
.pc-n{color:inherit}
.pc-n{background:none;border:1.5px solid currentColor}
.pc-disc{padding:4px 10px;border-radius:999px;border:1.5px solid currentColor;font-size:12.5px}
.pc-title{margin:0;font-weight:700;font-size:clamp(30px,3.4vw,52px);line-height:1.02;letter-spacing:-.045em;max-width:18ch}
.pc-go{color:inherit;text-decoration:none}
.pc-go::after{content:"";position:absolute;inset:0;z-index:1}
.pc-go:focus-visible{outline:none}.pc:has(.pc-go:focus-visible){outline:3px solid #FF5A2A;outline-offset:4px}
.pc-dl{margin:22px 0 0;display:grid;gap:14px;max-width:62ch}
.pc-dl dt{font:700 11.5px/1.4 'DM Sans',system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;opacity:.7}
.pc-dl dd{margin:3px 0 0;font-size:16px;line-height:1.55}
.pc-res dd{font:600 19px/1.35 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.015em}
.pc-links{position:relative;z-index:2;margin:20px 0 0;display:flex;flex-wrap:wrap;gap:10px}
.pc-ext{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 16px;border-radius:999px;border:1.5px solid currentColor;color:inherit;font-weight:700;font-size:14.5px;text-decoration:none;transition:background .25s,color .25s}
.pc-ext:hover{background:#111;color:#FFC83D;border-color:#111}
.pc-media{position:relative}
.pc-media img{display:block;border-radius:12px;box-shadow:0 24px 50px rgba(0,0,0,.28);transition:transform .7s cubic-bezier(.2,.8,.2,1)}
.pc-big{margin:18px 0 0;display:flex;align-items:baseline;flex-wrap:wrap;gap:6px 14px;font-size:16px;font-weight:600;max-width:40ch}
.pc-big .sg{font-size:clamp(64px,7vw,112px);font-weight:700;line-height:.85;letter-spacing:-.065em}
.view-pill{position:fixed;left:0;top:0;z-index:60;pointer-events:none;padding:10px 16px;border-radius:999px;background:#FF5A2A;color:#111;font:700 14px/1 'DM Sans',system-ui,sans-serif;opacity:0;transform:translate(-50%,-50%) scale(.6);transition:opacity .2s,transform .2s;white-space:nowrap}
.view-pill.on{opacity:1;transform:translate(-50%,-50%) scale(1)}
/* 01 Stears: tabs */
.pc-stears{background:#0E2A2E;color:#EAF6F1}
.st-head{display:flex;flex-direction:column}
.st-title{font-size:clamp(36px,4.8vw,76px);max-width:16ch}
.st-body{margin-top:clamp(28px,3.4vw,44px);display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(28px,4vw,64px);align-items:start}
.st-tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}
.st-tabs button{min-height:44px;padding:0 18px;border-radius:999px;border:1.5px solid rgba(234,246,241,.35);background:none;color:#EAF6F1;font:700 14.5px 'DM Sans',system-ui,sans-serif;cursor:pointer;transition:background .25s,color .25s,border-color .25s}
.st-tabs button:hover{border-color:#8FE3B0}
.st-tabs button[aria-selected="true"]{background:#8FE3B0;border-color:#8FE3B0;color:#0E2A2E}
.st-panel{min-height:230px}
.st-panel p,.st-steps li{margin:0;font-size:18px;line-height:1.62;color:#CFE3DC;max-width:56ch}
.st-panel .st-role{margin-top:14px;font-size:15px;color:#8FBFB0}
.st-panel:not([hidden]){animation:pop .45s cubic-bezier(.2,.8,.2,1)}
.st-steps{margin:0;padding:0;list-style:none;counter-reset:s;display:grid;gap:14px}
.st-steps li{counter-increment:s;display:grid;grid-template-columns:38px 1fr}
.st-steps li::before{content:counter(s,decimal-leading-zero);font:700 14px/1.9 'Space Grotesk',system-ui,sans-serif;color:#8FE3B0}
.st-results{display:grid;gap:18px}
.st-results p{display:flex;flex-direction:column;gap:6px;font-size:15.5px !important}
.st-big{font-size:clamp(56px,6vw,92px);font-weight:700;line-height:.86;letter-spacing:-.06em;color:#EAF6F1}
.st-hot{color:#FFC83D}
.st-next{margin:22px 0 0}
.st-stage{position:relative;aspect-ratio:16/11;border-radius:18px;background:#123A3F;overflow:hidden}
.st-v{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.97);transition:opacity .5s,transform .7s cubic-bezier(.2,.8,.2,1);pointer-events:none}
.st-v.is-on{opacity:1;transform:none}
.st-v[data-v="0"] img{width:92%;border-radius:10px;box-shadow:0 24px 50px rgba(0,0,0,.4)}
.st-chip{position:absolute;left:16px;bottom:14px;padding:6px 12px;border-radius:999px;background:#0E2A2E;color:#CFE3DC;font-size:12.5px;font-weight:600}
.st-v[data-v="1"]{flex-direction:column;gap:18px;padding:28px}
.st-dots{position:relative;width:100%;flex:1;border-radius:10px;background:radial-gradient(circle,rgba(207,227,220,.22) 3px,transparent 3.5px) 0 0/18px 18px}
.st-dots-on{position:absolute;inset:0;background:radial-gradient(circle,#8FE3B0 3px,transparent 3.5px) 0 0/18px 18px;clip-path:inset(0 100% 0 0)}
.st-v.is-on .st-dots-on{animation:fill 2.2s .2s cubic-bezier(.5,0,.2,1) forwards}
@keyframes fill{to{clip-path:inset(0 0 0 0)}}
.st-dots-n{margin:0;font-size:15px;color:#CFE3DC;align-self:flex-start}
.st-dots-n b{display:block;font-size:40px;line-height:1;letter-spacing:-.04em;color:#8FE3B0}
.st-serp{position:absolute;right:6%;top:8%;width:52%;border-radius:10px;box-shadow:0 24px 50px rgba(0,0,0,.45)}
.st-rank{position:absolute;left:7%;top:50%;transform:translateY(-50%);margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px;width:36%}
.st-rank li{padding:12px 14px;border-radius:12px;background:#1B4A50;color:#CFE3DC;font-weight:600;font-size:15px;transition:transform .9s cubic-bezier(.2,.8,.2,1)}
.st-rank .st-me{order:-1;background:#FFC83D;color:#111;font-family:'Space Grotesk',system-ui,sans-serif;font-size:17px}
.st-v.is-on .st-rank .st-me{animation:climb 1.1s .25s cubic-bezier(.2,.8,.2,1) both}
@keyframes climb{from{transform:translateY(calc(300% + 30px))}to{transform:none}}
.st-v.is-on .st-rank li:not(.st-me){animation:drop 1.1s .25s cubic-bezier(.2,.8,.2,1) both}
@keyframes drop{from{transform:translateY(calc(-100% - 10px))}to{transform:none}}
/* paired cards */
.pc-pair{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(18px,2vw,28px);margin-top:clamp(18px,2vw,28px)}
.pc-pair .pc{margin-top:0}
.pc-certn{background:#FF5A2A;color:#111;display:flex;flex-direction:column;gap:28px}
.cn-media{height:clamp(240px,24vw,340px)}
.cn-media img{position:absolute;width:48%;aspect-ratio:4/3;object-fit:cover;border:1.5px solid #111}
.cn-a{left:0;top:10%;transform:rotate(-6deg)}
.cn-b{left:26%;top:0;transform:rotate(2deg);z-index:1}
.cn-c{right:0;top:14%;transform:rotate(7deg)}
.pc-certn:hover .cn-a{transform:rotate(-10deg) translate(-12px,8px)}
.pc-certn:hover .cn-b{transform:rotate(0) translateY(-10px) scale(1.04)}
.pc-certn:hover .cn-c{transform:rotate(11deg) translate(12px,8px)}
.cn-press{position:absolute;left:4%;bottom:0;z-index:2;margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:8px}
.cn-press li{padding:8px 14px;border-radius:999px;background:#111;color:#FFF5D9;font:700 13.5px 'DM Sans',system-ui,sans-serif;box-shadow:3px 3px 0 #FFC83D}
.cn-press li:nth-child(2){transform:rotate(-4deg)}.cn-press li:nth-child(3){transform:rotate(3deg)}
.pc-askai{background:#FFC83D;color:#111;display:flex;flex-direction:column;gap:28px}
.pc-askai .pc-title{font-size:clamp(30px,2.9vw,44px)}
.ai-media{margin:0 calc(clamp(24px,3.4vw,52px) * -1) calc(clamp(24px,3.4vw,52px) * -1) 0}
.ai-media img{width:100%;border-radius:12px 0 0 0;border:1.5px solid #111;border-right:0;border-bottom:0;box-shadow:none}
.ai-q{position:absolute;left:-10px;top:-22px;z-index:2;padding:10px 14px;border-radius:16px 16px 16px 4px;background:#111;color:#FFF5D9;font:600 14px/1.3 'DM Sans',system-ui,sans-serif;transform:rotate(-3deg);box-shadow:3px 3px 0 #FF5A2A}
.pc-askai:hover .ai-media img{transform:translate(-8px,-8px)}
/* Xofu: type-led */
.pc-xofu{background:#FFF5D9;color:#111}
.xf-top{display:flex;flex-direction:column}
.xf-quote{margin:4px 0 0;font-size:clamp(56px,9vw,148px);font-weight:700;line-height:.9;letter-spacing:-.06em}
.xf-quote span{color:#C23A0E;text-decoration:underline;text-decoration-thickness:.07em;text-underline-offset:.1em;text-decoration-color:#FFC83D}
.xf-sub{margin:14px 0 0;font-size:17px;color:#45423C}
.xf-grid{margin-top:clamp(28px,3.4vw,48px);display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(28px,4vw,64px);align-items:center}
.xf-media{height:clamp(300px,30vw,440px)}
.xf-media img{position:absolute;background:#fff;border:1.5px solid #111}
.xf-a{left:0;top:0;width:76%;z-index:1}
.xf-b{right:0;top:18%;width:46%;transform:rotate(4deg)}
.xf-c{left:30%;bottom:0;width:36%;transform:rotate(-5deg);z-index:2}
.pc-xofu:hover .xf-a{transform:translateY(-8px)}
.pc-xofu:hover .xf-b{transform:rotate(7deg) translateX(10px)}
.pc-xofu:hover .xf-c{transform:rotate(-8deg) translateY(8px)}
/* Engine */
.pc-engine{background:#8FE3B0;color:#0E2A2E;display:grid;grid-template-columns:minmax(0,6fr) minmax(0,6fr);gap:clamp(28px,4vw,64px);align-items:center}
.en-stats{margin:20px 0 0;display:flex;flex-wrap:wrap;gap:12px 36px}
.en-stats p{margin:0;display:flex;flex-direction:column;font-size:14.5px;font-weight:600;max-width:20ch}
.en-stats .sg{font-size:clamp(52px,5.2vw,84px);font-weight:700;line-height:.9;letter-spacing:-.06em}
.en-media{height:clamp(320px,32vw,460px)}
.en-media img{position:absolute;border:1.5px solid #0E2A2E}
.en-a{left:0;top:0;width:78%;z-index:1}
.en-b{right:0;bottom:6%;width:62%;transform:rotate(3deg)}
.en-c{left:6%;bottom:0;width:30%;transform:rotate(-6deg);z-index:2}
.pc-engine:hover .en-a{transform:translate(-6px,-8px)}
.pc-engine:hover .en-b{transform:rotate(5deg) translate(8px,6px)}
.pc-engine:hover .en-c{transform:rotate(-9deg) translateY(-6px)}
/* ---------- quotes ---------- */
.qs{background:#F2EFE8;color:#111;padding:clamp(80px,10vw,140px) 0}
.qs-title{margin:0;max-width:20ch;font-weight:700;font-size:clamp(34px,4vw,60px);line-height:1;letter-spacing:-.045em}
.qt-row{margin-top:clamp(36px,4.4vw,56px);display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;align-items:start}
.qt{margin:0;padding:26px 24px 22px;border:1.5px solid #111;border-radius:22px;box-shadow:5px 5px 0 #111;transition:transform .45s cubic-bezier(.2,.8,.2,1)}
.qt:nth-child(odd){transform:rotate(-1.6deg)}.qt:nth-child(even){transform:rotate(1.4deg) translateY(28px)}
.qt:hover{transform:rotate(0) translateY(-6px)}
.qt blockquote{margin:0;font-size:clamp(20px,1.7vw,24px);font-weight:600;line-height:1.24;letter-spacing:-.02em}
.qt figcaption{margin-top:18px;font-size:14px;color:#2D2B27}
.q-sun{background:#FFC83D}.q-mint{background:#8FE3B0}.q-blush{background:#FF8FB6}.q-paper{background:#FFFDF6}
/* ---------- disciplines ---------- */
.xs{background:#0E2A2E;color:#EAF6F1;padding:clamp(80px,10vw,140px) 0}
.xs-head{display:grid;grid-template-columns:minmax(0,8fr) minmax(0,4fr);gap:24px 48px;align-items:end}
.xs-title{margin:0;font-weight:700;font-size:clamp(36px,4.4vw,68px);line-height:1;letter-spacing:-.05em;max-width:18ch}
.xs-sub{margin:0;font-size:16px;line-height:1.6;color:#A9C6BE}
.xd-grid{margin-top:clamp(40px,5vw,64px);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.xd{display:flex;flex-direction:column;gap:10px;padding:clamp(24px,2.4vw,34px);border-radius:24px;color:#111;text-decoration:none;transition:transform .4s cubic-bezier(.2,.8,.2,1)}
.xd:hover{transform:translateY(-8px) rotate(-.6deg);color:#111}
.d-clear{background:#FFC83D}.d-land{background:#FF5A2A}.d-travel{background:#8FE3B0}
.xd-badge{position:relative;width:76px;height:76px;margin-bottom:18px;display:grid;place-items:center}
.xd-shp{position:absolute;inset:0}
.d-clear .xd-shp{background:#8FE3B0}.d-land .xd-shp{background:#FFC83D}.d-travel .xd-shp{background:#1FA463}
.xd-emo{position:relative;font-size:32px;line-height:1}
.xd:hover .xd-shp{animation:spin 6s linear infinite}
.d-clear:hover .xd-emo{animation:seek 1.4s ease-in-out infinite}
.d-land:hover .xd-emo{animation:lift 1.2s cubic-bezier(.5,0,.2,1) infinite}
.d-travel:hover .xd-emo{animation:fly 1.6s cubic-bezier(.5,0,.5,1) infinite}
@keyframes seek{0%,100%{transform:translate(0,0)}25%{transform:translate(5px,-4px)}50%{transform:translate(-4px,-6px)}75%{transform:translate(-5px,3px)}}
@keyframes lift{0%{transform:none}45%{transform:translate(18px,-28px) scale(.85);opacity:1}46%{opacity:0}55%{transform:translate(-12px,18px);opacity:0}100%{transform:none;opacity:1}}
@keyframes fly{0%{transform:none}45%{transform:translateX(52px);opacity:1}46%{opacity:0}55%{transform:translateX(-52px);opacity:0}100%{transform:none;opacity:1}}
.xd-verb{font-size:clamp(52px,5vw,80px);font-weight:700;line-height:.86;letter-spacing:-.06em}
.xd-verb i{font-style:normal;color:#FFFDF6}
.d-clear .xd-verb i,.d-travel .xd-verb i{color:#FF5A2A}
.xd-name{font-size:21px;font-weight:700;letter-spacing:-.02em}
.xd-long{font-size:16px;line-height:1.55;max-width:36ch}
.xd-proof{font-size:14px;line-height:1.5}
.xd-go{margin-top:auto;padding-top:14px;align-self:flex-start;display:inline-flex;gap:8px;align-items:center;min-height:46px;padding:0 18px;border-radius:999px;background:#111;color:#FFFDF6;font-weight:700;font-size:15px}
.xd:hover .arr{transform:translateX(4px)}
/* ---------- research ---------- */
.rs{background:#FFF5D9;color:#111;padding:clamp(80px,10vw,140px) 0;overflow-x:clip}
.rs-grid{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(40px,6vw,96px);align-items:start}
.rs-fan{margin:0;position:sticky;top:110px}
.rs-fan a{position:relative;display:block;max-width:420px;aspect-ratio:1000/1414}
.rs-fan img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:6px;box-shadow:0 30px 60px rgba(17,17,17,.22);transition:transform .9s cubic-bezier(.2,.8,.2,1)}
.rs-back{background:#fff}
.rs-fan.in .rs-back{transform:rotate(8deg) translate(16%,4%)}
.rs-fan.in .rs-front{transform:rotate(-3deg)}
.rs-fan a:hover .rs-back{transform:rotate(12deg) translate(24%,2%)}
.rs-fan a:hover .rs-front{transform:rotate(-5deg) translate(-4%,-2%)}
.rs-sticker{position:absolute;right:-8%;top:-5%;z-index:2;display:grid;place-items:center;width:104px;height:104px;border-radius:50%;background:#1FA463;color:#FFFDF6;font-size:15px;font-weight:700;line-height:1.05;text-align:center;transform:rotate(12deg)}
.rs-fan figcaption{margin-top:22px;display:flex;flex-direction:column;gap:2px;font-size:14px;color:#6B675F}
.rs-fan figcaption b{color:#111;font-size:16px}
.rs-title{margin:0 0 28px;font-weight:700;font-size:clamp(38px,4.4vw,68px);line-height:.98;letter-spacing:-.05em;max-width:14ch}
.rs-title span{color:#1FA463}
.rs-list{margin:0 0 28px;padding:0;list-style:none;border-top:2px solid #111}
.rs-row{display:grid;grid-template-columns:150px minmax(0,1fr);gap:4px 24px;padding:18px 0;border-bottom:1px solid #E3D6B0;color:#111;text-decoration:none;transition:padding .3s cubic-bezier(.2,.8,.2,1)}
.rs-outlet{grid-row:span 2;font-size:13px;font-weight:700;color:#6B675F}
.rs-t{font:700 20px/1.25 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em}
.rs-note{font-size:15px;line-height:1.55;color:#45423C;max-width:60ch}
.rs-row:hover{padding-left:10px}
.rs-row:hover .rs-t{color:#C23A0E}
/* ---------- about ---------- */
.ab{background:#F2EFE8;color:#111;padding:clamp(80px,10vw,140px) 0 clamp(64px,8vw,104px)}
.ab-grid{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(40px,6vw,96px);align-items:center}
.ab-copy p{max-width:58ch;font-size:18px;line-height:1.65;color:#2D2B27}
.ab-title{margin:0 0 18px;font-weight:700;font-size:clamp(44px,5.6vw,88px);line-height:1;letter-spacing:-.055em;max-width:12ch}
.ab-strike{position:relative;display:inline-block}
.ab-strike i{position:absolute;left:-3%;right:-3%;top:54%;height:.1em;background:#FF5A2A;border-radius:99px;transform:scaleX(0) rotate(-4deg);transform-origin:left;transition:transform .7s .2s cubic-bezier(.7,0,.2,1)}
.ab-ins{display:inline-block;margin-left:.18em;padding:0 .1em;background:#FFC83D;border-radius:.12em;transform:rotate(-3deg) scale(.4);opacity:0;transition:transform .55s 1s cubic-bezier(.3,1.6,.5,1),opacity .3s 1s}
.ab-title.in .ab-strike i{transform:scaleX(1) rotate(-4deg)}
.ab-title.in .ab-strike{color:#8A867E}
.ab-title.in .ab-ins{transform:rotate(-3deg);opacity:1}
.ab-photo{position:relative;margin:0}
.ab-photo img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:center 20%;border-radius:200px 200px 24px 24px}
.ab-stk{position:absolute;left:-18px;top:28%;display:grid;place-items:center;width:76px;height:76px;border-radius:50%;background:#FF5A2A;font-size:34px;transform:rotate(-10deg);box-shadow:4px 4px 0 #111}
.ab-photo figcaption{margin-top:12px;font-size:13.5px;color:#6B675F}
.tl{margin-top:clamp(64px,8vw,104px)}
.tl-track{position:relative;height:4px;border-radius:4px;background:#DDD6C8;margin:26px 0 0}
.tl-fill{position:absolute;inset:0;border-radius:4px;background:#111;transform-origin:left;transform:scaleX(var(--p,1))}
.tl-plane{position:absolute;top:50%;left:calc(var(--p,1) * 100%);font-size:28px;line-height:1;transform:translate(-50%,-56%) rotate(45deg)}
.tl-list{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(8,minmax(0,1fr))}
.tl-i{position:relative;padding:28px 16px 0 0}
.tl-i::before{content:"";position:absolute;left:0;top:-12px;width:16px;height:16px;border-radius:50%;background:var(--dot,#111);border:3px solid #F2EFE8;box-shadow:0 0 0 1.5px #111;transform:scale(.6);transition:transform .4s cubic-bezier(.3,1.6,.5,1)}
.tl-i.on::before,.tl:not([data-live]) .tl-i::before{transform:none}
.tl-y{display:block;font-size:26px;font-weight:700;letter-spacing:-.04em}
.tl-w{display:block;margin-top:6px;font-size:14px;line-height:1.45;color:#45423C}
/* ---------- EmpowerQ ---------- */
.eq{position:relative;overflow:hidden;background:#B9A6FF;color:#1C1430;padding:clamp(80px,10vw,140px) 0}
.eq-s1{position:absolute;right:-60px;top:-60px;width:220px;height:220px;background:#FFC83D;animation:spin 50s linear infinite}
.eq-s2{position:absolute;left:42%;bottom:-50px;width:120px;height:120px;background:#FF8FB6;animation:spin 40s linear infinite reverse}
.eq-grid{position:relative;display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(40px,6vw,96px);align-items:center}
.eq-top{margin:0 0 18px;display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px}
.eq-top .eyebrow{margin:0}
.eq-eyebrow{color:#3B2C6E}
.eq-pill{padding:6px 12px;border-radius:999px;background:#1C1430;color:#E9E2FF;font-size:12.5px;font-weight:700}
.eq-title{margin:0;font-weight:700;font-size:clamp(72px,10vw,160px);line-height:.82;letter-spacing:-.07em}
.eq-lede{margin:22px 0 0;max-width:24ch;font-size:clamp(24px,2.3vw,34px);font-weight:600;line-height:1.12;letter-spacing:-.025em}
.eq-copy>p:not(.eq-lede):not(.eq-top){max-width:58ch;font-size:17px;line-height:1.65;color:#2E2350}
.eq-list{margin:28px 0 0;padding:0;list-style:none;border-top:2px solid #1C1430}
.eq-list li{display:grid;grid-template-columns:210px minmax(0,1fr);gap:4px 20px;padding:14px 0;border-bottom:1px solid rgba(28,20,48,.22);font-size:15px;line-height:1.5}
.eq-list b{font-family:'Space Grotesk',system-ui,sans-serif;font-size:18px;letter-spacing:-.015em}
.eq-cta{margin-top:30px;display:flex;flex-wrap:wrap;align-items:center;gap:14px 28px}
.eq-btn{display:inline-flex;align-items:center;gap:8px;min-height:54px;padding:0 24px;border-radius:999px;background:#1C1430;color:#F1ECFF;font-weight:700;text-decoration:none;box-shadow:3px 3px 0 #FFC83D;transition:transform .2s,box-shadow .2s}
.eq-btn:hover{color:#F1ECFF;transform:translate(-2px,-2px);box-shadow:5px 5px 0 #FFC83D}
.eq-link{color:#1C1430;font-weight:700;text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:2px}
.eq-photo{position:relative;margin:0}
.eq-photo img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:58% center;border-radius:24px 200px 24px 24px}
.eq-badge{position:absolute;left:-28px;bottom:48px;display:flex;flex-direction:column;align-items:center;justify-content:center;width:148px;height:148px;border-radius:50%;background:#1C1430;color:#E9E2FF;font-size:13px;font-weight:600;text-align:center;line-height:1.2;padding:16px;box-sizing:border-box;transform:rotate(-8deg)}
.eq-badge b{font-size:44px;letter-spacing:-.05em;line-height:1}
.eq-photo figcaption{margin-top:12px;font-size:13.5px;line-height:1.5;color:#2E2350}
/* ---------- contact ---------- */
.ct{background:#F2EFE8;color:#111;padding:clamp(80px,10vw,140px) 0 clamp(36px,4vw,56px)}
.ct-title{margin:0;font-weight:700;font-size:clamp(52px,8vw,128px);line-height:.9;letter-spacing:-.065em;max-width:10ch}
.ct-grid{margin-top:clamp(36px,4.4vw,56px);display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(28px,4vw,56px);align-items:start}
.ct-doors{display:flex;flex-direction:column;gap:10px}
.ct-door{display:grid;grid-template-columns:44px minmax(0,1fr) auto;align-items:center;gap:16px;min-height:72px;padding:12px 18px 12px 12px;border:1.5px solid #C9C3B6;border-radius:18px;background:#FFFDF6;color:#111;font:inherit;text-align:left;cursor:pointer;transition:border-color .25s,background .25s,color .25s,transform .25s}
.ct-door:hover{border-color:#111;background:#FFF5D9}
.ct-door[aria-checked="true"]{background:#111;border-color:#111;color:#F2EFE8}
.ct-ic{display:grid;place-items:center;width:44px;height:44px;border-radius:12px;font-size:22px}
.ct-door:nth-child(1) .ct-ic{background:#FFC83D}.ct-door:nth-child(2) .ct-ic{background:#FF5A2A}.ct-door:nth-child(3) .ct-ic{background:#8FE3B0}.ct-door:nth-child(4) .ct-ic{background:#B9A6FF}.ct-door:nth-child(5) .ct-ic{background:#FF8FB6}
.ct-label{font-size:clamp(19px,1.7vw,24px);font-weight:700;letter-spacing:-.02em}
.ct-who{font-size:13px;font-weight:600;color:#6B675F;white-space:nowrap}
.ct-door[aria-checked="true"] .ct-who{color:#B5B0A6}
.ct-panel{position:sticky;top:110px;padding:clamp(26px,3vw,40px);border-radius:24px;background:#111;color:#F2EFE8;display:flex;flex-direction:column;gap:16px}
.ct-p-who{margin:0;font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:#8A867E}
.ct-p-title{margin:0;font-size:clamp(26px,2.4vw,36px);font-weight:700;line-height:1.08;letter-spacing:-.035em}
.ct-p-body{margin:0;font-size:16px;line-height:1.6;color:#C9C4BA}
.ct-p-cta{align-self:flex-start;display:inline-flex;align-items:center;min-height:52px;padding:0 24px;border-radius:999px;font-weight:700}
.ct-p-mail{margin:6px 0 0;padding-top:16px;border-top:1px solid #2E2D2A;font-size:14px;color:#B5B0A6}
.ct-p-mail a{color:#F2EFE8;font-weight:700;text-underline-offset:4px}
.ct-foot{margin-top:clamp(64px,9vw,120px);padding-top:22px;border-top:1.5px solid #111;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px;font-size:14px;color:#6B675F}
.ct-brand{display:inline-flex;align-items:center;gap:10px;font-size:18px;font-weight:700;letter-spacing:-.04em;color:#111}
.ct-mark{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:8px;background:#FF5A2A;color:#111;font-size:14px}
.ct-nav{display:flex;flex-wrap:wrap;gap:8px 22px}
.ct-nav a{color:#2D2B27;text-decoration:none}
.ct-nav a:hover{color:#C23A0E}
/* image reveal */
.js-rv .img-rv{clip-path:inset(8% 0 0 0);opacity:0;transform:translateY(18px);transition:clip-path 1s cubic-bezier(.2,.8,.2,1),opacity .8s,transform 1s cubic-bezier(.2,.8,.2,1)}
.js-rv .img-rv.in{clip-path:inset(0 0 0 0);opacity:1;transform:none}
/* ---------- responsive ---------- */
@media (max-width: 1080px){
.h-grid{grid-template-columns:1fr;grid-template-areas:"copy" "stage" "foot"}
.h-stage{width:min(100%,520px);margin:28px auto 0;min-height:0}
.sw-head,.st-body,.pc-pair,.xf-grid,.pc-engine,.xs-head,.rs-grid,.ab-grid,.eq-grid,.ct-grid{grid-template-columns:1fr}
.qt-row{grid-template-columns:repeat(2,minmax(0,1fr))}
.xd-grid{grid-template-columns:1fr}
.rs-fan{position:static;max-width:320px}
.tl-list{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:28px}
.tl-track{display:none}
.tl-i{padding-top:20px;border-top:2px solid #111}
.tl-i::before{top:-9px}
.ct-panel{position:static}
.pc-engine .en-media{order:-1}
}
@media (max-width: 640px){
.h-display{font-size:clamp(46px,14vw,68px)}
.h-row:nth-child(2),.h-row:nth-child(3){padding-left:0}
.h-tag-s{display:none}
.h-peeks{left:-4%;top:-2%;width:56%}
.h-bub{position:relative;left:auto;bottom:auto;margin:-6px 0 0 0;max-width:none}
.h-stage{aspect-ratio:auto;display:flex;flex-direction:column}
.h-stage::before{content:"";display:block;aspect-ratio:1/1.02}
.h-lede,.st-panel p,.st-steps li,.ab-copy p{font-size:17px}
.h-btn{flex:1 1 auto;justify-content:center}
.pc{padding:22px 20px 26px}
.st-stage{aspect-ratio:4/3.4}
.st-rank{width:44%;gap:6px}.st-rank li{padding:8px 10px;font-size:13px}.st-rank .st-me{font-size:14px}
.st-serp{width:50%}
.cn-media{height:220px}
.ai-media{margin:0 -20px -26px 0}
.xf-media{height:260px}.en-media{height:280px}
.qt-row{grid-template-columns:1fr}
.qt:nth-child(even){transform:rotate(1.2deg)}
.rs-row{grid-template-columns:1fr}.rs-outlet{grid-row:auto}
.eq-list li{grid-template-columns:1fr}
.eq-badge{left:-8px;width:120px;height:120px}.eq-badge b{font-size:36px}
.ct-door{grid-template-columns:40px minmax(0,1fr)}.ct-who{grid-column:2}
.ab-stk{left:-6px}
.rs-sticker{right:-4%;width:88px;height:88px;font-size:13px}
}
@media (prefers-reduced-motion: reduce){
.h-rays,.h-flower,.h-ring svg,.eq-s1,.eq-s2,.logo-track,.h-ink,.h-photo{animation:none !important}
.xd:hover .xd-shp,.xd:hover .xd-emo{animation:none !important}
.st-v.is-on .st-dots-on{animation:none;clip-path:none}
.st-v.is-on .st-rank li{animation:none !important}
.h-peek,.pc-media img,.rs-fan img,.ab-strike i,.ab-ins,.st-v{transition:none !important}
.js-rv .img-rv{clip-path:none;opacity:1;transform:none;transition:none}
.logo-track{flex-wrap:wrap;justify-content:center;width:auto}.logo-track li[aria-hidden="true"]{display:none}
}
/*home:end*/
'''


def main():
    s = HOME.read_text()
    a = s.index('<section id="top"')
    b = s.index('\n\n</div>\n</x-dc>')
    body = '\n\n'.join([hero(), work(), quotes(), expertise(), research(), about(), empowerq(), contact()])
    s = s[:a] + body + s[b:]
    s = re.sub(r'\n?/\*hero:start\*/.*?/\*hero:end\*/\n?', '\n', s, flags=re.S)
    s = re.sub(r'\n?/\*home:start\*/.*?/\*home:end\*/\n?', '\n', s, flags=re.S)
    s = s.replace('</style>\n</helmet>', CSS.strip('\n') + '\n</style>\n</helmet>', 1)
    s = s.replace('class="grid-bg hero-anim"', '')
    facts_js = json.dumps(FACTS, ensure_ascii=False)
    s = s.replace("this.state = { time: this.lagosTime(), door: 0 };", "this.state = { time: this.lagosTime(), door: 0, fact: 0 };")
    if 'const FACTS =' not in s:
        s = s.replace("    return {\n      time: this.state.time,", "    const FACTS = " + facts_js + ";\n    return {\n      time: this.state.time,\n      fact: FACTS[this.state.fact % FACTS.length],\n      nextFact: () => this.setState({ fact: (this.state.fact + 1) % FACTS.length }),", 1)
    # clip (not hidden) so the sticky header and the hero curtain can stick
    s = s.replace('box-sizing: border-box; overflow-x: hidden">', 'box-sizing: border-box; overflow-x: clip">', 1)
    HOME.write_text(s)
    print('home written', len(s))


if __name__ == '__main__':
    main()
