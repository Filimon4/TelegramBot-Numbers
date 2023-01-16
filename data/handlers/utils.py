from aiogram import Dispatcher, types
from aiogram.types import Message
from .Inline_kb_menu import ikb_menu
from .bkb_menu import kb_menu, kb_menu2



async def errors(mes: Message):
    await mes.answer(f'Command {mes.text} not found!')

async def show_inline_menu(message: types.Message):
    await  message.answer ("Инлайн кнопки ниже", reply_markup=ikb_menu) 

async def send_message2(message: types.Message):
    await message.answer('You search new item',reply_markup=kb_menu2)

async def send_message3(message: types.Message):
    await message.answer('You beat',reply_markup=kb_menu2)

async def send_message4(message: types.Message):
    await message.answer('It your name',reply_markup=kb_menu2)

async def send_message5(message: types.Message):
    await message.answer('Funny',reply_markup=kb_menu2)

async def send_message6(message: types.Message):
    await message.answer('Evil',reply_markup=kb_menu2)

async def back_message(message: types.Message):
    await message.answer('ok', reply_markup=kb_menu)

async def menu(message: types.Message):
    await message.answer("new keyboard", reply_markup=kb_menu)




def regirst_events(dp: Dispatcher):
    # register events
    
    dp.register_message_handler(show_inline_menu, commands = 'menu')
    dp.register_message_handler(menu, commands = 'kmenu')
    dp.register_message_handler(send_message2, text= 'radar'   )
    dp.register_message_handler(send_message3, text= 'kieeea'   )
    dp.register_message_handler(send_message4, text= 'Mark'   )
    dp.register_message_handler(send_message4, text= 'Joi'   ) 
    dp.register_message_handler(send_message5, text= 'kleo'   )
    dp.register_message_handler(send_message6, text= 'Dash'   )
    dp.register_message_handler(back_message, text= 'go'   )
    dp.register_message_handler(back_message, text= 'back'   )
    dp.register_message_handler(errors, content_types=['text'])
    