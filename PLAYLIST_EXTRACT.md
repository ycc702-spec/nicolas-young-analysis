# Nicolas Young 財經 - 播放清單分析

## 播放清單資訊
- **連結**: https://youtube.com/playlist?list=PL682mLo5auWcfHS9I2Op4m4iOBdUZb7k4
- **名稱**: Nicolas Young 財經
- **頻道**: @nicolasyounglive

---

## 🎯 快速收集方法

### 步驟 1: 打開播放清單
點擊上面的連結，或複製到瀏覽器開啟

### 步驟 2: 顯示所有影片
在 YouTube 頁面上，捲動到底部載入所有影片

### 步驟 3: 使用瀏覽器控制台提取
按 **F12** → 選擇 **Console** → 貼上以下程式碼：

```javascript
// 提取播放清單中的所有影片資訊
const videos = [];
document.querySelectorAll('ytd-playlist-video-renderer').forEach((el, index) => {
    const title = el.querySelector('#video-title')?.textContent?.trim();
    const link = el.querySelector('#video-title')?.href;
    const date = el.querySelector('.style-scope.ytd-video-meta-block')?.textContent?.trim();
    if (title) {
        videos.push(`${index + 1}. ${title} | ${link} | ${date}`);
    }
});
console.log(videos.join('\n'));
copy(videos.join('\n'));
```

然後 **Ctrl+V** 貼給我！

---

## 替代方法: 手動貼上

如果上面的方法不行，請直接貼上影片標題：

```
1. [影片標題 1]
2. [影片標題 2]
3. [影片標題 3]
...
16. [影片標題 16]
```

---

## 分析準備

收到清單後，我會立即：

1. **📝 阿Prompt** - 為每部影片設計分析指令
2. **🔍 狗仔隊** - 補充影片詳細資訊
3. **💰 老K** - 執行財經分析
4. **📊 數據妹** - 整理成結構化資料
5. **💻 碼農** - 更新 GitHub Pages

---

**現在就使用上面的方法提取清單給我！** 🚀
