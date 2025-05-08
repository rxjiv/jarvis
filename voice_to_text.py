# voice_to_text.py

import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Didn't catch that.")
        return ""
    except sr.RequestError:
        print("Speech recognition service error.")
        return ""
