from data.config import ADMINS
from handlers.users.detectors import is_admin
from keyboards.inline.rating import answer
from loader import dp, bot
from states.ratings import Rating
from keyboards.default.ratings import ratings

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📜 Biz haqimizda", state='*')
async def meaning_of_name(message: types.Message, state: FSMContext):
    text = "<b>O'zingizga keraklisini tanlang👇</b>"

    await message.answer(text=text, reply_markup=ratings)

    await Rating.rate.set()


@dp.message_handler(text="📩 Fikr bildirish", state=Rating.rate)
async def rate_opinion(message: types.Message, state: FSMContext):
    text = "<i>Fikringizni yozib yuboring...</i>"
    await message.answer(text=text)

    await Rating.opinion.set()


@dp.message_handler(state=Rating.opinion)
async def get_opinion(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    user_mention = message.from_user.get_mention(name=full_name)

    user_opinion = message.text

    await message.answer(text="Xabaringiz adminga yuborildi✔️", reply_markup=is_admin(user_id=user_id))

    text = f"<b>{user_mention} -- fikr bildirdi👇</b>\n\n<i>{user_opinion}</i>"

    await bot.send_message(chat_id=ADMINS[0], text=text, reply_markup=answer)
