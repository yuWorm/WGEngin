from sanic import Request

from common.context import g
from common.request import request_parmas_to_dict
from game.核心.基础异常 import 页面异常
from game.核心.基础数据类 import 字典, 文本
from game.核心.基础数据类型 import 文本类型, 字典类型, 空, 是
from game.核心.工具方法.数据库 import 数据库工具
from game.核心.工具方法.时间 import 当前时间_单位秒
from game.核心.数据.游戏数据 import 页面表
from game.核心.工具方法 import 页面 as 页面工具
from game.核心.基类.游戏.用户 import 用户类
from game.页面 import 页面配置


async def 登录检测(_请求: Request):
    _用户ID = _请求.ctx.session.get("user_id")
    if _用户ID:
        _用户 = await 用户类.获取(_用户ID)
        if not _用户:
            return
        else:
            g.用户 = _用户
            g.是否登录 = 是


async def 页面路由(_请求: Request):
    if _请求.route.path == "" or _请求.route.path == "/":
        await 登录检测(_请求)
        return await 渲染游戏首页()

    _页面参数加密字符 = 文本(_请求.args.get("p", ""))
    _页面参数 = 字典({})
    if not _页面参数加密字符.去空():
        return await 渲染错误页面("无法正确解析页面")
    _页面参数.更新(页面工具.解密页面路径数据(_页面参数加密字符))
    _页面名称 = _页面参数.弹出("p")
    _页面构建的时间 = _页面参数.弹出("t")
    if not _页面名称:
        return await 渲染错误页面("找不到页面")

    _当前时间 = 当前时间_单位秒()
    # 如果刷新时间小于2秒,就跳转到错误页面
    # if (float(_页面构建的时间) - _当前时间) < 2:
    #     # 当然这里也能加次数,如过连续多少次就报错
    #     return await 渲染错误页面("你的动作太快了,请休息一样")

    # 检测是否登录, 然后将用户信息挂载到全局变量
    await 登录检测(_请求)
    # 登录校验
    if _页面名称 not in 页面配置.不需要登录的页面:
        if not g.是否登录:
            _登录页面路径 = 页面工具.获取页面路径(页面配置.登录页面)
            return 页面工具.重定向页面(_登录页面路径)

    _请求参数 = 字典({})
    form_data = request_parmas_to_dict(_请求.form.copy())
    get_data = request_parmas_to_dict(_请求.args.copy())
    # 将加密参数弹出
    get_data.pop("p")
    # 将数据更新到请求参数
    _请求参数.更新(form_data)
    _请求参数.更新(get_data)
    return await 渲染页面(_页面名称, _页面参数, _请求参数)


async def 渲染页面(
    _页面名称: 文本类型, _页面参数: 字典类型 = 空, _请求参数: 字典类型 = 空
):
    _页面类 = 页面表.get(_页面名称)
    # 判断页面是否存在
    if not _页面类:
        return 页面工具.错误页面("页面不存在")

    if not _页面参数:
        _页面参数 = {}

    if not _请求参数:
        _请求参数 = {}

    _页面 = _页面类()
    try:
        await _页面.加载数据(_页面参数, _请求参数)
        _页面渲染结果 = await _页面.渲染页面()
    except 页面异常 as e:
        return 页面工具.错误页面(str(e))
    except 页面工具.跳转页面标志 as re:
        return 页面工具.重定向页面(re.页面路径())
    return _页面渲染结果


async def 渲染错误页面(_消息: 文本类型):
    return 页面工具.错误页面(_消息)


async def 渲染游戏首页():
    return await 渲染页面("首页")
