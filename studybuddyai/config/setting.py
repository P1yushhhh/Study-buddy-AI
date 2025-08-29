import os
from dotenv import load_dotenv


load_dotenv()

class Settings():

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = "gpt-5-nano"
    TEMPERATURE = 0.4
    MAX_RETRIES = 3

settings = Settings()