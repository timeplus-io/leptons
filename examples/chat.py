import os
import openai
from leptons.agent import Agent


api_key = os.environ.get("TIMEPLUS_API_KEY")
api_address = os.environ.get("TIMEPLUS_ADDRESS")
agent = Agent(api_address=api_address, api_key=api_key)
agent.start()


def chat(input, temp):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input}],
        temperature=temp
    )
    return response['choices'][0]['message']['content']


class Bot:
    def __init__(self):
        openai.organization = "org-2lL52vp8vsIoEQ5VxEZzb1UC"
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, input, temp):
        return chat(input, temp)


bot = Bot()
print(bot.chat('hello', 0))
