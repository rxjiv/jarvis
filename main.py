from voice_to_text_whisper import listen
from text_to_voice import speak
from jarvis_brain import ask_jarvis
from conversation_memory import save_conversation


from conversation_memory import save_conversation, load_memory

memory = load_memory()
print(f"🧠 Loaded {len(memory)} past conversations.")

print("✅ JARVIS Booted. Listening for your voice...")

while True:
    query = listen()

    if not query:
        continue  # If nothing was said, skip the rest

        # ENDS JARVIS BY KEYWORDS
    if query.lower() in ["exit", "quit", "goodbye", "shut down", "thanks Jarvis"]:
        speak("Shutting down now. Goodbye, Ra.")
        print("👋 JARVIS session ended.")
        break

    response = ask_jarvis(query)
    print(f"🤖 JARVIS: {response}")
    speak(response)
    save_conversation(query, response)
