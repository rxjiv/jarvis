from elevenlabs import ElevenLabs, play

client = ElevenLabs(api_key="sk_879db36e91115a449cb30ebafe058056ba7d7463fb7147b2")  # Replace with your real key

def speak(text):
    audio = client.generate(
        text=text,
        voice="John Shaw - Polite Customer Care Voice",
        model="eleven_monolingual_v1"
    )
    play(audio)
