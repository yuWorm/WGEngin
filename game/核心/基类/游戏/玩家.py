from abc import ABC
from typing import TypeVar

from game.核心.基础数据类 import 列表
from game.核心.基础数据类型 import 文本类型, 整数类型, 小数类型, 字典类型, 是或否
from game.核心.基类.元类 import 固定属性元类
from game.核心.基类.数据库映射 import 数据库映射类
from game.核心.工具方法.数据库 import 数据库工具
from game.核心.数据模板 import 技能

T = TypeVar("T")

_字段映射表 = {}


class 玩家属性元类(ABC, metaclass=固定属性元类):
    pass


class 玩家资源类:
    pass


class 玩家类(ABC, 数据库映射类, metaclass=固定属性元类):
    """
    玩家基类, 属性命名规则, 所有不需要保存到数据库中的数据都不需要使用_开头, 需要保存的数据不可以用_开头, 并且必须指定类型注释
    """

    _表名 = "玩家表"

    用户ID: 文本类型
    昵称: 文本类型
    头像: 文本类型
    职业: 文本类型
    血量: 小数类型
    蓝量: 小数类型
    等级: 整数类型
    经验值: 整数类型
    属性: 整数类型
    称号: 列表[文本类型]
    装备: 字典类型
    技能: 字典类型
    任务: 字典类型
    宠物: 字典类型
    好友: 字典类型
    组织: 文本类型
    所在地点: 文本类型
    是否在副本: 是或否

    # 这里定义拓展属性即可

    # 控制加载元类
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def __init__(self, **kwargs):
        super().__init__()

    @classmethod
    async def 设置数据库(cls):
        await 数据库工具[cls._表名].设置索引({"邮箱": 1}, {"unique": True})

    async def 加载玩家数据(self, _玩家ID):
        pass

    async def 从缓存中加载玩家数据(self):
        pass

    async def 攻击力(self):
        pass

    async def 添加物品(self):
        pass

    async def 使用物品(self):
        pass

    async def 装备物品(self):
        pass

    async def 进入地图(self):
        pass

    async def 添加任务(self):
        pass

    async def 学习技能(self):
        pass

    async def 添加宠物(self):
        pass

    async def 保存(self):
        pass

    @classmethod
    async def 创建玩家(cls, _玩家昵称: 文本类型, _玩家性别: 文本类型):
        """
        床架一个玩家
        :param _玩家昵称:
        :param _玩家性别:
        :return:
        """
