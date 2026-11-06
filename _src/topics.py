"""SEO 主題頁內容（第一批 7 頁，依 SEO_RESEARCH.md 第 4 節）。

每張範例圖：(檔名, 圖上文字, 英文場景描述（生圖用）, 中文畫面描述（alt 用）)
- 圖上文字空白 = 換行（生圖時分兩行）
- 圖檔在 <slug>/img/<檔名>.webp，由早安圖王同款 AI（gpt-image-2 low）產生，人工逐張檢查錯字
- 每年更新：title／description／lead 的年份與日期（網址不帶年份）
"""

# 頁面共用的生圖風格（kind）
#   base: 開頭描述；tstyle: 文字樣式；tail: 風格與限制
KINDS = {
    "dongzhi": dict(
        base="Create a cozy and heartwarming Taiwanese Winter Solstice (Dongzhi) greeting image.",
        tstyle="warm red or gold, rounded friendly calligraphy font",
        tail="Mood: warm, reunion, comforting. Style: appetizing photorealistic with soft warm lighting. NO Western elements."),
    "morning": dict(
        base="Create a warm and cheerful Chinese-style morning greeting image for Taiwanese elders.",
        tstyle="elegant brush calligraphy or modern rounded font, golden or warm red color",
        tail="Mood: gentle, auspicious, warm. Style: photorealistic with warm lighting, NOT cartoon. NO Western elements."),
    "christmas": dict(
        base="Create a warm and cheerful Christmas greeting image for Taiwanese elders.",
        tstyle="festive red or gold, elegant rounded font",
        tail="Mood: warm, peaceful, joyful. Style: photorealistic with warm glowing lights."),
    "newyear": dict(
        base="Create a bright and auspicious New Year's Day (January 1st) greeting image for Taiwanese elders.",
        tstyle="shining gold or warm red, bold elegant font",
        tail="Mood: hopeful, joyful, fresh start. Style: vibrant photorealistic with glowing light."),
    "cold": dict(
        base="Create a warm and caring Chinese-style winter morning greeting image for Taiwanese elders, reminding them to keep warm in cold weather.",
        tstyle="warm red, orange or gold, rounded friendly font, very easy to read",
        tail="Mood: caring, cozy, warm. Style: photorealistic with soft warm lighting, NOT cartoon. NO Western elements."),
    "deity": dict(
        base="Create a reverent and auspicious Taiwanese traditional religious morning blessing image.",
        tstyle="auspicious gold or cinnabar red, elegant brush calligraphy fitting Taiwanese temple art, inside ONE vertical banner or ONE horizontal plaque",
        tail=("The deity must be the unambiguous focal point, depicted with full dignity and respect, faithful to traditional iconography. "
              "Decorative elements: auspicious clouds, lotus flowers, golden halo, temple ornaments. "
              "Style: traditional Chinese temple mural painting or Taiwanese folk religious art with rich gold accents. "
              "NO Western religious elements. NO modern elements. NO distorted, comical, or disrespectful features."),
        faces=True),
    "cny": dict(
        base="Create a festive Chinese New Year greeting image for Taiwanese elders, for the 2027 Year of the Goat (Sheep).",
        tstyle="gold text with red outline, bold and celebratory",
        tail="Mood: joyful, prosperous, festive, auspicious. Style: rich and luxurious photorealistic. NO Western elements."),
    "generic": dict(
        base="Create a warm Chinese-style greeting image for Taiwanese elders.",
        tstyle="elegant brush calligraphy or modern rounded font, gold or warm red",
        tail="Mood: auspicious, warm, sincere. Style: photorealistic, NOT cartoon. NO Western elements."),
}

LINE_CTA = "想打上親友名字？加 LINE 免費做 5 張"

TOPICS = [
# ───────────────────────────── 1. 冬至 ─────────────────────────────
dict(
 slug="dongzhi", kind="dongzhi", crumb="冬至祝福圖", short="冬至祝福圖", emoji="🥣",
 title="2026 冬至祝福圖｜冬至圖片、湯圓早安圖與祝福語｜早安圖王",
 desc="2026 冬至是 12 月 22 日（星期二）。15 張冬至祝福圖、湯圓早安圖、冬至長輩圖，繁體中文、可長按存圖轉傳，附可直接複製的冬至祝福語。想打上親友名字，加 LINE 好友免費做 5 張。",
 h1="冬至祝福圖",
 lead=["2026 年冬至是 <b>12 月 22 日（星期二）</b>。冬至吃湯圓，祝福家人團團圓圓、平平安安。",
       "下面有 15 張冬至祝福圖、冬至早安圖，還有可以直接複製的祝福語。歡迎長按存圖，傳給親友。"],
 sections=[
  dict(id="tangyuan", h2="湯圓冬至圖", intro="紅白湯圓、芝麻湯圓、熱騰騰的甜湯，一看就知道是冬至。",
   images=[
    ("dongzhi-tangyuan-01", "冬至快樂", "a steaming bowl of red and white tangyuan rice balls in sweet ginger soup on a wooden table, warm kitchen light", "一碗紅白湯圓冒著熱氣"),
    ("dongzhi-tangyuan-02", "冬至吃湯圓", "a blue-and-white porcelain bowl full of pink and white tangyuan, rising steam, a porcelain spoon", "青花瓷碗裝著粉紅與白色湯圓"),
    ("dongzhi-tangyuan-03", "團團圓圓", "black sesame tangyuan, one cut open showing the sesame filling, in a red bowl, warm glow", "芝麻湯圓切開露出內餡"),
    ("dongzhi-tangyuan-04", "冬至暖心", "peanut tangyuan in sweet soup in a rustic ceramic bowl, steam, red plum blossom twig beside", "花生湯圓與一枝紅梅"),
    ("dongzhi-tangyuan-05", "冬至平安", "a pot of hot tangyuan soup with a wooden ladle, several small bowls, golden warm light", "一鍋熱湯圓與幾個小碗"),
   ],
   wishes=["冬至快樂！吃碗熱湯圓，全家團團圓圓、平平安安。",
           "冬至到了，記得吃湯圓，祝您甜甜蜜蜜、身體健康。",
           "一碗湯圓一份心，祝您冬至快樂、福氣滿滿。"]),
  dict(id="morning", h2="冬至早安圖", intro="冬至當天早上傳一張，順便提醒親友天冷保暖。",
   images=[
    ("dongzhi-morning-01", "冬至早安", "winter sunrise over misty Taiwanese mountains, a bowl of tangyuan on a windowsill in the foreground", "山上冬日日出，窗台放著一碗湯圓"),
    ("dongzhi-morning-02", "冬至早安 平安喜樂", "red plum blossoms on snowy branches in soft golden morning light", "晨光中的紅梅與白雪"),
    ("dongzhi-morning-03", "早安 冬至快樂", "a cup of hot tea and a small bowl of tangyuan by a sunny window in the morning", "窗邊一杯熱茶和一碗湯圓"),
    ("dongzhi-morning-04", "冬至早安 天冷保暖", "a red knitted scarf and a steaming bowl of tangyuan on a table, morning sunlight", "紅色圍巾與熱湯圓"),
   ],
   wishes=["冬至早安！天冷了，出門多穿一件，記得吃湯圓暖暖身子。",
           "早安！今天冬至，祝您平安喜樂、事事順心。",
           "冬至早安，白天最短、思念最長，祝您一切安好。"]),
  dict(id="reunion", h2="團圓與梅花", intro="想要莊重一點、適合傳到家族群組的，可以選這幾張。",
   images=[
    ("dongzhi-reunion-01", "冬至團圓", "a round dining table set with many bowls of tangyuan, warm lamp light, a family home atmosphere with no people", "圓桌上擺滿一碗碗湯圓"),
    ("dongzhi-plum-01", "冬至吉祥", "red plum blossoms in the snow, traditional Chinese ink wash painting style", "水墨畫風的雪中紅梅"),
    ("dongzhi-plum-02", "闔家平安", "ink wash painting of plum branches with a bowl of tangyuan, red seal stamp accent", "水墨梅枝與一碗湯圓"),
   ],
   wishes=["冬至團圓，祝您闔家平安、幸福美滿。",
           "冬至吉祥，梅花迎冬，好運跟著來。",
           "冬至大如年，祝您全家和樂、健康平安。"]),
  dict(id="name", h2="打上名字的冬至圖", intro="下面這幾張是在早安圖王打上稱呼做出來的，收到的人會特別有感覺。",
   images=[
    ("dongzhi-name-01", "阿嬤冬至快樂", "a steaming bowl of red and white tangyuan, a warm cozy kitchen, plum blossoms", "熱湯圓與梅花"),
    ("dongzhi-name-02", "爸媽冬至平安", "two bowls of tangyuan side by side on a wooden table, warm golden light", "兩碗湯圓並排"),
    ("dongzhi-name-03", "美華姐 冬至快樂", "a bowl of colorful tangyuan with red plum blossoms, soft warm light", "彩色湯圓與紅梅"),
   ],
   wishes=["阿嬤，冬至快樂！記得吃湯圓，身體健康喔。",
           "爸、媽，冬至天冷多穿一點，週末回家一起吃湯圓。"]),
 ],
 faq=[
  ("2026 年冬至是哪一天？",
   ["2026 年冬至是 <b>12 月 22 日（星期二）</b>。冬至是二十四節氣之一，落在國曆 12 月 21 日或 22 日，每年不一定。台灣習俗吃湯圓，俗話說「吃了湯圓又長一歲」。"]),
  ("這些冬至圖可以免費存下來、傳給親友嗎？",
   ["可以。這頁的圖都是早安圖王用 AI 做的，歡迎長按圖片存到手機，再到 LINE 傳給親友或群組。"]),
  ("可以做一張打上家人名字的冬至圖嗎？",
   ["可以。加 LINE 好友「早安圖王」，冬至前後在選單「節慶圖」就有「冬至湯圓」；任何時候也可以點「自己打字」，輸入「阿嬤冬至快樂」。",
    "加好友先送 5 張免費，大約 20 秒做好。"]),
  ("冬至祝福語怎麼寫比較得體？",
   ["短短一句就好：問候＋湯圓＋平安健康。例如「冬至快樂！吃碗熱湯圓，全家團團圓圓、平平安安。」給長輩可以加一句「天冷多穿一件」。"]),
 ],
 related=["christmas", "new-year", "cold-weather", "generator"],
),

# ───────────────────────────── 2. 長輩圖產生器 ─────────────────────────────
dict(
 slug="generator", kind="morning", crumb="長輩圖產生器", short="長輩圖產生器", emoji="✍️",
 title="長輩圖產生器 2026｜LINE 打上名字，AI 做早安圖｜早安圖王",
 desc="2026 長輩圖產生器比較：App、線上工具、LINE 早安圖王差在哪？早安圖王不用下載 App，在 LINE 打上名字，AI 約 20 秒做好繁體中文早安圖、生日、節慶長輩圖。加好友免費送 5 張。",
 h1="長輩圖產生器",
 lead=["想做一張有名字的早安圖、長輩圖？早安圖王是 <b>LINE 裡的 AI 長輩圖產生器</b>：點選單、打上名字，大約 20 秒就做好，不用下載 App。",
       "下面有範例圖、和 App／線上工具的比較，還有三步驟教學。加好友先送 5 張免費。"],
 sections=[
  dict(id="names", h2="同一張早安圖，打上不同名字", intro="一樣是向日葵早安圖，打上不同的稱呼，就變成只給那個人的一張。",
   images=[
    ("generator-name-01", "媽媽早安", "warm sunflowers and roses with morning dew, golden sunrise light", "向日葵與玫瑰"),
    ("generator-name-02", "阿嬤早安 身體健康", "warm sunflowers and roses with morning dew, golden sunrise light", "向日葵與玫瑰"),
    ("generator-name-03", "王老師早安", "warm sunflowers and roses with morning dew, golden sunrise light", "向日葵與玫瑰"),
    ("generator-name-04", "美華姐早安", "warm sunflowers and roses with morning dew, golden sunrise light", "向日葵與玫瑰"),
   ],
   wishes=["媽媽早安！今天也要開開心心的。",
           "阿嬤早安，祝您身體健康、天天笑呵呵。",
           "王老師早安，謝謝您的照顧，祝您一切順心。"]),
  dict(id="themes", h2="各種主題都能做", intro="早安、晚安、生日、新婚、添丁、康復、升官、神佛加持，點選單就有。",
   images=[
    ("generator-morning-01", "早安 平安喜樂", "traditional Chinese ink wash painting of green bamboo and a gentle sunrise", "水墨竹子與日出", "morning"),
    ("generator-night-01", "晚安 好夢", "serene moonlit night with stars over a peaceful lake, deep blue sky", "月光與星空下的湖面", "generic"),
    ("generator-birthday-01", "生日快樂 福如東海", "pink longevity peach buns (shoutao) and a red birthday cake with gold decorations", "壽桃與紅色生日蛋糕", "generic"),
    ("generator-wedding-01", "新婚誌喜 百年好合", "red double happiness wedding decorations, red roses and gold ribbons", "紅色囍字與玫瑰", "generic"),
    ("generator-baby-01", "恭喜添丁", "a small pair of red baby shoes, a gold longevity lock pendant and red envelopes", "紅色嬰兒鞋與金鎖片", "generic"),
    ("generator-getwell-01", "早日康復", "a bouquet of fresh yellow and white flowers in soft morning light by a window", "窗邊一束黃白色鮮花", "generic"),
    ("generator-promotion-01", "步步高升", "golden ingots, a red ribbon, and a staircase of golden steps rising into light", "金元寶與往上的金色階梯", "generic"),
    ("generator-deity-01", "笑口常開", "Maitreya Buddha as a joyful laughing monk with a broad happy smile and a large round belly, loose orange robes, prayer beads, golden auspicious light and lotus flowers", "笑容滿面的彌勒佛", "deity"),
   ],
   wishes=["晚安，好夢！明天又是美好的一天。",
           "祝您生日快樂，福如東海、壽比南山。",
           "祝你們新婚快樂，百年好合、永結同心。"]),
 ],
 faq=[
  ("長輩圖產生器要錢嗎？",
   ["早安圖王加 LINE 好友先送 <b>5 點</b>（可做 5 張，沒有使用期限）。用完想再做，再買點數：NT$10 買 1 點、NT$90 買 10 點、NT$160 買 20 點、NT$500 買 100 點（含稅，平均每張最低 NT$5）。不買也不會被收費。",
    "市面上也有免費的長輩圖 App 和網站，可以依自己的需要選。"]),
  ("要下載 App 嗎？",
   ["不用。早安圖王是 LINE 官方帳號，加好友後在聊天室點選單就能做，做好的圖會直接傳到聊天室。"]),
  ("圖上的字是繁體中文嗎？會不會有錯字？",
   ["是繁體中文。中文字一般都清楚好讀，但 AI 每次畫的結果不一定相同。做圖失敗一律不扣點；成功送出的圖扣 1 點。"]),
  ("可以用自己的照片做長輩圖嗎？",
   ["可以。傳一張照片給早安圖王，再打字說明想怎麼改，例如「幫我加上早安祝福字」。照片修圖一樣是 1 點。"]),
  ("做好的圖怎麼傳給親友？",
   ["圖做好會傳到 LINE 聊天室，按住圖片選「轉傳」就能傳給親友或群組。圖片只暫存供傳送，喜歡的圖請自己存到手機。"]),
 ],
 related=["dongzhi", "christmas", "chinese-new-year", "deity"],
),

# ───────────────────────────── 3. 聖誕節 ─────────────────────────────
dict(
 slug="christmas", kind="christmas", crumb="聖誕節祝福圖片", short="聖誕節祝福圖片", emoji="🎄",
 title="2026 聖誕節祝福圖片｜聖誕快樂、平安夜圖片與祝福語｜早安圖王",
 desc="2026 平安夜是 12 月 24 日（四）、聖誕節 12 月 25 日（五）。15 張聖誕快樂圖片、平安夜祝福圖、聖誕早安圖，中文祝福、可長按存圖轉傳，附可複製的祝福語。加 LINE 好友免費做 5 張打上名字的。",
 h1="聖誕節祝福圖片",
 lead=["2026 年平安夜是 <b>12 月 24 日（星期四）</b>，聖誕節是 <b>12 月 25 日（星期五）</b>。",
       "這頁有 15 張中文的聖誕快樂圖片、平安夜祝福圖和聖誕早安圖，都附上可以直接複製的祝福語。歡迎長按存圖，傳給親友。"],
 sections=[
  dict(id="merry", h2="聖誕快樂圖片", intro="聖誕樹、花圈、雪景小屋，暖暖的燈光，中文字清楚好讀。",
   images=[
    ("christmas-tree-01", "聖誕快樂", "a glowing decorated Christmas tree with warm fairy lights and gifts in a cozy living room", "掛滿燈飾的聖誕樹與禮物"),
    ("christmas-tree-02", "聖誕快樂 平安喜樂", "a tall Christmas tree with red and gold ornaments beside a window with falling snow", "紅金裝飾的聖誕樹與窗外飄雪"),
    ("christmas-wreath-01", "溫馨聖誕", "a red and green Christmas wreath with pine cones, bells and red ribbon on a wooden door", "木門上的聖誕花圈"),
    ("christmas-snow-01", "聖誕節快樂", "a cozy snow-covered cabin with warm lit windows at night, gentle snowfall", "雪夜裡亮著燈的小木屋"),
    ("christmas-gift-01", "幸福滿滿", "a pile of red and gold wrapped gift boxes with ribbons and poinsettia flowers", "一堆紅金色禮物盒與聖誕紅"),
    ("christmas-snowman-01", "聖誕快樂", "a cute smiling snowman with a red scarf and a knitted hat in a snowy garden, soft warm light", "戴紅圍巾的可愛雪人"),
   ],
   wishes=["聖誕快樂！祝您平安喜樂、天天開心。",
           "聖誕節到了，祝福您和家人幸福滿滿、溫暖過冬。",
           "送您一棵祝福的聖誕樹，掛滿健康、平安和好運。"]),
  dict(id="eve", h2="平安夜祝福圖", intro="12 月 24 日晚上傳，祝對方平平安安。",
   images=[
    ("christmas-eve-01", "平安夜快樂", "warm glowing candles with pine branches and red berries on a table at night", "燭光、松枝與紅色果實"),
    ("christmas-eve-02", "平安夜 平安喜樂", "a peaceful snowy village at night under a starry sky with warm lit windows", "星空下的雪地小鎮"),
    ("christmas-eve-03", "平安夜 闔家平安", "a lantern glowing in the snow beside a small decorated pine tree at night", "雪地裡的燈籠與小松樹"),
    ("christmas-eve-04", "平平安安", "shiny red apples wrapped in festive cellophane with red ribbons, Christmas lights in the background", "包著緞帶的紅蘋果（平安果）"),
    ("christmas-eve-05", "平安夜晚安", "a crescent moon over snowy pine trees, deep blue night sky with stars", "雪松上的彎月與星空"),
   ],
   wishes=["平安夜快樂，祝您平平安安、一夜好眠。",
           "今晚平安夜，送上一顆平安果，祝您全家平安健康。",
           "平安夜，願您身邊都是溫暖和愛。"]),
  dict(id="morning", h2="聖誕節早安圖", intro="聖誕節早上傳一張早安圖，比貼圖多一分心意。",
   images=[
    ("christmas-morning-01", "聖誕早安", "morning sunrise over snowy pine trees with red holly berries in the foreground", "晨光中的雪松與紅色冬青果"),
    ("christmas-morning-02", "早安 聖誕快樂", "red poinsettia flowers and a cup of hot cocoa on a windowsill in soft morning light", "聖誕紅與一杯熱可可"),
    ("christmas-morning-03", "平安夜早安", "a small Christmas tree with soft fairy lights on a sunny morning table, gift box", "晨光裡的小聖誕樹"),
    ("christmas-name-01", "阿明 聖誕快樂", "a glowing Christmas tree with gifts and warm fairy lights", "聖誕樹與禮物"),
   ],
   wishes=["聖誕早安！天冷了多穿一件，祝您今天開開心心。",
           "早安，聖誕快樂！願這個冬天溫暖又平安。"]),
 ],
 faq=[
  ("2026 年平安夜、聖誕節是哪一天？",
   ["平安夜是 <b>12 月 24 日（星期四）</b>，聖誕節是 <b>12 月 25 日（星期五）</b>。台灣的 12 月 25 日不放假。"]),
  ("這些聖誕圖片可以免費存下來嗎？",
   ["可以。這頁的圖都是早安圖王用 AI 做的，歡迎長按圖片存到手機，再傳給親友。"]),
  ("怎麼做一張打上名字的聖誕圖？",
   ["加 LINE 好友「早安圖王」，12 月聖誕節期間，選單「節慶圖」裡有「聖誕快樂」，選好風格再打上名字就行；也可以點「自己打字」。加好友先送 5 張免費。"]),
  ("給長輩的聖誕祝福語怎麼寫？",
   ["用中文、講平安和健康最得體，例如「聖誕快樂！祝您平安喜樂、天天開心。」平安夜可以說「祝您平平安安、一夜好眠」。"]),
 ],
 related=["dongzhi", "new-year", "cold-weather", "generator"],
),

# ───────────────────────────── 4. 元旦 ─────────────────────────────
dict(
 slug="new-year", kind="newyear", crumb="元旦祝福圖", short="元旦祝福圖", emoji="🎆",
 title="2027 元旦祝福圖｜元旦圖片、新年快樂早安圖與祝福語｜早安圖王",
 desc="2027 元旦是 1 月 1 日（星期五）。14 張元旦祝福圖、2027 新年快樂圖片、元旦早安圖與長輩圖，繁體中文、可長按存圖轉傳，附可複製的元旦祝福語。加 LINE 好友免費做 5 張打上名字的。",
 h1="元旦祝福圖",
 lead=["2027 年元旦是 <b>1 月 1 日（星期五）</b>，國曆新年的第一天。",
       "這頁有 14 張 2027 新年快樂圖片、元旦早安圖和給長輩的元旦祝福圖，都附上可以直接複製的祝福語。歡迎長按存圖，跨年夜或元旦早上傳給親友。"],
 sections=[
  dict(id="2027", h2="2027 新年快樂圖片", intro="煙火、金色亮片，圖上直接寫著 2027。",
   images=[
    ("newyear-2027-01", "2027 新年快樂", "brilliant golden fireworks over a city skyline at night", "城市夜空的金色煙火"),
    ("newyear-2027-02", "2027 元旦快樂", "elegant gold and red festive decorations with sparkles and bokeh lights", "紅金裝飾與閃亮光點"),
    ("newyear-2027-03", "2027 平安喜樂", "the first sunrise of the year over the sea, golden sky", "海上的新年第一道曙光"),
    ("newyear-2027-04", "2027 萬事如意", "red and gold fireworks with plum blossoms in the foreground", "紅金煙火與梅花"),
    ("newyear-2027-05", "2027 好運來", "golden sparkles and colorful fireworks over a calm lake at night", "湖面上的煙火"),
   ],
   wishes=["2027 新年快樂！祝您新的一年平安健康、萬事如意。",
           "元旦快樂！新年新希望，願您天天都有好心情。",
           "跨年快樂，2027 一起好好過，祝福滿滿！"]),
  dict(id="sunrise", h2="元旦早安圖（新年第一道曙光）", intro="元旦早上傳日出圖，祝對方新的一年順順利利。",
   images=[
    ("newyear-sunrise-01", "元旦早安", "the first sunrise of the year over the ocean and a rocky coast, golden light", "海岸邊的元旦日出"),
    ("newyear-sunrise-02", "新年新希望", "sunrise over a sea of clouds in Taiwanese high mountains", "高山雲海日出"),
    ("newyear-sunrise-03", "元旦快樂 早安", "red plum blossoms in front of a golden sunrise", "日出前的紅梅"),
    ("newyear-sunrise-04", "迎接新的一年", "a golden sunrise over rice terraces and mountains, fresh morning mist", "梯田與山間的日出"),
    ("newyear-sunrise-05", "新年早安 身體健康", "golden morning sunrise with blooming red camellias in the foreground", "晨光中的紅色山茶花"),
   ],
   wishes=["元旦早安！迎接新年的第一道陽光，祝您一整年都順順利利。",
           "新年新希望，祝您身體健康、心想事成。",
           "早安！新的一年，願您每天都平安喜樂。"]),
  dict(id="elder", h2="給長輩的元旦祝福圖", intro="傳給爸媽、長輩，講平安和健康最得體。",
   images=[
    ("newyear-elder-01", "新年快樂 身體健康", "red peonies and gold decorations with soft golden glow", "紅牡丹與金色裝飾"),
    ("newyear-elder-02", "元旦快樂 闔家平安", "warm festive red lanterns and gold sparkles, soft bokeh", "紅燈籠與金色光點"),
    ("newyear-elder-03", "新的一年 平安順心", "a calm sunrise over a lake with plum blossom branches", "湖面日出與梅枝"),
    ("newyear-name-01", "爸媽 新年快樂", "golden fireworks and red plum blossoms, warm festive glow", "金色煙火與紅梅"),
   ],
   wishes=["新的一年，祝爸媽身體健康、笑口常開。",
           "元旦快樂！祝您闔家平安、幸福美滿。"]),
 ],
 faq=[
  ("元旦和過年有什麼不一樣？",
   ["元旦是<b>國曆</b> 1 月 1 日，2027 年是星期五，放假。過年是<b>農曆</b>新年（春節），2027 年大年初一是 2 月 6 日。過年的祝福圖請看<a href=\"../chinese-new-year/\">2027 羊年過年祝福圖</a>。"]),
  ("這些元旦圖片可以免費存下來嗎？",
   ["可以。這頁的圖都是早安圖王用 AI 做的，歡迎長按圖片存到手機，再傳給親友。"]),
  ("怎麼做一張打上名字的元旦圖？",
   ["加 LINE 好友「早安圖王」，12 月下旬到 1 月初，選單「節慶圖」裡有「元旦新年」；任何時候也可以點「自己打字」，輸入「爸媽新年快樂」。加好友先送 5 張免費。"]),
  ("元旦祝福圖什麼時候傳比較好？",
   ["12 月 31 日晚上跨年時，或 1 月 1 日早上傳都很適合。早上傳可以選日出圖，配一句「元旦早安」。"]),
 ],
 related=["christmas", "chinese-new-year", "dongzhi", "generator"],
),

# ───────────────────────────── 5. 天冷早安圖 ─────────────────────────────
dict(
 slug="cold-weather", kind="cold", crumb="天冷早安圖", short="天冷早安圖", emoji="🧣",
 title="天冷早安圖 2026｜寒流來襲、注意保暖長輩圖與問候語｜早安圖王",
 desc="2026 冬天的天冷早安圖：寒流來襲、天冷保暖、早晚溫差大，14 張繁體中文早安圖，可長按存圖轉傳，附可複製的天冷問候語。想打上爸媽的稱呼，加 LINE 好友免費做 5 張。",
 h1="天冷早安圖",
 lead=["天冷了、寒流來了，傳一張早安圖提醒親友<b>多穿一件、注意保暖</b>。",
       "這頁有 14 張天冷早安圖、寒流早安圖，都附上可以直接複製的問候語。歡迎長按存圖，傳給家人和朋友。"],
 sections=[
  dict(id="warm", h2="天冷了，多穿一件", intro="熱茶、圍巾、暖暖的光，一看就覺得溫暖。",
   images=[
    ("cold-tea-01", "天冷了 多穿一件", "a cup of hot tea with steam beside a folded red knitted scarf, warm morning light", "熱茶與紅色毛線圍巾"),
    ("cold-scarf-01", "天冷 注意保暖", "a warm wool scarf, knitted gloves and a beanie on a wooden chair, soft sunlight", "毛線圍巾、手套與帽子"),
    ("cold-tea-02", "暖暖早安", "a clay teapot pouring hot tea into a cup, steam rising, winter morning window", "陶壺倒出熱茶"),
    ("cold-ginger-01", "喝杯熱茶 暖暖身", "a glass cup of hot ginger tea with sliced ginger and red dates, steam", "薑茶與紅棗"),
    ("cold-heater-01", "早安 記得保暖", "a cozy room with a warm glowing heater, a knitted blanket and a cup of tea", "暖爐、毛毯與熱茶"),
   ],
   wishes=["早安！天冷了，出門記得多穿一件、戴圍巾。",
           "天氣變冷，喝杯熱茶暖暖身子，祝您平安健康。",
           "早晚溫差大，衣服帶一件，別著涼了。"]),
  dict(id="cold-front", h2="寒流早安圖", intro="寒流、冷氣團來的時候，提醒長輩保暖最實在。",
   images=[
    ("cold-front-01", "寒流來了 注意保暖", "frosty pine trees on a cold Taiwanese mountain morning, thin mist, pale sunrise", "結霜的松樹與山間晨霧"),
    ("cold-snow-01", "寒流早安", "light snow on mountain pine trees at sunrise, high mountains of Taiwan", "高山上的雪與日出"),
    ("cold-snow-02", "天冷 保重身體", "red camellia flowers covered with frost in the morning", "結霜的紅山茶花"),
    ("cold-rain-01", "天冷下雨 出門小心", "a red umbrella on a rainy cold street with soft lights, raindrops", "雨天裡的紅雨傘"),
    ("cold-frost-01", "早安 平安健康", "frost on plum blossom branches in golden morning sunlight", "晨光中結霜的梅枝"),
   ],
   wishes=["寒流來了，晚上睡覺蓋好被子，注意保暖。",
           "天冷又下雨，出門帶傘、走路慢慢來。",
           "寒流早安！頭、脖子、手腳都要顧好，別著涼。"]),
  dict(id="cozy", h2="冬天暖心問候", intro="天冷的時候，一句「吃飽穿暖」就是最好的祝福。",
   images=[
    ("cold-soup-01", "吃飽穿暖", "a steaming hot pot of chicken soup on a table in a warm home, winter evening glow", "一鍋熱騰騰的雞湯"),
    ("cold-plum-01", "冬日平安", "red plum blossoms in the snow, traditional Chinese ink wash painting style", "水墨畫風的雪中紅梅"),
    ("cold-sun-01", "冬陽暖暖 早安", "warm winter sunshine through a window onto potted flowers and a cup of tea", "冬日陽光照著窗邊盆花"),
    ("cold-name-01", "媽媽 天冷多穿點", "a red knitted scarf and a cup of hot tea, warm golden morning light", "紅圍巾與熱茶"),
   ],
   wishes=["冬天的太陽暖暖的，祝您今天心情也暖暖的。",
           "媽，天冷多穿點，記得吃飽穿暖。",
           "冬日平安，祝您身體健康、天天開心。"]),
 ],
 faq=[
  ("寒流來的時候，可以提醒長輩什麼？",
   ["多穿一件、圍巾帽子戴起來，頭、脖子、手腳都要保暖；早晚溫差大，出門前看一下氣象。身體如果不舒服，記得找醫師。"]),
  ("天冷早安圖可以免費存下來嗎？",
   ["可以。這頁的圖都是早安圖王用 AI 做的，歡迎長按圖片存到手機，再傳給親友。"]),
  ("怎麼做一張打上名字的天冷早安圖？",
   ["加 LINE 好友「早安圖王」，點選單「早安」或「自己打字」，輸入「媽媽早安，天冷多穿一件」，大約 20 秒就做好。加好友先送 5 張免費。"]),
 ],
 related=["dongzhi", "christmas", "deity", "generator"],
),

# ───────────────────────────── 6. 神明早安圖 ─────────────────────────────
dict(
 slug="deity", kind="deity", crumb="神明早安圖", short="神明早安圖", emoji="🙏",
 title="神明早安圖 2026｜觀音、媽祖、關公、土地公、財神｜早安圖王",
 desc="2026 神明早安圖：觀世音菩薩、媽祖、關聖帝君、土地公、財神爺、彌勒佛，6 尊神佛共 18 張，莊重好看、繁體中文，可長按存圖轉傳，每尊附適合的祝福語。加 LINE 好友免費做 5 張。",
 h1="神明早安圖",
 lead=["想傳一張神明保佑的早安圖給親友？這頁有 <b>觀世音菩薩、媽祖、關聖帝君、土地公、財神爺、彌勒佛</b> 6 尊神佛，共 18 張神明早安圖。",
       "每一尊都附上適合的祝福語，可以直接複製。歡迎長按存圖，以恭敬的心分享給親友。"],
 sections=[
  dict(id="guanyin", h2="觀世音菩薩早安圖", intro="白衣觀音、蓮花座，祝福平安、慈悲護佑。",
   images=[
    ("deity-guanyin-01", "早安 平安吉祥", "Guanyin Bodhisattva in flowing white silk robes seated serenely on a pink lotus throne, holding a willow branch and a gold vase, serene compassionate downcast eyes, luminous golden halo, auspicious clouds", "白衣觀世音菩薩坐在蓮花座上"),
    ("deity-guanyin-02", "觀音護佑 平安", "Guanyin Bodhisattva in white robes standing on a lotus above calm water, holding a willow branch, golden halo, soft morning light", "站在蓮花上的觀世音菩薩"),
    ("deity-guanyin-03", "慈悲喜樂", "Guanyin Bodhisattva in white robes with a gentle compassionate expression among pink lotus flowers, golden halo, temple mural style", "蓮花環繞的觀世音菩薩"),
   ],
   wishes=["早安！願觀音菩薩保佑您平安健康、事事順心。",
           "早安，心存善念，日日平安。",
           "願菩薩慈悲護佑，闔家平安、喜樂自在。"]),
  dict(id="mazu", h2="媽祖早安圖", intro="海上守護神，祝福出入平安、闔家安康。",
   images=[
    ("deity-mazu-01", "媽祖保佑 平安", "Goddess Mazu in imperial red and gold ceremonial robes wearing the black mian guan crown with jade tassels, peaceful blue ocean waves and distant sailing junks, red temple lanterns, golden halo, Taiwanese folk temple painting", "身穿紅金禮袍的媽祖與海上帆船"),
    ("deity-mazu-02", "早安 出入平安", "Goddess Mazu in red and gold robes with the mian guan crown, standing on auspicious clouds above calm sea at sunrise, golden halo", "日出海上祥雲中的媽祖"),
    ("deity-mazu-03", "風調雨順", "Goddess Mazu in imperial robes seated in a Taiwanese temple with red lanterns and incense smoke, golden halo, reverent", "廟中端坐的媽祖與紅燈籠"),
   ],
   wishes=["早安！媽祖保佑，出入平安、全家健康。",
           "願媽祖庇佑，風調雨順、闔家平安。",
           "早安，祝您今天一路平安、順順利利。"]),
  dict(id="guangong", h2="關公早安圖", intro="關聖帝君忠義正直，祝福事業順利、正氣滿滿。",
   images=[
    ("deity-guangong-01", "忠義護佑 早安", "Guan Gong deity in emerald green imperial robes with a ruddy red face and a long flowing black beard, holding the Spring and Autumn Annals book, dignified righteous expression, golden halo", "綠袍紅臉、手持春秋的關聖帝君"),
    ("deity-guangong-02", "早安 事業順利", "Guan Gong deity in green robes and golden armor with a long black beard, holding the Green Dragon Crescent Blade upright, dignified, golden halo, auspicious clouds", "手持青龍偃月刀的關聖帝君"),
    ("deity-guangong-03", "正氣平安", "Guan Gong deity seated on a temple throne in green robes with a long black beard, red face, golden halo, temple lanterns", "端坐廟中的關聖帝君"),
   ],
   wishes=["早安！關聖帝君護佑，事業順利、正氣滿滿。",
           "忠義長存，祝您今天做事順順利利。",
           "早安，祝您平安健康、貴人相助。"]),
  dict(id="tudigong", h2="土地公早安圖", intro="福德正神慈祥和氣，祝福平安發財、生意興隆。",
   images=[
    ("deity-tudigong-01", "福德正神 保佑", "Tudigong the Earth God as a kindly elderly deity with a long silver white beard, bright red official robe with gold trim and a black official hat, holding a gold yuanbao ingot and a wooden staff, gentle benevolent smile, Taiwanese folk art", "白鬍子、手拿元寶的土地公"),
    ("deity-tudigong-02", "早安 生意興隆", "Tudigong the Earth God smiling kindly, red robe, holding a gold ingot, surrounded by gold coins and auspicious clouds", "金幣祥雲環繞的土地公"),
    ("deity-tudigong-03", "福氣滿滿", "Tudigong the Earth God with silver beard in a small Taiwanese shrine with red lanterns and offerings of fruit, warm light", "小廟裡的土地公與供品"),
   ],
   wishes=["早安！土地公保佑，生意興隆、福氣滿門。",
           "福德正神護佑，祝您平安發財、事事如意。",
           "早安，祝您福氣滿滿、闔家安康。"]),
  dict(id="caishen", h2="財神早安圖", intro="財神爺招財進寶，初五迎財神也很適合傳。",
   images=[
    ("deity-caishen-01", "早安 財源廣進", "Caishen the God of Wealth in an ornate red and gold embroidered imperial robe, holding a treasure bowl overflowing with gold ingots and coins, gold coins falling around, auspicious clouds", "手捧聚寶盆的財神爺"),
    ("deity-caishen-02", "招財進寶", "Caishen the God of Wealth smiling, red and gold robe, holding a gold ingot, surrounded by red lanterns and plum blossoms", "紅燈籠與梅花旁的財神爺"),
    ("deity-caishen-03", "財神到 早安", "Caishen the God of Wealth on auspicious clouds with gold coins raining down, golden halo, festive red background", "金幣如雨的財神爺"),
   ],
   wishes=["早安！財神到，祝您財源廣進、荷包滿滿。",
           "招財進寶，祝您今天好運旺旺來。",
           "早安，祝您生意興隆、年年有餘。"]),
  dict(id="maitreya", h2="彌勒佛早安圖", intro="彌勒佛笑口常開，祝福歡喜自在、天天開心。",
   images=[
    ("deity-maitreya-01", "笑口常開", "Maitreya Buddha as a joyful laughing monk with a broad happy smile and a large round belly, loose orange monk robes, holding prayer beads, golden auspicious light and lotus flowers", "笑容滿面、大肚子的彌勒佛"),
    ("deity-maitreya-02", "早安 歡喜自在", "Maitreya Buddha sitting happily with a cloth sack, broad smile, golden light and lotus flowers, temple mural style", "背著布袋、笑呵呵的彌勒佛"),
    ("deity-maitreya-03", "知足常樂", "Maitreya Buddha laughing joyfully under a blossoming tree, orange robes, golden halo, auspicious clouds", "花樹下開懷大笑的彌勒佛"),
   ],
   wishes=["早安！笑口常開，好運自然來。",
           "歡喜自在、知足常樂，祝您天天開心。",
           "早安，願您煩惱少一點、笑容多一點。"]),
 ],
 faq=[
  ("早安圖王可以做哪幾尊神明的圖？",
   ["六尊：<b>觀世音菩薩、媽祖、關聖帝君、土地公、財神爺、彌勒佛</b>。加 LINE 好友「早安圖王」後，點選單「神佛加持」選一尊，再打上名字或祝福話就行。加好友先送 5 張免費。"]),
  ("神明早安圖可以加上自己的祝福話嗎？",
   ["可以。例如「觀音保佑 美華姊平安健康」「財神到 阿明生意興隆」，會寫在圖上的題字區。"]),
  ("傳神明圖給別人，會不會不太好？",
   ["神明早安圖是一份祝福的心意。選對方平常信仰的神明，搭配平安、健康的祝福話就很得體；不要拿神明圖開玩笑。這頁的圖都依傳統廟宇畫風製作，莊重不搞笑。"]),
  ("這些神明圖可以免費存下來嗎？",
   ["可以。這頁的圖都是早安圖王用 AI 做的，歡迎長按圖片存到手機，以恭敬的心分享給親友。"]),
 ],
 related=["chinese-new-year", "cold-weather", "generator", "dongzhi"],
),

# ───────────────────────────── 7. 過年（2027 羊年） ─────────────────────────────
dict(
 slug="chinese-new-year", kind="cny", crumb="過年祝福圖", short="2027 羊年過年祝福圖", emoji="🧧",
 title="2027 羊年過年祝福圖｜新年快樂圖片、除夕初一長輩圖｜早安圖王",
 desc="2027 羊年過年：除夕 2 月 5 日（五）、大年初一 2 月 6 日（六）。16 張羊年新年快樂圖片、除夕圍爐圖、初一早安圖與拜年長輩圖，附可複製的羊年吉祥話。加 LINE 好友免費做 5 張打上名字的。",
 h1="2027 羊年過年祝福圖",
 lead=["2027 年是<b>羊年</b>：除夕是 <b>2 月 5 日（星期五）</b>，大年初一是 <b>2 月 6 日（星期六）</b>。",
       "這頁有 16 張羊年新年快樂圖片、除夕圍爐圖、初一早安圖和拜年長輩圖，還有可以直接複製的吉祥話。歡迎長按存圖，傳給親友拜年。"],
 sections=[
  dict(id="goat", h2="羊年新年快樂圖", intro="金色小羊、紅燈籠、春聯，喜氣洋洋。",
   images=[
    ("cny-goat-01", "羊年行大運", "a cute golden sheep figurine with red lanterns and plum blossoms, red and gold background", "金色小羊、紅燈籠與梅花"),
    ("cny-goat-02", "三羊開泰", "three cute golden sheep figurines on a red festive table with gold coins and lanterns", "三隻金色小羊與金幣"),
    ("cny-goat-03", "喜氣洋洋", "a cute white sheep figurine wearing a red scarf among red envelopes and firecrackers", "戴紅圍巾的白色小羊與紅包"),
    ("cny-goat-04", "新年快樂", "red envelopes, gold coins and firecrackers on a red silk background with lanterns", "紅包、金幣與鞭炮"),
    ("cny-goat-05", "恭賀新禧", "a traditional red wooden door with round gold door knockers, red lanterns hanging, gold accents, no other writing", "掛著紅燈籠的紅色大門"),
    ("cny-goat-06", "吉祥如意", "blooming red peonies and plum blossoms with a small golden sheep ornament, red and gold", "紅牡丹、梅花與金色小羊"),
   ],
   wishes=["新年快樂！羊年行大運，祝您身體健康、萬事如意。",
           "三羊開泰、喜氣洋洋，祝您全家平安、福氣滿滿。",
           "恭賀新禧，祝您新的一年吉祥如意、心想事成。"]),
  dict(id="eve", h2="除夕圍爐圖", intro="除夕（2 月 5 日）晚上圍爐，祝福全家團圓、年年有餘。",
   images=[
    ("cny-eve-01", "除夕快樂 闔家團圓", "a round table full of Chinese New Year dishes with a hot pot in the center, red lanterns, no people", "擺滿年菜與火鍋的圓桌"),
    ("cny-eve-02", "圍爐團圓", "a steaming hot pot surrounded by plates of food on a red tablecloth, warm festive light", "熱騰騰的圍爐火鍋"),
    ("cny-eve-03", "年年有餘", "a whole steamed fish on a festive plate with red decorations and gold coins", "一整條蒸魚象徵年年有餘"),
    ("cny-eve-04", "除夕平安", "red lanterns glowing at night over a traditional Taiwanese courtyard house, festive", "夜裡紅燈籠高掛的三合院"),
   ],
   wishes=["除夕快樂！闔家團圓，祝您年年有餘。",
           "圍爐吃飽飽，祝您全家平安、身體健康。",
           "除夕夜，祝您守歲平安，明年更好。"]),
  dict(id="day1", h2="初一早安圖", intro="大年初一（2 月 6 日）早上，傳一張新春早安圖拜年。",
   images=[
    ("cny-day1-01", "新春早安", "blooming plum blossoms and red peonies in golden morning sunlight, red lanterns", "晨光中的梅花牡丹與燈籠"),
    ("cny-day1-02", "初一早安 萬事如意", "a red lantern and plum blossom branch against a golden sunrise sky", "日出天空下的紅燈籠與梅枝"),
    ("cny-day1-03", "新年早安 身體健康", "a tray of mandarin oranges and red envelopes in the morning sunlight, festive", "一盤橘子與紅包"),
   ],
   wishes=["初一早安！新春如意，祝您一整年順順利利。",
           "新年早安，祝您身體健康、笑口常開。",
           "大年初一，祝您大吉大利、好運連連。"]),
  dict(id="elder", h2="拜年長輩圖", intro="給爸媽、阿公阿嬤拜年，講健康長壽最貼心。",
   images=[
    ("cny-elder-01", "恭喜發財", "gold ingots and red envelopes overflowing from a treasure bowl, red lanterns, gold sparkles", "聚寶盆裡滿出來的金元寶與紅包"),
    ("cny-elder-02", "身體健康 萬事如意", "red peonies and pink longevity peach buns with gold decorations, festive red", "紅牡丹與壽桃"),
    ("cny-name-01", "阿公阿嬤 新年快樂", "red lanterns, plum blossoms and a golden sheep ornament, warm festive glow", "紅燈籠、梅花與金色小羊"),
   ],
   wishes=["祝阿公阿嬤新年快樂、身體健康、長命百歲。",
           "爸、媽，新年快樂！祝你們平安健康、天天開心。",
           "恭喜發財，祝您新的一年財源滾滾。"]),
 ],
 schedule=[
  ("小年夜", "2 月 4 日（四）", "大掃除、準備年菜"),
  ("除夕", "2 月 5 日（五）", "圍爐、守歲、發紅包"),
  ("大年初一", "2 月 6 日（六）", "拜年、走春"),
  ("初二", "2 月 7 日（日）", "回娘家"),
  ("初四", "2 月 9 日（二）", "接神"),
  ("初五", "2 月 10 日（三）", "迎財神、開市"),
 ],
 faq=[
  ("2027 年過年是哪幾天？",
   ["2027 年小年夜是 2 月 4 日（星期四），除夕是 <b>2 月 5 日（星期五）</b>，大年初一是 <b>2 月 6 日（星期六）</b>，初五迎財神是 2 月 10 日（星期三）。2027 年農曆十二月只有 29 天，除夕是臘月廿九。實際放假日請以行政院人事行政總處公告為準。"]),
  ("2027 年是什麼年？",
   ["2027 年是<b>羊年</b>（農曆丁未年）。常用的羊年吉祥話有「三羊開泰」「喜氣洋洋」「羊年行大運」「吉祥如意」。"]),
  ("怎麼做一張打上名字的過年圖？",
   ["加 LINE 好友「早安圖王」，過年前約兩週起，選單「節慶圖」裡就有「過年大吉」，選好風格再打上「阿公阿嬤新年快樂」；也可以點「自己打字」。加好友先送 5 張免費。"]),
  ("這些過年圖可以免費存下來嗎？",
   ["可以。這頁的圖都是早安圖王用 AI 做的，歡迎長按圖片存到手機，再傳給親友拜年。"]),
 ],
 related=["new-year", "deity", "dongzhi", "generator"],
),
]

TOPIC_BY_SLUG = {t["slug"]: t for t in TOPICS}


def iter_images(topic):
    """依序回傳 (section, 檔名, 圖上文字, 英文場景, 中文描述, kind)。"""
    for sec in topic["sections"]:
        for img in sec["images"]:
            f, t, s, d = img[:4]
            kind = img[4] if len(img) > 4 else topic["kind"]
            yield sec, f, t, s, d, kind
