"""raumwert plus: Stil für Python-Programme laden.

Holt raumwert.css, tokens.css, tokens.json, Logo und Schriften von GitHub Pages und behält eine
Kopie im Ordner `stil_cache`. Ist GitHub nicht erreichbar, nimmt das Programm die letzte Kopie.
So ändert eine Anpassung im Repository alle Programme beim nächsten Start, und ein PDF entsteht
trotzdem, wenn das Internet einmal fehlt.

Verwendung:
    import raumwert_stil as stil
    css = stil.css()                 # ganzer Stil als Text, zum Einbetten in HTML
    t = stil.tokens()                # Farben und Masse als dict
    logo = stil.datei("assets/logo.png")
"""
import json
import time
from pathlib import Path

import requests

BASIS = "https://skraumwertplus.github.io/raumwert-design/"
CACHE = Path(__file__).resolve().parent / "stil_cache"
DATEIEN = ["css/tokens.css", "css/raumwert.css", "css/druck.css", "tokens.json",
           "assets/logo.png", "assets/logo_web.png",
           "fonts/Montserrat-Variable.woff2", "fonts/Montserrat-Italic-Variable.woff2"]
MAX_ALTER_S = 6 * 3600  # Kopie höchstens 6 Stunden lang ohne Nachfrage verwenden


def _hole(rel, erzwingen=False):
    ziel = CACHE / rel
    frisch = ziel.exists() and time.time() - ziel.stat().st_mtime < MAX_ALTER_S
    if frisch and not erzwingen:
        return ziel
    try:
        r = requests.get(BASIS + rel, timeout=15)
        r.raise_for_status()
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_bytes(r.content)
    except Exception:  # noqa: BLE001  ohne Netz: letzte Kopie verwenden
        if not ziel.exists():
            raise
    return ziel


def aktualisieren():
    """Alle Dateien neu laden (z.B. beim Programmstart)."""
    for rel in DATEIEN:
        try:
            _hole(rel, erzwingen=True)
        except Exception:  # noqa: BLE001
            pass


def datei(rel):
    """Pfad zur lokalen Kopie einer Datei aus dem Repository."""
    return _hole(rel)


def tokens():
    return json.loads(_hole("tokens.json").read_text(encoding="utf-8"))


def css(mit_druck=True):
    """Stil als ein Text, mit lokalen Pfaden zu den Schriften, für Chrome-PDF oder eingebettetes HTML."""
    teile = [_hole("css/tokens.css").read_text(encoding="utf-8"),
             _hole("css/raumwert.css").read_text(encoding="utf-8").replace('@import url("tokens.css");', "")]
    if mit_druck:
        teile.append(_hole("css/druck.css").read_text(encoding="utf-8"))
    text = "\n".join(teile)
    for f in ("Montserrat-Variable.woff2", "Montserrat-Italic-Variable.woff2"):
        text = text.replace(f"../fonts/{f}", _hole(f"fonts/{f}").as_uri())
    return text
