#!/usr/bin/env python
# ////////////////////////////////////////
# //	pushbutton.py
# //      Reads P9_42 and prints its value.
# //	Wiring:	Connect a switch between P9_42 and 3.3V
# //	Setup:	
# //	See:	
# ////////////////////////////////////////
import time
import gpiod
import os

ms = 100    # Read time in ms
CHIP = 'gpiochip0'
LINE_OFFSET = [7] #  P9_42 is gpio 7
chip = gpiod.Chip(CHIP)
lines = chip.get_lines(LINE_OFFSET)
lines.request(consumer='pushbutton.py', type=gpiod.LINE_REQ_DIR_IN)

while True:
    data = lines.get_values()
    print('data = ' + str(data[0]))
    time.sleep(ms/1000)
