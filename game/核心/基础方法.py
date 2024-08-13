from typeguard import TypeCheckError, check_type

from game.核心.基础数据类型 import 任意值, 否, 是, 是或否


def 校验数据类型(_值: 任意值, _类型: 任意值) -> 是或否:
    """
    检查值是否是这个类型的数据
    :param _值: 要检查的值
    :param _类型: 值属于的类型
    :return: 是否属于这个 _类型
    """
    try:
        check_type(_值, _类型)
        return 是
    except TypeCheckError as te:
        return 否
