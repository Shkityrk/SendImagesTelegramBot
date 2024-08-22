from aiogram.filters.state import State, StatesGroup


class CommandStates(StatesGroup):
    waiting_for_prompt = State()
    sleep_time = State()