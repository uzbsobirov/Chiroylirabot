from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


ratings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📩 Fikr bildirish"
            ),
            KeyboardButton(
                text="🌟 Botni baholash"
            )
        ],
        [
            KeyboardButton(
                text="◀️ Orqaga"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)