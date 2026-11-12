// Browser checks for the key patient journeys. Needs Playwright with Chromium and a local server:
//   python3 -m http.server 8765 &        (from the repository root, or from _src/site for a local build)
//   node _src/tests/browser_check.js     (BASE=http://localhost:8765 by default)
// Fails (exit code 1) on script errors, pages wider than the phone screen, or a broken journey.
const { chromium } = require('playwright');
const BASE = process.env.BASE || 'http://localhost:8765';
const PAGES = ['/', '/hi/', '/conditions/fatty-liver/', '/hi/conditions/acidity-reflux-gerd/', '/procedures/ercp/', '/answers/gas-and-bloating/',
  '/guides/colonoscopy-preparation/', '/hi/guides/endoscopy-preparation/', '/tools/gut-tracker/', '/tools/stool-check/', '/diet-charts/',
  '/diet-charts/fatty-liver/', '/hi/diet-charts/ulcerative-colitis-crohns/', '/about-dr-kshitij-lochab/', '/gastroenterologist-in-gurgaon/', '/404.html'];
const fails = [];
const fail = (where, msg) => fails.push(`${where}: ${msg}`);

(async () => {
  const b = await chromium.launch();
  // 1. every representative page: no script errors, nothing wider than the screen
  for (const w of [360, 1280]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 800 } });
    for (const u of PAGES) {
      const pg = await ctx.newPage(); const errs = [];
      pg.on('pageerror', e => errs.push(e.message));
      pg.on('console', m => { if (m.type() === 'error' && !/favicon|404 \(File not found\)/.test(m.text())) errs.push(m.text().slice(0, 140)); });
      const r = await pg.goto(BASE + u, { waitUntil: 'load' });
      if (!r || (r.status() >= 400 && !u.includes('404'))) fail(u, `HTTP ${r && r.status()}`);
      await pg.waitForTimeout(400);
      if (errs.length) fail(`${u} @${w}px`, 'script error: ' + errs.join(' | '));
      if (await pg.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)) fail(`${u} @${w}px`, 'page is wider than the screen');
      await pg.close();
    }
    await ctx.close();
  }
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, acceptDownloads: true });
  const pg = await ctx.newPage();
  // 2. home: tips load, symptom gives a booking button, booking link names the reason
  for (const lang of ['', 'hi/']) {
    await pg.goto(`${BASE}/${lang}`); await pg.waitForTimeout(800);
    const tip = await pg.$eval('#tipBody', e => e.textContent);
    if (/could not load|लोड नहीं/.test(tip) || tip.trim().length < 40) fail(`/${lang}`, "today's tip did not load");
    await pg.$$eval('#symList button', x => x[2].click());
    if (!(await pg.$('#symResult .sym-go'))) fail(`/${lang}`, 'symptom result has no booking button');
    await pg.$$eval('#reasonChips .chip', x => x[1].click());
    const wa = await pg.$eval('#waBook', e => decodeURIComponent(e.href));
    if (!wa.startsWith('https://wa.me/919667104882?text=') || wa.length < 60) fail(`/${lang}`, 'WhatsApp booking link is wrong: ' + wa.slice(0, 80));
    if ((await pg.$$('#procGrid .ptile')).length < 9) fail(`/${lang}`, 'procedure tiles missing');
  }
  // 2b. phones: one-tap Call and WhatsApp at the top of the home page and under the opening paragraph of an article, and as floating buttons
  for (const [u, top] of [['/', '.id-cta'], ['/hi/', '.id-cta'], ['/conditions/fatty-liver/', '.ds-cta'], ['/hi/answers/gas-and-bloating/', '.ds-cta'], ['/procedures/ercp/', '.ds-cta']]) {
    await pg.goto(BASE + u); await pg.waitForTimeout(500);
    const r = await pg.evaluate(sel => {
      const box = document.querySelector(sel); if (!box) return { box: false };
      const vis = e => !!e && e.getBoundingClientRect().width > 0;
      const tel = box.querySelector('a[href="tel:+919667104882"]'), wa = box.querySelector('a[href^="https://wa.me/919667104882?text="]');
      return { box: true, y: Math.round(box.getBoundingClientRect().top + scrollY), tel: vis(tel), wa: vis(wa),
               fabCall: !!document.querySelector('.fabs .fab-call[href="tel:+919667104882"]'), fabWa: !!document.querySelector('.fabs a.fab[href^="https://wa.me/919667104882?text="]') };
    }, top);
    if (!r.box || !r.tel || !r.wa) fail(u, 'Call and WhatsApp buttons near the top are missing');
    else if (r.y > 1300) fail(u, `Call and WhatsApp buttons are too far down the page (${r.y}px)`);
    if (!r.fabCall || !r.fabWa) fail(u, 'floating Call or WhatsApp button is missing');
  }
  // 2c. the floating buttons show once the top buttons have scrolled away, and fit side by side on a small phone
  {
    const small = await b.newContext({ viewport: { width: 360, height: 740 } }); const sp = await small.newPage();
    for (const u of ['/', '/hi/', '/conditions/fatty-liver/', '/hi/conditions/fatty-liver/']) {
      await sp.goto(BASE + u); await sp.waitForTimeout(400); await sp.evaluate(() => scrollTo(0, 3000)); await sp.waitForTimeout(500);
      const boxes = await sp.$$eval('.fabs .fab', x => x.map(e => { const r = e.getBoundingClientRect(), s = getComputedStyle(e); return { l: r.left, r: r.right, shown: s.visibility !== 'hidden' && r.width > 0 }; }));
      if (boxes.length < 3 || boxes.some(x => !x.shown)) fail(u, 'floating Diet charts, Call and Book buttons are not all showing after scrolling');
      const s = boxes.slice().sort((x, y) => x.l - y.l);
      if (s.some((x, i) => i && x.l < s[i - 1].r - 1) || s[0].l < 0 || s[s.length - 1].r > 360) fail(u, 'floating buttons overlap or run off a 360px screen');
    }
    await small.close();
  }
  // 3. a shared link to the booking section lands on it
  await pg.goto(`${BASE}/#visit`); await pg.waitForTimeout(2200);
  const top = await pg.$eval('#visit', e => e.getBoundingClientRect().top);
  if (Math.abs(top - 70) > 40) fail('/#visit', `lands ${Math.round(top)}px from the top`);
  // 3b. a shared link to the Thali meter opens it, with the section heading and tabs showing (not hidden under the header)
  await pg.goto(`${BASE}/#fibre`); await pg.waitForTimeout(2200);
  const fib = await pg.evaluate(() => ({ hidden: document.getElementById('fibre').hidden, top: document.getElementById('daily').getBoundingClientRect().top }));
  if (fib.hidden || Math.abs(fib.top - 70) > 40) fail('/#fibre', `Thali meter link lands wrongly (hidden=${fib.hidden}, section ${Math.round(fib.top)}px from the top)`);
  // 4. preparation planner makes a dated plan and a calendar file
  await pg.goto(`${BASE}/guides/colonoscopy-preparation/`);
  const d = new Date(Date.now() + 5 * 864e5).toISOString().slice(0, 10);
  await pg.evaluate(d => { const i = document.getElementById('ppDate'); i.value = d; i.dispatchEvent(new Event('input', { bubbles: true })); i.dispatchEvent(new Event('change', { bubbles: true })); }, d);
  await pg.waitForTimeout(200);
  const ics = await pg.$('.pp-ics, button:has-text("calendar")');
  if (!ics) fail('prep planner', 'calendar button missing');
  else {
    const [dl] = await Promise.all([pg.waitForEvent('download', { timeout: 4000 }).catch(() => null), ics.click()]);
    if (!dl) fail('prep planner', 'calendar file was not created');
  }
  // 5. diet diary: adding a food updates the day
  await pg.goto(`${BASE}/diet-charts/fatty-liver/#diary`); await pg.waitForTimeout(500);
  const ok = await pg.evaluate(async () => {
    const slot = document.querySelector('.dd-slots button, [data-slot]'); if (!slot) return false; slot.click();
    await new Promise(r => setTimeout(r, 200));
    const food = document.querySelector('.dd-sheet .chip, .dd-sheet button'); if (!food) return false; food.click();
    await new Promise(r => setTimeout(r, 200)); return true;
  });
  if (!ok) fail('diet diary', 'could not add a food');
  // 6. stool check gives an answer
  await pg.goto(`${BASE}/tools/stool-check/`); await pg.click('.sc-opt[data-kind="s"][data-i="3"]'); await pg.waitForTimeout(150);
  if (await pg.$eval('#scResS', e => e.hidden)) fail('stool check', 'no answer shown');
  // 7. tracker: the private page still blocks outgoing connections
  await pg.goto(`${BASE}/tools/gut-tracker/`);
  const csp = await pg.$eval('meta[http-equiv="Content-Security-Policy"]', e => e.content).catch(() => '');
  if (!csp.includes("connect-src 'none'")) fail('gut tracker', 'privacy policy header missing');
  await b.close();
  if (fails.length) { console.log(`${fails.length} problem(s):`); fails.forEach(f => console.log('  ✗', f)); process.exit(1); }
  console.log(`Browser checks passed (${PAGES.length} pages at 2 widths, 9 journeys).`);
})().catch(e => { console.error(e); process.exit(1); });
