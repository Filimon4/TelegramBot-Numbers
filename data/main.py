from aiogram import Bot, Dispatcher, executor, types
import os

def start_bot():
    print(os.getenv('TOKEN'))