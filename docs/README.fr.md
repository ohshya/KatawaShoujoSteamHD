<p align="center">
  <img src="../hd-logo.webp" alt="Katawa Shoujo HD Patch - Steam Edition logo" width="420">
</p>

# Katawa Shoujo HD Patch — Steam Edition (1080p)

<p align="center">
  :gb: <a href="../README.md">English</a> ·
  :es: <a href="README.es.md">Español</a> ·
  :fr: <b>Français</b> ·
  :jp: <a href="README.ja.md">日本語</a> ·
  :de: <a href="README.de.md">Deutsch</a> ·
  :kr: <a href="README.ko.md">한국어</a> ·
  :poland: <a href="README.pl.md">Polski</a> ·
  :brazil: <a href="README.pt-BR.md">Português (Brasil)</a> ·
  :ru: <a href="README.ru.md">Русский</a> ·
  :cn: <a href="README.zh-CN.md">简体中文</a> ·
  :taiwan: <a href="README.zh-TW.md">繁體中文</a>
</p>

**Jouez à la version Steam de Katawa Shoujo en 1920×1080 grand écran, R18 inclus.**

Un patch non officiel réalisé par des fans qui fait tourner la version Steam de **Katawa Shoujo**, le visual
novel de Four Leaf Studios, en **Full HD (1920×1080, grand écran 16:9)** au lieu de sa résolution d'origine de
800×600 (4:3). Les décors, les sprites des personnages, les CG, l'interface et les vidéos sont remplacés par des
versions HD. Il fonctionne avec le moteur Ren'Py 6.16 de la version Steam, dans ses 11 langues.

**[Télécharger la dernière version](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest)**

> Il s'agit d'une adaptation du [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) de **letow**.
> Toutes les illustrations HD (décors, sprites, CG, interface, effets et vidéos) viennent de ce projet. Les crédits
> complets se trouvent à la fin.

## Nouveautés de cette édition

Fonctionnalités exclusives à cette édition, absentes du patch HD d'origine :

- **Les 11 langues de Steam.** Le patch d'origine couvrait l'anglais, l'espagnol, le français et le japonais,
  avec l'allemand et le russe en extra. Cette édition ajoute le coréen, le polonais, le portugais du Brésil et
  le chinois simplifié et traditionnel, y compris leurs scènes R18. Les quatre panneaux de bande dessinée en
  polonais (`comic_vfx*_pl`), absents du patch d'origine, ont été réalisés en HD de la même façon que ceux des
  autres langues.
- **Compatibilité avec la version Steam.** Les ajustements HD (résolution, positions, zooms, panoramiques,
  disposition de l'interface) sont appliqués par-dessus les scripts Steam au lieu de les remplacer, donc les
  fonctions de Steam continuent de marcher : succès, prise en charge de la manette, l'option R18 et les fichiers
  de langue empaquetés.
- **Patch R18 en HD.** `r18-hd.rpa` remplace le `r18.rpa` officiel avec les mêmes scènes en HD.
- **Écran des langues défilant.** Il garde la disposition HD et défile pour que les 11 langues tiennent.
- **Fenêtre adaptée à l'écran.** Le jeu s'ouvre dans une fenêtre centrée à 90 % de la zone utile du bureau
  (sans la barre des tâches ni la barre de titre), entre 1280×720 et 1920×1080 et jamais plus grande que
  l'écran. Le plein écran fonctionne comme avant.
- **Base du jeu plus récente.** Construit sur les scripts Steam actuels (v1.3.2) au lieu de Katawa Shoujo
  1.3/1.3.1, donc les corrections ultérieures du jeu sont conservées.
- **Archives au lieu de fichiers séparés.** Les ressources HD sont livrées dans deux archives `.rpa` :
  installer ou retirer le patch consiste simplement à ajouter ou supprimer des fichiers.

## Description

Le patch HD d'origine a été conçu pour la version StandAlone de Katawa Shoujo (Ren'Py 6.10), qui inclut le
contenu pour adultes dans le jeu lui-même. La version Steam utilise un Ren'Py plus récent (6.16.5), déplace ce
contenu dans un patch R18 séparé (`r18.rpa`) avec les illustrations d'origine en 4:3 et ajoute ses propres
fonctionnalités. C'est pourquoi le patch d'origine fait planter la version Steam.

Cette édition apporte le même remaster HD à la version Steam et inclut le patch R18 en HD.

### Changements visuels

Cette édition est une adaptation du code : elle n'apporte aucun changement visuel, le jeu a donc le même
aspect qu'avec le patch HD d'origine. Pour voir les comparaisons avant/après, consultez le [dépôt du Katawa
Shoujo HD Patch d'origine](https://github.com/letow/KatawaShoujoHDPatch).

## Langues disponibles

Anglais, espagnol, français, japonais, allemand, coréen, polonais, portugais du Brésil, russe, chinois
simplifié et chinois traditionnel : les 11 langues de la version Steam.

## Installation

Aucun installateur nécessaire.

> **Téléchargez le patch depuis la page [Releases](https://github.com/ohshya/KatawaShoujoSteamHD/releases/latest).**
> Le dépôt contient l'outil de compilation ; les archives HD (`patch-hd.rpa`, environ 660 Mo, et `r18-hd.rpa`)
> se trouvent uniquement dans le zip de la release.

1. Téléchargez [`KS-HD-1.0.1-Steam-Patch.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Steam-Patch.zip) depuis la dernière release.
   C'est le seul fichier nécessaire pour jouer. L'autre, `Assets-For-Building-Only`, sert uniquement à
   compiler le patch vous-même.
2. Dans Steam, faites un clic droit sur **Katawa Shoujo** > **Gérer** > **Parcourir les fichiers locaux**.
3. Extrayez le zip dans ce dossier (celui qui contient `Katawa Shoujo.exe`).
4. Quand c'est demandé, choisissez **remplacer tous les fichiers**.
5. Lancez le jeu depuis Steam.

**Linux et macOS :** le patch remplace uniquement des données du jeu (scripts et archives), identiques sur tous
les systèmes. Sous Linux, les étapes sont les mêmes. Sous macOS, **Parcourir les fichiers locaux** ouvre un
dossier contenant l'application du jeu : faites un clic droit dessus, choisissez **Afficher le contenu du
paquet** et fusionnez le dossier `game` du zip avec le dossier `game` qui s'y trouve.

Le `r18.rpa` officiel n'est pas nécessaire. S'il est déjà dans le dossier, vous pouvez le laisser ; le jeu
utilise la version HD.

**Pour désinstaller :** supprimez `game/patch-hd.rpa` et `game/r18-hd.rpa`, puis dans Steam allez dans
**Propriétés** > **Fichiers installés** > **Vérifier l'intégrité des fichiers du jeu**.

> Une mise à jour de Steam peut écraser les scripts patchés. Dans ce cas, extrayez à nouveau le patch.

> **Utilisez la branche Steam par défaut.** Le patch est conçu pour la version principale du jeu (Ren'Py 6.16).
> Il ne fonctionne pas encore avec la bêta **modern - Ren'Py 8 branch** : si vous l'avez sélectionnée, revenez à
> la branche par défaut dans **Propriétés** > **Bêtas** avant d'installer le patch. La prise en charge de la
> branche Ren'Py 8 est en cours.

### Contenu du zip de la release

| Fichier | Description |
|---|---|
| `game/patch-hd.rpa` | Décors, sprites, CG, interface, effets et vidéos en HD. |
| `game/r18-hd.rpa` | Le patch R18 en HD. Remplace le `r18.rpa` officiel. |
| `game/*.rpyc` | Scripts du jeu Steam avec les ajustements de disposition HD, pour les 11 langues. |
| `game/presplash.png` | Écran de chargement du patch HD. |

## FAQ

**Fonctionne-t-il avec la branche « modern - Ren'Py 8 branch » de Steam ?**
Pas encore ; sa prise en charge est en cours. Le patch est conçu pour la branche par défaut (Ren'Py 6.16), et la
bêta Ren'Py 8 utilise un autre format de scripts : installer ce patch dessus casserait le jeu.

**Ai-je besoin du patch R18 officiel (`r18.rpa`) ?**
Non. `r18-hd.rpa` contient déjà les scènes R18 en HD, et l'option du jeu pour les désactiver fonctionne
toujours.

**Est-ce la même chose que le Katawa Shoujo HD Patch de letow ?**
Il utilise les mêmes illustrations HD et les mêmes ajustements de scènes, adaptés à la version Steam, plus les
changements listés dans « Nouveautés de cette édition ». Le patch d'origine de letow est conçu pour la version
StandAlone et plante sur Steam.

**Fonctionne-t-il sous Linux, macOS ou sur Steam Deck ?**
Normalement oui : le patch ne modifie que des données du jeu, identiques sur tous les systèmes. Il n'a été testé
que sous Windows pour l'instant, donc les retours sont les bienvenus.

**Comment revenir au jeu d'origine ?**
Supprimez `game/patch-hd.rpa` et `game/r18-hd.rpa`, puis utilisez **Vérifier l'intégrité des fichiers du jeu**
dans Steam.

## Compiler depuis les sources

Le dépôt contient le code qui génère le patch : les modifications HD enregistrées sous forme de données et un
outil qui les applique à votre propre copie du jeu. Les fichiers du jeu et les illustrations HD ne sont pas
inclus.

L'outil existe par souci de transparence, pour que chacun puisse voir exactement ce que le patch modifie et le
recompiler. Adapter le patch HD a demandé d'extraire des informations de la version StandAlone de Katawa
Shoujo, de la version Steam, du `r18.rpa` officiel et du patch HD pour StandAlone, puis de les comparer pour
trouver chaque modification du patch HD. Ces modules d'extraction n'ont servi qu'une fois et ont été laissés de
côté : leur résultat est enregistré dans `kshd/edits`.

### Utilisation de l'IA

Le portage lui-même a été un processus long et désorganisé, avec des quantités massives de code de test jetable
et d'expérimentations. Publier les outils d'origine, écrits à la main au fil du travail, n'était pas viable et
n'aurait servi à rien. L'outil de compilation de ce dépôt a donc été créé avec **Claude (Opus 5.5)**,
d'Anthropic, afin d'offrir un moyen propre et fiable de compiler le patch à partir des données issues du
portage.

### Prérequis

- [Python](https://www.python.org/) 3.9 ou plus récent. Aucun paquet supplémentaire n'est nécessaire.
- La version Steam de Katawa Shoujo, **non modifiée** et sur la branche par défaut (pas la bêta Ren'Py 8).
- Le paquet de ressources HD : [`KS-HD-1.0.1-Assets-For-Building-Only.zip`](https://github.com/ohshya/KatawaShoujoSteamHD/releases/download/v1.0.1/KS-HD-1.0.1-Assets-For-Building-Only.zip) (environ 700 Mo).

### Compilation

1. Clonez ou téléchargez ce dépôt.
2. Donnez à l'outil accès au jeu, de l'une de ces deux façons :
   - **Une copie du jeu dans le dépôt :** copiez le dossier du jeu (celui qui contient `Katawa Shoujo.exe`) à la
     racine du dépôt et nommez-le `Katawa Shoujo`. Utilisez une copie faite avant d'installer le patch. Avec
     cette option, l'installation Steam peut rester patchée pendant la compilation.
   - **L'installation Steam :** s'il n'y a pas de copie dans le dépôt, l'outil cherche le jeu dans vos
     bibliothèques Steam. Si vous y avez déjà installé ce patch, utilisez d'abord **Vérifier l'intégrité des
     fichiers du jeu** dans Steam.
3. Placez `KS-HD-1.0.1-Assets-For-Building-Only.zip` dans le dossier `assets`, compressé ou extrait.
4. Exécutez :

```bash
python build.py
```

L'outil patche les scripts et crée `KS-HD-1.0.1-Steam-Patch.zip` à côté de `build.py`. Ce zip est le patch :
installez-le comme décrit dans « Installation ».

Si un script ne correspond pas à ce que le patch attend, la compilation s'arrête et indique lequel : cela
arrive quand les fichiers du jeu ont été modifiés ou appartiennent à une autre version.

### Fonctionnement

Le patch HD ne modifie que quelques éléments des scripts du jeu : la résolution, les positions, les zooms, les
panoramiques et la disposition de l'interface, ainsi que la taille de la fenêtre décrite dans « Nouveautés de
cette édition ». Ces modifications sont enregistrées sous forme de données lisibles dans `kshd/edits`, un
fichier JSON par script :

- **`code`** : remplacements dans le code de l'interface, chacun avec le texte d'origine exact et le nombre de
  fois où il doit apparaître, afin de détecter une mauvaise version du jeu au lieu de mal la patcher.
- **`nodes`** : modifications des instructions de scène (`show`, `scene` et transformations ATL), repérées par
  leur label et leur contenu d'origine, afin que le même fichier serve pour les 11 langues.

| Fichier | Rôle |
|---|---|
| `build.py` | Trouve le jeu et les ressources, patche les scripts en parallèle et crée le zip du patch. |
| `kshd/edits/*.json` | Les modifications HD, sous forme de données. |
| `kshd/patch.py` | Applique un fichier de modifications à un script. |
| `kshd/tree.py` | Parcourt la structure des scripts pour trouver le code et les instructions à modifier. |
| `kshd/rpyc.py` | Charge et enregistre les scripts compilés `.rpyc`, en restant compatible avec Ren'Py 6.16. |
| `kshd/rpa.py` | Lit et écrit les archives `.rpa` de Ren'Py. |

### Paquet de ressources HD

Les images, les vidéos et les scènes R18 sont conservées dans le paquet de ressources, séparées du code, afin
de pouvoir les améliorer sans y toucher. Les illustrations HD viennent du [Katawa Shoujo HD
Patch](https://github.com/letow/KatawaShoujoHDPatch) de letow, agrandies avec waifu2x de nagadomi. Les seuls
ajouts de cette édition sont les quatre panneaux de bande dessinée en polonais, réalisés de la même façon que
les autres :

```
presplash.png    écran de chargement
hd/              décors, sprites, CG, interface, effets et vidéos (empaquetés dans patch-hd.rpa)
r18/             scènes R18 et leurs images (empaquetées dans r18-hd.rpa)
```

Pour mettre à jour les illustrations, extrayez le paquet dans le dossier `assets`, remplacez ou ajoutez des
fichiers en gardant les mêmes noms et dossiers, puis lancez la compilation. Pour le partager, recompressez le
dossier et publiez-le dans une release.

## Tests et retours

Le patch passe le lint de Ren'Py avec les mêmes avertissements que le jeu Steam non modifié. Les menus, les
options, l'écran de sauvegarde, la galerie, l'opening et plusieurs scènes de l'histoire et R18 ont été vérifiés
en jeu, et chaque instruction de scène et chaque définition d'image a été comparée au patch HD d'origine.
Katawa Shoujo est un long jeu et toutes les scènes de toutes les routes et langues n'ont pas été jouées, donc
**il a besoin de plus de tests**. Il n'a été testé que sous Windows ; les retours des joueurs sous Linux et macOS
sont particulièrement bienvenus.

Si vous trouvez un sprite mal placé, un CG rogné, un élément d'interface mal placé ou tout autre problème,
ouvrez une issue avec la scène, la langue et si possible une capture d'écran. Les contributions sont aussi les
bienvenues.

## Licence

Ce projet de fans est non officiel et non commercial, et n'est pas associé à Four Leaf Studios.
Tous les droits du jeu et de ses ressources appartiennent à leurs propriétaires respectifs.

## Crédits

- **[letow](https://github.com/letow)**, auteur du
  [Katawa Shoujo HD Patch](https://github.com/letow/KatawaShoujoHDPatch) (« Remastered by Letow »). letow a
  agrandi chaque ressource, redessiné l'interface en 16:9 et réalisé les ajustements de scènes sur lesquels
  repose ce portage.
- **[Four Leaf Studios](https://www.katawa-shoujo.com/)**, créateurs de Katawa Shoujo.
- **[nagadomi](https://github.com/nagadomi)**, auteur de **waifu2x**, l'outil d'agrandissement par IA utilisé
  par le patch HD d'origine.
- **Novellae Subs** (traduction russe) et **HikariTranslations** (traduction allemande), crédités dans le patch
  HD d'origine.
- **Valjean_Lafitte**, crédité comme source d'inspiration dans le patch HD d'origine.
