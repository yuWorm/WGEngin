from typing import List

from database.mongo import client
import motor.motor_asyncio as async_motor
from game.核心.基础数据类 import 列表, 字典
from game.核心.基础数据类型 import 文本类型, 字典类型, 整数类型, 空, 任意值

数据库连接: async_motor.AsyncIOMotorClient | 任意值 = None


class 数据库操作类:
    表名: 文本类型

    def __init__(self, 表名: 文本类型):
        global 数据库连接
        self.表名 = 表名
        if 数据库连接 is None:
            数据库连接 = client.get_client()

    async def 插入一条数据(self, _数据: 字典类型):
        return await 数据库连接[self.表名].insert_one(_数据)

    async def 插入多条数据(self, _多条数据: 列表[字典类型]):
        return await 数据库连接[self.表名].insert_many(_多条数据)

    async def 查询一个文档(self, _查询条件: 字典类型) -> 字典:
        _查询结果 = await 数据库连接[self.表名].find_one(_查询条件)
        return 字典(_查询结果)

    async def 查询多个文档(
        self, _查询条件: 字典类型, _需要的数量: 整数类型
    ) -> 列表[字典]:
        _查询缓存 = 数据库连接[self.表名].find(_查询条件)
        _查询结果 = await _查询缓存.to_list(length=_需要的数量)

        return 列表([字典(_结果) for _结果 in _查询结果])

    async def 获取表数据数量(self, _查询条件: 字典类型 | 空 = 空) -> 整数类型:
        if _查询条件 is 空:
            _查询条件 = {}

        return await 数据库连接[self.表名].count_documents(_查询条件)

    async def 更新一条数据(
        self, _判断条件: 字典类型, _更新的数据: 字典类型
    ) -> 整数类型:
        _更新结果 = await 数据库连接[self.表名].update_one(_判断条件, _更新的数据)
        return _更新结果.modified_count

    async def 更新多条数据(
        self, _判断条件: 字典类型, _更新的数据: 字典类型
    ) -> 整数类型:
        _更新结果 = await 数据库连接[self.表名].update_many(_判断条件, _更新的数据)
        return _更新结果.modified_count

    async def 删除数据(self, _判断条件: 字典类型) -> 整数类型:
        _删除结果 = await 数据库连接[self.表名].delete_many(_判断条件)
        return _删除结果

    async def 设置索引(self, _信息: 字典类型):
        pass


class 数据库工具类:
    _data: dict = {}

    def __getattr__(self, name: str) -> 数据库操作类:

        if name in self._data.keys():
            return self._data[name]

        _操作 = 数据库操作类(name)
        self._data[name] = _操作
        return _操作

    def __getitem__(self, name: str):
        return self.__getattr__(name)


数据库工具 = 数据库工具类()
