"""把 topics.py 的資料組成主題頁 <main> 內容（SEO 第一批）。"""
import html as h

from parts import HOME, line_btn
from topics import LINE_CTA, TOPIC_BY_SLUG, TOPICS, iter_images

R = "../"  # 主題頁在 /zaoan/<slug>/，回網站根目錄


def esc(s):
    return h.escape(s, quote=True)


def alt_of(topic, desc, text):
    return f"{topic['crumb']}範例：{desc}，寫著「{text.replace(' ', '　')}」"


def first_image(topic):
    sec, f, t, s, d, k = next(iter_images(topic))
    return f, t, d


def pic(topic, f, t, d, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<figure class="pic"><img src="img/{f}.webp" width="800" height="800" {load} decoding="async" '
            f'alt="{esc(alt_of(topic, d, t))}"><figcaption>「{esc(t.replace(" ", "　"))}」</figcaption></figure>')


def wishes(lines):
    lis = "\n".join(
        f'        <li><span class="wish-text">{esc(w)}</span>'
        f'<button type="button" class="copy-btn" data-copy="{esc(w)}" aria-label="複製這句：{esc(w)}">複製</button></li>'
        for w in lines)
    return f'''    <div class="wish-box">
      <h3>可以複製的祝福語</h3>
      <ul class="wish-list">
{lis}
      </ul>
    </div>'''


def cta(topic, where):
    more = ("" if topic["slug"] == "generator" else
            f'\n    <p class="cta-more"><a href="{R}generator/">長輩圖產生器：怎麼做一張打上名字的圖 →</a></p>')
    return f'''  <div class="topic-cta" data-ga-loc="{topic['slug']}" id="cta-{where}">
    <p class="cta-title">{LINE_CTA}</p>
    <p>在 LINE 點選單、打上「阿嬤」「美華姊」這樣的稱呼，AI 大約 20 秒做好。加好友先送 5 張，不用綁卡、不用下載 App。</p>
    {line_btn("加好友・免費做 5 張", "xl")}{more}
  </div>
'''


def faq(topic):
    items = []
    for i, (q, ans) in enumerate(topic["faq"]):
        ps = "".join(f"<p>{a}</p>" for a in ans)
        items.append(f'      <details{" open" if i == 0 else ""}>\n        <summary>{q}</summary>\n'
                     f'        <div class="ans">{ps}</div>\n      </details>')
    return '  <section id="faq">\n    <h2>常見問題</h2>\n    <div class="faq">\n' + "\n".join(items) + "\n    </div>\n  </section>\n"


def rel_card(t, prefix):
    f, txt, d = first_image(t)
    return (f'<a class="rel-card" href="{prefix}{t["slug"]}/"><img src="{prefix}{t["slug"]}/img/{f}.webp" width="800" height="800" '
            f'loading="lazy" decoding="async" alt="{esc(t["short"])}範例圖"><span>{t["emoji"]} {esc(t["short"])}</span></a>')


def related(topic):
    cards = "\n      ".join(rel_card(TOPIC_BY_SLUG[s], R) for s in topic["related"])
    others = [t for t in TOPICS if t["slug"] not in topic["related"] and t["slug"] != topic["slug"]]
    more = "、".join(f'<a href="{R}{t["slug"]}/">{esc(t["short"])}</a>' for t in others)
    return f'''  <section id="related">
    <h2>相關主題</h2>
    <div class="rel-grid">
      {cards}
    </div>
    <p class="rel-more">更多：{more}；<a href="{HOME}">早安圖王首頁</a>、<a href="{R}pricing.html">價目與退款</a></p>
  </section>
'''


SAVE = '''  <section id="save">
    <h2>怎麼存圖、傳給親友</h2>
    <ol class="flow">
      <li>手指<b>按住圖片不放</b>（長按）。</li>
      <li>iPhone 選「<b>加入「照片」</b>」，Android 選「<b>下載圖片</b>」，圖就存到手機相簿了。</li>
      <li>打開 LINE 聊天室，點相片圖示，選剛剛存的圖傳出去。</li>
    </ol>
    <p class="note-free">這頁的範例圖都是早安圖王用 AI 做的，<b>歡迎長按存圖、分享給親友</b>。</p>
  </section>
'''


def extra_generator():
    rows = [
        ("要不要安裝", "要從 App Store／Google Play 下載", "不用，用瀏覽器打開網站", "不用，加 LINE 好友就能用"),
        ("怎麼做", "選背景圖，自己打字、調字型和位置", "選背景圖，自己打字", "點選單選主題、打上名字，AI 畫好整張圖"),
        ("圖上加名字", "可以，自己排版", "可以，自己排版", "可以，AI 直接寫進圖裡"),
        ("背景圖", "App 內建圖庫，數量多", "依網站而定", "每次由 AI 重新畫，不會和別人一模一樣"),
        ("費用", "多數免費，可能有廣告或付費進階功能", "多數免費", "加好友送 5 張，之後每張 NT$5～10"),
        ("等多久", "馬上", "馬上", "約 20 秒"),
        ("要注意", "選可信任的 App，留意權限和廣告", "要自己存圖，再傳到 LINE", "前 5 張後要付費；字的位置不能自己調"),
        ("適合誰", "會操作 App、想自己慢慢排版的人", "用電腦、想快速加字的人", "不想學排版、想在 LINE 直接收圖轉傳的長輩"),
    ]
    head = "<tr><th>比較</th><th>長輩圖 App</th><th>線上長輩圖產生器（網頁）</th><th>早安圖王（LINE）</th></tr>"
    labels = ["長輩圖 App", "線上產生器", "早安圖王"]
    body = "\n".join(
        f'          <tr><th>{r[0]}</th>' + "".join(
            f'<td data-label="{labels[i]}"{" class=\"us\"" if i == 2 else ""}>{c}</td>' for i, c in enumerate(r[1:])) + "</tr>"
        for r in rows)
    return f'''  <section id="compare">
    <h2>長輩圖 App、線上工具、早安圖王比較</h2>
    <p>三種方法都能做長輩圖，各有適合的人。下面是一般情況的比較，各 App 和網站的功能不同，以實際為準。</p>
    <div class="table-wrap stack cmp">
      <table>
        <thead>{head}</thead>
        <tbody>
{body}
        </tbody>
      </table>
    </div>
  </section>

  <section id="how">
    <h2>用早安圖王做長輩圖：三個步驟</h2>
    <ol class="flow">
      <li><b>加 LINE 好友</b>：點下面的綠色按鈕，或在 LINE 搜尋 ID <b>@581vndzf</b>。加入就送 5 點免費。</li>
      <li><b>點選單選主題</b>：聊天室下方有早安、晚安、生日、節慶圖、祝賀圖、神佛加持，點一下再選風格。</li>
      <li><b>打上名字</b>：輸入「媽媽早安」這樣的字，大約 20 秒，圖就傳到聊天室，按住圖片就能轉傳。</li>
    </ol>
    <p>也可以點「自己打字」，輸入想說的話；或傳一張自己的照片，請 AI 加上祝福字（一樣 1 點）。價格請看<a href="{R}pricing.html">價目與退款</a>。</p>
  </section>
'''


def extra_cny(topic):
    rows = "\n".join(f'          <tr><th>{a}</th><td data-label="日期">{b}</td><td data-label="習俗">{c}</td></tr>'
                     for a, b, c in topic["schedule"])
    return f'''  <section id="dates">
    <h2>2027 過年日期一覽</h2>
    <div class="table-wrap dates">
      <table>
        <thead><tr><th>日子</th><th>國曆日期</th><th>習俗</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
    <p>初五迎財神，也可以傳一張<a href="{R}deity/#caishen">財神早安圖</a>。實際放假日以行政院人事行政總處公告為準。</p>
  </section>
'''


def render(topic):
    secs = topic["sections"]
    jump = "".join(f'<li><a href="#{s["id"]}">{esc(s["h2"])}</a></li>' for s in secs)
    lead = "\n  ".join(f"<p>{p}</p>" for p in topic["lead"])
    out = [f'''<main id="main" class="subpage topic">
<div class="wrap">
  <nav class="crumbs" aria-label="麵包屑"><a href="{HOME}">早安圖王</a><span aria-hidden="true">›</span><span aria-current="page">{esc(topic["crumb"])}</span></nav>
</div>
<div class="wrap page-head">
  <h1>{esc(topic["h1"])}</h1>
  {lead}
  <ul class="topic-jump">{jump}</ul>
</div>

<div class="wrap doc wide">
''']
    if topic["slug"] == "chinese-new-year":
        out.append(extra_cny(topic))
    first = True
    for i, s in enumerate(secs):
        pics = "\n      ".join(pic(topic, f, t, d, eager=(first and j == 0))
                               for j, (f, t, _, d, *_) in enumerate(s["images"]))
        first = False
        out.append(f'''  <section id="{s["id"]}">
    <h2>{esc(s["h2"])}</h2>
    <p>{s["intro"]}</p>
    <div class="pic-grid">
      {pics}
    </div>
{wishes(s["wishes"])}
  </section>
''')
        if i == 0:
            out.append(cta(topic, "top"))
    if topic["slug"] == "generator":
        out.append(extra_generator())
    out.append(SAVE)
    out.append(cta(topic, "bottom"))
    out.append(faq(topic))
    out.append(related(topic))
    out.append('''</div>
</main>
<script>
// 複製祝福語：先用 Clipboard API，LINE 內建瀏覽器等不支援時退回 execCommand
document.addEventListener('click', function (e) {
  var b = e.target.closest && e.target.closest('.copy-btn');
  if (!b) return;
  var t = b.getAttribute('data-copy');
  function done() {
    b.textContent = '已複製 ✓'; b.classList.add('ok');
    setTimeout(function () { b.textContent = '複製'; b.classList.remove('ok'); }, 2000);
  }
  function fallback() {
    var ta = document.createElement('textarea');
    ta.value = t; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { if (document.execCommand('copy')) done(); } catch (_) {}
    document.body.removeChild(ta);
  }
  if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(t).then(done, fallback);
  else fallback();
});
</script>
''')
    return "".join(out)


def hot_topics():
    """首頁「熱門主題」區塊。"""
    cards = "\n      ".join(rel_card(t, "") for t in TOPICS)
    return f'''  <section class="sec" id="topics">
    <div class="sec-head">
      <div class="sec-eyebrow">熱門主題</div>
      <h2 class="sec-title">冬至、聖誕、過年……<br><span class="red">當季祝福圖</span>先看看</h2>
      <p class="sec-sub">每個主題都有十幾張範例圖和可以直接複製的祝福語，歡迎長按存圖、分享給親友。</p>
    </div>
    <div class="rel-grid hot">
      {cards}
    </div>
  </section>
'''


def image_urls(topic, base):
    return [f"{base}{topic['slug']}/img/{f}.webp" for _, f, *_ in iter_images(topic)]
