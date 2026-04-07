import psycopg2
from os import getenv
from dotenv import load_dotenv
from api_directory.api_classes.api_cls import History

load_dotenv()
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")

def get_connection():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    return conn

def db_init():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                       CREATE TABLE IF NOT EXISTS launch_history
                       (
                           user_id BIGINT NOT NULL,
                           username TEXT NOT NULL,
                           launch_time TEXT NOT NULL
                       )
                       """)
    conn.commit()

    cur.close()
    conn.close()

def launch_init(user_id: int, username: str, launch_time: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO launch_history (user_id, username, launch_time) VALUES (%s, %s, %s)",
        (user_id, username, launch_time)
    )
    conn.commit()

    cursor.close()
    conn.close()

def launch_history(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT username, launch_time FROM launch_history WHERE user_id = %s ORDER BY launch_time DESC LIMIT 5
    """, (user_id, ))

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return [History(username=el[0], date=el[1]) for el in result]

