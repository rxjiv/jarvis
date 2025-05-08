import os
from openai import OpenAI
from dotenv import load_dotenv


from elevenlabs import ElevenLabs, play

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def speak(text):
    audio = client.generate(
        text=text,
        voice="John Shaw - Polite Customer Care Voice",
        model="eleven_monolingual_v1"
    )
    play(audio)
