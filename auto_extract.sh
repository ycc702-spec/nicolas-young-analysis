#!/bin/bash
# Nicolas Young 自動字幕提取系統
# 每週日 21:00 自動執行

set -e

API_KEY="${TRANSCRIPT_API_KEY:-sk_RjQ61Oo1PENPpEGEKQwNjGhmKHYEOtD1ReXLAWPEwgM}"
PLAYLIST_ID="PL682mLo5auWcfHS9I2Op4m4iOBdUZb7k4"
OUTPUT_DIR="/root/.openclaw/workspace/nicolas-young-analysis/transcripts"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$OUTPUT_DIR"

echo "🎬 Nicolas Young 自動提取系統"
echo "================================"
echo "時間: $(date)"
echo ""

# 1. 獲取播放清單所有影片
echo "📋 步驟 1: 獲取播放清單..."
yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://youtube.com/playlist?list=$PLAYLIST_ID" 2>/dev/null > /tmp/playlist.txt || {
    echo "⚠️ 無法獲取播放清單，使用預設清單"
    cat > /tmp/playlist.txt << 'EOF'
YU-Ci7VRQA0|Tariffs Blocked — A Get Rich Moment?
sNWNCg1s4-E|Strangest Market Signal Yet… Get Rich Opportunity?
4rVfvvk5IbQ|Where Will Sanae Takaichi Lead Japan's Stock Market?
SI6V4Oi2Y4Y|SpaceX IPO Strategy: How I'm Positioning to Get Rich
l7_3brMj_Yo|Global Market Crash: Ordinary People's Chance to Get Rich
bsgjD3Uf8T4|Gold & Silver Collapse: Only Trump Can Stop It
IijbvUP-J5g|Takaichi, Japan Collapse, Iran War — A Rare Chance to Get Rich
zH2Kyex5Dgs|Japan's Collapse: A Once-in-a-Lifetime Wealth Event
6IGt19-CzmU|Trump's Next Move Could Make You Rich
0C2lF8pKwlI|Sanae Takaichi Just Revealed the Next 3-Year Wealth Play
0-0_kHauSrk|To Get Rich, You Have to Follow Trump
c5PHFkviXYg|Jensen Huang has spoken — how do we get rich with him?
h3r6-jfu7k0|This will make us rich
TBTLMn6lvNA|How can we get rich after Maduro is arrested?
IlsHGywzSf4|2026年新的開始
EOF
}

TOTAL=$(wc -l < /tmp/playlist.txt)
echo "找到 $TOTAL 部影片"
echo ""

# 2. 逐一提取字幕
echo "📝 步驟 2: 提取字幕..."
SUCCESS=0
FAILED=0

while IFS='|' read -r VIDEO_ID TITLE; do
    echo -n "提取: ${TITLE:0:40}... "
    
    RESPONSE=$(curl -s -H "Authorization: Bearer $API_KEY" \
        "https://transcriptapi.com/api/v2/youtube/transcript?video_url=$VIDEO_ID&format=text&include_timestamp=false" 2>/dev/null)
    
    if echo "$RESPONSE" | grep -q '"transcript"'; then
        # 儲存成功
        echo "$RESPONSE" > "$OUTPUT_DIR/${VIDEO_ID}_${DATE}.json"
        echo "✅"
        ((SUCCESS++))
    else
        echo "❌"
        ((FAILED++))
    fi
    
    # 避免 rate limit
    sleep 1
done < /tmp/playlist.txt

# 3. 生成報告
echo ""
echo "================================"
echo "🎉 提取完成!"
echo "✅ 成功: $SUCCESS"
echo "❌ 失敗: $FAILED"
echo "📁 儲存位置: $OUTPUT_DIR"
echo ""

# 4. 通知（可選）
if [ $SUCCESS -gt 0 ]; then
    echo "📊 已提取 $SUCCESS 部影片字幕，請查看分析報告"
fi
