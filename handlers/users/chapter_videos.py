from loader import dp, bot
from states.video_chapter import Video
from keyboards.default.video_chapter import menues
from .detectors import search_video
from keyboards.inline.applying import apply

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📹 Videolar bo'limi", state='*')
async def chapter_of_videos(message: types.Message, state: FSMContext):
    text = "<b>O'zingizga mosini tanlang👇</b>"
    await message.answer(text=text, reply_markup=menues)

    await Video.menu.set()


@dp.message_handler(text="🎁 Bepul", state=Video.menu)
async def free_videos(message: types.Message, state: FSMContext):
    text = "Iltimos ismingizni bosh harfini kiriting...\n❗Faqat lotin harflaridan foydalaning"

    await message.answer(text=text)

    await Video.search.set()


@dp.message_handler(state=Video.search)
async def get_item_video(message: types.Message, state: FSMContext):
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    msg = message.text

    if len(msg) == 1:
        get_data = search_video(item=msg)

        if get_data == 1:
            await message.answer(text="Iltimos faqat harflardan foydalaning!!!")

        elif get_data == 2:
            await message.answer(text="Nimadir xato ketti🤔")

        else:
            caption = f"<b>{msg.upper()}</b> harfiga video tayyor✅\n\n" \
                      f"✨<b>@{bot_username}</b> tomonidan taqdim etildi"
            await message.answer_video(video=get_data, caption=caption, reply_markup=menues)

            await Video.menu.set()
    else:
        await message.answer(text="Iltimos faqat ismingizni bosh harfini kiriting...")
        await Video.search.set()


@dp.message_handler(text="💸 Pullik", state=Video.menu)
async def free_videos(message: types.Message, state: FSMContext):
    text = "Pullik videolar yasash uchun admin bilan bog'laning👇\n\n" \
           "❗️<b>Har bittasi uchun narx video turiga qarab belgilanadi</b>"
    await message.answer(text=text, reply_markup=apply)
    await Video.menu.set()
