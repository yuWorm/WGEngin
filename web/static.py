import os

from sanic import Sanic
from config.path_conf import BASE_DIR


def init(app: Sanic):
    app.static("/static/game", os.path.join(BASE_DIR, "game/页面资源"))
