from elevenlabs import ElevenLabs, play

client = ElevenLabs(api_key="sk_879db36e91115a449cb30ebafe058056ba7d7463fb7147b2")

audio = client.generate(
    text="Testing ElevenLabs voice integration with JARVIS.",
    voice="John Shaw - Polite Customer Care Voice",
    model="eleven_monolingual_v1"
)

play(audio)
