from typing import Type

from game.核心.基类.游戏.页面 import 页面基类

技能表 = {}
怪物表 = {}
NPC表 = {}
地图表 = {}
页面表: dict[str, Type[页面基类]] = {}
事件表 = {}
副本表 = {}
副本地图表 = {}
装备表 = {}
物品表 = {}
区域表 = {}
