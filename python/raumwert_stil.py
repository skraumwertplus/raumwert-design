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
SCHNITTE = ["Light", "Regular", "Medium", "SemiBold", "Bold", "LightItalic", "RegularItalic", "SemiBoldItalic"]
CACHE = Path(__file__).resolve().parent / "stil_cache"
DATEIEN = ["css/tokens.css", "css/raumwert.css", "css/druck.css", "tokens.json",
           "assets/logo.png", "assets/logo_web.png",
           ] + [f"fonts/Montserrat-{n}.woff2" for n in SCHNITTE]
MAX_ALTER_S = 6 * 3600  # Kopie höchstens 6 Stunden lang ohne Nachfrage verwenden
_offline = False         # nach dem ersten Fehler nicht bei jeder Datei erneut warten


def _hole(rel, erzwingen=False):
    global _offline
    ziel = CACHE / rel
    frisch = ziel.exists() and time.time() - ziel.stat().st_mtime < MAX_ALTER_S
    if (frisch and not erzwingen) or (_offline and ziel.exists()):
        return ziel
    try:
        r = requests.get(BASIS + rel, timeout=8)
        r.raise_for_status()
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_bytes(r.content)
    except Exception:  # noqa: BLE001  ohne Netz: letzte Kopie verwenden
        _offline = True
        if not ziel.exists():
            raise
    return ziel


def farben_ersetzen(text, zuordnung):
    """Ersetzt fest eingebaute Farbwerte durch die aktuellen Werte aus tokens.json.
    zuordnung: {"#1F1D5C": "farben.navy", ...}. Hilft beim Umstellen bestehender Programme."""
    t = tokens()
    for alt, pfad in zuordnung.items():
        wert = t
        for teil in pfad.split("."):
            wert = wert[teil]
        if wert.lower() != alt.lower():
            text = text.replace(alt, wert).replace(alt.lower(), wert).replace(alt.upper(), wert)
    return text


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
    for n in SCHNITTE:
        f = f"Montserrat-{n}.woff2"
        text = text.replace(f"../fonts/{f}", _hole(f"fonts/{f}").as_uri())
    return text


def schrift_css_eingebettet():
    """@font-face mit eingebetteten Schriften (data-URL), für HTML, das als Datei weitergegeben oder als PDF gedruckt wird."""
    import base64
    import re
    text = _hole("css/tokens.css").read_text(encoding="utf-8")
    faces = re.findall(r"@font-face\s*\{[^}]*\}", text)
    out = []
    for fc in faces:
        m = re.search(r'\.\./fonts/([^"\)]+)', fc)
        if m:
            b64 = base64.b64encode(_hole("fonts/" + m.group(1)).read_bytes()).decode()
            fc = fc.replace("../fonts/" + m.group(1), "data:font/woff2;base64," + b64)
        out.append(fc)
    return "\n".join(out)
