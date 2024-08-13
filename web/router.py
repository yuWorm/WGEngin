# 路由信息表
from sanic import Sanic


def init(app: Sanic):
    # app.add_route()
    from web.game.page import bp as game_page

    app.blueprint(game_page)
