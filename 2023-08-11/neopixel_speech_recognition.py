# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin1, 10)

uart.init(115200)

# Code in a 'while True:' loop repeats forever
while True:
    speech = uart.read()
    if speech != None:
        display.scroll(speech)
        if speech == b"red":
            np[0] = (255, 0, 0)
            np.show()
        elif speech == b"green" or speech == b"Green":
            np[0] = (0, 255, 0)
            np.show()
        elif speech == b"blue":
            np[0] = (0, 0, 255)
            np.show()
