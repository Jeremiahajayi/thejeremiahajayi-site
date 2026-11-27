  renderVals() {
    const S = 'https://www.thejeremiahajayi.com/post/';
    return {
      time: this.state.time,
      svc: {
        slug: 'product-launch-gtm', name: 'Launches & go-to-market', verb: 'land',
        title: 'Product launch and GTM consultant for B2B SaaS teams',
        intro: 'Launches built for pipeline, not just attention: a GTM brief, a launch plan, sales enablement and measurement, so every release starts sales conversations.',
        stats: [ { big: '20+', label: 'product launches led, at RemotePass and beyond' }, { big: '270+', label: 'media pickups for the RemotePass × Certn launch' }, { big: '134%', label: 'RemotePass revenue growth the year I led GTM' } ],
        forWho: [ { t: 'B2B SaaS teams shipping a major feature, a new product or a new market entry' }, { t: 'Product marketing leads who need senior launch support' }, { t: 'Founders running founder-led sales who need launches sales can use' } ],
        signs: [ { t: 'Launches get a spike of attention, then nothing happens in the pipeline.' }, { t: 'Sales hears about a release after customers do.' }, { t: 'No one can say what the last launch did for pipeline.' }, { t: 'Partner launches stall on timing, approvals and whose story it is.' }, { t: 'You’re entering a new market without a story that works there.' } ],
        getsTitle: 'Everything a launch needs to reach pipeline.',
        gets: [
          { n: '01', h: 'GTM brief', t: 'Who the release is for, the problem it solves, and how it changes the pitch.' },
          { n: '02', h: 'Launch plan and tiering', t: 'A calendar, owners and channels, scaled to how big the release really is.' },
          { n: '03', h: 'Launch messaging', t: 'The announcement, website and in-product copy, and the press and partner story.' },
          { n: '04', h: 'Sales enablement kit', t: 'Deck, battlecards, one-pagers, FAQs and talk tracks that sales actually uses.' },
          { n: '05', h: 'Internal alignment', t: 'Product, sales, customer success and partners working to one timeline.' },
          { n: '06', h: 'Launch-to-pipeline measurement', t: 'Agreed before launch, reported after it, with lessons for the next one.' }
        ],
        extraTitle: 'Launches I handle',
        extraText: '',
        extra: [ { t: 'Major features and new product lines' }, { t: 'Integrations and partnership launches' }, { t: 'New market entry, including English and Arabic launches for MENA' }, { t: 'Launch content and lead magnets' } ],
        extraLink: '', extraLinkLabel: '',
        steps: [
          { n: '1', h: 'Diagnose', t: 'The release, the buyer, the sales motion and what success means in pipeline.' },
          { n: '2', h: 'Plan', t: 'The GTM brief, launch tier, calendar and owners, agreed with product and sales.' },
          { n: '3', h: 'Launch', t: 'Messaging, press, partners and the enablement kit, shipped on the same day.' },
          { n: '4', h: 'Measure', t: 'Pipeline, sales usage and what to repeat or change for the next launch.' }
        ],
        proofTitle: 'Launches that reached sales, not just the news.',
        cases: [
          { client: 'RemotePass × Certn', year: '2024', big: '270+', title: 'The partnership launch that went global', result: 'Media pickups including Yahoo Finance, Fox and NBC, and enterprise conversations in regulated industries.', href: 'Site-Work.dc.html#certn', bg: 'var(--night)', fg: '#F2EFE8' },
          { client: 'RemotePass', year: '2024–25', big: '134%', title: 'A launch program built for pipeline', result: 'GTM for 15+ launches, including Org Chart, Time-Off, Local Payroll, Open APIs and Wafeq.', href: 'Site-Work.dc.html#launches', bg: 'var(--blush)', fg: '#111' },
          { client: 'RemotePass · Ask AI', year: 'Feature launch', big: 'Record', title: 'Everyone was selling AI. We sold the answer.', result: 'MQL performance after the launch, from one story carried across the landing page, video and sales enablement.', href: 'Site-Work.dc.html#askai', bg: 'var(--blush)', fg: '#111' }
        ],
        hasQuote: true, quote: 'He doesn’t just blur the lines between Sales and Marketing—he obliterates them.', quoteName: 'Wesley Hattingh', quoteOrg: 'RemotePass',
        note: 'My Product Marketing Alliance piece covers the systems I built to coordinate the first 15 of these launches.',
        tool: { name: 'GTM Readiness Scorecard', line: 'Check whether your next launch is ready to create sales conversations.', href: '/resources/gtm-scorecard/' },
        paired: { name: 'Positioning & messaging', line: 'A launch is only as strong as the story behind it.', href: 'Site-Service-Positioning.dc.html' },
        reading: [
          { title: 'How to turn a B2B product launch into sales conversations', where: 'My site', href: S + 'saas-product-launch-proof-gap' },
          { title: '7 systems that let me coordinate 15 launches', where: 'Product Marketing Alliance', href: 'https://www.productmarketingalliance.com/7-systems-that-let-me-coordinate-15-launches/' }
        ]
      },
      faq: [
        { q: 'When should we bring you in?', a: 'As soon as the release is defined. The earlier the positioning and GTM brief are agreed, the less rework there is for sales and marketing later. I can also step in mid-launch to rescue a plan that’s drifting.' },
        { q: 'How do you work with our sales team?', a: 'Sales is part of the plan from day one. I talk to reps about the objections they hear, build the enablement kit with them, and check after launch which assets they actually used.' },
        { q: 'How do you measure whether a launch created pipeline?', a: 'We agree the measures before launch: sourced and influenced pipeline, demo requests, sales usage of launch assets and early adoption. Then I report against them after launch, using your CRM and analytics.' },
        { q: 'Can you run one launch, or only a launch program?', a: 'Both. A single launch is a fixed-scope project. For teams that ship often, I run the launch program as an embedded partner and leave you a repeatable playbook.' },
        { q: 'Which regions do you cover?', a: 'I work from Lagos with teams in Europe, North America, the Middle East and Africa, and I’ve run launches in both English and Arabic.' }
      ]
    };
  }
