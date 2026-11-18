"""About, Writing, EmpowerQ and Contact in the homepage's language."""
from kit import mark, ARR, footer_html, motif

B = lambda i: '/_blob/' + i

ABOUT_CSS = '''
<style>
.ab-hero .k-hero-g{align-items:center}
.ab-big{margin:0;font-weight:700;font-size:clamp(46px,6.6vw,108px);line-height:.94;letter-spacing:-.055em}
.ab-big+.ab-big{margin-top:6px}
.ab-id{margin:0 0 22px;max-width:40ch;font-size:16px;line-height:1.5;color:#9DB8B0}
.ab-id b{color:#EAF6F1}
.ab-port{position:relative;aspect-ratio:1/1.12;max-width:520px;justify-self:end;width:100%}
.ab-port .f{position:absolute;left:6%;top:4%;width:88%;aspect-ratio:1;background:#FF8FB6;animation:spin 70s linear infinite}
.ab-port .ph{position:absolute;left:18%;top:12%;width:64%;aspect-ratio:4/5;object-fit:cover;object-position:center 15%;border-radius:200px 200px 24px 24px;border:1.5px solid #111;transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.ab-port:hover .ph{transform:rotate(-3deg)}
.ab-port .k-badge{right:2%;bottom:10%;width:120px;height:120px;background:#FFC83D;color:#111}
.ab-ch{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,5fr);gap:clamp(32px,5vw,80px);align-items:center;padding:clamp(48px,6vw,80px) 0;border-top:2px solid #111}
.ab-ch:nth-of-type(even) .ab-ch-m{order:-1}
.ab-ch-n{display:flex;align-items:center;gap:14px;margin:0 0 14px;font-weight:700;font-size:14px}
.ab-ch-n b{display:inline-grid;place-items:center;width:58px;height:58px;border-radius:50%;border:1.5px solid #111;box-shadow:3px 3px 0 #111;font:700 20px 'Space Grotesk',system-ui,sans-serif}
.ab-ch:nth-of-type(4n+1) .ab-ch-n b{background:#FFC83D}.ab-ch:nth-of-type(4n+2) .ab-ch-n b{background:#8FE3B0}.ab-ch:nth-of-type(4n+3) .ab-ch-n b{background:#FF8FB6}.ab-ch:nth-of-type(4n+4) .ab-ch-n b{background:#B9A6FF}
.ab-ch h3{margin:0 0 16px;font-weight:700;font-size:clamp(30px,3.4vw,52px);line-height:1;letter-spacing:-.045em}
.ab-ch-m{display:flex;flex-direction:column;gap:22px}
.ab-ch-m .k-fig:nth-child(1) .k-shot{transform:rotate(-2deg)}
.ab-ch-m .k-fig:nth-child(2){max-width:70%;margin-left:auto}
.ab-ch-m .k-fig:nth-child(2) .k-shot{transform:rotate(2.5deg)}
.ab-pull{margin:0;padding:clamp(56px,7vw,96px) 0;text-align:center}
.ab-pull p{margin:0 auto;max-width:18ch;font-weight:700;font-size:clamp(38px,5vw,80px);line-height:1;letter-spacing:-.05em}
.ab-now-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(32px,5vw,80px);align-items:center}
.ab-now-ph{position:relative}
.ab-now-ph img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:58% center;border-radius:24px 200px 24px 24px;border:1.5px solid #1C1430}
.ab-now-ph figcaption{margin-top:12px;font-size:13.5px}
.ab-rec{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:clamp(32px,5vw,72px);align-items:start;margin-top:clamp(64px,8vw,104px)}
.ab-rec ul{margin:0;padding:0;list-style:none;border-top:2px solid #111}
.ab-rec li{display:grid;grid-template-columns:64px 1fr;gap:16px;padding:16px 0;border-bottom:1px solid #C9C3B6;font-size:17px;line-height:1.5}
.ab-rec li b{font:700 17px 'Space Grotesk',system-ui,sans-serif;color:#C23A0E}
.ab-rec .k-fig img{display:block;width:100%;aspect-ratio:560/996;object-fit:cover;border-radius:200px 200px 24px 24px;border:1.5px solid #111}
.ab-facts{margin-top:clamp(40px,5vw,56px);border:1.5px solid #111;border-radius:22px;background:#FFFDF6;box-shadow:5px 5px 0 #111;padding:0 clamp(20px,2.4vw,30px)}
.ab-facts summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;padding:20px 0;font:700 22px 'Space Grotesk',system-ui,sans-serif}
.ab-facts summary::-webkit-details-marker{display:none}
.ab-facts dl{margin:0 0 18px;display:grid;gap:12px}
.ab-facts dl div{display:grid;grid-template-columns:140px 1fr;gap:14px;font-size:16px;line-height:1.5}
.ab-facts dt{font-weight:700}
.ab-facts p{display:flex;flex-wrap:wrap;gap:8px 18px;margin:0 0 22px}
.ab-facts p a{font-weight:700;color:#111;text-underline-offset:4px;text-decoration-color:#FF5A2A}
@media (max-width:1080px){.ab-ch,.ab-now-g,.ab-rec{grid-template-columns:1fr}.ab-ch:nth-of-type(even) .ab-ch-m{order:0}.ab-port{justify-self:center;max-width:420px}}
@media (max-width:640px){.ab-facts dl div{grid-template-columns:1fr;gap:2px}.ab-ch-m .k-fig:nth-child(2){max-width:100%}}
</style>'''


def about():
    return f'''{ABOUT_CSS}
<section class="k-hero k-night ab-hero">
{motif('route')}
<div class="wrap k-hero-g">
<div>
<h1 class="ab-id"><b>Jeremiah Ajayi.</b> Marketing consultant for B2B SaaS and technology companies, based in Lagos.</h1>
<p class="sg ab-big">I studied how to win an argument.</p>
<p class="sg ab-big">Now I help good products {mark('win theirs.', '#FF8FB6', '#111')}</p>
<p class="k-lede">Eight years of positioning, launches and content for companies in fintech, HR tech, AI and media. Before that, a law student who couldn’t stop writing. Now also the co-founder of EmpowerQ.</p>
<div class="k-cta"><a class="h-btn k-btn-paper" href="#story">Read the story <span class="arr arr-d" aria-hidden="true">↓</span></a><a class="h-link" href="#now">Hiring? Start here {ARR}</a></div>
</div>
<div class="ab-port">
<span class="shp shp-flower f" aria-hidden="true"></span>
<img class="ph" src="{B('ed98487bc78b8be08bddc3d53416cc60')}" alt="Jeremiah Ajayi, standing outside in Lagos">
<span class="k-badge" aria-hidden="true">Lagos<br>🇳🇬</span>
</div>
</div>
</section>

<section id="story" class="k-sec k-paper" aria-labelledby="story-t">
<div class="wrap">
<p class="eyebrow">The story so far</p>
<h2 id="story-t" class="sg k-h2" style="margin-bottom: clamp(32px, 4vw, 56px)">The chapters {mark('a summary skips.', '#FFC83D')}</h2>
<sc-for list="{{{{chapters}}}}" as="c" hint-placeholder-count="3">
<article id="{{{{c.id}}}}" class="ab-ch">
<div>
<p class="ab-ch-n"><b>{{{{c.n}}}}</b><span>{{{{c.when}}}}</span></p>
<h3 class="sg">{{{{c.h}}}}</h3>
<p class="k-p">{{{{c.p1}}}}</p>
<p class="k-p">{{{{c.p2}}}}</p>
</div>
<sc-if value="{{{{c.photo}}}}"><div class="ab-ch-m"><figure class="k-fig"><img class="k-shot" src="{{{{c.photo}}}}" alt="{{{{c.alt}}}}" loading="lazy"><figcaption>{{{{c.caption}}}}</figcaption></figure><sc-if value="{{{{c.photo2}}}}"><figure class="k-fig"><img class="k-shot" src="{{{{c.photo2}}}}" alt="{{{{c.alt2}}}}" loading="lazy"><figcaption>{{{{c.caption2}}}}</figcaption></figure></sc-if></div></sc-if>
</article>
</sc-for>
</div>
</section>

<section class="k-sun ab-pull" aria-label="A lesson"><div class="wrap"><p class="sg">Small proof compounds. Nothing is truly wasted when you are {mark('paying attention.', '#111', '#FFC83D')}</p></div></section>

<section class="k-sec k-paper" aria-label="Chapter four">
<div class="wrap">
<article id="ch4" class="ab-ch" style="border-top: 0; padding-top: 0">
<div>
<p class="ab-ch-n"><b style="background: #B9A6FF">04</b><span>2023 to 2026</span></p>
<h3 class="sg">Starting again, and going global</h3>
<p class="k-p">Leaving OAU left a gap that mattered to me. In 2023 I went back to school, studying Business Management at Miva Open University while working full-time.</p>
<p class="k-p">At RemotePass, a Dubai-based HR and payroll platform, I led GTM for launches across EMEA, North America and APAC. Some went out in English and Arabic on the same day; one partnership reached 270+ media outlets. The work took me to more than ten countries.</p>
<p class="k-p">Then I led product marketing at Xofu, an AI visibility platform, and started publishing my own research on how AI assistants choose which brands to recommend.</p>
<p style="margin-top: 22px"><a class="h-link" href="Site-Work.dc.html">See the work {ARR}</a></p>
</div>
<div class="ab-ch-m"><figure class="k-fig"><img class="k-shot" src="{{{{dfs}}}}" alt="Campaign post counting down to RemotePass at Dubai Fintech Summit 2025" loading="lazy" style="max-width: 420px"><figcaption>Campaign creative for RemotePass at Dubai Fintech Summit 2025</figcaption></figure></div>
</article>
</div>
</section>

<section id="empowerq" class="k-sec k-lav" aria-labelledby="eq-now-t">
<span class="shp shp-flower k-shape" aria-hidden="true" style="right: -70px; top: -70px; width: 240px; height: 240px; background: #FFC83D; z-index: 0"></span>
<div class="wrap ab-now-g" style="position: relative">
<div>
<p class="ab-ch-n"><b style="background: #FFFDF6">05</b><span>Now</span></p>
<h2 id="eq-now-t" class="sg k-h2">Opening doors I had to {mark('find my own way through.', '#1C1430', '#E9E2FF')}</h2>
<p class="k-p" style="margin-top: 22px">In 2025 I co-founded EmpowerQ, a nonprofit working on economic inclusion for LGBTQ+ professionals in Nigeria. It takes what I learned pitching my way into global work and makes that path open to more people.</p>
<div class="k-stats"><sc-for list="{{{{empowerq}}}}" as="e" hint-placeholder-count="3"><div class="k-stat"><b>{{{{e.big}}}}</b><span>{{{{e.label}}}}</span></div></sc-for></div>
<div class="k-cta"><a class="eq-btn" href="Site-EmpowerQ.dc.html">Inside EmpowerQ {ARR}</a></div>
</div>
<figure class="ab-now-ph"><img src="{B('2887802b6b670e13694193452b911747')}" alt="Name tags and lanyards for Out of Office, EmpowerQ’s queer career conference" loading="lazy"><figcaption>Name tags for Out of Office, our first conference. We keep attendees’ faces off the web.</figcaption></figure>
</div>
<div class="wrap k-g3 k-rot" style="margin-top: clamp(40px, 5vw, 64px); position: relative">
<sc-for list="{{{{alsoNow}}}}" as="a" hint-placeholder-count="3"><div class="k-stk"><span class="sg k-h3">{{{{a.h}}}}</span><span style="font-size: 16px; line-height: 1.55">{{{{a.t}}}}</span></div></sc-for>
</div>
</section>

<section class="qs" aria-labelledby="qs-title">
<div class="wrap">
<p class="eyebrow">In their words</p>
<h2 id="qs-title" class="sg qs-title">What people say about working with me.</h2>
<div class="qt-row"><sc-for list="{{{{quotes}}}}" as="q" hint-placeholder-count="4"><figure class="qt {{{{q.cls}}}}"><blockquote class="sg">“{{{{q.text}}}}”</blockquote><figcaption><b>{{{{q.name}}}}</b> · {{{{q.org}}}}</figcaption></figure></sc-for></div>
<div class="ab-rec">
<figure class="k-fig"><img src="{B('1ada8c43b66919c70ad6d23904db5df0')}" alt="Jeremiah receiving the Martech Africa award for Content Marketing Specialist of the Year" loading="lazy"><figcaption>Receiving the Martech Africa award, 2025</figcaption></figure>
<div>
<h3 class="sg k-h2" style="margin-bottom: 24px">Recognition</h3>
<ul><sc-for list="{{{{recognition}}}}" as="r" hint-placeholder-count="6"><li><b>{{{{r.y}}}}</b><span>{{{{r.t}}}}</span></li></sc-for><li><b>↗</b><a class="h-link" href="https://blog.useaccrue.com/this-marketer-wants-to-earn-7k-next-how-can-he-do-it">Read my Accrue spotlight</a></li></ul>
<div class="k-stk s-mint" style="margin-top: 28px; transform: rotate(-1deg)"><span class="k-tag">A side note</span><span class="k-big">60+</span><span class="sg k-h3">certifications</span><span style="font-size: 16px; line-height: 1.55">From CXL, HubSpot, the University of London and the International Business Management Institute, among others. I never stopped studying, even when I left school.</span></div>
</div>
</div>
</div>
</section>

<section id="now" class="k-sec k-cream" aria-labelledby="now-t" style="padding-bottom: clamp(110px, 12vw, 170px)">
<div class="wrap">
<h2 id="now-t" class="sg k-h2" style="margin-bottom: clamp(32px, 4vw, 52px)">Let’s work out {mark('the next chapter.', '#FF5A2A', '#111')}</h2>
<div class="k-g3 k-rot">
<a class="k-stk s-sun" href="Site-Contact.dc.html#hiring"><span class="k-emo"><span class="shp shp-flower" style="background: #FFFDF6"></span><i aria-hidden="true">💼</i></span><span class="k-kicker">For employers and hiring managers</span><span class="sg k-h3">I’m open to senior product marketing, content and growth roles, remote or with relocation.</span><span class="k-go">Get my CV {ARR}</span></a>
<a class="k-stk s-mint" href="Site-Services.dc.html"><span class="k-emo"><span class="shp shp-star" style="background: #FFC83D"></span><i aria-hidden="true">🧭</i></span><span class="k-kicker">For companies</span><span class="sg k-h3">Select consulting projects in positioning, launches and content.</span><span class="k-go">See the services {ARR}</span></a>
<a class="k-stk s-lav" href="Site-EmpowerQ.dc.html"><span class="k-emo"><span class="shp shp-clover" style="background: #1C1430"></span><i aria-hidden="true">🌈</i></span><span class="k-kicker">For funders and partners</span><span class="sg k-h3">Help EmpowerQ open more doors.</span><span class="k-go">Support EmpowerQ {ARR}</span></a>
</div>
<details class="ab-facts"><summary>Quick facts <span aria-hidden="true">+</span></summary>
<dl><sc-for list="{{{{brief}}}}" as="b" hint-placeholder-count="6"><div><dt>{{{{b.k}}}}</dt><dd>{{{{b.v}}}}</dd></div></sc-for></dl>
<p><sc-for list="{{{{profiles}}}}" as="l" hint-placeholder-count="5"><a href="{{{{l.href}}}}">{{{{l.label}}}} ↗</a></sc-for></p>
</details>
</div>
</section>
<!--NOBAND-->
'''


WR_CSS = '''
<style>
.wr-hero .k-h1{max-width:12ch}
.wr-hero .rs-fan{position:relative;top:auto;justify-self:center;width:min(100%,400px)}
.wr-studies .k-stk{min-height:300px}
.wr-studies .k-big{font-size:clamp(56px,5.6vw,88px)}
.wr-start{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(22px,3vw,36px);align-items:stretch}
.wr-essay{padding:0;overflow:hidden}
.wr-essay img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;object-position:center 20%;border-bottom:1.5px solid #111}
.wr-essay .in{display:flex;flex-direction:column;gap:10px;padding:clamp(20px,2.4vw,30px)}
.wr-feat{display:grid;gap:16px}
.wr-feat .k-stk{display:grid;grid-template-columns:auto 1fr;gap:6px 20px;align-items:center}
.wr-feat .k-big{font-size:clamp(44px,4.4vw,68px);grid-row:span 2}
.wr-feat small{display:block;font-size:12.5px;font-weight:700;opacity:.7}
.wr-arch-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:20px;margin-bottom:28px}
.wr-search{display:flex;flex-direction:column;gap:8px;min-width:min(100%,380px)}
.wr-search label{font-size:13px;font-weight:700}
.wr-search input{min-height:52px;padding:0 20px;border-radius:999px;border:1.5px solid #111;background:#FFFDF6;font:500 16px 'DM Sans',system-ui,sans-serif;color:#111;box-shadow:3px 3px 0 #111}
.wr-search input:focus{outline:3px solid #FF5A2A;outline-offset:2px}
.wr-list{margin:24px 0 0;padding:0;list-style:none;border-top:2px solid #111}
.wr-list .rs-row{grid-template-columns:170px minmax(0,1fr) 110px}
.wr-list .rs-row>span:last-child{text-align:right;font-size:13px;color:#6B675F}
.wr-list .rs-t,.wr-list .rs-note{display:block}
.wr-feats{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,340px),1fr));gap:16px}
.wr-feats a{height:100%;box-sizing:border-box}
@media (max-width:1080px){.wr-start{grid-template-columns:1fr}}
@media (max-width:640px){.wr-list .rs-row{grid-template-columns:1fr}.wr-list .rs-row>span:last-child{text-align:left}.wr-feat .k-stk{grid-template-columns:1fr}.wr-feat .k-big{grid-row:auto}}
</style>'''


def writing():
    return f'''{WR_CSS}
<section class="k-hero k-cream wr-hero">
{motif('ruled')}
<div class="wrap k-hero-g">
<div>
<p class="eyebrow">Writing &amp; research</p>
<h1 class="sg k-h1">How buyers find, judge and {mark('choose.', '#1FA463', '#FFFDF6')}</h1>
<p class="k-lede">Original research on AI search, teardowns of launches and growth, and the playbooks I use. Published here, at Foundation Labs, Condia, Buffer and the Product Marketing Alliance.</p>
<div class="k-cta"><a class="btn-o h-btn" href="#all">Browse the archive <span class="arr arr-d" aria-hidden="true">↓</span></a><a class="h-link" href="https://stateofaisearchinnigeria.eo.page/download">Read the report {ARR}</a></div>
</div>
<figure class="rs-fan" data-inview>
<a href="https://stateofaisearchinnigeria.eo.page/download" aria-label="Read The State of AI Search in Nigeria">
<img class="rs-back" src="{B('7eb8244cdcb54835b411e77a562f76ac')}" alt="" loading="lazy">
<img class="rs-front" src="{B('33c1f064948e333f4df17633271445aa')}" alt="Cover of The State of AI Search in Nigeria, by Jeremiah Ajayi and Felix Akinnibi" width="1000" height="1414">
<span class="rs-sticker sg" aria-hidden="true">A first<br>for Nigeria</span>
</a>
<figcaption><b>The State of AI Search in Nigeria</b><span>2026 · co-authored with Felix Akinnibi</span></figcaption>
</figure>
</div>
</section>

<section class="k-sec k-night wr-studies" aria-labelledby="st-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">Foundation Labs research</p><h2 id="st-t" class="sg k-h2">Four studies on how {mark('AI chooses its sources.', '#8FE3B0', '#0E2A2E')}</h2><p class="k-sum">Original investigations I authored for Foundation Marketing’s research lab.</p></div>
<div class="k-g4 k-rot">
<sc-for list="{{{{studies}}}}" as="s" hint-placeholder-count="4">
<a class="k-stk" href="{{{{s.href}}}}" style="background: {{{{s.bg}}}}; color: {{{{s.fg}}}}"><span class="k-kicker">{{{{s.no}}}} · {{{{s.subject}}}}</span><span class="k-big">{{{{s.big}}}}</span><span class="sg k-h3">{{{{s.title}}}}</span><span style="font-size: 15px; line-height: 1.5">{{{{s.finding}}}}</span><span class="k-go">Read the study {ARR}</span></a>
</sc-for>
</div>
</div>
</section>

<section class="k-sec k-paper" aria-labelledby="sh-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow">Start here</p><h2 id="sh-t" class="sg k-h2">An essay, and three pieces built on {mark('original data.', '#FFC83D')}</h2></div>
<div class="wr-start">
<a class="k-stk wr-essay" href="https://www.thejeremiahajayi.com/post/the-life-i-chose-after-the-life-i-planned" style="transform: rotate(-1deg)">
<img src="{B('bdf09678f86df90bce8dc2fbad846823')}" alt="Jeremiah as a law student at Obafemi Awolowo University" loading="lazy">
<span class="in"><span class="k-tag">Personal essay · July 2026</span><span class="sg k-h3">The life I chose after the life I planned</span><span>Leaving Law, starting again, and the people who left fingerprints on the story.</span><span class="k-go">Read the essay {ARR}</span></span>
</a>
<div class="wr-feat">
<sc-for list="{{{{featured}}}}" as="f" hint-placeholder-count="3">
<a class="k-stk" href="{{{{f.href}}}}" style="background: {{{{f.bg}}}}; color: {{{{f.fg}}}}"><span class="k-big">{{{{f.big}}}}</span><span><small>{{{{f.unit}}}}</small><span class="sg k-h3" style="font-size: 22px">{{{{f.title}}}}</span></span><span style="font-size: 15px">{{{{f.dek}}}}</span></a>
</sc-for>
</div>
</div>
</div>
</section>

<section id="all" class="k-sec k-cream" aria-labelledby="ar-t">
<div class="wrap">
<div class="wr-arch-h">
<div><h2 id="ar-t" class="sg k-h2" style="margin-bottom: 18px">The archive</h2>
<div class="k-chips" role="group" aria-label="Filter writing by topic"><sc-for list="{{{{filters}}}}" as="f" hint-placeholder-count="6"><button class="k-chip" data-css data-f="{{{{f.id}}}}" aria-pressed="{{{{f.pressed}}}}" onClick="{{{{f.pick}}}}">{{{{f.label}}}} <span>{{{{f.count}}}}</span></button></sc-for></div></div>
<div class="wr-search"><label for="q">Search the archive</label><input id="q" type="search" data-search placeholder="Try “AI search”, “launch” or “Condia”" value="{{{{q}}}}" onInput="{{{{onSearch}}}}"></div>
</div>
<ul class="wr-list">
<sc-for list="{{{{shown}}}}" as="p" hint-placeholder-count="10">
<li data-k="{{{{p.cat}}}}" data-text="{{{{p.text}}}}"><a class="rs-row" href="{{{{p.href}}}}"><span class="rs-outlet">{{{{p.where}}}}</span><span><span class="rs-t">{{{{p.title}}}}</span><span class="rs-note">{{{{p.dek}}}}</span></span><span>{{{{p.meta}}}}</span></a></li>
</sc-for>
</ul>
<p data-empty style="display: none; margin-top: 24px; font-size: 17px">Nothing matches that yet. Try a broader word, or <a class="h-link" href="Site-Contact.dc.html">ask me about it</a>.</p>
</div>
</section>

<section class="k-sec k-paper" aria-labelledby="fm-t" style="padding-bottom: clamp(110px, 12vw, 170px)">
<div class="wrap">
<h2 id="fm-t" class="sg k-h2" style="margin-bottom: 28px">Features &amp; mentions</h2>
<ul class="wr-feats k-rot k-rot5"><sc-for list="{{{{features}}}}" as="x" hint-placeholder-count="6"><li><a class="k-stk" href="{{{{x.href}}}}"><span class="k-tag">{{{{x.who}}}}</span><span style="font-size: 16px; line-height: 1.5; font-weight: 600">{{{{x.what}}}}</span><span class="k-go">Read it <span aria-hidden="true">↗</span></span></a></li></sc-for></ul>
</div>
</section>
<!--CONTACT:Need this thinking on {mark('your positioning, launch or content?', '#FFC83D', '#111')}-->
'''


EQ_CSS = '''
<style>
.eqp-hero{background:#B9A6FF;color:#1C1430}
.eqp-hero .k-h1{font-size:clamp(64px,8.4vw,136px);line-height:.8;letter-spacing:-.075em;max-width:none}
.eqp-lede{margin:22px 0 0;max-width:22ch;font:600 clamp(24px,2.4vw,36px)/1.12 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.025em}
.eqp-why{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(32px,5vw,80px);align-items:start}
.eqp-why .k-p{color:#D6CCFF}
.eqp-why .sig{margin-top:22px;font-weight:700;color:#B9A6FF}
.eqp-ll{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(20px,2.6vw,32px);align-items:start}
.eqp-ll-c{background:#1C1430;color:#E9E2FF;box-shadow:6px 6px 0 #B9A6FF}
.eqp-ll-c video{display:block;width:min(100%,280px);margin:10px auto 0;border-radius:22px;border:1.5px solid #B9A6FF}
.eqp-progs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.eqp-progs .k-stk{padding:18px 20px;box-shadow:4px 4px 0 #1C1430;border-color:#1C1430}
.eqp-progs .k-stk:nth-child(4n+1){background:#E9E2FF}.eqp-progs .k-stk:nth-child(4n+2){background:#FFC83D}.eqp-progs .k-stk:nth-child(4n+3){background:#FF8FB6}.eqp-progs .k-stk:nth-child(4n+4){background:#FFFDF6}
.eqp-receipts{background:#FFF5D9;color:#1C1430;--dot:#7B5CF0}
.eqp-core{margin:0;max-width:20ch;font-weight:700;font-size:clamp(38px,4.8vw,76px);line-height:.98;letter-spacing:-.05em}
.eqp-poster{margin-top:clamp(40px,5vw,64px);display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:clamp(28px,3vw,44px) clamp(20px,2.4vw,36px);align-items:end;border-top:2px solid #1C1430;padding-top:clamp(28px,3vw,40px)}
.eqp-n{grid-column:span 2;display:flex;flex-direction:column;gap:8px}
.eqp-n b{font-size:clamp(56px,5.4vw,88px);line-height:.86;letter-spacing:-.06em}
.eqp-n span{font-size:15.5px;line-height:1.45;max-width:26ch;color:#2E2350}
.eqp-n.is-hero{grid-column:span 6;flex-direction:row;align-items:flex-end;gap:12px 28px;flex-wrap:wrap}
.eqp-n.is-hero b{font-size:clamp(140px,19vw,300px);color:#1C1430}
.eqp-n.is-hero span{font:700 clamp(24px,2.6vw,40px)/1.05 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.03em;max-width:12ch;padding-bottom:.6em;color:#7B5CF0}
.eqp-n.is-big{grid-column:span 3}
.eqp-n.is-big b{font-size:clamp(80px,9vw,150px)}
.eqp-built{margin:clamp(36px,4vw,52px) 0 0;padding:18px 0;border-top:1px solid rgba(28,20,48,.25);border-bottom:1px solid rgba(28,20,48,.25);font-size:16px;line-height:1.6;color:#2E2350}
.eqp-next{margin:clamp(28px,3vw,40px) 0 0;font-size:clamp(28px,3.2vw,48px);font-weight:700;letter-spacing:-.04em;line-height:1.05}
.eqp-partners{margin:22px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,210px),1fr));gap:14px}
.eqp-partners li{display:grid;place-items:center;height:128px;padding:16px 26px;box-sizing:border-box;border-radius:20px;background:#FFFFFF;border:1.5px solid #1C1430;box-shadow:4px 4px 0 #1C1430;transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.eqp-partners li:hover{transform:translate(-2px,-3px) rotate(-1deg)}
.eqp-partners img{max-height:80px;max-width:100%;width:auto;object-fit:contain}
.eqp-stats .k-stat{border-color:#1C1430;box-shadow:4px 4px 0 #1C1430}
.eqp-ways{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:16px}
.eqp-ways .k-stk{border-color:#1C1430;box-shadow:5px 5px 0 #1C1430}
.eqp-note{margin:28px 0 0;max-width:70ch;font-size:14.5px;line-height:1.6;opacity:.8}
.eqp-end{background:#1C1430;color:#E9E2FF}
.eqp-end .k-end-s{background:#B9A6FF}
@media (max-width:1080px){.eqp-why,.eqp-ll{grid-template-columns:1fr}}
@media (max-width:640px){.eqp-progs{grid-template-columns:1fr}.eqp-poster{grid-template-columns:repeat(2,minmax(0,1fr))}.eqp-n,.eqp-n.is-big{grid-column:span 1}.eqp-n.is-hero{grid-column:span 2}.eqp-partners{grid-template-columns:repeat(2,minmax(0,1fr))}.eqp-partners li{height:100px}}
</style>'''


def empowerq():
    return f'''{EQ_CSS}
<section class="k-hero eqp-hero">
{motif('arches')}
<span class="shp shp-flower k-shape" aria-hidden="true" style="left: 38%; bottom: -60px; width: 150px; height: 150px; background: #FF8FB6"></span>
<div class="wrap eq-grid">
<div class="eq-copy">
<p class="eq-top"><span class="eyebrow eq-eyebrow">Co-founded in 2025 · now in year two</span><span class="eq-pill">Finalist · Social Shifters Global Innovation Challenge 2026</span></p>
<h1 class="sg k-h1">EmpowerQ</h1>
<p class="eq-lede eqp-lede sg">Every queer Nigerian professional deserves a fair shot at a good career.</p>
<p class="k-p" style="margin-top: 20px; color: #2E2350">EmpowerQ builds career infrastructure for LGBTQ+ professionals in Nigeria: jobs, skills, mentorship, research and a community that makes work safer and more rewarding. In our first year, we supported 20+ people into jobs and trained 500+.</p>
<div class="eq-cta"><a class="eq-btn" href="#involved">Get involved <span aria-hidden="true">↓</span></a><a class="eq-link" href="https://www.empowerqueer.org">Visit EmpowerQ ↗</a></div>
</div>
<figure class="eq-photo"><img src="{B('2887802b6b670e13694193452b911747')}" alt="Name tags and lanyards laid out for Out of Office, EmpowerQ’s queer career conference"><span class="eq-badge sg"><b>100+</b>registered for our first Out of Office</span><figcaption>Name tags for Out of Office, Nigeria’s first queer career conference. We keep attendees’ faces off the web.</figcaption></figure>
</div>
</section>

<section class="k-sec k-plum" aria-labelledby="why-t">
<div class="wrap eqp-why">
<div><p class="eyebrow">Why it exists</p><h2 id="why-t" class="sg k-h2">Talent is everywhere. {mark('Opportunity isn’t.', '#B9A6FF', '#1C1430')}</h2></div>
<div>
<p class="k-p">My career started because a friend told me about an opportunity in a law lecture. One open door changed everything that came after it. Since 2020 I’ve tried to open doors for others: Digivention, Write to Win, and a career newsletter read by 900+ people.</p>
<p class="k-p">But some people need more than a newsletter. Many LGBTQ+ Nigerians are shut out of the networks, mentorship and fair hiring that careers depend on, and too often they have to choose between being safe and being seen. In 2025, I co-founded EmpowerQ with Alexandria to change that.</p>
<p class="k-p">We focus on what moves a career: jobs, skills, research that makes the case to employers, and a community where people don’t have to hide to get ahead.</p>
<p class="sig">— Jeremiah Ajayi, Executive Director and Co-Founder</p>
</div>
</div>
</section>

<section class="k-sec" style="background: #E9E2FF; color: #1C1430" aria-labelledby="build-t">
<div class="wrap">
<div class="k-head"><p class="eyebrow" style="color: #3B2C6E">What we’re building</p><h2 id="build-t" class="sg k-h2">Practical support at every step of {mark('a career.', '#B9A6FF')}</h2></div>
<div class="eqp-ll">
<article class="k-stk eqp-ll-c"><span class="k-tag" style="color: #FFC83D">Flagship · Social Shifters 2026 finalist</span><h3 class="sg k-h2" style="font-size: clamp(34px, 3.6vw, 54px)">Lavender Ladder</h3><p style="margin: 0; font-size: 16px; line-height: 1.6; color: #D6CCFF">An employment programme built for progression, not just placement. Participants get mentorship from working professionals, career coaching and a route into recruiter-ready talent pools with employers who want to hire inclusively.</p>
<figure class="k-fig"><video src="/_blob/040da4b995e99035dda7fe59d67b1464" poster="/_blob/326c0bfe0ddf15444f246261858a4af6" autoplay muted loop playsinline aria-label="A walkthrough of the Lavender Ladder app: the home screen, your ladder from Explore to Earn, opportunities, the Career Bestie AI coach, events and support"></video><figcaption style="text-align: center; color: #D6CCFF">The Lavender Ladder app, where participants track their next move</figcaption></figure></article>
<div class="eqp-progs"><sc-for list="{{{{programs}}}}" as="p" hint-placeholder-count="8"><a class="k-stk" href="{{{{p.href}}}}" style="color: #1C1430"><span class="k-kicker">{{{{p.kind}}}}</span><span class="sg k-h3" style="font-size: 21px">{{{{p.name}}}}</span><span style="font-size: 15px; line-height: 1.5">{{{{p.line}}}}</span></a></sc-for></div>
</div>
</div>
</section>

<section class="k-sec eqp-receipts" aria-labelledby="yr-t">
<div class="wrap">
<p class="eyebrow" style="color: #3B2C6E">Year one, in receipts</p>
<h2 id="yr-t" class="sg eqp-core">In year one, we proved the need. In year two, {mark('we build the ladder.')}</h2>
<div class="eqp-poster"><sc-for list="{{{{impact}}}}" as="m" hint-placeholder-count="9"><div class="eqp-n {{{{m.cls}}}}"><b class="sg">{{{{m.big}}}}</b><span>{{{{m.label}}}}</span></div></sc-for></div>
<p class="eqp-built"><b>Also built:</b> Nigeria’s first LGBTQ+ Workforce Report · Career Bestie, our AI career coach · Lavender Ladder · the Resource Vault · Out of Office, Nigeria’s first queer career conference · finalist, Social Shifters Global Innovation Challenge 2026</p>
<p class="eqp-next sg">Year two: more jobs. More income. More options<span class="k-dot">.</span></p>
<h3 class="eyebrow" style="color: #3B2C6E; margin: clamp(56px, 7vw, 88px) 0 0">The partners who chose to stand with us</h3>
<ul class="eqp-partners"><sc-for list="{{{{partners}}}}" as="l" hint-placeholder-count="12"><li><img src="{{{{l.src}}}}" alt="{{{{l.alt}}}}" loading="lazy"></li></sc-for></ul>
</div>
</section>

<section id="involved" class="k-sec k-cream" aria-labelledby="inv-t" style="padding-bottom: clamp(110px, 12vw, 170px)">
<div class="wrap">
<div class="k-head"><p class="eyebrow">Get involved</p><h2 id="inv-t" class="sg k-h2">There’s a door {mark('you can open.', '#B9A6FF')}</h2></div>
<div class="eqp-ways k-rot k-rot5"><sc-for list="{{{{ways}}}}" as="w" hint-placeholder-count="5"><a class="k-stk" href="{{{{w.href}}}}" style="color: #1C1430"><span class="sg k-h3">{{{{w.h}}}}</span><span style="font-size: 15.5px; line-height: 1.55">{{{{w.t}}}}</span><span class="k-go">{{{{w.cta}}}}</span></a></sc-for></div>
<p class="eqp-note">We protect our community’s privacy. We never share participants’ details, and photos only show people who have agreed to be shown. EmpowerQ is registered in Nigeria as Career Growth Initiative for the Disadvantaged.</p>
</div>
</section>

<section class="k-end eqp-end" aria-label="Get in touch with EmpowerQ">
<span class="shp shp-flower k-end-s" aria-hidden="true"></span>
<div class="wrap">
<h2 class="sg k-end-t">Want to open {mark('a door?', '#B9A6FF', '#1C1430')}</h2>
<div class="k-cta"><a class="eq-btn" style="background: #B9A6FF; color: #1C1430" href="mailto:info@empowerqueer.org?subject=Supporting%20EmpowerQ">Contact EmpowerQ ↗</a><a class="h-btn k-btn-line" href="https://www.empowerqueer.org">Visit EmpowerQ ↗</a><a class="h-btn k-btn-line" href="https://calendly.com/empowerqueer-info/30min">Book career office hours</a></div>
{footer_html()}
</div>
</section>
<!--NOEND-->
'''


CT_CSS = '''
<style>
.ctp{padding-top:clamp(40px,5vw,72px);padding-bottom:clamp(110px,12vw,170px);position:relative;overflow:hidden;isolation:isolate}
.ctp .ct-title{max-width:11ch}
.ctp-info{margin-top:clamp(36px,4vw,52px);display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;font-size:15px}
</style>'''


def contact():
    return f'''{CT_CSS}
<section class="ct ctp k-cream" aria-labelledby="ct-title">
{motif('signal')}
<div class="wrap">
<p class="eyebrow">Contact</p>
<h1 id="ct-title" class="sg ct-title">What are you {mark('working on?', '#FF5A2A', '#111')}</h1>
<p class="k-lede">Pick what fits and I’ll point you to the right next step. Most conversations start with a 30-minute call.</p>
<div class="ct-grid">
<div id="hiring" class="ct-doors" role="radiogroup" aria-label="What you need">
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
<p class="ctp-info"><span>Based in Lagos (UTC+1), working with teams in Europe, North America, the Middle East and Africa.</span><a class="h-link" href="https://www.linkedin.com/in/jeremiah-ajayi/">LinkedIn ↗</a><a class="h-link" href="Site-EmpowerQ.dc.html">Looking for EmpowerQ? {ARR}</a></p>
</div>
</section>
<!--NOBAND-->
'''
