import os
from openai import OpenAI
from dotenv import load_dotenv
from conversation_memory import load_memory


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_jarvis(prompt):
    memory = load_memory()
    recent = memory[-5:]  # Get last 5 interactions

    context = [
        {"role": "system", "content": "You are JARVIS, a helpful AI assistant loyal to Ra."}
    ]

    # Add recent memory to the prompt
    for convo in recent:
        context.append({"role": "user", "content": convo["user"]})
        context.append({"role": "assistant", "content": convo["jarvis"]})

    # Add the new message
    context.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=context
    )

    return response.choices[0].message.content
