# Telegram Bot with Database

This is a **Telegram Bot** written in the Python programming language, which supports a database and its main function is to parse the web pages of an online bookstore.

It is easy to use and has simple commands underneath.

## Как его найти?
- Cсылка для работы с ботом: [t.me/parse14bot](https://t.me/parse14bot)

## Какие команды он имеет?
- ```/parse``` - команда которая выводит пять сообщений с заголовком, ценой и рейтингом книги
- ```/history``` - показывает историю запуска парсера пользователем 
- ```/help``` - выводит список имеющихся команд
- ```/url``` - возвращает ссылку на сайт с которого были взяты товары
## Установка дополнительного ПО
### PostgreSQL
- [Ссылка на гайд с полной установкой PostgreSQL](https://youtu.be/nxGhGQFk34Y?si=RHKnMYhpvTR8VZsm)
### BotFather
Здесь ничего устанавливать не нужно, от этого бота мы получаем только токен:<br>
- [Переходим по ссылке на BotFather](https://telegram.me/s/BotFther)
- Прописываем ```/newbot```
- Даём название своему боту
- Копируем токен
## Установка бота
1) Вам необходимо клонировать бота в любое место где вам удобно: <br>
   - ```git
     git clone https://github.com/JioSun/TGBotWithDB.git
     ```
2) Создаём и активируем виртуальное окружение
   -  ```python
      python -m venv venv
      ```
   - ```bash
     path\to\venv\Scripts\activate
     ```
3) В корне проекта открываем командную строку и прописываем в ней команду:<br>
   - ```python
     pip install -r requirements.txt
     ```
4) В корне проекта создаём файл ```.env```, копируем необходимые переменные из ```.env.exmaple``` и заполняем:
   ```
   BOT_TOKEN=токен бота, получаемый в BotFather
   DB_HOST=имя хоста, на котором активирована база данных
   DB_PORT=порт хоста
   DB_NAME=название базы данных
   DB_USER=имя пользователя базы данных
   DB_PASSWORD=пароль от базы данных
   ```
5) Активируем API-приложение(создаём локальный хост):<br>
   - ```python
     uvicorn api_directory.api_main:app --reload
     ```

6) Запускаем нашего бота: <br>
   - ```python
     python main.py
     ```
  
## Примеры работы бота
- [Вывод пять первых карточек магазина с книгами](https://s10.iimage.su/s/04/gKhv0eixVVk1dQiVMEvz59vX4jvzdWIZEP6gyURS6.png)
- [Показ истории запуска пользователем](https://iimg.su/i/inuIO4)
- [Вывод ссылки с магазином](https://iimg.su/i/ZpqWqu)
- [Описание изображения](https://site/foto)

## Какие библиотеки использовались для разработки?
[BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
[aiogram](https://docs.aiogram.dev/en/latest/)
[psycopg2](https://www.psycopg.org/docs/)
[dotenv](https://www.dotenv.org/docs/)

