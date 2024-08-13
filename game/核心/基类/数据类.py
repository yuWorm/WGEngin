from typing import Any, Callable


from game.核心.基础异常 import 类参数异常, 类型检测异常
from game.核心.基础方法 import 校验数据类型


class 基础数据结构:
    def __init__(self, **kwargs):
        self.校验参数(kwargs)

    # 校验参数
    def 校验参数(self, kwargs: dict[str, Any]):
        # 校验值是否存在
        for _属性名, _属性类型 in self.__annotations__.items():
            if _属性名 not in kwargs:
                if _属性名 in self.__dict__.keys():
                    continue
                raise 类参数异常(f"{self.__class__.__name__}的{_属性名}为必填项")

            _属性值 = kwargs.get("_属性名")
            # 校验数据类型是否符合
            if not 校验数据类型(_属性值, _属性类型):
                raise 类型检测异常(
                    f"{self.__class__.__name__}的{_属性名}的值必须为f{_属性类型}"
                )

            # 调用校验方法，前提是有
            _校验方法名 = f"校验_{_属性名}"
            if not hasattr(self, _校验方法名):
                continue

            _校验方法 = getattr(self, _校验方法名)
            _校验结果 = _校验方法(_属性值)
            if _校验结果 is True:
                raise 类型检测异常(
                    f"{self.__class__.__name__}的{_属性名}值输入有误，{_校验结果}"
                )
