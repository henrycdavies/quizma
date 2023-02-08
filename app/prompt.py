import os
import openai

def send_prompt(prompt: str, settings):
    openai.api_key = settings.openai_api_key
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )