import sqlite3

def db_init() -> None:
    with sqlite3.connect('TGbot.db') as db:
        cursor = db.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS launch_history
                       (
                           user_id INT NOT NULL,
                           username TEXT NOT NULL,
                           launch_time TEXT NOT NULL
                       )
                       """)

        db.commit()

def launch_init(user_id: int, username: str, launch_time: str) -> None:
    with sqlite3.connect('TGbot.db') as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO launch_history (user_id, username, launch_time) VALUES (?, ?, ?)",
            (user_id, username, launch_time)
        )
        db.commit()

def launch_history(user_id: int) -> list:
    with sqlite3.connect('TGbot.db') as db:
        cursor = db.cursor()
        cursor.execute("""
        SELECT username, launch_time FROM launch_history WHERE user_id = ? ORDER BY launch_time DESC LIMIT 5
        """, (user_id, ))
        return cursor.fetchall()
