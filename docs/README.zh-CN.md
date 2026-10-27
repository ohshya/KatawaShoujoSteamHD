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
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e8-1f1f3.svg" width="20" alt="CN"> <b>简体中文</b> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f9-1f1fc.svg" width="20" alt="TW"> <a href="README.zh-TW.md">繁體中文</a>
</p>

**以 1920×1080 宽屏游玩 Steam 版《Katawa Shoujo》，含 R18 内容。**

这是一个非官方的粉丝补丁，让 Four Leaf Studios 的视觉小说 **《Katawa Shoujo》（片轮少女）** 的 Steam 版以
**全高清（1920×1080，16:9 宽屏）** 运行，而不是原本的 800×600（4:3）。背景、角色立绘、CG、界面和视频都会替换为
高清版本。补丁适用于 Steam 版的 Ren'Py 6.16 引擎，支持全部 11 种语言。

**[下载最新版本](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)**

> 本补丁移植自 **letow** 的 [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch)。
> 所有高清美术素材（背景、立绘、CG、界面、特效和视频）均来自该项目。完整的致谢列表见文末。

## 本版本的新内容

以下是本版本独有、原版高清补丁中没有的内容：

- **Steam 版全部 11 种语言。** 原版补丁支持英语、西班牙语、法语和日语，德语和俄语为额外附加。本版本新增了
  韩语、波兰语、巴西葡萄牙语以及简体和繁体中文，并包含各语言的 R18 场景。原版补丁缺少的四张波兰语漫画面板
  （`comic_vfx*_pl`）也按照其他语言面板的相同方式制作成了高清版本。
- **支持 Steam 版。** 高清调整（分辨率、位置、缩放、平移、界面布局）是叠加在 Steam 版脚本之上，而不是替换
  脚本，因此 Steam 版的功能依然可用：成就、手柄支持、R18 开关以及打包的语言文件。
- **高清 R18 补丁。** `r18_hd.rpa` 以相同场景的高清版本替代官方的 `r18.rpa`。
- **可滚动的语言选择界面。** 保持高清布局，并可滚动以容纳全部 11 种语言。
- **适应屏幕的窗口。** 游戏会在屏幕中央打开一个窗口，大小为桌面可用区域（不含任务栏和标题栏）的 90%，介于
  1280×720 和 1920×1080 之间，且不会超过屏幕大小。全屏模式与以前相同。
- **更新的游戏基础。** 基于当前的 Steam 版脚本（v1.3.2），而不是《Katawa Shoujo》1.3/1.3.1，因此保留了游戏
  后续的修正。
- **使用归档文件而非零散文件。** 高清素材以两个 `.rpa` 归档文件提供，安装和卸载补丁只需添加或删除文件。

## 简介

原版高清补丁是为《Katawa Shoujo》的 StandAlone 版（Ren'Py 6.10）制作的，该版本的成人内容包含在游戏本体中。
Steam 版运行在更新的 Ren'Py（6.16.5）上，把这部分内容连同原本的 4:3 美术单独分离为 R18 补丁（`r18.rpa`），
并加入了自己的功能。因此，原版补丁会导致 Steam 版崩溃。

本版本将同样的高清重制带到 Steam 版，并包含高清版 R18 补丁。

### 画面变化

本版本只是代码移植，没有加入新的画面变化：游戏画面与原版高清补丁相同。前后对比请查看[原版 Katawa Shoujo HD Patch 的仓库](https://github.com/letow/KatawaShoujoHDPatch)。

## 支持的语言

英语、西班牙语、法语、日语、德语、韩语、波兰语、巴西葡萄牙语、俄语、简体中文和繁体中文：Steam 版的全部
11 种语言。

## 安装

无需安装程序。

> **请从 [Releases](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest) 页面下载补丁。** 仓库中是
> 构建工具；高清归档文件（约 660 MB 的 `patch-hd.rpa` 和 `r18_hd.rpa`）只包含在发布的 zip 中。

1. 从最新发布中下载 [`KS-HD-1.0.2-Steam-Patch.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.2/KS-HD-1.0.2-Steam-Patch.zip)。
   游玩只需要这一个文件。另一个文件 `Assets-For-Building-Only` 仅用于自行构建补丁。
2. 在 Steam 中右键点击 **Katawa Shoujo** > **管理** > **浏览本地文件**。
3. 将 zip 解压到该文件夹（包含 `Katawa Shoujo.exe` 的文件夹）。
4. 出现提示时，选择 **替换所有文件**。
5. 从 Steam 启动游戏。

**Linux 和 macOS：** 补丁只替换游戏数据（脚本和归档文件），这些数据在所有系统上都相同。在 Linux 上步骤完全
一样。在 macOS 上，**浏览本地文件** 会打开一个包含游戏应用的文件夹：右键点击该应用，选择 **显示包内容**，
然后把 zip 中的 `game` 文件夹合并到其中的 `game` 文件夹。

不需要官方的 `r18.rpa`。如果它已经在文件夹中，可以保留；游戏会使用高清版本。

**卸载方法：** 删除 `game/patch-hd.rpa` 和 `game/r18_hd.rpa`（如果安装过 v1.0.0 或 v1.0.1，还有 `game/r18-hd.rpa`），然后在 Steam 中进入
**属性** > **已安装文件** > **验证游戏文件的完整性**。

> Steam 更新可能会覆盖已修改的脚本。遇到这种情况，重新解压补丁即可。

> **请使用 Steam 的默认分支。** 本补丁适用于游戏的主版本（Ren'Py 6.16），暂不支持测试版
> **modern - Ren'Py 8 branch**：如果你选择了该测试版，请在安装补丁前于 **属性** > **测试版** 中切换回默认
> 分支。Ren'Py 8 分支的支持正在开发中。

### 发布 zip 的内容

| 文件 | 说明 |
|---|---|
| `game/patch-hd.rpa` | 高清背景、立绘、CG、界面、特效和视频。 |
| `game/r18_hd.rpa` | 高清版 R18 补丁，替代官方的 `r18.rpa`。 |
| `game/*.rpyc` | 加入高清布局调整的 Steam 版游戏脚本，涵盖全部 11 种语言。 |
| `game/presplash.png` | 高清补丁的加载画面。 |

## 常见问题

**能在 Steam 的“modern - Ren'Py 8 branch”上使用吗？**
暂时不能，相关支持正在开发中。补丁是为默认分支（Ren'Py 6.16）制作的，而 Ren'Py 8 测试版使用不同的脚本
格式，在其上安装本补丁会导致游戏损坏。

**需要官方的 R18 补丁（`r18.rpa`）吗？**
不需要。`r18_hd.rpa` 已经包含高清版 R18 场景，游戏中关闭这些场景的选项也依然有效。

**它和 letow 的 Katawa Shoujo HD Patch 是一样的吗？**
它使用相同的高清美术和场景调整，并移植到了 Steam 版，另外还有“本版本的新内容”中列出的改动。letow 的原版补丁
是为 StandAlone 版制作的，在 Steam 版上会崩溃。

**能在 Linux、macOS 或 Steam Deck 上使用吗？**
应该可以：补丁只修改游戏数据，这些数据在所有系统上都相同。不过目前只在 Windows 上测试过，欢迎反馈。

**如何恢复原版游戏？**
删除 `game/patch-hd.rpa` 和 `game/r18_hd.rpa`，然后在 Steam 中使用 **验证游戏文件的完整性**。

## 从源码构建

仓库包含生成补丁的代码：以数据形式保存的高清改动，以及把这些改动应用到你自己游戏副本上的工具。仓库不包含
游戏文件和高清美术素材。

这个工具是为了透明度而存在的，让任何人都能准确看到补丁改了什么，并重新构建它。移植高清补丁需要从
《Katawa Shoujo》StandAlone 版、Steam 版、官方 `r18.rpa` 以及 StandAlone 版的高清补丁中提取信息，并进行比较，
找出高清补丁的每一处改动。这些提取模块只需要使用一次，因此没有包含在内：它们的结果保存在 `kshd/edits` 中。

### AI 的使用

移植过程本身漫长而杂乱，产生了大量一次性的测试代码和各种试验。公开当时手写的原始工具既不现实，也没有意义。
因此，本仓库的构建工具是使用 Anthropic 的 **Claude（Opus 5.5）** 制作的，以便根据移植得到的数据，干净可靠地
构建补丁。

### 要求

- [Python](https://www.python.org/) 3.9 或更高版本，无需额外的软件包。
- Steam 版《Katawa Shoujo》，**未经修改**且位于默认分支（不是 Ren'Py 8 测试版）。
- 高清素材包：[`KS-HD-1.0.2-Assets-For-Building-Only.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.2/KS-HD-1.0.2-Assets-For-Building-Only.zip)（约 700 MB）。

### 构建

1. 克隆或下载本仓库。
2. 通过以下两种方式之一，让工具读取游戏：
   - **在仓库中放一份游戏副本：** 将游戏文件夹（包含 `Katawa Shoujo.exe` 的文件夹）复制到仓库根目录，并命名为
     `Katawa Shoujo`。请使用安装补丁之前的副本。使用这种方式，Steam 中的安装可以在构建时保持已打补丁的状态。
   - **使用 Steam 中的安装：** 如果仓库中没有副本，工具会在你的 Steam 库中查找游戏。如果你已经在那里安装了
     本补丁，请先在 Steam 中执行 **验证游戏文件的完整性**。
3. 将 `KS-HD-1.0.2-Assets-For-Building-Only.zip` 放入 `assets` 文件夹，压缩或解压均可。
4. 运行：

```bash
python build.py
```

工具会修改脚本，并在 `build.py` 旁边生成 `KS-HD-1.0.2-Steam-Patch.zip`。这个 zip 就是补丁，按照“安装”中的说明
安装即可。

如果某个脚本与补丁预期的不一致，构建会停止并指出是哪一个。这种情况发生在游戏文件被修改过或属于其他版本时。

### 工作原理

高清补丁只修改游戏脚本中的少数内容：分辨率、位置、缩放、平移和界面布局，以及“本版本的新内容”中介绍的窗口
大小。这些改动以可读的数据形式保存在 `kshd/edits` 中，每个脚本对应一个 JSON 文件：

- **`code`**：界面代码的替换，每一项都记录了确切的原始文本以及它必须出现的次数，从而能发现游戏版本不对，
  而不是打错补丁。
- **`nodes`**：场景语句（`show`、`scene` 和 ATL 变换）的改动，通过标签和原始内容定位，因此同一个文件适用于
  全部 11 种语言。

| 文件 | 作用 |
|---|---|
| `build.py` | 查找游戏和素材，并行修改脚本并生成补丁 zip。 |
| `kshd/edits/*.json` | 以数据形式保存的高清改动。 |
| `kshd/patch.py` | 将改动文件应用到脚本上。 |
| `kshd/tree.py` | 遍历脚本结构，查找需要修改的代码和语句。 |
| `kshd/rpyc.py` | 读取和保存编译后的 `.rpyc` 脚本，并保持与 Ren'Py 6.16 兼容。 |
| `kshd/rpa.py` | 读写 Ren'Py 的 `.rpa` 归档文件。 |

### 高清素材包

图片、视频和 R18 场景存放在与代码分开的素材包中，这样无需改动代码就能改进它们。高清美术来自 letow 的 [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch)，使用 nagadomi 的 waifu2x 放大。本版本唯一新增的是按相同方式制作的四张波兰语漫画面板：

```
presplash.png    加载画面
hd/              背景、立绘、CG、界面、特效和视频（打包为 patch-hd.rpa）
r18/             R18 场景及其图片（打包为 r18_hd.rpa）
```

要更新美术素材，请把素材包解压到 `assets` 文件夹，保持相同的文件名和文件夹结构替换或添加文件，然后运行构建。
要分享素材包，请重新压缩该文件夹并上传到发布中。

## 测试与反馈

补丁通过了 Ren'Py 的 lint 检查，警告与未修改的 Steam 版游戏相同。菜单、设置、存档界面、画廊、片头以及若干
剧情和 R18 场景都已在游戏中检查过，每一条场景语句和每一个图片定义也都与原版高清补丁进行了比较。不过
《Katawa Shoujo》篇幅很长，并非每条路线、每种语言的每个场景都玩过，因此 **还需要更多测试**。目前只在
Windows 上测试过，特别欢迎 Linux 和 macOS 玩家的反馈。

如果发现立绘位置错误、CG 被裁切、界面元素错位或其他问题，请提交 issue，并注明场景、语言，可能的话附上截图。
也欢迎参与贡献。

## 许可

这是一个非官方、非商业性的粉丝项目，与 Four Leaf Studios 无关。
游戏及其素材的所有权利归各自的权利人所有。

## 致谢

- **[letow](https://github.com/letow)**：[Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch)
  （“Remastered by Letow”）的作者。letow 放大了所有素材，为 16:9 重新设计了界面，并完成了本移植所依据的场景
  调整。
- **[Four Leaf Studios](https://www.katawa-shoujo.com/)**：《Katawa Shoujo》的制作团队。
- **[nagadomi](https://github.com/nagadomi)**：原版高清补丁所用 AI 放大工具 **waifu2x** 的作者。
- **Novellae Subs**（俄语翻译）和 **HikariTranslations**（德语翻译）：在原版高清补丁中署名。
- **Valjean_Lafitte**：在原版高清补丁中作为灵感来源署名。
