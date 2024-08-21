from tortoise import Tortoise
from config.setting import settings

db_conf = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": settings.MYSQL_HOST,
                "port": settings.MYSQL_PORT,
                "user": settings.MYSQL_USER,
                "password": settings.MYSQL_PASSWORD,
                "database": settings.MYSQL_DATABASE,
            },
        }
    },
    "apps": {
        "models": {
            "models": [
                "database.base",
                "aerich.models",
                # "game.db.models",
            ],  # 替换为你自己的模型模块路径
            "default_connection": "default",
        }
    },
}


async def init_db():
    await Tortoise.init(db_conf)


async def close_db():
    await Tortoise.close_connections()
