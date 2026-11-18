"""Shared design kit for the inner pages, in the homepage's visual language.

The homepage stylesheet (home.CSS) is included on every inner page so its
components (.pc project cards, .qt sticker quotes, .xd discipline cards, the
Stears tabs, .tl timeline, .ct contact doors) can be reused as-is. KIT_CSS adds
the inner-page pieces: coloured heroes with rays, highlight marks, sticker
cards, steps, FAQs, chips, bars, and the closing band.
"""

import re

CAL = 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi'
MAIL = 'jeremiah@thejeremiahajayi.com'
ARR = '<span class="arr" aria-hidden="true">→</span>'

FOOT = [
    ('Positioning', 'Site-Service-Positioning.dc.html'),
    ('Launches & GTM', 'Site-Service-Launch.dc.html'),
    ('Content & storytelling', 'Site-Service-Content.dc.html'),
    ('Work', 'Site-Work.dc.html'),
    ('Writing', 'Site-Writing.dc.html'),
    ('About', 'Site-About.dc.html'),
    ('EmpowerQ', 'Site-EmpowerQ.dc.html'),
    ('Contact', 'Site-Contact.dc.html'),
    ('LinkedIn', 'https://www.linkedin.com/in/jeremiah-ajayi/'),
]


def mark(word, color=None, text=None, cls=''):
    """Emphasis without a highlighter: the words stay plain and the closing
    punctuation becomes the site's signature orange full stop."""
    m = re.match(r'^(.*?)([.?!]+)$', word, re.S)
    if m:
        return f'{m.group(1)}<span class="k-dot">{m.group(2)}</span>'
    return word


MOTIFS = {
    # Positioning: focus. Concentric rings around one orange point.
    'target': '''<svg class="mo-svg mo-target" viewBox="0 0 600 600"><g fill="none" stroke="currentColor" stroke-width="2"><circle cx="300" cy="300" r="280"/><circle cx="300" cy="300" r="220"/><circle cx="300" cy="300" r="160"/><circle cx="300" cy="300" r="100"/><circle cx="300" cy="300" r="46"/></g><circle class="mo-bull" cx="300" cy="300" r="16" fill="#FF5A2A"/></svg>''',
    # Launches: a flight path coming in to land on a runway.
    'flight': '''<svg class="mo-svg mo-flight" viewBox="0 0 900 500" preserveAspectRatio="xMaxYMid meet"><path class="mo-path" d="M20 60 C 300 20, 560 120, 760 380" fill="none" stroke="currentColor" stroke-width="3" stroke-dasharray="10 14"/><line x1="600" y1="430" x2="890" y2="430" stroke="currentColor" stroke-width="6" stroke-linecap="round"/><g stroke="currentColor" stroke-width="3" stroke-linecap="round" opacity=".6"><line x1="640" y1="452" x2="680" y2="452"/><line x1="720" y1="452" x2="760" y2="452"/><line x1="800" y1="452" x2="840" y2="452"/></g><circle cx="760" cy="380" r="12" fill="#111"/></svg>''',
    # Content: ripples that keep travelling outwards.
    'ripple': '''<div class="mo-ripple"><i></i><i></i><i></i><i></i><b></b></div>''',
    # Expertise: three disciplines, one practice.
    'venn': '''<svg class="mo-svg mo-venn" viewBox="0 0 600 560"><circle cx="220" cy="210" r="170" fill="#FFC83D"/><circle cx="380" cy="210" r="170" fill="#FF5A2A"/><circle cx="300" cy="350" r="170" fill="#8FE3B0"/></svg>''',
    # Work: evidence. Graph paper with a line that climbs.
    'proof': '''<div class="mo-grid"></div><svg class="mo-svg mo-proof" viewBox="0 0 800 420" preserveAspectRatio="xMaxYMax meet"><path class="mo-line" d="M10 400 L 140 360 L 250 372 L 360 300 L 470 280 L 580 190 L 690 150 L 790 30" fill="none" stroke="#FF5A2A" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/><circle cx="790" cy="30" r="10" fill="#FF5A2A"/></svg>''',
    # About: a route with turns, from law to marketing.
    'route': '''<svg class="mo-svg mo-route" viewBox="0 0 700 700"><path class="mo-path" d="M40 660 C 160 520, 40 420, 200 360 S 420 380, 420 240 S 600 120, 660 40" fill="none" stroke="currentColor" stroke-width="3" stroke-dasharray="8 14"/><circle cx="40" cy="660" r="10" fill="currentColor"/><circle cx="200" cy="360" r="10" fill="currentColor"/><circle cx="420" cy="240" r="10" fill="currentColor"/><circle cx="660" cy="40" r="14" fill="#FF5A2A"/></svg>''',
    # Writing: a ruled page with a margin line.
    'ruled': '''<div class="mo-ruled"></div>''',
    # EmpowerQ: doorways.
    'arches': '''<svg class="mo-svg mo-arches" viewBox="0 0 640 420" preserveAspectRatio="xMaxYMax meet"><g fill="none" stroke="currentColor" stroke-width="3"><path d="M20 420 V170 a80 80 0 0 1 160 0 V420"/><path d="M230 420 V120 a80 80 0 0 1 160 0 V420"/></g><path d="M440 420 V70 a80 80 0 0 1 160 0 V420 Z" fill="#E9E2FF"/><path d="M440 420 V70 a80 80 0 0 1 160 0 V420" fill="none" stroke="currentColor" stroke-width="3"/></svg>''',
    # Contact: a signal going out.
    'signal': '''<svg class="mo-svg mo-signal" viewBox="0 0 500 500"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path class="s1" d="M500 380 A 120 120 0 0 0 380 500"/><path class="s2" d="M500 260 A 240 240 0 0 0 260 500"/><path class="s3" d="M500 140 A 360 360 0 0 0 140 500"/><path class="s4" d="M500 20 A 480 480 0 0 0 20 500"/></g></svg>''',
}


def motif(name):
    """A background drawing chosen for what the page is about (the homepage keeps the sun)."""
    return f'<div class="k-motif m-{name}" aria-hidden="true">{MOTIFS[name]}</div>'


def footer_html():
    links = ''.join(f'<a href="{h}">{l}</a>' for l, h in FOOT)
    return (f'<footer class="k-foot"><a class="sg k-brand" href="Home-B2.dc.html"><span aria-hidden="true" class="ct-mark">JA</span>Jeremiah Ajayi</a>'
            f'<span class="k-fnav">{links}<span>Lagos 🇳🇬 · {{{{time}}}} · © 2026</span></span></footer>')


def end_band(title_html, sub='', buttons=None):
    if buttons is None:
        buttons = (f'<a class="btn-o h-btn" href="{CAL}">Book a call <span class="arr" aria-hidden="true">↗</span></a>'
                   f'<a class="h-btn k-btn-line" href="mailto:{MAIL}">{MAIL}</a>'
                   f'<a class="h-btn k-btn-line" href="https://www.linkedin.com/in/jeremiah-ajayi/">LinkedIn <span aria-hidden="true">↗</span></a>')
    s = f'<p class="k-end-sub">{sub}</p>' if sub else ''
    return f'''<section id="contact" class="k-end" aria-label="Next step">
<span class="shp shp-flower k-end-s" aria-hidden="true"></span>
<div class="wrap">
<h2 class="sg k-end-t">{title_html}</h2>
{s}
<div class="k-cta">{buttons}</div>
{footer_html()}
</div>
</section>'''


def footer_band():
    return f'''<section class="k-end k-end-min" aria-label="Footer"><div class="wrap">{footer_html()}</div></section>'''


KIT_CSS = r'''
/*kit:start*/
html{scroll-padding-top:84px}
.k-cream{background:#FFF5D9;color:#111}.k-sun{background:#FFC83D;color:#111}.k-orange{background:#FF5A2A;color:#111}
.k-night{background:#0E2A2E;color:#EAF6F1}.k-ink{background:#111;color:#F2EFE8}.k-paper{background:#F2EFE8;color:#111}
.k-mint{background:#8FE3B0;color:#0E2A2E}.k-lav{background:#B9A6FF;color:#1C1430}.k-plum{background:#1C1430;color:#E9E2FF}
.k-white{background:#FFFDF6;color:#111}.k-blush{background:#FF8FB6;color:#111}
.k-night .eyebrow,.k-ink .eyebrow,.k-plum .eyebrow{color:#9DB8B0}
.k-ink .eyebrow{color:#8A867E}.k-plum .eyebrow{color:#B9A6FF}
.k-orange .eyebrow,.k-sun .eyebrow,.k-mint .eyebrow,.k-lav .eyebrow,.k-blush .eyebrow{color:rgba(17,17,17,.72)}
/* heroes */
.k-hero{position:relative;overflow:hidden;isolation:isolate;padding:clamp(36px,4.6vw,68px) 0 clamp(64px,7vw,108px)}
.k-rays{position:absolute;right:-14vw;top:-34vw;width:88vw;height:88vw;color:var(--rc,#FFC83D);opacity:var(--ro,.5);z-index:-1;background:repeating-conic-gradient(from 0deg at 50% 50%,currentColor 0 4deg,transparent 4deg 11deg);-webkit-mask:radial-gradient(closest-side,#000 40%,transparent 100%);mask:radial-gradient(closest-side,#000 40%,transparent 100%);animation:spin 160s linear infinite}
.k-shape{position:absolute;z-index:-1;animation:spin 60s linear infinite}
.k-crumb{margin:0 0 22px;font-size:14px;font-weight:600;opacity:.8}
.k-crumb a{color:inherit;text-decoration:underline;text-underline-offset:4px;text-decoration-color:rgba(127,127,127,.5)}
.k-hero-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(32px,5vw,80px);align-items:center}
.k-h1{margin:0;font-weight:700;font-size:clamp(46px,6.4vw,104px);line-height:.94;letter-spacing:-.055em;max-width:15ch}
.k-h1-s{font-size:clamp(40px,5vw,80px);max-width:17ch}
.k-mark{display:inline;padding:0 .1em;border-radius:.14em;color:var(--mkt,inherit);background:linear-gradient(var(--mk,#FFC83D),var(--mk,#FFC83D)) no-repeat 0 92%/0% 86%;-webkit-box-decoration-break:clone;box-decoration-break:clone;animation:kmk .8s .35s cubic-bezier(.7,0,.2,1) forwards}
.k-ink{display:none}
.k-mt{color:var(--mkt,inherit)}
@keyframes kmk{to{background-size:100% 86%}}
.k-lede{margin:clamp(20px,2.4vw,30px) 0 0;max-width:52ch;font-size:19px;line-height:1.6;opacity:.92}
.k-cta{margin-top:28px;display:flex;flex-wrap:wrap;gap:12px 14px;align-items:center}
.k-btn-line{border:1.5px solid currentColor;color:inherit;transition:background .25s,color .25s}
.k-btn-line:hover{background:#F2EFE8;color:#111;border-color:#F2EFE8}
.k-paper .k-btn-line:hover,.k-cream .k-btn-line:hover,.k-sun .k-btn-line:hover,.k-mint .k-btn-line:hover,.k-orange .k-btn-line:hover,.k-lav .k-btn-line:hover{background:#111;color:#F2EFE8;border-color:#111}
.k-btn-paper{background:#F2EFE8;color:#111;box-shadow:3px 3px 0 #FF5A2A;transition:transform .2s,box-shadow .2s}
.k-btn-paper:hover{color:#111;transform:translate(-2px,-2px);box-shadow:5px 5px 0 #FF5A2A}
/* stat stickers row in heroes */
.k-stats{margin-top:clamp(36px,4.4vw,56px);display:flex;flex-wrap:wrap;gap:14px}
.k-stat{flex:1 1 200px;padding:16px 18px 18px;border:1.5px solid #111;border-radius:18px;background:#FFFDF6;color:#111;box-shadow:4px 4px 0 #111}
.k-stat b{display:block;font:700 clamp(36px,3.6vw,56px)/.9 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.055em}
.k-stat span{display:block;margin-top:8px;font-size:14px;line-height:1.4;color:#45423C}
.k-stat:nth-child(4n+1){transform:rotate(-1deg)}.k-stat:nth-child(4n+2){background:#8FE3B0;transform:rotate(.8deg)}.k-stat:nth-child(4n+3){background:#FF8FB6;transform:rotate(-.6deg)}.k-stat:nth-child(4n+4){background:#FFC83D;transform:rotate(1deg)}
/* sections */
.k-sec{position:relative;padding:clamp(72px,9vw,128px) 0}
.k-sec-t{padding-top:clamp(48px,6vw,80px)}
.k-h2{margin:0;font-weight:700;font-size:clamp(36px,4.4vw,68px);line-height:.98;letter-spacing:-.05em;max-width:18ch}
.k-h3{margin:0;font-weight:700;font-size:clamp(24px,2.2vw,32px);line-height:1.08;letter-spacing:-.035em}
.k-head{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:14px 48px;align-items:end;margin-bottom:clamp(32px,4vw,56px)}
.k-head .eyebrow{grid-column:1/-1;margin:0}
.k-sum{margin:0;font-size:17px;line-height:1.6;opacity:.82;max-width:46ch}
.k-p{font-size:18px;line-height:1.65;max-width:62ch}
.k-p+.k-p{margin-top:14px}
.k-g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(18px,2vw,28px)}
.k-g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,1.8vw,24px)}
.k-g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(14px,1.6vw,20px)}
.k-split{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(32px,5vw,80px);align-items:start}
.k-split-r{grid-template-columns:minmax(0,7fr) minmax(0,5fr)}
/* sticker cards */
.k-stk{position:relative;display:flex;flex-direction:column;gap:10px;padding:clamp(22px,2.4vw,32px);border:1.5px solid #111;border-radius:22px;background:#FFFDF6;color:#111;box-shadow:5px 5px 0 #111;text-decoration:none;transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s}
a.k-stk:hover{color:#111;transform:translate(-2px,-4px);box-shadow:7px 9px 0 #111}
a.k-stk:hover .arr{transform:translateX(4px)}
.k-stk>*{flex-shrink:0}
.k-stk.s-sun{background:#FFC83D}.k-stk.s-mint{background:#8FE3B0}.k-stk.s-blush{background:#FF8FB6}.k-stk.s-lav{background:#B9A6FF}.k-stk.s-orange{background:#FF5A2A}.k-stk.s-cream{background:#FFF5D9}
.k-stk.s-ink{background:#111;color:#F2EFE8}.k-stk.s-night{background:#0E2A2E;color:#EAF6F1}.k-stk.s-plum{background:#1C1430;color:#E9E2FF}
a.k-stk.s-ink:hover,a.k-stk.s-night:hover,a.k-stk.s-plum:hover{color:#F2EFE8}
.k-ink .k-stk,.k-night .k-stk,.k-plum .k-stk{border-color:#111}
.k-rot>*:nth-child(odd){transform:rotate(-.8deg)}.k-rot>*:nth-child(even){transform:rotate(.7deg)}
.k-rot>a:hover{transform:translate(-2px,-4px) rotate(0)}
.k-rot5>*:nth-child(5n+1){background:#FFC83D}.k-rot5>*:nth-child(5n+2){background:#8FE3B0}.k-rot5>*:nth-child(5n+3){background:#FF8FB6}.k-rot5>*:nth-child(5n+4){background:#B9A6FF}.k-rot5>*:nth-child(5n+5){background:#FFFDF6}
.k-tag{align-self:flex-start;display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;border:1.5px solid currentColor;font-size:12.5px;font-weight:700}
.k-kicker{font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;opacity:.72}
.k-big{font:700 clamp(48px,5vw,80px)/.88 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.06em}
.k-go{margin-top:auto;padding-top:10px;display:inline-flex;gap:8px;align-items:center;font-weight:700;font-size:15px}
.k-emo{display:grid;place-items:center;width:58px;height:58px;position:relative;margin-bottom:6px}
.k-emo .shp{position:absolute;inset:0}
.k-emo i{position:relative;font-style:normal;font-size:26px}
/* lists */
.k-list{margin:0;padding:0;list-style:none;display:grid;gap:12px}
.k-list li{display:grid;grid-template-columns:30px 1fr;gap:10px;font-size:17px;line-height:1.5}
.k-list li::before{content:"✓";display:grid;place-items:center;width:26px;height:26px;border-radius:50%;background:#111;color:#8FE3B0;font-size:13px;font-weight:700}
.k-list.k-x li::before{content:"✕";color:#FF8FB6}
.k-list.k-dot li::before{content:"";width:12px;height:12px;margin:7px 0 0 7px;background:#FF5A2A}
.k-num{margin:0;padding:0;list-style:none;counter-reset:n;display:grid;gap:0;border-top:2px solid currentColor}
.k-num li{counter-increment:n;display:grid;grid-template-columns:56px minmax(0,1fr);gap:12px;padding:18px 0;border-bottom:1px solid rgba(127,127,127,.35)}
.k-num li::before{content:counter(n,decimal-leading-zero);font:700 15px/1.6 'Space Grotesk',system-ui,sans-serif;color:#FF5A2A}
.k-num b{display:block;font:700 20px/1.25 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em}
.k-num span{display:block;margin-top:4px;font-size:16px;line-height:1.55;opacity:.85}
.k-num li>span:only-child{margin:0;font-size:17px;opacity:1}
/* steps */
.k-steps{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;position:relative}
.k-steps li{position:relative;display:flex;flex-direction:column;gap:8px;padding-top:68px}
.k-steps li::before{content:attr(data-n);position:absolute;left:0;top:0;display:grid;place-items:center;width:52px;height:52px;border-radius:50%;border:1.5px solid #111;background:#FFC83D;color:#111;font:700 20px 'Space Grotesk',system-ui,sans-serif;box-shadow:3px 3px 0 #111;z-index:1}
.k-steps li:nth-child(2)::before{background:#FF5A2A}.k-steps li:nth-child(3)::before{background:#8FE3B0}.k-steps li:nth-child(4)::before{background:#FF8FB6}
.k-steps li::after{content:"";position:absolute;left:52px;right:-16px;top:26px;border-top:2px dashed currentColor;opacity:.35}
.k-steps li:last-child::after{display:none}
.k-steps b{font:700 22px/1.15 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.025em}
.k-steps span{font-size:16px;line-height:1.55;opacity:.85;max-width:30ch}
/* faq */
.k-faq{border-top:2px solid currentColor}
.k-faq details{border-bottom:1px solid rgba(127,127,127,.35)}
.k-faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:22px 0;font:700 clamp(19px,1.7vw,23px)/1.3 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em}
.k-faq summary::-webkit-details-marker{display:none}
.k-faq summary i{flex:none;display:grid;place-items:center;width:36px;height:36px;border-radius:50%;border:1.5px solid currentColor;font-style:normal;font-size:20px;transition:transform .3s,background .3s,color .3s}
.k-faq details[open] summary i{transform:rotate(45deg);background:#FF5A2A;color:#111;border-color:#FF5A2A}
.k-faq details p{margin:0 0 22px;max-width:66ch;font-size:17px;line-height:1.65;opacity:.88}
/* chips */
.k-chips{display:flex;flex-wrap:wrap;gap:8px}
.k-chip{min-height:42px;padding:0 16px;border-radius:999px;border:1.5px solid #111;background:#FFFDF6;color:#111;font:700 14px 'DM Sans',system-ui,sans-serif;cursor:pointer;transition:background .25s,color .25s,transform .2s}
.k-chip span{opacity:.6;font-weight:600;margin-left:4px}
.k-chip:hover{transform:translateY(-2px)}
.k-chip[aria-pressed="true"]{background:#111;color:#FFF5D9;box-shadow:3px 3px 0 #FF5A2A}
.k-pills{display:flex;flex-wrap:wrap;gap:8px}
.k-pills>*{padding:7px 13px;border-radius:999px;border:1.5px solid #111;font-size:14px;font-weight:700;background:#FFFDF6;color:#111}
.k-pills>*:nth-child(5n+1){background:#FFC83D}.k-pills>*:nth-child(5n+2){background:#8FE3B0}.k-pills>*:nth-child(5n+3){background:#FF8FB6}.k-pills>*:nth-child(5n+4){background:#B9A6FF}
/* media */
.k-shot{display:block;width:100%;height:auto;border-radius:12px;border:1.5px solid #111;background:#fff;box-shadow:0 22px 48px rgba(0,0,0,.18)}
.k-fig{margin:0}
.k-fig figcaption{margin-top:10px;font-size:13.5px;line-height:1.45;opacity:.78}
.k-fan{position:relative}
.k-fan img{position:absolute;border-radius:12px;border:1.5px solid #111;background:#fff;box-shadow:0 22px 48px rgba(0,0,0,.22);transition:transform .7s cubic-bezier(.2,.8,.2,1)}
.k-arch img{border-radius:220px 220px 24px 24px}
.k-badge{position:absolute;display:grid;place-items:center;text-align:center;border-radius:50%;font:700 14px/1.1 'Space Grotesk',system-ui,sans-serif;transform:rotate(-10deg);box-shadow:4px 4px 0 #111;border:1.5px solid #111}
/* marquee of real work */
.k-wall{overflow:hidden;padding:6px 0 18px}
.k-wall-t{display:flex;gap:16px;width:max-content;animation:logos 70s linear infinite}
.k-wall:hover .k-wall-t{animation-play-state:paused}
.k-wall-t img{height:clamp(150px,15vw,210px);width:auto;border-radius:14px;border:1.5px solid #111;background:#fff;flex:none}
.k-wall-t img:nth-child(odd){transform:rotate(-1.5deg)}.k-wall-t img:nth-child(even){transform:rotate(1.5deg) translateY(10px)}
/* horizontal scroller */
.k-hs{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:8px 4px 22px;scrollbar-width:thin}
.k-hs figure{flex:none;scroll-snap-align:start;margin:0;width:min(420px,78vw)}
.k-hs img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:14px;border:1.5px solid #111;background:#fff}
.k-hs figcaption{margin-top:10px;display:flex;justify-content:space-between;gap:10px;font-size:14px}
/* bars */
.k-bars{display:grid;gap:14px}
.k-bar{display:grid;gap:6px}
.k-bar>div:first-child{display:flex;justify-content:space-between;font-size:14px;font-weight:600}
.k-bar>div:first-child b{font:700 26px/1 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.04em}
.k-bar-t{height:16px;border-radius:99px;background:rgba(127,127,127,.25);overflow:hidden;border:1.5px solid #111}
.k-bar-f{height:100%;width:var(--w);background:var(--c,#FF5A2A);border-radius:99px;transform-origin:left;transform:scaleX(0);transition:transform 1.4s cubic-bezier(.2,.8,.2,1)}
[data-inview].in .k-bar-f{transform:scaleX(1)}
/* case sections on the Work page */
.k-case{position:relative;padding:clamp(72px,9vw,128px) 0;overflow:hidden}
.k-cmeta{margin:0 0 20px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;font-size:14px;font-weight:700}
.k-cmeta .k-cn{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;border:1.5px solid currentColor;font:700 15px 'Space Grotesk',system-ui,sans-serif}
.k-cmeta a{color:inherit;margin-left:auto;text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:2px;text-decoration-color:#FF5A2A}
.k-ct{margin:0;font-weight:700;font-size:clamp(40px,5.6vw,92px);line-height:.94;letter-spacing:-.055em;max-width:16ch}
.k-quote{margin:0;padding:clamp(24px,3vw,40px);border:1.5px solid #111;border-radius:24px;background:#FFFDF6;color:#111;box-shadow:6px 6px 0 #111;transform:rotate(-1deg)}
.k-quote blockquote{margin:0;font:600 clamp(22px,2.4vw,34px)/1.18 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.025em}
.k-quote figcaption{margin-top:16px;font-size:14.5px}
.k-chat{display:flex;flex-direction:column;gap:10px}
.k-chat li{list-style:none;align-self:flex-start;max-width:92%;padding:12px 16px;border-radius:18px 18px 18px 4px;border:1.5px solid #111;background:#FFFDF6;color:#111;font-size:15px;line-height:1.4;box-shadow:3px 3px 0 #111}
.k-chat li:nth-child(even){align-self:flex-end;border-radius:18px 18px 4px 18px;background:#111;color:#FFF5D9;box-shadow:3px 3px 0 #FF5A2A}
.k-hub{display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center}
.k-hub-c{padding:14px 22px;border-radius:999px;border:1.5px solid #111;background:#111;color:#8FE3B0;font:700 20px 'Space Grotesk',system-ui,sans-serif;box-shadow:4px 4px 0 #FFFDF6}
.k-hub-c small{display:block;font:600 12.5px 'DM Sans',system-ui,sans-serif;color:#EAF6F1;opacity:.8}
.k-hub-l{width:2px;height:28px;border-left:2px dashed currentColor;opacity:.5}
/* closing band */
.k-end{position:relative;z-index:1;overflow:hidden;background:#111;color:#F2EFE8;padding:clamp(80px,10vw,140px) 0 clamp(32px,4vw,48px);border-radius:clamp(24px,3.4vw,48px) clamp(24px,3.4vw,48px) 0 0;margin-top:-34px}
.k-end-min{padding-top:clamp(40px,5vw,60px)}
.k-end-s{position:absolute;right:-90px;top:-90px;width:300px;height:300px;background:#FF5A2A;animation:spin 60s linear infinite;opacity:.95}
.k-end-t{position:relative;margin:0;font-weight:700;font-size:clamp(48px,7.4vw,124px);line-height:.92;letter-spacing:-.06em;max-width:13ch}
.k-end-sub{margin:20px 0 0;max-width:52ch;font-size:18px;line-height:1.6;color:#C9C4BA}
.k-end .k-cta{margin-top:clamp(28px,3.4vw,44px)}
.k-foot{margin-top:clamp(64px,9vw,120px);padding-top:22px;border-top:1px solid #2E2D2A;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px;font-size:14px;color:#8A867E}
.k-end-min .k-foot{margin-top:0}
.k-brand{display:inline-flex;align-items:center;gap:10px;font-size:18px;font-weight:700;letter-spacing:-.04em;color:#F2EFE8;text-decoration:none}
.k-brand:hover{color:#F2EFE8}
.k-fnav{display:flex;flex-wrap:wrap;gap:8px 20px}
.k-fnav a{color:#B5B0A6;text-decoration:none}
.k-fnav a:hover{color:#FF5A2A}
/* responsive */
@media (max-width: 1080px){
.k-hero-g,.k-head,.k-split,.k-split-r{grid-template-columns:1fr}
.k-g4{grid-template-columns:repeat(2,minmax(0,1fr))}
.k-g3{grid-template-columns:1fr}
.k-steps{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:28px}
.k-steps li:nth-child(2)::after{display:none}
}
@media (max-width: 640px){
.k-g2,.k-g4{grid-template-columns:1fr}
.k-steps{grid-template-columns:1fr}
.k-steps li::after{display:none}
.k-h1{font-size:clamp(42px,12vw,64px)}
.k-lede,.k-p{font-size:17px}
.k-stat{flex-basis:100%}
.k-rot>*{transform:none !important}
.k-end-s{width:180px;height:180px;right:-60px;top:-60px}
.k-cmeta a{margin-left:0}
}
@media (prefers-reduced-motion: reduce){
.k-rays,.k-shape,.k-end-s,.k-wall-t{animation:none !important}
.k-mark{animation:none;background-size:100% 86%}
.k-wall-t{flex-wrap:wrap;width:auto}
.k-bar-f{transform:none;transition:none}
.k-stk,.k-fan img{transition:none}
}

/* emphasis: the orange full stop */
.k-dot{color:var(--dot,#FF5A2A)}
.k-orange{--dot:#111}
/* page motifs */
.k-motif{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden}
.mo-svg{position:absolute;display:block}
.m-target{color:rgba(17,17,17,.14)}
.mo-target{right:-6vw;top:50%;width:min(62vw,820px);transform:translateY(-50%)}
.mo-bull{transform-origin:300px 300px;animation:bull 3.2s ease-in-out infinite}
@keyframes bull{50%{transform:scale(1.35)}}
.m-flight{color:rgba(17,17,17,.3)}
.mo-flight{right:0;bottom:4%;width:min(70vw,980px)}
.mo-path{animation:dash 30s linear infinite}
@keyframes dash{to{stroke-dashoffset:-480}}
.mo-ripple{position:absolute;right:8%;top:22%;width:2px;height:2px}
.mo-ripple i{position:absolute;left:50%;top:50%;width:620px;height:620px;margin:-310px 0 0 -310px;border-radius:50%;border:2px solid #8FE3B0;opacity:0;animation:ripple 9s cubic-bezier(.2,.6,.4,1) infinite}
.mo-ripple i:nth-child(2){animation-delay:2.25s}.mo-ripple i:nth-child(3){animation-delay:4.5s}.mo-ripple i:nth-child(4){animation-delay:6.75s}
.mo-ripple b{position:absolute;left:-9px;top:-9px;width:18px;height:18px;border-radius:50%;background:#8FE3B0}
@keyframes ripple{0%{transform:scale(.05);opacity:.55}100%{transform:scale(1.4);opacity:0}}
.mo-venn{right:-4vw;top:-6%;width:min(52vw,700px);opacity:.16;mix-blend-mode:screen;animation:spin 120s linear infinite}
.mo-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(17,17,17,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(17,17,17,.06) 1px,transparent 1px);background-size:44px 44px;-webkit-mask:linear-gradient(100deg,transparent 30%,#000 75%);mask:linear-gradient(100deg,transparent 30%,#000 75%)}
.mo-proof{right:2%;bottom:6%;width:min(56vw,760px);opacity:.35}
.mo-line{stroke-dasharray:1400;stroke-dashoffset:1400;animation:draw 2.4s .4s cubic-bezier(.5,0,.2,1) forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.m-route{color:rgba(255,143,182,.55)}
.mo-route{right:-2vw;top:-4%;width:min(56vw,760px)}
.mo-ruled{position:absolute;inset:0;background:linear-gradient(90deg,transparent calc(100% - 46vw),rgba(255,90,42,.35) calc(100% - 46vw),rgba(255,90,42,.35) calc(100% - 46vw + 2px),transparent calc(100% - 46vw + 2px)),repeating-linear-gradient(180deg,transparent 0 37px,rgba(17,17,17,.08) 37px 38px)}
.m-arches{color:rgba(28,20,48,.32)}
.mo-arches{right:2%;bottom:0;width:min(46vw,620px)}
.m-signal{color:rgba(255,90,42,.45)}
.mo-signal{right:0;top:0;width:min(46vw,560px);transform:scaleY(-1)}
.mo-signal path{animation:sig 3.6s ease-in-out infinite}
.mo-signal .s2{animation-delay:.3s}.mo-signal .s3{animation-delay:.6s}.mo-signal .s4{animation-delay:.9s}
@keyframes sig{0%,100%{opacity:.25}40%{opacity:1}}
@media (max-width:640px){.mo-target{width:120vw;right:-50vw;opacity:.7}.mo-flight{width:150vw;right:-30vw;bottom:0}.mo-ripple{right:12%;top:12%}.mo-venn{width:110vw;right:-40vw}.mo-proof,.mo-route,.mo-arches{opacity:.5}.mo-ruled{opacity:.6}}
@media (prefers-reduced-motion: reduce){.mo-bull,.mo-path,.mo-ripple i,.mo-venn,.mo-signal path{animation:none !important}.mo-ripple i{opacity:.2;transform:scale(.6)}.mo-ripple i:nth-child(2){transform:scale(.9)}.mo-line{animation:none;stroke-dashoffset:0}}
/*kit:end*/
'''
