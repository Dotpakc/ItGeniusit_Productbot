import os
import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from slugify import slugify

from loader import dp
from keyboards.main_kb import *
from keyboards.admin_kb import *
from states.admin import AdminMenu



from aiogram.dispatcher.filters.state import State, StatesGroup


class AddCategory(StatesGroup):
    name = State()
    description = State()
    image = State()
    
@dp.callback_query_handler(text='add_category', state=AdminMenu.menu)
async def add_category(call: types.CallbackQuery, state: FSMContext):
    await call.answer() # Відповідаємо на колбек запит
    await call.message.edit_text('Введіть назву категорії: ')
    await AddCategory.name.set() # Переходимо в стан name
    
@dp.message_handler(state=AddCategory.name)
async def add_category_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name) # Записуємо в state назву категорії
    
    await message.answer('Введіть опис категорії: ')
    await AddCategory.description.set() # Переходимо в стан description

@dp.message_handler(state=AddCategory.description)
async def add_category_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description) # Записуємо в state опис категорії
    
    await message.answer('Відправте фото категорії: ')
    await AddCategory.image.set() # Переходимо в стан image
    
@dp.message_handler(content_types=['photo'], state=AddCategory.image)
async def add_category_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id) # Записуємо в state фото категорії
    
    data = await state.get_data() # Отримуємо дані з state
    
    payload = {
        "name": data.get('name'),
        "description": data.get('description'),
        "image": data.get('image'),
        'products': []
        }
    slug_name = slugify(data.get('name'),replacements=[['#','-sharp'],['&','-and'],['+','-plus']])
    
    json.dump(payload,
              open(f"courses/{slug_name}/init.json", "w", encoding="utf-8"),
              indent=4, 
              ensure_ascii=False)
    
    await message.answer('Категорію додано', reply_markup=admin_main_back_keyboard)
    await state.finish()
    await AdminMenu.menu.set()