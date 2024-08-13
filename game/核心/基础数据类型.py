from typing import NewType, Any, Type
from game.核心.基础数据类 import 文本, 字典, 整数, 元组, 小数, 列表

空 = None
无 = None
是 = True
否 = False
是或否 = bool
任意值 = NewType("任意值", Any)
文本类型 = str | 文本
整数类型 = int | 整数
小数类型 = float | 小数
列表类型 = 列表 | list
字典类型 = 字典 | dict
元组类型 = 元组 | tuple
二进制数据 = bytes
