from pydantic import BaseModel
from typing import Optional

class HistoryCreate(BaseModel):
    username: str
    date: str
    user_id: int

class History(BaseModel):
    username: str
    date: str

class HistoryList(BaseModel):
    history: list[History]

class Book(BaseModel):
    title: str
    price: str
    rating: str

class BookList(BaseModel):
    books: list[Book]

class User(BaseModel):
    user_id: int
    username: Optional[str] = None
