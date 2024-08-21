from sanic import Blueprint, Request, text
from common.context import context_bind, r
from common.request import request_parmas_to_dict
from game.核心.工具方法 import 页面
from game.页面 import 页面管理, 页面配置


bp = Blueprint("Game")


@bp.route("/")
@context_bind
async def index(request: Request):
    return await 页面管理.页面路由(request)


@bp.route("/game", methods=["GET", "POST"])
@context_bind
async def page(request: Request):
    return await 页面管理.页面路由(request)
