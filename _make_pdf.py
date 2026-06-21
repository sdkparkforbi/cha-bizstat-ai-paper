# -*- coding: utf-8 -*-
import sys, pathlib; sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

HTML = pathlib.Path(r"D:\Teaching\2026_1\BizStat\web\index.html").resolve()
OUT  = r"D:\Teaching\2026_1\BizStat\web\BizStat-AI-TeachingBot.pdf"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.route("**/paged.polyfill.js", lambda r: r.abort())
    pg.route("**/pagedjs*", lambda r: r.abort())
    pg.goto(HTML.as_uri(), wait_until="networkidle")
    pg.emulate_media(media="print")
    pg.pdf(path=OUT, format="A4", print_background=True,
           display_header_footer=False, prefer_css_page_size=True)
    b.close()
print("PDF:", OUT)
