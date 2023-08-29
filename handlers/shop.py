import os
import json

from aiogram import types
from slugify import slugify

from loader import dp
from keyboards.main_kb import *


def get_all_courses():
    courses = []
    for folder in os.listdir("courses"):
       files_in_folder = os.listdir(f"courses/{folder}")
       if "init.json" in files_in_folder:
           with open(f"courses/{folder}/init.json", "r", encoding="utf-8") as file:
               data = json.load(file)
               data["slug"] = slugify(data["name"])
               courses.append(data)
    return courses


def gen_keyboard_by_courses(courses):
    keyboard = types.InlineKeyboardMarkup()
    for course in courses:
        keyboard.add(types.InlineKeyboardButton(text=course["name"], callback_data=course["slug"]))
    return keyboard



@dp.callback_query_handler(text="courses")
async def courses(call: types.CallbackQuery):
    courses = get_all_courses()
    markup = gen_keyboard_by_courses(courses)
    markup.add(btn_main_back_keyboard)
    await call.message.edit_text("Оберіть курс, який вас цікавить", reply_markup=markup)