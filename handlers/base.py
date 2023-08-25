from aiogram import types

from loader import dp

from keyboards.main_kb import main_keyboard, main_back_keyboard


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт! Вітаю тебе в IT Школі Hillel!\n"
                         +"Якщо ти хочеш дізнатися більше про нас, натисни на кнопку нижче 👇",
                         reply_markup=main_keyboard)

@dp.callback_query_handler(text="main_menu")
async def main_menu(call: types.CallbackQuery):
    await call.message.edit_text("Привіт! Вітаю тебе в IT Школі Hillel!\n"
                         +"Якщо ти хочеш дізнатися більше про нас, натисни на кнопку нижче 👇",
                         reply_markup=main_keyboard)
    
@dp.callback_query_handler(text="support")
async def support(call: types.CallbackQuery):
    await call.message.edit_text("Служба підтримки \"Hillel\". \n Напиши своє питання і ми зв'яжемось з тобою найближчим часом",
                                reply_markup= main_back_keyboard)
    