from game.核心.基础属性 import 基础类
from game.核心.基础数据类 import 列表
from game.核心.基础数据类型 import 文本类型, 列表类型
from game.核心.基类.元类 import 固定属性元类


class 区域基类(基础类, metaclass=固定属性元类):
    区域名称: 文本类型
    区域介绍: 文本类型
    区域图标: 文本类型

    # 区域所拥有的地图
    地图: 列表[文本类型]
