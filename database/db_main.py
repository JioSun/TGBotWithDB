import psycopg2
from os import getenv

DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")

def db_init():
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        cur = conn.cursor()
        cur.execute("""
                           CREATE TABLE IF NOT EXISTS launch_history
                           (
                               user_id INT NOT NULL,
                               username TEXT NOT NULL,
                               launch_time TEXT NOT NULL
                           )
                           """)
        conn.commit()

def launch_init( user_id: int, username: str, launch_time: str) -> None:
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO launch_history (user_id, username, launch_time) VALUES (%s, %s, %s)",
            (user_id, username, launch_time)
        )
        conn.commit()

def launch_history(user_id: int) -> list:
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT username, launch_time FROM launch_history WHERE user_id = %s ORDER BY launch_time DESC LIMIT 5
        """, (user_id, ))
        return cursor.fetchall()