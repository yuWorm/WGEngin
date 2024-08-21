from game.核心.基础异常 import 页面异常
from game.核心.基础数据类型 import 文本类型, 字典类型, 空
from game.核心.工具方法.数据库 import 数据库工具
from game.核心.数据.游戏数据 import 页面表
from game.核心.工具方法 import 页面


async def 渲染页面(
    _页面名称: 文本类型, _页面参数: 字典类型 = 空, _请求参数: 字典类型 = 空
):
    _页面类 = 页面表.get(_页面名称)
    # 判断页面是否存在
    if not _页面类:
        return 页面.错误页面("页面不存在")

    if not _页面参数:
        _页面参数 = {}

    if not _请求参数:
        _请求参数 = {}

    _页面 = _页面类()
    try:
        await _页面.加载数据(_页面参数, _请求参数)
        _页面渲染结果 = await _页面.渲染页面()
    except 页面异常 as e:
        return 页面.错误页面(str(e))
    except 页面.跳转页面标志 as re:
        return 页面.重定向页面(re.页面路径())
    return _页面渲染结果


async def 渲染错误页面(_消息: 文本类型):
    return 页面.错误页面(_消息)


async def 渲染游戏首页():
    return await 渲染页面("首页")
