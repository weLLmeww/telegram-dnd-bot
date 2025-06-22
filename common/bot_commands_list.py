from aiogram.types import BotCommand

private = [
    BotCommand(command="start", description="запустить бота"),
    BotCommand(command="campaign", description="начать новую кампанию"),
    BotCommand(command="back", description="вернутся к прошлому шагу"),
    BotCommand(command="cancel", description="отменить создание кампании")
]