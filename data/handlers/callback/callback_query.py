from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

async def session_today(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал')
    await callback.answer()

def register_query(dp: Dispatcher):
    dp.register_callback_query_handler(session_today, Text(startswith = "sesstion_"))