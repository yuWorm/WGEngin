from game.核心.基础数据类型 import 文本类型, 列表类型, 字典类型, 是, 是或否
from game.核心.页面.html5 import 标签表, 无需闭合标签, 资源类型表
from game.核心.页面.工具 import (
    解析样式,
    解析标签参数,
    转义HTML文本,
    转义特殊标签,
    JS脚本关闭标签,
    CSS样式关闭标签,
    HTML文本,
)


class 页面构建类:
    名称: 文本类型
    _页面内容: 列表类型
    _结尾标签: 文本类型
    _标签栈: 列表类型

    def __init__(self, _名称: 文本类型, _是否初始化为网页=是):
        self.名称 = _名称
        self._初始化页面设置()

    def _初始化页面设置(self):
        self._页面内容 = []
        self._模板 = {}
        self._结尾标签 = ""
        self._标签栈 = []

    def _关闭标签(self):
        if self._结尾标签:
            self._页面内容.append(self._结尾标签)
            self._结尾标签 = ""

    @property
    def _页面内容元组(self):
        _页面内容列表 = []
        _页面内容列表.extend(self._页面内容)
        _页面内容列表.append(self._结尾标签)
        _页面内容列表.extend(self._标签栈[::-1])
        return tuple(_页面内容列表)

    def __getattr__(self, name: str):
        # 防止unitest debug的时候出现的许多shape标签
        if name == "shape":
            raise Exception("异常数据")

        if name[0] == "_":
            return self.__getattr__(name)

        # 模板都是以_结尾
        if name.startswith("模板_"):
            # 以__结尾的模板会将添加到页面当中
            _是否添加到页面中 = name.endswith("_")
            if _是否添加到页面中:
                name = name[:-1]

            _模板: 页面构建类 = self._模板.get(name)
            if not _模板:
                if not _是否添加到页面中:
                    raise AttributeError(
                        "请在第一次使用模板的时候以__结尾,不然无法正确创建模板"
                    )
                _模板 = self._模板[name] = 页面构建类(name)

            if _是否添加到页面中:
                self._页面内容.append(_模板)
                return self
            else:
                return _模板

        _标签名 = 标签表.get(name, name)
        self._关闭标签()
        self._页面内容.append(f"<{_标签名}>")
        if _标签名 not in 无需闭合标签:
            self._结尾标签 = f"</{_标签名}>"
        return self

    def __setattr__(self, name: str, value):
        if not name.startswith("模板_"):
            return object.__setattr__(self, name, value)

        _模板: 页面构建类 = self._模板.get(name)
        if _模板:
            _模板._初始化页面设置()
            _模板(value)

    def __call__(self, *_内容, 样式: 字典类型 = None, **_参数):

        if self._页面内容 and isinstance(self._页面内容[-1], 页面构建类):
            if _参数:
                raise AttributeError("无法为模板站位符号添加参数")
            self._页面内容[-1](*_内容)
            return self

        if 样式 or _参数:
            _标签 = self._页面内容[-1]
            if _标签[0] == "<" and _标签[-1] == ">" and not _标签.startswith("</"):
                _样式字符串 = ""
                if 样式:
                    _样式字符串 = 解析样式(样式)

                _参数字符串 = ""
                if _参数:
                    _参数字符串 = 解析标签参数(_参数)

                if _样式字符串:
                    _参数字符串 += f' style="{_样式字符串}"'

                if _参数字符串:
                    self._页面内容[-1] = f"{_标签[:-1]} {_参数字符串} >"
        if _内容:
            self._(*_内容)
            self._关闭标签()
        return self

    def _(self, *_内容列表):
        for _内容 in _内容列表:

            if _内容 is None:
                continue

            # 如果传入的为本身,直接跳过
            if _内容 is self:
                continue

            if type(_内容) is 页面构建类:
                if _内容.名称 in self._模板:
                    self._页面内容.append(_内容)
                else:
                    self._模板.update(_内容._模板)
                    self._页面内容.extend(_内容._页面内容)
            else:
                self._页面内容.append(
                    str(
                        _内容.__html__()
                        if hasattr(_内容, "__html__")
                        else 转义HTML文本(_内容)
                    )
                )
        return self

    def __str__(self):
        return "".join(str(_标签) for _标签 in self._页面内容元组)

    def 渲染(self):
        return str(self)

    def __enter__(self):
        assert self._结尾标签, "with 用法智能用于可以闭合的标签"
        self._标签栈.append(self._结尾标签)
        self._结尾标签 = ""
        return self

    def __exit__(self, w, t, f):
        self._关闭标签()
        self._页面内容.append(self._标签栈.pop())

    def _添加注释(self, _内容):
        """
        添加注释内容
        :param _内容:
        :return:
        """
        _注释内容 = str(_内容).replace("-->", "‒‒>")
        self._页面内容.append(f"<!--{_内容}-->")
        return self

    def _添加JS(self, _代码: str, **attrs):
        """
        添加js脚本
        :param code:
        :param attrs:
        :return:
        """
        self._关闭标签()
        _代码 = 转义特殊标签(JS脚本关闭标签, _代码)
        self._pieces.append(f"<script{解析标签参数(attrs)}>{_代码}</script>")
        return self

    def _添加样式(self, _代码: str, **attrs):
        """

        :param code:
        :param attrs:
        :return:
        """
        self._关闭标签()
        _代码 = 转义特殊标签(CSS样式关闭标签, _代码)
        self._pieces.append(f"<style{解析标签参数(attrs)}>{_代码}</style>")
        return self


def 创建页面(
    标题: 文本类型,
    资源列表: list[文本类型] = None,
    自适应窗口: 是或否 = 是,
    **_html参数,
):
    if 资源列表 is None:
        资源列表 = []

    _页面 = 页面构建类(标题)(HTML文本("<!DOCTYPE html>"))

    if _html参数:
        _页面.html(**_html参数)
    else:
        _页面.html()

    if 标题:
        _页面.标题(标题)

    if 自适应窗口:
        _页面.meta(name="viewport", content="width=device-width, initial-scale=1")

    for _资源 in 资源列表:
        _文件 = _资源.rsplit("/", 1)[-1]
        _文件后缀 = _资源.rsplit(".", 1)[-1]
        _资源参数 = 资源类型表.get(_文件) or 资源类型表.get(_文件后缀)
        if _资源参数:
            _页面.引入资源(链接地址=_资源, **_资源参数)
        elif _资源.endswith("js"):
            _页面.JS脚本(None, 资源=_资源, defer=True)
        elif _资源.endswith("mjs"):
            _页面.JS脚本(None, 资源=_资源, 类型="module")
        else:
            raise ValueError("不支持的资源类型")

    # 添加header模板
    _页面.模板_页头_()
    return _页面
