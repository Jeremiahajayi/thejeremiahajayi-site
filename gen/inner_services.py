"""Expertise pages (overview + three services) in the homepage's language."""
from kit import mark, ARR, CAL, motif

B = lambda i: '/_blob/' + i

# ---------- per-service pieces ----------
HERO = {
    'svc-positioning': dict(motif='target', bg='k-sun', rays='#FFFDF6', verb='clear', ink='#111', vt='#FFC83D', cta='Book a call',
        side='''<figure class="k-fig sv-ladder" aria-label="The five questions a positioning framework answers">
<ol>
<li><b>Who it’s for</b><span>01</span></li>
<li><b>The problem they feel</b><span>02</span></li>
<li><b>What they’d use instead</b><span>03</span></li>
<li><b>Why you, and why now</b><span>04</span></li>
<li><b>The proof that makes it believable</b><span>05</span></li>
</ol>
<figcaption>The five questions every positioning answers before a word of copy is written.</figcaption>
</figure>'''),
    'svc-launch': dict(motif='flight', bg='k-orange', rays='#FFC83D', verb='land', ink='#111', vt='#FF5A2A', cta='Plan my launch',
        side='''<figure class="k-fig sv-count" aria-label="A launch, from six weeks out to thirty days after">
<figcaption class="sv-count-h">The countdown I run</figcaption>
<ol>
<li><b>6 weeks out</b><span>GTM brief, launch tier and success measures, agreed with product and sales.</span></li>
<li><b>4 weeks out</b><span>Messaging, press and partner story, and the sales enablement kit.</span></li>
<li class="is-day"><b>Launch day</b><span>Announcement, website, email, social, press and partners, on the same day.</span></li>
<li><b>30 days after</b><span>Pipeline, sales usage and adoption, reported with lessons for the next launch.</span></li>
</ol>
</figure>'''),
    'svc-content': dict(motif='ripple', bg='k-night', rays='#8FE3B0', verb='{{svc.verb}}', ink='#8FE3B0', vt='#0E2A2E', cta='Book a call',
        side=f'''<figure class="k-fig sv-serp"><img class="k-shot" src="{B('97c7a07c9e01d68334e57d95e5d31f53')}" alt="Google results for 2023 election results with Stears ranked first, above the BBC"><span class="k-badge sv-one" style="background: #FFC83D; color: #111">#1<br>on Google</span><figcaption>Stears, still first on Google for “2023 election results”</figcaption></figure>'''),
}

PRACTICE = {
    'svc-positioning': f'''<section class="k-sec k-night sv-practice" aria-labelledby="pr-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">In practice · Xofu, 2026</p><h2 id="pr-t" class="sg sv-q">One question, {mark('everywhere.', '#FFC83D', '#111')}</h2>
<p class="k-sum">Xofu was a new category that buyers struggled to place. I rebuilt its story around the question they were already asking, “Does AI recommend us?”, then carried it through the homepage, pricing and launch emails.</p></div>
<div class="sv-xofu">
<div class="k-fan sv-xofu-fan" data-inview>
<img class="f1" src="{B('0dfa31b585c479139da9600a8bdd8b9d')}" alt="Xofu homepage hero from the rewrite draft" loading="lazy">
<img class="f2" src="{B('a4cbf106e17930bec111332800b706fd')}" alt="Xofu pricing page draft with four tiers" loading="lazy">
</div>
<div class="k-stk s-sun sv-result"><span class="k-kicker">The launch email that followed</span><span class="k-big">3.7%</span><span>click-through rate, double the previous best.</span><a class="k-go" href="Site-Work.dc.html#xofu" style="color: inherit">The full case {ARR}</a></div>
</div>
</div>
</section>''',
    'svc-launch': f'''<section class="k-sec k-ink sv-practice" aria-labelledby="pr-t">
<div class="wrap"><div class="k-head"><p class="eyebrow">Launch day, in creative</p><h2 id="pr-t" class="sg k-h2">Real launches, shipped with {mark('product, sales and partners.', '#FF5A2A', '#111')}</h2></div></div>
<div class="k-wall" aria-label="Launch creative from RemotePass launches"><div class="k-wall-t">
<img src="{B('059d23d54fba852a7e2e28c2b4ef3db4')}" alt="RemotePass × Certn launch visual" loading="lazy">
<img src="{B('c7e58c431da5738727e39bea1b223b8d')}" alt="Wafeq integration announcement visual" loading="lazy">
<img src="{B('c3cb1759fffe47bc7bbed1cc3895d701')}" alt="QuickBooks integration launch post" loading="lazy">
<img src="{B('ef8d3efbfc1194e978574d9eb50ef96f')}" alt="Time-Off Policies launch visual" loading="lazy">
<img src="{B('89d9fecea4c00f909e23139b6e195ac7')}" alt="KSA Payroll launch visual" loading="lazy">
<img src="{B('7b26ce554a84b7e8f8efc0c9b7b09d2e')}" alt="Dubai Fintech Summit countdown post" loading="lazy">
<img src="{B('059d23d54fba852a7e2e28c2b4ef3db4')}" alt="" aria-hidden="true" loading="lazy">
<img src="{B('c7e58c431da5738727e39bea1b223b8d')}" alt="" aria-hidden="true" loading="lazy">
<img src="{B('c3cb1759fffe47bc7bbed1cc3895d701')}" alt="" aria-hidden="true" loading="lazy">
<img src="{B('ef8d3efbfc1194e978574d9eb50ef96f')}" alt="" aria-hidden="true" loading="lazy">
<img src="{B('89d9fecea4c00f909e23139b6e195ac7')}" alt="" aria-hidden="true" loading="lazy">
<img src="{B('7b26ce554a84b7e8f8efc0c9b7b09d2e')}" alt="" aria-hidden="true" loading="lazy">
</div></div>
<div class="wrap k-g2 sv-two">
<div class="k-stk s-orange"><span class="k-big">270+</span><span>media pickups for the RemotePass × Certn launch, including Yahoo Finance, Fox and NBC.</span></div>
<div class="k-stk s-cream" data-inview><span class="k-big">103</span><span>pieces of coverage for the Wafeq integration across the UAE and Saudi Arabia.</span>
<div class="k-bars"><div class="k-bar"><div><span>In Arabic</span><b>56</b></div><div class="k-bar-t"><div class="k-bar-f" style="--w: 54%; --c: #FF5A2A"></div></div></div><div class="k-bar"><div><span>In English</span><b>47</b></div><div class="k-bar-t"><div class="k-bar-f" style="--w: 46%; --c: #111"></div></div></div></div></div>
</div>
</section>''',
    'svc-content': f'''<section class="k-sec k-mint sv-practice" aria-labelledby="pr-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">Why it compounds</p><h2 id="pr-t" class="sg k-h2">Search, AI answers and buyers all reward the same thing: {mark('useful pages, kept up to date.', '#111', '#8FE3B0')}</h2></div>
<div class="k-split">
<div class="k-fan sv-ksa" role="group" aria-label="KSA Payroll campaign posts">
<img class="f1" src="{B('11081f461253fb84fb4a4bb9bf11f88b')}" alt="Carousel cover: Risks of manual payroll in Saudi Arabia" loading="lazy">
<img class="f2" src="{B('a05b79e6e02bc194855c581a19c30ed7')}" alt="Carousel slide: the problem with payroll in KSA" loading="lazy">
<img class="f3" src="{B('8c1cfd21b8b0bd938501fbe875856a81')}" alt="Carousel slide comparing a local payroll provider with RemotePass" loading="lazy">
</div>
<div class="k-stk" data-inview>
<span class="k-kicker">Share of tracked AI answers mentioning RemotePass</span>
<div class="k-bars"><div class="k-bar"><div><span>Before the GEO playbook</span><b>10%</b></div><div class="k-bar-t"><div class="k-bar-f" style="--w: 10%; --c: #8A867E"></div></div></div><div class="k-bar"><div><span>After</span><b>40%</b></div><div class="k-bar-t"><div class="k-bar-f" style="--w: 40%; --c: #1FA463"></div></div></div></div>
<p class="k-p" style="font-size: 16px; margin: 6px 0 0">Alongside an English–Arabic MENA hub, 150+ country guides and a freelance team I hired and briefed, content became a pipeline channel: <strong>$500K+ influenced in under a year</strong>.</p>
<a class="k-go" href="Site-Work.dc.html#engine" style="color: inherit">The full case {ARR}</a>
</div>
</div>
</div>
</section>''',
}

END_TITLE = {
    'svc-positioning': f'Is your story {mark("ready to be told?", "#FFC83D", "#111")}',
    'svc-launch': f'Got a launch {mark("on the calendar?", "#FF5A2A", "#111")}',
    'svc-content': f'Want content that {mark("keeps working?", "#8FE3B0", "#111")}',
}

SVC_CSS = '''
<style>
.sv-ladder ol{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.sv-ladder li{display:flex;justify-content:space-between;align-items:center;gap:14px;padding:16px 20px;border:1.5px solid #111;border-radius:16px;background:#FFFDF6;box-shadow:4px 4px 0 #111;font:700 clamp(18px,1.6vw,22px) 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em;transition:transform .3s}
.sv-ladder li span{font:700 13px 'DM Sans',system-ui,sans-serif;opacity:.6}
.sv-ladder li:nth-child(2){margin-left:6%}.sv-ladder li:nth-child(3){margin-left:12%}.sv-ladder li:nth-child(4){margin-left:18%;background:#111;color:#FFF5D9;box-shadow:4px 4px 0 #FF5A2A}.sv-ladder li:nth-child(5){margin-left:24%;background:#FF5A2A}
.sv-ladder li:hover{transform:translateX(-6px)}
.sv-ladder figcaption{margin-top:14px;font-size:13.5px;opacity:.8}
.sv-count{padding:clamp(22px,2.6vw,32px);border:1.5px solid #111;border-radius:24px;background:#111;color:#F2EFE8;box-shadow:6px 6px 0 #FFC83D}
.sv-count-h{margin:0 0 18px;font:700 13px 'DM Sans',system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#FFC83D}
.sv-count ol{margin:0;padding:0 0 0 28px;list-style:none;display:grid;gap:18px;border-left:2px dashed #45423C}
.sv-count li{position:relative;display:flex;flex-direction:column;gap:4px;font-size:15px;line-height:1.5;color:#C9C4BA}
.sv-count li::before{content:"";position:absolute;left:-38px;top:3px;width:16px;height:16px;border-radius:50%;background:#111;border:2px solid #FF5A2A}
.sv-count li.is-day::before{background:#FF5A2A;box-shadow:0 0 0 6px rgba(255,90,42,.25)}
.sv-count b{font:700 18px 'Space Grotesk',system-ui,sans-serif;color:#F2EFE8}
.sv-serp{position:relative}
.sv-serp .k-shot{transform:rotate(2deg);box-shadow:0 30px 60px rgba(0,0,0,.45)}
.sv-one{left:-22px;top:-26px;width:104px;height:104px;font-size:20px}
.sv-q{margin:0;font-weight:700;font-size:clamp(48px,7vw,116px);line-height:.9;letter-spacing:-.06em;max-width:12ch}
.sv-xofu{display:grid;grid-template-columns:minmax(0,8fr) minmax(0,4fr);gap:clamp(28px,4vw,56px);align-items:center}
.sv-xofu-fan{height:clamp(300px,32vw,460px)}
.sv-xofu-fan .f1{left:0;top:0;width:72%;z-index:1;transform:rotate(-2deg)}
.sv-xofu-fan .f2{right:0;bottom:0;width:52%;transform:rotate(4deg)}
.sv-xofu-fan:hover .f1{transform:rotate(-4deg) translate(-8px,-6px)}.sv-xofu-fan:hover .f2{transform:rotate(7deg) translate(8px,6px)}
.sv-result{transform:rotate(1.5deg)}
.sv-two{margin-top:clamp(28px,3vw,44px)}
.sv-ksa{height:clamp(320px,30vw,420px)}
.sv-ksa img{width:44%;aspect-ratio:4/5;object-fit:cover}
.sv-ksa .f1{left:0;top:8%;transform:rotate(-7deg)}.sv-ksa .f2{left:28%;top:0;z-index:2}.sv-ksa .f3{right:0;top:10%;transform:rotate(7deg)}
.sv-ksa:hover .f1{transform:rotate(-11deg) translateX(-12px)}.sv-ksa:hover .f3{transform:rotate(11deg) translateX(12px)}
.sv-get{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(32px,5vw,72px);align-items:start}
.sv-aside{position:sticky;top:100px;transform:rotate(1deg)}
.sv-aside ul{margin:6px 0 0;padding:0;list-style:none;display:grid;gap:10px}
.sv-aside li{padding:12px 14px;border-radius:12px;background:rgba(255,253,246,.12);font-weight:600}
.sv-cases{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:22px}
.sv-case .k-big{font-size:clamp(64px,7vw,108px)}
.sv-more{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:22px;align-items:stretch}
.sv-read ul{margin:4px 0 0;padding:0;list-style:none;display:grid;gap:12px}
.sv-read a{display:flex;flex-direction:column;gap:2px;color:inherit;text-decoration:none}
.sv-read a b{font:700 17px/1.3 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.015em}
.sv-read a:hover b{color:#C23A0E}
.sv-read a span{font-size:13px;opacity:.7}
.sv-overview .xd-grid{margin-top:clamp(36px,4vw,56px)}
.sv-tool{margin-top:22px;padding:14px 18px;border:1.5px dashed currentColor;border-radius:16px;font-size:15px;line-height:1.6}
@media (max-width:1080px){.sv-xofu,.sv-get{grid-template-columns:1fr}.sv-aside{position:static}}
@media (max-width:640px){.sv-ladder li{margin-left:0 !important}.sv-one{left:-6px;width:84px;height:84px;font-size:16px}.sv-ksa{height:280px}.sv-xofu-fan{height:260px}}
</style>'''


def service(pid):
    h = HERO[pid]
    verb = f'{h["verb"]}<span class="k-dot sv-dot">.</span>'
    light = h['bg'] in ('k-night',)
    btn = 'k-btn-paper' if light else 'h-btn-ink'
    return f'''{SVC_CSS}
<section class="k-hero {h['bg']}">
{motif(h['motif'])}
<div class="wrap">
<nav class="k-crumb" aria-label="Breadcrumb"><a href="Site-Services.dc.html">Expertise</a> / <span>{{{{svc.name}}}}</span></nav>
<div class="k-hero-g">
<div>
<p class="sg sv-verb">Make it {verb}</p>
<h1 class="sg k-h1 k-h1-s">{{{{svc.title}}}}</h1>
<p class="k-lede">{{{{svc.intro}}}}</p>
<div class="k-cta"><a class="h-btn {btn}" href="{CAL}">{h['cta']} <span class="arr" aria-hidden="true">↗</span></a><a class="h-link" href="#proof">See the proof <span aria-hidden="true">↓</span></a></div>
</div>
{h['side']}
</div>
<div class="k-stats"><sc-for list="{{{{svc.stats}}}}" as="s" hint-placeholder-count="3"><div class="k-stat"><b>{{{{s.big}}}}</b><span>{{{{s.label}}}}</span></div></sc-for></div>
</div>
</section>

<section class="k-sec k-paper" aria-label="Who it’s for">
<div class="wrap k-g2">
<div class="k-stk s-mint" style="transform: rotate(-.8deg)"><h2 class="sg k-h3">Who it’s for</h2><ul class="k-list"><sc-for list="{{{{svc.forWho}}}}" as="w" hint-placeholder-count="3"><li>{{{{w.t}}}}</li></sc-for></ul></div>
<div class="k-stk" style="transform: rotate(.7deg)"><h2 class="sg k-h3">Signs you need this</h2><ul class="k-list k-bul"><sc-for list="{{{{svc.signs}}}}" as="g" hint-placeholder-count="5"><li>{{{{g.t}}}}</li></sc-for></ul></div>
</div>
</section>

{PRACTICE[pid]}

<section class="k-sec k-cream" aria-labelledby="get-t">
<div class="wrap sv-get">
<div><p class="eyebrow">What you get</p><h2 id="get-t" class="sg k-h2" style="margin-bottom: 32px">{{{{svc.getsTitle}}}}</h2>
<ol class="k-num"><sc-for list="{{{{svc.gets}}}}" as="g" hint-placeholder-count="5"><li><span><b>{{{{g.h}}}}</b><span>{{{{g.t}}}}</span></span></li></sc-for></ol></div>
<aside class="k-stk s-ink sv-aside"><h3 class="sg k-h3">{{{{svc.extraTitle}}}}</h3>
<sc-if value="{{{{svc.extraText}}}}" hint-placeholder-val="{{{{ true }}}}"><p style="margin: 0; color: #C9C4BA">{{{{svc.extraText}}}}</p></sc-if>
<ul><sc-for list="{{{{svc.extra}}}}" as="x" hint-placeholder-count="4"><li>{{{{x.t}}}}</li></sc-for></ul>
<sc-if value="{{{{svc.extraLink}}}}" hint-placeholder-val="{{{{ true }}}}"><a class="k-go" href="{{{{svc.extraLink}}}}" style="color: #FFC83D">{{{{svc.extraLinkLabel}}}} {ARR}</a></sc-if></aside>
</div>
</section>

<section class="k-sec k-white" aria-labelledby="how-t">
<div class="wrap"><div class="k-head"><p class="eyebrow">How it works</p><h2 id="how-t" class="sg k-h2">Four steps, agreed up front.</h2></div>
<ol class="k-steps"><sc-for list="{{{{svc.steps}}}}" as="s" hint-placeholder-count="4"><li data-n="{{{{s.n}}}}"><b>{{{{s.h}}}}</b><span>{{{{s.t}}}}</span></li></sc-for></ol></div>
</section>

<section id="proof" class="k-sec k-ink" aria-labelledby="proof-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">Proof</p><h2 id="proof-t" class="sg k-h2">{{{{svc.proofTitle}}}}</h2></div>
<div class="sv-cases">
<sc-for list="{{{{svc.cases}}}}" as="c" hint-placeholder-count="2">
<a class="k-stk sv-case" href="{{{{c.href}}}}" style="background: {{{{c.bg}}}}; color: {{{{c.fg}}}}"><span class="k-kicker">{{{{c.client}}}} · {{{{c.year}}}}</span><span class="k-big">{{{{c.big}}}}</span><span class="sg k-h3">{{{{c.title}}}}</span><span style="font-size: 16px; line-height: 1.55">{{{{c.result}}}}</span><span class="k-go">Read the case study {ARR}</span></a>
</sc-for>
</div>
<sc-if value="{{{{svc.hasQuote}}}}" hint-placeholder-val="{{{{ true }}}}"><figure class="k-quote" style="margin-top: 36px; max-width: 900px"><blockquote>“{{{{svc.quote}}}}”</blockquote><figcaption><b>{{{{svc.quoteName}}}}</b> · {{{{svc.quoteOrg}}}}</figcaption></figure></sc-if>
<sc-if value="{{{{svc.note}}}}" hint-placeholder-val="{{{{ true }}}}"><p class="sv-tool">{{{{svc.note}}}}</p></sc-if>
</div>
</section>

<section class="k-sec k-paper" aria-label="Related">
<div class="wrap sv-more">
<sc-if value="{{{{svc.tool}}}}" hint-placeholder-val="{{{{ true }}}}"><a class="k-stk s-sun" href="{{{{svc.tool.href}}}}" style="transform: rotate(-1deg)"><span class="k-tag">Free tool</span><span class="sg k-h3">{{{{svc.tool.name}}}}</span><span>{{{{svc.tool.line}}}}</span><span class="k-go">Try it {ARR}</span></a></sc-if>
<a class="k-stk s-mint" href="{{{{svc.paired.href}}}}"><span class="k-tag">Often paired with</span><span class="sg k-h3">{{{{svc.paired.name}}}}</span><span>{{{{svc.paired.line}}}}</span><span class="k-go">See the service {ARR}</span></a>
<div class="k-stk sv-read" style="transform: rotate(.8deg)"><span class="k-tag">Further reading</span><ul><sc-for list="{{{{svc.reading}}}}" as="r" hint-placeholder-count="2"><li><a href="{{{{r.href}}}}"><b>{{{{r.title}}}}</b><span>{{{{r.where}}}}</span></a></li></sc-for></ul></div>
</div>
</section>

<section id="faq" class="k-sec k-cream" aria-labelledby="faq-t">
<div class="wrap k-split"><h2 id="faq-t" class="sg k-h2">Questions people ask</h2>
<div class="k-faq"><sc-for list="{{{{faq}}}}" as="q" hint-placeholder-count="5"><details><summary>{{{{q.q}}}}<i aria-hidden="true">+</i></summary><p>{{{{q.a}}}}</p></details></sc-for></div></div>
</section>

<!--CONTACT:{END_TITLE[pid]}-->
'''


def services():
    return f'''{SVC_CSS}
<section class="k-hero k-night sv-overview">
{motif('venn')}
<div class="wrap">
<p class="eyebrow">Expertise</p>
<h1 class="sg k-h1" style="max-width: 17ch">Marketing for B2B SaaS and technology companies: {mark('three services, one practice.', '#8FE3B0', '#0E2A2E')}</h1>
<p class="k-lede">Choose by the problem you have, then by how you want to work. Research, SEO, AI search and sales enablement are how I do the work. These three are what the work is for.</p>
<div class="xd-grid">
<sc-for list="{{{{services}}}}" as="d" hint-placeholder-count="3">
<a class="xd {{{{d.cls}}}}" href="{{{{d.href}}}}"><span class="xd-badge"><span class="shp {{{{d.shp}}}} xd-shp" aria-hidden="true"></span><span class="xd-emo" aria-hidden="true">{{{{d.emo}}}}</span></span><span class="xd-verb sg">{{{{d.verb}}}}<i>.</i></span><span class="xd-name sg">{{{{d.name}}}}</span><span class="xd-long"><b>Choose this when</b> {{{{d.when}}}}</span><span class="xd-proof"><b>Proof</b> {{{{d.proof}}}}</span><span class="xd-go">See the service {ARR}</span></a>
</sc-for>
</div>
</div>
</section>

<section class="k-sec k-paper" aria-label="Who it’s for">
<div class="wrap k-g2">
<div class="k-stk s-mint" style="transform: rotate(-.8deg)"><h2 class="sg k-h3">Who it’s for</h2><ul class="k-list"><sc-for list="{{{{forWho}}}}" as="w" hint-placeholder-count="4"><li>{{{{w.t}}}}</li></sc-for></ul></div>
<div class="k-stk s-blush" style="transform: rotate(.7deg)"><h2 class="sg k-h3">Who it isn’t for</h2><ul class="k-list k-x"><sc-for list="{{{{notFor}}}}" as="w" hint-placeholder-count="3"><li>{{{{w.t}}}}</li></sc-for></ul></div>
</div>
</section>

<section class="k-sec k-cream" aria-labelledby="ways-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">Ways to work together</p><h2 id="ways-t" class="sg k-h2">Pick the shape that fits {mark('your problem.', '#FF5A2A', '#111')}</h2></div>
<div class="k-g4 k-rot k-rot5">
<sc-for list="{{{{ways}}}}" as="w" hint-placeholder-count="4">
<a class="k-stk" href="{{{{w.href}}}}"><span class="sg k-big" style="font-size: 44px">{{{{w.n}}}}</span><h3 class="sg k-h3">{{{{w.h}}}}</h3><span style="font-size: 16px; line-height: 1.55">{{{{w.t}}}}</span><span class="k-go">{{{{w.cta}}}}</span></a>
</sc-for>
</div>
</div>
</section>

<section class="k-sec k-white" aria-labelledby="run-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">How an engagement runs</p><h2 id="run-t" class="sg k-h2">From first call to measured result.</h2></div>
<ol class="k-steps"><sc-for list="{{{{steps}}}}" as="s" hint-placeholder-count="4"><li data-n="{{{{s.n}}}}"><b>{{{{s.h}}}}</b><span>{{{{s.t}}}}</span></li></sc-for></ol>
</div>
</section>

<section class="k-sec k-sun" aria-label="Results">
<div class="wrap"><p class="eyebrow">Across my work</p>
<div class="k-stats" style="margin-top: 12px"><sc-for list="{{{{proof}}}}" as="p" hint-placeholder-count="4"><div class="k-stat"><b>{{{{p.big}}}}</b><span>{{{{p.label}}}}</span></div></sc-for></div></div>
</section>

<section id="faq" class="k-sec k-paper" aria-labelledby="faq-t">
<div class="wrap k-split"><h2 id="faq-t" class="sg k-h2">Questions people ask</h2>
<div><div class="k-faq"><sc-for list="{{{{faq}}}}" as="q" hint-placeholder-count="5"><details><summary>{{{{q.q}}}}<i aria-hidden="true">+</i></summary><p>{{{{q.a}}}}</p></details></sc-for></div>
<p class="sv-tool"><b>Toolkit</b> · {{{{toolkit}}}}</p></div></div>
</section>

<!--CONTACT:Which one are you {mark('working on?', '#FFC83D', '#111')}-->
'''
