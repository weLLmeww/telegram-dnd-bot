from aiogram import types, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from ai import handle_message
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
    await message.answer("Это команда старт", reply_markup=reply_keyboard.start_kb)
    await state.set_state(SetCampaign.setting)


@user_router.message(SetCampaign.setting)
async def set_setting(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    answer = handle_message(message)
    await state.update_data(setting = message.text)
    await message.answer(answer, parse_mode="Markdown")
    print(f"выдан ответ: \n{answer}")
    await state.set_state(SetCampaign.class_and_race)


@user_router.message(SetCampaign.class_and_race)
async def set_setting(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    answer = handle_message(message)
    await state.update_data(class_and_race = message.text)
    await message.answer(answer, parse_mode="Markdown")
    print(f"выдан ответ: \n{answer}")
    await state.set_state(SetCampaign.story)

@user_router.message(SetCampaign.story)
async def set_setting(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    answer = handle_message(message)
    await state.update_data(story = message.text)
    await message.answer(answer, parse_mode="Markdown")
    print(f"выдан ответ: \n{answer}")
    await state.set_state(SetCampaign.wishes)

@user_router.message(SetCampaign.wishes)
async def set_setting(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    answer = handle_message(message)
    await state.update_data(wishes = message.text)
    await message.answer(answer, parse_mode="Markdown")
    print(f"выдан ответ: \n{answer}")
    await state.set_state(SetCampaign.wishes)