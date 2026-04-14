import click
from database.db_main import table_add

@click.group()
def cli():
    pass

@cli.group()
def task():
    pass

@task.command()
@click.argument('text', type=str)
def add(text):
    table_add(text)
    click.echo('Task added')
