from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from ai import handle_message
from keyboards.reply_keyboard import fsm_kb
user_router = Router()



class SetCampaign(StatesGroup):
    setting = State()
    class_and_race = State()
    story = State()
    wishes = State()

    texts = {
        'SetCampaign:setting': 'Опиши мир заново',
        'SetCampaign:class_and_race': 'Выбери класс и расу заново',
        'SetCampaign:story': 'Расскажи предысторию заново',
        'SetCampaign:wishes': 'Пожелания?',
    }



@user_router.message(StateFilter('*'), Command("cancel"))
@user_router.message(F.text.lower() == "отменить")
async def cancel_hadler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("действия отменены", reply_markup=fsm_kb)


@user_router.message(StateFilter('*'), Command("back"))
@user_router.message(F.text.lower() == "назад")
async def back_handler(message: types.Message, state: FSMContext):

    current_state = await state.get_state()

    if current_state == SetCampaign.setting:
        await message.answer("Предыдущего шага нет, опишите сеттинг или введите \"отмена\"")

    previous = None
    for step in SetCampaign.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"Вы вернулись к предыдущему шагу. \n{SetCampaign.texts[previous.state]}")

        previous = step


@user_router.message(StateFilter(None), Command("campaign"))
async def start_cmd(message: types.Message, state: FSMContext):
    print("поступила команда старта компании")
    await message.answer("привет бла бла бла, расскажи про мир", reply_markup=fsm_kb)
    await state.set_state(SetCampaign.setting)


@user_router.message(SetCampaign.setting, F.text)
async def set_setting(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(setting = message.text)
    await message.answer("теперь выбери класс и расу", reply_markup=fsm_kb)
    await state.set_state(SetCampaign.class_and_race)


@user_router.message(SetCampaign.class_and_race, F.text)
async def set_class_and_race(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(class_and_race = message.text)
    await message.answer("теперь выбери предысторию", reply_markup=fsm_kb)
    await state.set_state(SetCampaign.story)


@user_router.message(SetCampaign.story, F.text)
async def set_story(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(story = message.text)
    await message.answer("пожелания?", reply_markup=fsm_kb)
    await state.set_state(SetCampaign.wishes)


@user_router.message(SetCampaign.wishes, F.text)
async def set_wishes(message: types.Message, state: FSMContext):
    print(f"поступило сообщение {message.text}")
    await state.update_data(wishes = message.text)
    data = await state.get_data()
    await message.answer(f"правильно? {data}")
    await state.clear()


@user_router.message()
async def bla(message: types.Message):
    print(f"поступило сообщение {message.text}")
    await message.answer(handle_message(message))