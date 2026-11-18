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
<a class="btn-o nav-cta" href="Site-Contact.dc.html">Book a call ↗</a>
</nav>
</div>
</header>'''


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
/*shared:end*/
"""
