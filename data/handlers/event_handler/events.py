from aiogram import types, Dispatcher
from ..buttons import *

async def start(message: types.Message):
    await message.answer('''
        Здравствуй, я бот транслирующий сеансы в Смене.''', reply_markup=bkb_menu.kb_menu)
    await message.delete()

async def sessions(message: types.Message):
    await message.answer('''Выберете Дату''', reply_markup=Inline_kb_menu.ikb_session)
    await message.delete()

async def errors(mes: types.Message):
    await mes.answer(f'Command {mes.text} not found!')

async def helper(mes: types.Message):
    await mes.answer('''
        Что бы увидеть список сенасов воспользуйся командой /sessions
    ''')
    await mes.delete()