import json
from datetime import datetime

new_video = {
    "id": "RhLpV6QDBFE",
    "title": "OpenClaw is 100x better with this tool (Mission Control)",
    "url": "https://youtube.com/watch?v=RhLpV6QDBFE",
    "date": "2026-03-03",
    "summary": "Alex Finn 介紹 Mission Control 概念，這是一個為 OpenClaw 量身打造的自定義儀表板，讓 OpenClaw 能即時建立所需的任何工具。影片詳細展示三個關鍵工具：任務板（追蹤 OpenClaw 活動）、日曆（確認排程任務和 cron jobs）、專案螢幕（管理主要專案進度）。所有工具都透過簡單提示詞建立，無需程式碼。",
    "key_points": [
        "Mission Control 是為 OpenClaw 設計的自定義儀表板，允許即時建立任何工具",
        "完全自定義：所有工具由 OpenClaw 自行建立，非預設或下載",
        "零程式碼：僅需簡單提示詞即可建立",
        "任務板：看板模式追蹤 OpenClaw 活動，即時活動動態顯示每一步操作",
        "心跳檢查：OpenClaw 每次心跳時檢查任務板，自動執行積壓任務",
        "日曆螢幕：顯示所有 cron jobs 和排程任務，確認 OpenClaw 主動性",
        "專案螢幕：追蹤主要專案進度，避免分心",
        "反向提示技巧：詢問 OpenClaw 如何推進專案",
        "建立提示：使用 Next.js 和 Linear 風格"
    ],
    "tags": ["OpenClaw", "Mission Control", "任務板", "日曆", "專案管理", "Cron Jobs", "Agent 架構", "零程式碼", "反向提示", "儀表板"],
    "techniques": [
        {
            "title": "Mission Control 自定義儀表板架構",
            "description": "為 OpenClaw 建立中央儀表板，作為所有工具的統一入口。由 OpenClaw 自行建立和維護，允許即時添加新工具，提供對 Agent 活動的完全可視性。",
            "priority": "高",
            "apply_to_system": "為我們的系統建立類似的 Mission Control 儀表板，整合任務追蹤、日曆排程、專案管理等功能。"
        },
        {
            "title": "看板式任務追蹤與心跳檢查",
            "description": "使用看板介面追蹤 OpenClaw 及其子代理的所有任務。關鍵創新是心跳檢查機制：Agent 在每次心跳時自動檢查任務板，執行積壓任務。",
            "priority": "高",
            "apply_to_system": "在我們的系統中實現任務板功能，讓 Agent 在每次心跳時檢查並執行分配的任務。"
        },
        {
            "title": "日曆視覺化確認 Agent 主動性",
            "description": "建立日曆螢幕顯示所有排程任務和 cron jobs，解決 Agent 承諾執行任務卻未實際執行的問題。",
            "priority": "高",
            "apply_to_system": "為我們的 cron job 系統建立視覺化日曆，顯示所有排程任務的執行時間和狀態。"
        },
        {
            "title": "專案導向的反向提示技巧",
            "description": "利用專案螢幕進行反向提示，主動詢問 Agent 如何推進主要專案，將 Agent 從被動執行轉為主動建議。",
            "priority": "中",
            "apply_to_system": "在我們的專案管理功能中整合反向提示機制，讓 Agent 能主動建議下一步行動。"
        },
        {
            "title": "自然語言工具生成",
            "description": "透過簡單的自然語言提示詞，讓 OpenClaw 即時建立所需工具，消除工具建設的技術門檻。",
            "priority": "中",
            "apply_to_system": "強化我們系統的自然語言理解能力，讓用戶能用簡單描述要求建立自定義工具。"
        }
    ]
}

with open('alex_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

exists = any(v['id'] == new_video['id'] for v in data['videos'])
if exists:
    print('影片已存在')
else:
    data['videos'].append(new_video)
    data['techniques'].extend(new_video['techniques'])
    data['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('alex_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print('已新增影片:', new_video['title'][:40])
    print('總影片數:', len(data['videos']))
    print('總技巧數:', len(data['techniques']))
