from aiogram.dispatcher.filters.state import StatesGroup, State


class Rating(StatesGroup):
    rate = State()
    opinion = State()
