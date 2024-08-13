import click
from command.db import cli
from click import Command
from command.server import run_server

db_cli: Command = cli


@click.group()
def main():
    pass


main.add_command(db_cli, name="db")
main.add_command(run_server)
