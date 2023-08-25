# Imports go at the top
from microbit import *

lcw_direction = pin0
lacw_direction = pin14
rcw_direction = pin15
racw_direction = pin1

# Code in a 'while True:' loop repeats forever
while True:
    x_value = accelerometer.get_x()
    if 0 < x_value < 1023:
        pin2.write_analog(x_value)
        pin16.write_analog(x_value)
        lcw_direction.write_digital(1)
        lacw_direction.write_digital(0)
        rcw_direction.write_digital(1)
        racw_direction.write_digital(0)
    elif -1023 < x_value < 0:
        pin2.write_analog(abs(x_value))
        pin16.write_analog(abs(x_value))
        lcw_direction.write_digital(0)
        lacw_direction.write_digital(1)
        rcw_direction.write_digital(0)
        racw_direction.write_digital(1)
    
