from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[ [
                        InlineKeyboardButton(text = "Your text", callback_data= 'Your text'),
                        InlineKeyboardButton(text = 'your text 2', callback_data = 'Your text2')
                        ]
                        ])
