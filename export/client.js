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
})();
