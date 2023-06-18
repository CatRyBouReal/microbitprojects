from microbit import *
import radio

# Turn on the radio
radio.on()

while True:
    led_state = input("Enter the LED state (1/0)\n")
    radio.send(led_state)
