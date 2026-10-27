<p align="center">
  <img src="../hd-logo.webp" alt="Katawa Shoujo HD Patch - Steam Edition logo" width="420">
</p>

# Katawa Shoujo HD Patch — Steam Edition (1080p)

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1ec-1f1e7.svg" width="20" alt="GB"> <a href="../README.md">English</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1ea-1f1f8.svg" width="20" alt="ES"> <a href="README.es.md">Español</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1eb-1f1f7.svg" width="20" alt="FR"> <a href="README.fr.md">Français</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1ef-1f1f5.svg" width="20" alt="JP"> <a href="README.ja.md">日本語</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e9-1f1ea.svg" width="20" alt="DE"> <b>Deutsch</b> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f0-1f1f7.svg" width="20" alt="KR"> <a href="README.ko.md">한국어</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f5-1f1f1.svg" width="20" alt="PL"> <a href="README.pl.md">Polski</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e7-1f1f7.svg" width="20" alt="BR"> <a href="README.pt-BR.md">Português (Brasil)</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f7-1f1fa.svg" width="20" alt="RU"> <a href="README.ru.md">Русский</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1e8-1f1f3.svg" width="20" alt="CN"> <a href="README.zh-CN.md">简体中文</a> ·
  <img src="https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f1f9-1f1fc.svg" width="20" alt="TW"> <a href="README.zh-TW.md">繁體中文</a>
</p>

**Spiele die Steam-Version von Katawa Shoujo in 1920×1080 im Breitbildformat, R18 inklusive.**

Ein inoffizieller Fan-Patch, mit dem die Steam-Version von **Katawa Shoujo**, der Visual Novel von Four Leaf
Studios, in **Full HD (1920×1080, 16:9-Breitbild)** statt in ihrer ursprünglichen Auflösung von 800×600 (4:3)
läuft. Hintergründe, Charakter-Sprites, CGs, die Oberfläche und die Videos werden durch HD-Versionen ersetzt. Er
funktioniert mit der Ren'Py-6.16-Engine der Steam-Version, in allen 11 Sprachen.

**[Neueste Version herunterladen](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)**

> Dies ist eine Portierung des [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) von **letow**.
> Alle HD-Grafiken (Hintergründe, Sprites, CGs, Oberfläche, Effekte und Videos) stammen aus diesem Projekt. Die
> vollständigen Credits stehen am Ende.

## Neu in dieser Edition

Funktionen, die es nur in dieser Edition gibt und die der ursprüngliche HD-Patch nicht hat:

- **Alle 11 Steam-Sprachen.** Der ursprüngliche Patch unterstützte Englisch, Spanisch, Französisch und
  Japanisch, dazu Deutsch und Russisch als Extras. Diese Edition ergänzt Koreanisch, Polnisch, brasilianisches
  Portugiesisch sowie vereinfachtes und traditionelles Chinesisch, einschließlich ihrer R18-Szenen. Die vier
  polnischen Comic-Panels (`comic_vfx*_pl`), die im ursprünglichen Patch fehlten, wurden auf dieselbe Weise in
  HD erstellt wie die der anderen Sprachen.
- **Unterstützung der Steam-Version.** Die HD-Anpassungen (Auflösung, Positionen, Zooms, Kameraschwenks,
  Oberflächenlayout) werden auf die Steam-Skripte angewendet, statt sie zu ersetzen. So funktionieren die
  Steam-Funktionen weiterhin: Errungenschaften, Controller-Unterstützung, die R18-Option und die gepackten
  Sprachdateien.
- **R18-Patch in HD.** `r18-hd.rpa` ersetzt die offizielle `r18.rpa` mit denselben Szenen in HD.
- **Scrollbarer Sprachbildschirm.** Er behält das HD-Layout bei und scrollt, damit alle 11 Sprachen Platz haben.
- **Fenster, das auf den Bildschirm passt.** Das Spiel öffnet sich in einem zentrierten Fenster mit 90 % des
  nutzbaren Desktopbereichs (ohne Taskleiste und Titelleiste), zwischen 1280×720 und 1920×1080 und nie größer
  als der Bildschirm. Der Vollbildmodus funktioniert wie bisher.
- **Neuere Spielbasis.** Basiert auf den aktuellen Steam-Skripten (v1.3.2) statt auf Katawa Shoujo 1.3/1.3.1,
  sodass spätere Korrekturen am Spiel erhalten bleiben.
- **Archive statt einzelner Dateien.** Die HD-Ressourcen werden als zwei `.rpa`-Archive geliefert, sodass das
  Installieren und Entfernen des Patches nur das Hinzufügen oder Löschen von Dateien bedeutet.

## Beschreibung

Der ursprüngliche HD-Patch wurde für die StandAlone-Version von Katawa Shoujo (Ren'Py 6.10) erstellt, die die
Inhalte für Erwachsene im Spiel selbst enthält. Die Steam-Version läuft mit einem neueren Ren'Py (6.16.5),
lagert diese Inhalte mit den ursprünglichen 4:3-Grafiken in einen separaten R18-Patch (`r18.rpa`) aus und bringt
eigene Funktionen mit. Deshalb lässt der ursprüngliche Patch die Steam-Version abstürzen.

Diese Edition bringt dasselbe HD-Remaster auf die Steam-Version und enthält den R18-Patch in HD.

### Optische Änderungen

Diese Edition ist eine reine Code-Anpassung und bringt keine neuen optischen Änderungen: Das Spiel sieht so
aus wie mit dem ursprünglichen HD-Patch. Vorher-Nachher-Vergleiche findest du im [Repository des
ursprünglichen Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch).

## Verfügbare Sprachen

Englisch, Spanisch, Französisch, Japanisch, Deutsch, Koreanisch, Polnisch, brasilianisches Portugiesisch,
Russisch, vereinfachtes Chinesisch und traditionelles Chinesisch: alle 11 Sprachen der Steam-Version.

## Installation

Kein Installationsprogramm nötig.

> **Lade den Patch von der [Releases](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)-Seite
> herunter.** Das Repository enthält das Build-Werkzeug; die HD-Archive (`patch-hd.rpa`, etwa 660 MB, und
> `r18-hd.rpa`) sind nur im Release-Zip enthalten.

1. Lade [`KS-HD-1.0.1-Steam-Patch.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Steam-Patch.zip) aus dem neuesten Release herunter.
   Das ist die einzige Datei, die du zum Spielen brauchst. Die andere, `Assets-For-Building-Only`, dient nur
   dazu, den Patch selbst zu erstellen.
2. Klicke in Steam mit der rechten Maustaste auf **Katawa Shoujo** > **Verwalten** > **Lokale Dateien durchsuchen**.
3. Entpacke das Zip in diesen Ordner (den mit `Katawa Shoujo.exe`).
4. Wähle bei der Nachfrage **alle Dateien ersetzen**.
5. Starte das Spiel über Steam.

**Linux und macOS:** Der Patch ersetzt nur Spieldaten (Skripte und Archive), die auf jedem System gleich sind.
Unter Linux sind die Schritte identisch. Unter macOS öffnet **Lokale Dateien durchsuchen** einen Ordner mit der
Spiel-App: Klicke sie mit der rechten Maustaste an, wähle **Paketinhalt zeigen** und führe den Ordner `game` aus
dem Zip mit dem Ordner `game` darin zusammen.

Die offizielle `r18.rpa` wird nicht benötigt. Wenn sie schon im Ordner liegt, kannst du sie dort lassen; das
Spiel verwendet die HD-Version.

**Zum Deinstallieren:** Lösche `game/patch-hd.rpa` und `game/r18-hd.rpa` und gehe dann in Steam auf
**Eigenschaften** > **Installierte Dateien** > **Spieldateien auf Fehler überprüfen**.

> Ein Steam-Update kann die gepatchten Skripte überschreiben. Entpacke den Patch in diesem Fall einfach erneut.

> **Verwende den Standard-Branch von Steam.** Der Patch ist für die Hauptversion des Spiels (Ren'Py 6.16)
> gemacht. Mit der Beta **modern - Ren'Py 8 branch** funktioniert er noch nicht: Wenn du sie ausgewählt hast,
> wechsle vor der Installation des Patches unter **Eigenschaften** > **Betas** zurück zum Standard-Branch. An
> der Unterstützung des Ren'Py-8-Branches wird gearbeitet.

### Inhalt des Release-Zips

| Datei | Beschreibung |
|---|---|
| `game/patch-hd.rpa` | HD-Hintergründe, Sprites, CGs, Oberfläche, Effekte und Videos. |
| `game/r18-hd.rpa` | Der R18-Patch in HD. Ersetzt die offizielle `r18.rpa`. |
| `game/*.rpyc` | Spielskripte der Steam-Version mit den HD-Layoutanpassungen, für alle 11 Sprachen. |
| `game/presplash.png` | Ladebildschirm des HD-Patches. |

## FAQ

**Funktioniert er mit dem „modern - Ren'Py 8 branch“ von Steam?**
Noch nicht; an der Unterstützung wird gearbeitet. Der Patch ist für den Standard-Branch (Ren'Py 6.16) gemacht,
und die Ren'Py-8-Beta verwendet ein anderes Skriptformat. Den Patch dort zu installieren, würde das Spiel
beschädigen.

**Brauche ich den offiziellen R18-Patch (`r18.rpa`)?**
Nein. `r18-hd.rpa` enthält die R18-Szenen bereits in HD, und die Spieloption, sie auszuschalten, funktioniert
weiterhin.

**Ist das dasselbe wie der Katawa Shoujo HD Patch von letow?**
Er verwendet dieselben HD-Grafiken und Szenenanpassungen, portiert auf die Steam-Version, plus die Änderungen
aus „Neu in dieser Edition“. Der ursprüngliche Patch von letow ist für die StandAlone-Version gemacht und stürzt
unter Steam ab.

**Funktioniert er unter Linux, macOS oder auf dem Steam Deck?**
Das sollte er: Der Patch ändert nur Spieldaten, die auf jedem System gleich sind. Bisher wurde er nur unter
Windows getestet, daher sind Rückmeldungen willkommen.

**Wie komme ich zum Originalspiel zurück?**
Lösche `game/patch-hd.rpa` und `game/r18-hd.rpa` und verwende dann in Steam **Spieldateien auf Fehler
überprüfen**.

## Aus dem Quellcode erstellen

Das Repository enthält den Code, der den Patch erzeugt: die als Daten gespeicherten HD-Änderungen und ein
Werkzeug, das sie auf deine eigene Kopie des Spiels anwendet. Die Spieldateien und die HD-Grafiken sind nicht
enthalten.

Das Werkzeug dient der Transparenz, damit jeder genau sehen kann, was der Patch ändert, und ihn neu erstellen
kann. Für die Portierung des HD-Patches mussten Informationen aus der StandAlone-Version von Katawa Shoujo, der
Steam-Version, der offiziellen `r18.rpa` und dem HD-Patch für StandAlone extrahiert und verglichen werden, um
jede Änderung des HD-Patches zu finden. Diese Extraktionsmodule wurden nur einmal gebraucht und sind nicht
enthalten: Ihr Ergebnis ist in `kshd/edits` gespeichert.

### Einsatz von KI

Die Portierung selbst war ein langer und unstrukturierter Prozess mit enormen Mengen an Wegwerf-Testcode und
Experimenten. Die ursprünglichen, dabei von Hand geschriebenen Werkzeuge zu veröffentlichen, war nicht
praktikabel und hätte keinen Sinn ergeben. Stattdessen wurde das Build-Werkzeug dieses Repositorys mit
**Claude (Opus 5.5)** von Anthropic erstellt, um den Patch sauber und zuverlässig aus den Daten der Portierung
erstellen zu können.

### Voraussetzungen

- [Python](https://www.python.org/) 3.9 oder neuer. Zusätzliche Pakete sind nicht nötig.
- Die Steam-Version von Katawa Shoujo, **unverändert** und im Standard-Branch (nicht die Ren'Py-8-Beta).
- Das HD-Ressourcenpaket: [`KS-HD-1.0.1-Assets-For-Building-Only.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Assets-For-Building-Only.zip) (etwa 700 MB).

### Erstellen

1. Klone dieses Repository oder lade es herunter.
2. Gib dem Werkzeug auf eine dieser beiden Arten Zugriff auf das Spiel:
   - **Eine Kopie des Spiels im Repository:** Kopiere den Spielordner (den mit `Katawa Shoujo.exe`) in das
     Stammverzeichnis des Repositorys und nenne ihn `Katawa Shoujo`. Verwende eine Kopie von vor der
     Installation des Patches. So kann die Steam-Installation gepatcht bleiben, während du den Patch erstellst.
   - **Die Steam-Installation:** Gibt es keine Kopie im Repository, sucht das Werkzeug das Spiel in deinen
     Steam-Bibliotheken. Wenn du diesen Patch dort schon installiert hast, verwende vorher in Steam
     **Spieldateien auf Fehler überprüfen**.
3. Lege `KS-HD-1.0.1-Assets-For-Building-Only.zip` in den Ordner `assets`, gepackt oder entpackt.
4. Führe aus:

```bash
python build.py
```

Das Werkzeug patcht die Skripte und erstellt `KS-HD-1.0.1-Steam-Patch.zip` neben `build.py`. Dieses Zip ist der
Patch: Installiere ihn wie unter „Installation“ beschrieben.

Wenn ein Skript nicht dem entspricht, was der Patch erwartet, bricht der Vorgang ab und nennt das Skript. Das
passiert, wenn die Spieldateien verändert wurden oder zu einer anderen Version gehören.

### Funktionsweise

Der HD-Patch ändert nur wenige Dinge in den Spielskripten: Auflösung, Positionen, Zooms, Kameraschwenks und das
Oberflächenlayout, dazu die in „Neu in dieser Edition“ beschriebene Fenstergröße. Diese Änderungen sind als
lesbare Daten in `kshd/edits` gespeichert, eine JSON-Datei pro Skript:

- **`code`**: Ersetzungen im Oberflächencode, jeweils mit dem exakten Originaltext und der Anzahl, wie oft er
  vorkommen muss. So wird eine falsche Spielversion erkannt, statt fehlerhaft gepatcht zu werden.
- **`nodes`**: Änderungen an Szenenanweisungen (`show`, `scene` und ATL-Transformationen), gefunden über ihr
  Label und ihren ursprünglichen Inhalt, damit dieselbe Datei für alle 11 Sprachen funktioniert.

| Datei | Aufgabe |
|---|---|
| `build.py` | Findet das Spiel und die Ressourcen, patcht die Skripte parallel und erstellt das Patch-Zip. |
| `kshd/edits/*.json` | Die HD-Änderungen als Daten. |
| `kshd/patch.py` | Wendet eine Änderungsdatei auf ein Skript an. |
| `kshd/tree.py` | Durchläuft die Skriptstruktur, um den zu ändernden Code und die Anweisungen zu finden. |
| `kshd/rpyc.py` | Lädt und speichert kompilierte `.rpyc`-Skripte und hält sie kompatibel mit Ren'Py 6.16. |
| `kshd/rpa.py` | Liest und schreibt `.rpa`-Archive von Ren'Py. |

### HD-Ressourcenpaket

Die Bilder, Videos und R18-Szenen liegen getrennt vom Code im Ressourcenpaket, damit sie verbessert werden
können, ohne den Code anzufassen. Die HD-Grafiken stammen aus letows [Katawa Shoujo HD
Patch](https://github.com/letow/KatawaShoujoHDPatch) und wurden mit waifu2x von nagadomi hochskaliert. Die
einzige Ergänzung dieser Edition sind die vier polnischen Comic-Panels, die auf dieselbe Weise wie die anderen
erstellt wurden:

```
presplash.png    Ladebildschirm
hd/              Hintergründe, Sprites, CGs, Oberfläche, Effekte und Videos (gepackt in patch-hd.rpa)
r18/             R18-Szenen und ihre Bilder (gepackt in r18-hd.rpa)
```

Um die Grafiken zu aktualisieren, entpacke das Paket in den Ordner `assets`, ersetze oder ergänze Dateien mit
denselben Namen und Ordnern und starte die Erstellung. Zum Teilen packe den Ordner wieder als Zip und lade ihn
in einem Release hoch.

## Tests und Rückmeldungen

Der Patch besteht Ren'Pys Lint mit denselben Warnungen wie das unveränderte Steam-Spiel. Menüs, Optionen,
Speicherbildschirm, Galerie, Opening sowie mehrere Story- und R18-Szenen wurden im Spiel geprüft, und jede
Szenenanweisung und jede Bilddefinition wurde mit dem ursprünglichen HD-Patch verglichen. Katawa Shoujo ist ein
langes Spiel, und nicht jede Szene jeder Route und Sprache wurde durchgespielt, daher **braucht der Patch noch
weitere Tests**. Getestet wurde er nur unter Windows; Rückmeldungen von Linux- und macOS-Spielern sind besonders
willkommen.

Wenn du ein falsch platziertes Sprite, ein abgeschnittenes CG, ein verrutschtes Oberflächenelement oder ein
anderes Problem findest, eröffne bitte ein Issue mit der Szene, der Sprache und nach Möglichkeit einem
Screenshot. Beiträge sind ebenfalls willkommen.

## Lizenz

Dies ist ein inoffizielles, nicht kommerzielles Fanprojekt und steht in keiner Verbindung zu Four Leaf Studios.
Alle Rechte am Spiel und an seinen Ressourcen liegen bei den jeweiligen Inhabern.

## Credits

- **[letow](https://github.com/letow)**, Autor des
  [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) („Remastered by Letow“). letow hat
  jede Ressource hochskaliert, die Oberfläche für 16:9 neu gestaltet und die Szenenanpassungen vorgenommen, auf
  denen diese Portierung aufbaut.
- **[Four Leaf Studios](https://www.katawa-shoujo.com/)**, die Macher von Katawa Shoujo.
- **[nagadomi](https://github.com/nagadomi)**, Autor von **waifu2x**, dem KI-Upscaler, den der ursprüngliche
  HD-Patch verwendet hat.
- **Novellae Subs** (russische Übersetzung) und **HikariTranslations** (deutsche Übersetzung), im
  ursprünglichen HD-Patch genannt.
- **Valjean_Lafitte**, im ursprünglichen HD-Patch als Inspiration genannt.
