from aiogram import types, Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import reply_keyboard
user_router = Router()



class SetCampaign(StatesGroup):
    setting = State()
    class_and_race = State()
    story = State()
    wishes = State()


@user_router.message(StateFilter(None), CommandStart())
async def start_cmd(message: types.Message, state: FSMContext):
    print("поступила команда старт")
    await message.answer("привет бла бла бла, расскажи про мир")
    await state.set_state(SetCampaign.setting)


@user_router.message(SetCampaign.setting, F.text)
async def set_setting(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(setting = message.text)
    await message.answer("теперь выбери класс и расу")
    await state.set_state(SetCampaign.class_and_race)


@user_router.message(SetCampaign.class_and_race, F.text)
async def set_class_and_race(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(class_and_race = message.text)
    await message.answer("теперь выбери предысторию")
    await state.set_state(SetCampaign.story)


@user_router.message(SetCampaign.story, F.text)
async def set_story(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(story = message.text)
    await message.answer("пожелания?")
    await state.set_state(SetCampaign.wishes)


@user_router.message(SetCampaign.wishes, F.text)
async def set_wishes(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(wishes = message.text)
    data = await state.get_data()
    await message.answer(f"правильно? {data}")
    await state.clear()