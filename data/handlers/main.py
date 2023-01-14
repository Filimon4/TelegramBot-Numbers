from aiogram import Dispatcher

from .utils import regirst_events

def register_modules(dp: Dispatcher):
    print('hi')
    handlers = (
        regirst_events
    )
    for handler in handlers:
        handler(dp)