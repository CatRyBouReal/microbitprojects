from microbit import *

while True:
    pin0.write_analog(1023)
    sleep(1000)
    pin0.write_analog(512)
    sleep(1000)
    pin0.write_analog(0)
    sleep(1000)
