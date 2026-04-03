from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from Parser.parse_file import orchestrator
from database.db_main import launch_init, launch_history
from datetime import datetime
router = Router()

@router.message(Command("start"))
async def hello(message: Message) -> None:
    await message.answer(f"Привет, это парсер интернет магазина!")

@router.message(Command("parse"))
async def parse(message: Message) -> None:
    products = orchestrator()
    if products is None:
        await message.answer('Список книг пуст. Не удалось обработать информацию')
    else:
        for i, product in enumerate(products):
            await message.answer(f'Книга {i + 1}:\n'
                                 f'\tНазвание: {product['title']}\n'
                                 f'\tЦена: {product["price"]}\n'
                                 f'\tРейтинг: {product["rating"]}\n')
    launch_init(message.from_user.id, message.from_user.username, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@router.message(Command("history"))
async def history(message: Message) -> None:
    lst = launch_history(message.from_user.id)[::-1][:5]
    if len(lst) == 0:
        await message.answer('Вы ещё не делали запросов')
    else:
        history_stroke = [f'{i + 1}) {' '.join(el)}\n' for i, el in enumerate(lst)]
        await message.answer(f'Ваши последнии запросы:\n{''.join(history_stroke)}')

@router.message(Command('url'))
async def start(message: Message) -> None:
    await message.answer('Ссылка на сайт, откуда бралась информация\nhttps://books.toscrape.com/')

@router.message(Command("help"))
async def help(message: Message) -> None:
    await message.answer('Всё команды на данный момент:\n/parse\n/url\n/history\n/help')

@router.message()
async def echo_handler(message: Message) -> None:
    await message.answer('Не понимаю команду. Используй /parse')




