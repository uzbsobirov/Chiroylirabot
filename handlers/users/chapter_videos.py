from loader import dp
from states.video_chapter import Video
from keyboards.default.video_chapter import menues

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📹 Videolar bo'limi", state='*')
async def chapter_of_videos(message: types.Message, state: FSMContext):
    text = "<b>O'zingizga mosini tanlang👇</b>"
    await message.answer(text=text, reply_markup=menues)

    await Video.menu.set()


@dp.message_handler(text="🎁 Bepul", state=Video.menu)
async def free_videos(message: types.Message, state: FSMContext):
    print('Bepul')


@dp.message_handler(text="💸 Pullik", state=Video.menu)
async def free_videos(message: types.Message, state: FSMContext):
    print('Pullik')
