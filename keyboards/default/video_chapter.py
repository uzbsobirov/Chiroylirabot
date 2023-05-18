from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menues = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🎁 Bepul"
            ),
            KeyboardButton(
                text="💸 Pullik"
            )
        ],
        [
            KeyboardButton(
                text="◀️ Orqaga"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)