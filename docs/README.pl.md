<p align="center">
  <img src="../hd-logo.webp" alt="Katawa Shoujo HD Patch - Steam Edition logo" width="420">
</p>

# Katawa Shoujo HD Patch — Steam Edition (1080p)

<p align="center">
  :gb: <a href="../README.md">English</a> ·
  :es: <a href="README.es.md">Español</a> ·
  :fr: <a href="README.fr.md">Français</a> ·
  :jp: <a href="README.ja.md">日本語</a> ·
  :de: <a href="README.de.md">Deutsch</a> ·
  :kr: <a href="README.ko.md">한국어</a> ·
  :poland: <b>Polski</b> ·
  :brazil: <a href="README.pt-BR.md">Português (Brasil)</a> ·
  :ru: <a href="README.ru.md">Русский</a> ·
  :cn: <a href="README.zh-CN.md">简体中文</a> ·
  :taiwan: <a href="README.zh-TW.md">繁體中文</a>
</p>

**Zagraj w wersję Steam gry Katawa Shoujo w panoramicznej rozdzielczości 1920×1080, R18 w zestawie.**

Nieoficjalna, fanowska łatka, dzięki której wersja Steam **Katawa Shoujo**, powieści wizualnej studia Four Leaf
Studios, działa w **Full HD (1920×1080, panoramiczne 16:9)** zamiast w oryginalnej rozdzielczości 800×600 (4:3).
Tła, sprite'y postaci, CG, interfejs i filmy zostają zastąpione wersjami HD. Łatka działa z silnikiem Ren'Py
6.16 wersji Steam, we wszystkich 11 językach gry.

**[Pobierz najnowszą wersję](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)**

> To adaptacja [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) autorstwa **letow**.
> Cała grafika HD (tła, sprite'y, CG, interfejs, efekty i filmy) pochodzi z tamtego projektu. Pełne podziękowania
> znajdują się na końcu.

## Nowości w tej edycji

Funkcje dostępne wyłącznie w tej edycji, których nie ma w oryginalnej łatce HD:

- **Wszystkie 11 języków wersji Steam.** Oryginalna łatka obejmowała angielski, hiszpański, francuski i
  japoński, a niemiecki i rosyjski jako dodatki. Ta edycja dodaje koreański, polski, portugalski brazylijski
  oraz chiński uproszczony i tradycyjny, łącznie z ich scenami R18. Cztery polskie panele komiksowe
  (`comic_vfx*_pl`), których brakowało w oryginalnej łatce, wykonano w HD tak samo jak panele w innych językach.
- **Obsługa wersji Steam.** Poprawki HD (rozdzielczość, pozycje, przybliżenia, panoramy, układ interfejsu) są
  nakładane na skrypty wersji Steam zamiast je zastępować, więc funkcje Steam nadal działają: osiągnięcia,
  obsługa kontrolera, przełącznik R18 i spakowane pliki językowe.
- **Łatka R18 w HD.** `r18-hd.rpa` zastępuje oficjalny `r18.rpa` tymi samymi scenami w HD.
- **Przewijany ekran wyboru języka.** Zachowuje układ HD i przewija się, aby zmieścić wszystkie 11 języków.
- **Okno dopasowane do ekranu.** Gra otwiera się w wyśrodkowanym oknie zajmującym 90% użytecznego obszaru
  pulpitu (bez paska zadań i paska tytułu), w rozmiarze od 1280×720 do 1920×1080 i nigdy większym niż ekran.
  Tryb pełnoekranowy działa tak jak wcześniej.
- **Nowsza podstawa gry.** Oparta na aktualnych skryptach wersji Steam (v1.3.2) zamiast na Katawa Shoujo
  1.3/1.3.1, więc późniejsze poprawki gry zostają zachowane.
- **Archiwa zamiast luźnych plików.** Zasoby HD są dostarczane w dwóch archiwach `.rpa`, więc instalacja i
  usunięcie łatki sprowadzają się do dodania lub usunięcia plików.

## Opis

Oryginalna łatka HD powstała dla wersji StandAlone Katawa Shoujo (Ren'Py 6.10), która zawiera treści dla
dorosłych w samej grze. Wersja Steam działa na nowszym Ren'Py (6.16.5), przenosi te treści do osobnej łatki R18
(`r18.rpa`) z oryginalną grafiką 4:3 i dodaje własne funkcje. Dlatego oryginalna łatka powoduje awarię wersji
Steam.

Ta edycja przenosi ten sam remaster HD do wersji Steam i zawiera łatkę R18 w HD.

### Zmiany wizualne

Ta edycja to wyłącznie adaptacja kodu i nie wprowadza nowych zmian wizualnych: gra wygląda tak samo jak z
oryginalną łatką HD. Porównania przed i po znajdziesz w [repozytorium oryginalnej Katawa Shoujo HD
Patch](https://github.com/letow/KatawaShoujoHDPatch).

## Dostępne języki

Angielski, hiszpański, francuski, japoński, niemiecki, koreański, polski, portugalski brazylijski, rosyjski,
chiński uproszczony i chiński tradycyjny: wszystkie 11 języków wersji Steam.

## Instalacja

Instalator nie jest potrzebny.

> **Pobierz łatkę ze strony [Releases](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest).**
> Repozytorium zawiera narzędzie do budowania; archiwa HD (`patch-hd.rpa`, około 660 MB, i `r18-hd.rpa`) są
> tylko w pliku zip wydania.

1. Pobierz [`KS-HD-1.0.1-Steam-Patch.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Steam-Patch.zip) z najnowszego wydania.
   To jedyny plik potrzebny do gry. Drugi, `Assets-For-Building-Only`, służy tylko do samodzielnego
   zbudowania łatki.
2. W Steam kliknij prawym przyciskiem **Katawa Shoujo** > **Zarządzaj** > **Przeglądaj pliki lokalne**.
3. Rozpakuj zip do tego folderu (tego, w którym jest `Katawa Shoujo.exe`).
4. Gdy pojawi się pytanie, wybierz **zastąp wszystkie pliki**.
5. Uruchom grę ze Steam.

**Linux i macOS:** łatka zastępuje tylko dane gry (skrypty i archiwa), które są takie same w każdym systemie.
W systemie Linux kroki są identyczne. W systemie macOS **Przeglądaj pliki lokalne** otwiera folder z aplikacją
gry: kliknij ją prawym przyciskiem, wybierz **Pokaż zawartość pakietu** i połącz folder `game` z pliku zip z
folderem `game` w środku.

Oficjalny `r18.rpa` nie jest potrzebny. Jeśli już jest w folderze, możesz go zostawić; gra użyje wersji HD.

**Aby odinstalować:** usuń `game/patch-hd.rpa` i `game/r18-hd.rpa`, a następnie w Steam przejdź do
**Właściwości** > **Zainstalowane pliki** > **Zweryfikuj spójność plików gry**.

> Aktualizacja Steam może nadpisać spatchowane skrypty. W takim przypadku rozpakuj łatkę ponownie.

> **Używaj domyślnej gałęzi Steam.** Łatka jest przeznaczona dla głównej wersji gry (Ren'Py 6.16). Nie działa
> jeszcze z wersją beta **modern - Ren'Py 8 branch**: jeśli ją wybrałeś, przed instalacją łatki wróć do
> domyślnej gałęzi w **Właściwości** > **Wersje beta**. Trwają prace nad obsługą gałęzi Ren'Py 8.

### Zawartość pliku zip wydania

| Plik | Opis |
|---|---|
| `game/patch-hd.rpa` | Tła, sprite'y, CG, interfejs, efekty i filmy w HD. |
| `game/r18-hd.rpa` | Łatka R18 w HD. Zastępuje oficjalny `r18.rpa`. |
| `game/*.rpyc` | Skrypty gry z wersji Steam z poprawkami układu HD, dla wszystkich 11 języków. |
| `game/presplash.png` | Ekran ładowania łatki HD. |

## FAQ

**Czy działa z gałęzią „modern - Ren'Py 8 branch” w Steam?**
Jeszcze nie; trwają prace nad jej obsługą. Łatka jest przeznaczona dla domyślnej gałęzi (Ren'Py 6.16), a beta
Ren'Py 8 używa innego formatu skryptów, więc zainstalowanie tam tej łatki zepsułoby grę.

**Czy potrzebuję oficjalnej łatki R18 (`r18.rpa`)?**
Nie. `r18-hd.rpa` zawiera już sceny R18 w HD, a opcja gry pozwalająca je wyłączyć nadal działa.

**Czy to to samo co Katawa Shoujo HD Patch od letow?**
Używa tej samej grafiki HD i tych samych poprawek scen, przeniesionych do wersji Steam, oraz zmian z sekcji
„Nowości w tej edycji”. Oryginalna łatka letow jest przeznaczona dla wersji StandAlone i w wersji Steam
powoduje awarię.

**Czy działa w systemach Linux, macOS lub na Steam Deck?**
Powinna: łatka zmienia tylko dane gry, które są takie same w każdym systemie. Na razie testowano ją tylko w
systemie Windows, więc zgłoszenia są mile widziane.

**Jak wrócić do oryginalnej gry?**
Usuń `game/patch-hd.rpa` i `game/r18-hd.rpa`, a następnie użyj **Zweryfikuj spójność plików gry** w Steam.

## Budowanie ze źródeł

Repozytorium zawiera kod, który tworzy łatkę: zmiany HD zapisane jako dane i narzędzie, które nakłada je na
twoją własną kopię gry. Pliki gry i grafika HD nie są dołączone.

Narzędzie istnieje dla przejrzystości, aby każdy mógł dokładnie zobaczyć, co zmienia łatka, i zbudować ją
ponownie. Przeniesienie łatki HD wymagało wyciągnięcia informacji z wersji StandAlone Katawa Shoujo, wersji
Steam, oficjalnego `r18.rpa` i łatki HD dla wersji StandAlone oraz porównania ich, aby znaleźć każdą zmianę
wprowadzaną przez łatkę HD. Te moduły ekstrakcji były potrzebne tylko raz i nie zostały dołączone: ich wynik jest
zapisany w `kshd/edits`.

### Wykorzystanie AI

Sam port był długim i chaotycznym procesem, z ogromną ilością jednorazowego kodu testowego i eksperymentów.
Publikacja oryginalnych narzędzi, pisanych ręcznie po drodze, nie była wykonalna i nie miałaby sensu. Dlatego
narzędzie do budowania w tym repozytorium zostało stworzone przy użyciu **Claude (Opus 5.5)** firmy Anthropic,
aby zapewnić czysty i niezawodny sposób budowania łatki z danych uzyskanych podczas portowania.

### Wymagania

- [Python](https://www.python.org/) 3.9 lub nowszy. Dodatkowe pakiety nie są potrzebne.
- Wersja Steam Katawa Shoujo, **niezmodyfikowana** i na domyślnej gałęzi (nie beta Ren'Py 8).
- Pakiet zasobów HD: [`KS-HD-1.0.1-Assets-For-Building-Only.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Assets-For-Building-Only.zip) (około 700 MB).

### Budowanie

1. Sklonuj lub pobierz to repozytorium.
2. Daj narzędziu dostęp do gry na jeden z tych dwóch sposobów:
   - **Kopia gry w repozytorium:** skopiuj folder gry (ten, w którym jest `Katawa Shoujo.exe`) do katalogu
     głównego repozytorium i nazwij go `Katawa Shoujo`. Użyj kopii zrobionej przed instalacją łatki. Przy tej
     opcji instalacja Steam może pozostać spatchowana podczas budowania.
   - **Instalacja Steam:** jeśli w repozytorium nie ma kopii, narzędzie szuka gry w twoich bibliotekach Steam.
     Jeśli łatka jest już tam zainstalowana, najpierw użyj w Steam **Zweryfikuj spójność plików gry**.
3. Umieść `KS-HD-1.0.1-Assets-For-Building-Only.zip` w folderze `assets`, spakowany lub rozpakowany.
4. Uruchom:

```bash
python build.py
```

Narzędzie nakłada zmiany na skrypty i tworzy `KS-HD-1.0.1-Steam-Patch.zip` obok `build.py`. Ten zip to łatka:
zainstaluj ją zgodnie z opisem w sekcji „Instalacja”.

Jeśli skrypt nie zgadza się z tym, czego oczekuje łatka, budowanie zostaje przerwane z informacją, którego
skryptu dotyczy problem. Dzieje się tak, gdy pliki gry zostały zmodyfikowane lub pochodzą z innej wersji.

### Jak to działa

Łatka HD zmienia w skryptach gry tylko kilka rzeczy: rozdzielczość, pozycje, przybliżenia, panoramy i układ
interfejsu, a także rozmiar okna opisany w sekcji „Nowości w tej edycji”. Te zmiany są zapisane jako czytelne
dane w `kshd/edits`, po jednym pliku JSON na skrypt:

- **`code`**: zamiany w kodzie interfejsu, każda z dokładnym oryginalnym tekstem i liczbą wystąpień, jaka musi
  się zgadzać, aby wykryć niewłaściwą wersję gry zamiast źle ją spatchować.
- **`nodes`**: zmiany instrukcji scen (`show`, `scene` i transformacji ATL), odnajdywanych po etykiecie i
  oryginalnej zawartości, aby ten sam plik działał dla wszystkich 11 języków.

| Plik | Rola |
|---|---|
| `build.py` | Znajduje grę i zasoby, równolegle nakłada zmiany na skrypty i tworzy zip z łatką. |
| `kshd/edits/*.json` | Zmiany HD w postaci danych. |
| `kshd/patch.py` | Nakłada plik zmian na skrypt. |
| `kshd/tree.py` | Przechodzi przez strukturę skryptów, aby znaleźć kod i instrukcje do zmiany. |
| `kshd/rpyc.py` | Wczytuje i zapisuje skompilowane skrypty `.rpyc`, zachowując zgodność z Ren'Py 6.16. |
| `kshd/rpa.py` | Odczytuje i zapisuje archiwa `.rpa` Ren'Py. |

### Pakiet zasobów HD

Obrazy, filmy i sceny R18 są trzymane w pakiecie zasobów, oddzielnie od kodu, aby można je było ulepszać bez
ruszania kodu. Grafika HD pochodzi z [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) od
letow i została przeskalowana za pomocą waifu2x autorstwa nagadomi. Jedynym dodatkiem tej edycji są cztery
polskie panele komiksowe, wykonane tak samo jak pozostałe:

```
presplash.png    ekran ładowania
hd/              tła, sprite'y, CG, interfejs, efekty i filmy (pakowane do patch-hd.rpa)
r18/             sceny R18 i ich obrazy (pakowane do r18-hd.rpa)
```

Aby zaktualizować grafikę, rozpakuj pakiet do folderu `assets`, zastąp lub dodaj pliki, zachowując te same
nazwy i foldery, i uruchom budowanie. Aby go udostępnić, ponownie spakuj folder i prześlij go do wydania.

## Testy i opinie

Łatka przechodzi lint Ren'Py z tymi samymi ostrzeżeniami co niezmodyfikowana gra ze Steam. Menu, opcje, ekran
zapisu, galerię, opening oraz kilka scen fabularnych i R18 sprawdzono w grze, a każdą instrukcję sceny i każdą
definicję obrazu porównano z oryginalną łatką HD. Katawa Shoujo to długa gra i nie każda scena każdej ścieżki i
języka została rozegrana, więc **łatka wymaga dalszych testów**. Testowano ją tylko w systemie Windows;
zgłoszenia od graczy używających systemów Linux i macOS są szczególnie mile widziane.

Jeśli znajdziesz źle umieszczony sprite, przycięte CG, przesunięty element interfejsu lub inny problem, otwórz
issue z opisem sceny, językiem i, jeśli to możliwe, zrzutem ekranu. Wkład w projekt jest również mile widziany.

## Licencja

To nieoficjalny, niekomercyjny projekt fanowski, niezwiązany z Four Leaf Studios.
Wszystkie prawa do gry i jej zasobów należą do ich właścicieli.

## Podziękowania

- **[letow](https://github.com/letow)**, autor
  [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) („Remastered by Letow”). letow
  przeskalował każdy zasób, przeprojektował interfejs na 16:9 i wykonał poprawki scen, na których opiera się ten
  port.
- **[Four Leaf Studios](https://www.katawa-shoujo.com/)**, twórcy Katawa Shoujo.
- **[nagadomi](https://github.com/nagadomi)**, autor **waifu2x**, narzędzia AI do skalowania użytego w
  oryginalnej łatce HD.
- **Novellae Subs** (tłumaczenie rosyjskie) i **HikariTranslations** (tłumaczenie niemieckie), wymienieni w
  oryginalnej łatce HD.
- **Valjean_Lafitte**, wymieniony jako inspiracja w oryginalnej łatce HD.
