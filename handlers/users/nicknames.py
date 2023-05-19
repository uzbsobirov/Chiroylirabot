import logging

import requests

from handlers.users.detectors import is_admin
from loader import dp, bot
from states.nicknames import Nick

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="✍️ Niklar bo'limi", state='*')
async def meaning_of_name(message: types.Message, state: FSMContext):
    text = "<b>Biror bitta matn kiriting👇</b>"
    await message.answer(text=text)

    await Nick.name.set()


@dp.message_handler(state=Nick.name)
async def get_user_name(message: types.Message, state: FSMContext):
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    user_id = message.from_user.id

    txt = message.text

    url = f"https://apilar.uz/api/name/index.php?text={txt}"

    deleted = await message.answer(text="<i>Biroz kuting...</i>")

    try:
        requesting = requests.get(url=url).json()

        text = f"<b>{txt}</b> - matni uchun nicknamelar✍️👇\n\n"
        for item in requesting:
            text += f"<code>{item}</code>\n"

        text += f"\n✨<b>@{bot_username}</b> tomonidan taqdim etildi"

        await deleted.delete()
        await message.answer(text=text, reply_markup=is_admin(user_id=user_id))
        await state.finish()

    except Exception as error:
        logging.info(error)
        await deleted.delete()
        await message.answer(text="<b>Qandaydir xatolik yuz berdi\n\nBoshqattan urinib ko'ring✍️👇</b>")

        await Nick.name.set()
