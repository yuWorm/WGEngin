from game.核心.基础属性 import 基础异常
from game.核心.基础数据类型 import 文本类型


class 文件异常(基础异常):
    pass


class 文件不存在(文件异常):
    pass


class 页面模板不存在(文件异常):
    _模板名称: 文本类型

    def __init__(self, _模板名称):
        self._模板名称 = _模板名称

    def __str__(self):
        return f"{self._模板名称}模板不存在"


class 类参数异常(Exception):
    pass


class 类型检测异常(Exception):
    pass


class 页面异常(Exception):
    msg: str

    def __init__(self, _内容):
        self.msg = _内容

    def __str__(self):
        return self.msg
