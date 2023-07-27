import serial
import turtle

serial_port = 'COM5'
baudrate = 115200

s = serial.Serial(serial_port, baudrate)

while True:
    accelerometer_values = eval(s.readline().decode())
    
    turtle.forward(accelerometer_values["x"])
    turtle.pendown()
    turtle.penup()