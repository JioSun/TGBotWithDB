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
План установки предполагает, что у вас установлено всё ПО, которое может позволить установить все следующие зависимости
1) Вам необходимо клонировать бота в любое место где вам удобно:
   ```git clone https://github.com/JioSun/TGBotWithDB.git```
   ![Компьютер](computer.png)
2) Создаём и активируем виртуальное окружение
   1. Создаёте каталог с своим названием в корне репозитория: ```python -m venv <имя>```
   2. Активируете с помощью такого пути сразу после создания виртуального окружения: ```path\to\venv\Scripts\activate```
3) В корне проекта открываем командную строку и прописываем в ней команду:
   ```pip install -r requirements.txt```
4) В корне проекта создаём файл ```.env```, копируем необходимые переменные из ```.env.exmaple``` и заполняем:
   ```
   BOT_TOKEN=токен бота, получаемый в BotFather
   DB_HOST=имя хоста, на котором активирована база данных
   DB_PORT=порт хоста
   DB_NAME=название базы данных
   DB_USER=имя пользователя базы данных
   DB_PASSWORD=пароль от базы данных
   ```
5) Активируем API-приложение(создаём локальный хост):
   В командной строке в корне проекта прописываем
   ```uvicorn api_directory.api_main:app --reload```
  
## Примеры работы бота
+ [Вывод пять первых карточек магазина с книгами](https://s10.iimage.su/s/04/gKhv0eixVVk1dQiVMEvz59vX4jvzdWIZEP6gyURS6.png)
+ [Показ истории запуска пользователем](https://iimg.su/i/inuIO4)
+ [Вывод ссылки с магазином](https://iimg.su/i/ZpqWqu)
![Описание изображения](https://site/foto)
## Какие библиотеки использовались для разработки?
[BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
[aiogram](https://docs.aiogram.dev/en/latest/)
[psycopg2](https://www.psycopg.org/docs/)
[dotenv](https://www.dotenv.org/docs/)

