import serial

s = serial.Serial("/dev/ttyACM1", 115200)

while True:
    print(s.readline().decode('utf-8'))