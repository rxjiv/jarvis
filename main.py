from voice_to_text_whisper import listen
from text_to_voice import speak
from jarvis_brain import ask_jarvis

print("✅ JARVIS Booted. Listening for your voice...")

while True:
    query = listen()
    if query:
        response = ask_jarvis(query)
        print(f"🤖 JARVIS: {response}")
        speak(response)
