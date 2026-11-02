import sys, json, subprocess, time, os, urllib.request
from playwright.sync_api import sync_playwright

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.environ.get("TEMP", "."), "zaoan_shots")
PAGES = sys.argv[3].split(",") if len(sys.argv) > 3 else ["index.html", "pricing.html", "terms.html", "privacy.html"]
PORT = int(os.environ.get("PORT", "8765"))
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "-d", ROOT],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
os.makedirs(SHOTS, exist_ok=True)

JS = r"""
() => {
  const vw = document.documentElement.clientWidth;
  const res = {scrollW: document.documentElement.scrollWidth, bodyScrollW: document.body.scrollWidth, vw, small: [], overflow: [], links: [], ids: []};
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode; if (!t.textContent.trim()) continue;
    const el = t.parentElement; if (seen.has(el)) continue; seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    if (el.closest('.skip')) continue;
    const r = el.getBoundingClientRect(); if (r.width === 0 && r.height === 0) continue;
    const fs = parseFloat(cs.fontSize);
    if (fs < 16) res.small.push(fs + 'px ' + el.tagName + '.' + el.className + ' "' + t.textContent.trim().slice(0, 30) + '"');
  }
  document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el); if (cs.position === 'fixed') return;
    if (el.closest('.table-wrap')) return;
    const r = el.getBoundingClientRect();
    if (r.width && (r.right > vw + 0.5 || r.left < -0.5)) {
      // ignore children clipped by an overflow:hidden ancestor
      let p = el.parentElement, clipped = false;
      while (p && p !== document.body) { const pc = getComputedStyle(p); if (pc.overflowX !== 'visible') { const pr = p.getBoundingClientRect(); if (pr.right <= vw + 0.5 && pr.left >= -0.5) { clipped = true; break; } } p = p.parentElement; }
      if (!clipped && !el.closest('.skip') && !el.matches('body::before')) res.overflow.push(el.tagName + '.' + el.className + ' L' + Math.round(r.left) + ' R' + Math.round(r.right));
    }
  });
  document.querySelectorAll('a[href]').forEach(a => res.links.push(a.getAttribute('href')));
  document.querySelectorAll('[id]').forEach(e => res.ids.push(e.id));
  res.tableScroll = [...document.querySelectorAll('.table-wrap')].filter(t=>t.scrollWidth>t.clientWidth+1).length;
  res.imgsBroken = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src);
  return res;
}
"""
report = {}
bad_resp = []
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    for name, vp in [("mobile", {"width": 375, "height": 812}), ("desktop", {"width": 1366, "height": 900})]:
        ctx = b.new_context(viewport=vp, device_scale_factor=1 if name == "desktop" else 2,
                            is_mobile=(name == "mobile"), has_touch=(name == "mobile"))
        for pg in PAGES:
            page = ctx.new_page()
            page.on("response", lambda r: bad_resp.append((r.status, r.url)) if r.status >= 400 else None)
            page.goto(f"http://localhost:{PORT}/{pg}", wait_until="networkidle")
            page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
            page.wait_for_timeout(1500)
            r = page.evaluate(JS)
            report[f"{name}:{pg}"] = r
            out = os.path.join(SHOTS, f"{pg.replace('.html','')}-{name}.png")
            H = page.evaluate("document.documentElement.scrollHeight"); W = vp["width"]
            dpr = 1 if name == "desktop" else 2
            from PIL import Image
            canvas = Image.new("RGB", (W*dpr, H*dpr)); seg = 3000; tmp = out + ".part.png"
            for y in range(0, H, seg):
                h = min(seg, H - y)
                page.screenshot(path=tmp, full_page=True, clip={"x":0,"y":y,"width":W,"height":h})
                canvas.paste(Image.open(tmp), (0, y*dpr))
            os.remove(tmp); canvas.save(out)
            page.close()
        ctx.close()
    b.close()

# link check
ids = {k.split(":")[1]: set(v["ids"]) for k, v in report.items()}
link_problems = set()
for k, v in report.items():
    pg = k.split(":")[1]
    for h in v["links"]:
        if h.startswith(("http", "mailto:")):
            if "line.me" in h and h != "https://line.me/R/ti/p/@581vndzf": link_problems.add((pg, h))
            continue
        if h == "#" or h == "": link_problems.add((pg, "EMPTY " + h)); continue
        file, _, frag = h.partition("#")
        file = file or pg
        if not os.path.exists(os.path.join(ROOT, file)): link_problems.add((pg, "MISSING " + h)); continue
        if frag and file in ids and frag not in ids[file]: link_problems.add((pg, "BADFRAG " + h))
srv.terminate()
for k, v in report.items():
    print(f"== {k}: scrollW={v['scrollW']} vw={v['vw']} small={len(v['small'])} overflow={len(v['overflow'])} broken_img={v['imgsBroken']} tableScroll={v['tableScroll']}")
    for s in v["small"][:15]: print("   small:", s)
    for s in v["overflow"][:15]: print("   overflow:", s)
print("HTTP>=400:", sorted(set(bad_resp)))
print("link problems:", sorted(link_problems))
