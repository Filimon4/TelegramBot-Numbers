from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import date
import calendar

def get_day(increment=0):
    today = date.today()
    return today.day + increment

def get_month():
    today = date.today()
    month_name = calendar.month_abbr[today.month]
    return month_name

ikb_session = InlineKeyboardMarkup(row_width=8, inline_keyboard=[[
    InlineKeyboardButton(text = f"{get_day()} {get_month()}", callback_data = f"session_{get_day()}"),
    InlineKeyboardButton(text = f"{get_day(1)} {get_month()}", callback_data = f"session_{get_day(1)}"),
    InlineKeyboardButton(text = f"{get_day(2)} {get_month()}", callback_data = f"session_{get_day(2)}"),
    InlineKeyboardButton(text = f"{get_day(3)} {get_month()}", callback_data = f"session_{get_day(3)}")
]])