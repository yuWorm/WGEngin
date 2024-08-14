from typing import Any, Callable

from game.核心.基础异常 import 类参数异常, 类型检测异常
from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import (
    字典类型,
    整数类型,
    文本类型,
    小数类型,
    列表类型,
    元组类型,
    二进制数据,
)
from game.核心.基础方法 import 校验数据类型

_类型名称映射字典 = {
    字典类型: "字典类型",
    整数类型: "整数",
    文本类型: "文本",
    小数类型: "小数",
    列表类型: "字典类型",
    元组类型: "字典类型",
    二进制数据: "二进制数据",
}


def _类型名称映射(_类型):
    if _类型 in _类型名称映射字典:
        return _类型名称映射字典[_类型]
    return _类型


class 基础数据结构:
    def __init__(self, **kwargs):
        _需要的参数 = self.校验参数(kwargs)
        self.绑定参数(_需要的参数)

    # 校验参数
    def 校验参数(self, kwargs: dict[str, Any]):
        _需要的参数 = 字典({})

        # 校验值是否存在
        for _属性名, _属性类型 in self.__annotations__.items():
            if _属性名 not in kwargs:
                if _属性名 in self.__dict__.keys():
                    continue
                raise 类参数异常(f"{self.__class__.__name__}的{_属性名}为必填项")

            _属性值 = kwargs.get(_属性名)
            # 校验数据类型是否符合
            if not 校验数据类型(_属性值, _属性类型):
                raise 类型检测异常(
                    f"{self.__class__.__name__}的{_属性名}的值必须为{_类型名称映射(_属性类型)}"
                )

            # 调用校验方法，前提是有
            _校验方法名 = f"校验_{_属性名}"
            if hasattr(self, _校验方法名):
                _校验方法 = getattr(self, _校验方法名)
                _校验结果 = _校验方法(_属性值)
                if _校验结果 is not True:
                    raise 类型检测异常(
                        f"{self.__class__.__name__}的{_属性名}值输入有误，{_校验结果}"
                    )

            _需要的参数[_属性名] = _属性值

        return _需要的参数

    def 绑定参数(self, _参数: 字典类型):
        for _名称, _值 in _参数.键值对():
            self.__setattr__(_名称, _值)
