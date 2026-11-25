# Pläne und Schnitte in Programmen

Gilt für alle Situationspläne, Grundrisse und Schnitte, die ein Programm von raumwert plus zeichnet. Farben stehen in `css/tokens.css` unter `--rw-plan-…`.

## Gebäude

| Darstellung | Bedeutung |
|---|---|
| Dunkelgrau | Gebäude, mehrgeschossig (ab 6 m über Terrain) |
| Mittleres Grau | Tieferer Gebäudeteil (3.6 bis 6 m) |
| Hellgrau | Eingeschossig, Garage (unter 3.6 m) |
| Gleiche Abstufung, insgesamt heller | Nachbargebäude |
| Strichliert | Verdeckt oder unter Terrain (unterirdische Bauten, Vordächer, Untergeschosse) |
| Dicke schwarze Linie | First |
| Dünne schwarze Linie | Grat, Kehle, Absatz |
| Gepunktet | Dachterrasse |
| Rot | Neubau |
| Gelb, gestrichelte Kontur | Abbruch |

## Parzellen

- Eigene Parzelle mit kräftiger Grenze in Navy, Fläche hell.
- Grenzpunkte als Kreise, wie im Grundbuchplan, auch bei den Nachbarparzellen.
- Nicht bebaubare Bereiche schraffiert in Petrol.
- Grenzabstand und Baufenster gestrichelt in Navy.
- Höhenlinien des Terrains (swissALTI3D) fein in `--rw-plan-hoehenlinie`, jede fünfte Linie etwas kräftiger, beschriftet in m ü. M. ausserhalb der Gebäude. Abstand je nach Gefälle 0.5, 1, 2 oder 5 m.

## Schnitte

- Terrain als Linie in Navy, Erdreich hell.
- Grenzen als gestrichelte Senkrechte mit Grenzpunkt und Terrainhöhe in m ü. M.
- Höhenangabe nur beim Hauptbau, als Masslinie.
- Dachform aus swissBUILDINGS3D: an jeder Stelle der Schnittlinie die höchste Dachfläche, begrenzt durch den Gebäudeumriss der amtlichen Vermessung.
- Untergeschoss gestrichelt (unter Terrain). Ist es nicht vermessen, wird es bei Bauten ab 4.8 m Höhe mit 2.8 m Tiefe angenommen und so beschriftet. Garagen und eingeschossige Teile ohne UG.
- Unterirdische Bauten der amtlichen Vermessung (Tiefgaragen) gestrichelt mit 3 m Tiefe.

## Immer dabei

- Nordpfeil, Massstabsbalken, Legende mit allen verwendeten Darstellungen.
- Beschriftung Montserrat, mit weissem Rand, wo sie über Linien liegt.
- Quelle der Daten in einer kleinen Zeile unter dem Plan.
