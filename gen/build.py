#!/usr/bin/env python3
"""Assemble the inner site pages from shared chrome + per-page bodies.

Usage: python3 build.py <page-id> [...]
Each page lives in pages/<id>.html (markup) and pages/<id>.js (renderVals body).
"""
import sys, pathlib, re

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / 'project'

NAV = [
    ('Work', 'Site-Work.dc.html'),
    ('Expertise', 'Site-Services.dc.html'),
    ('EmpowerQ', 'Site-EmpowerQ.dc.html'),
    ('Writing', 'Site-Writing.dc.html'),
    ('About', 'Site-About.dc.html'),
]

PAGES = {
    'work': ('Site-Work.dc.html', 'Work · Jeremiah Ajayi', 'Work', 7000),
    'services': ('Site-Services.dc.html', 'Services · Jeremiah Ajayi', 'Expertise', 6000),
    'svc-launch': ('Site-Service-Launch.dc.html', 'Product launch and GTM consultant · Jeremiah Ajayi', 'Expertise', 7200),
    'svc-positioning': ('Site-Service-Positioning.dc.html', 'Positioning and messaging consultant · Jeremiah Ajayi', 'Expertise', 7000),
    'svc-content': ('Site-Service-Content.dc.html', 'Content and organic growth consultant · Jeremiah Ajayi', 'Expertise', 7200),
    'contact': ('Site-Contact.dc.html', 'Contact · Jeremiah Ajayi', None, 2600),
    'empowerq': ('Site-EmpowerQ.dc.html', 'EmpowerQ · Jeremiah Ajayi', 'EmpowerQ', 6400),
    'writing': ('Site-Writing.dc.html', 'Writing & research · Jeremiah Ajayi', 'Writing', 5600),
    'about': ('Site-About.dc.html', 'About · Jeremiah Ajayi', 'About', 6600),
}

FOOT = [
    ('Positioning', 'Site-Service-Positioning.dc.html'),
    ('Launches & GTM', 'Site-Service-Launch.dc.html'),
    ('Content & growth', 'Site-Service-Content.dc.html'),
    ('Work', 'Site-Work.dc.html'),
    ('Writing', 'Site-Writing.dc.html'),
    ('About', 'Site-About.dc.html'),
    ('EmpowerQ', 'Site-EmpowerQ.dc.html'),
    ('Contact', 'Site-Contact.dc.html'),
    ('LinkedIn', 'https://www.linkedin.com/in/jeremiah-ajayi/'),
]

TEMPLATE = {}

CAL = 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi'
MAIL = 'jeremiah@thejeremiahajayi.com'

EXTRA_CSS = """
.nav-on{color:#FF5A2A !important}
.chip{font:inherit;cursor:pointer;transition:background .3s,color .3s,border-color .3s}
.chip:hover{border-color:#111}
.card-l{text-decoration:none;color:#111;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.card-l:hover{transform:translateY(-6px)}
.card-l:hover .card-t{color:#C23A0E}
.anch{text-decoration:none;color:inherit;transition:color .25s}
.anch:hover{color:#FF5A2A}
"""


def header(active):
    links = []
    for label, href in NAV:
        cls = 'nl nav-on' if label == active else 'nl'
        cur = ' aria-current="page"' if label == active else ''
        links.append(f'<a class="{cls}" href="{href}"{cur}>{label}</a>')
    return f'''<header style="position: sticky; top: 0; z-index: 40; background: rgba(17,17,17,0.9); backdrop-filter: blur(12px); border-bottom: 1px solid #2B2A27">
<div style="max-width: 1360px; margin: 0 auto; padding: 12px 28px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 28px">
<a href="Home-B2.dc.html" class="nl sg" style="display: inline-flex; align-items: center; gap: 10px; font-weight: 700; font-size: 21px; letter-spacing: -0.04em">
<span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 9px; background: #FF5A2A; color: #111; font-size: 16px; letter-spacing: -0.06em">JA</span>Jeremiah Ajayi</a>
<nav aria-label="Primary" style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px 26px; font-size: 15px; font-weight: 500">
{chr(10).join(links)}
<a class="btn-o" href="Site-Contact.dc.html" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 22px; border-radius: 999px; font-weight: 700">Book a call ↗</a>
</nav>
</div>
</header>'''


def contact_band(title_html):
    return f'''<section id="contact" style="background: #111; color: #F2EFE8">
<div style="max-width: 1360px; margin: 0 auto; padding: clamp(96px, 12vw, 152px) 28px clamp(48px, 6vw, 72px)">
<h2 class="sg" style="margin: 0; font-weight: 700; font-size: clamp(52px, 7.6vw, 120px); line-height: 0.9; letter-spacing: -0.065em">{title_html}</h2>
<div style="margin-top: clamp(36px, 4vw, 52px); display: flex; flex-wrap: wrap; gap: 14px">
<a class="btn-o" href="{CAL}" style="display: inline-flex; align-items: center; min-height: 58px; padding: 0 28px; border-radius: 999px; font-size: 17px; font-weight: 700">Book a call ↗</a>
<a class="btn-l" href="mailto:{MAIL}" style="display: inline-flex; align-items: center; min-height: 58px; padding: 0 28px; border-radius: 999px; font-size: 17px; font-weight: 600">{MAIL}</a>
<a class="btn-l" href="https://www.linkedin.com/in/jeremiah-ajayi/" style="display: inline-flex; align-items: center; min-height: 58px; padding: 0 28px; border-radius: 999px; font-size: 17px; font-weight: 600">LinkedIn</a>
</div>
<footer style="margin-top: clamp(72px, 9vw, 112px); padding-top: 22px; border-top: 1px solid #2B2A27; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; font-size: 14px; color: #B5B0A6">
<a href="Home-B2.dc.html" class="nl sg" style="display: inline-flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 700; letter-spacing: -0.04em"><span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; border-radius: 8px; background: #FF5A2A; color: #111; font-size: 14px">JA</span>Jeremiah Ajayi</a>
<span style="display: flex; flex-wrap: wrap; gap: 8px 22px">{''.join(f'<a class="nl" href="{h}">{l}</a>' for l, h in FOOT)}<span>Lagos · {{{{time}}}} · © 2026</span></span>
</footer>
</div>
</section>'''


def footer_only():
    return f'''<section style="background: #111; color: #F2EFE8">
<div style="max-width: 1360px; margin: 0 auto; padding: 0 28px clamp(40px, 5vw, 64px)">
<footer style="padding-top: 22px; border-top: 1px solid #2B2A27; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; font-size: 14px; color: #B5B0A6">
<a href="Home-B2.dc.html" class="nl sg" style="display: inline-flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 700; letter-spacing: -0.04em"><span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; border-radius: 8px; background: #FF5A2A; color: #111; font-size: 14px">JA</span>Jeremiah Ajayi</a>
<span style="display: flex; flex-wrap: wrap; gap: 8px 22px">{''.join(f'<a class="nl" href="{h}">{l}</a>' for l, h in FOOT)}<span>Lagos · {{{{time}}}} · © 2026</span></span>
</footer>
</div>
</section>'''


def build(pid):
    fname, title, active, height = PAGES[pid]
    body = (ROOT / 'pages' / f'{TEMPLATE.get(pid, pid)}.html').read_text()
    js = (ROOT / 'pages' / f'{pid}.js').read_text()
    helmet = (ROOT / 'helmet.html').read_text().replace('</style>', EXTRA_CSS + '</style>')
    m = re.search(r'<!--CONTACT:(.*?)-->', body, re.S)
    if '<!--NOBAND-->' in body:
        band = footer_only()
    else:
        band = contact_band(m.group(1).strip() if m else 'Let’s talk<span style="color: #FF5A2A">.</span>')
    body = body.replace('<!--NOBAND-->', '')
    body = re.sub(r'<!--CONTACT:.*?-->', '', body, flags=re.S)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{helmet}
<div style="width: 100%; min-height: 100vh; background: #111111; color: #F2EFE8; font-family: 'DM Sans', system-ui, sans-serif; box-sizing: border-box; overflow-x: hidden">
{header(active)}
{body}
{band}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{height}}}}}'>
class Component extends DCLogic {{
  constructor(props) {{
    super(props);
    this.state = Object.assign({{ time: this.lagosTime() }}, this.initialState ? this.initialState() : {{}});
  }}
  lagosTime() {{
    try {{ return new Intl.DateTimeFormat('en-GB', {{ hour: '2-digit', minute: '2-digit', timeZone: 'Africa/Lagos' }}).format(new Date()); }} catch (e) {{ return ''; }}
  }}
  componentDidMount() {{ this.timer = setInterval(() => this.setState({{ time: this.lagosTime() }}), 30000); }}
  componentWillUnmount() {{ clearInterval(this.timer); }}
{js}
}}
</script>
</body>
</html>
'''
    (OUT / fname).write_text(html)
    print('wrote', fname, len(html))


if __name__ == '__main__':
    for pid in sys.argv[1:]:
        build(pid)
