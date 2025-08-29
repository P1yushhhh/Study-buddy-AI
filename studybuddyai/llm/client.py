from langchain_openai import ChatOpenAI
from studybuddyai.config.setting import Settings

def get_openai_llm():
    return ChatOpenAI(
        api_key= Settings.OPENAI_API_KEY,
        model_name = Settings.MODEL_NAME,
        temperature = Settings.TEMPERATURE,
        max_retries= Settings.MAX_RETRIES
    )