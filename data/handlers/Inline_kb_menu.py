from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import date
from .callback import *
import calendar

def get_day(increment=0):
    today = date.today()
    return today.day + increment

def get_month():
    today = date.today()
    month_name = calendar.month_abbr[today.month]
    return month_name

ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[

        InlineKeyboardButton(text = "Your text", callback_data= 'Your text'),
        InlineKeyboardButton(text = 'your text 2', callback_data = 'Your text2')

    ]
])

ikb_session = InlineKeyboardMarkup(row_width=8, inline_keyboard=[[
    InlineKeyboardButton(text = f"{get_day()} {get_month()}", callback_data = "Test"),
    InlineKeyboardButton(text = f"{get_day(1)} {get_month()}", callback_data = "Test"),
    InlineKeyboardButton(text = f"{get_day(2)} {get_month()}", callback_data = "Test"),
    InlineKeyboardButton(text = f"{get_day(3)} {get_month()}", callback_data = "Test")
]])