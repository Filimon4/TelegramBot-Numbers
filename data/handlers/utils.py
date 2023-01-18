from aiogram import Dispatcher, types, Bot
from aiogram.types import ContentType, Message, CallbackQuery, Voice, File

# from .Inline_kb_menu import ikb_menu, ikb_session
# from .bkb_menu import kb_menu, kb_menu2

# import event_handler
# import buttons

import speech_recognition as sr
from pathlib import Path
import os
from pydub import AudioSegment 
import ffmpeg



def convent (File_name):
    in_file = ffmpeg.input(f"{File_name}.ogg")
    
    nFile = f"{File_name}.wav"
    


async def errors(mes: Message):
    await mes.answer(f'Command {mes.text} not found!')

def Listened (voice_file_id):
    File_voice = str(Path(f'./handler/voice_answer/{voice_file_id}.WAV'))
    r = sr.Recognizer() 
    with sr.AudioFile(File_voice) as source:
        audio = r.record(source)
        # sr.Recognizer.adjust_for_ambient_noise(source)
        # audio = sr.Recognizer.listened(source)
        try :
            text = r.recognize_google(audio, language= 'ru-Ru')
        except sr.UnknownValueError:
            text = ('i dont know')
        return (text)

async def handle_file(file: types.File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

async def Voice_answer(msg: types.Message):
    voice = await msg.voice.get_file()
    path = './handler/voice_answer'
    voice_path = str(Path(f'./handler/voice_answer/{voice.file_id}'))
    await handle_file(file = voice, file_name=f"{voice.file_id}.ogg", path=path)
    await msg.reply('Секунду  ')
    sound = AudioSegment.from_file(f"{voice_path}.ogg")
    sound.export(f"{voice_path}.WAV", format="WAV")
    await  msg.answer (Listened(voice.file_id))
    os.remove(f"{voice_path}.ogg")
    os.remove(f"{voice_path}.WAV")

    

# async def show_inline_menu(message: types.Message):
#     await  message.answer ("Инлайн кнопки ниже", reply_markup=ikb_menu) 

# async def send_message_ikb (call: CallbackQuery):
#     await call.message.answer("Какой то текст", reply_markup=ikb_menu)

# async def send_message2(message: types.Message):
#     await message.answer('You search new item',reply_markup=kb_menu2)

# async def send_message3(message: types.Message):
#     await message.answer('You beat',reply_markup=kb_menu2)

# async def send_message4(message: types.Message):
#     await message.answer('ahahahhahahaahhaahah',reply_markup=kb_menu2)

# async def send_message5(message: types.Message):
#     await message.answer('Funny',reply_markup=kb_menu2)

# async def send_message6(message: types.Message):
#     await message.answer('Evil',reply_markup=kb_menu2)

# async def back_message(message: types.Message):
#     await message.answer('ok', reply_markup=kb_menu)

# async def menu(message: types.Message):
#     await message.answer("new keyboard", reply_markup=kb_menu)

def registr_events(dp: Dispatcher):
    # register events

    dp.register_message_handler(Voice_answer, content_types=types.ContentTypes.VOICE)
    dp.register_message_handler(Voice_answer, content_types=types.ContentTypes.VOICE)
    # dp.register_message_handler(show_inline_menu, commands = 'menu')
    # dp.register_message_handler(menu, commands = 'kmenu')
    # dp.register_message_handler(start, commands = 'start')
    # dp.register_message_handler(sessions, commands = 'sessions')

    # dp.register_callback_query_handler(send_message_ikb, text = 'Your text')
    # dp.register_callback_query_handler(send_message_ikb, text = 'Your text2')

    # dp.register_message_handler(send_message2, text= 'radar')
    # dp.register_message_handler(send_message3, text= 'kieeea')
    # dp.register_message_handler(send_message4, text= 'Mark')
    # dp.register_message_handler(send_message4, text= 'Joi') 
    # dp.register_message_handler(send_message5, text= 'kleo')
    # dp.register_message_handler(send_message6, text= 'Dash')
    # dp.register_message_handler(back_message, text= 'go')
    # dp.register_message_handler(back_message, text= 'back')

    dp.register_message_handler(errors, content_types=['text'])

    