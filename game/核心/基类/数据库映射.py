from typing import Generic, TypeVar

from game.核心.基础数据类 import 列表, 字典
from game.核心.基础数据类型 import 文本类型, 字典类型, 整数类型, 空
from game.核心.基类.元类 import 固定属性元类
from game.核心.工具方法.数据库 import 数据库工具, 数据库操作类

T = TypeVar("T")


class 数据库字段(Generic[T]):
    def __new__(cls, *args, **kwargs) -> T:
        return T()


class 数据库映射类(数据库操作类, metaclass=固定属性元类):
    # 唯一ID
    _id: str
    _表名: 文本类型

    _需要的属性 = ["_表名"]

    def __init__(self):
        super().__init__(self._表名)

    def 解析数据(self):
        pass
