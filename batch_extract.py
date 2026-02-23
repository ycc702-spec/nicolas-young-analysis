#!/usr/bin/env python3
"""
Nicolas Young 播放清單批量字幕提取器
"""

import json
import os
import time
from datetime import datetime

# 播放清單影片（從 yt-dlp 提取）
PLAYLIST_VIDEOS = [
    {"id": "YU-Ci7VRQA0", "title": "Tariffs Blocked — A Get Rich Moment?", "analyzed": True},
    {"id": "sNWNCg1s4-E", "title": "Strangest Market Signal Yet… Get Rich Opportunity?", "analyzed": False},
    {"id": "4rVfvvk5IbQ", "title": "Where Will Sanae Takaichi Lead Japan's Stock Market?", "analyzed": False},
    {"id": "SI6V4Oi2Y4Y", "title": "SpaceX IPO Strategy: How I'm Positioning to Get Rich", "analyzed": False},
    {"id": "l7_3brMj_Yo", "title": "Global Market Crash: Ordinary People's Chance to Get Rich", "analyzed": False},
    {"id": "bsgjD3Uf8T4", "title": "Gold & Silver Collapse: Only Trump Can Stop It", "analyzed": False},
    {"id": "IijbvUP-J5g", "title": "Takaichi, Japan Collapse, Iran War — A Rare Chance to Get Rich", "analyzed": False},
    {"id": "zH2Kyex5Dgs", "title": "Japan's Collapse: A Once-in-a-Lifetime Wealth Event", "analyzed": False},
    {"id": "6IGt19-CzmU", "title": "Trump's Next Move Could Make You Rich", "analyzed": False},
    {"id": "0C2lF8pKwlI", "title": "Sanae Takaichi Just Revealed the Next 3-Year Wealth Play", "analyzed": False},
    {"id": "0-0_kHauSrk", "title": "To Get Rich, You Have to Follow Trump", "analyzed": False},
    {"id": "c5PHFkviXYg", "title": "Jensen Huang has spoken — how do we get rich with him?", "analyzed": False},
    {"id": "h3r6-jfu7k0", "title": "This will make us rich", "analyzed": False},
    {"id": "TBTLMn6lvNA", "title": "How can we get rich after Maduro is arrested?", "analyzed": False},
    {"id": "IlsHGywzSf4", "title": "2026年新的開始", "analyzed": False},
]

API_KEY = os.environ.get('TRANSCRIPT_API_KEY', 'sk_RjQ61Oo1PENPpEGEKQwNjGhmKHYEOtD1ReXLAWPEwgM')

def extract_transcript(video_id):
    """提取單部影片字幕"""
    import urllib.request
    import urllib.error
    
    url = f"https://transcriptapi.com/api/v2/youtube/transcript?video_url={video_id}&format=text&include_timestamp=false&send_metadata=true"
    
    req = urllib.request.Request(
        url,
        headers={'Authorization': f'Bearer {API_KEY}'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            return {
                'success': True,
                'video_id': video_id,
                'title': data.get('metadata', {}).get('title', 'Unknown'),
                'transcript': data.get('transcript', ''),
                'language': data.get('language', 'unknown')
            }
    except Exception as e:
        return {
            'success': False,
            'video_id': video_id,
            'error': str(e)
        }

def main():
    """主程式：批量提取"""
    print("🎬 Nicolas Young 播放清單批量提取")
    print("=" * 60)
    
    results = []
    
    for i, video in enumerate(PLAYLIST_VIDEOS, 1):
        print(f"\n[{i}/{len(PLAYLIST_VIDEOS)}] 提取: {video['title'][:50]}...")
        
        result = extract_transcript(video['id'])
        results.append(result)
        
        if result['success']:
            print(f"  ✅ 成功 - {len(result['transcript'])} 字")
        else:
            print(f"  ❌ 失敗 - {result.get('error', '未知錯誤')}")
        
        # 避免 rate limit
        if i < len(PLAYLIST_VIDEOS):
            time.sleep(1)
    
    # 儲存結果
    os.makedirs('transcripts', exist_ok=True)
    
    output_file = f"transcripts/nicolas_young_playlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # 統計
    success_count = sum(1 for r in results if r['success'])
    total_chars = sum(len(r.get('transcript', '')) for r in results if r['success'])
    
    print("\n" + "=" * 60)
    print(f"🎉 提取完成!")
    print(f"✅ 成功: {success_count}/{len(PLAYLIST_VIDEOS)}")
    print(f"📝 總字數: {total_chars:,}")
    print(f"💾 儲存: {output_file}")
    
    return results

if __name__ == '__main__':
    main()
