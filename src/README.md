# leptons

leptons records all openAI api calls by adding an api hook that sends request/response to Timeplus cloud.

to install leptons, run `pip install timeplus-leptons`

to use leptons, simple 

```
import openai
from leptons import agent

# start the monitor agent of leptons
agent.start()

# your open ai calls here
openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input}],
        temperature=temp
    )

```