from aiogram import Bot, Dispatcher, executor, types

from .handlers import registr_modules
from .bot import bot,dp

async def create_logic(dp: Dispatcher):
    registr_modules(dp)

def start_bot():
    executor.start_polling(dp, skip_updates=True, on_startup=create_logic)