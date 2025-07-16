import asyncio
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
import logging
from pathlib import Path
from config import Config

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('weather_avatar.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WeatherAvatarBot:
    def __init__(self):
        self.client = TelegramClient(
            'weather_avatar_session',
            Config.TELEGRAM_API_ID,
            Config.TELEGRAM_API_HASH
        )
        self.last_update_hour = None

    def _get_time_period(self, hour: int) -> str:
        """Определяет период суток по часу"""
        if 0 <= hour < 6:
            return 'night'
        elif 6 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 18:
            return 'day'
        return 'evening'

    def _parse_weather(self) -> str:
        """Парсит температуру с разных источников"""
        try:
            # Пробуем Яндекс
            response = requests.get(Config.WEATHER_SOURCES['yandex'], timeout=10)
            soup = bs(response.text, 'html.parser')
            temp = soup.find('div', class_='temp fact__temp fact__temp_size_s').find('span', class_='temp__value').text
            return f"{temp}°"
        except Exception as e:
            logger.warning(f"Yandex failed: {e}, trying Mail.ru")
            
            try:
                # Пробуем Mail.ru
                response = requests.get(Config.WEATHER_SOURCES['mail'], timeout=10)
                soup = bs(response.text, 'html.parser')
                temp = soup.find('div', class_='information__content__temperature').text.strip()
                return temp
            except Exception as e:
                logger.error(f"All sources failed: {e}")
                return "N/A°"

    def _generate_image(self, hour: int) -> Image.Image:
        """Генерирует изображение для аватарки"""
        temp = self._parse_weather()
        period = self._get_time_period(hour)
        color = Config.TIME_COLORS[period]
        
        try:
            font_large = ImageFont.truetype(*Config.FONTS['large'])
            font_small = ImageFont.truetype(*Config.FONTS['small'])
        except:
            logger.warning("Using default fonts")
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()

        img = Image.new('RGB', Config.IMAGE_SIZE, color='black')
        draw = ImageDraw.Draw(img)
        
        # Температура
        temp_bbox = draw.textbbox((0, 0), temp, font=font_large)
        temp_x = (Config.IMAGE_SIZE[0] - (temp_bbox[2] - temp_bbox[0])) // 2
        draw.text((temp_x, 50), temp, font=font_large, fill='white')
        
        # Город
        city_bbox = draw.textbbox((0, 0), Config.CITY_NAME, font=font_small)
        city_x = (Config.IMAGE_SIZE[0] - (city_bbox[2] - city_bbox[0])) // 2
        draw.text((city_x, 150), Config.CITY_NAME, font=font_small, fill=color)
        
        return img

    async def _update_avatar(self, hour: int) -> bool:
        """Обновляет аватар в Telegram"""
        try:
            # Удаляем старую аватарку
            photos = await self.client.get_profile_photos('me')
            if photos:
                await self.client(DeletePhotosRequest(
                    id=[InputPhoto(
                        id=photos[0].id,
                        access_hash=photos[0].access_hash,
                        file_reference=photos[0].file_reference
                    )]
                ))
            
            # Создаем и загружаем новую
            image = self._generate_image(hour)
            temp_file = Path('temp_avatar.png')
            image.save(temp_file)
            
            with open(temp_file, 'rb') as f:
                uploaded = await self.client.upload_file(f)
                await self.client(UploadProfilePhotoRequest(file=uploaded))
            
            temp_file.unlink()
            return True
        except Exception as e:
            logger.error(f"Update failed: {e}")
            return False

    async def run(self):
        """Основной цикл работы"""
        await self.client.start()
        logger.info("Bot started")
        
        try:
            while True:
                current_hour = datetime.now().hour
                if current_hour != self.last_update_hour:
                    if await self._update_avatar(current_hour):
                        self.last_update_hour = current_hour
                        logger.info(f"Updated for {current_hour}:00")
                
                await asyncio.sleep(Config.UPDATE_INTERVAL)
        except KeyboardInterrupt:
            logger.info("Stopping bot...")
        finally:
            await self.client.disconnect()

if __name__ == '__main__':
    bot = WeatherAvatarBot()
    with bot.client:
        bot.client.loop.run_until_complete(bot.run())
