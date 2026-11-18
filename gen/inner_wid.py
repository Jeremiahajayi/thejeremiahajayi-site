"""What I'd Do: a newsletter + live conversation series, as a section of the site.

Identity: a decision under examination. Newsprint and ink, the site's orange as an
editor's red pen, a serif italic for margin notes. Emphasis comes from red-pen
underlines, circled options and margin notes, never a highlighter.
Content and integration settings live in pages/what-id-do.js.
"""

B = lambda i: '/_blob/' + i
HEADSHOT = 'ab01351679f0c21d14aae4bf06f3affa'

CSS = r'''
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400;1,6..72,500&display=swap">
<style>
.wd{--paper:#F4F0E6;--ink:#141414;--pen:#C23A0E;--orange:#FF5A2A;--rule:rgba(20,20,20,.18);background:var(--paper);color:var(--ink)}
.wd-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.wd ::selection{background:#141414;color:#F4F0E6}
.wd .wrap{max-width:1240px}
.wd-serif{font-family:'Newsreader',Georgia,'Times New Roman',serif}
.wd-note{font:italic 500 17px/1.35 'Newsreader',Georgia,serif;color:var(--pen)}
.wd-kick{margin:0;font:700 12px/1.4 'DM Sans',system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase}
.wd-rule{border:0;border-top:1.5px solid var(--ink);margin:0}
.wd-link{display:inline-flex;align-items:center;gap:8px;color:inherit;font-weight:700;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px;text-decoration-color:var(--orange);transition:text-decoration-color .25s,gap .25s}
.wd-link:hover{color:inherit;gap:12px;text-decoration-color:currentColor}
.wd-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:56px;padding:0 26px;border-radius:999px;background:var(--ink);color:var(--paper);font-weight:700;font-size:16px;text-decoration:none;box-shadow:3px 3px 0 var(--orange);transition:transform .2s,box-shadow .2s}
.wd-btn:hover{color:var(--paper);transform:translate(-2px,-2px);box-shadow:5px 5px 0 var(--orange)}
.wd-btn-o{background:var(--orange);color:#111;box-shadow:3px 3px 0 #111}
.wd-btn-o:hover{color:#111;box-shadow:5px 5px 0 #111}
.wd-dot{color:var(--orange)}
/* red-pen marks: drawn, not highlighted */
.wd-ul{position:relative;white-space:nowrap}
.wd-ul svg{position:absolute;left:-2%;bottom:-.22em;width:104%;height:.36em;overflow:visible;pointer-events:none}
.wd-ul path{fill:none;stroke:var(--orange);stroke-width:3.2;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;animation:wdpen 1.1s .5s cubic-bezier(.6,0,.2,1) forwards}
.wd-circ{position:relative;display:inline-block}
.wd-circ svg{position:absolute;left:-14%;top:-22%;width:128%;height:144%;overflow:visible;pointer-events:none}
.wd-circ path{fill:none;stroke:var(--orange);stroke-width:2.6;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1}
.wd-circ.inked path,.wd-call.inked .wd-circ path{animation:wdpen 1.2s .2s cubic-bezier(.6,0,.2,1) forwards}
@keyframes wdpen{to{stroke-dashoffset:0}}
/* ── masthead / hero ── */
.wd-hero .wrap{position:relative}
.wd-hero{position:relative;padding:clamp(26px,3vw,40px) 0 clamp(72px,8vw,112px);overflow:hidden}
.wd-mast{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:8px 24px;padding:12px 0;border-top:1.5px solid var(--ink);border-bottom:1px solid var(--ink);box-shadow:0 4px 0 -3px var(--ink)}
.wd-mast span:last-child{font:italic 400 16px 'Newsreader',Georgia,serif;letter-spacing:0;text-transform:none}
.wd-word{position:relative;margin:clamp(28px,4vw,56px) 0 0;font:700 clamp(68px,13.6vw,210px)/.86 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.065em;white-space:nowrap}
.wd-i{position:relative;display:inline-block;padding:0 .08em;margin:0 .02em;border:.045em solid var(--ink);border-radius:.06em;line-height:.9;transform:rotate(-2deg)}
.wd-who{position:absolute;left:50%;top:100%;margin-top:.32em;transform:translateX(-50%) rotate(2deg);white-space:nowrap;font:italic 500 clamp(14px,1.25vw,19px)/1 'Newsreader',Georgia,serif;letter-spacing:0;color:var(--pen)}
.wd-who b{font-weight:500;display:inline-block;transition:opacity .35s,transform .35s}
.wd-who b.out{opacity:0;transform:translateY(6px)}
.wd-note-i{position:relative;margin:clamp(30px,3vw,44px) 0 0 auto;max-width:300px;text-align:left;padding-left:96px}
.wd-note-i svg{position:absolute;left:0;top:-14px;width:84px;height:52px;color:var(--pen)}
.wd-hero-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(32px,5vw,80px);margin-top:clamp(32px,4vw,56px);align-items:start}
.wd-sub{margin:0;font:400 clamp(28px,3vw,46px)/1.12 'Newsreader',Georgia,serif;letter-spacing:-.01em;max-width:20ch}
.wd-sub em{font-style:italic}
.wd-body{margin-top:28px;max-width:58ch}
.wd-body p{margin:0 0 16px;font-size:18px;line-height:1.7}
.wd-body .wd-q{font:italic 500 26px/1.3 'Newsreader',Georgia,serif;margin:22px 0}
.wd-hero-cta{margin-top:30px;display:flex;flex-wrap:wrap;align-items:center;gap:14px 26px}
/* subscribe slip */
.wd-slip{position:relative;padding:28px 26px 26px;background:#FFFDF8;border:1.5px solid var(--ink);box-shadow:6px 6px 0 var(--ink)}
.wd-slip::before{content:"";position:absolute;left:50%;top:-14px;width:84px;height:26px;transform:translateX(-50%) rotate(-3deg);background:rgba(255,90,42,.28);border:1px solid rgba(255,90,42,.35)}
.wd-slip h2,.wd-slip h3{margin:6px 0 10px;font:700 26px/1.1 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.03em}
.wd-slip p{margin:0;font-size:15.5px;line-height:1.6}
.wd-slip iframe{display:block;width:100%;min-height:140px;margin-top:16px;border:0;background:transparent}
.wd-slip-meta{margin-top:14px;padding-top:12px;border-top:1px dashed var(--rule);font-size:13.5px;color:#4A4741}
.wd-soon{margin-top:16px;padding:14px 16px;border:1.5px dashed var(--pen);font-size:15px;line-height:1.55}
.wd-soon b{color:var(--pen)}
.wd-soon .wd-link{margin-top:8px}
/* ── premise: the case file ── */
.wd-sec{position:relative;padding:clamp(80px,9vw,132px) 0}
.wd-h2{margin:0;font:700 clamp(40px,5vw,80px)/.98 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.055em;max-width:16ch}
.wd-premise-g{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(36px,5vw,88px);align-items:start}
.wd-premise-g .wd-body{margin-top:26px}
.wd-file{position:relative;background:#FFFDF8;border:1.5px solid var(--ink);padding:clamp(24px,3vw,40px);box-shadow:8px 8px 0 rgba(20,20,20,.12)}
.wd-file::before{content:"";position:absolute;left:clamp(56px,6vw,76px);top:0;bottom:0;border-left:1.5px solid rgba(255,90,42,.45)}
.wd-tab{position:absolute;left:-1.5px;top:-34px;padding:7px 16px 8px;background:#FFFDF8;border:1.5px solid var(--ink);border-bottom:0;font:700 12px 'DM Sans',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.wd-stamp{position:absolute;right:clamp(18px,3vw,34px);top:clamp(16px,2.4vw,28px);padding:6px 12px;border:2px solid var(--pen);color:var(--pen);font:700 12px 'DM Sans',system-ui,sans-serif;letter-spacing:.16em;text-transform:uppercase;transform:rotate(6deg);opacity:.9}
.wd-file-in{padding-left:clamp(40px,4.4vw,56px)}
.wd-situ{margin:0;font:400 clamp(21px,1.9vw,27px)/1.42 'Newsreader',Georgia,serif;max-width:40ch;padding-right:90px}
.wd-situ b{font-weight:600}
.wd-opts{margin-top:28px;border-top:1px solid var(--rule)}
.wd-opt{border-bottom:1px solid var(--rule)}
.wd-opt summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:16px;align-items:center;padding:20px 0;font:700 clamp(18px,1.6vw,22px)/1.3 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em}
.wd-opt summary::-webkit-details-marker{display:none}
.wd-opt summary:focus-visible{outline:3px solid var(--orange);outline-offset:4px}
.wd-letter{position:relative;display:grid;place-items:center;width:40px;height:40px;font:600 italic 24px 'Newsreader',Georgia,serif}
.wd-letter svg{position:absolute;inset:-6px;width:52px;height:52px;overflow:visible}
.wd-letter path{fill:none;stroke:var(--orange);stroke-width:2.6;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset .7s cubic-bezier(.6,0,.2,1)}
.wd-opt[open] .wd-letter path,.wd-opt summary:hover .wd-letter path{stroke-dashoffset:0}
.wd-opt summary i{font:italic 400 15px 'Newsreader',Georgia,serif;color:var(--pen);white-space:nowrap}
.wd-opt[open] summary i{color:transparent;position:relative}
.wd-opt[open] summary i::after{content:"close";position:absolute;right:0;color:var(--pen)}
.wd-why{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;padding:0 0 24px 60px}
.wd-why div{font-size:15.5px;line-height:1.6}
.wd-why b{display:block;margin-bottom:4px;font:700 11.5px 'DM Sans',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#4A4741}
.wd-opt[open] .wd-why{animation:wdin .45s cubic-bezier(.2,.8,.2,1)}
@keyframes wdin{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.wd-verdict{margin:24px 0 0;font:italic 400 19px/1.5 'Newsreader',Georgia,serif;max-width:52ch}
.wd-verdict b{font-style:normal;font-family:'Space Grotesk',system-ui,sans-serif;font-weight:700;letter-spacing:-.01em}
/* ── two ways: a spread ── */
.wd-spread{display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid var(--ink);border-bottom:1.5px solid var(--ink)}
.wd-page{position:relative;padding:clamp(40px,5vw,76px) clamp(24px,4vw,64px) clamp(44px,5vw,72px)}
.wd-page+.wd-page{border-left:1.5px solid var(--ink)}
.wd-page.dark{background:var(--ink);color:var(--paper)}
.wd-num{display:block;font:italic 400 clamp(88px,10vw,150px)/.8 'Newsreader',Georgia,serif;color:var(--orange);margin-bottom:22px}
.wd-page h3{margin:0 0 6px;font:700 clamp(34px,3.6vw,56px)/1 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.05em}
.wd-page .wd-kick{margin-bottom:16px;opacity:.75}
.wd-page p{margin:16px 0 0;font-size:17.5px;line-height:1.7;max-width:46ch}
.wd-sched{display:flex;flex-wrap:wrap;gap:8px 18px;margin:26px 0 30px;padding:14px 0;border-top:1px solid currentColor;border-bottom:1px solid currentColor;font:600 14.5px/1.4 'DM Sans',system-ui,sans-serif}
.wd-page.dark .wd-sched{border-color:rgba(244,240,230,.35)}
.wd-page.dark .wd-link{color:var(--paper)}
/* ── featured event ── */
.wd-event{background:var(--ink);color:var(--paper);overflow:hidden}
.wd-event .wd-kick{color:var(--orange)}
.wd-ev-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(36px,5vw,88px);align-items:end;margin-top:26px}
.wd-ev-t{margin:0;font:700 clamp(40px,5.4vw,88px)/.98 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.055em;max-width:15ch}
.wd-ev-t span{display:block;font:italic 400 .62em/1.1 'Newsreader',Georgia,serif;letter-spacing:-.01em;color:#D9D4CA;margin-top:.25em}
.wd-guest{display:flex;align-items:center;gap:16px;margin:30px 0 0;font-size:16px}
.wd-guest b{display:block;font:700 22px 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.02em}
.wd-guest span{color:#B5B0A6}
.wd-ev-d{margin:26px 0 0;max-width:56ch;font-size:17.5px;line-height:1.7;color:#D9D4CA}
.wd-ev-d+.wd-ev-d{margin-top:14px}
.wd-port{position:relative;margin:0}
.wd-port-f{position:relative;aspect-ratio:4/5;background:#232220;border:1.5px solid #3A3934;display:grid;place-items:center;overflow:hidden}
.wd-port-f img{width:100%;height:100%;object-fit:cover}
.wd-mono{font:italic 400 clamp(96px,11vw,170px)/1 'Newsreader',Georgia,serif;color:#3F3D38;letter-spacing:-.04em}
.wd-port figcaption{margin-top:10px;font:italic 400 15px 'Newsreader',Georgia,serif;color:#B5B0A6}
.wd-tba{position:absolute;right:-14px;top:22px;padding:10px 16px;border:2px solid var(--orange);color:var(--orange);background:var(--ink);font:700 13px 'DM Sans',system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;transform:rotate(7deg)}
.wd-ev-cta{margin-top:34px;display:flex;flex-wrap:wrap;align-items:center;gap:14px 24px}
.wd-ev-cta .wd-link{color:var(--paper)}
.wd-cal{margin-top:clamp(56px,7vw,96px);padding-top:28px;border-top:1px solid #3A3934}
.wd-cal iframe{display:block;width:100%;height:520px;border:1.5px solid #3A3934;border-radius:8px;background:#fff}
.wd-cal-empty{display:grid;grid-template-columns:auto 1fr;gap:16px 28px;align-items:center;margin-top:18px}
.wd-cal-empty p{margin:0;font:italic 400 20px/1.45 'Newsreader',Georgia,serif;color:#D9D4CA;max-width:52ch}
.wd-cal-empty .wd-blank{display:flex;gap:8px}
.wd-cal-empty .wd-blank i{width:44px;height:52px;border:1.5px dashed #5A5852;border-radius:4px}
/* ── how it works: a marked-up page ── */
.wd-how-head{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:20px 64px;align-items:end;margin-bottom:clamp(36px,4vw,56px)}
.wd-steps{margin:0;padding:0;list-style:none;border-top:1.5px solid var(--ink)}
.wd-step{display:grid;grid-template-columns:110px minmax(0,5fr) minmax(0,5fr) minmax(0,3fr);gap:20px 36px;align-items:baseline;padding:clamp(26px,3vw,40px) 0;border-bottom:1px solid var(--rule)}
.wd-step-n{font:italic 400 44px/1 'Newsreader',Georgia,serif;color:var(--pen)}
.wd-step h3{margin:0;font:700 clamp(34px,3.8vw,60px)/.95 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.05em}
.wd-step p{margin:0;font-size:17.5px;line-height:1.65}
.wd-step .wd-note{font-size:16px}
.wd-call h3{color:var(--ink)}
/* ── the decision files ── */
.wd-files{border-top:1.5px solid var(--ink)}
.wd-fr{display:grid;grid-template-columns:180px minmax(0,1fr) 180px;gap:8px 40px;padding:26px 0;border-bottom:1px solid var(--rule);color:inherit;text-decoration:none}
.wd-fr:hover .wd-fr-t{color:var(--pen)}
.wd-fr-c{font:700 12px/1.6 'DM Sans',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.wd-fr-t{display:block;font:700 clamp(22px,2vw,28px)/1.15 'Space Grotesk',system-ui,sans-serif;letter-spacing:-.025em;transition:color .2s}
.wd-fr-d{display:block;margin-top:8px;font-size:16px;line-height:1.6;max-width:62ch}
.wd-fr-m{font-size:14px;line-height:1.6;color:#4A4741;text-align:right}
.wd-drawer{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(32px,5vw,80px);align-items:center;padding:clamp(36px,4vw,56px) 0;border-bottom:1px solid var(--rule)}
.wd-tabs{position:relative;height:220px}
.wd-tabs span{position:absolute;left:0;right:0;height:150px;border:1.5px solid var(--ink);background:#FFFDF8;box-shadow:0 -1px 0 rgba(20,20,20,.04)}
.wd-tabs span::before{content:attr(data-l);position:absolute;top:-30px;left:var(--tx);padding:5px 14px;background:#FFFDF8;border:1.5px solid var(--ink);border-bottom:0;font:700 11.5px 'DM Sans',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.wd-tabs span:nth-child(1){top:20px;--tx:0%;opacity:.55}
.wd-tabs span:nth-child(2){top:46px;--tx:34%;opacity:.8}
.wd-tabs span:nth-child(3){top:72px;--tx:66%}
.wd-tabs em{position:absolute;right:16px;bottom:30px;z-index:2;padding:6px 12px;border:2px solid var(--pen);color:var(--pen);font:700 12px 'DM Sans',system-ui,sans-serif;font-style:normal;letter-spacing:.14em;text-transform:uppercase;transform:rotate(-6deg)}
.wd-drawer p{margin:0 0 14px;font:400 clamp(22px,2vw,28px)/1.4 'Newsreader',Georgia,serif;max-width:34ch}
/* ── submit a problem ── */
.wd-sub-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(36px,5vw,88px);align-items:start}
.wd-quote{margin:0;font:400 clamp(40px,5.2vw,82px)/1.02 'Newsreader',Georgia,serif;letter-spacing:-.02em;max-width:15ch}
.wd-quote em{font-style:italic}
.wd-card{position:relative;padding:30px 28px;background:#FFFDF8;border:1.5px solid var(--ink);box-shadow:6px 6px 0 var(--orange);transform:rotate(1.2deg)}
.wd-card ol{margin:16px 0 22px;padding:0;list-style:none;counter-reset:c}
.wd-card li{counter-increment:c;display:grid;grid-template-columns:30px 1fr;padding:12px 0;border-bottom:1px solid var(--rule);font-size:16px;line-height:1.5}
.wd-card li::before{content:counter(c);font:italic 500 18px 'Newsreader',Georgia,serif;color:var(--pen)}
.wd-card small{display:block;margin-top:14px;font-size:13.5px;line-height:1.5;color:#4A4741}
/* ── host ── */
.wd-host-g{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:clamp(36px,5vw,88px);align-items:center}
.wd-host-ph{position:relative;margin:0}
.wd-host-ph img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:center 18%;border:1.5px solid var(--ink);filter:grayscale(.15) contrast(1.02)}
.wd-host-ph figcaption{margin-top:10px}
.wd-host-ph::after{content:"";position:absolute;left:-14px;top:-14px;right:14px;bottom:44px;border:1.5px solid var(--orange);z-index:-1}
.wd-host p{margin:18px 0 0;font-size:18px;line-height:1.7;max-width:56ch}
/* ── final ── */
.wd-final{background:var(--ink);color:var(--paper);text-align:center}
.wd-final .wd-h2{margin:0 auto;max-width:14ch;font-size:clamp(46px,6.4vw,104px)}
.wd-final p.wd-lead{margin:24px auto 0;max-width:46ch;font:italic 400 22px/1.45 'Newsreader',Georgia,serif;color:#D9D4CA}
.wd-final .wd-slip{max-width:520px;margin:44px auto 0;text-align:left;color:var(--ink);box-shadow:6px 6px 0 var(--orange)}
.wd-micro{margin:20px 0 0;font:600 13px 'DM Sans',system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#B5B0A6}
.wd-back{display:flex;flex-wrap:wrap;justify-content:center;gap:12px 28px;margin-top:56px;padding-top:24px;border-top:1px solid #3A3934;font-size:15px}
.wd-back a{color:#D9D4CA}
/* ── responsive ── */
@media (max-width:1080px){
.wd-hero-g,.wd-premise-g,.wd-ev-g,.wd-how-head,.wd-sub-g,.wd-host-g,.wd-drawer{grid-template-columns:1fr}
.wd-note-i{margin-top:52px;padding-left:0;max-width:34ch}
.wd-note-i svg{display:none}
.wd-step{grid-template-columns:80px minmax(0,1fr);}
.wd-step p,.wd-step .wd-note{grid-column:2}
.wd-port{max-width:420px}
.wd-host-ph{max-width:360px}
}
@media (max-width:760px){
.wd-spread{grid-template-columns:1fr}
.wd-page+.wd-page{border-left:0;border-top:1.5px solid var(--ink)}
.wd-why{grid-template-columns:1fr;padding-left:0}
.wd-fr{grid-template-columns:1fr}
.wd-fr-m{text-align:left}
}
@media (max-width:640px){
.wd .wrap{padding-left:24px;padding-right:24px}
.wd-word{font-size:clamp(54px,17.4vw,80px)}
.wd-mast{font-size:11px}
.wd-sub{font-size:30px}
.wd-body p{font-size:17px}
.wd-situ{padding-right:0;padding-top:40px}
.wd-file::before{display:none}
.wd-file-in{padding-left:0}
.wd-opt summary{grid-template-columns:40px minmax(0,1fr);gap:12px}
.wd-opt summary i{display:none}
.wd-step{grid-template-columns:1fr;gap:12px}
.wd-step p,.wd-step .wd-note{grid-column:auto}
.wd-tba{right:8px}
.wd-cal-empty{grid-template-columns:1fr}
.wd-slip{padding:26px 22px 22px}
.wd-page{padding:48px 24px 52px}
.wd-sec{padding:88px 0}
.wd-card{transform:none}
}
@media (prefers-reduced-motion:reduce){
.wd-ul path,.wd-circ path{animation:none !important;stroke-dashoffset:0}
.wd-letter path{transition:none}
.wd-who b{transition:none}
.wd-opt[open] .wd-why{animation:none}
}
</style>'''

PEN_UL = '<svg viewBox="0 0 200 12" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M2 8 C 50 3, 120 10, 198 4"/></svg>'
PEN_CIRC = '<svg viewBox="0 0 200 100" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M150 12 C 110 -2, 30 4, 10 40 C -6 72, 60 98, 120 92 C 176 86, 204 56, 186 30 C 176 16, 150 8, 128 10"/></svg>'
LET_CIRC = '<svg viewBox="0 0 52 52" aria-hidden="true"><path pathLength="1" d="M38 6 C 22 -2, 2 10, 4 28 C 6 46, 30 52, 44 40 C 54 30, 50 12, 34 8"/></svg>'


def subscribe_slip(title, h='h2', uid='a'):
    return f'''<div class="wd-slip" id="subscribe{'' if uid == 'a' else '-' + uid}">
<p class="wd-kick">Free · twice a month</p>
<{h} class="wd-slip-h">{title}</{h}>
<p>Real marketing problems, the options on the table, and the reasoning behind a call. In your inbox on the first and third Wednesday.</p>
<sc-if value="{{{{hasSub}}}}" hint-placeholder-val="{{{{ false }}}}"><iframe src="{{{{cfg.beehiivEmbedUrl}}}}" data-test-id="beehiiv-embed" title="Subscribe to What I’d Do" loading="lazy" frameborder="0" scrolling="no"></iframe></sc-if>
<sc-if value="{{{{noSub}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="wd-soon" role="note"><b>Subscriptions open with the first issue.</b> Until the sign-up form is live, send a one-line email and you’ll be added when it opens.<br><a class="wd-link" href="{{{{notifyMail}}}}">Email me to be added <span aria-hidden="true">↗</span></a></div></sc-if>
<p class="wd-slip-meta">Newsletter only. Live sessions have their own registration, so you choose each one separately.</p>
</div>'''


def page():
    opts = [
        ('A', 'Rewrite the message', 'The people paying attention may be the right buyers who don’t yet see why it matters to them.', 'A new story needs new pages, new sales talk and time to test. The launch window closes while you rewrite.', 'Sales calls show buyers understood the pitch and still said no.'),
        ('B', 'Change who you’re talking to', 'Attention came from people who like the idea but will never buy it. Moving spend to the actual buyer fixes the input.', 'Smaller reach and quieter metrics for a while, which can look like failure to the rest of the company.', 'The few real buyers who saw the launch didn’t respond either.'),
        ('C', 'Fix the hand-off to sales', 'Interest may be real but going nowhere: no follow-up, no sales material, no clear next step.', 'Marketing gives up some credit and spends a month on unglamorous process work instead of new campaigns.', 'Sales already followed up quickly with good material, and nobody converted.'),
    ]
    opt_html = ''.join(
        f'<details class="wd-opt" name="wd-dilemma"><summary><span class="wd-letter" aria-hidden="true">{l}{LET_CIRC}</span><span><span class="wd-sr">Option {l}: </span>{t}</span><i>see the reasoning</i></summary>'
        f'<div class="wd-why"><div><b>Why you might</b>{why}</div><div><b>What it costs</b>{cost}</div><div><b>Wrong call if</b>{wrong}</div></div></details>'
        for l, t, why, cost, wrong in opts
    )
    steps = [
        ('i.', 'The Situation', 'Understand the problem and the constraints: the market, the team, the money and the clock.', 'What do we actually know?', ''),
        ('ii.', 'The Options', 'Lay out the real alternatives, including the unpopular one and doing nothing.', 'What else could work?', ''),
        ('iii.', 'The Call', 'Make the decision and explain the reasoning: the evidence that mattered and what was traded away.', 'Commit, and say why.', 'wd-call'),
        ('iv.', 'The Aftermath', 'What happened, what was learned, and what would change the decision next time.', 'Would we call it again?', ''),
    ]
    step_html = ''.join(
        f'<li class="wd-step {cls}" {"data-pen" if cls else ""}><span class="wd-step-n" aria-hidden="true">{n}</span>'
        f'<h3>{"<span class=wd-circ>" + t + PEN_CIRC + "</span>" if cls else t}</h3><p>{d}</p><p class="wd-note">{note}</p></li>'
        for n, t, d, note, cls in steps
    )
    return f'''{CSS}
<main class="wd" id="what-id-do">

<section class="wd-hero" aria-labelledby="wd-title">
<div class="wrap">
<p class="wd-mast wd-kick"><span>A newsletter + live conversation series</span><span>Edited by Jeremiah Ajayi, from Lagos</span></p>
<h1 id="wd-title" class="wd-word" aria-label="What I’d Do.">What <span class="wd-i" aria-hidden="true">I<span class="wd-who" data-who><b>says Jeremiah</b></span></span>’d Do<span class="wd-dot" aria-hidden="true">.</span></h1>
<p class="wd-note wd-note-i">The “I” changes depending on who’s speaking: Jeremiah in an analysis, the guest in a case.<svg viewBox="0 0 90 52" aria-hidden="true"><path d="M84 30 C 60 34, 26 30, 8 6 M8 6 L 22 10 M8 6 L 10 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></p>
<div class="wd-hero-g">
<div>
<p class="wd-sub">Marketing is full of hard calls. <em>Let’s work <span class="wd-ul">through them.{PEN_UL}</span></em></p>
<div class="wd-body">
<p>The campaign gets attention, but sales gets nothing. Users keep signing up, then disappearing. Your team has five priorities and enough budget for two.</p>
<p class="wd-q">What would you do?</p>
<p>Every two weeks, we unpack real marketing problems, explore the choices on the table, and hear how experienced founders and marketing leaders would approach them.</p>
<p>Twice a month, we take those conversations live.</p>
</div>
<div class="wd-hero-cta"><a class="wd-btn wd-btn-o" href="#subscribe">Subscribe for free <span aria-hidden="true">↓</span></a><a class="wd-link" href="#live">Explore live sessions <span aria-hidden="true">→</span></a></div>
</div>
{subscribe_slip('Get the next decision in your inbox.')}
</div>
</div>
</section>

<section class="wd-sec" aria-labelledby="wd-premise" style="padding-top: clamp(40px, 5vw, 72px)">
<div class="wrap wd-premise-g">
<div>
<p class="wd-kick" style="margin-bottom: 18px">The premise</p>
<h2 id="wd-premise" class="wd-h2">Every decision comes with a trade-off<span class="wd-dot">.</span></h2>
<div class="wd-body">
<p>Do you change the messaging or find a different audience? Invest more in acquisition or fix retention? Defend a campaign that’s struggling or admit it’s time to move on?</p>
<p>There’s rarely a single answer that works for everyone.</p>
<p>What I’d Do examines the context behind these decisions, the evidence people consider, and how they decide what happens next.</p>
</div>
</div>
<article class="wd-file" aria-labelledby="wd-case">
<span class="wd-tab">Case file · example</span>
<span class="wd-stamp">Hypothetical</span>
<div class="wd-file-in">
<h3 id="wd-case" class="wd-kick" style="margin-bottom: 14px">The situation</h3>
<p class="wd-situ">Your launch got real attention: views, sign-ups, a busy week on social. But sales says <b>not one qualified lead</b> came from it, and next quarter’s budget is due on Friday.</p>
<p class="wd-kick" style="margin: 30px 0 0">Three ways to respond. Open one to see the reasoning.</p>
<div class="wd-opts">{opt_html}</div>
<p class="wd-verdict"><b>The call?</b> It depends on one question: did the right people see it and pass, or did the wrong people see it and cheer? That’s the kind of reasoning every edition works through.</p>
</div>
</article>
</div>
</section>

<section aria-label="Two ways to take part" id="formats">
<div class="wd-spread">
<article class="wd-page">
<span class="wd-num" aria-hidden="true">01</span>
<p class="wd-kick">The newsletter</p>
<h3>Read the thinking<span class="wd-dot">.</span></h3>
<p>A twice-monthly newsletter examining real marketing problems through independent analysis, case studies and guest perspectives.</p>
<p>Each edition explains the circumstances, the competing choices and the reasoning behind a recommendation.</p>
<p class="wd-sched"><span>First and third Wednesdays</span><span>3 PM WAT</span><span>Free</span></p>
<a class="wd-link" href="#subscribe">Get the newsletter <span aria-hidden="true">↑</span></a>
</article>
<article class="wd-page dark" id="live">
<span class="wd-num" aria-hidden="true">02</span>
<p class="wd-kick">What I’d Do: Live</p>
<h3>Join the conversation<span class="wd-dot">.</span></h3>
<p>Twice a month, a founder or experienced marketing operator joins Jeremiah to unpack a consequential decision, or the room works through a real marketing problem together.</p>
<p>Expect candid perspectives, challenging questions and practical conclusions, in 45 to 50 minutes.</p>
<p class="wd-sched"><span>Second and fourth Tuesdays</span><span>7 PM WAT</span><span>Online</span></p>
<a class="wd-link" href="#next">Explore upcoming sessions <span aria-hidden="true">↓</span></a>
</article>
</div>
</section>

<section class="wd-sec wd-event" id="next" aria-labelledby="wd-next">
<div class="wrap">
<p class="wd-kick">The next conversation · What I’d Do: Live</p>
<div class="wd-ev-g">
<div>
<h2 id="wd-next" class="wd-ev-t">Your first 90 days as Content Lead<span>What do you fix first?</span></h2>
<p class="wd-guest"><span><b>John Iwuozor</b><span>Content Lead, DualEntry</span></span></p>
<p class="wd-ev-d">You’ve joined a new company. Everyone has an opinion about what marketing needs, and you have limited time to establish your priorities.</p>
<p class="wd-ev-d">John joins What I’d Do to explore his first 90 days at DualEntry: how he approached the role, weighed competing priorities and made his early decisions.</p>
<div class="wd-ev-cta">
<sc-if value="{{{{hasEvent}}}}" hint-placeholder-val="{{{{ false }}}}"><a class="wd-btn wd-btn-o luma-checkout--button" href="{{{{lumaEventHref}}}}" data-luma-action="checkout" data-luma-event-id="{{{{cfg.lumaEventId}}}}">Register on Luma <span aria-hidden="true">↗</span></a><script id="luma-checkout" src="https://embed.lu.ma/checkout-button.js"></script></sc-if>
<sc-if value="{{{{noEvent}}}}" hint-placeholder-val="{{{{ true }}}}"><a class="wd-btn wd-btn-o" href="#subscribe-final">Get the date by email <span aria-hidden="true">↓</span></a><span class="wd-note" style="color: #D9D4CA">Registration opens when the date is set.</span></sc-if>
</div>
</div>
<figure class="wd-port">
<div class="wd-port-f">
<sc-if value="{{{{hasPhoto}}}}" hint-placeholder-val="{{{{ false }}}}"><img src="{{{{cfg.guestPhoto}}}}" alt="John Iwuozor" loading="lazy"></sc-if>
<sc-if value="{{{{noPhoto}}}}" hint-placeholder-val="{{{{ true }}}}"><span class="wd-mono" aria-hidden="true">J.I.</span></sc-if>
</div>
<span class="wd-tba">Date to be announced</span>
<figcaption>Guest: John Iwuozor, Content Lead at DualEntry</figcaption>
</figure>
</div>
<div class="wd-cal" aria-labelledby="wd-up">
<p id="wd-up" class="wd-kick" style="color: #B5B0A6">Upcoming sessions</p>
<sc-if value="{{{{hasCal}}}}" hint-placeholder-val="{{{{ false }}}}"><iframe src="{{{{lumaSrc}}}}" title="Upcoming What I’d Do: Live sessions on Luma" loading="lazy" allowfullscreen aria-hidden="false" tabindex="0"></iframe></sc-if>
<sc-if value="{{{{noCal}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="wd-cal-empty"><span class="wd-blank" aria-hidden="true"><i></i><i></i></span><p>No sessions are open for registration yet. Dates are announced to newsletter readers first, then listed here.</p></div></sc-if>
</div>
</div>
</section>

<section class="wd-sec" aria-labelledby="wd-how">
<div class="wrap">
<div class="wd-how-head"><div><p class="wd-kick" style="margin-bottom: 18px">How it works</p><h2 id="wd-how" class="wd-h2">Put the problem on the table<span class="wd-dot">.</span></h2></div>
<p class="wd-note" style="font-size: 20px; color: var(--ink); max-width: 36ch">Every edition and every live session works through the same four stages, in this order.</p></div>
<ol class="wd-steps">{step_html}</ol>
</div>
</section>

<section class="wd-sec" aria-labelledby="wd-files" style="padding-top: 0">
<div class="wrap">
<div class="wd-how-head"><div><p class="wd-kick" style="margin-bottom: 18px">Recent thinking</p><h2 id="wd-files" class="wd-h2">The Decision Files<span class="wd-dot">.</span></h2></div>
<p style="margin: 0; font-size: 17px; line-height: 1.65; max-width: 44ch">Independent analyses, guest cases and the takeaways from each live session, filed in one place.</p></div>
<div class="wd-files">
<sc-if value="{{{{hasFiles}}}}" hint-placeholder-val="{{{{ false }}}}"><sc-for list="{{{{files}}}}" as="f" hint-placeholder-count="3"><a class="wd-fr" href="{{{{f.href}}}}"><span class="wd-fr-c">{{{{f.cat}}}}</span><span><span class="wd-fr-t">{{{{f.title}}}}</span><span class="wd-fr-d">{{{{f.dek}}}}</span></span><span class="wd-fr-m">{{{{f.by}}}}<br><time datetime="{{{{f.date}}}}">{{{{f.dateLabel}}}}</time> · {{{{f.read}}}}</span></a></sc-for></sc-if>
<sc-if value="{{{{noFiles}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="wd-drawer"><div class="wd-tabs" aria-hidden="true"><span data-l="Analysis"></span><span data-l="Guest case"></span><span data-l="Live takeaway"></span><em>Opening soon</em></div><div><p>The drawer is empty for now. The first file opens with the first issue.</p><a class="wd-link" href="#subscribe-final">Get it when it’s filed <span aria-hidden="true">↓</span></a></div></div></sc-if>
</div>
</div>
</section>

<section class="wd-sec" aria-labelledby="wd-shoes" style="background: #EDE7DA">
<div class="wrap wd-sub-g">
<div>
<p class="wd-kick" style="margin-bottom: 22px">Submit a problem</p>
<h2 id="wd-shoes" class="wd-quote">What would you do if you were <em>in my shoes?</em></h2>
<div class="wd-body"><p>Have a marketing problem you can’t quite figure out? Tell us what’s happening. We might select your case for a future newsletter issue or live conversation.</p><p>Cases can be anonymised, and we’ll ask permission before sharing anything that identifies you or your company.</p></div>
</div>
<div class="wd-card">
<p class="wd-kick">What to include</p>
<ol><li>What’s happening, in a few sentences</li><li>What you’ve tried or are considering</li><li>What’s at stake, and by when</li></ol>
<sc-if value="{{{{hasSubmitUrl}}}}" hint-placeholder-val="{{{{ false }}}}"><a class="wd-btn" href="{{{{cfg.submitUrl}}}}">Submit a problem <span aria-hidden="true">↗</span></a></sc-if>
<sc-if value="{{{{noSubmitUrl}}}}" hint-placeholder-val="{{{{ true }}}}"><a class="wd-btn" href="{{{{submitMail}}}}">Submit a problem by email <span aria-hidden="true">↗</span></a><small>Opens your email app with these three prompts ready to fill in.</small></sc-if>
</div>
</div>
</section>

<section class="wd-sec wd-host" aria-labelledby="wd-host">
<div class="wrap wd-host-g">
<figure class="wd-host-ph"><img src="{B(HEADSHOT)}" alt="Portrait of Jeremiah Ajayi" loading="lazy"><figcaption class="wd-note">Your host, asking the questions</figcaption></figure>
<div>
<p class="wd-kick" style="margin-bottom: 18px">About the host</p>
<h2 id="wd-host" class="wd-h2">The person asking the questions<span class="wd-dot">.</span></h2>
<p>Jeremiah Ajayi is a marketing strategist focused on positioning, product launches and growth for technology companies. His experience includes marketing work at RemotePass and Stears.</p>
<p>What I’d Do grew from his interest in how marketing decisions are made: the assumptions behind them, the alternatives people consider, and what happens when the original plan doesn’t work.</p>
<p style="margin-top: 26px"><a class="wd-link" href="Site-About.dc.html">More about Jeremiah <span aria-hidden="true">→</span></a></p>
</div>
</div>
</section>

<section class="wd-sec wd-final" aria-labelledby="wd-final">
<div class="wrap">
<h2 id="wd-final" class="wd-h2">A good question deserves a <span class="wd-serif" style="font-style: italic; font-weight: 400; letter-spacing: -.02em">better answer</span><span class="wd-dot">.</span></h2>
<p class="wd-lead">Subscribe for real marketing problems, thoughtful perspectives and decisions worth examining.</p>
{subscribe_slip('Subscribe for free', 'h3', 'final')}
<p class="wd-micro">Twice monthly. No noise.</p>
<nav class="wd-back" aria-label="Back to the main site"><a href="Home-B2.dc.html">Jeremiah Ajayi, home</a><a href="Site-Work.dc.html">Work</a><a href="Site-Writing.dc.html">Writing</a><a href="Site-About.dc.html">About</a></nav>
</div>
</section>
</main>
<!--NOBAND-->
'''
