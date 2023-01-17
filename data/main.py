from aiogram import Bot, Dispatcher, executor, types
import os

from .handlers import register_modules
from .database import register_database 

async def create_logic(dp: Dispatcher):
    register_modules(dp)
    register_database()

def start_bot():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)