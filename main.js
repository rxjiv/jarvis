const readline = require('readline');
const { askJarvis } = require('./jarvis_brain');
const { saveConversation } = require('./conversation_memory');
const say = require('say');
const { speak } = require('./text_to_voice');


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function promptUser() {
    rl.question('You: ', async (input) => {
        if (['exit', 'quit'].includes(input.toLowerCase())) {
            console.log("JARVIS: Goodbye, Ra.");
            rl.close();
            return;
        }

        const response = await askJarvis(input);
        console.log('JARVIS:', response);
        speak(response);
        saveConversation(input, response);

        promptUser();
    });
}

promptUser();
