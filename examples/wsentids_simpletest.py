# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_wsentids import wsentids

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
wsen = wsentids.WSENTIDS(i2c)

while True:
    temp = wsen.temperature
    print(f"Temperature: {temp:.1f}°C")
    print()
    time.sleep(0.5)
