from handlers.CLI_main import cli
from database.db_main import table_create
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    table_create()
    cli()
