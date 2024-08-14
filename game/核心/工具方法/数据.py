import re

from game.核心.基础数据类型 import 文本类型


def 判断是否为纯文本或数字(_需要判断的文本: 文本类型):
    _正则 = re.compile(r"[^a-zA-Z0-9]")
    if _正则.search(_需要判断的文本):
        return False

    return True
