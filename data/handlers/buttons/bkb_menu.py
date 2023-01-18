from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= 'radar'),
            KeyboardButton(text= 'kieeea') 
        ],
        [
            KeyboardButton(text= 'Joi'),
            KeyboardButton(text= 'Mark'),
            KeyboardButton(text= 'radar')
        ],
        [
            KeyboardButton(text= 'kleo'),
            KeyboardButton(text= 'Dash')
        ]], resize_keyboard=True)
    
kb_menu2 = ReplyKeyboardMarkup(
    keyboard = [ 
        [
            KeyboardButton(text= 'go'),
            KeyboardButton(text= 'back') 
        ]], resize_keyboard=True)
    