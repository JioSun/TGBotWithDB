from datetime import datetime
import json
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import requests

router = Router()

@router.message(Command("start"))
async def hello(message: Message) -> None:
    await message.answer(f"Привет, это парсер интернет магазина!")

@router.message(Command("parse"))
async def parse(message: Message) -> None:
    try:
        products = requests.get('http://127.0.0.1:8000/books')
        products.raise_for_status()

        if len(json.dumps(products.json())) == 0:
            await message.answer('Список книг пуст')
        else:
            s = ''
            for i, product in enumerate(products):
                s += f'Книга {i + 1}:\n'\
                                     f'\tНазвание: {product['title']}\n'\
                                     f'\tЦена: {product['price']}\n'\
                                     f'\tРейтинг: {product['rating']}\n\n'
            await message.answer(s)
    except Exception as e:


@router.message(Command("history"))
async def history(message: Message) -> None:
    try:
        products = requests.get(f'http://127.0.0.1:8000/history/{message.}')
    if len(lst) == 0:
        await message.answer('Вы ещё не делали запросов')
    else:
        history_stroke = [f'{i + 1}) {' '.join([el.username, el.date])}\n' for i, el in enumerate(lst)]
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


