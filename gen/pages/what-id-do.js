  initialState() { return {}; }
  renderVals() {
    // ── What I'd Do · configuration ─────────────────────────────────────────
    // Paste the official links here when they exist. Leave a value as '' until then:
    // the page shows an honest "not yet" state instead of a button that does nothing.
    const CONFIG = {
      // beehiiv subscribe form ID: the data-beehiiv-form value from beehiiv's embed code.
      // The page loads beehiiv's official loader (subscribe-forms.beehiiv.com/v3/loader.js) for it.
      beehiivFormId: '486dd20f-f759-4e17-a148-6ae63a258dcf',
      // Luma → Calendar → Settings → Embed. The calendar ID looks like cal-XXXXXXXX.
      lumaCalendarId: '',
      // The featured event's ID on Luma (evt-XXXXXXXX). Set it only once the real event exists.
      lumaEventId: '',
      // A form for problem submissions (Tally, Typeform, Google Forms…). Until then, email is used.
      submitUrl: '',
      // An approved photo of the featured guest, e.g. /_blob/<id> or https://…
      guestPhoto: ''
    };
    // ── The Decision Files ─────────────────────────────────────────────────
    // Add a published issue, guest case or live-session takeaway as an object, newest first:
    // { cat: 'Independent analysis', title: '…', by: 'Jeremiah Ajayi', date: '2026-12-02',
    //   dateLabel: '2 Dec 2026', read: '7 min read', dek: '…', href: 'https://…' }
    const FILES = [];

    const mail = 'mailto:jeremiah@thejeremiahajayi.com';
    const submitMail = mail + '?subject=' + encodeURIComponent('What I’d Do: a problem to work through') + '&body=' + encodeURIComponent('What’s happening:\n\nWhat you’ve tried or considered:\n\nWhat’s at stake, and by when:\n\nCan we share identifying details? (We’ll always ask first.)\n');
    const notifyMail = mail + '?subject=' + encodeURIComponent('What I’d Do: tell me when issue one is out');
    const luma = CONFIG.lumaCalendarId ? 'https://lu.ma/embed/calendar/' + CONFIG.lumaCalendarId + '/events' : '';
    return {
      time: this.state.time,
      cfg: CONFIG,
      hasForm: !!CONFIG.beehiivFormId,
      noForm: !CONFIG.beehiivFormId,
      notifyMail,
      hasCal: !!luma,
      noCal: !luma,
      lumaSrc: luma,
      hasEvent: !!CONFIG.lumaEventId,
      noEvent: !CONFIG.lumaEventId,
      lumaEventHref: CONFIG.lumaEventId ? 'https://lu.ma/event/' + CONFIG.lumaEventId : '',
      hasPhoto: !!CONFIG.guestPhoto,
      noPhoto: !CONFIG.guestPhoto,
      hasSubmitUrl: !!CONFIG.submitUrl,
      noSubmitUrl: !CONFIG.submitUrl,
      submitMail,
      files: FILES,
      hasFiles: FILES.length > 0,
      noFiles: FILES.length === 0
    };
  }
