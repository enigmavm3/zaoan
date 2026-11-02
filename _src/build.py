import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from parts import *

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "")
pages = [
 ("index.html", "早安圖王｜LINE AI 祝福圖，新朋友免費送 5 張",
  "在 LINE 裡點一下、打上名字，AI 約 40 秒做好專屬早安圖、生日、節慶、神佛祝福圖，直接轉傳親友。加好友免費送 5 張，之後每張 NT$8～10。"),
 ("pricing.html", "價目與退款政策｜早安圖王",
  "早安圖王點數價目：NT$10／1 點、NT$90／10 點、NT$160／20 點（含稅），付費點數效期 365 天；購買後 7 日內可退款（未使用全額、用過一部分按剩餘點數比例），超過 7 天恕不退款。"),
 ("terms.html", "服務條款｜早安圖王",
  "早安圖王服務條款：服務內容、點數、付款與發票、退款、使用規範、AI 生成內容與著作權、準據法與管轄。"),
 ("privacy.html", "隱私權政策｜早安圖王",
  "早安圖王隱私權政策：蒐集項目、利用目的、第三方服務、資料保存、您的權利與 Cookie。"),
]
for fn, title, desc in pages:
    is_index = fn == "index.html"
    body = open(fn.replace('.html', '_body.html'), encoding='utf8').read()
    body = (body.replace('__LINE_BTN_FINAL__', line_btn('加好友・領 5 張免費', 'xl'))
                .replace('__LINE_BTN_PLAN__', line_btn('加好友後在 LINE 購買', 'block'))
                .replace('__LINE_BTN__', line_btn()))
    if not is_index:
        body = body.replace('<main id="main">', '<main id="main" class="subpage">', 1)
    html = (head(title, desc, '' if is_index else fn, 'has-float' if is_index else '')
            + header(fn) + body + footer(float_cta=is_index))
    open(OUT + fn, 'w', encoding='utf8', newline='\n').write(html)
print('ok')
