import time
from datetime import datetime


def 当前时间_单位秒():
    """
    返回的是从 Unix 纪元（通常是 1970 年 1 月 1 日 00:00:00 UTC）开始到当前时间的秒数。
    :return:
    """
    return time.time()


def 当前时间():
    """
    返回当前的日期时间,并格式化为年-月-日 时:分:秒
    :return:
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
