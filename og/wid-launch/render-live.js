// Renders live.html in both formats at 2x into ./export, plus feed-size previews.
// Usage (from this folder): python3 -m http.server 8812 &  then  node render.js
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [hash, w, h, name] of [['portrait', 1080, 1350, 'what-id-do-live_linkedin_1080x1350'], ['wide', 1600, 900, 'what-id-do-live_x_1600x900']]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await p.goto('http://localhost:8812/live.html#' + hash);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    const boxes = await p.evaluate(() => [...document.querySelectorAll('.mast,.sheet,.photo,.who,.when,.topic,.url')].map(e => { const r = e.getBoundingClientRect(); return (e.className || e.tagName) + ' ' + [r.left, r.top, r.right, r.bottom].map(Math.round).join(',') }));
    console.log(name, '\n  ' + boxes.join('\n  '));
    await p.screenshot({ path: `export/${name}@2x.png` });
    await p.close();
    const p1 = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await p1.goto('http://localhost:8812/live.html#' + hash); await p1.evaluate(() => document.fonts.ready); await p1.waitForTimeout(300);
    await p1.screenshot({ path: `export/${name}.png` }); await p1.close();
  }
  await b.close();
})();
