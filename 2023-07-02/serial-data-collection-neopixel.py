# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin1, 10)

np.clear()

# Code in a 'while True:' loop repeats forever
while True:
    moisture = pin0.read_analog()
    light_ambient = display.read_light_level()
    temp = temperature()

    np.fill((int(light_ambient*1023/255), int(light_ambient*1023/255), int(light_ambient*1023/255)))
    np.show()
    
    print("Temp", temp, "Light", light_ambient, "Moisture", moisture)
    sleep(1000)
