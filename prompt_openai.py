#!/usr/bin/env python

import requests
import readline
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "text-davinci-003"

def query_chatgpt(prompt):
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text


while True:
    prompt = input("Enter your prompt: ")
    if prompt == "quit":
        break
    else:
        response = query_chatgpt(prompt)
        print('ChatGPT Response:', response)
        #print("You entered: {}".format(user_input))

