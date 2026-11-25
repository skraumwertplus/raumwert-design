# raumwert-design

Gemeinsamer Stil für alle Programme und Berichte von raumwert plus. Eine Änderung hier gilt für jedes Programm, das diese Dateien lädt, beim nächsten Start.

Musterseite: https://skraumwertplus.github.io/raumwert-design/

## Inhalt

| Datei | Zweck |
|---|---|
| `css/tokens.css` | Die einzige Stelle mit Farben, Schriften, Grössen, Abständen und Rundungen |
| `css/raumwert.css` | Bausteine: Buttons, Karten, Kennzahlen, Tabellen, Hinweise, Legenden, Formularfelder |
| `css/druck.css` | A4-Seite, Briefkopf, Blatt am Bildschirm, Druck |
| `tokens.json` | Dieselben Werte für Python und Diagramme |
| `vorlagen/briefkopf.html` | Briefkopf der ersten Seite |
| `python/raumwert_stil.py` | Lädt den Stil in Python-Programme, mit lokaler Kopie für den Fall ohne Internet |
| `docs/plaene.md` | Darstellungsregeln für Situationspläne und Schnitte |
| `assets/` | Logo |
| `fonts/` | Montserrat in festen Schnitten Light bis Bold, auch kursiv (SIL Open Font License, siehe `fonts/OFL.txt`). Die variablen Dateien sind nur noch als Reserve da. |

## In ein Programm einbinden

**Web-Seite oder Wix-Element (HTML):**

```html
<link rel="stylesheet" href="https://skraumwertplus.github.io/raumwert-design/css/raumwert.css">
<button class="rw-button">Analyse bestellen</button>
```

**PDF-Bericht (Python):** `python/raumwert_stil.py` ins Programm kopieren.

```python
import raumwert_stil as stil
html = f"<style>{stil.css()}</style> ..."
farben = stil.tokens()["farben"]
```

Bestehende Programme mit fest eingebauten Farben stellt man mit `stil.farben_ersetzen(html, zuordnung)` um: Die Funktion ersetzt jeden alten Farbwert durch den aktuellen aus `tokens.json`. So macht es die Grundstücksanalyse.

## Regeln

1. In Programmen nur Namen verwenden, zum Beispiel `var(--rw-akzent)` oder die Klasse `rw-button`, nie den Farbwert direkt.
2. Neue Farben oder Grössen zuerst in `css/tokens.css` und `tokens.json` eintragen, dann verwenden.
3. Keine farbigen Tabellenköpfe, Schrift in Navy, Fliesstext mindestens 11 pt.
4. Pläne nach `docs/plaene.md`.

## Ändern

Datei auf GitHub öffnen, Stift-Symbol, ändern, «Commit changes». Nach etwa einer Minute ist die neue Version unter der Adresse oben online. Jede Änderung bleibt in der Versionsgeschichte und lässt sich zurücknehmen.
