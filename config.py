import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    # Telegram
    TELEGRAM_API_ID = int(os.getenv('TELEGRAM_API_ID'))
    TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
    
    # Weather
    CITY_NAME = os.getenv('CITY_NAME', 'Krasnodar')
    WEATHER_SOURCES = {
        'yandex': os.getenv('YANDEX_WEATHER_URL'),
        'mail': os.getenv('MAIL_WEATHER_URL')
    }
    
    # Fonts
    FONTS = {
        'large': (os.getenv('LARGE_FONT'), int(os.getenv('LARGE_FONT_SIZE'))),
        'small': (os.getenv('SMALL_FONT'), int(os.getenv('SMALL_FONT_SIZE')))
    }
    
    # Design
    IMAGE_SIZE = (256, 256)
    TIME_COLORS = {
        'night': "#0000CD",    # 00:00-06:00
        'morning': "#FFD700",  # 06:00-12:00
        'day': "#FFFACD",      # 12:00-18:00
        'evening': "#FF8C00"   # 18:00-24:00
    }
    UPDATE_INTERVAL = 300  # 5 minutes in seconds