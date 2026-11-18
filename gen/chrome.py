"""Shared site chrome: the header with dropdown menus, and the CSS for the menu,
mobile layout and scroll reveals. Used by build.py (inner pages) and
sync_home.py (the homepage, which is edited directly)."""

WORK_MENU = [
    ('Stears Elections', 'How a new election tracker beat the BBC on Google', 'Site-Work.dc.html#stears'),
    ('RemotePass × Certn', 'A partnership launch with 270+ media pickups', 'Site-Work.dc.html#certn'),
    ('RemotePass Ask AI', 'Selling the answer, not the AI: record MQLs', 'Site-Work.dc.html#askai'),
    ('RemotePass content engine', '174% organic growth and an English–Arabic hub', 'Site-Work.dc.html#engine'),
    ('Xofu', 'One clear question for a new AI product', 'Site-Work.dc.html#xofu'),
]

EXPERTISE_MENU = [
    ('Positioning & messaging', 'Make it clear: a story buyers can repeat', 'Site-Service-Positioning.dc.html'),
    ('Launches & go-to-market', 'Make it land: launches built for pipeline', 'Site-Service-Launch.dc.html'),
    ('Content & organic growth', 'Make it travel: content, SEO and AI search', 'Site-Service-Content.dc.html'),
]

CHEV = '<span class="chev" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3.5 5 6.5 8 3.5"/></svg></span>'


def _dropdown(label, href, active, heading, items, all_label, all_href):
    on = label == active
    cls = 'dd-top nav-on' if on else 'dd-top'
    cur = ' aria-current="page"' if on else ''
    links = ''.join(
        f'<a class="dd-l" href="{h}"><b>{t}</b><span>{s}</span></a>' for t, s, h in items
    )
    return (
        f'<div class="dd"><a class="{cls}" href="{href}"{cur} aria-haspopup="true">{label}{CHEV}</a>'
        f'<div class="dd-p"><p class="dd-h">{heading}</p>{links}'
        f'<a class="dd-all" href="{all_href}">{all_label} →</a></div></div>'
    )


def header(active, home=False):
    def plain(label, href):
        on = label == active
        cls = 'nl nav-on' if on else 'nl'
        cur = ' aria-current="page"' if on else ''
        return f'<a class="{cls}" href="{href}"{cur}>{label}</a>'

    logo_href = '#top' if home else 'Home-B2.dc.html'
    return f'''<header class="site-h">
<div class="h-in">
<a href="{logo_href}" class="logo sg"><span aria-hidden="true" class="logo-m">JA</span>Jeremiah Ajayi</a>
<input type="checkbox" id="navt" class="nav-t" aria-label="Open the menu" aria-controls="nav-main">
<label for="navt" class="nav-btn" aria-hidden="true"><span class="nav-btn-t">Menu</span><span class="burger"></span></label>
<nav id="nav-main" class="nav-main" aria-label="Primary">
{_dropdown('Work', 'Site-Work.dc.html', active, 'Case studies', WORK_MENU, 'All work and projects', 'Site-Work.dc.html#index')}
{_dropdown('Expertise', 'Site-Services.dc.html', active, 'Services', EXPERTISE_MENU, 'All services', 'Site-Services.dc.html')}
{plain('EmpowerQ', 'Site-EmpowerQ.dc.html')}
{plain('Writing', 'Site-Writing.dc.html')}
{plain('About', 'Site-About.dc.html')}
<a class="btn-o nav-cta" href="Site-Contact.dc.html">Book a call <span class="arr" aria-hidden="true">→</span></a>
</nav>
</div>
</header>'''


GUIDE_OPTS = [
    ('positioning', '🧭', 'Our product is hard to explain'),
    ('launch', '🚀', 'We have a launch coming up'),
    ('content', '📈', 'We need content that ranks and converts'),
    ('ai', '🤖', 'We want to show up in AI answers'),
    ('hire', '💼', 'I’m hiring a marketer'),
    ('proof', '🏆', 'Show me results first'),
    ('read', '📚', 'I want to read your research'),
    ('empowerq', '🌈', 'I want to support EmpowerQ'),
]


def guide():
    av = '<img class="gd-av" src="/_blob/ab01351679f0c21d14aae4bf06f3affa" alt="" width="40" height="40">'
    peek_chips = ''.join(
        f'<button type="button" class="gd-chip" data-gd="{k}"><span aria-hidden="true">{e}</span> {t}</button>'
        for k, e, t in GUIDE_OPTS[:3]
    )
    return f'''<!--guide:start-->
<div class="gd" data-gd-root>
<div class="gd-peek" data-gd-peek hidden>
<button type="button" class="gd-peek-x" data-gd-dismiss aria-label="Dismiss">×</button>
<div class="gd-peek-top">{av}<p><b>Hi, I’m Jeremiah 👋</b><br>What brings you here today?</p></div>
<div class="gd-peek-chips">{peek_chips}<button type="button" class="gd-chip gd-chip-more" data-gd-open>Something else →</button></div>
</div>
<button type="button" class="gd-launch" data-gd-open aria-expanded="false" aria-controls="gd-panel">{av}<span>Ask me anything</span><span class="gd-wave" aria-hidden="true">👋</span></button>
<div class="gd-panel" id="gd-panel" role="dialog" aria-label="Chat with Jeremiah’s site guide" hidden>
<div class="gd-head">{av}<div class="gd-who"><b>Jeremiah</b><span>Here to point you the right way</span></div><button type="button" class="gd-ic" data-gd-restart aria-label="Start over" title="Start over">↺</button><button type="button" class="gd-ic" data-gd-close aria-label="Close the chat">×</button></div>
<div class="gd-thread" data-gd-thread aria-live="polite"></div>
<form class="gd-ask" data-gd-form><label class="gd-sr" for="gd-q">Type a question</label><input id="gd-q" name="q" autocomplete="off" placeholder="Type a question…"><button type="submit" aria-label="Send">↑</button></form>
</div>
</div>
<div class="mbar" aria-label="Quick actions"><a class="btn-o" href="Site-Contact.dc.html">Book a call <span class="arr" aria-hidden="true">→</span></a><button type="button" class="mbar-g" data-gd-open aria-controls="gd-panel">👋 Ask me</button></div>
<!--guide:end-->'''


SHARED_CSS = r"""
/*shared:start*/
.site-h{position:sticky;top:0;z-index:50;background:rgba(17,17,17,.92);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border-bottom:1px solid #2B2A27}
.h-in{max-width:1360px;margin:0 auto;padding:0 28px;height:68px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.logo{display:inline-flex;align-items:center;gap:10px;font-weight:700;font-size:21px;letter-spacing:-.04em;text-decoration:none;color:#F2EFE8}
.logo:hover{color:#F2EFE8}
.logo-m{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:9px;background:#FF5A2A;color:#111;font-size:16px;letter-spacing:-.06em}
.nav-t{display:none;position:absolute;opacity:0;pointer-events:none;width:1px;height:1px;margin:0}
.nav-btn{display:none}
.nav-main{display:flex;align-items:center;gap:4px;font-size:15px;font-weight:500}
.nav-main>a.nl,.dd-top{display:inline-flex;align-items:center;gap:7px;min-height:44px;padding:0 12px;border-radius:999px;text-decoration:none;color:#F2EFE8;transition:background .25s,color .25s}
.nav-main>a.nl:hover,.dd-top:hover{background:#262523;color:#F2EFE8}
.nav-on{color:#FF5A2A !important}
.dd{position:relative}
.chev{flex:none;width:20px;height:20px;border-radius:50%;background:#2E2D2A;color:#F2EFE8;display:inline-flex;align-items:center;justify-content:center;transition:transform .3s,background .3s,color .3s}
.chev svg{width:10px;height:10px}
.dd:hover .chev,.dd:focus-within .chev{transform:rotate(180deg);background:#FF5A2A;color:#111}
.dd-p{position:absolute;top:calc(100% + 12px);left:-8px;width:360px;padding:10px;box-sizing:border-box;border-radius:16px;background:#1A1A19;border:1px solid #33322E;box-shadow:0 28px 64px rgba(0,0,0,.5);opacity:0;visibility:hidden;transform:translateY(8px);transition:opacity .22s,transform .22s,visibility 0s .22s}
.dd-p::before{content:"";position:absolute;left:0;right:0;top:-14px;height:14px}
.dd:hover .dd-p,.dd:focus-within .dd-p{opacity:1;visibility:visible;transform:none;transition:opacity .22s,transform .22s}
.dd-h{margin:6px 12px 4px;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#8A867E}
.dd-l{display:flex;flex-direction:column;gap:3px;padding:11px 12px;border-radius:10px;text-decoration:none;color:#F2EFE8;transition:background .2s}
.dd-l:hover{background:#272624;color:#F2EFE8}
.dd-l b{font-size:15px;font-weight:600;transition:color .2s}
.dd-l span{font-size:13px;line-height:1.4;color:#B5B0A6}
.dd-l:hover b{color:#FF5A2A}
.dd-all{display:block;margin-top:6px;padding:12px 12px 8px;border-top:1px solid #33322E;font-size:14px;font-weight:700;color:#FF5A2A;text-decoration:none}
.dd-all:hover{color:#F2EFE8}
.nav-cta{margin-left:12px;display:inline-flex;align-items:center;min-height:44px;padding:0 22px;border-radius:999px;font-weight:700}
@media (max-width: 1000px){
.site-h{background:#111;-webkit-backdrop-filter:none;backdrop-filter:none}
.h-in{height:62px;padding:0 20px}
.logo{font-size:19px}.logo-m{width:30px;height:30px;font-size:14px;border-radius:8px}
.nav-t{display:block}
.nav-btn{display:inline-flex;align-items:center;gap:10px;min-height:44px;padding:0 6px 0 16px;border-radius:999px;border:1px solid #3A3934;color:#F2EFE8;font-size:14px;font-weight:600;cursor:pointer;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent}
.burger{position:relative;flex:none;width:32px;height:32px;border-radius:50%;background:#FF5A2A}
.burger::before,.burger::after{content:"";position:absolute;left:9px;right:9px;height:2px;border-radius:2px;background:#111;transition:transform .3s,top .3s}
.burger::before{top:12px}.burger::after{top:18px}
.nav-t:checked~.nav-btn .burger::before{top:15px;transform:rotate(45deg)}
.nav-t:checked~.nav-btn .burger::after{top:15px;transform:rotate(-45deg)}
.nav-t:focus-visible~.nav-btn{outline:2px solid #FF5A2A;outline-offset:2px}
.nav-main{position:fixed;left:0;right:0;top:62px;bottom:0;z-index:49;flex-direction:column;align-items:stretch;gap:0;padding:8px 20px 40px;background:#111;overflow-y:auto;-webkit-overflow-scrolling:touch;opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s .3s}
.nav-t:checked~.nav-main{opacity:1;visibility:visible;transition:opacity .3s}
.nav-main>a.nl,.dd-top{justify-content:space-between;min-height:64px;padding:0;border-radius:0;border-bottom:1px solid #2B2A27;font-family:'Space Grotesk',system-ui,sans-serif;font-size:30px;font-weight:600;letter-spacing:-.045em}
.nav-main>a.nl:hover,.dd-top:hover{background:none}
.dd-top{border-bottom:0}
.chev{display:none}
.dd-p{position:static;width:auto;padding:0 0 14px;border:0;border-bottom:1px solid #2B2A27;border-radius:0;background:none;box-shadow:none;opacity:1;visibility:visible;transform:none;transition:none}
.dd-p::before{display:none}
.dd-h{display:none}
.dd-l{padding:9px 0 9px 14px;border-left:2px solid #2B2A27;border-radius:0}
.dd-l:hover{background:none;border-left-color:#FF5A2A}
.dd-l b{font-size:16px}
.dd-all{margin:6px 0 0;padding:8px 0 0 14px;border-top:0}
.nav-cta{margin:28px 0 0;justify-content:center;min-height:58px;font-size:17px}
.nav-main>*{opacity:0;transform:translateY(14px);transition:opacity .45s cubic-bezier(.2,.8,.2,1),transform .45s cubic-bezier(.2,.8,.2,1)}
.nav-t:checked~.nav-main>*{opacity:1;transform:none}
.nav-t:checked~.nav-main>*:nth-child(2){transition-delay:.05s}
.nav-t:checked~.nav-main>*:nth-child(3){transition-delay:.1s}
.nav-t:checked~.nav-main>*:nth-child(4){transition-delay:.15s}
.nav-t:checked~.nav-main>*:nth-child(5){transition-delay:.2s}
.nav-t:checked~.nav-main>*:nth-child(6){transition-delay:.25s}
body:has(.nav-t:checked){overflow:hidden}
}
@media (max-width: 640px){
.mswipe{display:flex !important;flex-wrap:nowrap !important;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;gap:12px !important;margin-right:-20px !important;padding-right:20px !important;padding-bottom:8px;scrollbar-width:none}
.mswipe::-webkit-scrollbar{display:none}
.mswipe>*{flex:0 0 84% !important;scroll-snap-align:start;min-width:0}
.m2{grid-template-columns:repeat(2,minmax(0,1fr)) !important}
.mhint{display:flex !important}
}
.mhint{display:none;align-items:center;gap:8px;margin-top:14px;font-size:13px;font-weight:600;opacity:.65}
.js-rv .rv{opacity:0;transform:translateY(26px);transition:opacity .8s cubic-bezier(.2,.8,.2,1),transform .8s cubic-bezier(.2,.8,.2,1)}
.js-rv .rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){.js-rv .rv{opacity:1;transform:none;transition:none}.nav-main>*,.nav-main,.dd-p,.chev,.burger::before,.burger::after{transition:none !important}}
.arr{display:inline-block;transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.btn-o,.btn-k,.btn-l{position:relative}
.btn-o{box-shadow:0 3px 0 #B8431C,0 12px 28px rgba(255,90,42,.22)}
.btn-o:hover{box-shadow:0 5px 0 #B8431C,0 16px 32px rgba(255,90,42,.28)}
.btn-o:active{transform:translateY(1px);box-shadow:0 1px 0 #B8431C}
.btn-o:hover .arr,.btn-k:hover .arr,.btn-l:hover .arr{transform:translateX(5px)}
.btn-o:hover .arr-d,.btn-k:hover .arr-d,.btn-l:hover .arr-d{transform:translateY(4px)}
a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #FF5A2A;outline-offset:3px}
.gd{position:fixed;right:20px;bottom:20px;z-index:60;font-family:'DM Sans',system-ui,sans-serif;display:flex;flex-direction:column;align-items:flex-end;gap:12px}
.gd-av{flex:none;width:40px;height:40px;border-radius:50%;object-fit:cover;object-position:center 30%;background:#FFFFFF;box-shadow:0 0 0 2px #F2EFE8}
.gd-launch{display:inline-flex;align-items:center;gap:10px;min-height:56px;padding:0 18px 0 8px;border:0;border-radius:999px;background:#F2EFE8;color:#111;font:700 15px 'DM Sans',system-ui,sans-serif;cursor:pointer;box-shadow:0 14px 40px rgba(0,0,0,.3),0 0 0 1px rgba(17,17,17,.08);transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s}
.gd-launch .gd-av{width:40px;height:40px;box-shadow:none}
.gd-launch:hover{transform:translateY(-3px)}
.gd-wave{display:inline-block;font-size:20px;transform-origin:70% 70%;animation:wave 2.4s 1.2s ease-in-out 2}
@keyframes wave{0%,60%,100%{transform:rotate(0)}10%,30%{transform:rotate(16deg)}20%,40%{transform:rotate(-10deg)}50%{transform:rotate(10deg)}}
.gd-open .gd-launch,.gd-open .gd-peek{display:none}
.gd-peek{position:relative;width:min(360px,calc(100vw - 32px));padding:16px;box-sizing:border-box;border-radius:20px 20px 6px 20px;background:#FFFFFF;color:#111;box-shadow:0 22px 60px rgba(0,0,0,.35),0 0 0 1px rgba(17,17,17,.06);animation:gd-pop .45s cubic-bezier(.2,.8,.2,1)}
.gd-peek[hidden]{display:none}
.gd-peek-top{display:flex;gap:12px;align-items:flex-start;padding-right:22px}
.gd-peek-top p{margin:0;font-size:15px;line-height:1.45;color:#2D2B27}
.gd-peek-top b{color:#111;font-size:16px}
.gd-peek-x{position:absolute;top:8px;right:8px;width:30px;height:30px;border:0;border-radius:50%;background:none;color:#6B675F;font-size:20px;cursor:pointer}
.gd-peek-x:hover{background:#F2EFE8;color:#111}
.gd-peek-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.gd-chip{display:inline-flex;align-items:center;gap:6px;min-height:38px;padding:6px 13px;border:1px solid #D8D1C3;border-radius:999px;background:#FFFFFF;color:#111;font:600 14px 'DM Sans',system-ui,sans-serif;cursor:pointer;transition:border-color .2s,background .2s,transform .2s}
.gd-chip:hover{border-color:#111;transform:translateY(-1px)}
.gd-chip-more{background:#111;border-color:#111;color:#F2EFE8}
.gd-chip-more:hover{background:#2B2A27}
.gd-panel{width:min(400px,calc(100vw - 32px));height:min(640px,calc(100vh - 100px));display:flex;flex-direction:column;border-radius:22px;overflow:hidden;background:#F7F5F0;color:#111;box-shadow:0 30px 80px rgba(0,0,0,.42),0 0 0 1px rgba(17,17,17,.08);transform-origin:bottom right;animation:gd-pop .32s cubic-bezier(.2,.8,.2,1)}
.gd-panel[hidden]{display:none}
@keyframes gd-pop{from{opacity:0;transform:translateY(14px) scale(.96)}to{opacity:1;transform:none}}
.gd-head{flex:none;display:flex;align-items:center;gap:10px;padding:14px 12px 14px 16px;background:#111;color:#F2EFE8}
.gd-who{flex:1;min-width:0;display:flex;flex-direction:column}
.gd-who b{font:700 16px 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em}
.gd-who span{font-size:12px;color:#B5B0A6}
.gd-ic{flex:none;width:36px;height:36px;border:0;border-radius:50%;background:#2B2A27;color:#F2EFE8;font-size:18px;line-height:1;cursor:pointer}
.gd-ic:hover{background:#F2EFE8;color:#111}
.gd-thread{flex:1;overflow-y:auto;padding:16px 14px 6px;display:flex;flex-direction:column;gap:8px;scroll-behavior:smooth}
.gd-m{max-width:86%;padding:11px 14px;border-radius:18px;font-size:15px;line-height:1.5;animation:gd-msg .35s cubic-bezier(.2,.8,.2,1)}
@keyframes gd-msg{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.gd-bot{align-self:flex-start;background:#FFFFFF;border:1px solid #E6E1D6;border-bottom-left-radius:6px;color:#2D2B27}
.gd-bot b{color:#111}
.gd-you{align-self:flex-end;background:#111;color:#F2EFE8;border-bottom-right-radius:6px}
.gd-typing{display:inline-flex;gap:4px;align-items:center;padding:14px 16px}
.gd-typing i{width:7px;height:7px;border-radius:50%;background:#B5B0A6;animation:gd-dot 1s infinite}
.gd-typing i:nth-child(2){animation-delay:.15s}.gd-typing i:nth-child(3){animation-delay:.3s}
@keyframes gd-dot{0%,60%,100%{transform:none;opacity:.5}30%{transform:translateY(-4px);opacity:1}}
.gd-links{align-self:stretch;margin:2px 0 4px;padding:0;list-style:none;display:grid;gap:6px;animation:gd-msg .35s cubic-bezier(.2,.8,.2,1)}
.gd-links a{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:50px;padding:10px 14px;border-radius:14px;background:#FFFFFF;border:1px solid #E1DBCF;color:#111;font-weight:700;font-size:15px;text-decoration:none;transition:border-color .2s,background .2s,transform .2s}
.gd-links a:hover{border-color:#111;transform:translateX(2px)}
.gd-links a.gd-main{background:#FF5A2A;border-color:#FF5A2A;color:#111}
.gd-links a.gd-main:hover{background:#111;border-color:#111;color:#F2EFE8}
.gd-links a span{flex:none;font-weight:500;font-size:13px;opacity:.75;text-align:right}
.gd-choices{display:flex;flex-wrap:wrap;gap:6px;justify-content:flex-end;padding:2px 0 4px;animation:gd-msg .35s cubic-bezier(.2,.8,.2,1)}
.gd-ask{flex:none;display:flex;gap:8px;margin:8px 12px 12px;padding:5px 5px 5px 16px;border:1px solid #D8D1C3;border-radius:999px;background:#FFFFFF}
.gd-ask input{flex:1;min-width:0;border:0;background:none;font:500 15px 'DM Sans',system-ui,sans-serif;color:#111;outline:none}
.gd-ask button{flex:none;width:40px;height:40px;border:0;border-radius:50%;background:#111;color:#F2EFE8;font-size:18px;font-weight:700;cursor:pointer}
.gd-ask button:hover{background:#FF5A2A;color:#111}
.gd-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.mbar{display:none}
@media (max-width: 640px){
.gd{right:12px;left:12px;bottom:84px;align-items:stretch}
.gd-open{bottom:12px}
.gd-launch{display:none}
.gd-peek{width:auto}
.gd-panel{width:auto;height:calc(100vh - 24px);height:calc(100dvh - 24px)}
.mbar{position:fixed;left:0;right:0;bottom:0;z-index:55;display:flex;gap:10px;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(17,17,17,.94);border-top:1px solid #2B2A27}
.mbar .btn-o{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:50px;border-radius:999px;font-weight:700;font-size:16px}
.mbar-g{flex:none;min-height:50px;padding:0 18px;border:1px solid #4A4842;border-radius:999px;background:#1E1D1B;color:#F2EFE8;font:700 15px 'DM Sans',system-ui,sans-serif;cursor:pointer}
body{padding-bottom:72px}
body:has(.nav-t:checked) .mbar,body:has(.gd-open) .mbar,body:has(.nav-t:checked) .gd{display:none}
}
@media (prefers-reduced-motion: reduce){.gd-wave,.gd-panel,.gd-peek,.gd-m,.gd-links,.gd-typing i{animation:none}.gd-launch,.gd-chip,.arr{transition:none}}
.rp{position:fixed;left:0;right:0;top:0;height:3px;z-index:70;pointer-events:none}
.rp span{display:block;height:100%;background:#FF5A2A;transform:scaleX(0);transform-origin:left center}
.btn-o,.gd-launch{transition:background .3s,color .3s,transform .3s,box-shadow .3s,translate .35s cubic-bezier(.2,.8,.2,1)}
@view-transition{navigation:auto}
.site-h{view-transition-name:site-header}
::view-transition-old(root){animation:vt-out .22s ease both}
::view-transition-new(root){animation:vt-in .38s cubic-bezier(.2,.8,.2,1) both}
@keyframes vt-out{to{opacity:0}}
@keyframes vt-in{from{opacity:0;transform:translateY(10px)}}
@media (prefers-reduced-motion: reduce){@view-transition{navigation:none}}
/* report-inspired kit: colours, shapes, patterns */
:root{--ink:#111;--paper:#F2EFE8;--cream:#FFF5D9;--orange:#FF5A2A;--sun:#FFC83D;--leaf:#1FA463;--mint:#8FE3B0;--blush:#FF8FB6;--lav:#B9A6FF;--night:#0E2A2E}
.shp{display:inline-block;-webkit-mask:var(--m) center/contain no-repeat;mask:var(--m) center/contain no-repeat}
.shp-flower{--m:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20100%20100%22%3E%3Ccircle%20cx%3D%2281.00%22%20cy%3D%2250.00%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2271.92%22%20cy%3D%2271.92%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2250.00%22%20cy%3D%2281.00%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2228.08%22%20cy%3D%2271.92%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2219.00%22%20cy%3D%2250.00%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2228.08%22%20cy%3D%2228.08%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2250.00%22%20cy%3D%2219.00%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2271.92%22%20cy%3D%2228.08%22%20r%3D%2218.5%22/%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2234%22/%3E%3C/svg%3E")}
.shp-clover{--m:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20100%20100%22%3E%3Ccircle%20cx%3D%2266.97%22%20cy%3D%2266.97%22%20r%3D%2225%22/%3E%3Ccircle%20cx%3D%2233.03%22%20cy%3D%2266.97%22%20r%3D%2225%22/%3E%3Ccircle%20cx%3D%2233.03%22%20cy%3D%2233.03%22%20r%3D%2225%22/%3E%3Ccircle%20cx%3D%2266.97%22%20cy%3D%2233.03%22%20r%3D%2225%22/%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2222%22/%3E%3C/svg%3E")}
.shp-star{--m:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20100%20100%22%3E%3Cpath%20d%3D%22M50%200C54%2034%2066%2046%20100%2050C66%2054%2054%2066%2050%20100C46%2066%2034%2054%200%2050C34%2046%2046%2034%2050%200Z%22/%3E%3C/svg%3E")}
.shp-cross{--m:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20100%20100%22%3E%3Crect%20x%3D%2238%22%20y%3D%222%22%20width%3D%2224%22%20height%3D%2296%22%20rx%3D%2212%22%20transform%3D%22rotate%280%2050%2050%29%22/%3E%3Crect%20x%3D%2238%22%20y%3D%222%22%20width%3D%2224%22%20height%3D%2296%22%20rx%3D%2212%22%20transform%3D%22rotate%2860%2050%2050%29%22/%3E%3Crect%20x%3D%2238%22%20y%3D%222%22%20width%3D%2224%22%20height%3D%2296%22%20rx%3D%2212%22%20transform%3D%22rotate%28120%2050%2050%29%22/%3E%3C/svg%3E")}
.shp-scallop{--m:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20100%20100%22%3E%3Ccircle%20cx%3D%2294.00%22%20cy%3D%2250.00%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2290.65%22%20cy%3D%2266.84%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2281.11%22%20cy%3D%2281.11%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2266.84%22%20cy%3D%2290.65%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2250.00%22%20cy%3D%2294.00%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2233.16%22%20cy%3D%2290.65%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2218.89%22%20cy%3D%2281.11%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%229.35%22%20cy%3D%2266.84%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%226.00%22%20cy%3D%2250.00%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%229.35%22%20cy%3D%2233.16%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2218.89%22%20cy%3D%2218.89%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2233.16%22%20cy%3D%229.35%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2250.00%22%20cy%3D%226.00%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2266.84%22%20cy%3D%229.35%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2281.11%22%20cy%3D%2218.89%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2290.65%22%20cy%3D%2233.16%22%20r%3D%228.6%22/%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2245%22/%3E%3C/svg%3E")}
.pat-tri{-webkit-mask:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2040%2020%22%3E%3Cpath%20d%3D%22M0%2020L10%200L20%2020Z%20M20%2020L30%200L40%2020Z%22%20fill%3D%22black%22/%3E%3C/svg%3E") 0 0/40px 20px repeat;mask:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2040%2020%22%3E%3Cpath%20d%3D%22M0%2020L10%200L20%2020Z%20M20%2020L30%200L40%2020Z%22%20fill%3D%22black%22/%3E%3C/svg%3E") 0 0/40px 20px repeat}
.pat-rays{background:repeating-conic-gradient(from 0deg at 0% 100%,currentColor 0 3deg,transparent 3deg 7deg)}
.spin{animation:spin 24s linear infinite}
.spin-r{animation:spin 30s linear infinite reverse}
.floaty{animation:floaty 6s ease-in-out infinite}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes floaty{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-12px) rotate(6deg)}}
@media (prefers-reduced-motion: reduce){.spin,.spin-r,.floaty{animation:none}}
/* results bento */
.bento{margin-top:48px;display:grid;grid-template-columns:1.25fr 1fr 1fr;grid-template-rows:auto auto;gap:14px}
.bt{position:relative;overflow:hidden;border-radius:22px;padding:clamp(22px,2.6vw,34px);min-height:180px;display:flex;flex-direction:column;justify-content:flex-end;color:#111}
.bt-n{position:relative;margin:0;font-weight:700;font-size:clamp(56px,6vw,96px);line-height:.85;letter-spacing:-.06em}
.bt-l{position:relative;margin:10px 0 0;font-size:15px;line-height:1.45;font-weight:600;max-width:260px}
.bt-1{grid-row:span 2;background:var(--sun);min-height:380px}
.bt-1 .bt-n{font-size:clamp(80px,9vw,150px)}
.bt-2{background:var(--leaf);color:#FFFFFF}
.bt-3{background:var(--mint)}
.bt-4{grid-column:span 2;background:var(--orange)}
.bt-rays{position:absolute;right:-30%;top:-40%;width:110%;aspect-ratio:1;color:rgba(255,90,42,.55);border-radius:50%}
.bt-sh{position:absolute;right:-26px;top:-26px;width:120px;aspect-ratio:1}
.bt-2 .bt-sh{background:rgba(255,255,255,.22)}
.bt-3 .bt-sh{background:var(--leaf);opacity:.35;width:90px;right:16px;top:16px}
.bt-tri{position:absolute;right:0;top:0;width:46%;height:100%;background:var(--sun);opacity:.9}
@media (max-width: 760px){.bento{grid-template-columns:1fr 1fr}.bt-1{grid-row:auto;grid-column:span 2;min-height:220px}.bt-4{grid-column:span 2}.bt{min-height:150px}.bt-n{font-size:52px}.bt-1 .bt-n{font-size:84px}.bt-tri{width:34%}}
/* case number badges */
.num-b{display:inline-flex;align-items:center;justify-content:center;width:46px;height:46px;font-size:14px;font-weight:700;color:#111}
/* disciplines as tiles */
.xp-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.xp{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:12px;min-height:440px;padding:clamp(24px,2.6vw,34px);border-radius:24px;text-decoration:none;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.xp:hover{transform:translateY(-8px) rotate(-.6deg);color:#111}
.xp-art{position:relative;width:110px;height:110px;margin-bottom:auto}
.xp-shape{position:absolute;inset:0}
.xp-emo{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:46px;transition:transform .5s cubic-bezier(.3,1.6,.5,1)}
.xp:hover .xp-emo{transform:scale(1.18) rotate(-10deg)}
.xp-verb{font-size:clamp(56px,5.6vw,88px);font-weight:700;line-height:.85;letter-spacing:-.06em}
.xp-name{font-size:22px;font-weight:600;letter-spacing:-.02em}
.xp-long{font-size:16px;line-height:1.55;color:#2D2B27}
.xp-proof{font-size:13.5px;line-height:1.5;color:#2D2B27}
.xp-go{margin-top:6px;display:inline-flex;align-items:center;gap:8px;align-self:flex-start;min-height:46px;padding:0 18px;border-radius:999px;background:#111;color:#F2EFE8;font-weight:700;font-size:15px}
.xp:hover .xp-go .arr{transform:translateX(5px)}
@media (max-width: 900px){.xp-grid{grid-template-columns:1fr}.xp{min-height:0}.xp-art{width:84px;height:84px}.xp-emo{font-size:36px}}
/* contact doors */
.door-e{flex:none;display:inline-flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:14px;font-size:20px;background:var(--sun)}
.door:nth-of-type(2) .door-e{background:var(--orange)}
.door:nth-of-type(3) .door-e{background:var(--mint)}
.door:nth-of-type(4) .door-e{background:var(--lav)}
.door:nth-of-type(5) .door-e{background:var(--blush)}

/* rollout helpers */
.has-deco{position:relative;overflow:hidden}
.has-deco>*:not(.deco){position:relative;z-index:1}
.deco{position:absolute;pointer-events:none;z-index:0}
.dot-bg{background-image:radial-gradient(rgba(17,17,17,.09) 1.4px,transparent 1.6px);background-size:22px 22px}
.btn-d{text-decoration:none;color:#111;border:1.5px solid #111;transition:background .3s,color .3s}
.btn-d:hover{background:#111;color:#F2EFE8}
.tiles-rot>*:nth-child(6n+1){background:var(--sun) !important;color:#111 !important}
.tiles-rot>*:nth-child(6n+2){background:var(--mint) !important;color:#111 !important}
.tiles-rot>*:nth-child(6n+3){background:var(--blush) !important;color:#111 !important}
.tiles-rot>*:nth-child(6n+4){background:var(--lav) !important;color:#111 !important}
.tiles-rot>*:nth-child(6n+5){background:var(--night) !important;color:#F2EFE8 !important}
.tiles-rot>*:nth-child(6n+6){background:var(--cream) !important;color:#111 !important}
.chips-rot>*:nth-child(5n+1){background:var(--sun) !important}
.chips-rot>*:nth-child(5n+2){background:var(--mint) !important}
.chips-rot>*:nth-child(5n+3){background:var(--blush) !important}
.chips-rot>*:nth-child(5n+4){background:var(--lav) !important}
.chips-rot>*:nth-child(5n+5){background:#FFFFFF !important}
@media (max-width: 760px){.deco-dsk{display:none}}
.vpill{display:inline-block;padding:0 .14em;border-radius:.12em;color:#111}
/*shared:end*/
"""
