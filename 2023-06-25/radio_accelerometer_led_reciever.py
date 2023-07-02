# Imports go at the top
from microbit import *
import radio

radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    x_value = radio.receive()
    if x_value != None:
        if int(x_value) >= 0 and int(x_value) <= 1023:
            pin0.write_analog(int(x_value))
    