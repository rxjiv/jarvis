const axios = require('axios');
const { spawn } = require('child_process');
require('dotenv').config();

const VOICE_ID = "qxjGnozOAtD4eqNuXms4";

async function speak(text) {
    const response = await axios.post(
        `https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`,
        {
            text,
            model_id: "eleven_monolingual_v1",
            voice_settings: {
                stability: 0.4,
                similarity_boost: 0.8
            }
        },
        {
            headers: {
                "xi-api-key": process.env.ELEVENLABS_API_KEY,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg"
            },
            responseType: 'stream'
        }
    );

    // Pipe ElevenLabs MP3 stream directly into ffplay (no saving)
    const ffplay = spawn('ffplay', ['-nodisp', '-autoexit', '-i', 'pipe:0'], { stdio: ['pipe', 'ignore', 'ignore'] });
    response.data.pipe(ffplay.stdin);
}

module.exports = { speak };
