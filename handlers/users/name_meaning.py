import requests

from handlers.users.detectors import is_admin
from loader import dp, bot
from states.name_meaning import Meaning

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="ℹ️ Ismlar ma'nosi", state='*')
async def meaning_of_name(message: types.Message, state: FSMContext):
    text = "<b>Ismingizni kiriting✍️</b>"
    await message.answer(text=text)

    await Meaning.name.set()


@dp.message_handler(state=Meaning.name)
async def get_user_name(message: types.Message, state: FSMContext):
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    user_id = message.from_user.id

    name = message.text

    if name.isalpha():

        url = f"https://supercoders.uz/ism.php?text={name}"

        deleted = await message.answer(text="<i>Biroz kuting...</i>")

        requesting = requests.get(url=url).json()

        if len(requesting[0]) == 0:
            await deleted.delete()
            await message.answer(text='<b>Afsuski hech narsa topilmadi😔\n\nBoshqa ism kiriting👇</b>')
            await Meaning.name.set()

        else:
            await deleted.delete()
            text = f"<b>{name}</b> - ismining ma'nosi✍️👇\n\n<i>{requesting[0]}</i>\n\n" \
                   f"✨<b>@{bot_username}</b> tomonidan taqdim etildi"
            await message.answer(text=text, reply_markup=is_admin(user_id=user_id))
            await state.finish()
    else:
        await message.answer(text='<b>Faqat harflardan foydalaning❗️\n\nBoshqa ism kiriting👇</b>')
        await Meaning.name.set()
