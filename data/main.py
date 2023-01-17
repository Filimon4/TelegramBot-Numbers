from aiogram import Bot, Dispatcher, executor, types
import os

from .handlers import registr_modules

async def create_logic(dp: Dispatcher):
    registr_modules(dp)

def start_bot():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)