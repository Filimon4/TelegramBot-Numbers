from aiogram import Dispatcher, types
from aiogram.types import Message, CallbackQuery, Voice
from .Inline_kb_menu import ikb_menu
from .bkb_menu import kb_menu, kb_menu2
import speech_recognition as sr
r = sr.Recognizer()



async def errors(mes: Message):
    await mes.answer(f'Command {mes.text} not found!')

async def Listened():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listened(source)
        try :
            text = r.recongnize_google(audio, language= 'ru-Ru')
        except sr.UnknownValueError:
            pass
        print(text)
        return text

async def Voice_answer(message: types.message):
    await  message.answer ("Listen",  ) 

async def show_inline_menu(message: types.Message):
    await  message.answer ("Инлайн кнопки ниже", reply_markup=ikb_menu) 

async def send_message_ikb (call: CallbackQuery):
    await call.message.answer("Какой то текст", reply_markup=ikb_menu)

async def send_message2(message: types.Message):
    await message.answer('You search new item',reply_markup=kb_menu2)

async def send_message3(message: types.Message):
    await message.answer('You beat',reply_markup=kb_menu2)

async def send_message4(message: types.Message):
    await message.answer('ahahahhahahaahhaahah',reply_markup=kb_menu2)

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

    dp.register_message_handler(Voice_answer, content_types =  Voice )
    dp.register_message_handler(show_inline_menu, commands = 'menu')
    dp.register_message_handler(menu, commands = 'kmenu')
    dp.register_callback_query_handler(send_message_ikb, text = 'Your text')
    dp.register_callback_query_handler(send_message_ikb, text = 'Your text2')
    dp.register_message_handler(send_message2, text= 'radar'   )
    dp.register_message_handler(send_message3, text= 'kieeea'   )
    dp.register_message_handler(send_message4, text= 'Mark'   )
    dp.register_message_handler(send_message4, text= 'Joi'   ) 
    dp.register_message_handler(send_message5, text= 'kleo'   )
    dp.register_message_handler(send_message6, text= 'Dash'   )
    dp.register_message_handler(back_message, text= 'go'   )
    dp.register_message_handler(back_message, text= 'back'   )
    dp.register_message_handler(errors, content_types=['text'])

    