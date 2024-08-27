import re
from game.核心.基础数据类型 import 字典类型, 文本类型
from game.核心.页面.html5 import 样式表, 参数表, 参数值表, 样式值表, 无需转换的属性值


class HTML文本(str):
    """
    注意,html文本是不会被转义的,直接输入的文本内容是会被转义的
    """

    __html__ = _repr_html_ = str.__str__

    def __repr__(self):
        return f"HTML({super().__repr__()})"


def 解析标签参数(_参数: 字典类型):
    _参数字符串 = []
    for _名, _值 in _参数.items():
        _参数名 = 参数表.get(_名, _名)
        if type(_值) is bool and _值 is True:
            _参数字符串.append(f"{_参数名}")
            continue
        if not (_参数名 in 无需转换的属性值):
            _值 = 参数值表.get(_值, _值)

        _参数字符串.append(f'{_参数名}="{_值}"')
    return " ".join(_参数字符串)


def 解析样式(_样式: 字典类型) -> 文本类型:
    _样式字符串 = []
    for _名, _值 in _样式.items():
        _样式名 = 样式表.get(_名, _名)
        _样式值 = 样式值表.get(_值, _值)
        _样式字符串.append(f"{_样式名}: {_样式值}")

    return ";".join(_样式字符串)


def 转义HTML文本(_文本):
    return HTML文本(str(_文本).replace("&", "&amp;").replace("<", "&lt;"))


# Inline styles and scripts only escape the specific end tag
CSS样式关闭标签 = re.compile("</(style>)", re.IGNORECASE)
JS脚本关闭标签 = re.compile("</(script>)", re.IGNORECASE)


def 转义特殊标签(_标签: re, _内容):
    return HTML文本(_标签.sub(r"<\\/\1", _内容))
