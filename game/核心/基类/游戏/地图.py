from game.核心.基础属性 import 基础类
from game.核心.基础数据类 import 列表
from game.核心.基础数据类型 import 文本类型, 字典类型, 列表类型
from game.核心.基类.元类 import 固定属性元类


class 地图基类(基础类, metaclass=固定属性元类):
    区域: 文本类型
    地图名称: 文本类型
    地图介绍: 文本类型
    地图图标: 文本类型

    # 地图所拥有的npc
    NPC: 列表[文本类型] = []
    # 地图所拥有的资源
    资源: 列表[文本类型] = []
    # 地图所拥有的怪物
    怪物: 列表[文本类型] = []

    @classmethod
    def 四周(cls) -> 字典类型:
        """
        地图四周有哪些地图
        :return:
        """
        return {}

    def 进入事件(self):
        """
        进入地图会触发的事件
        :return:
        """
        pass

    def 离开事件(self):
        """
        离开地图会触发的事件
        :return:
        """
        pass
