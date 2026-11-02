"""自架子集字型：依四頁實際用到的字，把 Noto Serif TC / Noto Sans TC / Ma Shan Zheng
切成小 woff2，放到 ../fonts/，並回傳要內嵌在 <head> 的 @font-face CSS。

- 原始 TTF 第一次會從 Google Fonts 下載，快取在 _src/.fontcache/（不進 git）。
- 每次 build 都重算用字，改文案後只要重跑 build.py 就會自動補字，不必手動維護。
- 檔名含內容雜湊，內容變了網址就變，避免瀏覽器吃到舊快取。
"""
import hashlib, html, io, os, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, ".fontcache")
OUT_DIR = os.path.join(os.path.dirname(HERE), "fonts")

# (CSS family, weight, 檔名代號, Google Fonts css2 family 參數)
FACES = [
    ("Noto Serif TC", 700, "serif-700", "Noto+Serif+TC:wght@700"),
    ("Noto Serif TC", 900, "serif-900", "Noto+Serif+TC:wght@900"),
    ("Noto Sans TC", 400, "sans-400", "Noto+Sans+TC:wght@400"),
    ("Noto Sans TC", 700, "sans-700", "Noto+Sans+TC:wght@700"),
    ("Noto Sans TC", 900, "sans-900", "Noto+Sans+TC:wght@900"),
    ("Ma Shan Zheng", 400, "brush-400", "Ma+Shan+Zheng"),
]
# 書法字只用在印章「王」「福」，只切這幾個字
BRUSH_TEXT = "王福"


def _ttf_path(key, family_param):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, key + ".ttf")
    if not os.path.exists(p):
        css = urllib.request.urlopen(urllib.request.Request(
            "https://fonts.googleapis.com/css2?family=" + family_param,
            headers={"User-Agent": "Wget/1.21"})).read().decode()
        url = re.search(r"url\((https://[^)]+\.ttf)\)", css).group(1)
        data = urllib.request.urlopen(url).read()
        open(p, "wb").write(data)
    return p


def page_chars(html_pages):
    chars = set(chr(c) for c in range(0x20, 0x7F))
    chars |= set("，。、；：？！「」『』（）《》〈〉…—–‧・／～％＋＝×÷→←↑↓●○◎★☆✓✕｜·　")
    for s in html_pages:
        s = re.sub(r"<(script|style)\b[\s\S]*?</\1>", " ", s)
        # title / meta / alt 也算（分享預覽與輔助工具不會用到網頁字型，但多幾個字無妨）
        s = re.sub(r"<[^>]+>", " ", s)
        chars |= set(html.unescape(s))
    return {c for c in chars if not c.isspace() or c == " "}


def build(html_pages):
    from fontTools import subset
    os.makedirs(OUT_DIR, exist_ok=True)
    text = "".join(sorted(page_chars(html_pages)))
    css, keep = [], set()
    for family, weight, key, param in FACES:
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["*"]
        opts.name_IDs = ["*"]
        opts.notdef_outline = True
        font = subset.load_font(_ttf_path(key, param), opts)
        sub = subset.Subsetter(opts)
        sub.populate(text=BRUSH_TEXT if key.startswith("brush") else text)
        sub.subset(font)
        buf = io.BytesIO()
        subset.save_font(font, buf, opts)
        data = buf.getvalue()
        fn = f"{key}.{hashlib.sha1(data).hexdigest()[:8]}.woff2"
        keep.add(fn)
        path = os.path.join(OUT_DIR, fn)
        if not os.path.exists(path):
            open(path, "wb").write(data)
        css.append(f"@font-face{{font-family:\"{family}\";font-style:normal;font-weight:{weight};"
                   f"font-display:swap;src:url(fonts/{fn}) format(\"woff2\")}}")
    for f in os.listdir(OUT_DIR):
        if f.endswith(".woff2") and f not in keep:
            os.remove(os.path.join(OUT_DIR, f))
    return "\n".join(css)
