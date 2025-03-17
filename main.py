from javascript import require, On, Once, AsyncTask, once, off
from openai import OpenAI

client_ai = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your-openrouter-api-key"
)

mineflayer = require('mineflayer')

bot = mineflayer.createBot({'host': 'server-url/ip', 'port': server-port, 'username': 'username'})

# The spawn event
once(bot, 'login')
bot.chat("Hello there! To use me put Alybot in you chat message and I'll respond. My owner is Alybit.")

@On(bot, 'chat')
def onChat(this, user, message, *rest):
    if "Alybot" in message or "AlyBot" in message or "alybot" in message:
        if user != bot.username:
            completion = client_ai.chat.completions.create(
                extra_body={},
                model="ai-model",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": message
                            }
                        ]
                    }
                ]
            )
            bot.chat(completion.choices[0].message.content)
