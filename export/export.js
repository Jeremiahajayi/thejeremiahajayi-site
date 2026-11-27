// Turns the canvas .dc.html pages into a static site for Cloudflare Pages.
// Usage: node export.js <projectDir> <outDir>
const fs = require('fs');
const path = require('path');

const [, , projectDir, outDir] = process.argv;
const SITE = 'https://www.thejeremiahajayi.com';
// Google Tag Manager (container GTM-TQCD7V7B). GA4 is configured inside GTM, not here, so page views are sent once.
const GTM_ID = 'GTM-TQCD7V7B';
const GTM_HEAD = `<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','${GTM_ID}');</script>
<!-- End Google Tag Manager -->`;
// Google Analytics 4 (measurement ID G-537Y2VKCZ1), installed directly with gtag.js.
const GA4_ID = 'G-537Y2VKCZ1';
const GA4_HEAD = `<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=${GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '${GA4_ID}');
</script>`;
const GTM_BODY = `<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=${GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>`;
const ROLE = 'Marketing consultant for B2B SaaS and technology companies';

const PAGES = [
  { file: 'Home-B2.dc.html', out: 'index.html', url: '/', og: '/og-home-v2.png', title: 'Jeremiah Ajayi · Marketing consultant for B2B SaaS and technology companies', desc: 'Jeremiah Ajayi is a marketing consultant for B2B SaaS and technology companies, based in Lagos: positioning and messaging, product launches and GTM, and content and organic growth.' },
  { file: 'Site-Services.dc.html', out: 'services/index.html', url: '/services/', crumb: 'Services', title: 'B2B SaaS marketing services · Jeremiah Ajayi', desc: 'Three services for B2B SaaS and technology companies: positioning and messaging, product launches and GTM, and content and organic growth.' },
  { file: 'Site-Service-Positioning.dc.html', out: 'services/positioning-messaging/index.html', url: '/services/positioning-messaging/', crumb: 'Positioning & messaging', service: 'Positioning and messaging', title: 'Positioning and messaging consultant for B2B SaaS · Jeremiah Ajayi', desc: 'Positioning and messaging for B2B SaaS: customer research, a messaging framework and the website and sales copy that use it.' },
  { file: 'Site-Service-Launch.dc.html', out: 'services/product-launch-gtm/index.html', url: '/services/product-launch-gtm/', crumb: 'Launches & go-to-market', service: 'Product launch and go-to-market strategy', title: 'Product launch and GTM consultant for B2B SaaS · Jeremiah Ajayi', desc: 'Product launches built for pipeline: a GTM brief, launch plan, sales enablement and launch-to-pipeline measurement. 20+ launches led.' },
  { file: 'Site-Service-Content.dc.html', out: 'services/content-growth/index.html', url: '/services/content-growth/', crumb: 'Content & organic growth', service: 'Content and organic growth', title: 'Content and organic growth consultant for B2B SaaS · Jeremiah Ajayi', desc: 'Content strategy, SEO and AI search visibility for B2B SaaS, measured in pipeline. 174% organic growth at RemotePass.' },
  { file: 'Site-Industry-Fintech.dc.html', out: 'industries/b2b-fintech/index.html', url: '/industries/b2b-fintech/', crumb: 'B2B fintech', service: 'B2B fintech and HR tech marketing', title: 'B2B fintech marketing consultant: an agency alternative · Jeremiah Ajayi', desc: 'Fintech marketing for B2B payments, payroll, EOR and spend management companies: positioning, battlecards, launches and content that passes legal review. 174% organic growth at RemotePass.' },
  { file: 'Site-Work.dc.html', out: 'work/index.html', url: '/work/', crumb: 'Work', title: 'Work, case studies and portfolio · Jeremiah Ajayi', desc: 'Case studies and published work: Stears, RemotePass, Certn, Xofu, plus launch pages, search content, bylines, guides and customer stories you can read.' },
  { file: 'Site-Writing.dc.html', out: 'writing/index.html', url: '/writing/', crumb: 'Writing', title: 'Writing and research · Jeremiah Ajayi', desc: 'Original research on AI search, launch and growth teardowns, and marketing playbooks.' },
  { file: 'Site-About.dc.html', out: 'about/index.html', url: '/about/', crumb: 'About', title: 'About Jeremiah Ajayi · Marketing consultant in Lagos', desc: 'Jeremiah Ajayi is a marketing consultant for B2B SaaS and technology companies, based in Lagos, and the co-founder of EmpowerQ.' },
  { file: 'Site-EmpowerQ.dc.html', out: 'empowerq/index.html', url: '/empowerq/', crumb: 'EmpowerQ', title: 'EmpowerQ · Co-founded by Jeremiah Ajayi', desc: 'EmpowerQ builds economic inclusion for LGBTQ+ professionals in Nigeria. Co-founded by Jeremiah Ajayi in 2025.' },
  { file: 'Site-WhatIdDo.dc.html', out: 'what-id-do/index.html', url: '/what-id-do/', crumb: 'What I’d Do', og: '/og-what-id-do-v2.png', title: 'What I’d Do · What I’d do on their marketing team', desc: 'A free newsletter and live event series by Jeremiah Ajayi. Every month he studies a technology company’s marketing and explains what he’d keep, change or try, plus a live conversation with a founder or marketing leader.' },
  { file: 'Site-Contact.dc.html', out: 'contact/index.html', url: '/contact/', crumb: 'Contact', title: 'Contact · Jeremiah Ajayi', desc: 'Book a call with Jeremiah Ajayi about positioning, a product launch or content, or get in touch about a role or collaboration.' }
];
const LINKS = Object.fromEntries(PAGES.map((p) => [p.file, p.url]));

function lookup(scope, expr) {
  expr = expr.trim();
  if (expr === 'true') return true;
  if (expr === 'false') return false;
  if (/^-?\d+(\.\d+)?$/.test(expr)) return Number(expr);
  let cur = scope;
  for (const part of expr.split('.')) {
    if (cur == null) return undefined;
    cur = cur[part];
  }
  return cur;
}

function esc(v) {
  return String(v).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function holes(str, scope) {
  str = str.replace(/\s+on[A-Z]\w*="\{\{[^}]*\}\}"/g, '');
  return str.replace(/\{\{([^}]+)\}\}/g, (m, expr) => {
    if (expr.trim() === 'time') return '<span data-time></span>';
    const v = lookup(scope, expr);
    if (v == null || typeof v === 'function') return '';
    return esc(v);
  });
}

function findClose(str, from, tag) {
  const re = new RegExp(`<${tag}\\b|</${tag}>`, 'g');
  re.lastIndex = from;
  let depth = 1, m;
  while ((m = re.exec(str))) {
    depth += m[0].startsWith('</') ? -1 : 1;
    if (depth === 0) return m.index;
  }
  throw new Error('unclosed ' + tag);
}

function render(str, scope) {
  let out = '';
  let i = 0;
  const re = /<(sc-for|sc-if)\b([^>]*)>/g;
  let m;
  while ((m = re.exec(str))) {
    out += holes(str.slice(i, m.index), scope);
    const tag = m[1];
    const attrs = m[2];
    const innerStart = m.index + m[0].length;
    const close = findClose(str, innerStart, tag);
    const inner = str.slice(innerStart, close);
    if (tag === 'sc-for') {
      const listExpr = /list="\{\{([^}]+)\}\}"/.exec(attrs)[1];
      const as = /as="([^"]+)"/.exec(attrs)[1];
      const list = lookup(scope, listExpr) || [];
      list.forEach((item, idx) => { out += render(inner, Object.assign({}, scope, { [as]: item, $index: idx })); });
    } else {
      const v = lookup(scope, /value="\{\{([^}]+)\}\}"/.exec(attrs)[1]);
      if (v) out += render(inner, scope);
    }
    i = close + `</${tag}>`.length;
    re.lastIndex = i;
  }
  return out + holes(str.slice(i), scope);
}

function vals(scriptText) {
  class DCLogic {
    constructor(props) { this.props = props || {}; this.state = {}; }
    setState(s) { Object.assign(this.state, typeof s === 'function' ? s(this.state) : s); }
    forceUpdate() {}
  }
  const Component = new Function('DCLogic', scriptText + '\nreturn Component;')(DCLogic);
  const c = new Component({});
  return c.renderVals();
}

function plain(v) {
  return JSON.parse(JSON.stringify(v, (k, x) => (typeof x === 'function' ? undefined : x)));
}

const CLIENT_JS = fs.readFileSync(path.join(__dirname, 'client.js'), 'utf8');


// Map canvas asset URLs to local image files.
const BLOBS = JSON.parse(fs.readFileSync(path.join(__dirname,'..','assets','blobs.json'), 'utf8'));
const FNAME = (k) => (k.includes('.') ? k : k + '.webp');
const BLOB_TO_FILE = Object.fromEntries(Object.entries(BLOBS).map(([k, id]) => [id, FNAME(k)]));
fs.mkdirSync(path.join(outDir, 'img'), { recursive: true });
for (const k of Object.keys(BLOBS)) fs.copyFileSync(path.join(path.join(__dirname,'..','assets','web'), FNAME(k)), path.join(outDir, 'img', FNAME(k)));
const PERSON_ID = SITE + '/#person';
const PERSON = {
  '@type': 'Person', '@id': PERSON_ID,
  name: 'Jeremiah Ajayi',
  url: SITE + '/',
  jobTitle: ROLE,
  address: { '@type': 'PostalAddress', addressLocality: 'Lagos', addressCountry: 'NG' },
  sameAs: ['https://www.linkedin.com/in/jeremiah-ajayi/'],
  knowsAbout: ['Positioning and messaging', 'Product launches', 'Go-to-market strategy', 'Product marketing', 'Content marketing', 'SEO', 'Generative engine optimization', 'AI search'],
  founder: { '@id': SITE + '/empowerq/#org' }
};
const crumbs = (page) => page.url === '/' ? null : ({
  '@type': 'BreadcrumbList',
  itemListElement: [{ name: 'Home', url: '/' }]
    .concat((page.url.startsWith('/services/') && page.url !== '/services/') || page.url.startsWith('/industries/') ? [{ name: 'Services', url: '/services/' }] : [])
    .concat([{ name: page.crumb, url: page.url }])
    .map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c.name, item: SITE + c.url }))
});
function schema(page, v) {
  const g = [];
  if (page.url === '/') g.push(PERSON, { '@type': 'WebSite', '@id': SITE + '/#website', url: SITE + '/', name: 'Jeremiah Ajayi', publisher: { '@id': PERSON_ID } });
  else if (page.url === '/about/') g.push({ '@type': 'ProfilePage', url: SITE + page.url, mainEntity: PERSON });
  else g.push({ '@type': 'WebPage', url: SITE + page.url, name: page.title, author: { '@id': PERSON_ID } });
  if (page.url === '/services/') g.push({ '@type': 'ProfessionalService', '@id': SITE + '/services/#practice', name: 'Jeremiah Ajayi · Marketing consulting', url: SITE + '/services/', description: page.desc, founder: { '@id': PERSON_ID }, address: { '@type': 'PostalAddress', addressLocality: 'Lagos', addressCountry: 'NG' }, areaServed: ['Europe', 'North America', 'Middle East', 'Africa'], hasOfferCatalog: { '@type': 'OfferCatalog', name: 'Marketing services', itemListElement: ['Positioning and messaging', 'Product launch and go-to-market strategy', 'Content and organic growth', 'B2B fintech and HR tech marketing'].map((n) => ({ '@type': 'Offer', itemOffered: { '@type': 'Service', name: n } })) } });
  if (page.service) g.push({ '@type': 'Service', name: page.service, serviceType: page.service, description: page.desc, url: SITE + page.url, provider: { '@id': PERSON_ID }, areaServed: ['Europe', 'North America', 'Middle East', 'Africa'], audience: { '@type': 'BusinessAudience', name: 'B2B SaaS and technology companies' } });
  if (page.url === '/empowerq/') g.push({ '@type': 'NGO', '@id': SITE + '/empowerq/#org', name: 'EmpowerQ', legalName: 'Career Growth Initiative for the Disadvantaged', foundingDate: '2025', address: { '@type': 'PostalAddress', addressLocality: 'Lagos', addressCountry: 'NG' }, founder: { '@id': PERSON_ID } });
  if (page.url === '/what-id-do/') g.push({ '@type': 'CreativeWorkSeries', '@id': SITE + '/what-id-do/#series', name: 'What I’d Do', description: page.desc, url: SITE + page.url, inLanguage: 'en', author: { '@id': PERSON_ID }, publisher: { '@id': PERSON_ID }, genre: 'Marketing', audience: { '@type': 'Audience', audienceType: 'Founders, marketing leaders and marketing operators at technology companies' } }, { '@type': 'EventSeries', '@id': SITE + '/what-id-do/#live', name: 'What I’d Do: Live', description: 'A monthly online conversation with a founder or marketing leader about a marketing problem.', eventAttendanceMode: 'https://schema.org/OnlineEventAttendanceMode', organizer: { '@id': PERSON_ID }, location: { '@type': 'VirtualLocation', url: SITE + page.url } });
  if (Array.isArray(v.faq) && v.faq.length) g.push({ '@type': 'FAQPage', mainEntity: v.faq.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })) });
  const c = crumbs(page); if (c) g.push(c);
  return `<script type="application/ld+json">${JSON.stringify({ '@context': 'https://schema.org', '@graph': g }).replace(/</g, '\\u003c')}</script>`;
}

fs.mkdirSync(outDir, { recursive: true });
let contactLink = '';
for (const page of PAGES) {
  const src = fs.readFileSync(path.join(projectDir, page.file), 'utf8');
  if (!contactLink) { const cm = /href="(mailto:[^"?]+)/.exec(src); if (cm) contactLink = cm[1]; }
  const xdc = /<x-dc>([\s\S]*)<\/x-dc>/.exec(src)[1];
  const helmet = /<helmet>([\s\S]*?)<\/helmet>/.exec(xdc)[1];
  const body = xdc.replace(/<helmet>[\s\S]*?<\/helmet>/, '');
  const script = /<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/.exec(src)[1];
  const v = vals(script);
  let html = render(body, v);
  html = html.replace(/\/_blob\/([0-9a-f]{32})/g, (m, id) => BLOB_TO_FILE[id] ? '/img/' + BLOB_TO_FILE[id] : m);
  html = html.replace(/<div class="[^"]*" data-ph="asset"[^>]*>[\s\S]*?<\/div>/g, '').replace(/<div style="display: grid; grid-template-columns: repeat\(2, minmax\(0, 1fr\)\); gap: 14px">\s*<\/div>/g, '');
  html = html.replace(/href="([A-Za-z0-9_-]+\.dc\.html)(#[^"]*)?"/g, (m, f, hash) => `href="${(LINKS[f] || '/') + (hash || '')}"`);
  const extra = v.doors ? `<script type="application/json" id="doors-data">${JSON.stringify(plain(v.doors)).replace(/</g, '\\u003c')}</script>` : '';
  const doc = `<!doctype html>
<html lang="en">
<head>
${GA4_HEAD}
${GTM_HEAD}
${page.out === 'index.html' ? "<script>try{if(sessionStorage.getItem('jgSeen')==='1')document.documentElement.classList.add('jg-skip')}catch(e){}</script>\n" : ''}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${page.title}</title>
<meta name="description" content="${page.desc}">
<link rel="canonical" href="${SITE}${page.url}">
<meta property="og:type" content="website">
<meta property="og:title" content="${page.title}">
<meta property="og:description" content="${page.desc}">
<meta property="og:url" content="${SITE}${page.url}">
<meta property="og:image" content="${SITE}${page.og || '/og.png'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
${helmet.trim()}
${schema(page, v)}
</head>
<body>
${GTM_BODY}
${html.trim()}
${extra}
<script>${CLIENT_JS}</script>
</body>
</html>
`;
  const outPath = path.join(outDir, page.out);
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, doc);
  const leftover = (doc.match(/\{\{|<sc-|onClick=/g) || []).length;
  const placeholders = (doc.match(/\[[A-Z][A-Z ]+\]/g) || []);
  console.log(page.out, doc.length, 'template leftovers:', leftover, 'placeholders:', [...new Set(placeholders)].join(', '));
}

fs.writeFileSync(path.join(outDir, 'favicon.svg'), '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#FF5A2A"/><text x="32" y="42" font-family="Arial, sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#111" letter-spacing="-2">JA</text></svg>');
fs.writeFileSync(path.join(outDir, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${SITE}/sitemap.xml\n`);
fs.writeFileSync(path.join(outDir, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${PAGES.map((p) => `  <url><loc>${SITE}${p.url}</loc></url>`).join('\n')}\n</urlset>\n`);
fs.writeFileSync(path.join(outDir, 'llms.txt'), `# Jeremiah Ajayi

> ${ROLE}, based in Lagos, Nigeria. Three services: positioning and messaging, product launches and go-to-market, and content and organic growth. Works with teams in Europe, North America, the Middle East and Africa. Also co-founder and Executive Director of EmpowerQ, a nonprofit for the economic inclusion of LGBTQ+ professionals in Nigeria.

## Services

- [Services overview](${SITE}/services/): who it's for, engagement models and how pricing is scoped
- [Positioning and messaging](${SITE}/services/positioning-messaging/): customer research, positioning, messaging frameworks, website and sales copy
- [Product launch and GTM](${SITE}/services/product-launch-gtm/): GTM briefs, launch plans, sales enablement, launch-to-pipeline measurement; 20+ launches led
- [Content and organic growth](${SITE}/services/content-growth/): content strategy, SEO and AI search visibility; 174% organic growth at RemotePass
- [B2B fintech marketing](${SITE}/industries/b2b-fintech/): positioning, battlecards, launches and compliant content for B2B fintech and HR tech (payments, payroll, EOR, spend management)

## Free tools

- [GTM Readiness Scorecard](${SITE}/resources/gtm-scorecard/)
- [Marketing Function Audit](${SITE}/resources/marketing-audit/)
- [Category Visibility Audit](${SITE}/resources/category-visibility-audit/)
- [B2B SaaS product launch checklist](${SITE}/resources/b2b-saas-launch-checklist/): 33 steps with launch tiers, from GTM brief to 30-day review

## Proof

- [Work](${SITE}/work/): Stears Elections (#1 on Google above the BBC), RemotePass × Certn (270+ media pickups), RemotePass content ($500K+ pipeline in under a year), Xofu repositioning; $3M+ pipeline influenced overall
- [What I’d Do](${SITE}/what-id-do/): a free newsletter and monthly live event series about solving marketing problems
- [Blog](${SITE}/blog/): articles on marketing, product launches, content and AI search
- [Writing](${SITE}/writing/): AI search research, including The State of AI Search in Nigeria and four Foundation Labs studies
- [About](${SITE}/about/): background, recognition and education

## Other

- [EmpowerQ](${SITE}/empowerq/): programmes including Lavender Ladder, a 2026 Social Shifters finalist
- [Contact](${SITE}/contact/): ${contactLink} · https://www.linkedin.com/in/jeremiah-ajayi/
`);
fs.writeFileSync(path.join(outDir, '_redirects'), `# Old Wix URLs
/successstories /work/ 301
/successstories/ /work/ 301
/portfolio /work/#published 301
/portfolio/ /work/#published 301
/expertise /services/ 301
/expertise/ /services/ 301
# Before launch: migrate the Wix posts to /post/<slug> and the tool pages
# (/gtm-scorecard, /categoryvisibilityaudit, /marketingaudit) at their current paths.
`);
console.log('done');

// 404 page: reuse the Contact page shell, swap the main content.
{
  const shell = fs.readFileSync(path.join(outDir, 'contact/index.html'), 'utf8');
  const start = shell.indexOf('<section');
  const end = shell.lastIndexOf('<section', shell.indexOf('<footer'));
  const main = `<section class="grid-bg" style="min-height: 60vh"><div style="max-width: 1360px; margin: 0 auto; padding: clamp(96px, 12vw, 160px) 28px">
<p style="margin: 0 0 20px; font-size: 14px; font-weight: 700; color: #B5B0A6">404 · 🧭 Wrong turn</p>
<h1 class="sg" style="margin: 0; font-weight: 700; font-size: clamp(56px, 8.4vw, 136px); line-height: 0.88; letter-spacing: -0.065em">This page didn’t<br><span style="color: #FF5A2A">land.</span></h1>
<p style="margin: 28px 0 0; max-width: 560px; font-size: 19px; line-height: 1.6; color: #D8D3C9">It may have moved when the site was rebuilt. Try one of these instead.</p>
<div style="margin-top: 36px; display: flex; flex-wrap: wrap; gap: 12px">
<a class="btn-o" href="/" style="display: inline-flex; align-items: center; min-height: 56px; padding: 0 28px; border-radius: 999px; font-weight: 700">Home</a>
<a class="btn-l" href="/services/" style="display: inline-flex; align-items: center; min-height: 56px; padding: 0 28px; border-radius: 999px; font-weight: 600">Services</a>
<a class="btn-l" href="/work/" style="display: inline-flex; align-items: center; min-height: 56px; padding: 0 28px; border-radius: 999px; font-weight: 600">Work</a>
<a class="btn-l" href="/blog/" style="display: inline-flex; align-items: center; min-height: 56px; padding: 0 28px; border-radius: 999px; font-weight: 600">Writing</a>
</div></div></section>
`;
  let page = shell.slice(0, start) + main + shell.slice(end);
  page = page.replace(/<title>[^<]*<\/title>/, '<title>Page not found · Jeremiah Ajayi</title>')
    .replace(/<link rel="canonical"[^>]*>\n/, '').replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"')
    .replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>\n?/, '');
  fs.writeFileSync(path.join(outDir, '404.html'), page);
}
for (const f of ['og.png', 'og-home-v2.png', 'og-what-id-do-v2.png']) { const og = path.join(__dirname, '..', 'og', f); if (fs.existsSync(og)) fs.copyFileSync(og, path.join(outDir, f)); }

// Free tools: the original scorecards, restyled, at their existing URLs.
{
  const shell = fs.readFileSync(path.join(outDir, 'contact/index.html'), 'utf8');
  const start = shell.indexOf('<section');
  const end = shell.lastIndexOf('<section', shell.indexOf('<footer'));
  const tools = [
    { id: 'gtm-scorecard', slug: 'gtm-scorecard', desc: 'A free 15-question self-assessment of go-to-market readiness across positioning, sales alignment, content, launches and team, with an action plan.' },
    { id: 'marketingaudit', slug: 'marketing-audit', desc: 'A free 16-question audit of your marketing function across strategy, execution, alignment and measurement, with prioritised next steps.' },
    { id: 'b2b-saas-launch-checklist', slug: 'b2b-saas-launch-checklist', isNew: true, kind: 'checklist', desc: 'A free B2B SaaS product launch checklist: 33 steps from the GTM brief to the 30-day review, with launch tiers, so your launch creates sales conversations. Interactive, printable and free.' },
    { id: 'categoryvisibilityaudit', slug: 'category-visibility-audit', desc: 'A free diagnostic for B2B founders and CMOs: score your visibility across AI search, content, positioning and pipeline, with prioritised next steps.' }
  ];
  const faqOf = (b) => { const qs = [...b.matchAll(/<details><summary>([\s\S]*?)<\/summary><p>([\s\S]*?)<\/p><\/details>/g)].map((m) => ({ '@type': 'Question', name: m[1], acceptedAnswer: { '@type': 'Answer', text: m[2] } })); return qs.length ? [{ '@type': 'FAQPage', mainEntity: qs }] : []; };
  const extraUrls = [];
  const redirects = ['# Free tools moved to /resources/ (Nov 2026)'];
  for (const t of tools) {
    const body = fs.readFileSync(path.join(__dirname, '..', 'tools', t.id + '.html'), 'utf8');
    const title = fs.readFileSync(path.join(__dirname, '..', 'tools', t.id + '.title'), 'utf8').trim().replace(/\s*\|\s*Jeremiah Ajayi$/, '') + ' · Jeremiah Ajayi';
    let page = shell.slice(0, start) + body + shell.slice(end);
    page = page.replace(/<title>[^<]*<\/title>/, '<title>' + title + '</title>')
      .replace(/<meta name="description" content="[^"]*">/, '<meta name="description" content="' + t.desc + '">')
      .replace(/<link rel="canonical" href="[^"]*">/, '<link rel="canonical" href="' + SITE + '/resources/' + t.slug + '/">')
      .replace(/<meta property="og:url" content="[^"]*">/, '<meta property="og:url" content="' + SITE + '/resources/' + t.slug + '/">')
      .replace(/<meta property="og:title" content="[^"]*">/, '<meta property="og:title" content="' + title + '">')
      .replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>\n?/, '<script type="application/ld+json">' + JSON.stringify({ '@context': 'https://schema.org', '@graph': [(t.kind === 'checklist' ? { '@type': 'WebPage', name: title.replace(/ · Jeremiah Ajayi$/, ''), url: SITE + '/resources/' + t.slug + '/', description: t.desc, isAccessibleForFree: true, author: { '@id': PERSON_ID }, datePublished: '2026-11-27' } : { '@type': 'WebApplication', name: title.replace(/ · Jeremiah Ajayi$/, ''), url: SITE + '/resources/' + t.slug + '/', description: t.desc, applicationCategory: 'BusinessApplication', operatingSystem: 'Any', isAccessibleForFree: true, offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' }, author: { '@id': PERSON_ID } })].concat(faqOf(body)).concat([{ '@type': 'BreadcrumbList', itemListElement: [{ '@type': 'ListItem', position: 1, name: 'Home', item: SITE + '/' }, { '@type': 'ListItem', position: 2, name: title.replace(/ · Jeremiah Ajayi$/, ''), item: SITE + '/resources/' + t.slug + '/' }] }]) }).replace(/</g, '\\u003c') + '</script>\n');
    fs.mkdirSync(path.join(outDir, 'resources', t.slug), { recursive: true });
    fs.writeFileSync(path.join(outDir, 'resources', t.slug, 'index.html'), page);
    extraUrls.push(SITE + '/resources/' + t.slug + '/');
    if (!t.isNew) redirects.push('/' + t.id + ' /resources/' + t.slug + '/ 301', '/' + t.id + '/ /resources/' + t.slug + '/ 301');
  }
  const smPath = path.join(outDir, 'sitemap.xml');
  if (fs.existsSync(smPath)) {
    const sm = fs.readFileSync(smPath, 'utf8');
    fs.writeFileSync(smPath, sm.replace('</urlset>', extraUrls.map((u) => '  <url><loc>' + u + '</loc></url>\n').join('') + '</urlset>'));
  }
  const rd = path.join(outDir, '_redirects');
  fs.writeFileSync(rd, fs.readFileSync(rd, 'utf8').replace('# Before launch: migrate the Wix posts to /post/<slug> and the tool pages\n# (/gtm-scorecard, /categoryvisibilityaudit, /marketingaudit) at their current paths.\n', '') + redirects.join('\n') + '\n/resources /services/ 302\n/resources/ /services/ 302\n/industries /industries/b2b-fintech/ 302\n/industries/ /industries/b2b-fintech/ 302\n');
}

// Blog posts migrated from Wix, kept at their original /post/<slug> addresses.
{
  const postsFile = path.join(__dirname, '..', 'posts', 'posts.json');
  if (fs.existsSync(postsFile)) {
    const posts = JSON.parse(fs.readFileSync(postsFile, 'utf8'));
    const shell = fs.readFileSync(path.join(outDir, 'contact/index.html'), 'utf8');
    const start = shell.indexOf('<section');
    const end = shell.lastIndexOf('<section', shell.indexOf('<footer'));
    const imgSrc = path.join(__dirname, '..', 'posts', 'img');
    fs.mkdirSync(path.join(outDir, 'post-img'), { recursive: true });
    for (const f of fs.readdirSync(imgSrc)) fs.copyFileSync(path.join(imgSrc, f), path.join(outDir, 'post-img', f));
    fs.mkdirSync(path.join(outDir, 'post'), { recursive: true });
    const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    const fmt = (d) => new Date(d).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Africa/Lagos' });
    const css = `<style>
.post-body{max-width:720px;margin:0 auto;font-size:19px;line-height:1.75;color:#2D2B27}
.post-body p{margin:0 0 1.15em}
.post-body h2{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:clamp(28px,3vw,38px);line-height:1.1;letter-spacing:-.035em;color:#111;margin:1.8em 0 .6em}
.post-body h3{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:clamp(22px,2.2vw,27px);line-height:1.2;letter-spacing:-.025em;color:#111;margin:1.5em 0 .5em}
.post-body h4{font-size:19px;font-weight:700;color:#111;margin:1.4em 0 .4em}
.post-body a{color:#C23A0E;text-decoration:underline;text-underline-offset:3px}
.post-body a:hover{color:#111}
.post-body u{text-decoration:none}
.post-body ul,.post-body ol{margin:0 0 1.2em;padding-left:1.3em}
.post-body li{margin:.35em 0}
.post-body blockquote{margin:1.6em 0;padding:4px 0 4px 22px;border-left:4px solid #FF5A2A;font-family:'Space Grotesk',sans-serif;font-size:22px;line-height:1.4;color:#111}
.post-body figure{margin:1.8em 0}
.post-body img{display:block;width:100%;height:auto;border-radius:12px;background:#E6E1D6}
.post-body figcaption{margin-top:10px;font-size:14px;color:#6B675F}
.post-body table{width:100%;border-collapse:collapse;font-size:15px;line-height:1.5;margin:1.6em 0;display:block;overflow-x:auto}
.post-body th,.post-body td{border-bottom:1px solid #D9D3C7;padding:10px 12px;text-align:left;vertical-align:top}
.post-body th{border-bottom:2px solid #111;color:#111}
.post-body hr{border:0;border-top:1px solid #D9D3C7;margin:2.2em 0}
.post-body code{font-size:.9em;background:#E6E1D6;padding:2px 6px;border-radius:4px}
</style>`;
    const urls = [];
    for (const p of posts) {
      let body = p.html.replace(/<\/(p|h2|h3|h4|ul|ol|figure|blockquote|table)><br>/g, '</$1>').replace(/^(<br>)+|(<br>)+$/g, '').replace(/<a([^>]*)><u>([\s\S]*?)<\/u><\/a>/g, '<a$1>$2</a>');
      body = body.replace(/<a [^>]*href="\/blog\/hashtags\/[^"]*"[^>]*>([\s\S]*?)<\/a>/g, '$1'); // Wix hashtag pages no longer exist
      body = body.replace(/<a href="(https?:\/\/(?!www\.thejeremiahajayi\.com|thejeremiahajayi\.com)[^"]+)"/g, '<a href="$1" rel="noopener" target="_blank"');
      // Wix table-of-contents links point at heading ids that were not exported: match each link to its heading by text.
      { const strip = (h) => h.replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim().toLowerCase();
        const toc = [...body.matchAll(/<a href="#([^"]+)"[^>]*>([\s\S]*?)<\/a>/g)].map((m) => [m[1], strip(m[2])]);
        for (const [id, text] of toc) {
          let done = false;
          body = body.replace(/<(h2|h3|h4)>([\s\S]*?)<\/\1>/g, (m, t, inner) => { if (done || !text) return m; const h = strip(inner); if (h === text || h.startsWith(text)) { done = true; return `<${t} id="${id}">${inner}</${t}>`; } return m; });
        } }
      const words = body.replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length;
      const mins = Math.max(1, Math.round(words / 230));
      const url = SITE + '/post/' + p.slug;
      const cover = p.cover ? SITE + '/post-img/' + p.cover : SITE + '/og.png';
      // drop a leading image identical to the cover so it is not shown twice
      if (p.cover) body = body.replace(new RegExp('^<figure><img src="/post-img/' + p.cover.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '"[^>]*></figure>'), '');
      const ld = { '@context': 'https://schema.org', '@type': 'BlogPosting', headline: p.title, description: p.desc, datePublished: p.date, dateModified: p.modified || p.date, image: cover, url, mainEntityOfPage: url, author: { '@type': 'Person', '@id': SITE + '/#person', name: 'Jeremiah Ajayi', url: SITE + '/about/' }, publisher: { '@id': SITE + '/#person' } };
      const main = `${css}
<article>
<header style="background: #F2EFE8; color: #111">
<div style="max-width: 960px; margin: 0 auto; padding: clamp(56px, 7vw, 96px) 28px clamp(36px, 4vw, 56px)">
<nav aria-label="Breadcrumb" style="font-size: 14px; color: #6B675F; margin-bottom: 24px"><a class="nd" href="/blog/">Writing</a> <span aria-hidden="true">/</span> <span style="color: #111">Article</span></nav>
<h1 class="sg" style="margin: 0; font-weight: 600; font-size: clamp(38px, 5.2vw, 72px); line-height: 1; letter-spacing: -0.05em">${esc(p.title)}</h1>
<p style="margin: 24px 0 0; max-width: 720px; font-size: 20px; line-height: 1.55; color: #2D2B27">${esc(p.desc)}</p>
<p style="margin: 24px 0 0; display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 14px; font-weight: 600; color: #6B675F"><span style="color: #111">Jeremiah Ajayi</span><span>${fmt(p.date)}</span><span>${mins} min read</span></p>
</div>
${p.cover ? `<div style="max-width: 1100px; margin: 0 auto; padding: 0 28px clamp(48px, 6vw, 72px)"><img src="/post-img/${p.cover}" alt="" style="display: block; width: 100%; height: auto; border-radius: 16px; background: #E6E1D6"></div>` : ''}
</header>
<div style="background: #FFFFFF; padding: clamp(56px, 7vw, 88px) 28px">
<div class="post-body">${body}</div>
</div>
</article>
<section style="background: #F2EFE8; color: #111">
<div style="max-width: 960px; margin: 0 auto; padding: clamp(64px, 8vw, 96px) 28px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 16px">
<a class="path" href="/services/" style="display: flex; flex-direction: column; gap: 12px; padding: 26px; border-radius: 16px; background: #FF5A2A; color: #111"><span style="font-size: 13px; font-weight: 700">Work with me</span><span class="sg" style="font-size: 24px; font-weight: 600; letter-spacing: -0.03em; line-height: 1.1">Positioning, launches and content for B2B SaaS teams.</span><span style="margin-top: auto; font-weight: 700">See the services →</span></a>
<a class="path" href="/blog/" style="display: flex; flex-direction: column; gap: 12px; padding: 26px; border-radius: 16px; background: #111; color: #F2EFE8"><span style="font-size: 13px; font-weight: 700; color: #FF5A2A">Keep reading</span><span class="sg" style="font-size: 24px; font-weight: 600; letter-spacing: -0.03em; line-height: 1.1">Research on AI search, launch teardowns and playbooks.</span><span style="margin-top: auto; font-weight: 700">All writing →</span></a>
</div>
</section>
`;
      let page = shell.slice(0, start) + main + shell.slice(end);
      const title = esc(p.title) + ' · Jeremiah Ajayi';
      page = page.replace(/<title>[^<]*<\/title>/, '<title>' + title + '</title>')
        .replace(/<meta name="description" content="[^"]*">/, '<meta name="description" content="' + esc(p.desc) + '">')
        .replace(/<link rel="canonical" href="[^"]*">/, '<link rel="canonical" href="' + url + '">')
        .replace(/<meta property="og:type" content="[^"]*">/, '<meta property="og:type" content="article">')
        .replace(/<meta property="og:title" content="[^"]*">/, '<meta property="og:title" content="' + title + '">')
        .replace(/<meta property="og:description" content="[^"]*">/, '<meta property="og:description" content="' + esc(p.desc) + '">')
        .replace(/<meta property="og:url" content="[^"]*">/, '<meta property="og:url" content="' + url + '">')
        .replace(/<meta property="og:image" content="[^"]*">/, '<meta property="og:image" content="' + cover + '">')
        .replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, '<script type="application/ld+json">' + JSON.stringify(ld).replace(/</g, '\\u003c') + '</script>')
        .replace(/class="nl nav-on"/g, 'class="nl"').replace('<a class="nl" href="/blog/">Writing</a>', '<a class="nl nav-on" href="/blog/" aria-current="page">Writing</a>');
      fs.writeFileSync(path.join(outDir, 'post', p.slug + '.html'), page);
      urls.push(url);
    }
    const smPath = path.join(outDir, 'sitemap.xml');
    const sm = fs.readFileSync(smPath, 'utf8');
    fs.writeFileSync(smPath, sm.replace('</urlset>', urls.map((u) => '  <url><loc>' + u + '</loc></url>\n').join('') + '</urlset>'));
    const rd = path.join(outDir, '_redirects');
    fs.writeFileSync(rd, fs.readFileSync(rd, 'utf8').replace(/# Before launch: migrate the Wix posts[^\n]*\n/, '# Blog posts are migrated at their original /post/<slug> addresses.\n'));
    console.log('posts', posts.length);
  }
}

// The blog now runs on WordPress at /blog (src/worker.js proxies it). The research hub is /writing/.
// Old /post/<slug> addresses redirect to /blog/<slug>/ in the worker, so the static copies are removed.
{
  const postsFile = path.join(__dirname, '..', 'posts', 'posts.json');
  const posts = fs.existsSync(postsFile) ? JSON.parse(fs.readFileSync(postsFile, 'utf8')) : [];
  fs.rmSync(path.join(outDir, 'post'), { recursive: true, force: true });
  const smPath = path.join(outDir, 'sitemap.xml');
  fs.writeFileSync(smPath, fs.readFileSync(smPath, 'utf8').replace(/  <url><loc>[^<]*\/post\/[^<]*<\/loc><\/url>\n/g, ''));
  fs.writeFileSync(path.join(outDir, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${SITE}/sitemap.xml\nSitemap: ${SITE}/blog/sitemap_index.xml\n`);
  const rd = path.join(outDir, '_redirects');
  fs.writeFileSync(rd, fs.readFileSync(rd, 'utf8').replace(/# Blog posts are migrated[^\n]*\n/, '# Blog posts live on WordPress at /blog/<slug>/; /post/<slug> redirects there (src/worker.js).\n'));
  const walk = (d) => fs.readdirSync(d, { withFileTypes: true }).flatMap((e) => e.isDirectory() ? walk(path.join(d, e.name)) : [path.join(d, e.name)]);
  let n = 0;
  for (const f of walk(outDir).filter((f) => /\.(html|txt|xml)$/.test(f))) {
    const src = fs.readFileSync(f, 'utf8');
    const out = src.replace(/(https:\/\/www\.thejeremiahajayi\.com)?\/post\/([a-z0-9-]+)(\.html)?(?=["'#?\s<)])/g, (m, host, slug) => (host || '') + '/blog/' + slug + '/');
    if (out !== src) { fs.writeFileSync(f, out); n++; }
  }
  console.log('blog on WordPress: post links rewritten in', n, 'files;', posts.length, 'posts redirect from /post/');
}
