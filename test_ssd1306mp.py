"""
SSD1306 Library for multiple font sizes
Copyright 2023-2024 . All rights reserved.
Author = Masoun Mardini
"""

import ssd1306mp.ssd1306font as LCD
from machine import Pin
import time

i2c = machine.I2C(0, sda=Pin(16), scl=Pin(17))
# Enable both screen connected ports 3, 4
i2c.writeto(0x70, b'\x0C')
lcd = LCD.ssd1306font(128, 64, i2c)


val = 0.0
while True:
    lcd.clear()
    i2c.writeto(0x70, b'\x08')
    lcd.text_fb("Test 1", 0, 0, 16)
    lcd.text_fb("{:.2f}".format(val), 0, 32, 32)
#     time.sleep_ms(50)
    lcd.show()

    i2c.writeto(0x70, b'\x04')
    lcd.text_fb("Test 2", 0, 0, 16)
    lcd.text_fb("{:.2f}".format(val), 0, 32, 32)
#     time.sleep_ms(50)
    lcd.show()
    val += 0.05
