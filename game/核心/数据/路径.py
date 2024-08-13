import os
from config.path_conf import BASE_DIR

游戏文件夹 = os.path.join(BASE_DIR, "game")
游戏公共模板文件夹 = os.path.join(BASE_DIR, "game/核心/页面模板")
游戏数据文件夹 = os.path.join(游戏文件夹, "数据")
游戏页面文件夹 = os.path.join(游戏文件夹, "页面")

__all__ = [
    "游戏文件夹",
    "游戏数据文件夹",
    "游戏页面文件夹",
    "游戏公共模板文件夹",
    "BASE_DIR",
]
