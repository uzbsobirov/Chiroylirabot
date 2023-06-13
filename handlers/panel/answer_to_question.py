from loader import dp, bot
from states.ratings import Rating

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="answer_to_user", state=Rating.answer)
async def get_user_opinion(call: types.CallbackQuery, state: FSMContext):
    text = "<b>Javobingizni yozing...</b>"
    await bot.send_message(chat_id=call.message.chat.id, text=text)

    await Rating.answer_text.set()


@dp.message_handler(state=Rating.answer_text, content_types=types.ContentType.ANY)
async def get_answer_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    text = data.get('user_request')

    await message.send_copy(chat_id=user_id)

    await text.delete()
    await message.delete()

    await bot.send_message(chat_id=message.chat.id, text="Javob yuboildi")

    await state.finish()

