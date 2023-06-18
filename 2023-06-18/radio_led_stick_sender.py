from microbit import *
import radio

# Turn on the radio
radio.on()

while True:
    r_value = input("Enter the red value for the LED (0-255)\n")
    g_value = input("Enter the green value for the LED (0-255)\n")
    b_value = input("Enter the blue value for the LED (0-255)\n")

    radio.send("r" + r_value + "g" + g_value + "b" + b_value)