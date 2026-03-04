import json
from datetime import datetime

with open('alex_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 按日期排序（最新在前）
data['videos'].sort(key=lambda x: x['date'], reverse=True)

# 重新整理技巧順序
all_techniques = []
for v in data['videos']:
    all_techniques.extend(v.get('techniques', []))

data['techniques'] = all_techniques

# 更新時間
data['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')

with open('alex_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('✅ 已按日期排序')
print('\n最新5部影片:')
for v in data['videos'][:5]:
    print(f'  - {v["title"][:45]}... ({v["date"]})')
