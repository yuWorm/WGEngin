from sanic import Blueprint, Request, text
from common.context import context_bind, r
from common.request import request_parmas_to_dict
from game.核心.工具方法 import 页面
from game.页面 import 页面管理, 页面配置
from web.auth import user_info

bp = Blueprint("Game")


@bp.route("/")
@context_bind
@user_info
async def index(request: Request):
    return await 页面管理.渲染游戏首页()


@bp.route("/game", methods=["GET", "POST"])
@context_bind
@user_info
async def page(request: Request):
    en_args_str = request.args.get("p")
    request_args = {}
    if not en_args_str:
        return await 页面管理.渲染错误页面("无法正确解析页面")

    en_args = 页面.解密页面路径数据(en_args_str)
    page_name = en_args.pop("p", None)
    time = en_args.pop("t", None)
    if not page_name:
        return await 页面管理.渲染错误页面("找不到页面")

    # 登录校验
    if page_name not in 页面配置.不需要登录的页面:
        if not r.ctx.g.是否登录:
            _登录页面路径 = 页面.获取页面路径(页面配置.登录页面)
            return 页面.重定向页面(_登录页面路径)

    # 将请求数据更新到请求参数中
    form_data = request_parmas_to_dict(request.form.copy())
    get_data = request_parmas_to_dict(request.args.copy())
    get_data.pop("p", None)
    request_args.update(get_data)
    request_args.update(form_data)

    page_response = await 页面管理.渲染页面(page_name, en_args, request_args)
    return page_response
