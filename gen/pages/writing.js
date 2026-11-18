  initialState() { return { cat: 'all', q: '' }; }
  renderVals() {
    const B = 'https://www.thejeremiahajayi.com/post/';
    const posts = [
      { cat: 'gtm', where: 'My site', meta: '3 Nov 2026', title: 'How to turn a B2B product launch into sales conversations', dek: 'What Arrows’ relaunch shows about the gap between launch attention and pipeline.', href: B + 'saas-product-launch-proof-gap' },
      { cat: 'ai', where: 'My site', meta: '21 Oct 2026', title: 'Who owns AEO? Hiring lessons from 40 job listings', dek: 'What companies expect from AI-search hires, and how they split the work.', href: B + 'who-owns-aeo-hiring-lessons' },
      { cat: 'gtm', where: 'My site', meta: '15 Oct 2026', title: 'Does founder-led content work? Data from 530 LinkedIn posts', dek: 'Comparing fintech brands with their founders on LinkedIn, post by post.', href: B + 'does-founder-led-content-work-data-from-530-linkedin-posts' },
      { cat: 'ai', where: 'My site', meta: '24 Sep 2026', title: 'OPay, Kuda and Moniepoint: what AI recommends as the best digital bank in Nigeria', dek: 'One prompt, four AI platforms, run twice.', href: B + 'opay-kuda-and-moniepoint-what-ai-recommends-as-the-best-digital-bank-in-nigeria' },
      { cat: 'ai', where: 'My site', meta: '18 Sep 2026', title: 'AEO and GEO: a simple guide to how AI search works', dek: 'A plain-language explainer for marketers.', href: B + 'aeo-and-geo-a-simple-guide-to-how-ai-search-works' },
      { cat: 'gtm', where: 'My site', meta: '2 Sep 2026', title: 'Granola is growing without a big editorial engine. Can that last?', dek: 'A small search footprint, fast adoption, and a crowding category.', href: B + 'granola-growth-strategy' },
      { cat: 'ai', where: 'My site', meta: '12 Aug 2026', title: 'Why AI keeps recommending PiggyVest for savings in Nigeria', dek: 'PiggyVest appeared in 14 of 15 answers. Where that story comes from.', href: B + 'why-ai-recommends-piggyvest' },
      { cat: 'ai', where: 'My site', meta: '7 Aug 2026', title: 'Best savings apps in Nigeria according to ChatGPT, Gemini and Perplexity', dek: 'What three AI tools recommend, and which brands they leave out.', href: B + 'best-savings-apps-in-nigeria-according-to-chatgpt-gemini-perplexity' },
      { cat: 'play', where: 'My site', meta: '6 Aug 2026', title: 'The three marketing checks I’d run before spending another dollar', dek: 'Category visibility, marketing function health and GTM readiness.', href: B + 'the-three-marketing-audit-tools-i-d-run-before-spending-another-dollar' },
      { cat: 'gtm', where: 'My site', meta: '23 Jul 2026', title: 'What comes after investor attention? A GTM analysis of Scale, Raven and Metrifox', dek: 'Three Nigerian startups, three different GTM challenges.', href: B + 'scale-raven-metrifox-gtm-analysis' },
      { cat: 'gtm', where: 'My site', meta: '9 Jul 2026', title: 'How do you know if B2B research is working? A teardown of 5 companies', dek: 'A scorecard for research reports, applied to Muck Rack, Ashby, Attest, Customer.io and AppFollow.', href: B + 'how-to-measure-b2b-research' },
      { cat: 'personal', where: 'My site', meta: '1 Jul 2026', title: 'The life I chose after the life I planned', dek: 'Leaving law, starting again, and graduating first class.', href: B + 'the-life-i-chose-after-the-life-i-planned' },
      { cat: 'gtm', where: 'My site', meta: '29 Apr 2026', title: 'How to run a local content strategy that scales globally', dek: 'Why the strongest strategies start narrow.', href: B + 'how-to-run-a-local-content-strategy-that-scales-globally' },
      { cat: 'play', where: 'My site', meta: '11 Feb 2026', title: '30+ resources that have made me a better marketer', dek: 'The books, newsletters and tools I keep coming back to.', href: B + '30-resources-that-have-made-me-a-better-marketer' },
      { cat: 'gtm', where: 'My site', meta: '9 Dec 2025', title: 'The 5 critical leaks killing your startup’s growth', dek: 'Where go-to-market quietly breaks down, and how to fix it.', href: B + 'the-5-critical-leaks-killing-your-startup-s-growth-and-how-to-fix-them' },
      { cat: 'play', where: 'My site', meta: '2 Dec 2025', title: 'A marketing manager’s guide to building a reliable freelance team', dek: 'How I built RemotePass’ first freelance content team.', href: B + 'a-marketing-manager-s-guide-to-building-a-reliable-freelance-team' },
      { cat: 'play', where: 'My site', meta: '25 Nov 2025', title: 'The template that turns your content audit into a growth lever', dek: 'A free template that scores business value, SEO and ICP fit.', href: B + 'the-template-that-turns-your-content-audit-from-spreadsheet-to-growth-lever' },
      { cat: 'play', where: 'My site', meta: '4 Nov 2025', title: 'The 90-day plan that helped me earn C-suite trust at RemotePass', dek: 'The 30/60/90 plan I used to go from new hire to trusted strategist.', href: B + 'the-90-day-plan-that-helped-me-earn-c-suite-trust-at-remotepass' },
      { cat: 'press', where: 'ProductLed', meta: 'Guest post', title: 'Product-led marketing and GTM strategy', dek: 'How product-led thinking shapes go-to-market.', href: 'https://productled.com/blog/product-led-marketing-gtm-strategy' },
      { cat: 'press', where: 'Product Marketing Alliance', meta: 'Guest post', title: '7 systems that let me coordinate 15 launches', dek: 'The launch systems I built at RemotePass.', href: 'https://www.productmarketingalliance.com/7-systems-that-let-me-coordinate-15-launches/' },
      { cat: 'press', where: 'Buffer', meta: '2023', title: 'How to be a consistent content creator', dek: 'Guest post. Ranked #1 on Google for its main search phrase.', href: 'https://buffer.com/resources/consistent-content-creator/' },
      { cat: 'press', where: 'Condia', meta: '2022', title: 'Succeeding in tech as a non-technical talent', dek: 'Insights from 20+ professionals. Condia’s 2nd most-read article of 2022.', href: 'http://benjamindada.com/succeeding-tech-non-technical-person-20-experts/' },
      { cat: 'press', where: 'Condia', meta: 'Series', title: 'How to know if your startup is venture-scalable', dek: 'The Investors’ Corner, with Kola Aina of Ventures Platform.', href: 'https://thecondia.com/kola-aina-vc-funding-africa-venture-scale/' },
      { cat: 'press', where: 'Condia', meta: 'Series', title: 'How to attract VC funding in today’s market', dek: 'The Investors’ Corner, with Basil Moftah of Nclude.', href: 'https://thecondia.com/attract-vc-funding-africa-basil-moftah/' },
      { cat: 'press', where: 'Condia', meta: 'Essay', title: 'Surviving VC-funded startups as a marketer', dek: 'Advice from marketing leaders at Flutterwave and PiggyVest.', href: 'https://thecondia.com/marketing-tips-startup-growth/' }
    ];
    const cats = [ { id: 'all', label: 'All' }, { id: 'ai', label: 'AI search' }, { id: 'gtm', label: 'GTM & growth' }, { id: 'play', label: 'Playbooks' }, { id: 'press', label: 'Published elsewhere' }, { id: 'personal', label: 'Personal' } ];
    const cur = this.state.cat;
    const q = (this.state.q || '').trim().toLowerCase();
    const match = (p) => !q || (p.title + ' ' + p.dek + ' ' + p.where).toLowerCase().indexOf(q) !== -1;
    return {
      time: this.state.time,
      studies: [
        { no: '01', subject: 'n8n', big: '16%', title: 'The Ghost Citation', finding: 'Of the citations behind n8n’s AI answers, only about 16% came from n8n’s own sites.', href: 'https://foundationinc.co/lab/n8n-ghost-citation-audit', bg: '#FF5A2A', fg: '#111' },
        { no: '02', subject: 'ClickUp', big: '0/12', title: 'Model Drift', finding: 'Named in 97.5% of discovery answers, recommended in none of 12 head-to-head comparisons.', href: 'https://foundationinc.co/lab/model-drift-clickup-ai-visibility', bg: '#F2EFE8', fg: '#111' },
        { no: '03', subject: 'ATS category', big: '73%', title: 'The Versus Layer', finding: 'Of the evidence in head-to-head answers, 73% came from outside the vendors being compared.', href: 'https://foundationinc.co/lab/versus-layer-ai-comparison-pages/', bg: '#2A2926', fg: '#F2EFE8' },
        { no: '04', subject: 'Docker', big: '54%', title: 'The Docs Dividend', finding: 'Docs were 54% of Docker’s own citations, but scale and upkeep explained the lead.', href: 'https://foundationinc.co/lab/docker-docs-ai-citations', bg: '#2A2926', fg: '#F2EFE8' }
      ],
      filters: cats.map((c) => ({ id: c.id, label: c.label, count: c.id === 'all' ? posts.length : posts.filter((p) => p.cat === c.id).length, pressed: c.id === cur ? 'true' : 'false', bg: c.id === cur ? '#111' : 'transparent', fg: c.id === cur ? '#F2EFE8' : '#111', border: c.id === cur ? '#111' : '#C9C3B6', pick: () => this.setState({ cat: c.id }) })),
      shown: posts.filter((p) => (cur === 'all' || p.cat === cur) && match(p)).map((p) => ({ ...p, text: (p.title + ' ' + p.dek + ' ' + p.where).toLowerCase() })),
      q: this.state.q || '',
      onSearch: (e) => this.setState({ q: e.target.value }),
      noneDisplay: posts.filter((p) => (cur === 'all' || p.cat === cur) && match(p)).length === 0 ? 'block' : 'none',
      none: posts.filter((p) => (cur === 'all' || p.cat === cur) && match(p)).length === 0,
      featured: [
        { big: '530', unit: 'LinkedIn posts', title: 'Does founder-led content work?', dek: 'Six fintech brands against their founders, post by post.', href: B + 'does-founder-led-content-work-data-from-530-linkedin-posts', bg: '#FF5A2A', fg: '#111' },
        { big: '40', unit: 'job listings', title: 'Who owns AEO? Hiring lessons', dek: 'What companies expect from AI-search hires, and how they split the work.', href: B + 'who-owns-aeo-hiring-lessons', bg: '#111', fg: '#F2EFE8' },
        { big: '14/15', unit: 'AI answers', title: 'Why AI keeps recommending PiggyVest', dek: 'Where one brand’s AI dominance in Nigerian savings comes from.', href: B + 'why-ai-recommends-piggyvest', bg: '#FFFFFF', fg: '#111' }
      ],
      features: [
        { who: 'Accrue', what: 'Spotlight: this marketer wants to earn $7K next. How can he do it?', href: 'https://blog.useaccrue.com/this-marketer-wants-to-earn-7k-next-how-can-he-do-it' },
        { who: 'Wimbart', what: 'Profile on becoming a recognised voice in African tech writing (2024)', href: 'https://wimbart.com/media-spotlight/jeremiah-ajayi-benjamindada/' },
        { who: 'Smarketers Hub', what: 'Career lessons from my path into tech (2023)', href: 'https://www.smarketershub.com/blog/career-lessons-from-jeremiah-ajayi-senior-content-marketer-at-stears' },
        { who: 'Smarketers Hub', what: 'Featured in The Essential Guide to Landing International Remote Marketing Roles (2025)', href: 'https://www.smarketershub.com/blog/landing-international-remote-marketing-roles' },
        { who: 'Product Marketing Alliance', what: 'Contributing writer for a 100K+ audience', href: 'https://productmarketingalliance.com/author/jeremiah' },
        { who: 'Africa Fintech Marketing Report', what: 'Co-author. Featured by 30+ media outlets', href: 'https://bitcoinke.io/wp-content/uploads/2024/03/Fintech-Marketing-Outlook-Nigeria-2024-BitKE.pdf' }
      ]
    };
  }
