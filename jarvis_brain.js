const axios = require('axios');
require('dotenv').config();
const { loadMemory } = require('./conversation_memory');

async function askJarvis(prompt) {
    const memory = loadMemory();
    const recent = memory.slice(-5);

    const messages = [
        { role: "system", content: "You are JARVIS, Ra's helpful assistant." },
        ...recent.flatMap(m => [
            { role: "user", content: m.user },
            { role: "assistant", content: m.jarvis }
        ]),
        { role: "user", content: prompt }
    ];

    const response = await axios.post(
        'https://api.openai.com/v1/chat/completions',
        {
            model: "gpt-3.5-turbo",
            messages
        },
        {
            headers: {
                Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
                'Content-Type': 'application/json'
            }
        }
    );

    return response.data.choices[0].message.content;
}

module.exports = { askJarvis };
