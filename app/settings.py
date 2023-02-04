from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

@lru_cache()
def get_settings():
    return Settings()