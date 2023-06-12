from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def share():
    markup = InlineKeyboardMarkup()
    markup.insert(
        InlineKeyboardButton(
            text="Do'stlarga ulashish ⤵️", switch_inline_query=f' | Sizga yoqishi aniq❤️‍🔥⚡️'
        )
    )
    return markup
