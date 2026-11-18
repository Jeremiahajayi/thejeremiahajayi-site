  renderVals() {
    return {
      time: this.state.time,
      services: [
        { cls: 'd-clear', verb: 'Clear', name: 'Positioning & messaging', when: 'buyers can’t explain what you do, or a launch, raise or new market is coming.', proof: 'Xofu: 2x click-through', href: 'Site-Service-Positioning.dc.html', bg: 'var(--sun)', fg: '#111', shp: 'shp-flower', shpc: 'var(--mint)', emo: '🔍', rule: 'rgba(17,17,17,.2)' },
        { cls: 'd-land', verb: 'Land', name: 'Launches & go-to-market', when: 'releases get attention but don’t reach sales conversations.', proof: '20+ launches led', href: 'Site-Service-Launch.dc.html', bg: 'var(--orange)', fg: '#111', shp: 'shp-star', shpc: 'var(--sun)', emo: '🚀', rule: 'rgba(17,17,17,.25)' },
        { cls: 'd-travel', verb: 'Travel', name: 'Content & storytelling', when: 'content isn’t turning into pipeline, or AI answers recommend competitors.', proof: '174% organic growth', href: 'Site-Service-Content.dc.html', bg: 'var(--mint)', fg: '#111', shp: 'shp-clover', shpc: 'var(--leaf)', emo: '✈️', rule: 'rgba(17,17,17,.2)' }
      ],
      forWho: [ { t: 'B2B SaaS and technology companies, from seed to growth stage' }, { t: 'Founders who need senior marketing judgment before a full-time hire' }, { t: 'Marketing and product leaders who need a hands-on partner for a launch, a repositioning or a content engine' }, { t: 'Teams in Europe, North America, the Middle East and Africa' } ],
      notFor: [ { t: 'Teams looking for volume content without a strategy behind it' }, { t: 'Paid ads management as a standalone service' }, { t: 'Projects where success can’t be tied to a business outcome' } ],
      ways: [
        { n: '01', h: 'Embedded partner', t: 'Senior, hands-on marketing leadership inside your team for several months, across positioning, launches and content.', cta: 'Book a call ↗', href: 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi' },
        { n: '02', h: 'Fixed-scope project', t: 'One clear piece of work: a repositioning, a launch or a content strategy, with a defined outcome.', cta: 'Book a call ↗', href: 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi' },
        { n: '03', h: 'Ongoing content partner', t: 'A content engine run month to month: strategy, editorial, distribution and reporting.', cta: 'Book a call ↗', href: 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi' },
        { n: '04', h: 'A full-time role', t: 'Open to senior marketing roles, remote or with relocation. Send me the role and I’ll reply with a tailored CV.', cta: 'Send me the role →', href: 'Site-Contact.dc.html#hiring' }
      ],
      steps: [
        { n: '1', h: 'Diagnostic call', t: '30 minutes on your product, buyers, goals and what’s getting in the way.' },
        { n: '2', h: 'Scope', t: 'A written proposal with the work, timeline, fee and how we’ll measure it.' },
        { n: '3', h: 'Delivery', t: 'Hands-on work with your team, with decisions made in short working sessions.' },
        { n: '4', h: 'Measurement', t: 'Results against the measures we agreed, and what to do next.' }
      ],
      proof: [ { big: '$3M+', label: 'pipeline influenced' }, { big: '20+', label: 'product launches led' }, { big: '#1', label: 'above the BBC on Google for Stears' }, { big: '174%', label: 'organic user acquisition growth at RemotePass' } ],
      faq: [
        { q: 'Should we hire you or a full-time marketing leader?', a: 'If you need senior judgment before you can justify a full-time hire, or a specific problem solved fast, an embedded or project engagement is usually the better first step. If the fit is right, I’m also open to full-time roles.' },
        { q: 'How is working with you different from an agency?', a: 'You work with me directly, not an account manager. When a project needs more hands, I bring in a vetted freelance team and stay accountable for the work.' },
        { q: 'What’s the smallest engagement?', a: 'A fixed-scope project, such as a positioning sprint or a single launch. We agree the scope after a diagnostic call.' },
        { q: 'Which regions and time zones do you work with?', a: 'I’m based in Lagos (UTC+1) and work with teams in Europe, North America, the Middle East and Africa. My hours overlap fully with Europe and the Middle East, and with US mornings.' },
        { q: 'How is pricing scoped?', a: 'Every engagement is scoped to the problem. After the diagnostic call, you get a written proposal with scope, timeline and either a fixed fee or a monthly rate.' }
      ],
      toolkit: 'Claude and Claude Code · ChatGPT · HubSpot · GA4 · Google Search Console · Ahrefs · Semrush · Profound · n8n · Apollo · HTML and CSS'
    };
  }
