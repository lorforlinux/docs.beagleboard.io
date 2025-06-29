#!/usr/bin/env python
# //////////////////////////////////////
# 	internLED.py
# 	Blinks A USR LED.
# 	Wiring:
# 	Setup:
# 	See:
# //////////////////////////////////////
import gpiod
import time

LED_CHIP = 'gpiochip1'
LED_LINE_OFFSET = [21]  # USR0 run: gpioinfo | grep -i -e chip -e usr

chip = gpiod.Chip(LED_CHIP)

lines = chip.get_lines(LED_LINE_OFFSET)
lines.request(consumer='internLED.py', type=gpiod.LINE_REQ_DIR_OUT)

state =  0      # Start with LED off
while True:
    lines.set_values([state])
    state = ~state      # Toggle the state
    time.sleep(0.25)
