"""Source data for the B2B SaaS product launch checklist.

Edit tasks, timings and guidance here, then run:  python3 tools/checklist/build.py
That writes tools/b2b-saas-launch-checklist.html, which export.js wraps in the site shell.

Task fields
  id      stable key used for saved progress (never rename an existing id)
  stage   1-6
  tiers   which launch tiers include the task: "123", "12" or "1"
  owner   suggested owner (one of OWNERS)
  na      True if the task can be marked "Not applicable" (conditional work)
  pri     True if it stays a priority when the plan has to be compressed
  t, d    title and description (Tier 1 and Tier 2 wording)
  t3, d3  lighter Tier 3 wording, where the task applies to Tier 3
  due     optional day offsets from launch day per tier, overriding the stage end
  guide   key into GUIDES for "What good looks like"
"""

OWNERS = ['Product marketing', 'Marketing', 'Product', 'Sales', 'Customer success', 'Design', 'Engineering', 'Leadership', 'Founder']

TIERS = {
    '1': {'name': 'Major launch', 'lead': 56, 'what': 'A new product, a major feature that changes the pitch, a partnership or a new market.', 'time': '6–8 weeks'},
    '2': {'name': 'Feature launch', 'lead': 28, 'what': 'A meaningful feature that solves an established customer problem or helps win deals.', 'time': '3–4 weeks'},
    '3': {'name': 'Small update', 'lead': 7, 'what': 'An incremental improvement for existing users.', 'time': 'About a week'},
}

# Stage windows: (label, start offset, end offset) in days relative to launch day, per tier.
STAGES = [
    {'n': 1, 'h': 'Define the launch', 'h3': 'Define the update',
     'w': {'1': ('8–6 weeks before', -56, -42), '2': ('4–3 weeks before', -28, -21), '3': ('About a week before', -7, -5)}},
    {'n': 2, 'h': 'Build the message and the plan', 'h3': 'Write what changed',
     'w': {'1': ('6–4 weeks before', -42, -28), '2': ('3–2 weeks before', -21, -14), '3': ('3–4 days before', -4, -3)}},
    {'n': 3, 'h': 'Enable sales and customer success', 'h3': 'Prepare help docs',
     'w': {'1': ('3–2 weeks before', -21, -14), '2': ('2 weeks to 1 week before', -14, -7), '3': ('2–3 days before', -3, -2)}},
    {'n': 4, 'h': 'Get ready', 'h3': 'Get ready',
     'w': {'1': ('Launch week', -7, -1), '2': ('Launch week', -5, -1), '3': ('The day before', -1, -1)}},
    {'n': 5, 'h': 'Launch', 'h3': 'Ship it',
     'w': {'1': ('Launch day', 0, 0), '2': ('Launch day', 0, 0), '3': ('Launch day', 0, 0)}},
    {'n': 6, 'h': 'Turn attention into pipeline', 'h3': 'Check how it landed',
     'w': {'1': ('2–30 days after', 2, 30), '2': ('2–30 days after', 2, 30), '3': ('The week after', 1, 7)}},
]

TASKS = [
    # 1. Define
    dict(id='brief', stage=1, tiers='123', owner='Product marketing', pri=True, guide='brief',
         t='Write the GTM brief',
         d='One page on who the release is for, the problem it solves, what buyers use today, and how it changes what sales says.',
         t3='Write a three-line release note brief',
         d3='What changed, who it helps and why it matters. Three lines is enough for a small update.'),
    dict(id='tier', stage=1, tiers='123', owner='Product marketing', pri=True,
         t='Agree the launch tier with product',
         d='Use the tier guide above. Agreeing it early stops a small update from eating a major launch’s budget, and the reverse.',
         t3='Confirm with product that this is a small update',
         d3='If it changes the pitch or affects live deals, it probably deserves Tier 2.'),
    dict(id='owner', stage=1, tiers='123', owner='Leadership', pri=True,
         t='Name one owner and a launch date',
         d='One person accountable for the launch, and a date product has committed to, not a hope.',
         t3='Name an owner and a ship date',
         d3='Someone who will make sure the release note, help doc and in-app message go out together.'),
    dict(id='measures', stage=1, tiers='12', owner='Product marketing', pri=True, guide='measures',
         t='Agree how you’ll measure it, before launch',
         d='Pick three to five measures, such as qualified demo requests, opportunities, pipeline, sales usage of assets and adoption. Write down the baseline and a target for each.'),
    dict(id='research', stage=1, tiers='1', owner='Product marketing', guide='research',
         t='Talk to 3–5 customers and 2–3 sales reps',
         d='Ask about the problem the release solves and the objections reps hear. Their words are often better messaging than anything written in a meeting.'),
    dict(id='position', stage=1, tiers='12', owner='Product marketing', pri=True, guide='position',
         t='Check the positioning',
         d='Can you say in one sentence why a buyer would choose this over their current alternative, including doing nothing?'),
    dict(id='partner', stage=1, tiers='1', owner='Marketing', na=True, pri=True,
         t='For partner launches: agree the story, timing and approvals',
         d='Settle whose story it is, who announces first and who signs off, with the partner’s marketing team, in writing. Mark this not applicable if there’s no partner.'),
    # 2. Message and plan
    dict(id='msg', stage=2, tiers='123', owner='Product marketing', pri=True, guide='msg',
         t='Write the launch messaging',
         d='A headline, three proof points and one customer use case. Every asset borrows from this, so everything says the same thing.',
         t3='Write one sentence on what changed and why it matters',
         d3='Use it in the changelog, the help doc and the in-app message so they all match.'),
    dict(id='calendar', stage=2, tiers='12', owner='Product marketing', guide='calendar',
         t='Build the launch calendar',
         d='Every asset, channel, owner and due date in one place, working back from launch day. The action plan export below is a good starting point.'),
    dict(id='design', stage=2, tiers='12', owner='Design', na=True,
         t='Brief design and video',
         d='Launch visuals, product screenshots and a short demo. Buyers usually want to see it working before they ask for a call.'),
    dict(id='page', stage=2, tiers='12', owner='Marketing', na=True, pri=True,
         t='Draft the landing page, or update the product page',
         d='Check whether pricing, comparison and integration pages also need changes.'),
    dict(id='press', stage=2, tiers='1', owner='Marketing', na=True,
         t='Plan press',
         d='The release, target outlets and journalists, an embargo date, and regional versions where the market needs them, such as Arabic for the Middle East. Not every major launch needs press.'),
    dict(id='accounts', stage=2, tiers='12', owner='Sales', pri=True,
         t='List the customers and open deals this release helps',
         d='These are your first sales conversations. Share the list with sales and customer success.'),
    dict(id='search', stage=2, tiers='12', owner='Marketing', na=True,
         t='Plan for search and AI answers',
         d='What will buyers search for, or ask ChatGPT, when they need this? Make sure a page answers it clearly.'),
    # 3. Enable
    dict(id='kit', stage=3, tiers='12', owner='Product marketing', pri=True, guide='kit',
         t='Build the sales enablement kit',
         d='A deck slide, a one-pager, an FAQ and a short talk track. Keep it to what a rep will use on a call.'),
    dict(id='battlecards', stage=3, tiers='12', owner='Product marketing', na=True,
         t='Update battlecards',
         d='If the release changes how you answer “why not the competitor?”, update the battlecard before reps need it.'),
    dict(id='training', stage=3, tiers='12', owner='Product marketing',
         t='Run a 30-minute training and record it',
         d='Sales and customer success should hear about the launch before customers do.'),
    dict(id='docs', stage=3, tiers='123', owner='Customer success', pri=True,
         t='Get help docs and in-product messages ready',
         d='Telling users inside the product, where they already are, is often the quickest route to adoption.',
         t3='Update the help doc and write the in-app message',
         d3='Keep the in-app message to one or two lines and link to the help doc.'),
    dict(id='tracking', stage=3, tiers='12', owner='Marketing', pri=True, guide='tracking',
         t='Set up tracking',
         d='UTM links, a campaign in your CRM and conversion events on the landing page, so engagement and pipeline can be traced back to the launch.'),
    # 4. Get ready
    dict(id='qa', stage=4, tiers='123', owner='Product', pri=True,
         t='Check everything works',
         d='The feature is live for the right users, and every link, form and tracking event works.',
         t3='Check it works for the right users',
         d3='Including any links in the release note and in-app message.'),
    dict(id='brief-teams', stage=4, tiers='123', owner='Product marketing', pri=True,
         t='Confirm the date and time with every team',
         d='Leadership, sales, support and any partners know exactly when it goes out.',
         t3='Tell support and sales it’s shipping',
         d3='A short message with what changed and a link to the help doc.'),
    dict(id='social', stage=4, tiers='12', owner='Founder', na=True, guide='social',
         t='Prepare posts for founders and the team',
         d='Posts from people often reach further than the company page, especially on LinkedIn. Draft them now so they’re ready on the day.'),
    dict(id='embargo', stage=4, tiers='1', owner='Marketing', na=True,
         t='Send the press release under embargo',
         d='Give journalists time to write, and confirm what they can publish and when.'),
    # 5. Launch
    dict(id='publish', stage=5, tiers='123', owner='Marketing', pri=True,
         t='Publish across your channels',
         d='The announcement, an email to customers and prospects, the landing page, social and in-app messages, scaled to the tier.',
         t3='Publish the changelog, help doc and in-app message',
         d3='Then mention it in your next customer email rather than sending one just for this.'),
    dict(id='press-live', stage=5, tiers='1', owner='Marketing', na=True,
         t='Go live with press and partners',
         d='The press release, partner posts and any co-marketing, at the agreed time.'),
    dict(id='sales-note', stage=5, tiers='12', owner='Product marketing', pri=True,
         t='Send sales a “use this today” note',
         d='Which accounts to contact, what to say and which asset to send. This is where attention starts turning into conversations.'),
    dict(id='watch', stage=5, tiers='12', owner='Sales',
         t='Watch the first signals',
         d='Replies, demo requests, sign-ups and questions coming into sales and support. Fix anything confusing the same day.'),
    # 6. After
    dict(id='followup', stage=6, tiers='12', owner='Sales', pri=True, guide='followup', due={'1': 3, '2': 3},
         t='Follow up with everyone who engaged',
         d='People who clicked, visited pricing or watched the demo. Timely, specific follow-up is often what turns early interest into a sales conversation.'),
    dict(id='stories', stage=6, tiers='12', owner='Customer success', na=True, due={'1': 21, '2': 21},
         t='Collect the first customer stories',
         d='A quote or a result from an early user is strong proof for the next round of content and sales conversations.'),
    dict(id='usage', stage=6, tiers='12', owner='Product marketing', due={'1': 14, '2': 14},
         t='Check which assets sales actually used',
         d='Ask reps. Unused assets can point to unclear messaging, too little training, assets that are hard to find, or a poor fit with real sales conversations.'),
    dict(id='report', stage=6, tiers='12', owner='Product marketing', pri=True, guide='report', due={'1': 30, '2': 30},
         t='Report against your measures at 30 days',
         d='Compare engagement, opportunities, pipeline, adoption and sales usage against the targets from step 1. Note which results need 60–90 days to read properly.'),
    dict(id='keep', stage=6, tiers='12', owner='Marketing', na=True, due={'1': 21, '2': 21},
         t='Keep it going',
         d='Plan two or three follow-up pieces: a use case, a customer story, a how-to. Most buyers won’t have seen launch day.'),
    dict(id='retro', stage=6, tiers='123', owner='Product marketing', pri=True, guide='retro', due={'1': 30, '2': 30, '3': 7},
         t='Run a short retro and update your playbook',
         d='What to repeat, what to drop and what to do earlier next time.',
         t3='Note how it landed',
         d3='Usage, support questions and anything users said. Two lines in your launch log is enough.'),
]

# "What good looks like" guidance. Each: produce, structure (list), example (optional), mistake, template (optional).
GUIDES = {
    'brief': dict(
        produce='One page that product, marketing and sales all agree with before anyone writes an asset. If people disagree on it, they will disagree on everything after it.',
        structure=['What we’re launching, in one sentence', 'Who it’s for, and who signs off on buying it', 'The problem, in the customer’s words', 'What they use today, including doing nothing', 'Why ours is different, and the proof', 'What we want the launch to achieve, and how we’ll measure it', 'Owner, date, dependencies and risks'],
        mistake='Writing a feature spec. A brief explains why a buyer should care; the spec explains how it works.',
        template='brief'),
    'position': dict(
        produce='One sentence your whole team could repeat, plus a clear view of what you’re being compared with.',
        structure=['For [target customer] who [problem],', '[product] is the [category] that [key benefit].', 'Unlike [current alternative], it [main difference].'],
        example='For finance teams at multi-entity companies who approve spend in spreadsheets, Fernway (a fictional company) is the spend management platform that routes every request to the right approver. Unlike email and spreadsheets, it keeps a full audit trail.',
        mistake='Positioning against a competitor buyers aren’t considering. Often the real alternative is a spreadsheet, an agency or doing nothing.'),
    'research': dict(
        produce='Short notes from 3–5 customer and 2–3 sales conversations, with the exact phrases people used.',
        structure=['Customers: “Walk me through the last time this problem came up.”', 'Customers: “What did you do about it? What did that cost you?”', 'Reps: “Where do deals stall when this comes up?”', 'Reps: “What do buyers compare us with?”'],
        mistake='Pitching the feature during the interview. You’ll hear polite agreement instead of how people actually describe the problem.'),
    'measures': dict(
        produce='Three to five measures with a baseline and a target, agreed before launch so the results can’t be reinterpreted afterwards.',
        structure=['Choose measures that match the launch’s goal, not every metric you can track', 'Record the baseline: what does a normal month look like?', 'Set a realistic target and a date to check it', 'Say where each number will come from: CRM, product analytics, the sales team'],
        mistake='Measuring only reach: impressions, likes and press mentions. They’re useful signals, but they don’t tell you whether the launch created sales conversations.',
        template='measure'),
    'msg': dict(
        produce='A short messaging block that every asset borrows from.',
        structure=['Headline: the outcome for the buyer, not the feature name', 'Three proof points, each backed by evidence: a number, a customer or a demo', 'One use case: a specific customer, situation and result'],
        example='Headline: “Approve spend across every entity in one place.” Proof: approvals routed by entity and amount; full audit trail for auditors; set up in a day with existing ERP data. (Fernway, a fictional company.)',
        mistake='Proof points that are really features with nothing behind them. If you can’t show it, a buyer is unlikely to believe it.'),
    'calendar': dict(
        produce='One shared list of every launch task, with an owner and a due date, working back from launch day.',
        structure=['Columns: task, channel, owner, due date, status, depends on', 'Start from launch day and work backwards', 'Add time for approvals: legal, partners, leadership'],
        mistake='No room for approvals. Partner and legal sign-off are where launch dates usually slip.'),
    'kit': dict(
        produce='The few things a rep needs to use the launch on a live call this week.',
        structure=['One deck slide: the problem, what’s new, the proof', 'A one-page summary they can send after a call', 'FAQ: the five questions and objections you expect, with answers', 'A three-sentence talk track', 'Which accounts to contact first'],
        mistake='A 20-slide deck nobody opens. If it isn’t short enough to use on a call, it probably won’t be used.'),
    'tracking': dict(
        produce='Tracking in place before launch, so you can see what the launch did after it.',
        structure=['UTM links for every channel, with one naming pattern (for example utm_campaign=launch-approvals-2027q1)', 'A launch campaign in your CRM that new and influenced opportunities can be tied to', 'Conversion events on the landing page and demo form', 'A “How did you hear about us?” field, since some buyers will come from posts and conversations that tracking can’t see'],
        mistake='Setting up tracking after launch. The first days are often when interest is highest, and that data can’t be recovered.'),
    'social': dict(
        produce='Drafts for the founder and three to five team members, written in each person’s own voice.',
        structure=['Start with the problem or a moment from a customer conversation', 'What changed, and who it’s for', 'One piece of proof', 'A soft next step: a link, a demo or “reply if this is you”'],
        mistake='Everyone posting the same company text. Identical posts read like an ad and tend to get less reach than personal ones.'),
    'followup': dict(
        produce='A short follow-up plan by signal, so interested people hear from you while the launch is fresh.',
        structure=['Visited pricing or the demo page: personal email from sales within 48 hours', 'Watched the demo or replied: offer a call', 'Existing customers who could use it: customer success shows them', 'Everyone else: add them to your next email or content piece'],
        mistake='A generic “Did you see our launch?” email. Mention what they looked at and why it might matter to them.'),
    'report': dict(
        produce='A one-page report against the targets you set before launch, separating what you can know now from what needs more time.',
        structure=['At 30 days: engagement, demo requests, opportunities created, sales usage of assets, early adoption', 'At 60–90 days or later: pipeline progression, revenue, retention and sustained adoption', 'For each measure: target, actual, and what you’ll do about the gap'],
        mistake='Calling the launch a success or failure on revenue at 30 days. In B2B, and especially enterprise sales, many deals take longer than that to close.',
        template='measure'),
    'retro': dict(
        produce='A 30-minute review with everyone who worked on the launch, ending with named owners and dates.',
        structure=['What worked, and why do we think so?', 'What underperformed, and what does the evidence say?', 'What will we do differently next time, who owns it and by when?'],
        mistake='A retro that ends with observations and no owners. Write the changes into your launch playbook so the next launch is easier.',
        template='review'),
}
