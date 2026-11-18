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
.logo-i{filter:grayscale(1) contrast(1.1);opacity:.75;transition:filter .3s,opacity .3s}
.logo-i:hover{filter:none;opacity:1}
@media (max-width: 640px){.logo-i{transform:scale(.8)}}
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
<span class="l1" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 18px"><span><span class="hl-mute">Make it</span> <span class="v-clear">clear<span class="v-dot">.</span></span></span>{tag('Site-Service-Positioning.dc.html', 'Positioning &amp; messaging')}</span>
<span class="l2" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 18px; padding-left: clamp(0px, 5vw, 80px)"><span><span class="hl-mute">Make it</span> <span class="v-land">land<span class="v-dot">.</span></span></span>{tag('Site-Service-Launch.dc.html', 'Launches &amp; go-to-market')}</span>
<span class="l3" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 18px; padding-left: clamp(0px, 10vw, 160px)"><span><span class="hl-mute">Make it</span> <span class="v-travel">travel<span class="v-dot">.</span></span></span>{tag('Site-Service-Content.dc.html', 'Content &amp; organic growth')}</span>
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
