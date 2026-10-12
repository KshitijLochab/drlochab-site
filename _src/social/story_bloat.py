"""Instagram story (1080x1920), Mon 12 Oct 2026: 'Bloated after meals?' with space for a poll sticker,
pointing to the gas and bloating carousel posted the same day. Reuses the balloon drawing from week_2026_10_12.py.
Run from anywhere: python3 _src/social/story_bloat.py  -> _src/out/week-2026-10-12/ig-story-bloated-poll.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, OUT, balloon, foot
from playwright.sync_api import sync_playwright

STORY = f"""<div class="s teal" style="width:1080px;height:1920px;padding:150px 80px">
 <div class="kick" style="font-size:30px;color:#9FD8CC;text-align:center">Quick question</div>
 <h1 style="font-size:112px;text-align:center;margin-top:22px">Bloated<br>after <em>meals?</em></h1>
 <div style="position:absolute;left:250px;top:560px;width:580px;height:619px">{balloon()}</div>
 <!-- empty band from about y=1230 to 1480 for the Instagram poll sticker -->
 <div style="position:absolute;left:80px;right:80px;top:1530px;text-align:center">
  <p style="font-size:40px;line-height:1.35;color:#FFFFFF">It is usually harmless.<br><b style="font-weight:600;color:#F3B84A">3 common causes</b> in today's post.</p>
 </div>
 {foot(light=True, pad=80, size=1.15)}</div>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        tmp = f"{OUT}/tmp-story.html"
        open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{STORY}</body></html>")
        pg.goto(f"file://{tmp}"); pg.wait_for_timeout(400)
        pg.screenshot(path=f"{OUT}/ig-story-bloated-poll.png")
        b.close()
    os.remove(tmp)
    print("done")
