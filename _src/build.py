import datetime, html as htmlmod, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from parts import *
import fonts

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "")
TODAY = datetime.date.today().isoformat()

# (檔名, title, description, 麵包屑名稱, sitemap priority)
pages = [
 ("index.html", "早安圖王｜AI 早安圖、長輩圖產生器，LINE 加好友送 5 張",
  "長輩最愛的早安圖、長輩圖！在 LINE 打上名字，AI 約 40 秒做好；生日、中秋、過年、神明保佑圖都有。加好友免費送 5 張，之後每張 NT$5～10。",
  "首頁", "1.0"),
 ("pricing.html", "價目與退款政策｜早安圖王 AI 早安圖・長輩圖",
  "NT$10／1 點、NT$90／10 點、NT$160／20 點、NT$500／100 點（含稅），1 點做 1 張圖，付費點數效期 365 天；可用信用卡、手機支付、ATM、超商付款，信用卡與手機支付 7 日內可退款。",
  "價目與退款政策", "0.8"),
 ("terms.html", "服務條款｜早安圖王 AI 祝福圖",
  "早安圖王服務條款：服務內容、點數、付款方式與發票、退款、邀請好友贈點、使用規範、AI 生成內容與著作權、準據法與管轄。",
  "服務條款", "0.5"),
 ("privacy.html", "隱私權政策｜早安圖王 AI 祝福圖",
  "早安圖王隱私權政策：蒐集項目、利用目的、第三方服務、資料保存、您的權利與 Cookie。",
  "隱私權政策", "0.5"),
]

ORG_ID, SITE_ID = BASE + "#org", BASE + "#website"


def ld(obj):
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": obj}, ensure_ascii=False, indent=1)
            + '\n</script>\n')


def text_of(fragment):
    t = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", htmlmod.unescape(t)).strip()


def faq_items(body):
    items = []
    for q, a in re.findall(r"<summary>(.*?)</summary>\s*<div class=\"ans\">(.*?)</div>\s*</details>", body, re.S):
        paras = [text_of(p) for p in re.findall(r"<p>(.*?)</p>", a, re.S)]
        items.append({"@type": "Question", "name": text_of(q),
                      "acceptedAnswer": {"@type": "Answer", "text": "\n".join(paras)}})
    return items


def offers():
    o = [("新朋友體驗（加好友送 5 點，無使用期限）", "0"), ("單張（1 點）", "10"),
         ("10 點方案", "90"), ("20 點方案", "160"), ("100 點方案", "500")]
    return [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "TWD",
             "availability": "https://schema.org/InStock", "url": BASE + "pricing.html#plans"} for n, p in o]


def jsonld_for(fn, crumb, body):
    if fn == "index.html":
        return ld([
            {"@type": "Organization", "@id": ORG_ID, "name": "艾鐸有限公司", "legalName": "艾鐸有限公司",
             "url": BASE, "logo": {"@type": "ImageObject", "url": BASE + "img/logo-512.jpg", "width": 512, "height": 512},
             "email": "contact@triplehai.com", "taxID": "62222415", "sameAs": [LINE_URL],
             "contactPoint": {"@type": "ContactPoint", "contactType": "customer service",
                              "email": "contact@triplehai.com", "url": LINE_URL, "availableLanguage": "zh-Hant-TW"}},
            {"@type": "WebSite", "@id": SITE_ID, "name": "早安圖王", "url": BASE, "inLanguage": "zh-Hant-TW",
             "publisher": {"@id": ORG_ID}},
            {"@type": "Service", "@id": BASE + "#service", "name": "早安圖王",
             "alternateName": ["早安圖王 AI 祝福圖", "AI 早安圖、長輩圖產生器"],
             "serviceType": "AI 早安圖、長輩圖與祝福圖生成（LINE 官方帳號）",
             "description": "在 LINE 官方帳號點選單、打上名字或想說的話，AI 約 40 秒做好專屬早安圖、晚安圖、生日、節慶與神佛祝福圖，可直接轉傳親友。加好友免費送 5 點，1 點 = 1 張圖。",
             "url": BASE, "image": OG_IMAGE, "provider": {"@id": ORG_ID}, "brand": {"@type": "Brand", "name": "早安圖王"},
             "areaServed": {"@type": "Country", "name": "TW"}, "availableChannel": {"@type": "ServiceChannel", "serviceUrl": LINE_URL},
             "offers": offers()},
            {"@type": "FAQPage", "@id": BASE + "#faq", "mainEntity": faq_items(body)},
        ])
    return ld([
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "早安圖王", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": BASE + fn}]},
    ])


def picture(m):
    """<img src="img/X.jpg"> → <picture> 先給 WebP，舊瀏覽器退回 JPG。"""
    tag, src = m.group(0), m.group(1)
    webp = src[:-4] + ".webp"
    if not os.path.exists(OUT + webp):
        return tag
    return f'<picture><source srcset="{webp}" type="image/webp">{tag}</picture>'


HERO = 'img/sample-1.webp'
built = {}
for fn, title, desc, crumb, _ in pages:
    is_index = fn == "index.html"
    body = open(fn.replace('.html', '_body.html'), encoding='utf8').read()
    body = (body.replace('__LINE_BTN_FINAL__', line_btn('加好友・領 5 張免費', 'xl'))
                .replace('__LINE_BTN_PLAN__', line_btn('加好友後在 LINE 購買', 'block'))
                .replace('__LINE_BTN__', line_btn()))
    if not is_index:
        body = body.replace('<main id="main">', '<main id="main" class="subpage">', 1)
    else:
        # hero 圖是 LCP：提高下載優先序
        body = body.replace('<img src="img/sample-1.jpg" alt=', '<img src="img/sample-1.jpg" fetchpriority="high" alt=', 1)
    body = re.sub(r'<img src="(img/[\w-]+\.jpg)"[^>]*>', picture, body)
    preload = (f'<link rel="preload" as="image" href="{HERO}" type="image/webp" fetchpriority="high">\n'
               if is_index and os.path.exists(OUT + HERO) else "")
    html = (head(title, desc, '' if is_index else fn, 'has-float' if is_index else '',
                 jsonld_for(fn, crumb, body), preload)
            + header(fn) + body + footer(float_cta=is_index))
    built[fn] = html

font_css = fonts.build(built.values())


def content_part(s):
    return s.split("<body", 1)[-1] if s else ""


# sitemap lastmod：只有 <body> 內容真的變了才更新日期
old_sm = open(OUT + "sitemap.xml", encoding="utf8").read() if os.path.exists(OUT + "sitemap.xml") else ""
old_dates = dict(re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", old_sm))
urls = []
for fn, title, desc, crumb, prio in pages:
    html = built[fn].replace("__FONT_FACE__", font_css)
    loc = BASE + ("" if fn == "index.html" else fn)
    old = open(OUT + fn, encoding="utf8").read() if os.path.exists(OUT + fn) else ""
    head_old, head_new = old.split("<body", 1)[0], html.split("<body", 1)[0]
    strip = lambda h: re.sub(r"<style>[\s\S]*?</style>", "", h)
    changed = content_part(old) != content_part(html) or strip(head_old) != strip(head_new)
    lastmod = TODAY if changed or loc not in old_dates else old_dates[loc]
    urls.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{prio}</priority></url>")
    open(OUT + fn, 'w', encoding='utf8', newline='\n').write(html)

open(OUT + "sitemap.xml", "w", encoding="utf8", newline="\n").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls) + "\n</urlset>\n")
print('ok')
