from loader import dp
from states.ratings import Rating

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="answer_to_user", state=Rating.rate)
async def get_user_opinion(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')

    print(user_id)