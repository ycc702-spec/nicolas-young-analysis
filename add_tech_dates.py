import json
from datetime import datetime

with open('alex_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 為每個技巧加上來源影片日期
tech_index = 0
for video in data['videos']:
    video_date = video.get('date', '2026-03-04')
    for tech in video.get('techniques', []):
        # 添加來源資訊
        tech['source_video'] = video['title']
        tech['source_date'] = video_date
        tech_index += 1

# 重新整理技巧列表（保持順序）
all_techniques = []
for video in data['videos']:
    all_techniques.extend(video.get('techniques', []))

data['techniques'] = all_techniques

# 儲存
with open('alex_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'✅ 已為 {tech_index} 個技巧添加來源日期')
print('\n範例：')
for t in data['techniques'][:3]:
    print(f"- {t['title'][:40]}... 來源: {t.get('source_date', 'N/A')}")
