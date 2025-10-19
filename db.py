import sqlite3
from typing import List, Tuple
from loguru import logger


def init_db() -> None:
    logger.debug("Инициализация базы данных")
    try:
        with sqlite3.connect("dialogues.db") as conn:
            cr = conn.cursor()
            cr.execute(
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
            conn.commit()
            logger.debug("База данных инициализирована успешно")
    except sqlite3.Error as e:
        logger.error(f"Ошибка при инициализации базы данных: {e}")
    

def add_message(user_id: int, role: str, content: str) -> None:
    logger.debug("Добавление сообщения в базу данных...")
    try:
        with sqlite3.connect("dialogues.db") as conn:
            cr = conn.cursor()
            cr.execute(
                "INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, content)
            )
            conn.commit()
            logger.info(f"Сообщение от '{role}' добавлено в базу данных")
    except sqlite3.Error as e:
        logger.error(f"Ошибка при добавлении сообщения {e}")


def get_history(user_id: int, limit: int = 10) -> List[Tuple[str, str]]:
    logger.debug("Чтение истории сообщений...")
    try:
        with sqlite3.connect("dialogues.db") as conn:
            cr = conn.cursor()
            cr.execute(
                """
                SELECT role, content
                FROM messages
                WHERE user_id = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (user_id, limit)
            )
            rows = cr.fetchall()
            logger.debug("История сообщений успешно прочитана")
            return [(role, content) for role, content in reversed(rows)]
        
    except sqlite3.Error as e:
        logger.error(f"Ошибка при чтении истории: {e}")
    

def clear_history(user_id: int) -> None:
    logger.debug(f"Инициализация очистки истории пользователя {user_id}")
    try:
        with sqlite3.connect("dialogues.db") as conn:
            cr = conn.cursor()
            cr.execute(
                "DELETE FROM messages WHERE user_id = ?;", (user_id,)
            )
            logger.success("История пользователя очищена")
            conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Ошибка при очистке истории: {e}")

init_db()