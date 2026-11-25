# ROBOBOOZ displays

Retro thema voor drie Guition ESP32-S3-4848S040 touch-displays (480×480) met ESPHome +
LVGL, gekoppeld aan Home Assistant (HA) en Music Assistant (MA). Elk display is één groot
YAML-bestand: `display-woonkamer.yaml`, `display-studio.yaml`, `display-jip.yaml` en
`display-slaapkamer.yaml` (nieuwe stijl "Raster & Cirkel"; apparaatnaam nog `display-test`).
De README beschrijft de functies en welke HA-entiteiten nodig zijn.

## Werkafspraken
- Schrijf in het Nederlands: commentaar, commits, README en antwoorden aan Jeroen.
- Jeroen is geen fulltime programmeur: leg kort uit wat je doet en waarom, zonder jargon.
- Een functie die op meerdere displays staat, pas je op alle displays aan waar hij hoort.
  Bewuste verschillen (zie README-tabel) laat je staan.
- De repo is openbaar: geheimen alleen via `!secret`. `secrets.yaml` staat in `.gitignore`;
  houd `secrets.example.yaml` bij als er een nieuw geheim bijkomt.
- Werk de README bij bij nieuwe functies of nieuwe benodigde HA-entiteiten.
- Geluiden en afbeeldingen voor HA staan in `www/robobooz/` (komt in `/config/www/robobooz/`).

## Valideren
- `pip install esphome` als het er niet is.
- `esphome config display-<naam>.yaml` — snelle controle. Maak zo nodig een tijdelijke
  `secrets.yaml` uit `secrets.example.yaml` met nepwaarden en verwijder die daarna.
- `esphome compile display-<naam>.yaml` vraagt ~2,5 GB RAM: één display tegelijk en alleen
  als het nodig is. `components/robobooz_build` is nodig om het linken te laten lukken.
- Installeren op de displays gaat draadloos via ESPHome Device Builder in HA; dat doet Jeroen.

## Agents (`.claude/agents/`)
- `robobooz-tester` — na elke wijziging: valideren en fouten zoeken, ook verschillen tussen de displays.
- `robobooz-ontwikkelaar` — na een nieuwe pagina of functie: review van opbouw, geheugen en HA-koppeling.
- `robobooz-gebruiker` — bij nieuwe pagina's of teksten: feedback als huisgenoot, Jip of gast.
Stel na een grotere wijziging voor om de tester en de ontwikkelaar te laten kijken.
