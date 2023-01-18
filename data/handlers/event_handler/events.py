from aiogram import types, Dispatcher
from ..buttons import *

async def start(message: types.Message):
    await message.answer('''
        Здравствуй, я бот транслирующий сеансы в Смене.
        \nЧто бы увидеть список сенасов воспользуйся командой /sessions
    ''')

async def sessions(message: types.Message):
    await message.answer('''Выберете Дату''', reply_markup=Inline_kb_menu.ikb_session)

async def errors(mes: types.Message):
    await mes.answer(f'Command {mes.text} not found!')