# Telegram Bot with Database

This is a **Telegram Bot** written in the Python programming language, which supports a database and its main function is to parse the web pages of an online bookstore.

It is easy to use and has simple commands underneath.

## How to find it?
- Link for working with Bot: [t.me/parse14bot](https://t.me/parse14bot)

## Available commands
- ```/parse``` - command that returns five product cards in a single message
- ```/history``` - shows the user's command history 
- ```/help``` - displays the list of available commands
- ```/url``` - returns the link to the website from which the products were taken
## Additional software installation
### Git
- [Git installation guide](https://youtu.be/xiPXztV8WUk?si=Wh9n4y1sA0pyv9mf)
### PostgreSQL
- [Full PostgreSQL installation guide](https://youtu.be/nxGhGQFk34Y?si=RHKnMYhpvTR8VZsm)
### BotFather
Nothing needs to be installed here, this bot is only used to obtain a token:<br>
- [Open BotFather via the link](https://telegram.me/s/BotFther)
- Enter ```/newbot```<br>
![Enter /newbot](IFG/IFG6.png)
- Set a name for your bot<br>
![Enter /newbot](IFG/IFG7.png)
- Copy the token<br>
![Копируем](IFG/IFG8.png)
## Bot installation
1) Clone the bot to any convenient location: <br>
   - ```git
     git clone https://github.com/JioSun/TGBotWithDB.git
     ```
     ![Cloning the repository to your device](IFG/IFG1.png)
2) Create and activate a virtual environment
   -  ```
      python -m venv venv
      ```
      ![Creating a virtual environment](IFG/IFG2.png)
   - ```
     path\to\venv\Scripts\activate
     ```
     ![Activating a virtual environment](IFG/IFG3.png)
3) In the project root, open a terminal and run:<br>
   - ```
     pip install -r requirements.txt
     ```
4) In the project root, create a file ```.env```, copy the required variables from ```.env.exmaple``` and fill them in:
     ```
     BOT_TOKEN=token received from BotFather
     DB_HOST=database host
     DB_PORT=host port
     DB_NAME=database name
     DB_USER=database username
     DB_PASSWORD=database password
     ```
5) Start the API application (create a local server):<br>
   - ```
     uvicorn api_directory.api_main:app --reload
     ```
     ![Running the API application](IFG/IFG4.png)
6) Run the bot: <br>
   - ```
     python main.py
     ```
     ![Running the bot](IFG/IFG5.png)
## Examples of bot usage
### Example of /parse command
![Example of /parse command](IFG/IFG9.png)
### Example of /history command
![Example of /history command](IFG/IFG10.png)
### Example of /url command
![Example of /url command](IFG/IFG11.png)
### Example of /help command
![Example of /help command](IFG/IFG12.png)


