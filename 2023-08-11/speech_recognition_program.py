import speech_recognition as sr

speech = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source)
            inp = speech.recognize_google(audio, language="en-GB")
            print(inp)
    except:
        continue