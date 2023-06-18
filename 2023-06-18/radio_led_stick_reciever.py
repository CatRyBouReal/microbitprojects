from microbit import *
import neopixel
import radio

# Initialise a NeoPixel
np = neopixel.NeoPixel(pin0, 10)
np.clear()

# Turn on the radio
radio.on()

# r255g255b255

while True:
    led_state = radio.receive()
    if led_state != None:
        led_state = led_state.split("r")
        led_state = [led_state[0], led_state[1].split("g")]
        #led_state = [led_state[0], led_state[1].split("b")]
        led_state = [int(led_state[1][0]), int(led_state[1][1].split("b")[0]), int(led_state[1][1].split("b")[1])]

        np.clear()
        np[0] = (led_state[0], led_state[1], led_state[2])
        np.show()