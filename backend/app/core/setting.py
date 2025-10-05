import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    ALLOWED_TELEGRAM_USER_IDS = os.getenv("ALLOWED_TELEGRAM_USER_IDS", "")

    def is_allowed_user(self, user_id: int) -> bool:
        if not self.ALLOWED_TELEGRAM_USER_IDS:
            return True  
        allowed = [int(x) for x in self.ALLOWED_TELEGRAM_USER_IDS.split(",")]
        return user_id in allowed


settings = Settings()
