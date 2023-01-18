from aiogram import types, Dispatcher
from .callback_query import register_query 

def registr_callbackes(dp: Dispatcher):
    register_query(dp)