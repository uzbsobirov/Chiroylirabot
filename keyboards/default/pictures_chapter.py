from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menues = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🧑‍🦰 O'g'il bolalar uchun"
            ),
            KeyboardButton(
                text="👱‍♀️ Qiz bolalar uchun"
            )
        ],
        [
            KeyboardButton(
                text="👫 Juftlik rasmlar"
            )
        ],
        [
            KeyboardButton(
                text="📝 Status yasash"
            )
        ],
        [
            KeyboardButton(
                text="◀️ Orqaga"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)