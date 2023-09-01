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
    
@dp.callback_query_handler(text="main_menu_exit")
async def courses(call: types.CallbackQuery):
    await call.message.answer("Привіт! Вітаю тебе в IT Школі Hillel!\n"
                         +"Якщо ти хочеш дізнатися більше про нас, натисни на кнопку нижче 👇",
                         reply_markup=main_keyboard)
    await call.message.delete()
    
@dp.callback_query_handler(text="support")
async def support(call: types.CallbackQuery):
    await call.message.edit_text("Служба підтримки \"Hillel\". \n Напиши своє питання і ми зв'яжемось з тобою найближчим часом",
                                reply_markup= main_back_keyboard)
    

@dp.callback_query_handler(text="contacts")
async def contacts(call: types.CallbackQuery):
    await call.message.edit_text("На всі ваші запитання дадуть відповідь адміністратори. \n"
                                 "📞 Телефон: 0800 20 8020  безкоштовно по Україні\n "
                                 "📧 Email: online@ithillel.ua", 
                                    reply_markup= main_back_keyboard)
    
    
@dp.callback_query_handler(text="about_us")
async def about_us(call: types.CallbackQuery):
    await call.message.edit_text("""<b>Комп'ютерна школа Hillel</b><u> — одна з найбільших IT-шкіл в Україні, і з кожним роком ми продовжуємо розвиватися і впроваджувати інновації у навчання.

До нас приходять і ті, хто хоче придбати нову професію або «прокачати» вже існуючі знання, і люди, які бажають підвищити свою кваліфікацію.

Одним з ключових показників нашої роботи є відсоток працевлаштованих студентів. Для того, щоб цей показник був максимально високим, до викладацького складу ми запрошуємо тільки практикуючих фахівців з кращих IT-компаній, підбираємо корисні відеоматеріали і максимально комфортно організовуємо навчальний процес.

Знання допомагають змінювати життя на краще. Вчися заради мрії 🚀</u>""",
    reply_markup= main_back_keyboard, parse_mode="HTML")
    
@dp.callback_query_handler(text="merch")
async def merch(call: types.CallbackQuery):
    await call.message.edit_text("Мерч IT Школи Hillel", reply_markup= main_back_keyboard)