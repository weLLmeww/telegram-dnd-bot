from aiogram.types import BotCommand

private = [
    BotCommand(command="start", description="Запустить бота"),
    BotCommand(command="clear", description="Очистить историю сообщений"),
    BotCommand(command="reset", description="Очистить контекст диалога")
    ]