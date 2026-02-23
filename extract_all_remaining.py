#!/usr/bin/env python3
"""
繼續提取剩餘影片 - 使用正確的 API Key
"""

import json
import time
import urllib.request

API_KEY = "sk_RjQ61Oo1PENPpEGEKQwNjGhmKHYEOtD1ReXLAWPEwgM"

VIDEOS = [
    ("c5PHFkviXYg", "黃仁勳發話"),
    ("zH2Kyex5Dgs", "日本崩盤一生一次"),
    ("IlsHGywzSf4", "2026新開始"),
    ("l7_3brMj_Yo", "全球市場崩盤"),
    ("IijbvUP-J5g", "高市早苗日本崩盤伊朗戰爭"),
    ("6IGt19-CzmU", "川普下一步"),
    ("0C2lF8pKwlI", "高市早苗3年財富"),
    ("0-0_kHauSrk", "跟著川普發財"),
    ("h3r6-jfu7k0", "這會讓我們發財"),
    ("TBTLMn6lvNA", "馬杜羅被捕"),
]

def extract(video_id):
    url = f"https://transcriptapi.com/api/v2/youtube/transcript?video_url={video_id}&format=text&include_timestamp=false&send_metadata=true"
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {API_KEY}'})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

print("🎬 繼續提取剩餘影片字幕\n")
print("=" * 60)

results = {}
for i, (vid, title) in enumerate(VIDEOS, 1):
    print(f"\n[{i}/{len(VIDEOS)}] {title}")
    print(f"    ID: {vid}")
    
    result = extract(vid)
    
    if "transcript" in result:
        transcript_len = len(result['transcript'])
        print(f"    ✅ 成功 - {transcript_len:,} 字")
        results[vid] = {
            "title": title,
            "success": True,
            "transcript": result["transcript"],
            "metadata": result.get("metadata", {})
        }
    else:
        error_msg = result.get('error', '未知錯誤')
        print(f"    ❌ 失敗 - {error_msg}")
        results[vid] = {"title": title, "success": False, "error": error_msg}
    
    # 等待 2 秒避免 rate limit
    if i < len(VIDEOS):
        time.sleep(2)

# 儲存結果
output_file = "/root/.openclaw/workspace/nicolas-young-analysis/all_transcripts_complete.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# 統計
success_count = sum(1 for r in results.values() if r["success"])
total_chars = sum(len(r.get("transcript", "")) for r in results.values() if r["success"])

print("\n" + "=" * 60)
print(f"🎉 提取完成!")
print(f"✅ 成功: {success_count}/{len(VIDEOS)}")
print(f"📝 總字數: {total_chars:,}")
print(f"💾 儲存: {output_file}")
