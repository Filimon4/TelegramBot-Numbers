import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from random import randint
from os import getenv
from sys import exit
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Errot: no token provided")

bot = Bot(token=bot_token, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)

callback_numbers = CallbackData('fabnum','action')

logging.basicConfig(level=logging.INFO)

user_data = {}

def get_keyboard_fab():
        buttons = [
            types.InlineKeyboardButton(text='-1', callback_data=callback_numbers.new(action='decr')),
            types.InlineKeyboardButton(text='+1', callback_data=callback_numbers.new(action="incr")),
            types.InlineKeyboardButton(text="Accept", callback_data=callback_numbers.new(action="accept"))
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(*buttons)
        return keyboard

async def update_num_text_fab(message: types.Message, new_value: int):
    with suppress(MessageNotModified):
        await message.edit_text(f"Укажите число: {new_value}", reply_markup=get_keyboard_fab())


@dp.message_handler(commands="numbers_fab")
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())


@dp.callback_query_handler(callback_numbers.filter(action=["incr", "decr"]))
async def callbacks_num_change_fab(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    action = callback_data["action"]
    if action == "incr":
        user_data[call.from_user.id] = user_value + 1
        await update_num_text_fab(call.message, user_value + 1)
    elif action == "decr":
        user_data[call.from_user.id] = user_value - 1
        await update_num_text_fab(call.message, user_value - 1)
    await call.answer()


@dp.callback_query_handler(callback_numbers.filter(action=["accept"]))
async def callbacks_num_finish_fab(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    await call.message.edit_text(f"Итого: {user_value}")
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)