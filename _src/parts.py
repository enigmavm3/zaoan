BASE = "https://triplehai.com/zaoan/"
LINE_URL = "https://line.me/R/ti/p/@581vndzf"

LINE_ICON = '<span class="line-icon" aria-hidden="true">LINE</span>'

OG_IMAGE = BASE + "img/og-image.jpg"
OG_ALT = "早安圖王：在 LINE 打上名字，AI 做好專屬早安圖、長輩圖、生日與節慶祝福圖"


def head(title, desc, path, body_class="", jsonld="", preload=""):
    url = BASE + path
    bc = f' class="{body_class}"' if body_class else ""
    return f'''<!doctype html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#b11a2a">
<link rel="icon" type="image/png" sizes="192x192" href="img/icon.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="zh_TW">
<meta property="og:site_name" content="早安圖王">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{OG_ALT}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE}">
<meta name="twitter:image:alt" content="{OG_ALT}">
{preload}<style>
__FONT_FACE__
</style>
<link rel="stylesheet" href="style.css">
{jsonld}
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QWQ6SVBYF4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-QWQ6SVBYF4');
</script>
</head>
<body{bc}>
<a class="skip" href="#main">跳到主要內容</a>
'''


NAV = [("index.html", "首頁"), ("pricing.html", "價目與退款"), ("terms.html", "服務條款"), ("privacy.html", "隱私權政策")]


def header(current):
    links = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV
    )
    return f'''<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="index.html">
      <span class="seal" aria-hidden="true">王</span>
      <span class="brand-text">
        <span class="brand-name">早安圖王</span>
        <span class="brand-sub">ZAOANTU · SINCE 2026</span>
      </span>
    </a>
    <nav class="nav" aria-label="主選單">
{links}
    </nav>
    <a class="top-cta" href="{LINE_URL}" rel="noopener">加 LINE 好友</a>
  </div>
</header>
'''


def footer(float_cta=False):
    fl = f'''
<div class="float-cta">
  <a href="{LINE_URL}" rel="noopener">{LINE_ICON}<span>加 LINE・領 5 張</span></a>
</div>''' if float_cta else ""
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand">
          <span class="seal sm" aria-hidden="true">王</span>
          <span><b>早安圖王</b><br>為台灣長輩設計的 LINE 祝福圖服務</span>
        </div>
        <p>艾鐸有限公司・統一編號 62222415</p>
        <p>客服信箱：<a href="mailto:contact@triplehai.com">contact@triplehai.com</a></p>
        <p>LINE 官方帳號 ID：<a href="{LINE_URL}" rel="noopener">@581vndzf</a></p>
      </div>
      <ul class="foot-links">
        <li><a href="terms.html">服務條款</a></li>
        <li><a href="privacy.html">隱私權政策</a></li>
        <li><a href="pricing.html">價目與退款</a></li>
      </ul>
    </div>
    <p class="copy">© 2026 艾鐸有限公司　早安圖王</p>
  </div>
</footer>{fl}
</body>
</html>
'''


def line_btn(text="加好友・領 5 張免費", cls=""):
    c = f"btn-line {cls}".strip()
    return f'<a class="{c}" href="{LINE_URL}" rel="noopener">{LINE_ICON}<span>{text}</span></a>'
