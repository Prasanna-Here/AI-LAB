import speech_recognition as sr

recognizer=sr.Recognizer()

with sr.Microphone() as source:
    print("Say something..")

    recognizer.adjust_for_ambient_noise(source,duration=1)

    audio=recognizer.listen(source)

try:
    text=recognizer.recognize_google(audio)
    print("you said: ",text)

except sr.UnknownValueError:
    print("Could not understand what you said.")

except sr.RequestError:
    print("API unavailable or connection error.")