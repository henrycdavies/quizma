import os
import openai
from fastapi import Depends
from app.settings import get_settings, Settings

def send_prompt(prompt: str, settings: Settings = Depends(get_settings)):
    openai.api_key = settings.openai_api_key
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=25,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )