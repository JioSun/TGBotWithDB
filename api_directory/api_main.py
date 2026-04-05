from fastapi import FastAPI
from Parser.parse_file import orchestrator
from database.db_main import launch_history, launch_init
app = FastAPI()


@app.get("/books/page{page_number}")
async def books_json(page_number: int):
    return orchestrator(page_number)

@app.get("/history/{user_id}")
async def history_list(user_id: int):
    return launch_history(user_id)

@app.post('/history')
async def history_init(user_id: int, username: str, launch_time: str):
    return launch_init(user_id, username, launch_time)