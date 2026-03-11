import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("audio.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Recognized Text:")
    print(text)

    with open("recognized_text.txt", "w") as f:
        f.write(text)

except:
    print("Could not understand audio")