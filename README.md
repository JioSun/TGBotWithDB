# Telegram Bot with Database

This is a **Telegram Bot** written in the Python programming language, which supports a database and its main function is to parse the web pages of an online bookstore.

It is easy to use and has simple commands underneath.

## Как его найти?
Вот ссылка для пользования ботом: [t.me/parse14bot](https://t.me/parse14bot)

## Какие команды он имеет?
```/parse``` - команда которая выводит пять сообщений с заголовком, ценой и рейтингом книги
```/history``` - показывает историю запуска парсера пользователем 
```/help``` - выводит список имеющихся команд
```/url``` - возвращает ссылку на сайт с которого были взяты товары

## Установка
1. Клонируй репозиторий
2. Установи зависимости: `pip install -r requirements.txt`
3. Создай `.env` из `.env.example` и заполни переменные
4. Запусти: `python main.py`
   
## Примеры работы бота
+ [Вывод пять первых карточек магазина с книгами](https://iimg.su/i/Khv0ei)
+ [Показ истории запуска пользователем](https://iimg.su/i/inuIO4)
+ [Вывод ссылки с магазином](https://iimg.su/i/ZpqWqu)

## Какие библиотеки использовались для разработки?
[BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
[aiogram](https://docs.aiogram.dev/en/latest/)
[psycopg2](https://www.psycopg.org/docs/)
[dotenv](https://www.dotenv.org/docs/)

