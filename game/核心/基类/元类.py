from abc import ABCMeta

from game.核心.基础异常 import 类参数异常
from game.核心.基础数据类型 import 任意值
from game.核心.基础方法 import 校验数据类型


class 固定属性元类(ABCMeta):
    """
    主要用于去固定属性，来限制子类的结构。
    """

    def __new__(cls, name, bases, attrs: dict[str, 任意值]):
        _需要的属性 = attrs.get("__需要的属性", [])
        cls.验证属性(_需要的属性, attrs, name)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def 验证属性(_需要的属性, attrs: dict[str, 任意值], name: str):
        __类型 = attrs.get("__annotations__", {})

        for __属性名 in _需要的属性:
            # 判断必填属性是否存在
            if __属性名 not in attrs:
                raise 类参数异常(f"{name}类的{__属性名}为必填项")

            __属性值 = attrs.get(__属性名)
            __属性类型 = __类型.get(__属性名)
            if not 校验数据类型(__属性值, __属性类型):
                raise 类参数异常(f"{name}类的{__属性名}的值类型必须为{__属性类型}")
