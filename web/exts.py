# 加载一些sanic的拓展
from sanic import Sanic
from sanic_session import Session
from common.session import AIORedisSessionInterface
from config.setting import settings
from database.redis import redis_client


def init(app: Sanic):
    init_session(app)


def init_session(app: Sanic):
    Session(
        app,
        interface=AIORedisSessionInterface(
            redis_client, expiry=settings.SESSION_EXPIRE_TIME
        ),
    )
