import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CRYPTO_TELEBOT_API_KEY = os.getenv('CRYPTO_TELEBOT_API_KEY')

    EXCHANGE_API = os.getenv('EXCHANGE_API')