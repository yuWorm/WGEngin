# sanic app 初始化的一些监听
import asyncio

from sanic import Sanic

from common.log import logger
from database.conf import init_db, close_db
from database.mongo import client


def load_game_data():
    from game.核心.数据.加载数据 import 加载所有数据

    加载所有数据()


async def before_server_start(app):
    client.connect()
    # await init_db()
    load_game_data()


async def after_server_stop(app):
    # await close_db()
    client.disconnect()


def init(app: Sanic):
    app.listener(before_server_start, "before_server_start")
    app.listener(after_server_stop, "after_server_stop")
