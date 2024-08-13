import click
from web.server import run


@click.command(name="run", help="启动游戏")
def run_server():

    run()
