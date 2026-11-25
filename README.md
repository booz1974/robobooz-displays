# ROBOBOOZ

Retro thema voor **Guition ESP32-S3-4848S040** (4", 480×480) touch displays met ESPHome + LVGL, gekoppeld aan Home Assistant en Music Assistant.

Ontwerp en idee: **Jeroen van Sonsbeek**

## Displays

| Bestand | Ruimte | Bijzonderheden |
|---|---|---|
| `display-woonkamer.yaml` | Woonkamer | TV-pagina, kachel-animatie, lampen woonkamer/keuken/eettafel, speler Yamaha woonkamer |
| `display-studio.yaml` | Studio | ON AIR, PC-pagina (Studio aan/uit), lampen studio/zolder/burolamp, speler Studio mini |
| `display-jip.yaml` | Slaapkamer Jip | RACE-thema met finishvlag, Kachel-pagina (paneel aan met timerkeuze 15/30/60 min, uit met één tik, kamertemperatuur en gewenste temperatuur instellen, vonkjes/vlokjes op de kamertegel), NIET STOREN, nieuw paneel met 1 relais (aanraakcalibratie 0..479), intercom naar de kijkpaal, speler kijkpaal |
| `display-slaapkamer.yaml` | Slaapkamer Maartje en Jeroen (apparaat `display-test`) | **Nieuwe stijl "Raster & Cirkel"** (v0.13): papierwit, Inter Tight + IBM Plex Mono, cirkels in vermiljoen en ultramarijn. Thuis (met LICHT UIT), Licht, Sfeer, Nu speelt (met hoes), Kamer, Weer, **Wekker** (+ wekkergeluid; afgaan-scherm met tijd, SLUIMER -/+ en STOP; volume 50% → 100%, Alarm 100%) en Menu. Spelerbalk bovenin, onderbalk met **LICHT** (lampen aan/gedimd/uit, scherm normaal/nachtstand/slapen, avondstand). Tikken: slapen → nachtstand (klok + wekkertijd) → normaal; 's nachts (21–6) na 1 min vanzelf slapen, avondstand en gedimd. Toont "geen verbinding met HA" als HA weg is. Paneel met 1 relais (aanraakcalibratie 0..479); relais niet ingesteld |

## Functies

- Thuisscherm met klok, datum en NOS-nieuws (3 regels), live ticker, weer, energie (incl. energiekosten vandaag en ZON/NET live) en nu-speelt met VU-meter
- Klik op de klok: alle lampen aan/uit
- Favorieten: alle favoriete radiozenders (links) en playlists (rechts) uit Music Assistant, meest gespeeld bovenaan, scrollbaar, met albumart en volumeslider van de eigen speler
- Nu speelt-popup en wachtrij
- Lampen, Sfeer (scènes + Alles uit / Random kleuren), Klimaat, Huis, Energie, Schakelaars
- 8 thema's (A–D, NEC, Oranje, NMHC, Disco) met automatisch wedstrijdthema; display Jip heeft RACE in plaats van Disco en kiest zijn thema zelf
- Menu met kaarten, ook Nachtstand (dimme klok met sterren)
- Dimmen: 1 min → 65 %, 2 min → 35 %, 30 min → nachtstand; eerste tik maakt alleen wakker
- Automatische nachtstand tussen 23:00 en 06:00, behalve als er muziek speelt of er nog lampen aan zijn
- Alle displays: pagina Home Assistant (services als modules, CPU/geheugen/schijf-meters, temperatuur, 24-uursgrafiek, terminal)
- Weerpagina (alle displays): regen voor de komende 2 uur (12 balkjes van 10 minuten, Buienradar) met het weericoon van nu als watermerk (doorzichtig, achter de balkjes)
- Alle displays: op Energie opent de tegel *Bespaard door zon vandaag* de pagina Zonnestroom (live zon / huis / net met lopende bolletjes, 'goed moment om te wassen')
- Woonkamer: op de weerpagina ook een paneel voor de zonwering eettafel: OMHOOG / STOP / OMLAAG, de stand in blokjes en een venstertje waarin het doek meebeweegt, met de batterij erin; woorden onder de knoppen en 'BATTERIJ LAADT OP' / 'BIJNA LEEG' in de standregel
- Woonkamer: pagina Plantenkas (4 planten; de pot is de vochtmeter, met status TOP / TE NAT / DORST, temperatuur en batterij)
- Studio: geheime Intercom naar parallelle universums (tik op het satellietblok in de LIVE-balk): kanaalkiezer met 12 kanalen (o.a. 9 Wekkerbrigade, 10 Keukenkazerne, 11 Shampoo-Commando, 12 Fluisterwekker), PUSH TO TALK, ruis + bericht via ElevenLabs als aankondiging op de studiospeaker (`script.intercom_zend`, `input_text.intercom_log`; geluiden in `www/robobooz/`, kanaal 12 begint met een zacht melodietje `intro_12.mp3`)
- Alle intercomschermen: kies de ontvanger (HIER of een andere kamer); PUSH TO TALK stuurt het kanaal van de draaischijf daarheen (`script.intercom_zend`, veld `naar`), het telefoonvak een oproep van Jeroen (`script.intercom_bel`). Berichten klinken op hetzelfde volume als de muziek op die speler
- Woonkamer: dezelfde Intercom, maar alleen bereikbaar als woonkamer, woonkamer totaal of eettafel speelt of klaar staat (dan toont het LIVE-blok een satelliet); het bericht gaat naar de speler die speelt
- Jip: muziek alleen van de kijkpaal (Music Assistant kent hem twee keer; beide spelers worden gevolgd); speelt de kijkpaal, dan na 30 s niets aanraken automatisch Nu speelt (een slapend scherm blijft tussen 23:00 en 07:00 uit), en 30 s na het stoppen terug naar Thuis
- Jip: Kachel-pagina voor `climate.paneel_jip` (`script.paneel_jip_timer_starten`, `script.paneel_jip_uit`, `binary_sensor.paneel_jip_aan`, `sensor.paneel_jip_resterend`), NIET STOREN (`input_boolean.jip_niet_storen`), intercom op de kijkpaal (`script.intercom_zend` met `speler`)
- Radio: bij reclame ('Advert') een eigen hoes "Commercial Break" (zet `www/robobooz/` uit deze repo in `/config/www/robobooz/`)
- LIVE-ticker: AI-roast plus bijzonderheden van server (service uit, CPU heet/druk) en planten (dorst, te koud/warm, batterij bijna leeg)

## Installeren

1. Zet de bestanden in je ESPHome-configmap (HA: `/config/esphome/`), inclusief de mappen `display/` en `components/`.
   `components/robobooz_build` is een klein lokaal component dat een compileroptie aanzet; zonder die optie faalt het linken van deze grote configuratie (`l32r: literal target out of range`).
2. Kopieer `secrets.example.yaml` naar `secrets.yaml` en vul je waarden in (wifi, de adressen van HA en Music Assistant (`ha_url`, `ma_url`), Music Assistant-token, API-/OTA-sleutels en de namen + `person.`-entiteiten van de huisgenoten).
3. De afbeeldingen in `display/` staan al in deze repo. `oranje.jpg` wordt lokaal gelezen; de kachelanimaties `vuur12.gif` en `sneeuw12.gif` (12 frames) haalt de build van GitHub. `vuur.gif` en `sneeuw.gif` zijn de oude, grote versies en worden niet meer gebruikt.
4. Installeer via ESPHome Device Builder (draadloos). Bouw één display tegelijk: het compileren vraagt ~2,5 GB RAM.
5. Een nieuw paneel de eerste keer via USB flashen ("Aansluiten op deze computer"); daarna kan het draadloos.

### ESPHome-versie en geheugen

- Getest met ESPHome **2026.11.0** (ESP-IDF 5.5.6).
- Alle displays hebben `esp32 > framework > advanced > loop_task_stack_size: 16384`. Met de standaard 8 KB liep de hoofdtaak bij het opstarten over (alle pagina's worden in één keer aangemaakt, ~8,5 KB nodig): crash 'Abort' op core 1 en een OTA-rollback.
- Diagnose in HA per display: *Stapel hoofdtaak vrij* (moet ruim boven ~5000 B blijven) en *Intern RAM vrij* (woonkamer is het krapst, ~25 kB; onder ~15 kB gaan https-hoesjes mis).
- Zuinig: themacontrole elke 5 s, Music Assistant elke 3 s als er muziek speelt of een muziekpagina open is, anders elke 12 s.

### Nodig in Home Assistant

Zet bij elk display in HA de ESPHome-integratie op *Configureren → "Sta het apparaat toe Home Assistant-acties uit te voeren"*.

**Alle displays**
- Music Assistant (app) op `http://<ha-ip>:8095` met API-token (`ma_api_token`); favorieten en spelers worden rechtstreeks uit Music Assistant gehaald
- Thema en teksten: `input_select.display_thema` (A–H), `input_text.nieuws_display` (NOS-feed), `input_text.display_roast`, `input_text.intercom_log`
- Weer: `weather.de_scholekster`, `input_text.weer_uren_display`, `input_text.weer_dagen_display`, `sensor.neerslag_buienradar_regen_data` (Neerslag-app, attribuut `data`)
- Goedemorgen: `input_text.ochtend_info_display`, `input_text.ochtend_agenda_display`
- Energie: `sensor.energiekosten_vandaag` / `_maand`, `sensor.stroomkosten_*`, `sensor.gaskosten_*`, `sensor.waterkosten_*`, `sensor.zonnepanelen_bespaard_vandaag`, `sensor.huisverbruik_nu`, `sensor.dle3a27053_generated_energy_today`
- Zonnestroom en ZON/NET op Thuis: `sensor.dle3a27053_pv_output_actual` (omvormer) en `sensor.p1_meter_3c39e7240afe_active_power` (P1)
- Server (pagina Home Assistant): `input_text.server_info_display`, `input_text.server_hist_cpu`, `input_text.server_hist_temp` (automatiseringen *Displays - serverinfo* en *servergeschiedenis*) en de System Monitor-sensoren `sensor.processor_use`, `sensor.processor_temperature`, `sensor.memory_use_percent`, `sensor.disk_use_percent`, `sensor.disk_free`
- Huis en deurbel: `binary_sensor.voordeur_ringing`, `camera.voordeur`, `image.voordeur_event_image`, `binary_sensor.regensensor_new`, `binary_sensor.tuinpoortdeur`, `binary_sensor.deursensor_schuur_openen`, `binary_sensor.raamsensor_zolderraam_openen`, `binary_sensor.lumi_lumi_sensor_magnet_aq2_opening`
- Scripts: `script.lampen_random_kleuren`, `script.intercom_zend`, `script.intercom_bel`
- Huisgenoten: `persoon_1..3_entity` (person-entiteiten) via `secrets.yaml`

**Woonkamer**
- Lampen en sfeer: `light.woonkamer`, `light.keuken`, `light.eettafel`, `scene.woonkamer_*`
- Spelers en TV: `media_player.yamaha_living_2`, `media_player.woonkamer_totaal`, `media_player.eettafel`, `media_player.bravia_tl2`, `remote.teevee`
- Klimaat: `climate.living_room`, `sensor.shelly_blu_h_t_1e68_luchtvochtigheid`
- Zonwering: `cover.eettafel_zonwering_eettafel` (met `current_position`), `sensor.eettafel_zonwering_eettafel_batterij`, `binary_sensor.eettafel_zonwering_eettafel_opladen`
- Schakelaars: `switch.smartplug2`, `switch.zbeacon_ts011f_4`
- Planten en wedstrijd: `input_text.planten_display` (automatisering *Displays - planten*), `input_text.wedstrijd_display`

**Studio**
- Lampen en sfeer: `light.studio`, `light.burolamp`, `light.extended_color_light_1_3`, `light.extended_color_light_1_4`, `scene.studio_*`
- Speler: `media_player.studio_mini_2`
- ON AIR en PC: `input_boolean.studio_opname_on_air`, `script.studio_pc_starten`, `script.studio_totaal_uit`, `switch.zbeacon_ts011f_2`
- Kamer: `sensor.thermo_studio_temperatuur`, `sensor.thermo_studio_luchtvochtigheid`

**Jip**
- Lampen en sfeer: `light.slaapkamer_jip_2` (groep), `light.slaapkamer_jip`, `light.lichtstrip_jip`, `light.hue_color_light_1`, `scene.slaapkamer_jip_*`
- Speler: `media_player.kijkpaal_woonkamer` (Music Assistant)
- Kachel: `climate.paneel_jip`, `script.paneel_jip_timer_starten` (optioneel veld `minuten`; anders `input_number.paneel_jip_timerduur`), `script.paneel_jip_uit`, `binary_sensor.paneel_jip_aan`, `sensor.paneel_jip_resterend`
- Kamer en rust: `sensor.thermo_slaapkamer_jip_temperatuur`, `sensor.thermo_slaapkamer_jip_luchtvochtigheid`, `input_boolean.jip_niet_storen`

**Slaapkamer (Raster & Cirkel, `display-slaapkamer.yaml`)**
- Lampen en sfeer: `light.slaapkamer_jeroen_maartje` (groep), `light.slaapkamer_jeroen_en_maartje`, `light.slaapkamer_lichtstrip`, `scene.slaapkamer_jeroen_maartje_helder` / `_gedimd` / `_lezen` / `_ontspannen` / `_nachtlampje` / `_lentebloesem` / `_savanne_zonsondergang`
- Speler: `media_player.yamaha_living_2` (titel, artiest, album, hoes en volume via HA; voorlopig de woonkamer)
- Kamer: `sensor.thermo_slaapkamer_jeroen_maartje_temperatuur_3`, `sensor.thermo_slaapkamer_jeroen_maartje_luchtvochtigheid_3`
- Weer: `weather.de_scholekster`, `input_text.weer_uren_display`, `sensor.neerslag_buienradar_regen_data`

**Wekker (display slaapkamer)**
- Helpers: `input_datetime.wekker_slaapkamer_tijd`, `input_boolean.wekker_slaapkamer_aan`, `input_boolean.wekker_slaapkamer_lampen`, `input_boolean.wekker_slaapkamer_gaat_af`, `input_select.wekker_slaapkamer_dagen` (Werkdagen / Elke dag / Weekend), `input_select.wekker_slaapkamer_geluid`, `input_text.wekker_slaapkamer_speaker`, `input_number.wekker_slaapkamer_sluimertijd` (5–30 min, standaard 5), `input_boolean.wekker_slaapkamer_muziek_hervatten` + `input_number.wekker_slaapkamer_oud_volume` (muziek van voor de wekker gaat na STOP verder)
- Scripts en automatisering: `script.wekker_slaapkamer_afgaan`, `script.wekker_slaapkamer_stop`, `script.wekker_slaapkamer_sluimer`, `automation.wekker_slaapkamer`; Fluisterwekker en Wekkerbrigade via `script.intercom_zend` (kanaal 12 en 9)
- Let op: de wekker gaat alleen af als Home Assistant draait; het display maakt zelf geen geluid. Is HA weg, dan staat dat op Thuis, op de wekkerpagina en in de nachtstand.
- Geluiden in `www/robobooz/`: `wekker_zoemer.mp3`, `wekker_klassiek.mp3`, `wekker_alarm.mp3`, `wekker_rustig.mp3`; zonsopgang op `light.slaapkamer_jeroen_maartje`

**Optioneel**: Team Tracker-sensoren voor NEC/Oranje en een agenda voor NMHC (automatisch wedstrijdthema).

## Screenshots

De afbeeldingen in `screenshots/` zijn ontwerp-mockups.

![Overzicht](screenshots/retro2-overzicht.png)
![Favorieten](screenshots/favorieten-lijst.png)
![Studio](screenshots/studio-retro.png)
![TV](screenshots/tv-pagina.png)
![Thema's](screenshots/nieuwe-themas.png)
![Serverkamer](screenshots/serverkamer.png)
![Plantenkas](screenshots/plantenkas.png)
![Intercom](screenshots/intercom.png)
![Display Jip](screenshots/display-jip-race.png)
![Intercom Jip](screenshots/display-jip-intercom.png)
