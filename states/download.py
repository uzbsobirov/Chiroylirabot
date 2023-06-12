from aiogram.dispatcher.filters.state import StatesGroup, State


class Downloader(StatesGroup):
    link = State()
