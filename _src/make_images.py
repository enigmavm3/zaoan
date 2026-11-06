"""產生 img/og-image.jpg（1200×630 分享圖）與 sample/rich-menu 的 WebP 版本。換範例圖後重跑：python _src/make_images.py"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os as _os
R=_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "img", "")
W,H=1200,630
PAPER=(246,236,215); RED=(177,26,42); INK=(28,22,17); GOLD=(182,134,45); CARD=(255,251,239)
im=Image.new("RGB",(W,H),PAPER); d=ImageDraw.Draw(im)
F=lambda s:ImageFont.truetype("C:/Windows/Fonts/msjhbd.ttc",s)
# 外框
d.rectangle([14,14,W-15,H-15],outline=GOLD,width=3); d.rectangle([24,24,W-25,H-25],outline=RED,width=2)
# 右側樣圖
def card(path,size,xy,rot):
    s=Image.open(R+path).convert("RGB").resize((size,size),Image.LANCZOS)
    b=12; c=Image.new("RGBA",(size+2*b,size+2*b),CARD+(255,)); c.paste(s,(b,b))
    sh=Image.new("RGBA",(c.width+40,c.height+40),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([20,26,c.width+20,c.height+26],fill=(60,40,10,90)); sh=sh.filter(ImageFilter.GaussianBlur(10))
    sh.paste(c,(20,20),c); sh=sh.rotate(rot,resample=Image.BICUBIC,expand=True)
    im.paste(sh,xy,sh)
card("sample-3.jpg",215,(905,42),-6)
card("sample-2.jpg",215,(910,318),5)
card("sample-1.jpg",330,(610,125),-2)
# 印章
d.rounded_rectangle([70,70,170,170],radius=14,fill=RED)
d.text((120,121),"王",font=F(70),fill=(251,239,214),anchor="mm")
d.text((195,88),"早安圖王",font=F(76),fill=INK)
d.text((70,205),"在 LINE 打上名字",font=F(44),fill=INK)
d.text((70,262),"AI 約 20 秒做好專屬祝福圖",font=F(44),fill=RED)
d.text((70,340),"早安圖・長輩圖・生日・節慶・神佛祝福",font=F(28),fill=(61,50,40))
# CTA pill
d.rounded_rectangle([70,410,520,486],radius=38,fill=(0,132,58))
d.text((295,448),"加好友免費送 5 張",font=F(36),fill=(255,255,255),anchor="mm")
d.text((70,520),"LINE ID：@581vndzf　triplehai.com/zaoan",font=F(26),fill=(122,85,18))
im.save(R+"og-image.jpg",quality=86,optimize=True,progressive=True)
# WebP
import os
for f in ["sample-1","sample-2","sample-3","sample-4","rich-menu"]:
    Image.open(R+f+".jpg").save(R+f+".webp","WEBP",quality=80,method=6)
    print(f, os.path.getsize(R+f+".jpg")//1024, "->", os.path.getsize(R+f+".webp")//1024,"KB")
print("og",os.path.getsize(R+"og-image.jpg")//1024)
