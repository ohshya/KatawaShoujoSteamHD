import json
import re
import sys
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from kshd import rpa
from kshd.patch import PatchError, apply

ROOT = Path(__file__).resolve().parent
# Patch version, used in the output file name "KS-HD-<VERSION>-Steam-Patch.zip".
VERSION = '1.0.0'
# Script suffixes of the Steam languages ('' is English); add new ones here if Steam adds languages.
LANGUAGES = ['', '_ES', '_FR', '_JP', '_DE', '_KR', '_PL', '_PT-BR', '_RU', '_ZH', '_ZH-HANT']


class Assets:
    def __init__(self, path):
        self.zip = zipfile.ZipFile(path) if path.is_file() else None
        names = [n for n in self.zip.namelist() if not n.endswith('/')] if self.zip else \
            [p.relative_to(path).as_posix() for p in path.rglob('*') if p.is_file()]
        root = min((n[:-len('presplash.png')] for n in names if n.endswith('presplash.png')), key=len, default=None)
        if root is None:
            sys.exit('%s is not the HD assets package.' % path)
        self.path, self.root = path, root
        self.names = [n[len(root):] for n in names if n.startswith(root)]

    def open(self, name):
        return self.zip.open(self.root + name) if self.zip else open(self.path / self.root / name, 'rb')

    def size(self, name):
        return self.zip.getinfo(self.root + name).file_size if self.zip else (self.path / self.root / name).stat().st_size


class Steam:
    def __init__(self, game):
        self.game = Path(game)
        self.index = {}
        for archive in self.game.glob('lang-*.rpa'):
            self.index.update(rpa.read_index(archive))

    def script(self, name):
        path = self.game / name
        return path.read_bytes() if path.exists() else rpa.read(self.index[name])


def steam_libraries():
    roots = []
    if sys.platform == 'win32':
        import winreg
        for hive, key, value in ((winreg.HKEY_CURRENT_USER, r'Software\Valve\Steam', 'SteamPath'),
                                 (winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\Valve\Steam', 'InstallPath')):
            try:
                with winreg.OpenKey(hive, key) as k:
                    roots.append(Path(winreg.QueryValueEx(k, value)[0]))
            except OSError:
                pass
    roots += [Path.home() / p for p in ('.steam/steam', '.local/share/Steam', 'Library/Application Support/Steam')]
    libraries = []
    for root in roots:
        vdf = root / 'steamapps' / 'libraryfolders.vdf'
        if vdf.exists():
            libraries += [root] + [Path(p.replace('\\\\', '\\')) for p in re.findall(r'"path"\s+"([^"]+)"', vdf.read_text(errors='ignore'))]
    return list(dict.fromkeys(libraries))


def find_game():
    for folder in [lib / 'steamapps' / 'common' / 'Katawa Shoujo' for lib in steam_libraries()] + [ROOT / 'Katawa Shoujo']:
        hit = next(folder.rglob('data.rpa'), None) if folder.is_dir() else None
        if hit:
            return hit.parent
    sys.exit('Katawa Shoujo was not found in Steam. Copy the game folder here as "Katawa Shoujo".')


def find_assets():
    folder = ROOT / 'assets'
    archive = next(folder.glob('*.zip'), None)
    if archive or folder.is_dir() and any(folder.rglob('presplash.png')):
        return Assets(archive or folder)
    sys.exit('HD assets not found. Download them from the releases page and put them in the "assets" folder.')


def init(game):
    global STEAM
    STEAM = Steam(game)


def task(job):
    name, edits = job
    return name, apply(name, STEAM.script(name), edits)


def main():
    game, assets = find_game(), find_assets()
    print('Game:', game.parent)
    jobs = []
    for f in sorted((ROOT / 'kshd' / 'edits').glob('*.json')):
        edits = json.loads(f.read_text(encoding='utf-8'))
        jobs += [(f.stem + s + '.rpyc', edits) for s in (LANGUAGES if edits.get('languages') else [''])]
    try:
        with ProcessPoolExecutor(initializer=init, initargs=(str(game),)) as pool:
            scripts = dict(pool.map(task, jobs, chunksize=4))
    except PatchError as e:
        sys.exit('%s\nThe game files are modified or from another version: verify them in Steam and try again.' % e)
    out = ROOT / ('KS-HD-%s-Steam-Patch.zip' % VERSION)
    with zipfile.ZipFile(out, 'w') as z:
        z.write(ROOT / 'README.md', 'README.md', zipfile.ZIP_DEFLATED)
        for name, data in sorted(scripts.items()):
            z.writestr('game/' + name, data, zipfile.ZIP_DEFLATED)
        with assets.open('presplash.png') as f:
            z.writestr('game/presplash.png', f.read())
        for archive, folder in (('patch-hd.rpa', 'hd/'), ('r18-hd.rpa', 'r18/')):
            with z.open('game/' + archive, 'w', force_zip64=True) as f:
                rpa.write(f, {n[len(folder):]: (assets.size(n), lambda n=n: assets.open(n)) for n in assets.names if n.startswith(folder)})
    print('Done:', out)


if __name__ == '__main__':
    main()
