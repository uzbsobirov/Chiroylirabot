from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📹 Videolar bo'limi"
            ),
            KeyboardButton(
                text="🖼 Suratlar bo'limi"
            )
        ],
        [
            KeyboardButton(
                text="📥 Video yuklash"
            )
        ],
        [
            KeyboardButton(
                text="🌙 Islomiy bo'lim"
            ),
            KeyboardButton(
                text="✍️ Niklar bo'limi"
            )
        ],
        [
            KeyboardButton(
                text="📩 Fikr bildirish"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

start_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📹 Videolar bo'limi"
            ),
            KeyboardButton(
                text="🖼 Suratlar bo'limi"
            )
        ],
        [
            KeyboardButton(
                text="📥 Video yuklash"
            )
        ],
        [
            KeyboardButton(
                text="🌙 Islomiy bo'lim"
            ),
            KeyboardButton(
                text="✍️ Niklar bo'limi"
            )
        ],
        [
            KeyboardButton(
                text="📩 Fikr bildirish"
            )
        ],
        [
            KeyboardButton(
                text="🖥 Admin panel"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)