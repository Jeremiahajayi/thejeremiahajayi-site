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
  function paint(o, on) { if (o.hasAttribute('data-css')) return; o.style.background = on ? '#111' : 'transparent'; o.style.color = on ? '#F2EFE8' : '#111'; o.style.borderColor = on ? '#111' : '#C9C3B6'; }
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
    if (/^#(hiring|hire|role)$/i.test(location.hash)) { var hb = document.querySelector('button[data-door="3"]'); if (hb) hb.click(); }
  }
  // Close the mobile menu when a same-page link is used.
  var navT = document.getElementById('navt');
  if (navT) document.querySelectorAll('.nav-main a').forEach(function (a) { a.addEventListener('click', function () { navT.checked = false; }); });
  // Escape closes the mobile menu.
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && navT && navT.checked) navT.checked = false; });
  // Scroll reveals: content eases up as it enters the screen.
  if ('IntersectionObserver' in window && !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    var SEL = 'section h2, section h3, section blockquote, section figure, section article, section li, section dl > div, section .card-l, section .path, section .row-x, section .door, section img';
    var SKIP = '.img-rv, .ix, .h-hero, .site-h, .wall-wrap, .marquee, .wall, .hscroll, .l1, .l2, .l3, .photo-in, .reveal, .wipe, .grow, .drawy, .nav-main, .mswipe, [data-k], .pc-media, .st-stage, .rs-fan, .qt, .tl, .ab-title, .wk-pl-media, .k-fan, .k-hs, .k-wall, .k-stk img, .sv-serp';
    var picked = [];
    document.querySelectorAll(SEL).forEach(function (el) {
      if (el.closest(SKIP)) return;
      if (el.parentElement && el.parentElement.closest('.rv')) return;
      if (el.getBoundingClientRect().top < innerHeight * 0.9) return; // already on screen: leave it be
      el.classList.add('rv'); picked.push(el);
    });
    document.documentElement.classList.add('js-rv');
    var io = new IntersectionObserver(function (entries) {
      var batch = entries.filter(function (e) { return e.isIntersecting || e.boundingClientRect.top < 0; });
      batch.forEach(function (e, i) {
        var el = e.target, d = Math.min(i * 70, 350);
        el.style.transitionDelay = d + 'ms'; el.classList.add('in'); io.unobserve(el);
        // hand the element back to its own hover transitions once it has arrived
        setTimeout(function () { el.classList.remove('rv', 'in'); el.style.transitionDelay = ''; }, 900 + d);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    picked.forEach(function (el) { io.observe(el); });
    window.addEventListener('hashchange', function () { picked.forEach(function (el) { if (el.getBoundingClientRect().top < innerHeight) el.classList.add('in'); }); });
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
  var LABEL = { positioning: '🧭 Our product is hard to explain', launch: '🚀 We have a launch coming up', content: '📈 We need content that ranks and converts', ai: '🤖 We want to show up in AI answers', hire: '💼 I’m hiring a marketer', proof: '🏆 Show me results first', read: '📚 I want to read your research', empowerq: '🌈 I want to support EmpowerQ' };
  var ORDER = ['positioning', 'launch', 'content', 'ai', 'hire', 'proof', 'read', 'empowerq'];
  var root = document.querySelector('[data-gd-root]');
  if (root) {
    var panel = root.querySelector('.gd-panel'), thread = root.querySelector('[data-gd-thread]'), chips = root.querySelector('[data-gd-chips]'), peek = root.querySelector('[data-gd-peek]');
    var form = root.querySelector('[data-gd-form]'), opener = null, busy = false, asked = [];
    var calm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    function track(intent, how) { try { (window.dataLayer = window.dataLayer || []).push({ event: 'guide_select', guide_intent: intent, guide_method: how }); } catch (e) {} }
    function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function scroll() { thread.scrollTop = thread.scrollHeight; }
    function add(html, cls, tag) { var el = document.createElement(tag || 'div'); el.className = cls; el.innerHTML = html; thread.appendChild(el); scroll(); return el; }
    function wait(ms) { return new Promise(function (r) { setTimeout(r, calm ? 0 : ms); }); }
    function typing(ms) { var t = add('<i></i><i></i><i></i>', 'gd-m gd-bot gd-typing'); t.setAttribute('aria-label', 'Jeremiah is typing'); return wait(ms).then(function () { t.remove(); }); }
    function clearChoices() { [].forEach.call(thread.querySelectorAll('.gd-choices'), function (g) { g.remove(); }); }
    function setChips(keys, extra) {
      clearChoices();
      add(keys.map(function (k) { return '<button type="button" class="gd-chip" data-gd="' + k + '">' + LABEL[k] + '</button>'; }).join('') + (extra || ''), 'gd-choices');
    }
    function greet() {
      if (thread.children.length) return Promise.resolve();
      busy = true;
      return typing(500).then(function () { add('Hi, I’m Jeremiah 👋 I help B2B SaaS and tech teams get understood, launched and chosen.', 'gd-m gd-bot'); return typing(700); })
        .then(function () { add('What brings you here today? Pick one below, or type your question.', 'gd-m gd-bot'); setChips(ORDER); busy = false; });
    }
    function answer(k, how, said) {
      if (busy) return; busy = true; clearChoices();
      var a = GD[k] || GD.none; track(k, how); if (asked.indexOf(k) < 0) asked.push(k);
      add(esc(said || LABEL[k] || k), 'gd-m gd-you');
      typing(650).then(function () {
        add('<b>' + esc(a.t) + '</b> ' + esc(a.p), 'gd-m gd-bot');
        return wait(250);
      }).then(function () {
        add(a.l.map(function (x) { var ext = /^(https?:|mailto:)/.test(x[1]); return '<li><a class="' + (x[3] ? 'gd-main' : '') + '" href="' + x[1] + '"' + (/^https?:/.test(x[1]) ? ' target="_blank" rel="noopener"' : '') + '>' + esc(x[0]) + '<span>' + esc(x[2]) + (ext ? ' ↗' : ' →') + '</span></a></li>'; }).join(''), 'gd-links', 'ul');
        return typing(900);
      }).then(function () {
        add('Anything else I can help you find?', 'gd-m gd-bot');
        var rest = ORDER.filter(function (x) { return asked.indexOf(x) < 0; }).slice(0, 4);
        setChips(rest, '<button type="button" class="gd-chip" data-gd-done>👍 That’s all, thanks</button>');
        busy = false;
      });
    }
    function openG(btn, then) {
      opener = btn || null; root.classList.add('gd-open'); panel.hidden = false; if (peek) peek.hidden = true;
      document.querySelectorAll('[data-gd-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'true'); });
      track('open', 'open'); try { sessionStorage.setItem('gdPeek', '1'); } catch (e) {}
      greet().then(function () { if (then) then(); else form.q.focus({ preventScroll: true }); });
    }
    function closeG() { root.classList.remove('gd-open'); panel.hidden = true; document.querySelectorAll('[data-gd-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); }); if (opener && opener.offsetParent) opener.focus(); }
    function restart() { thread.innerHTML = ''; asked = []; busy = false; greet(); }
    document.querySelectorAll('[data-gd-open]').forEach(function (b) { b.addEventListener('click', function () { panel.hidden ? openG(b) : closeG(); }); });
    root.querySelector('[data-gd-close]').addEventListener('click', closeG);
    root.querySelector('[data-gd-restart]').addEventListener('click', restart);
    thread.addEventListener('click', function (e) {
      var c = e.target.closest('[data-gd]'); if (c) return answer(c.getAttribute('data-gd'), 'option');
      if (e.target.closest('[data-gd-done]') && !busy) { clearChoices(); add('That’s all, thanks 👍', 'gd-m gd-you'); busy = true; typing(600).then(function () { add('Lovely. If anything comes up, email me at <a href="mailto:jeremiah@thejeremiahajayi.com">jeremiah@thejeremiahajayi.com</a>. Enjoy the site 👋', 'gd-m gd-bot'); busy = false; }); }
    });
    if (peek) {
      peek.addEventListener('click', function (e) {
        var c = e.target.closest('[data-gd]'); if (c) { var k = c.getAttribute('data-gd'); openG(null, function () { answer(k, 'peek'); }); }
        if (e.target.closest('[data-gd-dismiss]')) { peek.hidden = true; try { sessionStorage.setItem('gdPeek', '1'); } catch (x) {} }
      });
      var seenPeek = false; try { seenPeek = sessionStorage.getItem('gdPeek') === '1'; } catch (e) {}
      if (!seenPeek) setTimeout(function () { if (panel.hidden) { peek.hidden = false; track('peek', 'shown'); } }, 9000);
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault(); var raw = (form.q.value || '').trim(); if (!raw || busy) return; var q = raw.toLowerCase();
      var hit = 'none'; for (var i = 0; i < KEYS.length; i++) { if (KEYS[i][1].test(q)) { hit = KEYS[i][0]; break; } }
      form.q.value = ''; answer(hit, 'question', raw);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) closeG(); });
  }

  // ---- Motion layer (all of it respects reduced-motion) ----
  var CALM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FINE = window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches;
  var raf = window.requestAnimationFrame || function (f) { return setTimeout(f, 16); };
  var onScroll = [];
  var ticking = false;
  function runScroll() { ticking = false; onScroll.forEach(function (f) { f(); }); }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; raf(runScroll); } }, { passive: true });
  window.addEventListener('resize', function () { raf(runScroll); });

  // 1. Numbers count up when they come into view.
  if (!CALM && 'IntersectionObserver' in window) {
    var NUM = /^(\$?)(\d[\d,]*(?:\.\d+)?)(\s?[KMk]?)([%+]?)$/;
    var nums = [].filter.call(document.querySelectorAll('.sg, dt, [data-count]'), function (el) {
      if (el.children.length || el.hasAttribute('data-scrub') || el.closest('.nav-main, .gd, .jg, .logo-row, .mbar, button, label')) return false;
      var t = el.textContent.trim(), m = NUM.exec(t); if (!m) return false;
      var v = parseFloat(m[2].replace(/,/g, '')); if (!m[1] && !m[3] && !m[4] && v >= 1900 && v <= 2100) return false; // years
      return parseFloat(getComputedStyle(el).fontSize) >= 28;
    });
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; cio.unobserve(e.target);
        var el = e.target, final = el.textContent.trim(), m = NUM.exec(final), target = parseFloat(m[2].replace(/,/g, ''));
        var dec = (m[2].split('.')[1] || '').length, comma = m[2].indexOf(',') > -1, t0 = performance.now(), dur = 1500;
        el.style.fontVariantNumeric = 'tabular-nums';
        (function step(now) {
          var p = Math.min(1, (now - t0) / dur), k = 1 - Math.pow(1 - p, 3), v = target * k;
          var txt = dec ? v.toFixed(dec) : Math.round(v).toString(); if (comma) txt = Number(txt).toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec });
          el.textContent = p < 1 ? m[1] + txt + m[3] + m[4] : final;
          if (p < 1) raf(step);
        })(t0);
      });
    }, { threshold: 0.6 });
    nums.forEach(function (el) { cio.observe(el); });
  }

  // 2. Stears dot grid lights up row by row as you scroll, with the page count in step.
  var dg = document.querySelector('[data-dots]');
  if (dg && !CALM) {
    var lit = dg.querySelector('.dots-lit'), edge = dg.querySelector('.dots-edge'), dnum = document.querySelector('[data-scrub="dots"]');
    var dotsFn = function () {
      var r = dg.getBoundingClientRect(), vh = innerHeight;
      var p = Math.max(0, Math.min(1, (vh * 0.92 - r.top) / (r.height + vh * 0.42)));
      var total = p * 1000, rows = Math.floor(total / 40), frac = (total % 40) / 40, R = rows * 4;
      lit.style.clipPath = 'polygon(0 0,100% 0,100% ' + R + '%,0 ' + R + '%)';
      edge.style.clipPath = p >= 1 ? 'inset(100% 0 0 0)' : 'polygon(0 ' + R + '%,' + (frac * 100) + '% ' + R + '%,' + (frac * 100) + '% ' + (R + 4) + '%,0 ' + (R + 4) + '%)';
      if (dnum) dnum.textContent = p >= 1 ? '10,000+' : Math.round(total * 10).toLocaleString('en-US');
    };
    onScroll.push(dotsFn); dotsFn();
  }

  // 3. Reading progress bar on articles and the Work page.
  if (document.querySelector('.post-body') || /^\/work\/?$/.test(location.pathname)) {
    var bar = document.createElement('div'); bar.className = 'rp'; bar.setAttribute('aria-hidden', 'true'); bar.innerHTML = '<span></span>';
    document.body.appendChild(bar); var barIn = bar.firstChild;
    var target = document.querySelector('.post-body') || document.querySelector('main') || document.body;
    var barFn = function () {
      var r = target.getBoundingClientRect(), total = r.height - innerHeight * 0.6;
      var p = total > 0 ? Math.max(0, Math.min(1, -r.top / total)) : 0;
      barIn.style.transform = 'scaleX(' + p + ')';
    };
    onScroll.push(barFn); barFn();
  }

  // 5. Case images on the Work page drift at different depths as you scroll.
  if (!CALM && /^\/work\/?$/.test(location.pathname) && innerWidth > 640) {
    var depthEls = [].slice.call(document.querySelectorAll('#stears img, #certn img, #askai img, #askai .lift2, #engine img, #xofu img')).filter(function (el) { return !el.closest('.hscroll'); });
    var D = [0.07, 0.13, 0.1, 0.16];
    depthEls.forEach(function (el, i) { el.dataset.depth = D[i % D.length]; el.style.willChange = 'translate'; });
    var depthFn = function () {
      var vh = innerHeight;
      depthEls.forEach(function (el) {
        var r = el.getBoundingClientRect(); if (r.bottom < -200 || r.top > vh + 200) return;
        var off = ((r.top + r.height / 2) - vh / 2) * -parseFloat(el.dataset.depth);
        el.style.translate = '0 ' + Math.max(-48, Math.min(48, off)).toFixed(1) + 'px';
      });
    };
    onScroll.push(depthFn); depthFn();
  }
  // 6. Homepage route map: the road draws itself, a plane travels it, stops light up.
  var route = document.querySelector('[data-route]');
  if (route && !CALM) {
    route.classList.add('rt-live');
    var rline = route.querySelector('.rt-line'), rsvg = route.querySelector('.rt-svg'), rplane = route.querySelector('.rt-plane'), rfill = route.querySelector('.rt-rail-fill'), rrail = route.querySelector('.rt-rail');
    var rstops = [].slice.call(route.querySelectorAll('.rt-stop')), RL = rline.getTotalLength();
    rline.style.strokeDasharray = RL;
    var rtFn = function () {
      var r = route.getBoundingClientRect(), vh = innerHeight, desk = innerWidth > 860;
      var p = Math.max(0, Math.min(1, (vh * 0.78 - r.top) / (r.height * 0.85)));
      if (desk) {
        rline.style.strokeDashoffset = RL * (1 - p);
        var sr = rsvg.getBoundingClientRect(), sx = sr.width / 1000;
        var a = rline.getPointAtLength(RL * p), b = rline.getPointAtLength(Math.min(RL, RL * p + 2)), a0 = p >= 1 ? rline.getPointAtLength(RL - 2) : a;
        var X = a.x * sx + (sr.left - r.left), Y = a.y + (sr.top - r.top);
        var ang = Math.atan2((p >= 1 ? a.y - a0.y : b.y - a.y), (p >= 1 ? (a.x - a0.x) : (b.x - a.x)) * sx) * 180 / Math.PI;
        rplane.style.transform = 'translate(' + X + 'px,' + Y + 'px) translate(-50%,-50%) rotate(' + (ang + 45) + 'deg)';
        rstops.forEach(function (s) { s.classList.toggle('on', p >= parseFloat(s.getAttribute('data-at')) - 0.015); });
      } else {
        rfill.style.transform = 'scaleY(' + p + ')';
        var rl = rrail.getBoundingClientRect(), Y2 = (rl.top - r.top) + rl.height * p;
        rplane.style.transform = 'translate(20.5px,' + Y2 + 'px) translate(-50%,-50%) rotate(135deg)';
        rstops.forEach(function (s) { var t = s.getBoundingClientRect(); s.classList.toggle('on', (t.top + 30 - rl.top) <= rl.height * p); });
      }
    };
    onScroll.push(rtFn); rtFn();
  }
  // 7. Selected work index: the preview follows whichever project you point at or tab to.
  var ix = document.querySelector('.ix');
  if (ix) {
    var stage = ix.querySelector('.ix-stage'), imgs = ix.querySelectorAll('.ix-img'), cap = ix.querySelector('.ix-cap'), front = 0, cur = null;
    function show(row) {
      if (!row || row === cur || !stage) return; cur = row;
      ix.querySelectorAll('.ix-row').forEach(function (r) { r.classList.toggle('is-on', r === row); });
      var next = imgs[1 - front];
      next.src = row.getAttribute('data-img'); next.style.objectFit = row.getAttribute('data-fit'); next.style.objectPosition = row.getAttribute('data-pos');
      stage.style.background = row.getAttribute('data-bg');
      var swap = function () { imgs[front].classList.remove('is-on'); next.classList.add('is-on'); front = 1 - front; };
      if (next.complete) swap(); else next.onload = swap;
      if (cap) cap.textContent = row.getAttribute('data-alt');
    }
    ix.querySelectorAll('.ix-row').forEach(function (r, i) {
      r.addEventListener('mouseenter', function () { show(r); });
      r.addEventListener('focus', function () { show(r); });
      if (i === 0) { r.classList.add('is-on'); cur = r; }
    });
  }


  // 9. Homepage: hero rows show their project beside the portrait, a fact bubble, kinetic rows,
  //    the sheet rising over the hero, Stears tabs, in-view reveals, the route plane, the case pill.
  var hero = document.querySelector('[data-hero]');
  if (hero) {
    var hrows = [].slice.call(hero.querySelectorAll('.h-row[data-peek]')), cards = [].slice.call(hero.querySelectorAll('[data-peek-card]'));
    var hi = 0, held = false, timer = null;
    var setPeek = function (i) { hi = i; hrows.forEach(function (r, k) { r.classList.toggle('is-on', k === i); }); cards.forEach(function (c, k) { c.classList.toggle('is-on', k === i); }); };
    setPeek(0);
    var hdisp = hero.querySelector('.h-display'); if (hdisp && !CALM) hdisp.classList.add('is-cycling');
    hrows.forEach(function (r, k) {
      r.addEventListener('mouseenter', function () { held = true; setPeek(k); });
      r.addEventListener('focus', function () { held = true; setPeek(k); });
      r.addEventListener('mouseleave', function () { held = false; });
    });
    if (!CALM) timer = setInterval(function () { if (!held && !document.hidden && scrollY < innerHeight) setPeek((hi + 1) % hrows.length); }, 2800);
    // The sky follows the time of day in Lagos: dawn, morning, noon, golden hour, dusk, night.
    var skyL = hero.querySelector('[data-sky-label]');
    var paintSky = function () {
      var h = 12, m = 0;
      try { var parts = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'Africa/Lagos' }).formatToParts(new Date()); parts.forEach(function (x) { if (x.type === 'hour') h = +x.value % 24; if (x.type === 'minute') m = +x.value; }); } catch (e) {}
      var t = h + m / 60, sky, label;
      if (t >= 5.5 && t < 8) { sky = 'dawn'; label = '🌅 Sunrise in Lagos'; }
      else if (t >= 8 && t < 12) { sky = 'morning'; label = '☀️ Morning in Lagos'; }
      else if (t >= 12 && t < 15.5) { sky = 'noon'; label = '😎 Midday sun in Lagos'; }
      else if (t >= 15.5 && t < 18.75) { sky = 'golden'; label = '🌇 Golden hour in Lagos'; }
      else if (t >= 18.75 && t < 20.5) { sky = 'dusk'; label = '🌆 Dusk in Lagos'; }
      else { sky = 'night'; label = '🌙 Night in Lagos'; }
      var x, y;
      if (t >= 6 && t <= 19) { var f = (t - 6) / 13; x = 46 + 50 * f; y = 70 - 60 * Math.sin(Math.PI * f); }
      else { var n = ((t + 24 - 19) % 24) / 11; x = 50 + 44 * n; y = 26 - 14 * Math.sin(Math.PI * n); }
      hero.setAttribute('data-sky', sky);
      hero.style.setProperty('--sx', x.toFixed(1) + '%'); hero.style.setProperty('--sy', y.toFixed(1) + '%');
      if (skyL) skyL.textContent = label;
    };
    var qs = /[?&]sky=(dawn|morning|noon|golden|dusk|night)/.exec(location.search);
    if (qs) { hero.setAttribute('data-sky', qs[1]); var demo = { dawn: [50, 62], morning: [60, 24], noon: [72, 10], golden: [90, 40], dusk: [95, 66], night: [62, 14] }[qs[1]]; hero.style.setProperty('--sx', demo[0] + '%'); hero.style.setProperty('--sy', demo[1] + '%'); if (skyL) skyL.textContent = qs[1]; }
    else { paintSky(); setInterval(paintSky, 60000); }
    var bub = hero.querySelector('.h-bub');
    if (bub) {
      var facts = []; try { facts = JSON.parse(bub.getAttribute('data-facts')); } catch (e) {}
      var fi = 0, bt = bub.querySelector('.h-bub-t');
      var nextFact = function () { if (!facts.length) return; fi = (fi + 1) % facts.length; bt.textContent = facts[fi]; bub.classList.remove('pop'); void bub.offsetWidth; bub.classList.add('pop'); };
      bub.addEventListener('click', nextFact);
      var ph = hero.querySelector('.h-photo'); if (ph) { ph.style.cursor = 'pointer'; ph.addEventListener('click', nextFact); }
    }
    var sheet = document.querySelector('[data-sheet]');
    if (!CALM && innerWidth > 1080 && hero.offsetHeight <= innerHeight + 40) {
      hero.classList.add('h-stick');
      var kin = function () {
        var y = scrollY, h = hero.offsetHeight, p = Math.max(0, Math.min(1, y / h));
        hrows.forEach(function (r, k) { r.style.transform = 'translateX(' + ((k % 2 ? 1 : -1) * p * 90).toFixed(1) + 'px)'; });
        var st = hero.querySelector('.h-stage'); if (st) st.style.transform = 'translateY(' + (p * 60).toFixed(1) + 'px) rotate(' + (p * -4).toFixed(2) + 'deg)';
        if (sheet) {
          var sr = sheet.getBoundingClientRect(), q = Math.max(0, Math.min(1, 1 - (sr.top - 80) / (innerHeight * 0.75)));
          sheet.style.transform = 'scale(' + (0.92 + 0.08 * q).toFixed(4) + ')';
          hero.style.visibility = sr.top < -10 ? 'hidden' : '';
          hero.style.setProperty('--hp', Math.max(0, Math.min(1, 1 - sr.top / innerHeight)).toFixed(3));
        }
      };
      onScroll.push(kin); kin();
    }
  }
  // Stears tabs (work without motion too)
  var stTabs = [].slice.call(document.querySelectorAll('.st-tabs [role="tab"]'));
  if (stTabs.length) {
    var stSel = function (i, focus) {
      stTabs.forEach(function (t, k) {
        var on = k === i; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1;
        var pnl = document.getElementById(t.getAttribute('aria-controls')); if (pnl) pnl.hidden = !on;
      });
      document.querySelectorAll('.st-v').forEach(function (v) { v.classList.toggle('is-on', v.getAttribute('data-v') === String(i)); });
      if (focus) stTabs[i].focus();
    };
    stTabs.forEach(function (t, k) {
      t.addEventListener('click', function () { stSel(k); });
      t.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); stSel((k + (e.key === 'ArrowRight' ? 1 : stTabs.length - 1)) % stTabs.length, true); }
      });
    });
  }
  // In-view flags for small reveals (strike-through, report fan)
  var iv = document.querySelectorAll('[data-inview]');
  if (iv.length) {
    if (CALM || !('IntersectionObserver' in window)) iv.forEach(function (el) { el.classList.add('in'); });
    else { var ivo = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting || e.boundingClientRect.top < 0) { e.target.classList.add('in'); ivo.unobserve(e.target); } }); }, { threshold: 0.5 }); iv.forEach(function (el) { ivo.observe(el); }); }
  }
  // Route: the plane flies along as you scroll and stops light up
  var tl = document.querySelector('[data-tl]');
  if (tl && !CALM && innerWidth > 1080) {
    tl.setAttribute('data-live', '');
    var tis = [].slice.call(tl.querySelectorAll('.tl-i'));
    var tlFn = function () {
      var r = tl.getBoundingClientRect(), p = Math.max(0, Math.min(1, (innerHeight * 0.85 - r.top) / (innerHeight * 0.6)));
      tl.style.setProperty('--p', p.toFixed(3));
      tis.forEach(function (t, k) { t.classList.toggle('on', p >= k / tis.length); });
    };
    onScroll.push(tlFn); tlFn();
  }
  // A small "View case" pill follows the pointer over project imagery
  if (FINE && !CALM) {
    var cards2 = document.querySelectorAll('.pc .pc-media');
    if (cards2.length) {
      var pill = document.createElement('div'); pill.className = 'view-pill'; pill.setAttribute('aria-hidden', 'true'); pill.textContent = 'View case →'; document.body.appendChild(pill);
      cards2.forEach(function (m) {
        m.addEventListener('mousemove', function (e) { pill.style.left = e.clientX + 'px'; pill.style.top = e.clientY + 'px'; pill.classList.add('on'); });
        m.addEventListener('mouseleave', function () { pill.classList.remove('on'); });
      });
    }
  }
  // 8. Images unveil once as they come into view.
  if (!CALM && 'IntersectionObserver' in window) {
    var rimgs = document.querySelectorAll('.img-rv');
    var rio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting || e.boundingClientRect.top < 0) { e.target.classList.add('in'); rio.unobserve(e.target); } }); }, { threshold: [0, 0.15] });
    rimgs.forEach(function (el) { if (el.getBoundingClientRect().top < innerHeight * 0.9) el.classList.add('in'); else rio.observe(el); });
  }
})();
