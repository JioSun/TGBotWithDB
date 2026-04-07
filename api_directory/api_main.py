from fastapi import FastAPI, HTTPException
from Parser.parse_file import orchestrator
from api_directory.api_classes.api_cls import BookList, Book, HistoryCreate, User, HistoryList
from database.db_main import launch_history, launch_init


app = FastAPI()


@app.get("/books")
async def books_json() -> list[Book]:
    _obj = BookList(books=orchestrator())
    if len(_obj.books) == 0:
        raise HTTPException(status_code=404, detail="Page not found")
    return _obj.books[:5]

@app.get("/history/{user_id}")
async def api_launch_history(user_id: int) -> HistoryList:
    _obj = User(user_id=user_id)
    result = HistoryList(history=launch_history(_obj.user_id))
    return result

@app.post('/history', response_model=HistoryCreate)
async def api_launch_init(history_init: HistoryCreate):
    launch_init(history_init.user_id, history_init.username, history_init.date)
    return {"success": True}
