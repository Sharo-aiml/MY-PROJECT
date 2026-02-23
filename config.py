import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

LLM_CONFIG = {
    "model": "gpt-4",
    "api_key": OPENAI_API_KEY,
    "temperature": 0.3,
}