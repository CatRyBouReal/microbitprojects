# Imports go at the top
from microbit import *
from machine import time_pulse_us
from time import sleep_us

def sense_distance():
    trigger_pin = pin0
    reflected_echo_pin = pin0

    trigger_pin.write_digital(0)
    trigger_pin.write_digital(1)
    sleep_us(10)
    trigger_pin.write_digital(0)
    sleep_us(2)
    time_us = time_pulse_us(reflected_echo_pin, 1)
    return (time_us / 1000000) * 343

uart.init(115200)

# Code in a 'while True:' loop repeats forever
while True:
    print(sense_distance())
    sleep(2000)
