from microbit import *
import radio

# Turn on the radio
radio.on()

while True:
    led_state = radio.recieve()
    if led_state != None:
        pin0.write_digital(int(led_state))
