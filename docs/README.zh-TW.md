<p align="center">
  <img src="../hd-logo.webp" alt="Katawa Shoujo HD Patch - Steam Edition logo" width="420">
</p>

# Katawa Shoujo HD Patch — Steam Edition (1080p)

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1ec-1f1e7.svg" width="20" alt="GB"> <a href="../README.md">English</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1ea-1f1f8.svg" width="20" alt="ES"> <a href="README.es.md">Español</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1eb-1f1f7.svg" width="20" alt="FR"> <a href="README.fr.md">Français</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1ef-1f1f5.svg" width="20" alt="JP"> <a href="README.ja.md">日本語</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e9-1f1ea.svg" width="20" alt="DE"> <a href="README.de.md">Deutsch</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f0-1f1f7.svg" width="20" alt="KR"> <a href="README.ko.md">한국어</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f5-1f1f1.svg" width="20" alt="PL"> <a href="README.pl.md">Polski</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e7-1f1f7.svg" width="20" alt="BR"> <a href="README.pt-BR.md">Português (Brasil)</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f7-1f1fa.svg" width="20" alt="RU"> <a href="README.ru.md">Русский</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e8-1f1f3.svg" width="20" alt="CN"> <a href="README.zh-CN.md">简体中文</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f9-1f1fc.svg" width="20" alt="TW"> <b>繁體中文</b>
</p>

**以 1920×1080 寬螢幕遊玩 Steam 版《Katawa Shoujo》，含 R18 內容。**

這是一個非官方的粉絲修正檔，讓 Four Leaf Studios 的視覺小說 **《Katawa Shoujo》（片輪少女）** 的 Steam 版以
**全高畫質（1920×1080，16:9 寬螢幕）** 執行，而不是原本的 800×600（4:3）。背景、角色立繪、CG、介面和影片都會
替換為高畫質版本。修正檔適用於 Steam 版的 Ren'Py 6.16 引擎，支援全部 11 種語言。

**[下載最新版本](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)**

> 本修正檔移植自 **letow** 的 [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch)。
> 所有高畫質美術素材（背景、立繪、CG、介面、特效和影片）皆來自該專案。完整的致謝名單請見文末。

## 本版本的新內容

以下是本版本獨有、原版高畫質修正檔中沒有的內容：

- **Steam 版全部 11 種語言。** 原版修正檔支援英文、西班牙文、法文和日文，德文和俄文為額外附加。本版本新增了
  韓文、波蘭文、巴西葡萄牙文以及簡體和繁體中文，並包含各語言的 R18 場景。原版修正檔缺少的四張波蘭文漫畫面板
  （`comic_vfx*_pl`）也依照其他語言面板的相同方式製作成高畫質版本。
- **支援 Steam 版。** 高畫質調整（解析度、位置、縮放、平移、介面配置）是疊加在 Steam 版腳本之上，而不是取代
  腳本，因此 Steam 版的功能依然可用：成就、控制器支援、R18 開關以及封裝的語言檔案。
- **高畫質 R18 修正檔。** `r18_hd.rpa` 以相同場景的高畫質版本取代官方的 `r18.rpa`。
- **可捲動的語言選擇畫面。** 保持高畫質配置，並可捲動以容納全部 11 種語言。
- **符合螢幕的視窗。** 遊戲會在螢幕中央開啟一個視窗，大小為桌面可用區域（不含工作列和標題列）的 90%，介於
  1280×720 和 1920×1080 之間，且不會超過螢幕大小。全螢幕模式與以前相同。
- **更新的遊戲基礎。** 以目前的 Steam 版腳本（v1.3.2）為基礎，而不是《Katawa Shoujo》1.3/1.3.1，因此保留了
  遊戲後續的修正。
- **使用封存檔而非零散檔案。** 高畫質素材以兩個 `.rpa` 封存檔提供，安裝和移除修正檔只需新增或刪除檔案。

## 簡介

原版高畫質修正檔是為《Katawa Shoujo》的 StandAlone 版（Ren'Py 6.10）製作的，該版本的成人內容包含在遊戲本體
中。Steam 版執行於較新的 Ren'Py（6.16.5），把這部分內容連同原本的 4:3 美術另外分離為 R18 修正檔
（`r18.rpa`），並加入了自己的功能。因此，原版修正檔會導致 Steam 版當機。

本版本將同樣的高畫質重製帶到 Steam 版，並包含高畫質版 R18 修正檔。

### 畫面變化

本版本只是程式碼移植，沒有加入新的畫面變化：遊戲畫面與原版高畫質修正檔相同。前後比較請參閱[原版 Katawa Shoujo HD Patch 的儲存庫](https://github.com/letow/KatawaShoujoHDPatch)。

## 支援的語言

英文、西班牙文、法文、日文、德文、韓文、波蘭文、巴西葡萄牙文、俄文、簡體中文和繁體中文：Steam 版的全部
11 種語言。

## 安裝

不需要安裝程式。

> **請從 [Releases](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest) 頁面下載修正檔。** 儲存庫中
> 是建置工具；高畫質封存檔（約 660 MB 的 `patch-hd.rpa` 和 `r18_hd.rpa`）只包含在發行版的 zip 中。

1. 從最新發行版下載 [`KS-HD-1.0.2-Steam-Patch.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.2/KS-HD-1.0.2-Steam-Patch.zip)。
   遊玩只需要這一個檔案。另一個檔案 `Assets-For-Building-Only` 僅用於自行建置修正檔。
2. 在 Steam 中右鍵點選 **Katawa Shoujo** > **管理** > **瀏覽本機檔案**。
3. 將 zip 解壓縮到該資料夾（包含 `Katawa Shoujo.exe` 的資料夾）。
4. 出現提示時，選擇 **取代所有檔案**。
5. 從 Steam 啟動遊戲。

**Linux 和 macOS：** 修正檔只取代遊戲資料（腳本和封存檔），這些資料在所有系統上都相同。在 Linux 上步驟完全
一樣。在 macOS 上，**瀏覽本機檔案** 會開啟一個包含遊戲應用程式的資料夾：右鍵點選該應用程式，選擇
**顯示套件內容**，然後把 zip 中的 `game` 資料夾合併到其中的 `game` 資料夾。

不需要官方的 `r18.rpa`。如果它已經在資料夾中，可以保留；遊戲會使用高畫質版本。

**移除方法：** 刪除 `game/patch-hd.rpa` 和 `game/r18_hd.rpa`（如果安裝過 v1.0.0 或 v1.0.1，還有 `game/r18-hd.rpa`），然後在 Steam 中進入
**內容** > **已安裝的檔案** > **驗證遊戲檔案完整性**。

> Steam 更新可能會覆寫已修改的腳本。遇到這種情況，重新解壓縮修正檔即可。

> **請使用 Steam 的預設分支。** 本修正檔適用於遊戲的主要版本（Ren'Py 6.16），暫不支援測試版
> **modern - Ren'Py 8 branch**：如果你選擇了該測試版，請在安裝修正檔前於 **內容** > **Beta 版本** 中切換回
> 預設分支。Ren'Py 8 分支的支援正在開發中。

### 發行版 zip 的內容

| 檔案 | 說明 |
|---|---|
| `game/patch-hd.rpa` | 高畫質背景、立繪、CG、介面、特效和影片。 |
| `game/r18_hd.rpa` | 高畫質版 R18 修正檔，取代官方的 `r18.rpa`。 |
| `game/*.rpyc` | 加入高畫質配置調整的 Steam 版遊戲腳本，涵蓋全部 11 種語言。 |
| `game/presplash.png` | 高畫質修正檔的載入畫面。 |

## 常見問題

**能在 Steam 的「modern - Ren'Py 8 branch」上使用嗎？**
暫時不能，相關支援正在開發中。修正檔是為預設分支（Ren'Py 6.16）製作的，而 Ren'Py 8 測試版使用不同的腳本
格式，在其上安裝本修正檔會導致遊戲損壞。

**需要官方的 R18 修正檔（`r18.rpa`）嗎？**
不需要。`r18_hd.rpa` 已經包含高畫質版 R18 場景，遊戲中關閉這些場景的選項也依然有效。

**它和 letow 的 Katawa Shoujo HD Patch 一樣嗎？**
它使用相同的高畫質美術和場景調整，並移植到了 Steam 版，另外還有「本版本的新內容」中列出的變更。letow 的原版
修正檔是為 StandAlone 版製作的，在 Steam 版上會當機。

**能在 Linux、macOS 或 Steam Deck 上使用嗎？**
應該可以：修正檔只修改遊戲資料，這些資料在所有系統上都相同。不過目前只在 Windows 上測試過，歡迎回報。

**如何恢復原版遊戲？**
刪除 `game/patch-hd.rpa` 和 `game/r18_hd.rpa`，然後在 Steam 中使用 **驗證遊戲檔案完整性**。

## 從原始碼建置

儲存庫包含產生修正檔的程式碼：以資料形式儲存的高畫質變更，以及把這些變更套用到你自己遊戲副本上的工具。儲存庫
不包含遊戲檔案和高畫質美術素材。

這個工具是為了透明度而存在，讓任何人都能確切看到修正檔改了什麼，並重新建置它。移植高畫質修正檔需要從
《Katawa Shoujo》StandAlone 版、Steam 版、官方 `r18.rpa` 以及 StandAlone 版的高畫質修正檔中擷取資訊，並加以
比較，找出高畫質修正檔的每一處變更。這些擷取模組只需要使用一次，因此沒有包含在內：它們的結果儲存在
`kshd/edits` 中。

### AI 的使用

移植過程本身漫長而雜亂，產生了大量一次性的測試程式碼和各種實驗。公開當時手寫的原始工具既不實際，也沒有意義。
因此，本儲存庫的建置工具是使用 Anthropic 的 **Claude（Opus 5.5）** 製作的，以便根據移植得到的資料，乾淨可靠地
建置修正檔。

### 需求

- [Python](https://www.python.org/) 3.9 或更新版本，不需要額外的套件。
- Steam 版《Katawa Shoujo》，**未經修改**且位於預設分支（不是 Ren'Py 8 測試版）。
- 高畫質素材包：[`KS-HD-1.0.2-Assets-For-Building-Only.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.2/KS-HD-1.0.2-Assets-For-Building-Only.zip)（約 700 MB）。

### 建置

1. 複製（clone）或下載本儲存庫。
2. 透過以下兩種方式之一，讓工具讀取遊戲：
   - **在儲存庫中放一份遊戲副本：** 將遊戲資料夾（包含 `Katawa Shoujo.exe` 的資料夾）複製到儲存庫根目錄，並
     命名為 `Katawa Shoujo`。請使用安裝修正檔之前的副本。使用這種方式，Steam 中的安裝可以在建置時保持已安裝
     修正檔的狀態。
   - **使用 Steam 中的安裝：** 如果儲存庫中沒有副本，工具會在你的 Steam 收藏庫中尋找遊戲。如果你已經在那裡
     安裝了本修正檔，請先在 Steam 中執行 **驗證遊戲檔案完整性**。
3. 將 `KS-HD-1.0.2-Assets-For-Building-Only.zip` 放入 `assets` 資料夾，壓縮或解壓縮皆可。
4. 執行：

```bash
python build.py
```

工具會修改腳本，並在 `build.py` 旁邊產生 `KS-HD-1.0.2-Steam-Patch.zip`。這個 zip 就是修正檔，依照「安裝」中的
說明安裝即可。

如果某個腳本與修正檔預期的不一致，建置會停止並指出是哪一個。這種情況發生在遊戲檔案被修改過或屬於其他版本時。

### 運作原理

高畫質修正檔只修改遊戲腳本中的少數內容：解析度、位置、縮放、平移和介面配置，以及「本版本的新內容」中介紹的
視窗大小。這些變更以可讀的資料形式儲存在 `kshd/edits` 中，每個腳本對應一個 JSON 檔案：

- **`code`**：介面程式碼的取代，每一項都記錄了確切的原始文字以及它必須出現的次數，從而能察覺遊戲版本不對，
  而不是套錯修正。
- **`nodes`**：場景陳述式（`show`、`scene` 和 ATL 變換）的變更，透過標籤和原始內容定位，因此同一個檔案適用於
  全部 11 種語言。

| 檔案 | 用途 |
|---|---|
| `build.py` | 尋找遊戲和素材，平行修改腳本並產生修正檔 zip。 |
| `kshd/edits/*.json` | 以資料形式儲存的高畫質變更。 |
| `kshd/patch.py` | 將變更檔案套用到腳本上。 |
| `kshd/tree.py` | 走訪腳本結構，尋找需要修改的程式碼和陳述式。 |
| `kshd/rpyc.py` | 讀取和儲存編譯後的 `.rpyc` 腳本，並保持與 Ren'Py 6.16 相容。 |
| `kshd/rpa.py` | 讀寫 Ren'Py 的 `.rpa` 封存檔。 |

### 高畫質素材包

圖片、影片和 R18 場景存放在與程式碼分開的素材包中，這樣不必改動程式碼就能改進它們。高畫質美術來自 letow 的 [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch)，使用 nagadomi 的 waifu2x 放大。本版本唯一新增的是以相同方式製作的四張波蘭文漫畫面板：

```
presplash.png    載入畫面
hd/              背景、立繪、CG、介面、特效和影片（封裝為 patch-hd.rpa）
r18/             R18 場景及其圖片（封裝為 r18_hd.rpa）
```

要更新美術素材，請把素材包解壓縮到 `assets` 資料夾，保持相同的檔名和資料夾結構取代或新增檔案，然後執行建置。
要分享素材包，請重新壓縮該資料夾並上傳到發行版中。

## 測試與回饋

修正檔通過了 Ren'Py 的 lint 檢查，警告與未修改的 Steam 版遊戲相同。選單、設定、存檔畫面、畫廊、片頭以及若干
劇情和 R18 場景都已在遊戲中檢查過，每一條場景陳述式和每一個圖片定義也都與原版高畫質修正檔進行了比較。不過
《Katawa Shoujo》篇幅很長，並非每條路線、每種語言的每個場景都玩過，因此 **還需要更多測試**。目前只在
Windows 上測試過，特別歡迎 Linux 和 macOS 玩家的回報。

如果發現立繪位置錯誤、CG 被裁切、介面元素錯位或其他問題，請開立 issue，並註明場景、語言，可能的話附上截圖。
也歡迎參與貢獻。

## 授權

這是一個非官方、非商業性的粉絲專案，與 Four Leaf Studios 無關。
遊戲及其素材的所有權利歸各自的權利人所有。

## 致謝

- **[letow](https://github.com/letow)**：[Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch)
  （「Remastered by Letow」）的作者。letow 放大了所有素材，為 16:9 重新設計了介面，並完成了本移植所依據的場景
  調整。
- **[Four Leaf Studios](https://www.katawa-shoujo.com/)**：《Katawa Shoujo》的製作團隊。
- **[nagadomi](https://github.com/nagadomi)**：原版高畫質修正檔所用 AI 放大工具 **waifu2x** 的作者。
- **Novellae Subs**（俄文翻譯）和 **HikariTranslations**（德文翻譯）：在原版高畫質修正檔中署名。
- **Valjean_Lafitte**：在原版高畫質修正檔中作為靈感來源署名。
