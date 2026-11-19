"""主題頁範例圖產生器（gpt-image-2、quality=low、1024×1024 → 800px WebP）。

第一批的生圖腳本沒有進 repo，第二批照 topics.py 的 KINDS 與 tuwang seed_templates 的 prompt 結構重建。
已存在的圖檔會跳過（重做：先刪掉該檔，或用 --only 指定檔名）。

  python _src/gen_topic_images.py --slug caishen --dry-run      # 只印 prompt、不呼叫 API
  python _src/gen_topic_images.py --slug caishen --max-calls 16  # 真的生圖（會花錢）
  python _src/gen_topic_images.py --slug kaigong --only kaigong-daji-02 --max-calls 1

金鑰：環境變數 OPENAI_API_KEY，沒有就讀 C:\\Dev\\work\\tuwang\\.env 的 OPENAI_API_KEY。金鑰不會印出或寫進任何檔案。
每次呼叫都會記在 --log（預設 %TEMP%\\zaoan_imagegen.log），方便統計呼叫次數。
"""
import argparse, base64, datetime, io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from topics import KINDS, TOPIC_BY_SLUG, iter_images

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TUWANG_ENV = r"C:\Dev\work\tuwang\.env"
NO_EXTRA_TEXT = ("The ONLY text in the image is the greeting above. Do NOT add any other Chinese characters, seals, couplets, "
                 "signs, labels or small writing anywhere (not on envelopes, lanterns, pendants, ornaments or the background).")


def build_prompt(kind, text, scene):
    k = KINDS[kind]
    lines = text.split(" ")
    shown = "\n".join(f"「{x}」" for x in lines)
    return "\n".join([
        k["base"],
        f"Scene: {scene}.",
        f"Central text in large, clear traditional Chinese characters (繁體中文), exactly as written, {len(lines)} line(s):\n{shown}",
        f"Text styling: {k['tstyle']}.",
        k["tail"],
        "Aspect ratio: 1:1 (square).",
        "" if k.get("faces") else "NO people's faces.",
        NO_EXTRA_TEXT,
        "Ensure Chinese characters are rendered correctly and are the visual focus.",
    ]).replace("\n\n", "\n")


def api_key():
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    if os.path.exists(TUWANG_ENV):
        for line in open(TUWANG_ENV, encoding="utf8"):
            if line.strip().startswith("OPENAI_API_KEY="):
                v = line.split("=", 1)[1].strip().strip('"').strip("'")
                if v:
                    return v
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--only", default="", help="逗號分隔的檔名（不含副檔名）")
    ap.add_argument("--max-calls", type=int, default=0, help="這次最多呼叫幾次 API（必填，0＝不呼叫）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--log", default=os.path.join(os.environ.get("TEMP", "."), "zaoan_imagegen.log"))
    a = ap.parse_args()
    t = TOPIC_BY_SLUG[a.slug]
    only = set(filter(None, a.only.split(",")))
    out_dir = os.path.join(SITE, t["slug"], "img")
    todo = []
    for sec, f, text, scene, desc, kind in iter_images(t):
        if only and f not in only:
            continue
        if os.path.exists(os.path.join(out_dir, f + ".webp")) and not only:
            continue
        todo.append((f, build_prompt(kind, text, scene)))
    if a.dry_run:
        for f, p in todo:
            print(f"== {f}\n{p}\n")
        print(f"{len(todo)} 張待生（dry-run，未呼叫 API）")
        return
    key = api_key()
    if not key:
        sys.exit("找不到 OPENAI_API_KEY（環境變數或 tuwang/.env），停止。")
    from openai import OpenAI
    from PIL import Image
    client = OpenAI(api_key=key, timeout=180.0, max_retries=0)
    os.makedirs(out_dir, exist_ok=True)
    calls = 0
    for f, p in todo:
        if calls >= a.max_calls:
            print(f"已達 --max-calls {a.max_calls}，停止。剩 {len(todo) - calls} 張。")
            break
        calls += 1
        with open(a.log, "a", encoding="utf8") as lg:
            lg.write(f"{datetime.datetime.now().isoformat(timespec='seconds')}\t{a.slug}\t{f}\n")
        try:
            r = client.images.generate(model="gpt-image-2", prompt=p, quality="low", size="1024x1024")
            im = Image.open(io.BytesIO(base64.b64decode(r.data[0].b64_json))).convert("RGB")
            im.resize((800, 800), Image.LANCZOS).save(os.path.join(out_dir, f + ".webp"), "WEBP", quality=80, method=6)
            print("ok", f)
        except Exception as e:  # 失敗也算一次呼叫，不自動重試
            print("FAIL", f, type(e).__name__, str(e)[:200])
    print(f"本次呼叫 {calls} 次")


if __name__ == "__main__":
    main()
