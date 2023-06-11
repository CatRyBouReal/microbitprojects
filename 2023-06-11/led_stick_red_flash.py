# Imports go at the top
from microbit import *
import neopixel

# Create an instance of NeoPixel on pin0 with 10 LEDs
np = neopixel.NeoPixel(pin0, 10)

# Turn off all the pixels
np.clear()

# Code in a 'while True:' loop repeats forever
while True:
    for i in range(0, 10):
        np.clear()
        np[i] = (255, 0, 0)
        np.show()
        sleep(1000)
