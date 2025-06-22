from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


admin_kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="admin")]
    ]
)


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

fsm_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="cancel"),
            KeyboardButton(text="back")
        ]
    ]
)

del_kb = ReplyKeyboardRemove()