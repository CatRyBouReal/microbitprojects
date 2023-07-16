import time
import serial
from matplotlib import pyplot


baudrate = 115200
s = serial.Serial('COM6', baudrate)
pyplot.ion()

time_values = []
ambient_light_values = []

while True:
    time = time.time()
    ambient_light = int(sr.readline().decode('utf-8'))
    
    time_values.append(t0)
    ambient_light_values.append(ambient_light)
    
    pyplot.plot(time_values, ambient_light_values)
    pyplot.show()
    pyplot.pause(0.001)