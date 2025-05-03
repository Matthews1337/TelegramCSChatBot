from TelegramBot import TelegramBot
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    if not token:
        raise ValueError("TOKEN não encontrado no .env")
    bot = TelegramBot(token)
    bot.run()