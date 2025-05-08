import sounddevice as sd
import soundfile as sf
import whisper
import tempfile

model = whisper.load_model("base")

def listen():
    duration = 5  # seconds
    samplerate = 16000
    print("[🎙️] Listening for 5 seconds...")
    
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio, samplerate)
        print("[🧠] Transcribing...")
        result = model.transcribe(f.name)
        print("[DEBUG] Full result:", result)
        print("[✅] You said:", result["text"])
        return result["text"]
