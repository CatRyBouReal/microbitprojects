import serial
import speech_recognition as sr

port = "COM5"
baudrate = 115200

s = serial.Serial(port, baudrate)
speech = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)

            audio = speech.listen(source)

            inp = speech.recognize_google(audio, language="en-GB")

            print(inp)
            s.write(bytes(inp, 'utf-8'))
    except:
        continue