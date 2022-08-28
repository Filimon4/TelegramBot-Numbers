import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from random import randint
from os import getenv
from sys import exit
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Errot: no token provided")

bot = Bot(token=bot_token, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

user_data = {}

def get_keyboard():
        buttons = [
            types.InlineKeyboardButton(text='-1', callback_data='num_decr'),
            types.InlineKeyboardButton(text='+1', callback_data="num_incr"),
            types.InlineKeyboardButton(text="Accept", callback_data="num_accept")
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*buttons)
        return keyboard

async def update_num_text(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f'Enter a number: {new_value}', reply_markup=get_keyboard())

@dp.message_handler(commands="numbers")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Enter a number: 0", reply_markup=get_keyboard())

@dp.callback_query_handler(lambda call: call.data.startswith('num_'))
async def callbacks_num(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[-1]
    if action == 'incr':
        user_data[call.from_user.id] = user_value + 1
        await update_num_text(call.message, user_data[call.from_user.id])
    elif action == 'decr':
        user_data[call.from_user.id] = user_value - 1
        await update_num_text(call.message, user_data[call.from_user.id])
    else:
        await call.message.edit_text(f"Final number: {user_value}")
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)