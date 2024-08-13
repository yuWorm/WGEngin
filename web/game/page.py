from sanic import Blueprint, Request, text
from common.context import context_bind
from game.核心.工具方法 import 页面
from game.页面 import 页面管理

bp = Blueprint("Game")


@bp.route("/")
@context_bind
async def index(request: Request):
    return await 页面管理.渲染游戏首页()


@bp.route("/game", methods=["GET", "POST"])
@context_bind
async def page(request: Request):
    arg_str = request.args.get("p")
    if not arg_str:
        return await 页面管理.渲染错误页面("无法正确解析页面")

    args = 页面.解密页面路径数据(arg_str)
    page_name = args.pop("p", None)
    if not page_name:
        return await 页面管理.渲染错误页面("找不到页面")

    page_response = await 页面管理.渲染页面(page_name, **args)
    return page_response
