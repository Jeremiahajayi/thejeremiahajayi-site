  renderVals() {
    const S = 'https://www.thejeremiahajayi.com/post/';
    return {
      time: this.state.time,
      svc: {
        slug: 'positioning-messaging', name: 'Positioning & messaging', verb: 'clear',
        title: 'Positioning and messaging consultant for B2B SaaS',
        intro: 'One clear story that product, marketing and sales all use, so your product is easy to understand, easy to compare and easy to buy.',
        stats: [ { big: '2x', label: 'Xofu launch email click-through after repositioning' }, { big: '4', label: 'pricing tiers packaged around the new positioning' }, { big: '20+', label: 'launches positioned for new segments and markets' } ],
        forWho: [ { t: 'Founders before a launch, a fundraise or a move into a new segment' }, { t: 'Marketing leaders whose messaging has drifted across teams' }, { t: 'Teams building a new category that buyers don’t understand yet' } ],
        signs: [ { t: 'Prospects still can’t explain what you do after the demo.' }, { t: 'Your website, deck and sales calls tell different stories.' }, { t: 'You lose deals to “no decision” or to cheaper look-alikes.' }, { t: 'AI assistants describe your product vaguely, or wrongly.' }, { t: 'A launch, raise or new market is coming, and the story isn’t ready.' } ],
        getsTitle: 'A story your whole company can tell the same way.',
        gets: [
          { n: '01', h: 'Customer and competitor research', t: 'Interviews, call recordings, CRM notes, win/loss data and the alternatives buyers compare you with.' },
          { n: '02', h: 'Positioning', t: 'Who it’s for, what they’d use instead, what’s different and why it matters.' },
          { n: '03', h: 'Messaging framework', t: 'The core narrative, value pillars and proof points for each audience.' },
          { n: '04', h: 'Website and sales copy', t: 'Homepage, product and pricing pages, and the pitch narrative.' },
          { n: '05', h: 'AI-search perception check', t: 'How ChatGPT, Perplexity and Google’s AI describe you today, and what to change.' }
        ],
        extraTitle: 'When it pays off most',
        extraText: '',
        extra: [ { t: 'Before a major launch' }, { t: 'Before a fundraise' }, { t: 'When entering a new segment or region' }, { t: 'When a new category needs explaining' } ],
        extraLink: '', extraLinkLabel: '',
        steps: [
          { n: '1', h: 'Listen', t: 'Customers, sales calls, CRM notes, win/loss data and competitor research.' },
          { n: '2', h: 'Decide', t: 'One audience, one problem and one reason to choose you, agreed with leadership.' },
          { n: '3', h: 'Write', t: 'The messaging framework first, then the website, deck and onboarding copy.' },
          { n: '4', h: 'Test and roll out', t: 'Check the story with customers and sales, then use it everywhere.' }
        ],
        proofTitle: 'Clearer stories, measurable results.',
        cases: [
          { client: 'Xofu', year: '2026', big: '2x', title: 'Giving a new AI product one clear question to answer', result: 'Repositioned around “Does AI recommend us?”; the launch email hit a 3.7% click-through rate.', href: 'Site-Work.dc.html#xofu', bg: '#111', fg: '#F2EFE8' },
          { client: 'VEC Studio', year: '2021–22', big: '+49%', title: 'Product-led stories for SEON, Kittl and Blackthorn', result: 'Monthly organic traffic growth for a B2B SaaS client.', href: 'Site-Work.dc.html#index', bg: '#FF5A2A', fg: '#111' }
        ],
        hasQuote: false, quote: '', quoteName: '', quoteOrg: '', note: '',
        tool: null,
        paired: { name: 'Launches & go-to-market', line: 'New positioning lands best with a launch behind it.', href: 'Site-Service-Launch.dc.html' },
        reading: [
          { title: 'What comes after investor attention? A GTM analysis of Scale, Raven and Metrifox', where: 'My site', href: S + 'scale-raven-metrifox-gtm-analysis' },
          { title: 'How to turn a B2B product launch into sales conversations', where: 'My site', href: S + 'saas-product-launch-proof-gap' }
        ]
      },
      faq: [
        { q: 'How long does a positioning project take?', a: 'It depends on how much customer research already exists. We agree the timeline after a diagnostic call, and you see the positioning and messaging framework before any website copy is rewritten.' },
        { q: 'What do you need from our team?', a: 'Access to customers or call recordings, your CRM notes, one decision-maker from leadership, and a few short working sessions. I do the research and writing.' },
        { q: 'Is this a workshop or done with you?', a: 'Done with you. I run the research and draft everything; your team makes the decisions in short working sessions, so the story is yours, not mine.' },
        { q: 'How do you test the messaging?', a: 'With customers and prospects, with your sales team on live calls, and on the pages and emails where it goes first. I also check how AI assistants describe you before and after.' },
        { q: 'How is it priced?', a: 'Every project is scoped to the problem. After a diagnostic call, you get a written proposal with scope, timeline and fee.' }
      ]
    };
  }
