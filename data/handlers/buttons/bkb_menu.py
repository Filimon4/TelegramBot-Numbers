from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= '/help'),
            KeyboardButton(text= '/sessions') 
        ]
], resize_keyboard=True)
    
# kb_menu2 = ReplyKeyboardMarkup(
#     keyboard = [ 
#         [
#             KeyboardButton(text= 'go'),
#             KeyboardButton(text= 'back') 
#         ]], resize_keyboard=True)
    