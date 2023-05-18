from loader import dp
from states.video_chapter import Video
from data.config import ADMINS
from keyboards.default.start import start, start_admin

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="◀️ Orqaga", state='*')
async def back_to_main(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name

    text = f"<b>Assalomu aleykum {full_name}! Botimizga xush kelibsiz😊 " \
           f"Botimizdan bemalol foydalanishingiz mumkin💁‍♂️ Botda funksiyalar juda ko'p</b>"

    if user_id != ADMINS[0]:
        await message.answer(text=text, reply_markup=start)
    else:
        await message.answer(text=text, reply_markup=start_admin)

    await state.finish()