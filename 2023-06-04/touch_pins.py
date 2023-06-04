from microbit import *

while True:
    if pin0.is_pressed():
        pin14.write_digital(1)
    else:
        pin14.write_digital(0)
