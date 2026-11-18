  renderVals() {
    const site = 'https://www.empowerqueer.org';
    const mail = 'mailto:info@empowerqueer.org?subject=';
    return {
      time: this.state.time,
      programs: [
        { kind: 'Research', name: 'LGBTQ+ Workforce Pulse Report', line: '151 voices on queer working life in Nigeria, to make the case to employers.', href: 'https://www.empowerqueer.org/lgtbq-workforce-report' },
        { kind: 'Newsletter', name: 'EmpowerQ Debrief', line: 'A weekly newsletter on work, money, opportunity and queer professional life.', href: site },
        { kind: 'Launching soon', name: 'Your Career Bestie', line: 'An AI career coach for CVs, interviews and career decisions.', href: site },
        { kind: 'Conference', name: 'Out of Office', line: 'Nigeria’s first queer career conference: a career panel, CV reviews, networking and more.', href: site },
        { kind: 'Series', name: 'Working While Queer', line: 'Stories and advice from people building careers in Nigeria.', href: site },
        { kind: 'Live conversations', name: 'I Got Funded', line: 'A scholarship series on Twitter Spaces with funded scholars as guests.', href: site },
        { kind: 'Resource', name: 'Opportunities Tracker', line: 'Jobs, fellowships and scholarships, gathered in one place.', href: site },
        { kind: 'One-to-one', name: 'Career office hours', line: '30-minute career sessions anyone can book.', href: 'https://calendly.com/empowerqueer-info/30min' }
      ],
      impact: [
        { big: '20+', label: 'people supported into jobs', cls: 'is-hero' },
        { big: '500+', label: 'queer professionals trained across our programmes', cls: 'is-big' },
        { big: '130+', label: 'community members, past our year-one goal of 100', cls: 'is-big' },
        { big: '151', label: 'voices in Nigeria’s first LGBTQ+ Workforce Pulse Report', cls: '' },
        { big: '100+', label: 'registrations for Out of Office Vol. 1, Lagos, June 2026', cls: '' },
        { big: '90', label: 'professionals in Lavender Ladder, our flagship programme', cls: '' },
        { big: '60+', label: 'participants in our AI bootcamp', cls: '' },
        { big: '₦450K', label: 'in prizes at our hackathon', cls: '' },
        { big: '10+', label: 'partnerships with organisations that chose to stand with us', cls: '' }
      ],
      partners: [
        { src: '/_blob/ce8ca550d74948104701a827296fd9e5', alt: 'EmpowerQ partner logo' },
        { src: '/_blob/3e41588207cc2522ac580f81fd1c81ea', alt: 'Lenora' },
        { src: '/_blob/b3487e13b614562c1b382407e13d8f8d', alt: 'The Freelance Coalition for Developing Countries' },
        { src: '/_blob/46f3e7b061b135f8de2e2ba07b3f87e0', alt: 'Obodo' },
        { src: '/_blob/4f8956442c07286bc136767ac113081e', alt: 'Bisi Alimi Foundation' },
        { src: '/_blob/c58b4129f9039beffbf47f294583da8d', alt: 'Human Rights Hub' },
        { src: '/_blob/375782a82be8c161f1324af6ace3d1f8', alt: 'FUSE Varsity' },
        { src: '/_blob/2f44bae2f7270c9759f23bbe105d038e', alt: 'EmpowerQ partner logo' },
        { src: '/_blob/4f7a3ea1475b2cb871cd8ac20e922ea4', alt: 'Queer African Network' },
        { src: '/_blob/c89581c355581b0d5574105a25f14e01', alt: 'Q-Guard' },
        { src: '/_blob/35147fc4b2b0ca389608dea86484bc01', alt: 'CHEVS' },
        { src: '/_blob/203c1109956cb97625515fd1bfbc8dec', alt: 'Minority Africa' }
      ],
      ways: [
        { h: 'Hire from our talent pool', t: 'Meet recruiter-ready professionals from Lavender Ladder for open roles.', cta: 'Talk to us about hiring ↗', href: mail + 'Hiring%20from%20Lavender%20Ladder' },
        { h: 'Fund or sponsor', t: 'Back a programme, an event or the next Workforce Pulse Report.', cta: 'Start a conversation ↗', href: mail + 'Supporting%20EmpowerQ' },
        { h: 'Mentor', t: 'Give an hour a month to someone building their career.', cta: 'Become a mentor ↗', href: mail + 'Mentoring%20with%20EmpowerQ' },
        { h: 'Book office hours', t: 'Need career help? Book a 30-minute session with our team.', cta: 'Book a session ↗', href: 'https://calendly.com/empowerqueer-info/30min' },
        { h: 'Read the Debrief', t: 'Weekly notes on work, money and opportunity.', cta: 'Subscribe ↗', href: 'https://empowerq.substack.com' }
      ]
    };
  }
