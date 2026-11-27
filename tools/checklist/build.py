#!/usr/bin/env python3
"""Build tools/b2b-saas-launch-checklist.html from data.py, style.css and app.js.

The page is static HTML (fully readable without JavaScript, in Tier 1 wording) that app.js
then enhances: tier guide, tier-specific wording and timings, owners, due dates, not-applicable
states, templates, CSV export and GA4 events. export.js wraps the result in the site shell.
"""
import html, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from data import OWNERS, TIERS, STAGES, TASKS, GUIDES

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / 'b2b-saas-launch-checklist.html'
e = lambda s: html.escape(s, quote=True)

assert len(TASKS) == 33, len(TASKS)
counts = {t: sum(1 for x in TASKS if t in x['tiers']) for t in '123'}
assert counts == {'1': 33, '2': 28, '3': 9}, counts
assert len({x['id'] for x in TASKS}) == 33
for x in TASKS:
    assert x['owner'] in OWNERS, x
    assert x.get('guide') in (None, *GUIDES), x
    if '3' in x['tiers']:
        assert 't3' in x and 'd3' in x, x['id']

TPL_LABEL = {'brief': ('Open the GTM brief template', 'brief'), 'measure': ('Open the measurement template', 'measure'), 'review': ('Open the 30-day review template', 'review')}


def guide_html(key):
    g = GUIDES[key]
    out = [f'<details class="lc-guide"><summary>What good looks like</summary><div class="lc-guide-b">',
           f'<p><b>What to produce.</b> {e(g["produce"])}</p>',
           '<p><b>A simple structure</b></p><ul>' + ''.join(f'<li>{e(s)}</li>' for s in g['structure']) + '</ul>']
    if g.get('example'):
        out.append(f'<p class="lc-ex"><b>Example.</b> {e(g["example"])}</p>')
    out.append(f'<p><b>Common mistake.</b> {e(g["mistake"])}</p>')
    if g.get('template'):
        lab, k = TPL_LABEL[g['template']]
        out.append(f'<p><button type="button" class="lc-btn lc-btn-s" data-open="{k}">{lab}</button></p>')
    out.append('</div></details>')
    return ''.join(out)


def task_html(x):
    st = STAGES[x['stage'] - 1]
    return (f'<li class="lc-task" id="task-{x["id"]}" data-id="{x["id"]}" data-t="{x["tiers"]}">'
            f'<label class="lc-main"><input type="checkbox" class="lc-cb" data-id="{x["id"]}">'
            f'<span class="lc-txt"><b class="lc-title">{e(x["t"])}</b><span class="lc-desc">{e(x["d"])}</span></span></label>'
            f'<div class="lc-meta"><span class="lc-chip lc-own-static">Suggested owner: {e(x["owner"])}</span></div>'
            + (guide_html(x['guide']) if x.get('guide') else '') + '</li>')


def stage_html(st):
    w = st['w']['1']
    items = ''.join(task_html(x) for x in TASKS if x['stage'] == st['n'])
    return (f'<section class="lc-phase" data-stage="{st["n"]}" aria-labelledby="st{st["n"]}-h">'
            f'<div class="lc-ph"><h3 id="st{st["n"]}-h"><span class="lc-sn">{st["n"]}.</span> <span class="lc-sh">{e(st["h"])}</span></h3>'
            f'<p class="lc-when"><span class="lc-sw">{e(w[0])}</span><span class="lc-sd"></span></p><p class="lc-sc"></p></div>'
            f'<ul class="lc-items">{items}</ul></section>')


def field(name, label, hint='', rows=2, kind='textarea'):
    hid = f'f-{name}'
    h = f'<span class="lc-hint">{e(hint)}</span>' if hint else ''
    ctrl = (f'<textarea id="{hid}" name="{name}" rows="{rows}"></textarea>' if kind == 'textarea'
            else f'<input id="{hid}" name="{name}" type="text">')
    return f'<div class="lc-f"><label for="{hid}">{e(label)}</label>{h}{ctrl}</div>'


BRIEF_FIELDS = [
    ('b_product', 'Product or feature being launched', 'One sentence. What is it, in plain words?', 2),
    ('b_customer', 'Target customer and buying roles', 'Who uses it, who decides, who signs off?', 2),
    ('b_problem', 'Customer problem', 'In the customer’s words, if you have them.', 2),
    ('b_alternative', 'Current alternative', 'What they do today, including doing nothing.', 2),
    ('b_positioning', 'Positioning statement', 'For [who] who [problem], [product] is the [category] that [benefit]. Unlike [alternative], it [difference].', 3),
    ('b_value', 'Primary value proposition', 'The main outcome for the buyer.', 2),
    ('b_proof', 'Supporting proof', 'Numbers, customers, demos: anything a buyer can check.', 3),
    ('b_usecase', 'Customer use case', 'A specific customer, situation and result.', 2),
    ('b_tier', 'Launch tier', '', 1),
    ('b_objectives', 'Launch objectives', 'What should be different 30 days after launch?', 2),
    ('b_metrics', 'Success metrics', 'Three to five, with targets. The measurement template can help.', 2),
    ('b_owner', 'Launch owner and date', '', 1),
    ('b_risks', 'Dependencies and risks', 'Approvals, engineering dates, partners, legal.', 2),
]
REVIEW_FIELDS = [
    ('r_launched', 'What we launched', '', 2),
    ('r_objectives', 'Original objectives', 'Copy them from the GTM brief.', 2),
    ('r_results', 'Results against targets', 'Target, actual and the gap for each measure.', 3),
    ('r_channels', 'Channels that brought qualified engagement', 'Not just the most reach: which channels led to conversations?', 2),
    ('r_sales', 'What sales learned from conversations', 'Objections, questions, deals it helped or didn’t.', 2),
    ('r_adoption', 'Early adoption signals', 'Who used it, how often, and what they asked support.', 2),
    ('r_worked', 'What worked', '', 2),
    ('r_under', 'What underperformed', '', 2),
    ('r_next', 'What we’ll do next', '', 2),
    ('r_owners', 'Owners and dates for follow-up actions', 'Name, action, date.', 2),
]
MEASURES = [
    ('demos', 'Qualified demo requests', 'CRM', True),
    ('opps', 'Opportunities created', 'CRM', True),
    ('sourced', 'Sourced pipeline', 'CRM', True),
    ('influenced', 'Influenced pipeline', 'CRM', True),
    ('adoption', 'Product adoption', 'Product analytics', True),
    ('usage', 'Sales usage of launch assets', 'Sales team', False),
    ('questions', 'Customer questions and support tickets', 'Support desk', False),
]


def dialog(key, title, intro, body, example_note):
    return f'''<dialog class="lc-dlg" id="dlg-{key}" aria-labelledby="dlg-{key}-h">
<form method="dialog" class="lc-dlg-in" data-tpl="{key}">
<div class="lc-dlg-top"><h2 id="dlg-{key}-h">{e(title)}</h2><button type="submit" class="lc-x" aria-label="Close">×</button></div>
<p class="lc-dlg-intro">{intro}</p>
<div class="lc-dlg-acts"><button type="button" class="lc-btn lc-btn-s" data-act="example">Show the fictional example</button><button type="button" class="lc-btn lc-btn-s" data-act="clear">Clear</button></div>
<p class="lc-exnote" hidden>{e(example_note)}</p>
{body}
<div class="lc-dlg-foot"><button type="button" class="lc-btn" data-act="copy">Copy</button><button type="button" class="lc-btn" data-act="download">Download</button><button type="submit" class="lc-btn lc-btn-ghost">Done</button><span class="lc-msg" role="status" aria-live="polite"></span></div>
<p class="lc-saved">Saved in this browser as you type. Nothing is sent anywhere.</p>
</form></dialog>'''


def measure_body():
    rows = ''.join(
        f'<tr data-m="{k}"><td><label class="lc-mi"><input type="checkbox" name="m_{k}_on"{" checked" if on else ""}> <span>{e(n)}</span></label></td>'
        f'<td><label class="lc-ml" for="m_{k}_base"><span class="sr">{e(n)} </span>Baseline</label><input id="m_{k}_base" name="m_{k}_base" type="text" placeholder="Baseline"></td>'
        f'<td><label class="lc-ml" for="m_{k}_target"><span class="sr">{e(n)} </span>Target</label><input id="m_{k}_target" name="m_{k}_target" type="text" placeholder="Target"></td>'
        f'<td><label class="lc-ml" for="m_{k}_actual"><span class="sr">{e(n)} </span>Actual</label><input id="m_{k}_actual" name="m_{k}_actual" type="text" placeholder="Actual"></td>'
        f'<td><label class="lc-ml" for="m_{k}_src"><span class="sr">{e(n)} </span>Source</label><input id="m_{k}_src" name="m_{k}_src" type="text" placeholder="{e(s)}"></td></tr>'
        for k, n, s, on in MEASURES)
    return f'''<div class="lc-note-box"><p><b>Sourced or influenced?</b> Sourced pipeline is from opportunities that started with the launch, for example a demo request from the launch page. Influenced pipeline is from opportunities that already existed or started elsewhere, where the launch played a part, for example a rep sending the launch one-pager in a live deal. Agree how you’ll count each one before launch, so the numbers aren’t argued about afterwards.</p>
<p>These are examples, not requirements. Tick the measures that fit this launch and leave the rest.</p></div>
<div class="lc-mt-wrap"><table class="lc-mt"><thead><tr><th scope="col">Metric</th><th scope="col">Baseline</th><th scope="col">Target</th><th scope="col">Actual</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table></div>'''


def build():
    data = {
        'owners': OWNERS, 'tiers': TIERS,
        'stages': [{'n': s['n'], 'h': s['h'], 'h3': s['h3'], 'w': s['w']} for s in STAGES],
        'tasks': [{k: x[k] for k in ('id', 'stage', 'tiers', 'owner', 't', 'd', 't3', 'd3', 'due') if k in x} | {'na': bool(x.get('na')), 'pri': bool(x.get('pri'))} for x in TASKS],
        'measures': [{'k': k, 'n': n, 's': s} for k, n, s, _ in MEASURES],
        'brief': [(k, l) for k, l, *_ in BRIEF_FIELDS], 'review': [(k, l) for k, l, *_ in REVIEW_FIELDS],
    }
    css = (HERE / 'style.css').read_text()
    js = (HERE / 'app.js').read_text()
    tier_cards = ''.join(
        f'<div class="lc-tc" data-tc="{t}"><p class="lc-tc-n">Tier {t} · {e(v["name"])}</p><p>{e(v["what"])}</p><p class="lc-tc-t">{e(v["time"])}</p></div>'
        for t, v in TIERS.items())
    stages = ''.join(stage_html(s) for s in STAGES)
    brief = dialog('brief', 'One-page GTM brief',
                   'Fill this in before anyone writes a launch asset. It should take a founder 15–20 minutes. Share it with product and sales and agree it together.',
                   '<div class="lc-fields">' + ''.join(field(k, l, h, r, 'input' if k in ('b_tier', 'b_owner') else 'textarea') for k, l, h, r in BRIEF_FIELDS) + '</div>',
                   'Example only: Fernway is a fictional B2B SaaS company. Clear it before writing your own.')
    measure = dialog('measure', 'Launch measurement template',
                     'Set the baseline and target before launch, then fill in the actual results at 30 days. Download it as a CSV for Excel or Google Sheets.',
                     measure_body(), 'Example only: the numbers belong to Fernway, a fictional company. They are not benchmarks.')
    review = dialog('review', '30-day launch review',
                    'Run this with everyone who worked on the launch. At 30 days you can usually read engagement, demo requests, opportunities created, sales usage and early adoption. Pipeline progression, revenue and retention often need 60–90 days or longer, especially with enterprise sales cycles, so note what you’ll check again and when.',
                    '<div class="lc-fields">' + ''.join(field(k, l, h, r) for k, l, h, r in REVIEW_FIELDS) + '</div>',
                    'Example only: Fernway is a fictional company and these results are invented to show the format.')
    out = f'''<style>{css}</style>
<section class="lc-wrap"><div class="lc">
<p class="lc-crumb"><a href="/">Home</a> / <a href="/services/product-launch-gtm/">Launches &amp; GTM</a> / Launch checklist</p>
<h1>B2B SaaS product launch checklist<span>.</span></h1>
<p class="lc-lede">Go from “we have a launch coming up” to knowing what needs to happen, who does it, when, and how you’ll know it worked. Pick a launch tier, get a checklist sized to it with owners and dates, use the templates, and export the plan for your team.</p>
<div class="lc-meta-pills"><span class="lc-pill">Free, no signup</span><span class="lc-pill">33 tasks across six stages</span><span class="lc-pill">GTM brief, measurement and review templates</span><span class="lc-pill">Export to CSV or PDF</span></div>
<p class="lc-pair">Not sure you’re ready to launch at all? The <a href="/resources/gtm-scorecard/" data-track="readiness_scorecard_clicked" data-loc="intro">GTM Readiness Scorecard</a> answers “are we ready?”. This checklist answers “what needs to happen, and when?”.</p>

<section class="lc-sec" id="tier" aria-labelledby="tier-h">
<h2 id="tier-h"><span class="lc-step">1</span>How big a launch does this deserve?</h2>
<p class="lc-p">Not every release needs a press release. Answer up to three questions and we’ll suggest a tier. You can always pick a different one.</p>
<div class="lc-quiz lc-js">
<fieldset class="lc-q" data-q="1"><legend>Does this release introduce a new product, market or partnership, or significantly change your positioning?</legend><div class="lc-yn"><label><input type="radio" name="q1" value="yes"> Yes</label><label><input type="radio" name="q1" value="no"> No</label></div></fieldset>
<fieldset class="lc-q" data-q="2" hidden><legend>Will it materially affect purchase decisions, competitive differentiation or deals already in progress?</legend><div class="lc-yn"><label><input type="radio" name="q2" value="yes"> Yes</label><label><input type="radio" name="q2" value="no"> No</label></div></fieldset>
<fieldset class="lc-q" data-q="3" hidden><legend>Is it mainly an improvement for existing users?</legend><div class="lc-yn"><label><input type="radio" name="q3" value="yes"> Yes</label><label><input type="radio" name="q3" value="no"> No</label></div></fieldset>
<div class="lc-rec" hidden role="status" aria-live="polite"><p class="lc-rec-t"></p><p class="lc-rec-w"></p><div class="lc-rec-a"><button type="button" class="lc-btn" data-use-rec>Use this tier</button><button type="button" class="lc-btn lc-btn-ghost" data-quiz-reset>Start again</button></div></div>
</div>
<div class="lc-tcs">{tier_cards}</div>
</section>

<section class="lc-sec lc-js" id="details" aria-labelledby="details-h">
<h2 id="details-h"><span class="lc-step">2</span>Your launch details <span class="lc-opt">optional</span></h2>
<p class="lc-p">Add a launch date to get suggested due dates for every task. You can skip this and still use the checklist.</p>
<div class="lc-det">
<div class="lc-f"><label for="d-name">Launch name</label><input id="d-name" data-d="name" type="text" autocomplete="off" placeholder="e.g. Multi-entity approvals"></div>
<div class="lc-f"><label for="d-company">Company or product</label><input id="d-company" data-d="company" type="text" autocomplete="organization"></div>
<div class="lc-f"><label for="d-date">Target launch date</label><input id="d-date" data-d="date" type="date"></div>
<div class="lc-f"><label for="d-owner">Launch owner</label><input id="d-owner" data-d="owner" type="text" autocomplete="name"></div>
</div>
<p class="lc-save-note">Everything you enter is saved in this browser on this device only. It isn’t sent to us and won’t sync to your other devices.</p>
</section>

<section class="lc-sec" id="checklist" aria-labelledby="checklist-h">
<h2 id="checklist-h"><span class="lc-step">3</span>The checklist</h2>
<div class="lc-toolbar lc-js">
<div class="lc-tierbtns" role="group" aria-label="Launch tier"><button type="button" class="lc-tb" data-tier="1" aria-pressed="true">Tier 1<span> · Major</span></button><button type="button" class="lc-tb" data-tier="2" aria-pressed="false">Tier 2<span> · Feature</span></button><button type="button" class="lc-tb" data-tier="3" aria-pressed="false">Tier 3<span> · Small</span></button></div>
<div class="lc-acts"><button type="button" class="lc-act" id="lc-csv">Download plan (CSV)</button><button type="button" class="lc-act" id="lc-print">Print / PDF</button><button type="button" class="lc-act lc-act-q" id="lc-reset">Reset</button></div>
</div>
<div class="lc-print-head" aria-hidden="true"></div>
<div class="lc-banner" role="status" hidden></div>
<div class="lc-status lc-js"><span class="lc-st-t" id="lc-st-t">Tier 1 · 0 of 33 complete</span><span class="lc-track" aria-hidden="true"><span class="lc-fill" id="lc-fill"></span></span></div>
<p class="sr" id="lc-live" role="status" aria-live="polite"></p>
{stages}
</section>

<section class="lc-sec" id="templates" aria-labelledby="templates-h">
<h2 id="templates-h">Templates for the hard parts</h2>
<p class="lc-p">Free, editable and saved in your browser. Each one has a worked example from a fictional company, so you can see what good looks like before you start.</p>
<div class="lc-tpls">
<div class="lc-tpl"><h3>One-page GTM brief</h3><p>Product, buyer, problem, alternative, positioning, proof, objectives, metrics, owner and risks. About 15–20 minutes.</p><button type="button" class="lc-btn" data-open="brief">Open the template</button></div>
<div class="lc-tpl"><h3>Launch measurement</h3><p>Baseline, target and actual for the measures that fit your launch, with sourced and influenced pipeline explained.</p><button type="button" class="lc-btn" data-open="measure">Open the template</button></div>
<div class="lc-tpl"><h3>30-day launch review</h3><p>Results against targets, what sales learned, what worked and what to do next, with owners and dates.</p><button type="button" class="lc-btn" data-open="review">Open the template</button></div>
</div>
</section>

<section class="lc-sec" id="measure" aria-labelledby="measure-h">
<h2 id="measure-h">How to tell whether the launch worked</h2>
<p class="lc-p">Different things are knowable at different times. Judge each stage by what it can actually show you.</p>
<div class="lc-when-g">
<div class="lc-wc"><h3>Before launch</h3><p>Positioning tested with customers, a target account list, sales ready to use the launch, tracking working, and a baseline for every measure.</p></div>
<div class="lc-wc"><h3>Launch week</h3><p>Qualified engagement, demo requests, customer questions, the first sales conversations, and any technical issues.</p></div>
<div class="lc-wc"><h3>30 days after</h3><p>Opportunities created, sourced or influenced pipeline, how much sales used the assets, and early product adoption.</p></div>
<div class="lc-wc"><h3>Later</h3><p>Pipeline progression, revenue, retention and sustained adoption. With longer sales cycles, 30 days is often too early to judge revenue.</p></div>
</div>
<div class="lc-case">
<h3>Reading the numbers: a worked example</h3>
<p>A launch gets strong social engagement: plenty of likes, comments and shares. But two weeks later, sales has had very few qualified conversations from it. Before deciding the launch “didn’t work”, check:</p>
<ul>
<li><b>Audience fit.</b> Who engaged? Peers and other marketers, or people who could buy?</li>
<li><b>Messaging.</b> Did the posts explain the buyer’s problem, or mostly celebrate the feature?</li>
<li><b>Call to action.</b> Was there a clear next step for a buyer, and was it easy to take?</li>
<li><b>Lead quality.</b> Did the demo requests that came in match your target customer?</li>
<li><b>Sales follow-up.</b> Did sales contact the engaged accounts quickly, with a relevant message?</li>
<li><b>Measurement gaps.</b> Are conversations happening that tracking can’t see, such as buyers mentioning the launch on calls? A “How did you hear about us?” field helps here.</li>
</ul>
<p>Each answer points to a different fix: a different audience, sharper messaging, a better offer, or faster follow-up. That’s the point of measuring: to decide what to change next.</p>
</div>
<p class="lc-pair">Use the <a href="/resources/gtm-scorecard/" data-track="readiness_scorecard_clicked" data-loc="measurement">GTM Readiness Scorecard</a> before you start, to spot the gaps in positioning, sales alignment and distribution that most often hold a launch back.</p>
</section>

<section class="lc-sec" id="example" aria-labelledby="example-h">
<h2 id="example-h">See how this works in practice</h2>
<details class="lc-practice"><summary>The RemotePass × Certn partnership launch</summary><div class="lc-practice-b">
<p>RemotePass integrated Certn’s background checks into its platform, and launched the partnership in 2024. Here’s how parts of this checklist showed up in that launch, based on the public case study.</p>
<ol>
<li><b>Positioning (stage 1).</b> The integration was framed as proof that RemotePass was the safer, more compliant choice for regulated industries.</li>
<li><b>Partner alignment (stage 1).</b> The launch narrative and timing were agreed with Certn’s global marketing team.</li>
<li><b>Distribution (stages 2 and 5).</b> Global and Middle East press releases, the announcement blog, email and social posts.</li>
<li><b>Sales enablement (stage 3).</b> An enablement kit so the sales team could use the launch in live deals.</li>
<li><b>Outcome.</b> 270+ media pickups, including Yahoo Finance, Fox and NBC.</li>
</ol>
<p><a href="/work/#certn" data-track="case_study_clicked" data-loc="practice">Read the full case study</a></p>
</div></details>
</section>

<div class="lc-sec" id="subscribe"><div class="lc-join">
<div><h2>Get one company breakdown a month.</h2><p>What I’d Do is my free newsletter. Each month I study how a technology company markets itself and say what I’d keep, change or try, plus takeaways from a live conversation with a marketing leader. Two emails a month.</p></div>
<div><div class="lc-form wd-bh" data-beehiiv-slot="486dd20f-f759-4e17-a148-6ae63a258dcf" aria-live="polite"><p class="wd-bh-wait">Loading the sign-up form…</p></div>
<p class="lc-fall">Form not showing? <a href="mailto:jeremiah@thejeremiahajayi.com?subject=What%20I%E2%80%99d%20Do%3A%20please%20subscribe%20me">Email me</a> and I’ll add you.</p></div>
</div></div>

<section class="lc-sec" id="help" aria-labelledby="help-h">
<h2 id="help-h">If your launch needs more than a checklist</h2>
<div class="lc-cta">
<div class="lc-card dark"><h3>GTM Readiness Scorecard</h3><p>15 questions on whether your launch is ready to create sales conversations. Free, with an action plan.</p><a href="/resources/gtm-scorecard/" data-track="readiness_scorecard_clicked" data-loc="help">Take the scorecard →</a></div>
<div class="lc-card"><h3>Product launches and GTM</h3><p>I plan and run B2B SaaS launches built for pipeline: the GTM brief, the plan, sales enablement and measurement.</p><a href="/services/product-launch-gtm/" data-track="gtm_service_clicked" data-loc="help">See how I work →</a></div>
<div class="lc-card"><h3>The RemotePass × Certn launch</h3><p>How a partnership launch earned 270+ media pickups, and how sales used it.</p><a href="/work/#certn" data-track="case_study_clicked" data-loc="help">Read the case study →</a></div>
</div>
</section>

<div class="lc-sec lc-faq">
<h2>Questions people ask</h2>
<details><summary>What should a B2B SaaS product launch checklist include?</summary><p>Six stages: defining the launch (the GTM brief, tier, owner and measures), building the message and plan, enabling sales and customer success, launch-week checks, launch day itself, and the weeks after, when follow-up turns interest into sales conversations. Many checklists stop at launch day, which is one reason launches get attention but few conversations.</p></details>
<details><summary>How far in advance should you plan a product launch?</summary><p>As a guide, six to eight weeks for a major launch, three to four weeks for a feature launch, and about a week for a small update. Partner launches and press usually need the most lead time, because other people’s approvals set the pace. If your date is sooner, add it above and the checklist will compress the plan and show which tasks to do first.</p></details>
<details><summary>What is a launch tier?</summary><p>A way of sizing the launch effort to the release. Tier 1 is a new product, a major feature that changes the pitch, a partnership or a new market. Tier 2 is a meaningful feature that solves an established customer problem or helps win deals. Tier 3 is an incremental improvement. Tiering stops teams from overspending on small updates or underselling big ones.</p></details>
<details><summary>Who should own a product launch?</summary><p>One person accountable for the plan and the date, often product marketing, or a founder at an early-stage company. Product owns what ships; sales and customer success own using it with customers. The owner makes sure all three work to one timeline. The checklist suggests an owner for each task, which you can change.</p></details>
<details><summary>How do you measure whether a launch worked?</summary><p>Agree the measures and targets before launch: for example qualified demo requests, opportunities created, sourced and influenced pipeline, sales usage of launch assets and adoption. Review them at 30 days, and again later for results that take longer, such as revenue. Press coverage and social reach are useful signals, but they don’t show on their own whether the launch created sales conversations.</p></details>
<details><summary>Where is my progress saved?</summary><p>In your browser, on this device. Nothing you type is sent to us, and it won’t appear on your other devices. To share the plan with your team, download it as a CSV for Excel or Google Sheets, or print it to PDF.</p></details>
</div>

<div class="lc-by"><img src="/img/headshot.webp" alt="Jeremiah Ajayi" width="64" height="64" loading="lazy" onerror="this.remove()"><p><b>Built by Jeremiah Ajayi</b>, a marketing consultant for B2B SaaS and technology companies. It’s based on the process behind 20+ launches I’ve led, including 15+ at RemotePass and the RemotePass × Certn partnership launch.</p></div>
</div></section>
{brief}
{measure}
{review}
<script type="application/json" id="lc-data">{json.dumps(data, ensure_ascii=False).replace("</", "<\\/")}</script>
<script>{js}</script>
'''
    OUT.write_text(out)
    print('wrote', OUT, len(out), 'counts', counts)


if __name__ == '__main__':
    build()
