  initialState() { return { f: 'all' }; }
  renderVals() {
    const B = (id) => '/_blob/' + id;
    const img = {
      certnCheck: B('bf5746c3149793e151b4bc8233744e8b'), certnFlow: B('0dbab7ea27d1f6520f47891673fd0b97'), certnTeam: B('059d23d54fba852a7e2e28c2b4ef3db4'), certnSecured: B('36e76e09b9ca821b9929e0aefe6a563a'),
      timeoff: B('ef8d3efbfc1194e978574d9eb50ef96f'), wafeq: B('c7e58c431da5738727e39bea1b223b8d'),
      ksaRisks: B('11081f461253fb84fb4a4bb9bf11f88b'), ksaProblem: B('a05b79e6e02bc194855c581a19c30ed7'), ksaDirect: B('ab07fb1e23df7a3120b313684011d40c'), ksaCompare: B('8c1cfd21b8b0bd938501fbe875856a81'), ksaBefore: B('ae131050871cb1bad40ce559611da459'), ksaGosi: B('a16a3080e0b34e3d5e47ee597cfc4eb8'), ksaLaptop: B('89d9fecea4c00f909e23139b6e195ac7'),
      qbWhy: B('c3cb1759fffe47bc7bbed1cc3895d701'), qbMap: B('6e5af8e26a7f2dfa147986123957a4dc'), qbBeforeAfter: B('0252db9b8b96b18de3ef0a937db12529'),
      dfs: B('7b26ce554a84b7e8f8efc0c9b7b09d2e'), workforce: B('c33058fb79f973e3ab514f97af5a6e9a'),
      xofuHero: B('0dfa31b585c479139da9600a8bdd8b9d'), xofuPricing: B('a4cbf106e17930bec111332800b706fd'), xofuNewsletter: B('690c37a910717b44a095316769f59bf8'), xofuApp: B('cc9262829253a37970c303777c8535fa')
    };
    const wallItems = [
      { src: B('fc39c3db9800ffc1933e240a5186b657'), alt: 'Stears Elections presidential results page', w: 374, h: 233 },
      { src: img.certnTeam, alt: 'RemotePass × Certn launch visual', w: 380, h: 233 },
      { src: img.ksaRisks, alt: 'KSA Payroll launch carousel: Risks of manual payroll in Saudi Arabia', w: 188, h: 233 },
      { src: img.wafeq, alt: 'Announcement visual for the RemotePass and Wafeq integration', w: 416, h: 233 },
      { src: img.qbWhy, alt: 'QuickBooks integration launch post', w: 188, h: 233 },
      { src: img.timeoff, alt: 'Time-Off Policies launch visual', w: 416, h: 233 },
      { src: img.ksaCompare, alt: 'KSA Payroll carousel comparing local providers with RemotePass', w: 188, h: 233 },
      { src: img.dfs, alt: 'Dubai Fintech Summit 2025 countdown post', w: 233, h: 233 },
      { src: img.xofuPricing, alt: 'Xofu pricing page draft with four tiers', w: 401, h: 233 },
      { src: img.ksaBefore, alt: 'Before KSA Payroll campaign post', w: 188, h: 233 },
      { src: img.certnCheck, alt: 'Background check completed, Certn integration visual', w: 380, h: 233 },
      { src: img.workforce, alt: '2025 to 2026 workforce trends report cover', w: 416, h: 233 }
    ];
    const tags = { pos: 'Positioning & messaging', launch: 'Launches & go-to-market', content: 'Content & storytelling' };
    const projects = [
      { k: 'content', client: 'Stears', year: '2023', big: '#1', bigLabel: 'on Google for “2023 election results”, above the BBC, CNN and INEC', title: 'How a new election tracker beat the BBC on Google', href: '#stears', deep: true, dark: true },
      { k: 'launch', client: 'RemotePass × Certn', year: '2024', big: '270+', bigLabel: 'media pickups, including Yahoo Finance, Fox and NBC', title: 'The partnership launch that went global', href: '#certn', deep: true, orange: true },
      { k: 'launch', client: 'RemotePass', year: '2024–25', big: '15+', bigLabel: 'launches, in a year company revenue grew 134%', title: 'A launch program built for pipeline', href: '#launches', deep: true },
      { k: 'launch', client: 'RemotePass', year: 'Ask AI', big: 'Record', bigLabel: 'MQL performance after launch, with sales flooded with enquiries', title: 'Everyone was selling AI. We sold the answer.', href: '#askai', deep: true, orange: true },
      { k: 'content', client: 'RemotePass', year: '2024–25', big: '$192K', bigLabel: 'revenue from inbound content in Q1 2025 alone, with no ad spend; 174% organic user growth', title: 'A content engine that turned search into revenue', href: '#engine', deep: true },
      { k: 'pos', client: 'Xofu', year: '2026', big: '3.7%', bigLabel: 'launch email click-through, double the previous best', title: 'Giving a new AI product one clear question to answer', href: '#xofu', deep: true, dark: true },
      { k: 'launch', client: 'RemotePass × Wafeq', year: '2025', big: '103', bigLabel: 'pieces of coverage in the UAE and Saudi Arabia, 56 of them in Arabic', title: 'A regional integration, launched in two languages', href: '#launches' },
      { k: 'launch', client: 'Stears', year: '2023', big: '$70K+', bigLabel: 'qualified pipeline from the FX Monitor launch', title: 'Taking a data product to market after the B2B pivot', href: '#stears' },
      { k: 'content', client: 'Stears', year: '2023', big: '54%', bigLabel: 'newsletter open rate, with a 6.4% click-through rate', title: 'Redesigning the email program for B2B buyers', href: '#stears' },
      { k: 'content', client: 'PiggyVest', year: '2022', big: '40K+', bigLabel: 'app downloads and 100,000 readers', title: 'Storytelling about real money decisions', href: 'Site-Contact.dc.html' },
      { k: 'content', client: 'VEC Studio', year: '2021–22', big: '+49%', bigLabel: 'monthly organic traffic for a B2B SaaS client', title: 'Product-led content for SEON, Kittl and Blackthorn', href: 'Site-Contact.dc.html' },
      { k: 'content', client: 'Africa Fintech Marketing Report', year: 'Co-author', big: '30+', bigLabel: 'media outlets featured the report', title: 'Mapping how African fintechs market themselves', href: 'Site-Contact.dc.html' },
      { k: 'pos', client: 'Consulting', year: '2018–now', big: '5', bigLabel: 'Northzone, the Earthshot Prize, Africa Fintech Summit, SEON and Sokin', title: 'GTM and campaign projects for global organisations', href: 'Site-Contact.dc.html' }
    ];

    const RP = 'https://www.remotepass.com';
    const samples = [
      { id: 'pw-launch', label: 'Launch pages and sales content', note: 'Copy that explains a product clearly enough for buyers to act on it.', items: [
        { who: 'Xofu', t: 'Website and product messaging for an AI visibility platform', d: 'Homepage, free snapshot offer and product pages, all built around one buyer question: does AI recommend you when buyers shortlist vendors?', links: [ { l: 'Homepage', h: 'https://xofu.com/' }, { l: 'BOFU Visibility Snapshot', h: 'https://xofu.com/bofu' }, { l: 'How Xofu works', h: 'https://xofu.com/how-xofu-works' } ] },
        { who: 'RemotePass', t: 'Ask AI launch page', h: RP + '/ai', d: 'Positioned an AI feature as a secure way to query workforce data, not another chatbot. Sales saw record MQLs after launch.' },
        { who: 'RemotePass', t: 'APIs product page', h: RP + '/apis', d: 'Sells the outcome (fewer disconnected systems, cleaner workforce data) to buyers who will never read the API docs.' },
        { who: 'RemotePass', t: 'How RemotePass solves global hiring for HR, finance and legal', h: RP + '/blog/how-remotepass-solves-the-global-hiring-headache-for-hr-finance-and-legal-teams', d: 'One article that answers three buying teams’ objections, so sales could send it before the first call.' },
        { who: 'RemotePass', t: 'What the RemotePass EOR platform can and can’t do', h: RP + '/blog/what-remotepass-eor-platform-can-and-cant-do', d: 'Names the product’s limits up front, so prospects arrive with accurate expectations and leads fit better.' }
      ] },
      { id: 'pw-search', label: 'Content that ranks and brings in leads', note: 'Search assets built to win specific queries and turn readers into pipeline.', items: [
        { who: 'RemotePass', t: 'Global Contractor Rate Index', h: RP + '/blog/global-contractor-rates-2025', d: '#1 on Google for “global contractor rates” and cited in the AI Overview. Inbound leads from 20+ markets.' },
        { who: 'RemotePass', t: 'MENA HR & Payroll Hub', h: RP + '/mena-hr-payroll-hub', d: 'Strategy, site structure and technical SEO for UAE, Saudi, DIFC and ADGM topic clusters. Organic blog traffic grew to 50,000 visits a month and organic leads doubled.' },
        { who: 'RemotePass', t: 'Country guides', h: RP + '/countryguide', d: 'A repeatable system that turns each market’s hiring, payroll, tax and compliance rules into searchable guides that lead to EOR and payroll.' },
        { who: 'RemotePass', t: 'Remote work glossary', h: RP + '/remote-work-glossary', d: 'A to Z definitions built to win “what is” searches and build authority across EOR, payroll and contractor management.' },
        { who: 'RemotePass', t: 'Hybrid work content cluster', d: 'Two linked articles that take HR leaders from choosing a hybrid model to writing and rolling out the policy.', links: [ { l: 'Part 1: Models and foundations', h: RP + '/blog/remote-vs-in-office-bridging-the-divide-with-a-winning-hybrid-work-strategy' }, { l: 'Part 2: Execution framework', h: RP + '/blog/how-to-create-a-win-win-hybrid-work-policy-for-your-team' } ] },
        { who: 'Africa Fintech Summit', t: 'Fintech Marketing Report (co-author)', h: 'https://bitcoinke.io/wp-content/uploads/2024/03/Fintech-Marketing-Outlook-Nigeria-2024-BitKE.pdf', d: 'The first report on how Nigerian fintechs market themselves. Covered by 30+ media outlets.' }
      ] },
      { id: 'pw-bylines', label: 'Bylines and thought leadership', note: 'Frameworks from my own launches and teams, published where marketers read.', items: [
        { who: 'Product Marketing Alliance', t: '7 systems that let me coordinate 15+ launches without burnout', h: 'https://www.productmarketingalliance.com/7-systems-that-let-me-coordinate-15-launches/', d: 'The operating systems behind 11+ RemotePass launches across EMEA, APAC and North America.' },
        { who: 'Product Marketing Alliance', t: 'How I turned sales call chaos into GTM gold', h: 'https://www.productmarketingalliance.com/how-i-turned-sales-call-chaos-into-gtm-gold/', d: 'A three-step method for mining sales calls for buyer language, objections and positioning gaps.' },
        { who: 'Product Marketing Alliance', t: 'The Compete or Carve framework', h: 'https://www.productmarketingalliance.com/the-compete-or-carve-framework/', d: 'Four questions for deciding whether to fight in an existing category or create a new one.' },
        { who: 'Product Marketing Alliance', t: 'Messaging for multi-product companies', h: 'https://www.productmarketingalliance.com/messaging-for-multi-product-companies/', d: 'How to keep one clear story when several products and buyer types pull in different directions. Drawn from Stears and RemotePass.' },
        { who: 'Product Marketing Alliance', t: 'The 5 steps that took me from content marketer to PMM', h: 'https://www.productmarketingalliance.com/the-5-steps-that-helped-me-go-from-content-marketer-to-pmm/', d: 'A first-hand account of the move, and one of the PMA community’s most-shared career pieces.' },
        { who: 'ProductLed', t: 'Product-led marketing in a downturn', h: 'https://productled.com/blog/product-led-marketing-gtm-strategy', d: 'How to use the product itself to drive acquisition, activation and retention when budgets shrink.' },
        { who: 'Buffer', t: '5 tips that made me a consistent content creator', h: 'https://buffer.com/resources/consistent-content-creator/', d: 'A systems-first way to publish consistently alongside a full-time job. Ranked #1 on Google for its main phrase.' },
        { who: 'The Condia', t: 'How to execute community-led growth', h: 'https://thecondia.com/nigerian-startups-community-led-growth/', d: 'A playbook for Nigerian startups building an audience before they can afford to buy one.' },
        { who: 'RemotePass', t: 'How SMBs can compete for global talent', h: RP + '/blog/how-smbs-can-compete-for-top-talent-in-a-global-hiring-market-in-2025', d: 'Positions RemotePass as a strategic partner for smaller companies, not just a payroll tool.' },
        { who: 'RemotePass', t: 'The new $100K H-1B fee: a founder’s guide', h: RP + '/blog/the-new-100k-h1b-fee-a-founders-guide-to-global-talent-without-it', d: 'Published inside the news cycle to reach US founders rethinking how they hire.' },
        { who: 'VEC Studio', t: 'VC content marketing: First Round Capital’s playbook', h: 'https://victoreduoh.com/vc-content-marketing-first-round-capital-content-playbook/', d: 'How First Round uses long-form content to earn founders’ trust, written for a client copying the model.' },
        { who: 'Guide', t: 'Hiring global talent without Bay Area salaries', h: 'https://docs.google.com/document/d/1a_hWTNfAElKTLxcfhaSn74NzRteaix8n/edit', d: 'The financial case for early-stage founders to hire globally by default.' }
      ] },
      { id: 'pw-guides', label: 'Guides, toolkits and templates', note: 'Gated and downloadable assets built to capture demand.', items: [
        { who: 'Toolkit · 50+ pages', t: 'Contractor hiring toolkit', h: 'https://drive.google.com/file/d/1pNuYLGgN9QxatTP4CMc3oOvbB8V3AZpI/view', d: 'Classification, compliance, onboarding, payments and country tax rules, with templates and checklists.' },
        { who: 'Playbook', t: 'A founder’s playbook for hiring global talent', h: 'https://drive.google.com/file/d/1-T2xq4Wrd4cA5wELzKu0v-OhR_jaoI8r/view', d: 'Where, when and how to hire abroad, and when to use contractors, an EOR, a contractor of record or your own entity.' },
        { who: 'Template', t: 'Strategic HR plan template', h: 'https://docs.google.com/document/d/1z6KgU_a2PijIEPuH4UCoTwZjMSYIzmxV/edit', d: 'An eight-step template that ties people priorities to business goals, from objectives to quarterly reviews.' },
        { who: 'Report', t: 'The annual leave guide', h: 'https://drive.google.com/file/d/1VgkJhZ2X4i8tOGpQaAVP6wRilZtwx_Co/view', d: 'Statutory leave rules across 150+ countries, still bringing in organic traffic from HR teams.' }
      ] },
      { id: 'pw-stories', label: 'Customer stories', note: 'Proof sales could send to buyers.', items: [
        { who: 'RemotePass', t: 'Customer case study series', d: 'Problem, solution and result stories that gave sales credible proof for buyers comparing platforms.', links: [ { l: 'Podeo: 32% headcount growth, AED 50K+ saved', h: RP + '/case-studies/podeo' }, { l: 'Pemo: 7× team growth, onboarding under 10 minutes', h: RP + '/case-studies/pemo' }, { l: 'Moniepoint: payroll from five days to one', h: RP + '/case-studies/moniepoint' } ] }
      ] }
    ];
    const f = this.state.f;
    const filters = [{ id: 'all', label: 'All' }, { id: 'pos', label: 'Positioning' }, { id: 'launch', label: 'Launches' }, { id: 'content', label: 'Content' }];
    return {
      time: this.state.time,
      headline: [
        { big: '$3M+', label: 'pipeline influenced across my work', color: '#111' },
        { big: '20+', label: 'product launches led', color: '#111' },
        { big: '#1', label: 'above the BBC on Google for Stears', color: '#111' },
        { big: '270+', label: 'media pickups for one launch', color: '#111' }
      ],
      wall: wallItems.concat(wallItems),
      jumps: [
        { n: '01', href: '#stears', t: 'Stears Elections', s: 'Content' },
        { n: '02', href: '#certn', t: 'RemotePass × Certn', s: 'Launch' },
        { n: '03', href: '#launches', t: 'RemotePass launches', s: 'Launch' },
        { n: '04', href: '#askai', t: 'RemotePass Ask AI', s: 'Launch' },
        { n: '05', href: '#engine', t: 'RemotePass content engine', s: 'Content' },
        { n: '06', href: '#xofu', t: 'Xofu', s: 'Positioning' }
      ],
      stears: {
        did: [
          { n: '01', t: 'Built the SEO strategy from scratch for searches like “2023 election results” and “presidential candidates Nigeria”.' },
          { n: '02', t: 'Designed programmatic candidate profiles: 10,000+ pages covering every candidate for governor, senate and president.' },
          { n: '03', t: 'Trained the analyst team, mostly economists, to publish for search, with a framework used across hundreds of articles.' },
          { n: '04', t: 'Coordinated editorial, engineering, data and design so pages stayed accurate and fast at peak traffic.' }
        ],
        below: [ { t: 'BBC' }, { t: 'CNN' }, { t: 'INEC' } ],
        results: [ { big: '1.9M+', label: 'users, 52% from organic search' }, { big: '10K+', label: 'programmatic candidate pages' }, { big: '$70K+', label: 'qualified pipeline from the FX Monitor launch that followed' }, { big: '54%', label: 'newsletter open rate after the B2B redesign' } ],
        cited: 'Cited by the Financial Times, Quartz and Al Jazeera'
      },
      certn: {
        mosaic: [
          { i: 1, src: img.certnTeam, alt: 'Launch visual showing a global hiring team being screened', span: 'span 2', ratio: '1600 / 981' },
          { i: 2, src: img.certnCheck, alt: 'Launch visual: a completed background check report, powered by Certn', span: 'span 1', ratio: '1600 / 981' },
          { i: 3, src: img.certnSecured, alt: 'Launch visual: candidate data secured by Certn', span: 'span 1', ratio: '1600 / 980' }
        ],
        did: [
          { h: 'Positioning', t: 'Framed the integration as proof RemotePass was the safer, more compliant choice for regulated industries.' },
          { h: 'Partner alignment', t: 'Agreed the launch narrative and timing with Certn’s global marketing team.' },
          { h: 'Launch', t: 'Ran the launch content: global and Middle East press releases, the announcement blog, email and social posts.' },
          { h: 'Sales', t: 'Built the enablement kit so the team could use the launch in live deals.' }
        ],
        outlets: 'Yahoo Finance · Fox · NBC'
      },
      launches: {
        strip: [
          { src: img.certnFlow, alt: 'RemotePass and Certn integration visual', name: 'Background checks with Certn', when: '2024', w: 420 },
          { src: img.timeoff, alt: 'Time-Off Policies launch visual', name: 'Time-Off Policies', when: '2024', w: 420 },
          { src: img.wafeq, alt: 'Wafeq integration announcement visual', name: 'Wafeq integration', when: 'March 2025', w: 420 },
          { src: img.qbBeforeAfter, alt: 'QuickBooks integration before and after visual', name: 'QuickBooks integration', when: '2025', w: 400 },
          { src: img.ksaLaptop, alt: 'KSA Payroll product visual on a laptop', name: 'KSA Payroll', when: '2025', w: 420 },
          { src: img.dfs, alt: 'Dubai Fintech Summit countdown post', name: 'Dubai Fintech Summit', when: 'May 2025', w: 240 }
        ],
        log: [ { t: 'Ask AI' }, { t: 'Background checks (Certn)' }, { t: 'Time-Off Policies' }, { t: 'Org Chart' }, { t: 'Local Payroll' }, { t: 'KSA Payroll' }, { t: 'Open APIs' }, { t: 'Automations' }, { t: 'Bill Pay' }, { t: 'Bulk Actions' }, { t: 'Calendar revamp' }, { t: 'Contractor of Record' }, { t: 'Direct Employees' }, { t: 'QuickBooks' }, { t: 'Zapier' }, { t: 'Slack' }, { t: 'Wafeq' } ],
        steps: [
          { n: '1', h: 'Brief', t: 'Turned product specs into a customer story and a launch tier.' },
          { n: '2', h: 'Enable', t: 'Gave sales one-pagers, decks, FAQs and talk tracks before launch day.' },
          { n: '3', h: 'Launch', t: 'Blog, email, landing page, social, PR and partner posts, in English and Arabic where the market needed it.' },
          { n: '4', h: 'Measure', t: 'Reported adoption and pipeline, and fed lessons into the next launch.' }
        ]
      },
      engine: {
        posts: [
          { i: 1, src: img.ksaRisks, alt: 'Carousel cover: Risks of manual payroll in Saudi Arabia', rot: 'rotate(-4deg)', y: '18px' },
          { i: 2, src: img.ksaProblem, alt: 'Carousel slide: the problem with payroll in KSA', rot: 'rotate(0deg)', y: '0px' },
          { i: 3, src: img.ksaCompare, alt: 'Carousel slide comparing a local payroll provider with RemotePass', rot: 'rotate(4deg)', y: '18px' }
        ],
        hub: [ { t: 'EOR in the UAE' }, { t: 'EOR in Saudi Arabia' }, { t: 'UAE payroll' }, { t: 'KSA payroll' } ],
        guides: [ { t: 'Hiring in the UAE' }, { t: 'DIFC hiring guide' }, { t: 'ADGM hiring guide' }, { t: 'Contractors in Saudi Arabia' }, { t: 'Iqama sponsorship' }, { t: 'Saudization requirements' }, { t: 'Hiring in Egypt' } ],
        did: [
          { t: 'Built a content strategy around the questions buyers ask before hiring abroad, with about 40 country guides.' },
          { t: 'Created an English–Arabic MENA HR and payroll hub linking service pages, hiring guides and compliance explainers.' },
          { t: 'Turned sales objections and launch topics into content, produced with a freelance team I hired and briefed.' },
          { t: 'Wrote the GEO playbook and tracked AI answers across ChatGPT, Perplexity, Gemini and Google AI Overviews.' }
        ],
        results: [ { big: '174%', label: 'organic user acquisition, year on year' }, { big: '$500K+', label: 'pipeline influenced by content, in under a year' } ]
      },
      askai: {
        story: [
          { h: 'The insight', t: 'HR leaders, our customers and prospects, kept telling us they never had time to explore their own workforce data. Most competitors had not built a story on that.' },
          { h: 'What we made', t: 'One story from the landing page to the announcement video to the sales enablement documents, so buyers heard the same promise at every step.' },
          { h: 'My role', t: 'Led the campaign as Content Marketing Manager: the angle, the story and keeping it consistent across every channel.' }
        ],
        prompts: [
          { t: 'Where is my team located and how much are we spending by country?' },
          { t: 'Which contracts expire next month? Draft the renewals.' },
          { t: 'What are our top expenses this quarter?' }
        ],
        touch: [
          { n: '01', h: 'Landing page', s: 'remotepass.com/ai', href: 'https://www.remotepass.com/ai', go: '↗', bg: '#111', fg: '#F2EFE8', img: '/_blob/e2f2facb76d7585de187f135b62123f5', alt: 'The Ask AI landing page headline: Get answers from your workforce data and let Ask AI do the rest' },
          { n: '02', h: 'Announcement video', s: 'Watch it on LinkedIn', href: 'https://lnkd.in/p/gMXYb4hH', go: '↗', bg: '#111', fg: '#F2EFE8', img: '/_blob/03980524c45a3df2f820446ec7e9e0c2', alt: 'Opening frame of the Introducing Ask AI announcement video' },
          { n: '03', h: 'Sales enablement', s: 'Documents for the sales team, built on the same story', href: 'Site-Service-Launch.dc.html', go: '→', bg: '#F2EFE8', fg: '#111', img: '', alt: '' }
        ]
      },
      xofu: {
        did: [
          { t: 'Rebuilt the positioning around one buyer question: “Does AI recommend us?”' },
          { t: 'Rewrote the homepage, pricing, services and demo pages.' },
          { t: 'Packaged pricing into four tiers: Free, Personal, Business and Agency.' },
          { t: 'Launched the Citation Audit, with engagement-based onboarding emails.' }
        ]
      },
      pwGroups: samples.map((g) => ({ ...g, count: g.items.length, items: g.items.map((x) => ({ ...x, hasH: !!x.h, noH: !x.h, hasL: !!(x.links && x.links.length), links: x.links || [] })) })),
      pwCount: samples.reduce((n, g) => n + g.items.length, 0),
      filters: filters.map((x) => ({ id: x.id, label: x.label, count: x.id === 'all' ? projects.length : projects.filter((p) => p.k === x.id).length, pressed: x.id === f ? 'true' : 'false', bg: x.id === f ? '#111' : 'transparent', fg: x.id === f ? '#F2EFE8' : '#111', border: x.id === f ? '#111' : '#C9C3B6', pick: () => this.setState({ f: x.id }) })),
      shown: projects.filter((p) => f === 'all' || p.k === f).map((p) => ({ ...p, cls: p.dark ? 'is-deep' : '', tag: tags[p.k], cta: p.deep ? 'See the case →' : 'Ask me about it →', bg: p.dark ? '#111' : (p.orange ? '#E6E1D6' : '#F2EFE8'), fg: p.dark ? '#F2EFE8' : '#111', rule: p.dark ? '#3A3934' : 'rgba(17,17,17,.2)' }))
    };
  }
