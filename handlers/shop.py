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
               data["path"] = f"courses/{folder}"
               courses.append(data)
    return courses


def gen_keyboard_by_courses(courses):
    keyboard = types.InlineKeyboardMarkup()
    for course in courses:
        keyboard.add(types.InlineKeyboardButton(text=course["name"], callback_data=f'courses_{course["slug"]}'))
    return keyboard



@dp.callback_query_handler(text="courses")
async def courses(call: types.CallbackQuery):
    courses = get_all_courses()
    markup = gen_keyboard_by_courses(courses)
    markup.add(btn_main_back_keyboard)
    await call.message.edit_text("Оберіть курс, який вас цікавить", reply_markup=markup)

@dp.callback_query_handler(text="courses-back")
async def courses(call: types.CallbackQuery):
    courses = get_all_courses()
    markup = gen_keyboard_by_courses(courses)
    markup.add(btn_main_back_keyboard)
    await call.message.answer("Оберіть курс, який вас цікавить", reply_markup=markup)
    await call.message.delete()



  
    
@dp.callback_query_handler(text_contains="courses_")
async def courses(call: types.CallbackQuery):
    
    slug = call.data.split("_")[1]
    courses = get_all_courses()
    
    for course in courses:
        if course["slug"] == slug:
            image = open(f"{course['path']}/{course['image']}", "rb")
            text =f'<b>{course["name"]}</b>\n\n{course["description"]}\n\n Оберіть рівень курсу:'
            markup = types.InlineKeyboardMarkup()
            for product in course["products"]:
                slug = slugify(product["name"])
                markup.add(
                    types.InlineKeyboardButton(
                        text=product["name"], 
                        callback_data=f"product_{slug}")
                )
            back_btn = types.InlineKeyboardButton(text="Назад", callback_data="courses-back")
            markup.add(back_btn)
            await call.message.answer_photo(image, text, reply_markup=markup, parse_mode="HTML")
            await call.message.delete()
            
@dp.callback_query_handler(text_contains="product_")
async def courses(call: types.CallbackQuery):
    slug = call.data.split("_")[1]
    courses = get_all_courses()
    for course in courses:
        for product in course["products"]:
            if slug == slugify(product["name"]):
                image = open(f"{course['path']}/{product['image']}", "rb")
                text = f'<b>{product["name"]}</b>\n\n{product["description"]}\n\n Оберіть дію:'
                markup = types.InlineKeyboardMarkup()
                btn_link = types.InlineKeyboardButton(text="Перейти на сайт", url=product["link"])
                btn_back = types.InlineKeyboardButton(text="Назад на рівні", callback_data=f"courses_{course['slug']}")
                btn_main_back_keyboard = types.InlineKeyboardButton(text="Назад в головне меню", callback_data="main_menu_exit")
                markup.add(btn_link)
                markup.add(btn_back)
                markup.add(btn_main_back_keyboard)
                await call.message.answer_photo(image, text, reply_markup=markup, parse_mode="HTML")
                await call.message.delete()