import aiosqlite

from typing import List, Tuple
from loguru import logger

from config import BASE_DIR

DB_PATH = f"{BASE_DIR}\database\chat_history.db"


async def init_db() -> None:
    logger.debug("Инициализация базы данных")
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS messages (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    role    TEXT    NOT NULL, -- 'user' | 'assistant' | 'system' 
                    content TEXT    NOT NULL,
                    created_at  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            await db.commit()
            logger.debug("База данных инициализирована успешно")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка при инициализации базы данных: {e}")
    

async def add_message(user_id: int, role: str, content: str) -> None:
    logger.debug("Добавление сообщения в базу данных...")
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, content)
            )
            await db.commit()
            logger.info(f"Сообщение от '{role}' добавлено в базу данных")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка при добавлении сообщения {e}")


async def get_history(user_id: int, limit: int = 10) -> List[Tuple[str, str]]:
    logger.debug("Чтение истории сообщений...")
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            cr = await db.execute(
                """
                SELECT role, content
                FROM messages
                WHERE user_id = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (user_id, limit)
            )
            rows = await cr.fetchall()
            logger.debug("История сообщений успешно прочитана")
            return [(role, content) for role, content in reversed(rows)]
        
    except aiosqlite.Error as e:
        logger.error(f"Ошибка при чтении истории: {e}")
    

async def clear_history(user_id: int) -> None:
    logger.debug(f"Инициализация очистки истории пользователя {user_id}")
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "DELETE FROM messages WHERE user_id = ?;", (user_id,)
            )
            logger.success("История пользователя очищена")
            await db.commit()
    except aiosqlite.Error as e:
        logger.error(f"Ошибка при очистке истории: {e}")