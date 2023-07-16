# Imports go at the top
from microbit import *

uart.init(115200)

# Code in a 'while True:' loop repeats forever
while True:
    print(display.read_light_level())

    sleep(3000)
