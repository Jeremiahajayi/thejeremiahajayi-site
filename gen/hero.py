#!/usr/bin/env python3
"""Homepage hero: "the edit" animation. Jargon fills the hero, gets struck
through, falls away, and the headline arrives with each verb acting out its
meaning. Pure CSS so it plays in the design canvas and on the live site;
client.js adds replay and once-per-session behaviour."""
import pathlib, random, re

JARGON = [
    'all-in-one platform', 'AI-powered', 'seamless', 'next-gen', 'robust', 'synergy',
    'best-in-class', 'innovative solution', 'cutting-edge', 'frictionless', 'scalable',
    'revolutionary', 'end-to-end', 'game-changing', 'leverage', 'world-class',
    'holistic', 'streamline', 'unlock value', 'disruptive', 'paradigm shift', 'turnkey',
]

def words():
    """Place jargon without overlaps, on a stage of roughly 760 x 400 px."""
    rnd = random.Random(11)
    W, H = 760.0, 400.0
    boxes, out = [(0, 0, 330, 26)], []   # reserve the caption
    for i, w in enumerate(JARGON):
        for attempt in range(400):
            size = rnd.choice([16, 19, 22, 26, 30, 34] if attempt < 200 else [16, 19])
            bw, bh = len(w) * size * 0.56 + 14, size * 1.5
            x, y = rnd.uniform(0, W - bw), rnd.uniform(34, H - bh)
            if all(x + bw < bx or bx + bww < x or y + bh < by or by + bhh < y for bx, by, bww, bhh in boxes):
                boxes.append((x, y, bw, bh)); break
        rot = rnd.uniform(-7, 7)
        din = 0.08 + i * 0.045
        strike = 1.25 + rnd.uniform(0, 0.45)
        fall = 2.0 + rnd.uniform(0, 0.35)
        spin = rot + rnd.choice([-1, 1]) * rnd.uniform(25, 70)
        fy = rnd.uniform(260, 420)
        out.append(
            f'<span style="--x: {x / W * 100:.1f}%; --y: {y / H * 100:.1f}%; --s: {size}px; --r: {rot:.1f}deg; '
            f'--d: {din:.2f}s; --k: {strike:.2f}s; --o: {fall:.2f}s; --sp: {spin:.0f}deg; --fy: {fy:.0f}px">{w}</span>'
        )
    return '\n'.join(out)

CSS = r"""
/*hero:start*/
.jg{display:none}
.hero-anim .jg{display:block;position:absolute;inset:0 -2% -4% 0;pointer-events:none;z-index:3}
.jg span{position:absolute;left:var(--x);top:var(--y);font-family:'DM Sans',system-ui,sans-serif;font-size:var(--s);font-weight:600;letter-spacing:-.02em;line-height:1;white-space:nowrap;color:#8A867E;transform:rotate(var(--r));opacity:0;animation:jg-in .45s var(--d) cubic-bezier(.2,.8,.2,1) both,jg-fall 1s var(--o) cubic-bezier(.55,0,.85,.35) forwards}
.jg span::after{content:"";position:absolute;left:-4%;right:-4%;top:54%;height:max(2px,.1em);border-radius:2px;background:#FF5A2A;transform:scaleX(0);transform-origin:left center;animation:jg-strike .3s var(--k) cubic-bezier(.6,0,.2,1) forwards}
.jg .jg-cap{left:0;top:0;font-size:14px;font-weight:700;letter-spacing:.02em;text-transform:uppercase;color:#B5B0A6;transform:none;--r:0deg;--d:0s;--k:1.15s;--o:1.95s;--sp:-8deg;--fy:300px}
@keyframes jg-in{from{opacity:0;transform:translateY(16px) rotate(var(--r)) scale(.9)}to{opacity:1;transform:rotate(var(--r))}}
@keyframes jg-strike{to{transform:scaleX(1)}}
@keyframes jg-fall{from{opacity:1;transform:rotate(var(--r))}to{opacity:0;transform:translateY(var(--fy)) rotate(var(--sp))}}
.hl-mute{color:#6B675F}
.v-dot{color:#FF5A2A}
.v-clear,.v-land,.v-travel{display:inline-block}
.hero-anim .l1{animation-delay:2.15s}
.hero-anim .l2{animation-delay:2.4s}
.hero-anim .l3{animation-delay:2.65s}
.hero-anim .v-clear{animation:v-clear 1.2s 2.3s cubic-bezier(.2,.8,.2,1) both}
.hero-anim .v-land{animation:v-land 1s 2.6s cubic-bezier(.3,0,.3,1) both}
.hero-anim .v-travel{animation:v-travel 1.2s 2.85s cubic-bezier(.16,1,.3,1) both}
@keyframes v-clear{from{opacity:0;filter:blur(18px)}40%{opacity:1}to{opacity:1;filter:blur(0)}}
@keyframes v-land{0%{opacity:0;transform:translateY(-150%)}55%{opacity:1;transform:translateY(7%)}72%{transform:translateY(-5%)}86%{transform:translateY(2%)}100%{opacity:1;transform:none}}
@keyframes v-travel{from{opacity:0;transform:translateX(70vw) skewX(-12deg);filter:blur(4px)}70%{filter:blur(0)}to{opacity:1;transform:none;filter:none}}
.jg-replay{display:none;align-items:center;gap:8px;margin-top:18px;padding:6px 12px 6px 10px;border:1px solid #3A3934;border-radius:999px;background:none;color:#B5B0A6;font:600 13px 'DM Sans',system-ui,sans-serif;cursor:pointer;transition:color .25s,border-color .25s}
.jg-replay:hover{color:#F2EFE8;border-color:#F2EFE8}
.js-on .jg-replay{display:inline-flex}
/* returning visitors in the same session: no replay of the intro */
.jg-skip .hero-anim .jg{display:none}
.jg-skip .hero-anim .l1,.jg-skip .hero-anim .l2,.jg-skip .hero-anim .l3{animation-delay:0s}
.jg-skip .hero-anim .v-clear,.jg-skip .hero-anim .v-land,.jg-skip .hero-anim .v-travel{animation:none}
@media (max-width: 640px){.jg span:nth-child(n+16){display:none}.jg span{font-size:calc(var(--s) * .62)}.jg .jg-cap{font-size:12px}}
@media (prefers-reduced-motion: reduce){.hero-anim .jg{display:none}.hero-anim .l1,.hero-anim .l2,.hero-anim .l3,.hero-anim .v-clear,.hero-anim .v-land,.hero-anim .v-travel{animation:none !important;opacity:1;filter:none;transform:none}.jg-replay{display:none !important}}
.lt-wrap{overflow:hidden}
.logo-track{margin:0;padding:0;list-style:none;display:flex;align-items:center;width:max-content;animation:logos 30s linear infinite}
.lt-wrap:hover .logo-track{animation-play-state:paused}
.logo-track li{flex:none;display:flex;align-items:center;justify-content:center;height:64px;padding:0 clamp(26px,3.6vw,48px)}
.logo-i{transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.logo-i:hover{transform:scale(1.08)}
@keyframes logos{to{transform:translateX(-50%)}}
@media (max-width: 640px){.logo-track{animation-duration:22s}.logo-track li{height:52px;padding:0 22px}.logo-i{max-height:40px}}
@media (prefers-reduced-motion: reduce){.logo-track{animation:none;flex-wrap:wrap;justify-content:center;width:auto;row-gap:16px}.logo-track li[aria-hidden="true"]{display:none}}
/* verb emojis: rest state (also what the canvas and returning visitors see) */
.v-clear,.v-land,.v-travel{position:relative;margin-right:.62em}
.ve{position:absolute;display:inline-block;font-size:.4em;line-height:1;letter-spacing:0;pointer-events:none;font-family:'Apple Color Emoji','Segoe UI Emoji','Noto Color Emoji',sans-serif}
.ve-lens{left:0;top:.35em;opacity:0}
.ve-spark{right:-.95em;top:-.05em;animation:twinkle 3.2s 1s ease-in-out infinite}
.ve-rocket{right:-1em;top:.32em;transform:rotate(-45deg);animation:hover 3s 1s ease-in-out infinite}
.ve-puff{right:-1.55em;top:1.1em;font-size:.26em;opacity:0}
.ve-plane{right:-1.05em;top:.1em;animation:bob 3.4s 1s ease-in-out infinite}
.ve-trail{right:.1em;top:.36em;height:0;width:3.5em;border-top:3px dashed #6B675F;opacity:0}
@keyframes twinkle{0%,100%{transform:scale(1) rotate(0)}50%{transform:scale(1.25) rotate(14deg)}}
@keyframes hover{0%,100%{transform:rotate(-45deg) translateY(0)}50%{transform:rotate(-45deg) translateY(-6%)}}
@keyframes bob{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-10%) rotate(-4deg)}}
/* the intro: each emoji acts out its verb */
.hero-anim .ve-lens{animation:lens 1.3s 2.2s cubic-bezier(.45,0,.3,1) both}
.hero-anim .ve-spark{animation:pop .5s 3.35s cubic-bezier(.3,1.6,.5,1) both,twinkle 3.2s 4.2s ease-in-out infinite}
.hero-anim .ve-rocket{animation:touchdown 1.05s 2.55s cubic-bezier(.2,.7,.3,1) both,hover 3s 4.2s ease-in-out infinite}
.hero-anim .ve-puff{animation:puff .9s 3.45s ease-out both}
.hero-anim .ve-plane{animation:fly 1.5s 2.75s cubic-bezier(.25,.8,.3,1) both,bob 3.4s 4.4s ease-in-out infinite}
.hero-anim .ve-trail{animation:trail 1.9s 2.85s ease-out both}
@keyframes lens{0%{opacity:0;transform:translateX(-.8em) rotate(-10deg)}15%{opacity:1}80%{opacity:1;transform:translateX(5.6em) rotate(10deg)}100%{opacity:0;transform:translateX(6.6em) rotate(10deg) scale(.6)}}
@keyframes pop{from{opacity:0;transform:scale(0) rotate(-40deg)}to{opacity:1;transform:none}}
@keyframes touchdown{0%{opacity:0;transform:rotate(-45deg) translateY(-4em)}70%{opacity:1;transform:rotate(-45deg) translateY(.12em)}85%{transform:rotate(-45deg) translateY(-.06em)}100%{opacity:1;transform:rotate(-45deg)}}
@keyframes puff{0%{opacity:0;transform:translateX(0) scale(.6)}30%{opacity:.9}100%{opacity:0;transform:translateX(.9em) scale(1.4)}}
@keyframes fly{0%{opacity:0;transform:translate(-12em,1.2em) rotate(8deg)}20%{opacity:1}100%{opacity:1;transform:none}}
@keyframes trail{0%{opacity:0;clip-path:inset(0 100% 0 0)}25%{opacity:.7}60%{opacity:.7;clip-path:inset(0 0 0 0)}100%{opacity:0;clip-path:inset(0 0 0 0)}}
.jg-skip .hero-anim .ve-lens,.jg-skip .hero-anim .ve-puff,.jg-skip .hero-anim .ve-trail{animation:none;opacity:0}
.jg-skip .hero-anim .ve-spark{animation:twinkle 3.2s 1s ease-in-out infinite}
.jg-skip .hero-anim .ve-rocket{animation:hover 3s 1s ease-in-out infinite}
.jg-skip .hero-anim .ve-plane{animation:bob 3.4s 1s ease-in-out infinite}
@media (prefers-reduced-motion: reduce){.ve{animation:none !important}.ve-lens,.ve-puff,.ve-trail{opacity:0}}
/* route map timeline */
.route{position:relative;margin-top:clamp(56px,7vw,88px);height:600px}
.rt-label{position:absolute;left:0;top:0;margin:0;font-size:14px;font-weight:700;color:#111}
.rt-svg{position:absolute;left:0;top:180px;width:100%;height:300px;overflow:visible}
.rt-base{fill:none;stroke:#CFC7B8;stroke-width:3;stroke-dasharray:1 11;stroke-linecap:round;vector-effect:non-scaling-stroke}
.rt-line{fill:none;stroke:#111;stroke-width:3;stroke-linecap:round;vector-effect:non-scaling-stroke}
.rt-list{list-style:none;margin:0;padding:0}
.rt-stop{position:absolute;left:var(--x);top:calc(180px + var(--y));width:0;height:0}
.rt-pin{position:absolute;left:0;top:0;transform:translate(-50%,-50%);width:54px;height:54px;border-radius:50%;background:#FFFFFF;border:2px solid #111;display:flex;align-items:center;justify-content:center;font-size:25px;box-shadow:0 10px 24px rgba(17,17,17,.14);transition:transform .55s cubic-bezier(.3,1.6,.5,1),opacity .4s,border-color .3s}
.rt-stop:hover .rt-pin{transform:translate(-50%,-50%) scale(1.15) rotate(-8deg)}
.rt-card{position:absolute;left:0;width:172px;transform:translateX(-50%);display:flex;flex-direction:column;gap:4px;text-align:center;transition:opacity .5s,transform .5s cubic-bezier(.2,.8,.2,1)}
.rt-up .rt-card{bottom:44px}.rt-down .rt-card{top:44px}
.rt-stop:first-child .rt-card{transform:translateX(-30%)}
.rt-stop:last-child .rt-card{transform:translateX(-72%)}
.rt-year{font-size:32px;font-weight:700;line-height:1;letter-spacing:-.04em}
.rt-what{font-size:14px;line-height:1.4;color:#2D2B27}
.rt-plane{position:absolute;left:0;top:0;z-index:3;font-size:32px;line-height:1;opacity:0;pointer-events:none;will-change:transform}
.rt-rail{display:none}
.rt-live .rt-plane{opacity:1}
.rt-live .rt-stop .rt-pin{opacity:.35;transform:translate(-50%,-50%) scale(.72);border-color:#CFC7B8}
.rt-live .rt-stop .rt-card{opacity:.25}
.rt-live .rt-stop.on .rt-pin{opacity:1;transform:translate(-50%,-50%) scale(1);border-color:#111}
.rt-live .rt-stop.on .rt-card{opacity:1}
.rt-live .rt-stop.on:hover .rt-pin{transform:translate(-50%,-50%) scale(1.15) rotate(-8deg)}
@media (max-width: 860px){
.route{height:auto;padding-left:48px}
.rt-svg{display:none}
.rt-label{position:static;margin:0 0 22px -48px}
.rt-rail{display:block;position:absolute;left:19px;top:52px;bottom:24px;width:3px;border-radius:3px;background:#D8D1C3}
.rt-rail-fill{display:block;width:100%;height:100%;border-radius:3px;background:#111;transform-origin:top}
.rt-stop{position:relative;left:auto;top:auto;width:auto;height:auto;padding:0 0 28px}
.rt-pin{left:-27.5px;top:18px;width:42px;height:42px;font-size:20px}
.rt-card,.rt-stop:first-child .rt-card,.rt-stop:last-child .rt-card{position:static;width:auto;transform:none;text-align:left}
.rt-year{font-size:26px}
.rt-plane{font-size:26px}
}
@media (prefers-reduced-motion: reduce){.rt-plane{display:none}}
/*hero:end*/
"""

def tag(href, label):
    return (f'<a href="{href}" style="text-decoration: none; font-family: \'DM Sans\', sans-serif; font-size: 14px; font-weight: 600; '
            f'letter-spacing: 0; padding: 6px 12px; border: 1px solid #4A4842; border-radius: 999px; color: #D8D3C9">{label}</a>')

def headline():
    return f'''<div class="hero-stage" style="position: relative">
<div class="jg" aria-hidden="true">
<span class="jg-cap">Most B2B websites sound like this</span>
{words()}
</div>
<p class="sg" style="margin: 0; font-weight: 600; font-size: clamp(56px, 7.8vw, 120px); line-height: 0.95; letter-spacing: -0.055em">
<span class="l1" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 18px"><span><span class="hl-mute">Make it</span> <span class="v-clear">clear<span class="v-dot">.</span><span class="ve ve-lens" aria-hidden="true">🔍</span><span class="ve ve-spark" aria-hidden="true">✨</span></span></span>{tag('Site-Service-Positioning.dc.html', 'Positioning &amp; messaging')}</span>
<span class="l2" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 18px; padding-left: clamp(0px, 5vw, 80px)"><span><span class="hl-mute">Make it</span> <span class="v-land">land<span class="v-dot">.</span><span class="ve ve-rocket" aria-hidden="true">🚀</span><span class="ve ve-puff" aria-hidden="true">💨</span></span></span>{tag('Site-Service-Launch.dc.html', 'Launches &amp; go-to-market')}</span>
<span class="l3" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 18px; padding-left: clamp(0px, 10vw, 160px)"><span><span class="hl-mute">Make it</span> <span class="v-travel">travel<span class="v-dot">.</span><span class="ve ve-trail" aria-hidden="true"></span><span class="ve ve-plane" aria-hidden="true">✈️</span></span></span>{tag('Site-Service-Content.dc.html', 'Content &amp; organic growth')}</span>
</p>
<button class="jg-replay" type="button" data-jg-replay>↺ Replay the edit</button>
</div>'''

if __name__ == '__main__':
    home = pathlib.Path(__file__).parent.parent / 'project' / 'Home-B2.dc.html'
    s = home.read_text()
    if '<div class="hero-stage"' in s:
        s = re.sub(r'<div class="hero-stage".*?<button class="jg-replay"[^>]*>[^<]*</button>\n</div>', lambda m: headline(), s, count=1, flags=re.S)
    else:
        s = re.sub(r'<p class="sg" style="margin: 0; font-weight: 600; font-size: clamp\(56px, 7\.8vw, 120px\).*?</p>', lambda m: headline(), s, count=1, flags=re.S)
    s = s.replace('<section id="top" class="grid-bg">', '<section id="top" class="grid-bg hero-anim">')
    s = re.sub(r'\n?/\*hero:start\*/.*?/\*hero:end\*/\n?', '\n', s, flags=re.S)
    s = s.replace('</style>\n</helmet>', CSS.strip('\n') + '\n</style>\n</helmet>', 1)
    home.write_text(s)
    print('hero written', s.count('class="jg"'), s.count('hero-anim'))
