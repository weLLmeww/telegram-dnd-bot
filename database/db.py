import sqlite3
from pathlib import Path
from typing import List, Tuple


def init_db() -> None:
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
    

def add_message(user_id: int, role: str, content: str) -> None:
    with sqlite3.connect("dialogues.db") as conn:
        cr = conn.cursor()
        cr.execute(
            "INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, content)
        )
        conn.commit()

def get_history(user_id: int, limit: int = 10) -> List[Tuple[str, str]]:
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
        
        return [(role, content) for role, content in reversed(rows)]
    

init_db()