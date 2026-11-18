  renderVals() {
    const S = 'https://www.thejeremiahajayi.com/post/';
    return {
      time: this.state.time,
      svc: {
        slug: 'content-growth', name: 'Content & organic growth', verb: 'travel',
        title: 'Content and organic growth consultant for B2B SaaS',
        intro: 'Content buyers trust, that search engines and AI assistants surface, measured in pipeline rather than volume. SEO and AI search are part of the method, not separate offers.',
        stats: [ { big: '174%', label: 'organic user acquisition growth at RemotePass, year on year' }, { big: '$500K+', label: 'pipeline influenced by content in under a year' }, { big: '#1', label: 'above the BBC on Google for Stears' } ],
        forWho: [ { t: 'Marketing leaders who need content tied to pipeline' }, { t: 'Founders whose site attracts little organic demand' }, { t: 'Teams losing clicks as buyers ask ChatGPT and Perplexity instead of Google' } ],
        signs: [ { t: 'You publish a lot, but little of it turns into pipeline.' }, { t: 'Organic traffic is flat or falling as AI answers take clicks.' }, { t: 'AI assistants recommend your competitors, not you.' }, { t: 'Content depends on one person and stops when they’re busy.' }, { t: 'Sales doesn’t use what marketing publishes.' } ],
        getsTitle: 'A content engine that compounds.',
        gets: [
          { n: '01', h: 'Content strategy', t: 'Mapped to the questions buyers ask at each stage, and the gaps competitors miss.' },
          { n: '02', h: 'Editorial engine', t: 'Briefs, templates and a writing team that can publish at scale without losing quality.' },
          { n: '03', h: 'Pages at scale', t: 'Programmatic and templated pages where real demand justifies them, plus localized content.' },
          { n: '04', h: 'Search and AI visibility', t: 'Technical SEO, pages AI can quote, and tracking of how often AI answers mention you.' },
          { n: '05', h: 'Distribution', t: 'Email, partners, communities and the sources AI already trusts.' },
          { n: '06', h: 'Measurement', t: 'Pipeline and qualified leads first, then organic users and AI answer share.' }
        ],
        extraTitle: 'How AI search fits',
        extraText: 'Buyers now ask AI assistants for recommendations. My research for Foundation Labs found that only about 16% of the citations behind n8n’s AI answers came from n8n’s own sites. So the work covers your pages and the outside sources AI relies on.',
        extra: [ { t: 'At RemotePass: AI answer share grew from 10% to 40% of tracked prompts' }, { t: 'Co-author of The State of AI Search in Nigeria' } ],
        extraLink: 'Site-Writing.dc.html', extraLinkLabel: 'Read the research',
        steps: [
          { n: '1', h: 'Find the gap', t: 'Search demand, AI answers, sales objections and what competitors miss.' },
          { n: '2', h: 'Build the system', t: 'Strategy, templates, briefs and the team to publish.' },
          { n: '3', h: 'Publish and distribute', t: 'Search, AI answers, email, partners and the places buyers already read.' },
          { n: '4', h: 'Measure', t: 'Pipeline, qualified leads, organic users and AI answer share, reported monthly.' }
        ],
        proofTitle: 'Content that reached buyers, and pipeline.',
        cases: [
          { client: 'RemotePass', year: '2024–25', big: '174%', title: 'A content engine built for pipeline', result: 'About 40 country guides and an English–Arabic MENA hub; $500K+ pipeline in under a year.', href: 'Site-Work.dc.html#engine', bg: '#111', fg: '#F2EFE8' },
          { client: 'Stears', year: '2023', big: '#1', title: 'How a new election tracker beat the BBC on Google', result: '10,000+ programmatic candidate pages and 1.9M+ users, 52% from search.', href: 'Site-Work.dc.html#stears', bg: '#FF5A2A', fg: '#111' }
        ],
        hasQuote: true, quote: 'From day one, he was full of ideas on how we could improve our product growth. He also demonstrated exemplary ownership to drive the execution and reporting on business impact.', quoteName: 'Adetoro Adeniran', quoteOrg: 'Stears',
        note: '',
        tool: { name: 'Category Visibility Audit', line: 'See how visible your brand is in search and AI answers for your category.', href: 'https://www.thejeremiahajayi.com/categoryvisibilityaudit' },
        paired: { name: 'Positioning & messaging', line: 'Content scales whatever story you have. Make sure it’s the right one.', href: 'Site-Service-Positioning.dc.html' },
        reading: [
          { title: 'AEO and GEO: a simple guide to how AI search works', where: 'My site', href: S + 'aeo-and-geo-a-simple-guide-to-how-ai-search-works' },
          { title: 'Why AI keeps recommending PiggyVest for savings in Nigeria', where: 'My site', href: S + 'why-ai-recommends-piggyvest' }
        ]
      },
      faq: [
        { q: 'How quickly will we see results?', a: 'Leading signals move first: rankings, AI answer mentions and engagement on new pages. Pipeline follows as content builds up. I report on both, so you can see progress before the pipeline numbers arrive.' },
        { q: 'Who writes the content?', a: 'I set the strategy and edit everything. Writing can come from me, your team, or a freelance team I brief and manage, as I did at RemotePass.' },
        { q: 'How do you measure success?', a: 'Pipeline and qualified leads first. Then organic users, rankings for buying-stage searches, and how often AI assistants mention or cite you.' },
        { q: 'What’s the difference between SEO and AI search?', a: 'AI search sits on top of SEO. Search engines still decide much of what AI reads, but AI also leans heavily on outside sources such as reviews, comparisons and communities. Good content work now covers both.' },
        { q: 'What proof should I ask a content consultant for?', a: 'Named results with a timeframe, examples of the actual content, how they connected it to pipeline, and someone you can speak to. That’s the standard I hold my own work to.' }
      ]
    };
  }
