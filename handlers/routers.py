from datetime import datetime
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from .api_response import get_books, get_history, post_history


router = Router()


@router.message(Command("start"))
async def get_hello_message(message: Message) -> None:
    await message.answer(f"Привет, это парсер интернет магазина!")

@router.message(Command("parse"))
async def get_parse_page(message: Message) -> None:
    username = message.from_user.username or 'unknown_user'
    payload = {
        "user_id": message.from_user.id,
        "username": username,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        books = await get_books()
        if len(books) == 0:
            await message.answer('Список книг пуст')
        else:
            s = ''

            for i, book in enumerate(books):
                s += (
                    f"Книга {i + 1}:\n"
                    f"\tНазвание: {book['title']}\n"
                    f"\tЦена: £{book['price']}\n"
                    f"\tРейтинг: {book['rating']}\n\n"
                )

            await message.answer(s)
            await post_history(payload)
    except Exception:
        await message.answer("Ошибка при обращении к API")

@router.message(Command("history"))
async def get_history_message(message: Message) -> None:
    try:
        history_list = await get_history(message.from_user.id)
        if len(history_list['history']) == 0:
            await message.answer("Вы ещё не делали запросов")
        else:
            history_text = "Ваши последние запросы:\n\n" + "\n".join(
                f"{i + 1}) {item['username']} — {item['date']}"
                for i, item in enumerate(history_list['history'])
            )
            await message.answer(history_text)
    except Exception:
        await message.answer("Ошибка при обращении к API")


@router.message(Command('url'))
async def get_url(message: Message) -> None:
    await message.answer('Ссылка на сайт, откуда бралась информация\nhttps://books.toscrape.com/')

@router.message(Command("help"))
async def get_help(message: Message) -> None:
    await message.answer('Всё команды на данный момент:\n/parse\n/url\n/history\n/help')

@router.message()
async def echo_handler(message: Message) -> None:
    await message.answer('Не понимаю команду. Используй /parse')


