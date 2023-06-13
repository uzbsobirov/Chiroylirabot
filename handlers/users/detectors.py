from aiogram import types

from data.config import ADMINS
from keyboards.default.start import start_admin, start
from handlers.download_functions.functions import all_downloader
from keyboards.inline.share import share


def search_video(item):
    if item.lower() == 'a':
        return 'https://t.me/forchrabot/3'

    elif item.lower() == 'b':
        return 'https://t.me/forchrabot/4'

    elif item.lower() == 'd':
        return 'https://t.me/forchrabot/5'

    elif item.lower() == 'e':
        return 'https://t.me/forchrabot/6'

    elif item.lower() == 'f':
        return 'https://t.me/forchrabot/7'

    elif item.lower() == 'g':
        return 'https://t.me/forchrabot/8'

    elif item.lower() == 'h':
        return 'https://t.me/forchrabot/9'

    elif item.lower() == 'i':
        return 'https://t.me/forchrabot/10'

    elif item.lower() == 'j':
        return 'https://t.me/forchrabot/11'

    elif item.lower() == 'k':
        return 'https://t.me/forchrabot/12'

    elif item.lower() == 'l':
        return 'https://t.me/forchrabot/13'

    elif item.lower() == 'm':
        return 'https://t.me/forchrabot/14'

    elif item.lower() == 'n':
        return 'https://t.me/forchrabot/15'

    elif item.lower() == 'o':
        return 'https://t.me/forchrabot/17'

    elif item.lower() == 'p':
        return 'https://t.me/forchrabot/18'

    elif item.lower() == 'q':
        return 'https://t.me/forchrabot/19'

    elif item.lower() == 'r':
        return 'https://t.me/forchrabot/20'

    elif item.lower() == 's':
        return 'https://t.me/forchrabot/21'

    elif item.lower() == 't':
        return 'https://t.me/forchrabot/22'

    elif item.lower() == 'u':
        return 'https://t.me/forchrabot/23'

    elif item.lower() == 'v':
        return 'https://t.me/forchrabot/24'

    elif item.lower() == 'x':
        return 'https://t.me/forchrabot/25'

    elif item.lower() == 'y':
        return 'https://t.me/forchrabot/26'

    elif item.lower() == 'z':
        return 'https://t.me/forchrabot/27'

    elif item.lower() == 'sh':
        return 'https://t.me/forchrabot/28'

    elif item.lower() == 'ch':
        return 'https://t.me/forchrabot/29'

    else:
        if item.isalnum():
            return 1
        else:
            return 2


def is_admin(user_id):
    if user_id == ADMINS[0]:
        return start_admin

    else:
        return start


def detect_downloader(link):
    if link.startswith('https://www.instagram.com/') or link.startswith('www.instagram.com/') or link.startswith(
            'instagram.com/'):
        return all_downloader(link=link)
    elif link.startswith('https://www.tiktok.com/') or link.startswith('tiktok.com/') or link.startswith(
            'www.tiktok.com/'):
        pass

    elif link.isalnum():
        return '<b>Faqat linklardan foydalaning❗️</b>'


async def video_or_image(link, message, media, username):
    caption = f"<b>📥 Downloaded via @{username}</b>"

    if link['Type'] == 'Post-Image':
        return await message.answer_photo(photo=media, caption=caption, reply_markup=share())

    elif link['Type'] == 'Post-Video':
        return await message.answer_video(video=media, caption=caption, reply_markup=share())
