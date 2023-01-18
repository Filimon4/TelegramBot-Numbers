from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
import json
import requests
from ...parser import *
import os
from time import sleep

async def session_today(callback: types.CallbackQuery):
    res = int(callback.data.split("_")[1])
    try:
        json_file = await get_data_session(f'https://kinosmena.ru/?date=2023/01/{res}&facility=smena',res)

        f = open(json_file, encoding='utf-8')
        data = json.load(f)
        bot = Bot(token=os.getenv("TOKEN"))

        for key in data:
                await callback.message.answer(data[key])

        # for key in data:
        #     main_string = key

        #     img_url = data[key]["img"].split("?")[0]
        #     img_data = requests.get(img_url).content
        #     # img_url.split('/')[-1]
        #     img_name = str(key) + '.' + img_url.split('/')[-1].split('.')[-1]
        #     with open('./data/handlers/callback/photo/' + img_name.strip(), "wb") as photo:
        #         photo.write(img_data)

            
            
            # main_string += "\n" + data[key]["Смена"]
            # await callback.message.answer("Смена")
            # for key in sin_name:
            #     print(str(key) + " - " + str(sin_name[key]))
            #     main_string += "\n    " + str(key) + " - " + str(sin_name[key])

            # main_string += "\n" + data[key]["Дружба"]
            # await callback.message.answer("Дружба")
            # for key in sin_name:
            #     print(str(key) + " - " + str(sin_name[key]))
            #     main_string += "\n    " + str(key) + " - " + str(sin_name[key])

            # print(main_string)
            # await callback.message.answer(main_string)
        f.close()
    except:
        await callback.answer("Something goes wrong")
    finally:
        await callback.answer()

def register_query(dp: Dispatcher):
    dp.register_callback_query_handler(session_today, Text(startswith = "session_"))