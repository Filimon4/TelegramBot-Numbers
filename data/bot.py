from aiogram import Bot, Dispatcher, types
import os

bot = Bot(token=os.getenv("TOKEN"))
bp = Dispatcher(bot)