from loader import dp
from keyboards.default.pictures_chapter import menues
from states.picture_chapter import Picture

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="🖼 Suratlar bo'limi", state='*')
async def chapter_of_pictures(message: types.Message, state: FSMContext):
    text = "<b>O'zingizga keraklisini tanlang👇</b>"

    await message.answer(text=text, reply_markup=menues)

    await Picture.menu.set()


@dp.message_handler(text="🧑‍🦰 O'g'il bolalar uchun", state=Picture.menu)
async def boys_picture(message: types.Message, state: FSMContext):
    print('boy')


@dp.message_handler(text="👱‍♀️ Qiz bolalar uchun", state=Picture.menu)
async def girls_picture(message: types.Message, state: FSMContext):
    print('girls')


@dp.message_handler(text="👫 Juftlik rasmlar", state=Picture.menu)
async def para_pictures(message: types.Message, state: FSMContext):
    print('juftlik')


@dp.message_handler(text="📝 Status yasash", state=Picture.menu)
async def make_staus(message: types.Message, state: FSMContext):
    print('status')
