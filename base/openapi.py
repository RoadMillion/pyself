# -*- coding: utf-8 -*-

import openai

OPENAI_KEY = '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'
MODEL_NAME = 'text-davinci-003'
openai.api_key = OPENAI_KEY


def ask(text: str):
    response = openai.Completion.create(model=MODEL_NAME, prompt=text, temperature=0, max_tokens=4000)
    response_text = response.choices[0].text

    print('chatGpt answer: %s \n' % response_text)


while True:
    prompt = input("\nI say: ")
    if not prompt:
        continue
    if prompt == "exit":
        break
    ask(prompt)
