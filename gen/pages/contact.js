  initialState() { return { door: 0 }; }
  renderVals() {
    const cal = 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi';
    const doors = [
      { e: '🧭', label: 'Our positioning isn’t landing', who: 'For founders and marketing leads', title: 'Let’s find the one thing your market should remember.', body: 'We’ll work out what makes your product worth choosing, then turn it into messaging your whole team can tell the same way.', cta: 'Book a positioning call ↗', href: cal },
      { e: '🚀', label: 'We have a launch coming up', who: 'For product and marketing teams', title: 'Let’s make it a launch the market notices and sales can use.', body: 'Narrative and timing, press and partners, and the material sales needs on day one.', cta: 'Book a launch call ↗', href: cal },
      { e: '📈', label: 'Our content should work harder', who: 'For growth and content teams', title: 'Let’s build content that earns attention and turns into pipeline.', body: 'Editorial strategy, storytelling and distribution, built to keep working long after it’s published.', cta: 'Book a content call ↗', href: cal },
      { e: '💼', label: 'I’m hiring a marketer', who: 'For hiring managers', title: 'I’m open to senior marketing roles.', body: 'Remote, or with relocation for the right team. Send me the role and I’ll reply with a CV tailored to it.', cta: 'Email me the role ↗', href: 'mailto:jeremiah@thejeremiahajayi.com?subject=A%20role%20for%20you' },
      { e: '🤝', label: 'Let’s work on something together', who: 'For collaborators', title: 'Speaking, research, writing, or supporting EmpowerQ.', body: 'If it involves good ideas going somewhere useful, I’d like to hear about it.', cta: 'Start a conversation ↗', href: 'mailto:jeremiah@thejeremiahajayi.com?subject=Working%20together' }
    ];
    const di = this.state.door;
    return {
      time: this.state.time,
      doors: doors.map((d, i) => ({ ...d, selected: i === di ? 'true' : 'false', bg: i === di ? '#111' : 'transparent', fg: i === di ? '#F2EFE8' : '#111', border: i === di ? '#111' : '#C9C3B6', pick: () => this.setState({ door: i }) })),
      door: doors[di]
    };
  }
