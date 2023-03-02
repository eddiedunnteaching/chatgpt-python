import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write text for 30 slides on Linux shell expansion",
  temperature=0.3,
  max_tokens=120,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

response = completion.choices[0].text
print(response)