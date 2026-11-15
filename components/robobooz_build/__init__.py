"""ROBOBOOZ: compileropties voor de grote LVGL-displays.

ESPHome zet de hele yaml in één main.cpp. Bij een grote configuratie raken
'literals' dan buiten bereik van de l32r-instructie van de ESP32-S3:
  dangerous relocation: l32r: literal target out of range
-mauto-litpools laat de assembler de literals tussen de code zetten
(impliceert -mtext-section-literals), zodat de afstand altijd klopt.
esphome->build_flags geeft op de native ESP-IDF-build alleen -D/-W door,
daarom gaat het via dit kleine component.
"""
import esphome.codegen as cg
import esphome.config_validation as cv

CONFIG_SCHEMA = cv.Schema({})


async def to_code(config):
    cg.add_cxx_build_flag("-mauto-litpools")
