import time
from abc import ABC, abstractmethod
from typing import Any, Type

from sanic import text

from common.context import r, g
from config.setting import settings
from sanic.response import HTTPResponse

from game import 游戏配置
from game.核心.基础异常 import 类型检测异常
from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import 空, 文本类型, 否, 字典类型, 是或否, 列表类型, 是

from game.核心.基类.元类 import 固定属性元类
from game.核心.基类.数据类 import 基础数据结构
from game.核心.工具方法 import 文件
from game.核心.工具方法.时间 import 当前时间_单位秒

from game.核心.数据.路径 import 游戏页面文件夹
from game.核心.页面.构建 import 页面构建类
from game.游戏配置 import 游戏名称, 游戏副标题, 游戏介绍


class 页面参数基类(基础数据结构):
    pass


class 页面基类(ABC, metaclass=固定属性元类):
    页面组: 文本类型

    需要的属性 = ["页面组"]

    页面参数类: Type[页面参数基类] = None
    页面参数: 页面参数基类

    # 这个是页面的通过加密链接传入的参数, 用于构建返回上一页之类的
    _页面参数 = {}
    无输出页面: 是或否 = 否
    游戏名称 = 游戏配置.游戏名称
    游戏副标题 = 游戏配置.游戏副标题
    游戏介绍 = 游戏配置.游戏介绍

    def __init__(self):
        # self.加载页面模板()
        pass

    @classmethod
    def 页面名称(cls):
        return cls.__name__

    @classmethod
    def 页面模板路径(cls):
        return 文件.拼接文件路径(
            游戏页面文件夹, cls.页面组, "模板", f"{cls.__name__}.html"
        )

    def 页面返回请求头(self) -> 字典类型 | 空:
        return 空

    @abstractmethod
    async def 内容(self) -> 页面构建类 | None:
        pass

    async def 渲染页面(self):
        from game.核心.工具方法.页面 import 获取页面资源

        _页面内容 = await self.内容()

        if not _页面内容:
            return text("")

        # 加入最基础的css和js
        _页面内容.模板_页头.引入资源(
            链接地址=获取页面资源("css/base.css"), rel="stylesheet", 类型="text/css"
        )
        _页面内容.模板_页头.JS脚本(资源=获取页面资源("js/clock.js"), defer=True)

        if settings.DEBUG:
            _页面内容.段落(f"{round(time.time() * 1000 - g.start_time * 1000, 2)}毫秒")

        _请求头 = self.页面返回请求头()
        return HTTPResponse(
            str(_页面内容),
            status=200,
            headers=_请求头,
            content_type="text/html; charset=utf-8",
        )

    @classmethod
    async def 基础页面数据(cls) -> 字典类型:
        _数据 = 字典(
            {
                "游戏名称": 游戏名称,
                "游戏副标题": 游戏副标题,
                "游戏介绍": 游戏介绍,
                "页面消息": cls.获取页面消息,
                "是否登录": g.是否登录,
                "isDev": settings.DEBUG,
            }
        )

        if g.是否登录:
            _数据["用户"] = {"用户名": g.用户.用户名, "用户ID": g.用户.id}

        if settings.DEBUG:
            _数据["round"] = round
            _数据["g"] = g
            _数据["end_time"] = 当前时间_单位秒
        return _数据

    async def 页面数据(self) -> 字典类型:
        """
        用于渲染页面数据
        :return:
        """
        pass

    async def 加载数据(self, _页面参数: 字典类型, _请求参数: 字典类型):
        """
        调用加载数据
        :return:
        """
        self._页面参数 = _页面参数
        _请求参数.update(_页面参数)
        self.解析页面参数(字典(_请求参数))

    @classmethod
    def 获取页面消息(
        cls, _是否输出类别: 是或否 = 否, _需要的消息类别: 列表类型 | 空 = 空
    ):
        """
        获取页面消息
        :param _是否输出类别: 是否在返回消息的时候带上分类,默认不带
        :param _需要的消息类别: 需要哪些类型的消息,为一个列表,可以多个列表,默认为空,空则输出所有消息
        :return:
        """
        _消息 = r.ctx.session.pop("_flashes", [])
        if _需要的消息类别:
            _消息 = list(filter(lambda f: f[0] in _需要的消息类别, _消息))

        if not _是否输出类别:
            return [x[1] for x in _消息]

        return _消息

    @classmethod
    def 添加消息(cls, _内容, _分类="消息"):
        from game.核心.工具方法.页面 import 添加页面消息

        """
        添加页面消息
        :param _内容: 消息的内容
        :param _分类: 消息否分类
        :return:
        """
        添加页面消息(_内容, _分类)

    def 解析页面参数(self, _参数: 字典类型):
        from game.核心.工具方法.页面 import 跳转到错误页面, 获取页面路径

        if self.页面参数类:
            try:
                self.页面参数 = self.页面参数类(**_参数)
            except 类型检测异常 as e:
                _返回上一页 = 获取页面路径(self.__class__, self._页面参数)
                跳转到错误页面(str(e), {"back": _返回上一页})

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
