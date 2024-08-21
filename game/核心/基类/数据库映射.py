from bson.objectid import ObjectId
from game.核心.基础数据类型 import 文本类型, 字典类型, 整数类型, 空, 是或否
from game.核心.基础方法 import 校验数据类型
from game.核心.基类.元类 import 固定属性元类
from game.核心.工具方法.数据库 import 数据库操作类


class 数据库字段:
    pass


class 数据库映射类(数据库操作类, metaclass=固定属性元类):
    # 唯一ID
    id: str
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

    async def 保存(self):
        pass

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
