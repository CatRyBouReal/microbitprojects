from microbit import *

while True:
    if button_a.was_pressed():
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)
