(function () {
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
})();
