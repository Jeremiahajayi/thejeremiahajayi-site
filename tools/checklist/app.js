(function () {
  var wrap = document.querySelector('.lc-wrap');
  var dataEl = document.getElementById('lc-data');
  if (!wrap || !dataEl) return;
  var D = JSON.parse(dataEl.textContent);
  var TASK = {}; D.tasks.forEach(function (t) { TASK[t.id] = t; });
  var STAGE = {}; D.stages.forEach(function (s) { STAGE[s.n] = s; });
  var KEY = 'jaLaunchPlan.v2';
  var TPL_TYPE = { brief: 'gtm_brief', measure: 'launch_measurement', review: 'launch_review' };

  /* ---------- state (browser only) ---------- */
  var S = { tier: '1', tasks: {}, owners: {}, notes: {}, details: {}, fired: {}, tpl: { brief: {}, measure: {}, review: {} } };
  var store = null;
  try { store = window.localStorage; store.getItem(KEY); } catch (e) { store = null; }
  if (store) {
    try {
      var saved = JSON.parse(store.getItem(KEY) || 'null');
      if (saved && typeof saved === 'object') { for (var k in S) if (saved[k] != null) S[k] = saved[k]; }
      else {
        // migrate the first version of the checklist: { id: true } and a separate tier key
        var old = JSON.parse(store.getItem('jaLaunchChecklist') || '{}') || {};
        Object.keys(old).forEach(function (id) { if (old[id] && TASK[id]) S.tasks[id] = 'done'; });
        var ot = store.getItem('jaLaunchTier'); if (ot && D.tiers[ot]) S.tier = ot;
      }
    } catch (e) {}
  }
  ['brief', 'measure', 'review'].forEach(function (k) { if (!S.tpl[k]) S.tpl[k] = {}; });
  if (!D.tiers[S.tier]) S.tier = '1';
  var saveT;
  function save() { if (!store) return; clearTimeout(saveT); saveT = setTimeout(function () { try { store.setItem(KEY, JSON.stringify(S)); } catch (e) {} }, 150); }

  /* ---------- analytics: the site's existing GA4 gtag; no personal or typed content is sent ---------- */
  function track(name, params) { try { if (typeof window.gtag === 'function') window.gtag('event', name, params || {}); } catch (e) {} }

  /* ---------- dates ---------- */
  function parseDay(s) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || ''); return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null; }
  function today() { var d = new Date(); return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }
  function addDays(d, n) { return new Date(d.getFullYear(), d.getMonth(), d.getDate() + n); }
  function diffDays(a, b) { return Math.round((a - b) / 864e5); }
  function fmt(d) { return d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' }); }
  function iso(d) { return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }

  function plan() {
    var launch = parseDay(S.details.date), t0 = today();
    if (!launch) return { launch: null };
    var lead = D.tiers[S.tier].lead, left = diffDays(launch, t0);
    return { launch: launch, left: left, lead: lead, compressed: left >= 0 && left < lead, past: left < 0, today: t0 };
  }
  function offsetFor(t, tier) { return (t.due && t.due[tier] != null) ? t.due[tier] : STAGE[t.stage].w[tier][2]; }
  function dueFor(t, p) {
    if (!p.launch) return null;
    var off = offsetFor(t, S.tier);
    if (p.compressed && off < 0) off = Math.round(off * p.left / p.lead);
    return addDays(p.launch, off);
  }
  function stageRange(st, p) {
    if (!p.launch) return '';
    var w = st.w[S.tier], a = w[1], b = w[2];
    if (p.compressed) { if (a < 0) a = Math.round(a * p.left / p.lead); if (b < 0) b = Math.round(b * p.left / p.lead); }
    var da = addDays(p.launch, a), db = addDays(p.launch, b);
    return ' · ' + (a === b ? fmt(da) : fmt(da) + ' – ' + fmt(db));
  }

  /* ---------- build the interactive task controls ---------- */
  var ownerOpts = D.owners.map(function (o) { return '<option>' + o + '</option>'; }).join('');
  var items = [].slice.call(document.querySelectorAll('.lc-task'));
  items.forEach(function (li) {
    var id = li.dataset.id, t = TASK[id], meta = li.querySelector('.lc-meta');
    meta.innerHTML =
      '<span class="lc-chip lc-due" hidden></span><span class="lc-chip pri lc-pri" hidden>Priority</span><span class="lc-chip nastate lc-nas" hidden>Not applicable</span>' +
      '<label class="lc-ownw"><span>Owner</span><select class="lc-own" data-id="' + id + '" aria-label="Owner for: ' + t.t.replace(/"/g, '&quot;') + '">' + ownerOpts + '</select></label>' +
      (t.na ? '<button type="button" class="lc-mini lc-na" data-id="' + id + '" aria-pressed="false">Not applicable</button>' : '') +
      '<button type="button" class="lc-mini lc-nt" data-id="' + id + '" aria-expanded="false">Note</button>';
    var nw = document.createElement('div'); nw.className = 'lc-notew'; nw.hidden = true;
    nw.innerHTML = '<label class="sr" for="note-' + id + '">Note for this task</label><textarea id="note-' + id + '" data-id="' + id + '" rows="2" placeholder="Add a note: links, decisions, who’s helping"></textarea>';
    meta.after(nw);
    var ta = nw.querySelector('textarea'); ta.value = S.notes[id] || ''; if (ta.value) nw.hidden = false;
  });
  wrap.classList.add('lc-on');

  /* ---------- render ---------- */
  var announce = false, lastLive = '';
  function render() {
    var tier = S.tier, p = plan(), t0 = today(), tot = 0, done = 0, na = 0;
    document.querySelectorAll('.lc-tb').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.tier === tier ? 'true' : 'false'); });
    document.querySelectorAll('.lc-tc').forEach(function (c) { c.classList.toggle('on', c.dataset.tc === tier); });
    var byStage = {};
    items.forEach(function (li) {
      var id = li.dataset.id, t = TASK[id], vis = t.tiers.indexOf(tier) > -1, st = S.tasks[id];
      li.hidden = !vis;
      li.querySelector('.lc-title').textContent = (tier === '3' && t.t3) ? t.t3 : t.t;
      li.querySelector('.lc-desc').textContent = (tier === '3' && t.d3) ? t.d3 : t.d;
      var cb = li.querySelector('.lc-cb');
      cb.checked = st === 'done'; cb.disabled = st === 'na';
      li.classList.toggle('done', st === 'done'); li.classList.toggle('na', st === 'na');
      var nab = li.querySelector('.lc-na'); if (nab) { nab.setAttribute('aria-pressed', st === 'na' ? 'true' : 'false'); nab.textContent = st === 'na' ? 'Undo not applicable' : 'Not applicable'; }
      li.querySelector('.lc-nas').hidden = st !== 'na';
      var sel = li.querySelector('.lc-own'); sel.value = S.owners[id] || t.owner;
      var due = dueFor(t, p), dc = li.querySelector('.lc-due');
      if (due && st !== 'na') { dc.hidden = false; var late = due < t0 && st !== 'done'; dc.textContent = (late ? 'Overdue · ' : 'Due ') + fmt(due); dc.classList.toggle('late', late); }
      else dc.hidden = true;
      li.querySelector('.lc-pri').hidden = !(p.compressed && t.pri && vis && st !== 'na' && st !== 'done');
      if (!vis) return;
      var b = byStage[t.stage] || (byStage[t.stage] = { tot: 0, done: 0 });
      if (st === 'na') { na++; return; }
      tot++; b.tot++; if (st === 'done') { done++; b.done++; }
    });
    document.querySelectorAll('.lc-phase').forEach(function (sec) {
      var st = STAGE[+sec.dataset.stage], b = byStage[st.n];
      sec.hidden = !b;
      sec.querySelector('.lc-sh').textContent = tier === '3' ? st.h3 : st.h;
      sec.querySelector('.lc-sw').textContent = st.w[tier][0];
      sec.querySelector('.lc-sd').textContent = stageRange(st, p);
      sec.querySelector('.lc-sc').textContent = b ? b.done + ' of ' + b.tot + ' done' : '';
    });
    var name = D.tiers[tier].name, txt = 'Tier ' + tier + ' · ' + done + ' of ' + tot + ' complete' + (na ? ' · ' + na + ' not applicable' : '');
    document.getElementById('lc-st-t').textContent = txt;
    document.getElementById('lc-fill').style.width = (tot ? Math.round(done / tot * 100) : 0) + '%';
    if (announce && txt !== lastLive) { document.getElementById('lc-live').textContent = done + ' of ' + tot + ' tasks complete for a ' + name.toLowerCase() + '.'; }
    lastLive = txt; announce = false;
    // milestones, once per tier
    var pct = tot ? done / tot * 100 : 0;
    [25, 50, 75, 100].forEach(function (m) { var k = tier + ':' + m; if (pct >= m && !S.fired[k]) { S.fired[k] = 1; track('checklist_progress_milestone', { launch_tier: tier, milestone: m }); save(); } });
    // timing banner
    var bn = document.querySelector('.lc-banner');
    if (!p.launch) { bn.hidden = true; }
    else if (p.past) { bn.hidden = false; bn.className = 'lc-banner warn'; bn.innerHTML = '<b>That launch date has passed.</b> The due dates below are in the past. If the launch is still ahead, update the date in step 2.'; }
    else if (p.compressed) {
      bn.hidden = false; bn.className = 'lc-banner warn';
      bn.innerHTML = '<b>Your launch is ' + (p.left === 0 ? 'today' : 'in ' + p.left + ' day' + (p.left === 1 ? '' : 's')) + '.</b> A ' + name.toLowerCase() + ' usually needs about ' + D.tiers[tier].time.toLowerCase() + ', so the dates below are compressed to fit. Do the tasks marked <b>Priority</b> first, mark anything that doesn’t apply, and consider moving the date or launching with a smaller scope.';
    } else { bn.hidden = false; bn.className = 'lc-banner'; bn.innerHTML = '<b>Planned back from ' + fmt(p.launch) + '.</b> Suggested due dates are a starting point. Adjust them to how your team works.'; }
    // print header
    var d = S.details, ph = document.querySelector('.lc-print-head');
    ph.textContent = [d.name || 'Launch plan', d.company, 'Tier ' + tier + ' · ' + name, p.launch ? 'Launch date: ' + fmt(p.launch) : '', d.owner ? 'Owner: ' + d.owner : '', txt].filter(Boolean).join('  ·  ');
    // brief tier field mirrors the selection
    var bt = document.getElementById('f-b_tier'); if (bt && !S.tpl.brief.b_tier) bt.placeholder = 'Tier ' + tier + ' · ' + name;
  }

  function setTier(t, how) {
    if (!D.tiers[t]) return;
    var changed = S.tier !== t; S.tier = t; announce = true; save(); render();
    if (changed || how === 'guide') track('launch_tier_selected', { launch_tier: t, method: how });
  }

  /* ---------- checklist events ---------- */
  document.getElementById('checklist').addEventListener('change', function (e) {
    var el = e.target;
    if (el.classList.contains('lc-cb')) {
      var id = el.dataset.id;
      if (el.checked) { S.tasks[id] = 'done'; track('checklist_task_completed', { launch_tier: S.tier, task_id: id, stage: TASK[id].stage }); }
      else delete S.tasks[id];
      announce = true; save(); render();
    } else if (el.classList.contains('lc-own')) {
      var oid = el.dataset.id; if (el.value === TASK[oid].owner) delete S.owners[oid]; else S.owners[oid] = el.value; save();
    }
  });
  document.getElementById('checklist').addEventListener('input', function (e) {
    var el = e.target; if (el.tagName === 'TEXTAREA' && el.dataset.id) { if (el.value) S.notes[el.dataset.id] = el.value; else delete S.notes[el.dataset.id]; save(); }
  });
  document.getElementById('checklist').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.classList.contains('lc-na')) { var id = b.dataset.id; if (S.tasks[id] === 'na') delete S.tasks[id]; else S.tasks[id] = 'na'; announce = true; save(); render(); }
    else if (b.classList.contains('lc-nt')) { var w = b.closest('.lc-task').querySelector('.lc-notew'); w.hidden = !w.hidden; b.setAttribute('aria-expanded', w.hidden ? 'false' : 'true'); if (!w.hidden) w.querySelector('textarea').focus(); }
    else if (b.classList.contains('lc-tb')) setTier(b.dataset.tier, 'button');
  });

  /* ---------- tier guide ---------- */
  var quiz = document.querySelector('.lc-quiz'), rec = quiz.querySelector('.lc-rec'), recTier = null;
  var WHY = {
    '1': 'It changes what you sell, who you sell to or how you’re positioned, so it’s worth the full plan: GTM brief, sales enablement, partner and press planning, and measures agreed in advance. Plan on about 6–8 weeks.',
    '2': 'It matters to buyers and live deals, but doesn’t change your positioning. Give it messaging, sales enablement and a product page update, without press or partner work. Plan on about 3–4 weeks.',
    '3': 'It mainly improves things for existing users. A short release note, a help doc, an in-app message and a mention in your next customer email is usually enough. Plan on about a week.',
    '3x': 'It’s not a big change in positioning or sales, and not mainly for existing users either. Start with Tier 3, and move up to Tier 2 if sales expects to use it in deals.'
  };
  function val(n) { var c = quiz.querySelector('input[name="' + n + '"]:checked'); return c ? c.value : null; }
  quiz.addEventListener('change', function () {
    var a = val('q1'), b = val('q2'), c = val('q3');
    quiz.querySelector('[data-q="2"]').hidden = a !== 'no';
    quiz.querySelector('[data-q="3"]').hidden = !(a === 'no' && b === 'no');
    var r = null, why = '';
    if (a === 'yes') { r = '1'; why = WHY['1']; }
    else if (a === 'no' && b === 'yes') { r = '2'; why = WHY['2']; }
    else if (a === 'no' && b === 'no' && c) { r = '3'; why = c === 'yes' ? WHY['3'] : WHY['3x']; }
    recTier = r; rec.hidden = !r;
    if (r) { rec.querySelector('.lc-rec-t').textContent = 'We suggest Tier ' + r + ': ' + D.tiers[r].name.toLowerCase(); rec.querySelector('.lc-rec-w').textContent = why; rec.querySelector('[data-use-rec]').textContent = S.tier === r ? 'Tier ' + r + ' is selected' : 'Use Tier ' + r; }
  });
  rec.querySelector('[data-use-rec]').addEventListener('click', function () {
    if (!recTier) return; setTier(recTier, 'guide'); this.textContent = 'Tier ' + recTier + ' is selected';
    document.getElementById('details').scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
  });
  quiz.querySelector('[data-quiz-reset]').addEventListener('click', function () {
    quiz.querySelectorAll('input').forEach(function (i) { i.checked = false; });
    quiz.querySelector('[data-q="2"]').hidden = true; quiz.querySelector('[data-q="3"]').hidden = true; rec.hidden = true; recTier = null;
    quiz.querySelector('input[name="q1"]').focus();
  });

  /* ---------- launch details ---------- */
  document.querySelectorAll('[data-d]').forEach(function (inp) {
    inp.value = S.details[inp.dataset.d] || '';
    inp.addEventListener('input', function () { S.details[inp.dataset.d] = inp.value; save(); if (inp.dataset.d === 'date' || inp.dataset.d === 'name') render(); });
    inp.addEventListener('change', function () { render(); });
  });

  /* ---------- export, print, reset ---------- */
  function csvCell(v) { v = v == null ? '' : String(v); return /[",\n\r]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }
  function download(name, text, type) {
    var blob = new Blob([text], { type: type }), a = document.createElement('a');
    a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function slug(s) { return (s || 'launch').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40) || 'launch'; }
  document.getElementById('lc-csv').addEventListener('click', function () {
    var p = plan(), d = S.details, tier = S.tier, rows = [];
    rows.push(['Launch', 'Company', 'Tier', 'Launch date', 'Launch owner', 'Stage', 'Stage timing', 'Task', 'What it involves', 'Owner', 'Due date', 'Priority', 'Status', 'Notes']);
    D.tasks.forEach(function (t) {
      if (t.tiers.indexOf(tier) < 0) return;
      var st = S.tasks[t.id], due = dueFor(t, p), stage = STAGE[t.stage];
      rows.push([d.name || '', d.company || '', 'Tier ' + tier + ' · ' + D.tiers[tier].name, p.launch ? iso(p.launch) : '', d.owner || '',
        t.stage + '. ' + (tier === '3' ? stage.h3 : stage.h), stage.w[tier][0],
        (tier === '3' && t.t3) ? t.t3 : t.t, (tier === '3' && t.d3) ? t.d3 : t.d,
        S.owners[t.id] || t.owner, due && st !== 'na' ? iso(due) : '', p.compressed && t.pri ? 'Yes' : '',
        st === 'done' ? 'Done' : st === 'na' ? 'Not applicable' : 'To do', S.notes[t.id] || '']);
    });
    download('launch-plan-' + slug(d.name) + '-tier-' + tier + '.csv', '﻿' + rows.map(function (r) { return r.map(csvCell).join(','); }).join('\r\n'), 'text/csv;charset=utf-8');
    track('launch_plan_exported', { launch_tier: tier, format: 'csv', has_date: !!p.launch });
  });
  document.getElementById('lc-print').addEventListener('click', function () { track('launch_plan_exported', { launch_tier: S.tier, format: 'print' }); window.print(); });
  document.getElementById('lc-reset').addEventListener('click', function () {
    if (!window.confirm('Clear all ticked tasks, not-applicable marks, owners and notes for this checklist? Your launch details and templates stay. This can’t be undone.')) return;
    S.tasks = {}; S.owners = {}; S.notes = {}; S.fired = {};
    document.querySelectorAll('.lc-notew textarea').forEach(function (t) { t.value = ''; t.closest('.lc-notew').hidden = true; });
    announce = true; save(); render();
  });

  /* ---------- templates ---------- */
  var EX = {
    brief: {
      b_product: 'Multi-entity approvals: route every spend request to the right approver in each legal entity.',
      b_customer: 'Finance teams at companies with 3–20 legal entities. Users: finance managers. Decision: the Financial Controller. Sign-off: the CFO.',
      b_problem: '“Every entity has its own approval rules, so we chase approvals over email and fix mistakes at month-end.”',
      b_alternative: 'Email and spreadsheets, approvals inside the ERP, or doing nothing and fixing problems at close.',
      b_positioning: 'For finance teams at multi-entity companies who approve spend over email, Fernway is the spend management platform that routes every request to the right approver. Unlike email and ERP workflows, it keeps one audit trail across every entity.',
      b_value: 'Close the month faster, with every approval recorded.',
      b_proof: 'Beta: 6 customers. Example: one beta customer cut month-end approval chasing from 3 days to 1. Demo video of a cross-entity approval.',
      b_usecase: 'A logistics company with 7 entities moved approvals out of email; auditors now get one report instead of 7 spreadsheets.',
      b_tier: 'Tier 1 · Major launch',
      b_objectives: 'Create conversations with multi-entity prospects; move open deals that stalled on approvals; get 30% of multi-entity customers using it.',
      b_metrics: '40 qualified demo requests; 12 opportunities; adoption by 30% of eligible customers in 60 days.',
      b_owner: 'Ada (product marketing), 3 March',
      b_risks: 'ERP sync must ship by 17 February; legal review of the audit trail claims; partner logo approval from the ERP partner.'
    },
    review: {
      r_launched: 'Multi-entity approvals, Tier 1, launched 3 March.',
      r_objectives: 'Conversations with multi-entity prospects; unblock stalled deals; 30% adoption among eligible customers in 60 days.',
      r_results: 'Demo requests: 31 vs a target of 40. Opportunities: 9 vs 12. Adoption at 30 days: 18%, on track for 30% at 60 days.',
      r_channels: 'Founder posts and the customer email brought most qualified demo requests. Paid social brought clicks but few qualified buyers.',
      r_sales: 'Buyers asked about ERP sync more than approvals. Two stalled deals restarted after the demo video.',
      r_adoption: 'Customers with 5+ entities adopted first. Most support questions were about setting approval limits.',
      r_worked: 'The use case story from the logistics customer; the sales one-pager.',
      r_under: 'The landing page: visitors left before the demo. Paid social.',
      r_next: 'Rewrite the landing page around ERP sync; build a setup guide for approval limits; check pipeline again at 60 and 90 days.',
      r_owners: 'Ada: landing page by 31 March. Tunde: setup guide by 24 March. Ada: 60-day pipeline check on 2 May.'
    },
    measure: {
      demos: ['25 a month', '40', '31'], opps: ['8 a month', '12', '9'], sourced: ['$60K a month', '$120K', '$95K'],
      influenced: ['n/a', '$300K', '$240K'], adoption: ['0%', '30% at 60 days', '18% at 30 days'], usage: ['', '80% of reps', '65% of reps'], questions: ['', '', '']
    }
  };
  var activeDlg = null, lastFocus = null;
  function fillForm(k, form) {
    var v = S.tpl[k] || {};
    form.querySelectorAll('input,textarea').forEach(function (f) {
      if (!f.name) return;
      if (f.type === 'checkbox') { if (v[f.name] != null) f.checked = !!v[f.name]; }
      else f.value = v[f.name] || '';
    });
  }
  function openTpl(k, trigger) {
    var dlg = document.getElementById('dlg-' + k); if (!dlg) return;
    var form = dlg.querySelector('form'); fillForm(k, form);
    lastFocus = trigger || document.activeElement; activeDlg = dlg;
    if (typeof dlg.showModal === 'function') dlg.showModal(); else dlg.setAttribute('open', '');
    var first = form.querySelector('textarea,input[type=text]'); if (first) first.focus();
    if (k === 'review') track('launch_review_template_opened', { launch_tier: S.tier });
    else track('gtm_template_opened', { template_type: TPL_TYPE[k], launch_tier: S.tier });
  }
  document.addEventListener('click', function (e) { var b = e.target.closest('[data-open]'); if (b) { e.preventDefault(); openTpl(b.dataset.open, b); } });
  function textFor(k, form) {
    var d = S.details, head = (d.name ? d.name + ' · ' : '') + (d.company || '');
    if (k === 'measure') {
      var lines = ['Launch measurement' + (head ? ' · ' + head : ''), '', '| Metric | Baseline | Target | Actual | Source |', '| --- | --- | --- | --- | --- |'];
      D.measures.forEach(function (m) {
        if (!form.querySelector('[name="m_' + m.k + '_on"]').checked) return;
        var g = function (s) { return (form.querySelector('[name="m_' + m.k + '_' + s + '"]').value || '').replace(/\|/g, '/'); };
        lines.push('| ' + m.n + ' | ' + g('base') + ' | ' + g('target') + ' | ' + g('actual') + ' | ' + (g('src') || m.s) + ' |');
      });
      return lines.join('\n');
    }
    var title = k === 'brief' ? 'GTM brief' : '30-day launch review', out = [title + (head ? ' · ' + head : ''), ''];
    D[k].forEach(function (f) { var v = form.querySelector('[name="' + f[0] + '"]').value.trim(); out.push(f[1].toUpperCase()); out.push(v || '—'); out.push(''); });
    return out.join('\n');
  }
  function measureCsv(form) {
    var rows = [['Metric', 'Baseline', 'Target', 'Actual', 'Source']];
    D.measures.forEach(function (m) {
      if (!form.querySelector('[name="m_' + m.k + '_on"]').checked) return;
      var g = function (s) { return form.querySelector('[name="m_' + m.k + '_' + s + '"]').value; };
      rows.push([m.n, g('base'), g('target'), g('actual'), g('src') || m.s]);
    });
    return '﻿' + rows.map(function (r) { return r.map(csvCell).join(','); }).join('\r\n');
  }
  document.querySelectorAll('.lc-dlg').forEach(function (dlg) {
    var form = dlg.querySelector('form'), k = form.dataset.tpl, msg = dlg.querySelector('.lc-msg'), note = dlg.querySelector('.lc-exnote');
    function flash(t) { msg.textContent = t; setTimeout(function () { if (msg.textContent === t) msg.textContent = ''; }, 2500); }
    function persist() {
      var v = {}; form.querySelectorAll('input,textarea').forEach(function (f) { if (f.name) v[f.name] = f.type === 'checkbox' ? f.checked : f.value; });
      S.tpl[k] = v; save();
    }
    form.addEventListener('input', persist); form.addEventListener('change', persist);
    form.addEventListener('keydown', function (e) { if (e.key === 'Enter' && e.target.tagName === 'INPUT') e.preventDefault(); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener('close', function () { activeDlg = null; if (lastFocus && lastFocus.focus) lastFocus.focus(); render(); });
    form.addEventListener('click', function (e) {
      var b = e.target.closest('[data-act]'); if (!b) return;
      var act = b.dataset.act;
      if (act === 'example') {
        var has = [].some.call(form.querySelectorAll('input[type=text],textarea'), function (f) { return f.value.trim(); });
        if (has && !window.confirm('Replace what you’ve written with the fictional example?')) return;
        if (k === 'measure') D.measures.forEach(function (m) { var x = EX.measure[m.k]; form.querySelector('[name="m_' + m.k + '_base"]').value = x[0]; form.querySelector('[name="m_' + m.k + '_target"]').value = x[1]; form.querySelector('[name="m_' + m.k + '_actual"]').value = x[2]; });
        else Object.keys(EX[k]).forEach(function (n) { var f = form.querySelector('[name="' + n + '"]'); if (f) f.value = EX[k][n]; });
        note.hidden = false; persist();
      } else if (act === 'clear') {
        if (!window.confirm('Clear this template?')) return;
        form.querySelectorAll('input[type=text],textarea').forEach(function (f) { f.value = ''; }); note.hidden = true; persist();
      } else if (act === 'copy') {
        var text = textFor(k, form);
        var done = function () { flash('Copied'); };
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text) ? done() : flash('Copy didn’t work here. Use Download.'); });
        else fallbackCopy(text) ? done() : flash('Copy didn’t work here. Use Download.');
      } else if (act === 'download') {
        var base = slug(S.details.name);
        if (k === 'measure') download('launch-measurement-' + base + '.csv', measureCsv(form), 'text/csv;charset=utf-8');
        else download((k === 'brief' ? 'gtm-brief-' : 'launch-review-') + base + '.txt', textFor(k, form), 'text/plain;charset=utf-8');
        flash('Downloaded');
      }
    });
  });
  function fallbackCopy(text) {
    var t = document.createElement('textarea'); t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
    document.body.appendChild(t); t.select(); var ok = false; try { ok = document.execCommand('copy'); } catch (e) {} t.remove(); return ok;
  }

  /* ---------- outbound link events ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-track]'); if (a) track(a.dataset.track, { link_location: a.dataset.loc || 'page', launch_tier: S.tier });
  });

  render();
})();
