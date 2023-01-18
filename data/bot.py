from aiogram import Bot, Dispatcher, types
import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)