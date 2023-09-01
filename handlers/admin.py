from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.main_kb import *
from keyboards.admin_kb import *
from states.admin import AdminMenu


ADMIN_LIST = [
    222201019,
    1934648618,
    1235018495
]


@dp.message_handler(commands=['admin'], state="*")
async def admin(message: types.Message, state: FSMContext):
    if message.from_user.id not in ADMIN_LIST:
        await message.answer("Ви не адміністратор")
        return
    await state.finish()
    await message.answer("Ви увійшли в адмін панель", reply_markup=admin_main_keyboard)
    await AdminMenu.menu.set()
    
@dp.callback_query_handler(text='admin_main_back', state=AdminMenu)
async def admin_main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text('Виберіть дію: ', reply_markup=admin_main_keyboard)
    await state.finish()
    await AdminMenu.menu.set()

@dp.callback_query_handler(text='exit_admin_menu', state=AdminMenu)
async def exit_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Ви вийшли з адмін меню")
    await state.finish()

    await call.message.edit_text('Назад до головного меню бота ', reply_markup=main_back_keyboard)
    





