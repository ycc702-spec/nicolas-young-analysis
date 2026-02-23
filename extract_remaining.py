#!/usr/bin/env python3
"""
提取剩餘影片字幕
"""

import json
import time
import urllib.request

API_KEY = "sk_RjQ61Oo1PENPpEGEKQwNjGhmKHYEOtD1ReXLAWPEwgM"

VIDEOS = [
    ("l7_3brMj_Yo", "全球市場崩盤"),
    ("IijbvUP-J5g", "高市早苗日本崩盤伊朗戰爭"),
    ("zH2Kyex5Dgs", "日本崩盤一生一次"),
    ("6IGt19-CzmU", "川普下一步"),
    ("0C2lF8pKwlI", "高市早苗3年財富"),
    ("0-0_kHauSrk", "跟著川普發財"),
    ("c5PHFkviXYg", "黃仁勳發話"),
    ("h3r6-jfu7k0", "這會讓我們發財"),
    ("TBTLMn6lvNA", "馬杜羅被捕"),
    ("IlsHGywzSf4", "2026新開始"),
]

def extract(video_id):
    url = f"https://transcriptapi.com/api/v2/youtube/transcript?video_url={video_id}&format=text&include_timestamp=false&send_metadata=true"
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {API_KEY}'})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return {"error": str(e)}

print("🎬 提取剩餘影片字幕\n")

results = {}
for i, (vid, title) in enumerate(VIDEOS, 1):
    print(f"[{i}/{len(VIDEOS)}] {title}...", end=" ", flush=True)
    result = extract(vid)
    
    if "transcript" in result:
        print(f"✅ ({len(result['transcript'])} 字)")
        results[vid] = {
            "title": title,
            "success": True,
            "transcript": result["transcript"][:5000],  # 儲存前5000字
            "metadata": result.get("metadata", {})
        }
    else:
        print(f"❌ {result.get('error', '未知錯誤')}")
        results[vid] = {"title": title, "success": False, "error": result.get("error")}
    
    time.sleep(3)  # 避免限流

# 儲存結果
with open("/root/.openclaw/workspace/nicolas-young-analysis/all_transcripts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n💾 已儲存到 all_transcripts.json")
