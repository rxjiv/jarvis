const fs = require('fs');
const path = 'brain/memory_log.json';

function loadMemory() {
    if (!fs.existsSync(path)) return [];
    return JSON.parse(fs.readFileSync(path, 'utf8'));
}

function saveConversation(user, jarvis) {
    const memory = loadMemory();
    memory.push({ timestamp: new Date().toISOString(), user, jarvis });
    fs.writeFileSync(path, JSON.stringify(memory, null, 2));
}

module.exports = { loadMemory, saveConversation };
