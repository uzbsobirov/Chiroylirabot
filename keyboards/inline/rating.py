from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🖊 Javob yozish", callback_data='answer_to_user'
            )
        ]
    ]
)