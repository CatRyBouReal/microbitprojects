# Imports go at the top
from microbit import *
import random

# Code in a 'while True:' loop repeats forever
while True:
    if accelerometer.is_gesture('shake'):
        flicker = random.randint(0, 1)
        pin0.write_digital(flicker)
    else:
        pin0.write_digital(0)
