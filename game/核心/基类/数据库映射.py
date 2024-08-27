from abc import ABC

from bson.objectid import ObjectId
from game.核心.基础数据类型 import 文本类型, 字典类型, 整数类型, 空, 是或否
from game.核心.基础方法 import 校验数据类型
from game.核心.基类.元类 import 固定属性元类
from game.核心.工具方法.数据库 import 数据库操作类


class 数据库字段:
    pass


class 数据库映射类(数据库操作类, metaclass=固定属性元类):
    # 唯一ID
    id: str | None = None
    _表名: 文本类型
    # 查询出来的原始数据
    _数据: 字典类型

    _需要的属性 = ["_表名"]

    def __init__(self, _数据: 字典类型 | 空 = 空):
        super().__init__(self._表名)
        if _数据 is not 空:
            self._数据 = _数据
            self.解析数据(_数据)

    def 解析数据(self, _数据: 字典类型):
        self._数据 = _数据
        _类型注释 = self.__annotations__
        for _键, _值 in _数据.键值对():
            if _键 in _类型注释.keys():
                self.__dict__[_键] = _值
        self.id = str(_数据.get("_id"))

    @classmethod
    def 需要保存的字段(cls):
        _当前类的注释 = cls.__annotations__
        _排除的父类 = (数据库映射类, ABC)
        for _父类 in cls.__bases__:
            if type(_父类) not in _排除的父类:
                continue
            _当前类的注释.update(_父类.__annotations__)
        _当前类的注释.pop("id")
        return _当前类的注释.keys()

    @property
    def oid(self) -> ObjectId | None:
        if self.id:
            return ObjectId(self.id)

    async def 保存(self):
        _需要保存的字段 = self.需要保存的字段()
        _要保存的数据字典 = {}
        for _字段 in _需要保存的字段:
            _要保存的数据字典[_字段] = self.__dict__.get(_字段)
        if self.id:
            await self.更新一条数据({"_id": self.oid}, _要保存的数据字典)
        else:
            await self.添加一条数据(_要保存的数据字典)

    @classmethod
    async def 获取(cls, _条件: 文本类型 | 字典类型):

        if 校验数据类型(_条件, 文本类型):
            _查询条件 = {"_id": ObjectId(_条件)}
        else:
            _查询条件 = _条件
        _对象 = cls()
        _数据 = await _对象.查询一条数据(_查询条件)
        if not _数据:
            return None
        _对象.解析数据(_数据)
        return _对象
