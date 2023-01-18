from aiogram import Dispatcher

from .utils import registr_events
from .callback import registr_callbackes

def registr_modules(dp: Dispatcher):
    handlers = [
        registr_events,
        registr_callbackes
    ]
    for handler in handlers:
        handler(dp)