// Renders og/wid-launch.html to PNGs (1x and 2x). Usage: serve og/ on :8812, then NODE_PATH=$(npm root -g) node wid-launch-shot.js
const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
for (const [k,w,h] of [['li',1080,1350],['x',1600,900]]) for (const s of [1,2]){
 const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:s});
 await p.goto('http://localhost:8812/wid-launch.html#'+k);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 if(s===1) console.log(k, JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('h1,.tag,.rel,.url,.sun')].map(e=>{const r=e.getBoundingClientRect();return [e.className||e.tagName,Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]}))));
 await p.screenshot({path:`out/what-id-do-launch_${k==='li'?'linkedin_1080x1350':'x_1600x900'}${s==2?'@2x':''}.png`});await p.close();}
await b.close();})();
