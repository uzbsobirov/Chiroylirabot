import logging

from handlers.users.detectors import detect_downloader, video_or_image
from loader import dp, bot
from states.download import Downloader

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📥 Video yuklash", state='*')
async def video_downloader(message: types.Message, state: FSMContext):
    text = "<b>Video linkini yuboring men uni yuklab beraman👇</b>"

    await message.answer(text=text)

    await Downloader.link.set()


@dp.message_handler(state=Downloader.link)
async def get_video_link(message: types.Message, state: FSMContext):
    get_me = await bot.get_me()
    bot_username = get_me.username

    link = message.text

    get_data = detect_downloader(link=link)

    try:
        media = get_data['media']
        await video_or_image(link=get_data, message=message, media=media, username=bot_username)
    except Exception as error:
        logging.info(error)
        await message.answer('⚠️ The media file could not be downloaded')

    await state.finish()

