import logging #

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from decouple import config

# Налаштування логів
logging.basicConfig(level=logging.DEBUG)


API_TOKEN = config('API_TOKEN')


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

