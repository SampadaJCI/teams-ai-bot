import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    BOT_ID = os.getenv("BOT_ID")
    BOT_PASSWORD = os.getenv("BOT_PASSWORD")
    SPEECH_KEY = os.getenv("SPEECH_KEY")
    SPEECH_REGION = os.getenv("SPEECH_REGION")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
    TEAMS_APP_ID = os.getenv("TEAMS_APP_ID")
