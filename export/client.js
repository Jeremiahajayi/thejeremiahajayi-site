(function () {

  // Homepage hero: "the edit". Plays once per visit; the button replays it.
  document.documentElement.classList.add('js-on');
  var hero = document.querySelector('.hero-anim');
  if (hero) {
    try { sessionStorage.setItem('jgSeen', '1'); } catch (e) {}
    var rb = document.querySelector('[data-jg-replay]');
    if (rb) rb.addEventListener('click', function () {
      var sec = document.getElementById('top');
      document.documentElement.classList.remove('jg-skip'); sec.classList.remove('hero-anim'); void sec.offsetWidth; sec.classList.add('hero-anim');
    });
  }
  function t() { try { return new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: 'Africa/Lagos' }).format(new Date()); } catch (e) { return ''; } }
  function tick() { document.querySelectorAll('[data-time]').forEach(function (el) { el.textContent = t(); }); }
  tick(); setInterval(tick, 30000);
  function paint(o, on) { o.style.background = on ? '#111' : 'transparent'; o.style.color = on ? '#F2EFE8' : '#111'; o.style.borderColor = on ? '#111' : '#C9C3B6'; }
  function apply(sec) {
    var f = sec.getAttribute('data-cur') || 'all';
    var inp = sec.querySelector('[data-search]'); var q = inp ? inp.value.trim().toLowerCase() : '';
    var shown = 0;
    sec.querySelectorAll('[data-k]').forEach(function (el) {
      var ok = (f === 'all' || el.getAttribute('data-k') === f) && (!q || (el.getAttribute('data-text') || el.textContent.toLowerCase()).indexOf(q) !== -1);
      el.style.display = ok ? '' : 'none'; if (ok) shown++;
    });
    var empty = sec.querySelector('[data-empty]'); if (empty) empty.style.display = shown ? 'none' : 'block';
  }
  document.querySelectorAll('button[data-f]').forEach(function (b) {
    b.addEventListener('click', function () {
      var sec = b.closest('section'); sec.setAttribute('data-cur', b.getAttribute('data-f'));
      sec.querySelectorAll('button[data-f]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); paint(o, o === b); });
      apply(sec);
    });
  });
  document.querySelectorAll('[data-search]').forEach(function (i) { i.addEventListener('input', function () { apply(i.closest('section')); }); });
  var doorsEl = document.getElementById('doors-data');
  if (doorsEl) {
    var doors = JSON.parse(doorsEl.textContent);
    document.querySelectorAll('button[data-door]').forEach(function (b) {
      b.addEventListener('click', function () {
        var d = doors[+b.getAttribute('data-door')];
        document.querySelectorAll('button[data-door]').forEach(function (o) { o.setAttribute('aria-checked', o === b ? 'true' : 'false'); paint(o, o === b); });
        var s = function (k) { return document.querySelector('[data-slot="' + k + '"]'); };
        s('who').textContent = d.who; s('title').textContent = d.title; s('body').textContent = d.body;
        s('cta').textContent = d.cta; s('cta').setAttribute('href', d.href);
      });
    });
  }
  // Close the mobile menu when a same-page link is used.
  var navT = document.getElementById('navt');
  if (navT) document.querySelectorAll('.nav-main a').forEach(function (a) { a.addEventListener('click', function () { navT.checked = false; }); });
  // Escape closes the mobile menu.
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && navT && navT.checked) navT.checked = false; });
  // Scroll reveals: content eases up as it enters the screen.
  if ('IntersectionObserver' in window && !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    var SEL = 'section h2, section h3, section blockquote, section figure, section article, section li, section dl > div, section .card-l, section .path, section .row-x, section .door, section img';
    var SKIP = '.site-h, .wall-wrap, .marquee, .wall, .hscroll, .l1, .l2, .l3, .photo-in, .reveal, .wipe, .grow, .drawy, .nav-main, .mswipe, [data-k]';
    var picked = [];
    document.querySelectorAll(SEL).forEach(function (el) {
      if (el.closest(SKIP)) return;
      if (el.parentElement && el.parentElement.closest('.rv')) return;
      if (el.getBoundingClientRect().top < innerHeight * 0.9) return; // already on screen: leave it be
      el.classList.add('rv'); picked.push(el);
    });
    document.documentElement.classList.add('js-rv');
    var io = new IntersectionObserver(function (entries) {
      var batch = entries.filter(function (e) { return e.isIntersecting; });
      batch.forEach(function (e, i) {
        var el = e.target, d = Math.min(i * 70, 350);
        el.style.transitionDelay = d + 'ms'; el.classList.add('in'); io.unobserve(el);
        // hand the element back to its own hover transitions once it has arrived
        setTimeout(function () { el.classList.remove('rv', 'in'); el.style.transitionDelay = ''; }, 900 + d);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    picked.forEach(function (el) { io.observe(el); });
  }
  // Guide: "Not sure where to start?" Routes visitors by need or by a typed question.
  var CAL = 'https://calendly.com/jeremiahajayiconsultation/strategy-call-with-jeremiah-ajayi';
  var MAIL = 'mailto:jeremiah@thejeremiahajayi.com';
  var GD = {
    positioning: { e: '🧭', t: 'That’s positioning and messaging.', p: 'I find what makes your product worth choosing, then turn it into a story your website, sales team and launches can all tell the same way.',
      l: [['Book a call', CAL, 'Talk it through', 1], ['How I do positioning', '/services/positioning-messaging/', 'The service'], ['See it in action', '/work/#xofu', 'Xofu case study']] },
    launch: { e: '🚀', t: 'Let’s make it a launch sales can use.', p: 'Launches built for pipeline: a GTM brief, launch plan, sales enablement and launch-to-pipeline measurement. I’ve led 20+.',
      l: [['Book a launch call', CAL, 'Talk it through', 1], ['Check your launch readiness', '/gtm-scorecard', 'Free scorecard'], ['How I run launches', '/services/product-launch-gtm/', 'The service'], ['The Certn and Ask AI launches', '/work/#certn', 'Case studies']] },
    content: { e: '📈', t: 'Content that keeps working.', p: 'Content strategy, SEO and AI search visibility, measured in pipeline. At RemotePass that meant 174% organic growth and $500K+ pipeline in under a year.',
      l: [['Book a content call', CAL, 'Talk it through', 1], ['How I build content engines', '/services/content-growth/', 'The service'], ['The RemotePass content engine', '/work/#engine', 'Case study'], ['Audit your marketing', '/marketingaudit', 'Free tool']] },
    ai: { e: '🤖', t: 'Getting cited by ChatGPT, Gemini and co.', p: 'I research how AI assistants find and recommend brands, and help teams show up in those answers.',
      l: [['Run the category visibility audit', '/categoryvisibilityaudit', 'Free tool', 1], ['The State of AI Search in Nigeria', 'https://stateofaisearchinnigeria.eo.page/download', 'Report I co-authored'], ['My AI search research', '/blog/', 'Studies and articles'], ['Book a call', CAL, 'Talk it through']] },
    hire: { e: '💼', t: 'I’m open to senior marketing roles.', p: 'Product marketing, content and growth roles, remote or with relocation. Send me the role and I’ll reply with a CV tailored to it.',
      l: [['Email me the role', MAIL + '?subject=A%20role%20for%20you', 'jeremiah@thejeremiahajayi.com', 1], ['See my work', '/work/', 'Case studies'], ['My story', '/about/', 'About me'], ['LinkedIn', 'https://www.linkedin.com/in/jeremiah-ajayi/', 'Connect']] },
    proof: { e: '🏆', t: 'Here’s what the work has done.', p: '$3M+ pipeline influenced, 20+ product launches, #1 above the BBC on Google for Stears, and 174% organic growth at RemotePass.',
      l: [['See the case studies', '/work/', 'Six in depth, plus the rest', 1], ['What people say about working with me', '/about/', 'About'], ['Book a call', CAL, 'Talk it through']] },
    read: { e: '📚', t: 'Start with the research.', p: 'Original studies on AI search, teardowns of launches and growth, and the playbooks I use.',
      l: [['All writing and research', '/blog/', 'Searchable archive', 1], ['The State of AI Search in Nigeria', 'https://stateofaisearchinnigeria.eo.page/download', 'Report'], ['Turn a launch into sales conversations', '/post/saas-product-launch-proof-gap', 'Article']] },
    empowerq: { e: '🌈', t: 'Thank you for wanting to help.', p: 'EmpowerQ builds economic inclusion for LGBTQ+ professionals in Nigeria: career programmes, research and a community that makes work safer.',
      l: [['Ways to get involved', '/empowerq/#involved', 'Fund, mentor or hire', 1], ['Visit EmpowerQ', 'https://www.empowerqueer.org', 'empowerqueer.org'], ['Email about partnering', MAIL + '?subject=Partnering%20with%20EmpowerQ', 'Start a conversation']] },
    pricing: { e: '💬', t: 'Scope and pricing.', p: 'Every project is a little different, so the quickest way to a clear answer is a short call or an email about what you need.',
      l: [['Book a call', CAL, 'Talk it through', 1], ['Email me', MAIL + '?subject=Project%20enquiry', 'jeremiah@thejeremiahajayi.com'], ['See the services', '/services/', 'What I offer']] },
    contact: { e: '✉️', t: 'Let’s talk.', p: 'Book a call for a project, or email me for anything else.',
      l: [['Book a call', CAL, 'For projects', 1], ['Email me', MAIL, 'jeremiah@thejeremiahajayi.com'], ['All the ways to reach me', '/contact/', 'Contact']] },
    none: { e: '🤔', t: 'I couldn’t match that one.', p: 'Here are the best places to start, or email me and I’ll point you in the right direction.',
      l: [['Email me your question', MAIL + '?subject=A%20question', 'I reply personally', 1], ['See the work', '/work/', 'Case studies'], ['See the services', '/services/', 'What I offer']] }
  };
  var KEYS = [
    ['ai', /\b(ai search|geo|aeo|chatgpt|perplexity|gemini|claude|llm|ai visibility|citation|ai answer|overviews?)\b/],
    ['hire', /\b(hire|hiring|job|role|cv|resume|full[- ]?time|recruit|vacanc|employ)/],
    ['pricing', /\b(price|pricing|cost|rate|rates|budget|fee|fees|retainer|how much)\b/],
    ['launch', /\b(launch|gtm|go[- ]to[- ]market|release|feature|press|pr\b|product hunt)/],
    ['content', /\b(content|seo|blog|organic|rank|traffic|newsletter|writer|copywrit)/],
    ['positioning', /\b(position|messag|story|explain|brand|homepage|website copy|differentiat|startup|startups|b2b|saas)/],
    ['empowerq', /\b(empowerq|queer|lgbt|donat|fund|nonprofit|volunteer|mentor|sponsor)/],
    ['read', /\b(read|article|research|report|study|learn|writing|blog post)/],
    ['proof', /\b(result|case|portfolio|work|example|client|proof|testimonial)/],
    ['contact', /\b(contact|email|call|talk|book|meet|reach)/]
  ];
  var root = document.querySelector('[data-gd-root]');
  if (root) {
    var panel = root.querySelector('.gd-panel'), pick = root.querySelector('[data-gd-pick]'), ans = root.querySelector('[data-gd-ans]');
    var opener = null;
    function track(intent, how) { try { (window.dataLayer = window.dataLayer || []).push({ event: 'guide_select', guide_intent: intent, guide_method: how }); } catch (e) {} }
    function openG(btn) { opener = btn || null; root.classList.add('gd-open'); panel.hidden = false; document.querySelectorAll('[data-gd-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'true'); }); var f = panel.querySelector('.gd-opt'); if (f) f.focus(); track('open', 'open'); }
    function closeG() { root.classList.remove('gd-open'); panel.hidden = true; showPick(); document.querySelectorAll('[data-gd-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); }); if (opener && opener.offsetParent) opener.focus(); }
    function showPick() { ans.hidden = true; pick.hidden = false; }
    function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function show(k, how) {
      var a = GD[k] || GD.none; track(k, how);
      ans.innerHTML = '<div class="gd-big" aria-hidden="true">' + a.e + '</div><h3>' + esc(a.t) + '</h3><p>' + esc(a.p) + '</p><ul class="gd-links">' +
        a.l.map(function (x) { var ext = /^https?:/.test(x[1]); return '<li><a class="' + (x[3] ? 'gd-main' : '') + '" href="' + x[1] + '"' + (ext ? ' target="_blank" rel="noopener"' : '') + '>' + esc(x[0]) + ' <span>' + esc(x[2]) + ' ' + (ext ? '↗' : '→') + '</span></a></li>'; }).join('') +
        '</ul><button type="button" class="gd-back" data-gd-back>← Back to all options</button>';
      pick.hidden = true; ans.hidden = false; var h = ans.querySelector('h3'); h.setAttribute('tabindex', '-1'); h.focus();
    }
    document.querySelectorAll('[data-gd-open]').forEach(function (b) { b.addEventListener('click', function () { panel.hidden ? openG(b) : closeG(); }); });
    root.querySelector('[data-gd-close]').addEventListener('click', closeG);
    root.querySelectorAll('[data-gd]').forEach(function (b) { b.addEventListener('click', function () { show(b.getAttribute('data-gd'), 'option'); }); });
    ans.addEventListener('click', function (e) { if (e.target.closest('[data-gd-back]')) { showPick(); var f = panel.querySelector('.gd-opt'); if (f) f.focus(); } });
    root.querySelector('[data-gd-form]').addEventListener('submit', function (e) {
      e.preventDefault(); var q = (this.q.value || '').toLowerCase().trim(); if (!q) return;
      var hit = 'none'; for (var i = 0; i < KEYS.length; i++) { if (KEYS[i][1].test(q)) { hit = KEYS[i][0]; break; } }
      show(hit, 'question'); this.q.value = '';
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) closeG(); });
    document.addEventListener('click', function (e) { if (!panel.hidden && !e.target.closest('[data-gd-root]') && !e.target.closest('[data-gd-open]')) closeG(); });
  }
})();
