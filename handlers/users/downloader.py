import logging

from handlers.download_functions.functions import all_downloader
from handlers.users.detectors import detect_downloader, video_or_image
from keyboards.inline.share import share
from loader import dp, bot
from states.download import Downloader

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📥 Video yuklash", state='*')
async def video_downloader(message: types.Message, state: FSMContext):
    text = "<b>Video linkini yuboring men uni yuklab beraman👇</b>"

    await message.answer(text=text)

    await Downloader.link.set()


@dp.message_handler(state=Downloader.link, content_types=types.ContentType.ANY)
async def get_video_link(message: types.Message, state: FSMContext):
    get_me = await bot.get_me()
    bot_username = get_me.username

    link = message.text

    get_data = all_downloader(link=link)
    clock = await message.answer(text='⏳')

    caption = f"<b>📥 Downloaded via @{bot_username}</b>"

    try:
        media = get_data[0]
        await message.answer_video(video=media, caption=caption, reply_markup=share())

    except KeyError as Kerror:
        logging.info(Kerror)
        convert_to_dict = dict(get_data)
        video_mp3 = convert_to_dict['Download MP3']['url']
        video = convert_to_dict['Without watermark']['url']
        downlaod_file = await bot.download_file(video, destination=r'D:\Programming\video.mp4')
        # with open()
        await clock.delete()
        # await message.answer_video(video=video, caption=caption, reply_markup=share())
        # await message.answer_audio(audio=video_mp3, caption=caption, reply_markup=share())



    # try:
    #     await video_or_image(link=get_data, message=message, media=media, username=bot_username)
    # except Exception as error:
    #     logging.info(error)
    #     await message.answer('⚠️ The media file could not be downloaded')
    #
    # await state.finish()

