import os
from openai import OpenAI
from dotenv import load_dotenv


from elevenlabs import ElevenLabs, play

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

audio = client.generate(
    text="Testing ElevenLabs voice integration with JARVIS.",
    voice="John Shaw - Polite Customer Care Voice",
    model="eleven_monolingual_v1"
)

play(audio)
