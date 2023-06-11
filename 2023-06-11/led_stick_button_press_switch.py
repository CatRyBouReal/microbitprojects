# Imports go at the top
from microbit import *
import neopixel
import random

# Create an instance of NeoPixel on pin0 with 10 LEDs
np = neopixel.NeoPixel(pin0, 10)

# Turn off all the pixels
np.clear()

pixel = 0
going_back = False

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        if pixel < 9 and going_back == False:
            np.clear()
            np[pixel] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            np.show()
            pixel += 1
        elif pixel == 9:
            np.clear()
            np[pixel] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            np.show()
            going_back = True
            pixel -= 1
        elif pixel < 9 and pixel >= 0 and going_back:
            np.clear()
            np[pixel] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            np.show()
            pixel -= 1
            if pixel == 0:
                going_back = False
            
