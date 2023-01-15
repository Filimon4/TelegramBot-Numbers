from aiogram import Dispatcher
from aiogram.types import Message

async def echo(mes: Message):
    await mes.answer(mes.text)

def regirst_events(dp: Dispatcher):
    # register events
    dp.register_message_handler(echo, content_types=['text'])