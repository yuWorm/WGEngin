from abc import ABCMeta, ABC

from game.核心.基础异常 import 类参数异常
from game.核心.基础数据类型 import 任意值, 否
from game.核心.基础方法 import 校验数据类型


class 固定属性元类(ABCMeta):
    """
    主要用于去固定属性，来限制子类的结构。
    """

    def __new__(cls, name, bases, attrs: dict[str, 任意值]):
        for base in bases:
            if base.__name__.endswith("基类"):
                _需要的属性 = base.需要的属性
                cls.验证属性(_需要的属性, base, attrs, name)
                break
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def 验证属性(_需要的属性, base, attrs: dict[str, 任意值], name: str):
        _类型 = base.__annotations__

        for _属性名 in _需要的属性:
            # 判断必填属性是否存在
            if _属性名 not in attrs:
                raise 类参数异常(f"{name}类的{_属性名}为必填项")

            _属性值 = attrs.get(_属性名)
            _属性类型 = _类型.get(_属性名)
            if not 校验数据类型(_属性值, _属性类型):
                raise 类参数异常(f"{name}类的{_属性名}的值类型必须为{_属性类型}")
