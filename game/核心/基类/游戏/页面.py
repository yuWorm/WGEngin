import time
from abc import ABC, abstractmethod
from typing import Any, Type

from common.context import g, r
from config.setting import settings
from sanic.response import HTTPResponse
from jinja2 import Template, Environment, FileSystemLoader
from game.核心.基础异常 import 页面模板不存在
from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import 空, 文本类型, 否, 字典类型, 是或否, 列表类型
from game.核心.基类.元类 import 固定属性元类
from game.核心.基类.数据类 import 基础数据结构
from game.核心.工具方法 import 文件
from game.核心.工具方法.时间 import 当前时间_单位秒

from game.核心.数据.路径 import 游戏页面文件夹, 游戏公共模板文件夹
from game.游戏配置 import 游戏名称, 游戏副标题, 游戏介绍

模板加载器 = FileSystemLoader(
    searchpath=[游戏公共模板文件夹, 文件.拼接文件路径(游戏页面文件夹, "_模板")]
)
env = Environment(loader=模板加载器)


def _从文件中加载页面模板(_页面模板路径, _页面名称):
    if 文件.文件是否存在(_页面模板路径) is 否:
        raise 页面模板不存在(_页面名称)

    with 文件.打开文件(_页面模板路径, "只读") as f:
        _模板源码 = f.读取所有()
        _编译后的模板 = env.compile(_模板源码)
        return Template.from_code(env, _编译后的模板, {"页面名称": _页面名称})


class 页面参数基类(基础数据结构):
    pass


class 页面基类(ABC, metaclass=固定属性元类):
    页面模板: Template = 空
    页面组: 文本类型
    页面参数: Type[页面参数基类]

    参数: 页面参数基类

    # 用于将当前页面模板注入的全局的模板路径当中
    是否注入全局模版路径: 是或否 = 否

    __需要的属性 = ["页面组", "页面参数"]

    def __new__(cls, *args, **kwargs):
        if cls.是否注入全局模版路径:
            _当前页面组模板文件夹 = 文件.获取文件所处文件夹(cls.页面模板路径())
            if 文件.文件是否存在(_当前页面组模板文件夹):
                模板加载器.searchpath.append(_当前页面组模板文件夹)
                模板加载器.load()

        return super().__new__(cls)

    def __init__(self, _页面参数):
        self.加载页面模板()
        # self.解析页面参数(_页面参数)

    @classmethod
    def 页面名称(cls):
        return cls.__name__

    @classmethod
    def 页面模板路径(cls):
        return 文件.拼接文件路径(
            游戏页面文件夹, cls.页面组, "模板", f"{cls.__name__}.html"
        )

    @classmethod
    def 加载页面模板(cls):
        # debug 默认每次都加载，这样修改了模板内容才会及时显示
        if settings.DEBUG:
            cls.页面模板 = _从文件中加载页面模板(cls.页面模板路径(), cls.__name__)
            return

        if cls.页面模板 is 空:
            cls.页面模板 = _从文件中加载页面模板(cls.页面模板路径(), cls.__name__)

    def 页面返回请求头(self) -> 字典类型 | 空:
        return 空

    async def 渲染页面(self):
        _基础数据 = await self.基础页面数据()
        _页面数据 = await self.页面数据()
        _基础数据.更新(_页面数据)
        _渲染结果 = self.页面模板.render(**_基础数据)
        _请求头 = self.页面返回请求头()
        return HTTPResponse(
            _渲染结果,
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
                "isDev": settings.DEBUG,
            }
        )

        if settings.DEBUG:
            _数据["round"] = round
            _数据["g"] = g
            _数据["end_time"] = 当前时间_单位秒
        return _数据

    @abstractmethod
    async def 页面数据(self) -> 字典类型:
        pass

    async def 加载数据(self):
        pass

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
        self.参数 = self.页面参数(**_参数)
