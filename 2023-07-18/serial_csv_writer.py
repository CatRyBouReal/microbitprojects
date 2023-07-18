import serial
import time
import csv

serial_port = "COM5"
baudrate = 115200

s = serial.Serial(serial_port, baudrate)

with open("table.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Ambient Light"])
    
    while True:
        ctime = time.ctime().split()[3]
        light = s.readline().decode('utf-8')
        
        writer.writerow([ctime, light])
        
        file.flush()
        
        s.reset_input_buffer()