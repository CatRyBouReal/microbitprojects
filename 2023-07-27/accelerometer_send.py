# Imports go at the top
from microbit import *

uart.init(115200)

while True:
    values = {
        "x": accelerometer.get_x(),
        "y": accelerometer.get_y(),
        "z": accelerometer.get_z()
    }

    print(values)
    sleep(1000)