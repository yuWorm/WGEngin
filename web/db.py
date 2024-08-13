from sanic import Sanic
from database.conf import db_conf
from tortoise.contrib.sanic import register_tortoise


def init(app: Sanic):
    register_tortoise(app, config=db_conf)
