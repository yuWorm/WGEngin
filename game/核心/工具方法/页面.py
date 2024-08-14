from typing import Type
import urllib.parse
from sanic import redirect

from common.aes import aes_encrypt, aes_decrypt
from common.context import r
from game.核心.基础数据类 import 字典, 文本
from game.核心.基础数据类型 import 文本类型, 字典类型, 空
from game.核心.基类.游戏.页面 import 页面基类
from game.核心.工具方法 import 时间


class 跳转页面标志(Exception):
    _页面: Type[页面基类] | 文本类型
    _页面参数: 字典类型

    def __init__(self, _页面: Type[页面基类] | 文本类型, _页面参数: 字典类型):
        self._页面 = _页面
        self._页面参数 = _页面

    def 页面路径(self):
        _页面 = 文本(self._页面)
        if _页面.是否开头为("/"):
            return self._页面

        return 获取页面路径(self._页面, self._页面参数)


def 添加页面消息(_内容: 文本类型, _分类: 文本类型 = "消息"):
    """
    添加页面消息
    :param _内容: 消息内容
    :param _分类: 消息类别
    :return:
    """
    _flashes = r.ctx.session.get("_flashes", [])
    _flashes.append((_分类, _内容))
    r.ctx.session["_flashes"] = _flashes


def 回到首页():
    重定向页面("/")


def 重定向页面(_页面路径: 文本类型):
    return redirect(_页面路径)


def 加密页面路径数据(_数据: 字典类型) -> 文本类型:
    """
    对需要传入到页面的数据进行加密
    :param _数据:
    :return:
    """
    _数据文本 = urllib.parse.urlencode(_数据, quote_via=urllib.parse.quote)
    _加密后文本 = aes_encrypt(_数据文本)
    return _加密后文本


def 解密页面路径数据(_加密数据: 文本类型) -> 字典类型:
    _数据文本 = aes_decrypt(_加密数据)
    _数据 = urllib.parse.parse_qs(_数据文本)
    _整理好的数据 = 字典({})
    for k, v in _数据.items():
        if len(v) > 1:
            _整理好的数据[k] = v
        else:
            _整理好的数据[k] = v[0]

    return _整理好的数据


def 获取页面路径(_页面: 文本类型 | Type[页面基类], _页面数据: 字典类型 = 空):
    """
    返回加密的页面路径
    :param _页面: 页面名称或者页面类
    :param _页面数据: 需要传递给页面的数据
    :return:
    """
    if not _页面数据:
        _页面数据 = {}

    _页面名称 = _页面 if type(_页面) is str or type(_页面) is 文本 else _页面.页面名称()
    _页面数据组装 = 字典({"p": _页面名称, "t": 时间.当前时间_单位秒()})
    _页面数据组装.更新(_页面数据)
    _加密后的数据 = 加密页面路径数据(_页面数据组装)

    return f"/game?p={_加密后的数据}"


def 错误页面(_错误信息):
    from game.页面.页面配置 import 异常页面

    添加页面消息(_错误信息, "异常")
    _页面路径 = 获取页面路径(异常页面, {})
    return 重定向页面(_页面路径)


def 跳转到错误页面(_错误信息, _页面参数: 字典类型 = 空):
    from game.页面.页面配置 import 异常页面

    if _页面参数 is 空:
        _页面参数 = {}

    添加页面消息(_错误信息, "异常")
    raise 跳转页面标志(异常页面, _页面参数)


def 跳转页面(_页面: Type[页面基类] | 文本类型, _页面参数=空):
    if _页面参数 is 空:
        _页面参数 = {}
    raise 跳转页面标志(_页面, _页面参数)


def 返回游戏页面路径():
    pass


def 返回游戏首页地址():
    return "/"
