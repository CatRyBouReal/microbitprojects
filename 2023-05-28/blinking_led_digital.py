from microbit import *

while True:
    # Fully power a device connected to pin 0
    pin0.write_digital(1)
    sleep(1000)
    # Remove all power from a device connected to pin 0
    pin0.write_digital(0)
    sleep(1000)
