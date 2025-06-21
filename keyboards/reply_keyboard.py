from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Старт")
        ],
        [
            KeyboardButton(text="Оплата"),
            KeyboardButton(text="бебра")
        ]
    ],
    resize_keyboard = True,
    input_field_placeholder = "Что интересует?"
)

del_kb = ReplyKeyboardRemove()