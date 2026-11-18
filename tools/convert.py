import re,sys
for name in ['gtm-scorecard','marketingaudit']:
    s=open(f'{__import__('os').path.dirname(__import__('os').path.abspath(__file__))}/{name}.src.html').read()
    css=re.search(r'<style>(.*?)</style>',s,re.S).group(1)
    body=re.search(r'<body>(.*)</body>',s,re.S).group(1)
    title=re.search(r'<title>(.*?)</title>',s).group(1)
    # scope css
    css=re.sub(r'\*, \*::before, \*::after \{[^}]*\}', ".tool *, .tool *::before, .tool *::after { box-sizing: border-box; margin: 0; padding: 0; font-family: 'DM Sans', sans-serif; }", css, count=1)
    css=re.sub(r'html, body \{[^}]*\}','',css,count=1)
    css=re.sub(r'(^|\n)body \{', r'\1.tool {', css)
    css=re.sub(r'body \{ padding', '.tool { padding', css)
    css=css.replace('.tool {\n  background: #F4F4F4;','.tool {\n  max-width: 860px; margin: 0 auto;\n  background: #F2EFE8;')
    css=css.replace("'Poppins', sans-serif","'DM Sans', sans-serif")
    css=css.replace('.header','.t-header').replace('#0A0A0A','#111111').replace('#F4F4F4','#F2EFE8')
    css=css.replace('font-weight: 300;','font-weight: 400;').replace('font-weight: 200;','font-weight: 500;')
    css+="""
.tool .t-header-title, .tool .cta-heading, .tool .footer-heading, .tool .total-num, .tool .pill-val, .tool .next-steps-title { font-family: 'Space Grotesk', sans-serif; letter-spacing: -.04em; }
.tool .t-header-title em, .tool .cta-heading em { font-style: normal; color: #C23A0E; }
.tool .footer-btn, .tool .cta-btn { background: #FF5A2A; color: #111111; border-radius: 999px; }
.tool .btn-cta { border-radius: 999px; }
.tool-wrap { background: #F2EFE8; }
"""
    body=body.replace('class="header"','class="t-header"').replace('class="header-','class="t-header-')
    css=css.replace('.t-header-','.t-header-')
    # neutralise Wix iframe resize
    body=re.sub(r'function reportHeight\(\) \{.*?\n\}', 'function reportHeight() {}', body, count=1, flags=re.S)
    out=f'<style>{css}</style>\n<section class="tool-wrap"><div class="tool">{body}</div></section>\n'
    open(f'{__import__('os').path.dirname(__import__('os').path.abspath(__file__))}/{name}.html','w').write(out)
    open(f'{__import__('os').path.dirname(__import__('os').path.abspath(__file__))}/{name}.title','w').write(title)
    print(name, len(out), 'reportHeight() {}' in out)
