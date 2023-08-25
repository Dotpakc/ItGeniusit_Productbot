from aiogram import types

from loader import dp

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hi!\nI'm EchoBot!\nPowered by aiogram.")