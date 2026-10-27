<p align="center">
  <img src="hd-logo.webp" alt="Katawa Shoujo HD Patch - Steam Edition logo" width="420">
</p>

# Katawa Shoujo HD Patch — Steam Edition (1080p)

<p align="center">
  :gb: <b>English</b> ·
  :es: <a href="docs/README.es.md">Español</a> ·
  :fr: <a href="docs/README.fr.md">Français</a> ·
  :jp: <a href="docs/README.ja.md">日本語</a> ·
  :de: <a href="docs/README.de.md">Deutsch</a> ·
  :kr: <a href="docs/README.ko.md">한국어</a> ·
  :poland: <a href="docs/README.pl.md">Polski</a> ·
  :brazil: <a href="docs/README.pt-BR.md">Português (Brasil)</a> ·
  :ru: <a href="docs/README.ru.md">Русский</a> ·
  :cn: <a href="docs/README.zh-CN.md">简体中文</a> ·
  :taiwan: <a href="docs/README.zh-TW.md">繁體中文</a>
</p>

**Play the Steam version of Katawa Shoujo in 1920×1080 widescreen, R18 included.**

An unofficial fan patch that makes the Steam release of **Katawa Shoujo**, the visual novel by Four Leaf
Studios, run in **Full HD (1920×1080, 16:9 widescreen)** instead of its original 800×600 (4:3). Backgrounds,
character sprites, CGs, the interface and the videos are replaced with HD versions. It works with the
Ren'Py 6.16 engine of the Steam version, in all 11 of its languages.

**[Download the latest version](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)**

> This is an adaptation of the [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) by **letow**.
> All the HD artwork (backgrounds, sprites, CGs, UI, effects and videos) comes from that project. Full credits are
> at the end.

## What's New in This Edition

Features exclusive to this edition, not found in the original HD patch:

- **All 11 Steam languages.** The original patch covered English, Spanish, French and Japanese, with German
  and Russian as extras. This edition adds Korean, Polish, Brazilian Portuguese and Simplified and Traditional
  Chinese, including their R18 scenes. The four Polish comic panels (`comic_vfx*_pl`), missing from the
  original patch, were made in HD the same way as the other languages' panels.
- **Steam version support.** The HD adjustments (resolution, positions, zooms, pans, UI layout) are
  re-applied on top of the Steam scripts instead of replacing them, so Steam features keep working:
  achievements, controller support, the R18 toggle and the packed language files.
- **R18 patch in HD.** `r18-hd.rpa` replaces the official `r18.rpa` with the same scenes in HD.
- **Scrollable language screen.** It keeps the HD layout and scrolls so all 11 languages fit.
- **Window that fits the screen.** The game opens in a centered window at 90% of the usable desktop area
  (without the taskbar and the title bar), between 1280×720 and 1920×1080 and never bigger than the screen.
  Fullscreen works as before.
- **Newer game base.** Built on the current Steam scripts (v1.3.2) instead of Katawa Shoujo 1.3/1.3.1, so
  later game fixes are kept.
- **Archives instead of loose files.** The HD assets ship as two `.rpa` archives, so installing and removing
  the patch only means adding or deleting files.

## Description

The original HD patch was made for the StandAlone release of Katawa Shoujo (Ren'Py 6.10), which includes
the adult content in the game itself. The Steam release runs on a newer Ren'Py (6.16.5), moves that content
into a separate R18 patch (`r18.rpa`) with the original 4:3 art, and adds features of its own. Because of
that, the original patch makes the Steam version crash.

This edition brings the same HD remaster to the Steam version and includes the R18 patch in HD.

### Visual Changes

This edition is a code adaptation: it adds no new visual changes, so the game looks as it does with the
original HD patch. To see the before/after comparisons, visit the [original Katawa Shoujo HD Patch
repository](https://github.com/letow/KatawaShoujoHDPatch).

## Languages Available

English, Spanish, French, Japanese, German, Korean, Polish, Brazilian Portuguese, Russian,
Simplified Chinese and Traditional Chinese: all 11 languages of the Steam version.

## Installation

No installer needed.

> **Download the patch from the [Releases](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)
> page.** The repository contains the build tool; the HD archives (`patch-hd.rpa`, about 660 MB, and
> `r18-hd.rpa`) are only in the release zip.

1. Download [`KS-HD-1.0.1-Steam-Patch.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Steam-Patch.zip) from the latest release.
   It's the only file you need to play. The other one, `Assets-For-Building-Only`, is only for building
   the patch yourself.
2. In Steam, right-click **Katawa Shoujo** > **Manage** > **Browse local files**.
3. Extract the zip into that folder (the one containing `Katawa Shoujo.exe`).
4. When asked, choose **replace all files**.
5. Launch the game from Steam.

**Linux and macOS:** the patch only replaces game data (scripts and archives), which is the same on every
system. On Linux the steps are identical. On macOS, **Browse local files** opens a folder with the game app:
right-click it, choose **Show Package Contents** and merge the zip's `game` folder into the `game` folder
inside.

The official `r18.rpa` isn't needed. If it's already in the folder you can leave it there; the game uses the
HD version.

**To uninstall:** delete `game/patch-hd.rpa` and `game/r18-hd.rpa`, then in Steam go to
**Properties** > **Installed Files** > **Verify integrity of game files**.

> A Steam update may overwrite the patched scripts. If that happens, extract the patch again.

> **Use the default Steam branch.** The patch is made for the main version of the game (Ren'Py 6.16). It
> doesn't work with the **modern - Ren'Py 8 branch** beta yet: if you selected it, go back to the default
> branch in **Properties** > **Betas** before installing the patch. Support for the Ren'Py 8 branch is in
> progress.

### What's inside the release zip

| File | Description |
|---|---|
| `game/patch-hd.rpa` | HD backgrounds, sprites, CGs, UI, effects and videos. |
| `game/r18-hd.rpa` | The R18 patch in HD. Replaces the official `r18.rpa`. |
| `game/*.rpyc` | Steam game scripts with the HD layout adjustments, for all 11 languages. |
| `game/presplash.png` | HD patch loading screen. |

## FAQ

**Does it work with the "modern - Ren'Py 8 branch" of Steam?**
Not yet; support for it is in progress. The patch is made for the default branch (Ren'Py 6.16), and the
Ren'Py 8 beta uses a different script format, so installing this patch there would break the game.

**Do I need the official R18 patch (`r18.rpa`)?**
No. `r18-hd.rpa` already contains the R18 scenes in HD, and the game's option to turn them off still works.

**Is it the same as letow's Katawa Shoujo HD Patch?**
It uses the same HD art and scene adjustments, ported to the Steam version, plus the changes listed in
"What's New in This Edition". letow's original patch is made for the StandAlone release and crashes on Steam.

**Does it work on Linux, macOS or Steam Deck?**
It should: the patch only changes game data, which is the same on every system. It has only been tested on
Windows so far, so reports are welcome.

**How do I go back to the original game?**
Delete `game/patch-hd.rpa` and `game/r18-hd.rpa`, then use **Verify integrity of game files** in Steam.

## Building from Source

The repository contains the code that generates the patch: the HD changes stored as data and a tool that
applies them to your own copy of the game. The game files and the HD art are not included.

The tool exists for transparency, so anyone can see exactly what the patch changes and rebuild it. Porting
the HD patch required extracting information from the Katawa Shoujo StandAlone version, the Steam version,
the official `r18.rpa` and the StandAlone HD patch, and comparing them to find every change the HD patch
makes. Those extraction modules were only needed once and were left out: their result is stored in
`kshd/edits`.

### Use of AI

The port itself was a long and disorganized process, with massive amounts of throwaway test code and
experiments. Publishing the original tooling, written by hand along the way, wasn't viable and wouldn't have
served any purpose. Instead, the build tool in this repository was created with **Claude (Opus 5.5)**, by
Anthropic, to provide a clean and reliable way to build the patch from the data produced by the port.

### Requirements

- [Python](https://www.python.org/) 3.9 or newer. No extra packages are needed.
- The Steam version of Katawa Shoujo, **unmodified** and on the default branch (not the Ren'Py 8 beta).
- The HD assets package: [`KS-HD-1.0.1-Assets-For-Building-Only.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Assets-For-Building-Only.zip) (about 700 MB).

### Build

1. Clone or download this repository.
2. Give the tool access to the game, in one of these two ways:
   - **A copy of the game in the repository:** copy the game folder (the one that contains
     `Katawa Shoujo.exe`) into the root of the repository and name it `Katawa Shoujo`. Use a copy taken
     before installing the patch. With this option, the Steam installation can stay patched while you build.
   - **The Steam installation:** if there's no copy in the repository, the tool looks for the game in your
     Steam libraries. If you already installed this patch there, run **Verify integrity of game files** in
     Steam first.
3. Put `KS-HD-1.0.1-Assets-For-Building-Only.zip` in the `assets` folder, zipped or extracted.
4. Run:

```bash
python build.py
```

The tool patches the scripts and creates `KS-HD-1.0.1-Steam-Patch.zip` next to `build.py`. That zip is the
patch: install it as described in "Installation".

If a script doesn't match what the patch expects, the build stops and says which one: that happens when
the game files were modified or belong to another version.

### How it works

The HD patch only changes a few things in the game scripts: resolution, positions, zooms, pans and the
interface layout, plus the window size described in "What's New in This Edition". Those changes are stored
as readable data in `kshd/edits`, one JSON file per script:

- **`code`**: interface code replacements, each with the exact original text and how many times it must
  appear, so a wrong game version is detected instead of patched badly.
- **`nodes`**: changes to scene statements (`show`, `scene` and ATL transforms), located by their label
  and their original content, so the same file works for all 11 languages.

| File | Role |
|---|---|
| `build.py` | Finds the game and the assets, patches the scripts in parallel and creates the patch zip. |
| `kshd/edits/*.json` | The HD changes, as data. |
| `kshd/patch.py` | Applies an edits file to a script. |
| `kshd/tree.py` | Walks the script structure to find the code and statements to change. |
| `kshd/rpyc.py` | Loads and saves compiled `.rpyc` scripts, keeping them compatible with Ren'Py 6.16. |
| `kshd/rpa.py` | Reads and writes Ren'Py `.rpa` archives. |

### HD assets package

The images, videos and R18 scenes are kept in the assets package, separate from the code, so they can be
improved without touching it. The HD art comes from letow's [Katawa Shoujo HD
Patch](https://github.com/letow/KatawaShoujoHDPatch), upscaled with nagadomi's waifu2x. This edition's only
addition is the four Polish comic panels, made the same way as the others:

```
presplash.png    loading screen
hd/              backgrounds, sprites, CGs, interface, effects and videos (packed into patch-hd.rpa)
r18/             R18 scenes and their images (packed into r18-hd.rpa)
```

To update the art, extract the package into the `assets` folder, replace or add files keeping the same
names and folders, and run the build. To share it, zip the folder again and upload it to a release.

## Testing and Feedback

The patch passes Ren'Py's lint with the same warnings as the unmodified Steam game. The menus, options,
save screen, gallery, opening and several story and R18 scenes were checked in-game, and every scene
statement and image definition was compared with the original HD patch. Katawa Shoujo is a long game and not
every scene of every route and language has been played through, so **it needs more testing**. It has only
been tested on Windows; reports from Linux and macOS players are especially welcome.

If you find a misplaced sprite, a cropped CG, a UI element out of place or any other issue, please open an
issue with the scene, the language and a screenshot if possible. Contributions are welcome too.

## License

This is an unofficial, non-commercial fan project and is not associated with Four Leaf Studios.
All rights to the game and its assets belong to their respective owners.

## Credits

- **[letow](https://github.com/letow)**, author of the
  [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) ("Remastered by Letow"). letow
  upscaled every asset, redesigned the UI for 16:9 and made the scene adjustments this port is built on.
- **[Four Leaf Studios](https://www.katawa-shoujo.com/)**, creators of Katawa Shoujo.
- **[nagadomi](https://github.com/nagadomi)**, author of **waifu2x**, the AI upscaler used by the
  original HD patch.
- **Novellae Subs** (Russian translation) and **HikariTranslations** (German translation), credited in
  the original HD patch.
- **Valjean_Lafitte**, credited as inspiration in the original HD patch.
