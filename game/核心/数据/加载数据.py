"""
这个文件用来加载游戏数据数据
"""

import importlib
import os
import pkgutil

from common.log import logger
from game.核心.基础数据类型 import 任意值, 文本类型
from game.核心.数据.路径 import 游戏页面文件夹, 游戏数据文件夹, BASE_DIR


def 从文件夹加载数据(_模块路径: str):
    for _文件根目录, _路径下面的目录, _路径下面的文件 in os.walk(_模块路径):
        for _文件 in _路径下面的文件:
            if _文件.endswith(".py") and _文件 != "__init__.py":
                _模块路径 = os.path.join(_文件根目录, _文件)
                _模块名称 = os.path.relpath(_模块路径, BASE_DIR)[:-3].replace(
                    os.sep, "."
                )
                # 导入模块
                importlib.import_module(_模块名称)


def 加载所有数据():
    从文件夹加载数据(游戏页面文件夹)
