# Python bevezetés

## Python

```
python -m venv venv
```

## Git használat

Git repo létrehozása parancssorból:

```
git init
```

Felhasználó beállítása:

```
git config --global user.name trainer
git config --global user.email trainer@training360.com
```

Aktuális állapot lekérése:

```
git status
```

A könyvtárban lévő összes fájl hozzáadása:

```
git add .
```

Egy fájl hozzáadása:

```
git add README.txt
```

Összes hozzáadott commitolása:

```
git commit -m "Módosítások szöveges leírása"
```

Áttöltés a távoli repo-ba:

```
git push origin master
```

Letöltés a távoli repo-ból:

```
git pull
```

Távoli repo alapján lokális repo létrehozása:

```
git clone https://github.com/Training360/pr-pyb-2022-05-09
```

Lokális repo és távoli összekötése:

```
git remote add origin https://github.com/Training360/pr-pyb-2022-05-09
```
